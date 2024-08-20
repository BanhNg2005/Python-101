import re

url = input("URL: ").strip()

# Adjusted regular expression to capture the username as the second group
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print("Username:", matches.group(1))
