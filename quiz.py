QUESTIONS = [
    {
        "id": 1,
        "question": "What is phishing?",
        "options": [
            "A type of firewall",
            "A social engineering attack",
            "A programming language",
            "A cloud service"
        ],
        "answer": "A social engineering attack"
    },
    {
        "id": 2,
        "question": "Which password is generally stronger?",
        "options": [
            "123456",
            "password123",
            "A long, unique random password",
            "admin2026"
        ],
        "answer": "A long, unique random password"
    },
    {
        "id": 3,
        "question": "What does MFA stand for?",
        "options": [
            "Multi-Factor Authentication",
            "Multiple File Access",
            "Main Firewall Application",
            "Managed File Authentication"
        ],
        "answer": "Multi-Factor Authentication"
    },
    {
        "id": 4,
        "question": "What should you do with a suspicious email?",
        "options": [
            "Click every link",
            "Download attachments",
            "Report it through the appropriate channel",
            "Reply with your password"
        ],
        "answer": "Report it through the appropriate channel"
    },
    {
        "id": 5,
        "question": "What does HTTPS provide?",
        "options": [
            "Guaranteed website safety",
            "Encrypted communication with the website",
            "Automatic virus removal",
            "Free cloud storage"
        ],
        "answer": "Encrypted communication with the website"
    },
    {
        "id": 6,
        "question": "What is ransomware?",
        "options": [
            "A backup tool",
            "Malware that can encrypt files and demand payment",
            "A secure password manager",
            "A networking protocol"
        ],
        "answer": "Malware that can encrypt files and demand payment"
    },
    {
        "id": 7,
        "question": "What is the principle of least privilege?",
        "options": [
            "Give everyone admin access",
            "Disable all accounts",
            "Grant only the access necessary",
            "Share passwords with coworkers"
        ],
        "answer": "Grant only the access necessary"
    },
    {
        "id": 8,
        "question": "What is a recommended way to handle software updates?",
        "options": [
            "Ignore security patches",
            "Install updates from trusted sources",
            "Disable automatic security updates",
            "Download updates from unknown websites"
        ],
        "answer": "Install updates from trusted sources"
    },
    {
        "id": 9,
        "question": "What is social engineering?",
        "options": [
            "Manipulating people to reveal information or take actions",
            "Designing network cables",
            "Encrypting a hard drive",
            "Creating cloud servers"
        ],
        "answer": "Manipulating people to reveal information or take actions"
    },
    {
        "id": 10,
        "question": "What should you do if you suspect an account compromise?",
        "options": [
            "Ignore the warning",
            "Share your password",
            "Follow the organization's incident reporting process",
            "Disable security notifications"
        ],
        "answer": "Follow the organization's incident reporting process"
    }
]


def calculate_score(user_answers):

    if not isinstance(user_answers, dict):
        raise TypeError("Answers must be a dictionary")

    correct = 0

    for question in QUESTIONS:

        question_id = question["id"]

        if user_answers.get(question_id) == question["answer"]:
            correct += 1

    total = len(QUESTIONS)

    percentage = round((correct / total) * 100, 2)

    if percentage >= 80:
        awareness_level = "ADVANCED"

    elif percentage >= 50:
        awareness_level = "INTERMEDIATE"

    else:
        awareness_level = "BEGINNER"

    return {
        "correct_answers": correct,
        "total_questions": total,
        "percentage": percentage,
        "awareness_level": awareness_level
    }


if __name__ == "__main__":

    sample_answers = {
        question["id"]: question["answer"]
        for question in QUESTIONS
    }

    result = calculate_score(sample_answers)

    print("CYBERSECURITY AWARENESS QUIZ")
    print("----------------------------")
    print("Correct Answers:", result["correct_answers"])
    print("Total Questions:", result["total_questions"])
    print("Score:", result["percentage"], "%")
    print("Awareness Level:", result["awareness_level"])