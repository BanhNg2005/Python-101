def main():
    print_column(3)

def print_column(height):
    # print("#\n" * height, end="") => better way
    for _ in range(height):
        print("#")

main()