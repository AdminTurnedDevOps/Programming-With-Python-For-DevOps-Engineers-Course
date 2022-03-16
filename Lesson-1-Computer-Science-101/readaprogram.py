# Import a library, which allows us to interact with
# certain functions, variables, classes, and more
import os

# Create a global variable, outside of the function
# variables created inside of a function are "local variables"
run_command = os


# Create a function, which is a a set of instructions to be carried out
def run_a_command():
    # The below command can also be `os.system()`
    # Run the command to echo 'Hello michaellevan'
    run_command.system("echo Hello michaellevan")


# Run the command
run_a_command()