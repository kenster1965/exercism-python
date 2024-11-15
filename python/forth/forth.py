"""
Evaluator for Forth Stach program.
"""


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
    Save user defined word.

    :param input_data: List of commands
    :param user_defined_words: Dictionary to store user-defined words
    :param i: Current command index
    :return: Updated index (i)
    """
    i += 1

    word_name = input_data[i]
    if _is_number(word_name):
        # names can not be numbers
        raise ValueError("illegal operation")

    word_name = word_name.upper()

    # Loop to the ;
    i += 1
    definition = []
    while i < len(input_data) and input_data[i] != ";":
        command = input_data[i].upper()
        if command in user_defined_words:
            definition.append((command, list(user_defined_words[command])))
        else:
            definition.append((command, None))
        i += 1

    user_defined_words[word_name] = definition
    return i


def _execute_user_defined_word(command, user_defined_words, stack):
    """
    Execute a user-defined word.

    :param command: The user word to execute
    :param user_defined_words: Dictionary of user-defined words
    :param stack: The current stack
    """
    word_name = command.upper()
    definition = user_defined_words[word_name]

    for cmd, snapshot in definition:
        if _is_number(cmd):
            _process_number(cmd, stack)
        elif snapshot is not None:
            for sub_cmd, sub_snapshot in snapshot:
                if _is_number(sub_cmd):
                    _process_number(sub_cmd, stack)
                elif sub_snapshot is not None:
                    _execute_user_defined_word(sub_cmd, {sub_cmd: sub_snapshot}, stack)
                else:
                    _perform_operation(sub_cmd, stack)
        elif cmd in {"+", "-", "*", "/", "DUP", "DROP", "SWAP", "OVER"}:
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
    Take list of strings as Forth commands and return the stack as integers.

    :param input_data: List of strings
    :return: List of integers of the stack
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
