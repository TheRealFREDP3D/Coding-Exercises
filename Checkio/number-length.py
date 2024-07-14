import os
import sys

def generate_comment(command):
    if command == "hello":
        return "Hello! How can I assist you today?"
    elif command == "help":
        return "Here are some commands you can use: hello, help, exit."
    elif command == "exit":
        sys.exit("Exiting the terminal.")
    else:
        return f"Command '{command}' not recognized. Type 'help' for a list of available commands."

def main():
    while True:
        # Read input from the user (terminal)
        command = input(">>> ").strip()
        
        if command:
            comment = generate_comment(command)
            print(f"Comment: {comment}")

if __name__ == "__main__":
    main()
