def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # return True if n % 2 == 0 else False
    return n % 2 == 0
    
main()

