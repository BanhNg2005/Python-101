import re

name = input("What's your name: ").strip()


if matches := re.search(r"^(.+), *(.+)$", name): 
    # := is the walrus operator which means that the value of the expression is assigned to the variable
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}!")