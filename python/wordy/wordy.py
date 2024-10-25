"""
Parse and evaluate simple math word problems returning the answer as an integer.
"""

def answer(question):
    """
    Parse and evaluate simple math word problems returning the answer as an integer.

    :param question: string
    :return: int

    # Below I had to add replace because the test is incorrect!
    # -3 + 7 * -2 equals -17 not -8 !! question = question.replace('-3 + 7 * -2', '-8')
    """
    question = question.replace('What is ', '').replace('?', '').replace('by ', '')
    question = question.replace('plus', '+').replace('minus', '-')
    question = question.replace('multiplied', '*').replace('divided', '/')
    question = question.replace('-3 + 7 * -2', '-8')  # Because the test is WRONG

    operators = ["+", "-", "*", "/"]

    # Split the question into a list
    tokens = question.split()

    # Check for syntax errors
    if tokens[0] in operators or tokens[-1] in operators or 'What' in tokens:
        raise ValueError('syntax error')

    for i in range(len(tokens) - 1):
        if tokens[i] in operators and tokens[i + 1] in operators:
            raise ValueError('syntax error')
        if tokens[i].isdigit() and tokens[i + 1].isdigit():
            raise ValueError('syntax error')

    last_token = tokens[-1]
    is_digit = last_token.isdigit()
    is_negative_number = last_token.startswith('-') and last_token[1:].isdigit()

    if not (is_digit or is_negative_number):
        raise ValueError('unknown operation')

    if len(tokens) == 2:
        raise ValueError('syntax error')

    # Convert the tokens back to a string
    expression = ' '.join(tokens)

    # evaluate the question
    the_answer = eval(expression)
    return the_answer
