import random
import sys

def guessing_number():
    number = random.randint(1, 100)
    print("Day la 1 day so ngau nhien tu 1 den 100")
    print("Hay thu doan so do trong 10 luot choi")
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        guess = int(input("Nhap so: "))
        attempts += 1
        if guess < number:
            print("So ban doan nho hon so can tim")
        elif guess > number:
            print("So ban doan to hon so can tim")
        else:
            print(f"Cung kinh day, mat co {attempts} luot da tim ra so {number} roi :D")
            break
    else:
        print(f"Sozi nha. So chinh xac la {number}")


if __name__ == "__main__":
    guessing_number()
    sys.exit(0)