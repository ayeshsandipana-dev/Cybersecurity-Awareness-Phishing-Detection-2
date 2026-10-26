import re
import ipaddress
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "verify",
    "urgent",
    "account",
    "suspended",
    "confirm",
    "password",
    "login",
    "update",
    "secure"
]


def analyze_url(url):

    score = 0
    findings = []

    url = url.strip()

    if not url:
        return {
            "url": url,
            "risk_score": 0,
            "risk_level": "INVALID",
            "findings": ["URL is empty"]
        }

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)

    hostname = parsed.hostname or ""

    if not hostname:
        return {
            "url": url,
            "risk_score": 0,
            "risk_level": "INVALID",
            "findings": ["Invalid hostname"]
        }

    # Check HTTP
    if parsed.scheme == "http":
        score += 20
        findings.append("URL does not use HTTPS")

    # Check URL length
    if len(url) > 75:
        score += 15
        findings.append("Unusually long URL")

    # Check IP address as hostname
    try:
        ipaddress.ip_address(hostname)
        score += 25
        findings.append("IP address used instead of domain")
    except ValueError:
        pass

    # Check suspicious keywords
    matched_keywords = [
        keyword
        for keyword in SUSPICIOUS_KEYWORDS
        if keyword in url.lower()
    ]

    if matched_keywords:
        score += min(len(matched_keywords) * 5, 20)

        findings.append(
            "Keywords detected: " +
            ", ".join(matched_keywords)
        )

    # Check excessive subdomains
    if hostname.count(".") >= 3:
        score += 15
        findings.append("Multiple subdomains detected")

    # Check @ symbol
    if "@" in parsed.netloc:
        score += 25
        findings.append("URL contains @ symbol")

    # Check hyphens
    if hostname.count("-") >= 3:
        score += 10
        findings.append("Multiple hyphens in hostname")

    score = min(score, 100)

    if score >= 60:
        risk_level = "HIGH"
    elif score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    if not findings:
        findings.append("No selected suspicious patterns detected")

    return {
        "url": url,
        "risk_score": score,
        "risk_level": risk_level,
        "findings": findings
    }


if __name__ == "__main__":

    test_urls = [
        "https://example.com",
        "http://192.0.2.10/login/verify-account",
        "https://secure-login-update.example.com"
    ]

    for url in test_urls:

        result = analyze_url(url)

        print("\nURL:", result["url"])
        print("Risk Score:", result["risk_score"])
        print("Risk Level:", result["risk_level"])
        print("Findings:", result["findings"])