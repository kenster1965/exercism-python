"""
Evaluator for a very simple subset of Forth.
"""

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""
    def __init__(self, message="Insufficient number of items in stack"):
        super().__init__(message)



def evaluate(input_data):
    """
    Interpret a list of strings as Forth commands and return the stack as integers.

    Supports basic arithmetic operations, stack manipulation, and defining new words.

    :param input_data: List of strings (commands or numbers)
    :return: List of integers representing the stack after execution
    """
    stack = []
    user_defined_words = {}  # Dictionary to store user-defined words
    i = 0  # Command pointer for processing the input_data list

    while i < len(input_data):
        command = input_data[i]

        if command.isdigit():  # If it's a number, push it onto the stack
            stack.append(int(command))

        elif command == ':':  # Begin a new word definition
            i += 1
            if i >= len(input_data) or not input_data[i].isalpha():
                raise ValueError("Invalid word name in definition")

            word_name = input_data[i]
            if word_name.isdigit() or word_name in {"+", "-", "*", "/", "DUP", "DROP", "SWAP", "OVER"}:
                raise ValueError("Invalid word name: Cannot redefine reserved words or use a number")

            # Collect the definition until ';' is encountered
            i += 1
            definition = []
            while i < len(input_data) and input_data[i] != ';':
                definition.append(input_data[i])
                i += 1

            if i == len(input_data):
                raise ValueError("Missing ';' in word definition")

            # Store the word definition
            user_defined_words[word_name] = definition

        elif command in user_defined_words:  # Execute a user-defined word
            # Insert the user-defined word's definition into the command list
            input_data = input_data[:i] + user_defined_words[command] + input_data[i + 1:]
            continue  # Continue to process the inserted commands

        elif command in {"+", "-", "*", "/", "DUP", "DROP", "SWAP", "OVER"}:
            # Built-in operations handled here
            if command == '+':
                if len(stack) < 2:
                    raise StackUnderflowError()
                stack.append(stack.pop() + stack.pop())

            elif command == '-':
                if len(stack) < 2:
                    raise StackUnderflowError()
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)

            elif command == '*':
                if len(stack) < 2:
                    raise StackUnderflowError()
                stack.append(stack.pop() * stack.pop())

            elif command == '/':
                if len(stack) < 2:
                    raise StackUnderflowError()
                b, a = stack.pop(), stack.pop()
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(a // b)

            elif command == 'DUP':
                if not stack:
                    raise StackUnderflowError()
                stack.append(stack[-1])

            elif command == 'DROP':
                if not stack:
                    raise StackUnderflowError()
                stack.pop()

            elif command == 'SWAP':
                if len(stack) < 2:
                    raise StackUnderflowError()
                stack[-1], stack[-2] = stack[-2], stack[-1]

            elif command == 'OVER':
                if len(stack) < 2:
                    raise StackUnderflowError()
                stack.append(stack[-2])

        else:
            raise ValueError("undefined operation")

        i += 1  # Move to the next command

    return stack
