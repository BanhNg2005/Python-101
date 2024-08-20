import re

email = input("Enter your email address: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|gov|com)$", email, re.IGNORECASE):
# (\w+\.)? means that the group \w+ followed by a dot is optional
# [a-zA-Z0-9_\.]
    print("Valid email")
else:
    print("Invalid email")