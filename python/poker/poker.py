"""Poker Best Hand"""

from collections import Counter

# Define poker hand rankings in order of strength
HAND_RANKINGS = [
    "High Card",
    "One Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
]


def rank_hand(hand):
    """Rank a poker hand based on the strength of the hand.
    hand (str): A string a poker hand, with cards separated by spaces.
    Returns: tuple: A tuple containing the ran.
      The first element is the rank of the hand, and the second element
    is a list of card values in descending order.
    """
    ranks = "23456789TJQKA"  # Define card ranks
    suits = [card[-1] for card in hand.split()]  # Get suits from hand
    #  Get values from hand, put them in descending order
    values = sorted([ranks.index(card[:-1].replace('10', 'T'))
                     for card in hand.split()], reverse=True)

    is_flush = len(set(suits)) == 1  # Check if all suits are the same
    is_straight = (
        all(values[i] - 1 == values[i + 1] for i in range(len(values) - 1))
        or (values == [12, 3, 2, 1, 0])  # Handle 5-high straight (Ace low)
    )

    # Adjust for Ace-low straight (5-high straight) - 2 of the tests
    if values == [12, 3, 2, 1, 0]:
        values = [3, 2, 1, 0, 12]

    # Count each rank that I see
    counts = Counter(values)
    counts_sorted = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
    counts_values = [x[0] for x in counts_sorted]

    if is_straight and is_flush:
        return (8, values)
    elif counts_sorted[0][1] == 4:
        return (7, counts_values)
    elif counts_sorted[0][1] == 3 and counts_sorted[1][1] == 2:
        return (6, counts_values)
    elif is_flush:
        return (5, values)
    elif is_straight:
        return (4, values)
    elif counts_sorted[0][1] == 3:
        return (3, counts_values)
    elif counts_sorted[0][1] == 2 and counts_sorted[1][1] == 2:
        return (2, counts_values)
    elif counts_sorted[0][1] == 2:
        return (1, counts_values)
    else:
        return (0, values)

def best_hands(hands):
    """Find the best hand(s)."""
    ranked_hands = [(rank_hand(hand), hand) for hand in hands]

    best_rank = max(ranked_hands, key=lambda x: x[0])[0]
    best_hands_list = [hand_str for rank, hand_str in ranked_hands if rank == best_rank]

    # If multiple hands have the same rank, allow ties on highest card
    if len(best_hands_list) > 1:
        best_hands_values = [(rank_hand(hand)[1], hand) for hand in best_hands_list]
        max_values = max(best_hands_values, key=lambda x: x[0])[0]
        best_hands_list = [hand for values, hand in best_hands_values if values == max_values]

    return best_hands_list
