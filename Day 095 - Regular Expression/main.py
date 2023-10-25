import re

text = "Hello, my email is example@email.com, and my phone number is 123-456-7890."

# Search for an email address
email_pattern = r'\w+@\w+\.\w+'
email_match = re.search(email_pattern, text)
if email_match:
    print("Email found:", email_match.group())

# Search for phone numbers
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(phone_pattern, text)
print("Phone numbers found:", phone_numbers)
