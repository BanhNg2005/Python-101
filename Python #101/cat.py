# i = 0
# while i < 3:
#    print("meow")
#    i += 1

# print("meow\n" * 3, end="")

# for i in range(5):
#    print("meow")

# while True:
#    n = int(input("What is n? "))
#    if n > 0:
#        break

# for _ in range(n):
#    print("meow")

def main():
    number = getNum()
    meow(number)

def getNum():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n
def meow(n):
    for _ in range(n):
        print("meow")

main()