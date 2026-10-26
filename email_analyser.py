import re


SUSPICIOUS_PHRASES = {
    "verify your account": 20,
    "account suspended": 25,
    "urgent action": 15,
    "click here": 10,
    "confirm your password": 30,
    "unusual activity": 15,
    "limited time": 10,
    "update your payment": 25,
    "security alert": 10,
    "reset your password": 15,
}

PRESSURE_PHRASES = [
    "immediately",
    "within 24 hours",
    "final warning",
    "act now",
    "avoid suspension",
]


def analyze_email(email_text):

    if not isinstance(email_text, str):
        raise TypeError("Email content must be text")

    text = email_text.strip()

    if not text:
        return {
            "risk_score": 0,
            "risk_level": "INVALID",
            "findings": ["Email content is empty"]
        }

    text_lower = text.lower()

    score = 0
    findings = []

    # Detect suspicious phrases
    for phrase, points in SUSPICIOUS_PHRASES.items():

        if phrase in text_lower:
            score += points
            findings.append(
                f"Suspicious phrase detected: {phrase}"
            )

    # Detect pressure or urgency language
    for phrase in PRESSURE_PHRASES:

        if phrase in text_lower:
            score += 10
            findings.append(
                f"Urgency language detected: {phrase}"
            )

    # Detect requests for sensitive information
    sensitive_patterns = [
        r"\b(send|share|provide)\s+(your\s+)?password\b",
        r"\b(send|share|provide)\s+(your\s+)?otp\b",
        r"\b(send|share|provide)\s+(your\s+)?pin\b",
    ]

    for pattern in sensitive_patterns:

        if re.search(pattern, text_lower):
            score += 30
            findings.append(
                "Possible request for sensitive information"
            )
            break

    # Detect links
    links = re.findall(
        r"https?://[^\s<>\"']+",
        text,
        flags=re.IGNORECASE
    )

    if links:
        findings.append(
            f"Email contains {len(links)} URL(s)"
        )

        # Links are not automatically malicious
        score += min(len(links) * 5, 15)

    # Detect excessive exclamation marks
    if text.count("!") >= 4:
        score += 10
        findings.append(
            "Excessive exclamation marks detected"
        )

    score = min(score, 100)

    if score >= 60:
        risk_level = "HIGH"

    elif score >= 30:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    if not findings:
        findings.append(
            "No selected suspicious indicators detected"
        )

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "findings": findings,
        "links_found": links
    }


if __name__ == "__main__":

    sample_email = """
    URGENT ACTION REQUIRED!

    Your account suspended.
    Verify your account immediately.

    Click here:
    https://example.com/verify

    Confirm your password within 24 hours!
    """

    result = analyze_email(sample_email)

    print("Risk Score:", result["risk_score"])
    print("Risk Level:", result["risk_level"])

    for finding in result["findings"]:
        print("-", finding)