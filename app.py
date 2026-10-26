import streamlit as st
import pandas as pd
import plotly.express as px

from phishing_detector import analyze_url
from email_analyser import analyze_email
from password_checker import check_password_strength
from quiz import QUESTIONS, calculate_score
from database import (
    initialize_database,
    save_quiz_result,
    get_quiz_history,
)

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Cybersecurity Awareness Platform",
    page_icon="🛡️",
    layout="wide"
)

initialize_database()

# -----------------------------------
# CUSTOM STYLE
# -----------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #00D4FF;
}

div[data-testid="stMetric"] {
    background-color: #1C2333;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #30363D;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("🛡️ Cybersecurity SOC")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "URL Analyzer",
        "Email Analyzer",
        "Password Checker",
        "Awareness Quiz",
        "Quiz History",
        "Reports"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Educational Security Platform")


# -----------------------------------
# HELPER FUNCTIONS
# -----------------------------------

def show_risk(result):

    score = result["risk_score"]
    level = result["risk_level"]

    st.metric("Risk Score", f"{score}/100")

    if level == "HIGH":
        st.error("🔴 HIGH RISK")

    elif level == "MEDIUM":
        st.warning("🟠 MEDIUM RISK")

    elif level == "LOW":
        st.success("🟢 LOW RISK")

    else:
        st.info("Invalid input")

    st.subheader("Analysis Findings")

    for finding in result["findings"]:
        st.write(f"• {finding}")


def load_history():

    rows = get_quiz_history()

    columns = [
        "ID",
        "Username",
        "Score",
        "Correct Answers",
        "Total Questions",
        "Awareness Level",
        "Completed At"
    ]

    return pd.DataFrame(rows, columns=columns)


# -----------------------------------
# OVERVIEW
# -----------------------------------

if page == "Overview":

    st.title("🛡️ Cybersecurity Awareness Platform")

    st.write(
        "Phishing Detection, Password Security "
        "and Cybersecurity Awareness Training"
    )

    history = load_history()

    total_quizzes = len(history)

    average_score = (
        history["Score"].mean()
        if not history.empty
        else 0
    )

    advanced_users = (
        (history["Awareness Level"] == "ADVANCED").sum()
        if not history.empty
        else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Completed Quizzes",
        total_quizzes
    )

    col2.metric(
        "Average Quiz Score",
        f"{average_score:.1f}%"
    )

    col3.metric(
        "Advanced Results",
        advanced_users
    )

    st.divider()

    st.subheader("🔐 Security Modules")

    st.info("🔗 URL Phishing Analyzer")
    st.info("📧 Email Phishing Analyzer")
    st.info("🔐 Password Strength Checker")
    st.info("🧠 Cybersecurity Awareness Quiz")

    st.caption(
        "Analysis results are heuristic indicators, "
        "not proof that content is malicious or safe."
    )


# -----------------------------------
# URL ANALYZER
# -----------------------------------

elif page == "URL Analyzer":

    st.title("🔗 Phishing URL Analyzer")

    st.write(
        "Analyze URL patterns for potential "
        "phishing indicators."
    )

    url = st.text_input(
        "Enter URL",
        placeholder="https://example.com"
    )

    if st.button("Analyze URL"):

        if not url.strip():
            st.warning("Please enter a URL.")

        else:
            result = analyze_url(url)

            show_risk(result)

            st.caption(
                "This tool does not visit the URL. "
                "A low score does not guarantee safety."
            )


# -----------------------------------
# EMAIL ANALYZER
# -----------------------------------

elif page == "Email Analyzer":

    st.title("📧 Phishing Email Analyzer")

    st.write(
        "Check email text for suspicious phrases, "
        "urgency and requests for sensitive data."
    )

    email_text = st.text_area(
        "Paste Email Content",
        height=220,
        placeholder="Paste sample email text here..."
    )

    if st.button("Analyze Email"):

        if not email_text.strip():
            st.warning("Please enter email content.")

        else:
            result = analyze_email(email_text)

            show_risk(result)

            if result["links_found"]:

                st.subheader("Detected Links")

                # Display as plain text, not clickable links.
                for link in result["links_found"]:
                    st.code(link, language=None)

            st.caption(
                "Avoid pasting real emails containing "
                "passwords, OTPs or private information."
            )


# -----------------------------------
# PASSWORD CHECKER
# -----------------------------------

elif page == "Password Checker":

    st.title("🔐 Password Strength Checker")

    st.write(
        "Estimate password strength using "
        "length, character types and common patterns."
    )

    password = st.text_input(
        "Enter a TEST password",
        type="password"
    )

    if st.button("Check Strength"):

        result = check_password_strength(password)

        st.metric(
            "Password Score",
            f"{result['score']}/100"
        )

        st.progress(result["score"] / 100)

        if result["strength"] == "STRONG":
            st.success("🟢 STRONG")

        elif result["strength"] == "MEDIUM":
            st.warning("🟠 MEDIUM")

        elif result["strength"] == "WEAK":
            st.error("🔴 WEAK")

        else:
            st.info("Enter a password.")

        for feedback in result["feedback"]:
            st.write(f"• {feedback}")

    st.caption(
        "Use invented test passwords only. "
        "This demo does not store passwords. "
        "The score is not a guarantee of security."
    )


# -----------------------------------
# AWARENESS QUIZ
# -----------------------------------

elif page == "Awareness Quiz":

    st.title("🧠 Cybersecurity Awareness Quiz")

    st.write(
        f"Answer all {len(QUESTIONS)} questions."
    )

    with st.form("quiz_form"):

        username = st.text_input(
            "Enter Display Name",
            max_chars=50
        )

        user_answers = {}

        for question in QUESTIONS:

            st.markdown(
                f"### Question {question['id']}"
            )

            st.write(question["question"])

            options = [
                "Select an answer"
            ] + question["options"]

            answer = st.selectbox(
                "Choose your answer",
                options,
                key=f"question_{question['id']}"
            )

            if answer != "Select an answer":
                user_answers[question["id"]] = answer

        submitted = st.form_submit_button(
            "Submit Quiz"
        )

    if submitted:

        if not username.strip():
            st.error("Please enter a display name.")

        elif len(user_answers) != len(QUESTIONS):
            st.warning(
                "Please answer all questions."
            )

        else:

            result = calculate_score(user_answers)

            save_quiz_result(
                username,
                result
            )

            st.success("Quiz Completed!")

            st.metric(
                "Final Score",
                f"{result['percentage']}%"
            )

            st.write(
                "Correct Answers:",
                result["correct_answers"]
            )

            st.write(
                "Awareness Level:",
                result["awareness_level"]
            )

            st.progress(
                result["percentage"] / 100
            )

            st.info(
                "Your result has been saved "
                "to the SQLite database."
            )


# -----------------------------------
# QUIZ HISTORY
# -----------------------------------

elif page == "Quiz History":

    st.title("📊 Quiz History")

    history = load_history()

    if history.empty:

        st.info(
            "No quiz results available yet."
        )

    else:

        st.dataframe(
            history,
            use_container_width=True
        )

        st.subheader(
            "Awareness Level Distribution"
        )

        counts = (
            history["Awareness Level"]
            .value_counts()
            .reset_index()
        )

        counts.columns = [
            "Awareness Level",
            "Count"
        ]

        fig = px.bar(
            counts,
            x="Awareness Level",
            y="Count",
            title="Cybersecurity Awareness Results"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# -----------------------------------
# REPORTS
# -----------------------------------

elif page == "Reports":

    st.title("📥 Security Awareness Reports")

    history = load_history()

    if history.empty:

        st.warning(
            "Complete a quiz to generate a report."
        )

    else:

        csv_data = history.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="Download Quiz History CSV",
            data=csv_data,
            file_name="awareness_quiz_report.csv",
            mime="text/csv"
        )

        st.success(
            "Report is ready for download."
        )


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Cybersecurity Awareness & Phishing "
    "Detection Platform | Educational Project"
)