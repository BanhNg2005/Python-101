def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in a row
        for j in range(size):
            # print brick
            print("#", end="")
        print()

# alternative way

# def print_square(size):
#     for i in rage(size)
#          print_row(size)

# def print_row(width)
#   print("# * width)
main()