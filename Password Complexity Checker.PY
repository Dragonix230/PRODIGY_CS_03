import re
import math

# Function to calculate password entropy
def calculate_entropy(password):
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26  # lowercase letters
    if re.search(r'[A-Z]', password):
        charset_size += 26  # uppercase letters
    if re.search(r'\d', password):
        charset_size += 10  # numbers
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32  # special characters
    if re.search(r'\s', password):
        charset_size += 1  # space

    # Entropy formula: log2(charset_size^password_length)
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    return round(entropy, 2)

# Function to check the strength of a password
def check_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Scoring system
    score = 0
    if length_criteria:
        score += 2
    if uppercase_criteria:
        score += 2
    if lowercase_criteria:
        score += 2
    if number_criteria:
        score += 2
    if special_char_criteria:
        score += 2

    # Calculate entropy
    entropy = calculate_entropy(password)
    
    # Strength bar visualization
    strength_bar = "[" + "#" * score + "-" * (10 - score) + "]"
    
    # Strength feedback based on score
    feedback = []
    if score <= 4:
        feedback.append("Password is weak.")
        feedback.append("Consider adding more characters and mixing uppercase, lowercase, numbers, and symbols.")
    elif 5 <= score <= 7:
        feedback.append("Password is moderate.")
        feedback.append("You could strengthen it by adding special characters or increasing length.")
    else:
        feedback.append("Password is strong!")
    
    # Detailed feedback on missing criteria
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    return score, strength_bar, entropy, feedback

# Example usage
password = input("Enter your password: ")
score, strength_bar, entropy, feedback = check_password_strength(password)

print(f"\nPassword strength score: {score}/10")
print(f"Strength bar: {strength_bar}")
print(f"Entropy: {entropy} bits")

for f in feedback:
    print(f"- {f}")
