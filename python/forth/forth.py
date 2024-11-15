class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""
    def __init__(self, message="Insufficient number of items in stack"):
        super().__init__(message)


def _is_number(command):
    """Check if the command is a number."""
    return command.lstrip("-").isdigit()


def _process_number(command, stack):
    """Push a number onto the stack."""
    stack.append(int(command))


def _handle_user_defined_word(input_data, user_defined_words, i):
    """
    Process a user-defined word definition.

    :param input_data: List of commands
    :param user_defined_words: Dictionary to store user-defined words
    :param i: Current command index
    :return: Updated command index
    """
    i += 1
    if i >= len(input_data):
        raise ValueError("Invalid word name in definition")

    word_name = input_data[i]
    if _is_number(word_name):
        raise ValueError("illegal operation")  # Numbers cannot be word names

    word_name = word_name.upper()

    # Collect the definition until ';' is encountered
    i += 1
    definition = []
    while i < len(input_data) and input_data[i] != ";":
        definition.append(input_data[i])
        i += 1

    if i == len(input_data):
        raise ValueError("Missing ';' in word definition")

    # Store the definition
    user_defined_words[word_name] = definition
    return i


def _execute_user_defined_word(command, user_defined_words, stack):
    """
    Execute a user-defined word.

    :param command: The user-defined word to execute
    :param user_defined_words: Dictionary of user-defined words
    :param stack: The current stack
    """
    word_name = command.upper()
    definition = user_defined_words[word_name]

    # Process each command in the definition
    for cmd in definition:
        if _is_number(cmd):
            _process_number(cmd, stack)
        elif cmd.upper() in user_defined_words:
            _execute_user_defined_word(cmd, user_defined_words, stack)
        elif cmd.upper() in {"+", "-", "*", "/", "DUP", "DROP", "SWAP", "OVER"}:
            _perform_operation(cmd, stack)
        else:
            raise ValueError("undefined operation")


def _perform_operation(command, stack):
    """Perform a built-in operation on the stack."""
    command = command.upper()
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
            raise ZeroDivisionError("divide by zero")
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


def evaluate(input_data):
    """
    Interpret a list of strings as Forth commands and return the stack as integers.

    Supports basic arithmetic operations, stack manipulation, and defining new words.

    :param input_data: List of strings (commands or numbers)
    :return: List of integers representing the stack after execution
    """
    stack = []
    user_defined_words = {}
    input_data = " ".join(input_data).split()
    i = 0

    while i < len(input_data):
        command = input_data[i]

        if _is_number(command):
            _process_number(command, stack)
        elif command == ":":
            i = _handle_user_defined_word(input_data, user_defined_words, i)
        elif command.upper() in user_defined_words:
            _execute_user_defined_word(command, user_defined_words, stack)
        elif command.upper() in {"+", "-", "*", "/", "DUP", "DROP", "SWAP", "OVER"}:
            _perform_operation(command, stack)
        else:
            raise ValueError("undefined operation")

        i += 1

    return stack
