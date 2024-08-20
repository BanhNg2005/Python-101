import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments!")
# sys.argv[1:] is a list of all the command line arguments
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
# output: hello, my name is <name>
# sys.argv[1] is the first command line argument
# sys.argv[0] is the name of the script itself