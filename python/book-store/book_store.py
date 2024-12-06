"""Book Store"""
from collections import Counter

# Cost of each book as int
COST_PER_BOOK = 800

# Discount for each number of books in the series
DISCOUNTS_PER_NUMBER = {
    1: 0,
    2: .05,
    3: .10,
    4: .20,
    5: .25,
}


def _calculate_discounted_price(group_size):
    """Calculate the price of a group with discount applied."""
    discount = DISCOUNTS_PER_NUMBER[group_size]
    return group_size * COST_PER_BOOK * (1 - discount)


def _form_groups(basket):
    """Form series of unique books (1-5)."""
    counts = Counter(basket)
    series = []

    while any(counts.values()):
        group = []
        for book, count in list(counts.items()):
            if count > 0:
                group.append(book)
                counts[book] -= 1
        series.append(group)

    return series


def _optimize_groups(series):
    """
    Optimize groups to minimize the total price.
    If we reiterate through all combinations of series it can get very complex
    So we will just swap one book from a group of 5 to a group of 3
    """
    while True:
        # Find any group of 5 and any group of 3
        group_of_five = next(
            (group for group in series if len(group) == 5),
            None
        )
        group_of_three = next(
            (group for group in series if len(group) == 3),
            None
        )

        # Move the book from 5 series to 3 series if its there
        if group_of_five and group_of_three:
            book_to_move = group_of_five.pop()
            group_of_three.append(book_to_move)
        else:
            break
    return series


def total(basket):
    """
    Find the cost of a basket of books.

    :basket: list of books in the basket
    :return: total cost of the basket
    """
    if not basket:
        return 0

    series = _form_groups(basket)
    optimized_series = _optimize_groups(series)

    total_price = sum(
        _calculate_discounted_price(len(group))
        for group in optimized_series
    )

    return total_price
