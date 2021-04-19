# Use the OS and sys library
import os
import sys

# Define a function that uses the `os` library
def echo_name(name):
    # Use the `system()` method from the `os` library
    print_name = os.system("echo Hello, " + name)
    print(print_name)
    

# Use the `sys` library to pass in a value at runtime
name = sys.argv[1]

echo_name(name)