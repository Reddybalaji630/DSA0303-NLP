import re

# Sample text
text = "My email is student123@gmail.com and my phone number is 9876543210."

# 1. Search for an email address
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.search(email_pattern, text)

if email:
    print("Email found:", email.group())
else:
    print("Email not found.")

# 2. Search for a 10-digit phone number
phone_pattern = r'\b\d{10}\b'
phone = re.search(phone_pattern, text)

if phone:
    print("Phone number found:", phone.group())
else:
    print("Phone number not found.")

# 3. Find all words starting with 's'
words = re.findall(r'\bs\w*', text, re.IGNORECASE)
print("Words starting with 's':", words)

