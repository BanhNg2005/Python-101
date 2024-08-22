import re

def main():
    code = input("Hexadecimal color code: ").strip()
    pattern = r"^#[0-9a-fA-F]{6}$"
    if match := re.search(pattern, code):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")

main()