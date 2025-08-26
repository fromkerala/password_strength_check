import re

def password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length to at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r'[@#$%]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (@, #, $, %).")

    percentage = int((score / 5) * 100)

    return score, percentage, feedback

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    score, percentage, feedback = password_strength(pwd)
    print(f"Score: {score}/5 ({percentage}%)")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password is strong!")