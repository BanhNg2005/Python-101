import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, my name is " + sys.argv[1])