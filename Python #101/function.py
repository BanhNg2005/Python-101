"""
def hello(to):
    print("hello,", to)

name = input("Enter your name: ")
hello(name)
"""
# print the even numbers from 1 to 10
def roundNum():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in num:
        if i % 2 == 0:
            print(i)

roundNum()

# print the star pattern pyramid
def starPattern():
    n = 5
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

starPattern()