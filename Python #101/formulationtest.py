#1 print hello
print('Hello World')

print('-----------')
#2 sum of 2 number
print('Sum of 2 numbers')
a: int = int(input('Enter the first number: '))
b: int = int(input('Enter the second number number: '))
print(f'The sum of 2 numbers is {a+b}')

print('-----------')
#3 print the output based on the formula
print('print the output based on the formula: (num1 * (num2-num3)) / num4')
num1: int = int(input('Enter the first number: '))
num2: int = int(input('Enter the second number: '))
num3: int = int(input('Enter the third number: '))
num4: int = int(input('Enter the fourth number: '))
print(f'The output of the formula is: {(num1 * (num2-num3)) / num4}')

print('-----------')
#4 Given a proper description for user's age
print('“Child” for under 12s')
print('“Youth” for ages 12 and under and under 18')
print('“Adult” for 18 and under and under 60')
print('“Senior” for those 60 and over')
age: int = int(input('Enter your age: '))
if 0 > age < 12:
    print('Child')
elif 12 > age < 18:
    print('Youth')
elif 18 >= age < 60:
    print('Adult')
else:
    print('Senior')

print('-----------')
#5 Check whether the triangle exists or not
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

print('5. Check whether the triangle exists or not')
a: int = int(input('Enter the length first side: '))
b: int = int(input('Enter the length second side: '))
c: int = int(input('Enter the length third side: '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('The triangle exists')
else:
    print('The triangle doesn\'t exist')

print('-----------')
#6 returns a count of 1 to the number entered.

print('6. Returns a count of 1 to the number entered.')
while True:
    try:
        count: int = int(input('Enter a positive number: '))
        if count > 0:
            count += 1
            break
        else:
            print('Enter a positive number only.')
    except ValueError:
        print('Enter an integer number only.')

print(f'The return of a count of 1 to the number you entered is: {count}')

print('-----------')
#7 Receives a positive integer value representing the number of lines and returns the following output.
print('7. Receives a positive integer value representing the number of lines and returns the following output.')
lines: int = int(input('Enter the number of lines: '))
for i in range(1, lines+1):
    print('*' * i)

print('-----------')
#8 factorial number
print('8. Factorial number')

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        factorials: int = int(input('Enter a positive number: '))
        if factorials >= 0:
            print(f'The factorial of {factorials} is {factorial(factorials)}')
            break
        else:
            print('Enter number that is greater or equal to 0 only')
    except ValueError:
        print('Enter number only')

print('-----------')
#9 returns whether number is in the array or not
print('9. returns whether number is in the array or not')
def isContain(arr: list, num: int) -> bool:
    return num in arr

arr: list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
num: int = int(input('Enter a number: '))
print(isContain(arr, num))

print('-----------')
#10 receives a 4-digit (from ‘a’ to ‘z’) password from the user and finds it using brute force
print('10. receives a 4-digit (from \'a\' to \'z\') password from the user and finds it using brute force')
import string
import re

def bruteForce(password: str) -> str:
    characters = string.ascii_lowercase + string.ascii_uppercase
    for w in characters:
        for x in characters:
            for y in characters:
                for z in characters:
                    if w + x + y + z == password:
                        return w + x + y + z

def main() -> None:
    while True:
        password: str = input('Enter a 4-character password: ')
        if re.match(r'[a-zA-Z]{4}', password):
            print(f'The password is: {bruteForce(password)}')
            break
        else:
            print('Enter a 4 character password only (letters only).')

if __name__ == '__main__':
    main()

print('-----------')
#11 Create a list of students and calculate the average of their grades
print('11. Create a list of students and calculate the average of their grades')

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name: str, age: int, midterm: int, project: int, final: int) -> None:
        super().__init__(name, age)
        self.midterm = midterm
        self.project = project
        self.final = final
    
    def average(self) -> float:
        return (self.midterm + self.project + self.final) / 3

def main() -> None:
    students = []
    while True: 
        try:
            name: str = input('Enter the student name: ')
            if name.isalpha() and name != '':
                break
            else:
                print('Please enter the name in alphabetic characters only.')
        except ValueError:
            print('Enter a name only.')
        
    while True:
        try:
            age: int = int(input('Enter the student age: '))
            if age > 0:
                break
            else:
                print('Please enter a positive number only.')
        except ValueError:
            print('Enter a number only.')
    
    while True:
        try:
            midterm: int = int(input('Enter the midterm grade: '))
            if 0 <= midterm <= 100:
                break
            else:
                print('Please enter a number between 0 and 100 only.')
        except ValueError:
            print('Enter a number only.')

    while True:
        try:
            project: int = int(input('Enter the project grade: '))
            if 0 <= project <= 100:
                break
            else:
                print('Please enter a number between 0 and 100 only.')
        except ValueError:
            print('Enter a number only.')

    while True:
        try:
            final: int = int(input('Enter the final grade: '))
            if 0 <= final <= 100:
                break
            else:
                print('Please enter a number between 0 and 100 only.')
        except ValueError:
            print('Enter a number only.')   
    while True:
        students.append(Student(name, age, midterm, project, final))
        choice = input('Do you want to add another student? (y/n): ')
        if choice.lower() == 'n':
            break
    
    total = 0
    for student in students:
        total += student.average()
        print(f'{student.name}, Age: {student.age}, Average Grade: {student.average():.2f}')

if __name__ == '__main__':
    main()