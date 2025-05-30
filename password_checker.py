import re  # 🔹 're' module को import किया है - इससे हम Regular Expressions use कर सकते हैं (text pattern matching के लिए)

# 🔹 Function define कर रहे हैं जो password की strength चेक करेगा
def check_password_strength(password):
    score = 0  # 🔹 Score variable: हम इसमें 0 से शुरुआत करते हैं, और strong points add करते हैं
    suggestions = []  # 🔹 Suggestions की एक खाली list बनाते हैं, ताकि हम कमजोर password को सुधारने की tips दे सकें

    # 🔹 Check करते हैं कि password कम से कम 8 characters का है या नहीं
    if len(password) >= 8:
        score += 1  # अगर हाँ, तो score 1 बढ़ा दो
    else:
        suggestions.append("🔹 Use at least 8 characters")  # अगर नहीं, तो ये suggestion add करो

    # 🔹 Check for UPPERCASE letters (A-Z)
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("🔹 Add uppercase letters")  # अगर uppercase नहीं है तो सुझाव दो

    # 🔹 Check for lowercase letters (a-z)
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🔹 Add lowercase letters")

    # 🔹 Check for numbers (0-9)
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("🔹 Include numbers")

    # 🔹 Check for special characters (!, @, #, $, etc.)
    if re.search(r"[\W_]", password):
        score += 1
    else:
        suggestions.append("🔹 Include special characters (!, @, #, etc.)")

    # 🔹 अब हम score के हिसाब से strength decide करेंगे (dictionary बनाकर)
    strength = {
        5: "Strong ✅",
        4: "Good 👍",
        3: "Moderate ⚠️",
        2: "Weak ❌",
        1: "Very Weak ❌",
        0: "Extremely Weak ❌"
    }

    # 🔹 Output print करो - Password कितना strong है
    print(f"\nPassword Strength: {strength[score]}")

    # 🔹 अगर suggestions दिए गए हैं, तो उन्हें print करो
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(s)  # हर suggestion को एक-एक करके print करो

# 🔹 User से password input लो
user_input = input("Enter your password to check: ")

# 🔹 Function को call करो और user का password check करवाओ
check_password_strength(user_input)