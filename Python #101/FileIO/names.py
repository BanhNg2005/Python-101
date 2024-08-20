# name = input("What's your name?")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.strip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"hello, {name}")