def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.
    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.
    Returns:
        list:  All rounds played.
    """
    return rounds_1 + rounds_2

def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number. 
    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.
    Returns:
        bool: Was the round played?
    """
    return number in rounds

def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.
    Parameters:
        hand (list): The cards in the hand.
    Returns:
        float: The average value of the cards in the hand.
    """
    return sum(hand) / len(hand)

def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.
    Parameters:
        hand (list): The cards in the hand.
 
    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    hand.sort()
    middle_index = len(hand) // 2
    return ((hand[0] + hand[-1]) / 2) == card_average(hand) or hand[middle_index] == card_average(hand)

def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).
    Parameters:
        hand (list): The cards in the hand.
    Returns:
        bool: Are the even and odd averages equal?
    """
    even_list = hand[0::2]
    odd_list = hand[1::2]
    average_even = sum(even_list) / len(even_list)
    average_odd = sum(odd_list) / len(odd_list)
    return average_even == average_odd

def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.
    Parameters:
        hand (list): The cards in the hand.
    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    jack_card = 11
    if hand[-1] == jack_card:
        hand[-1] *= 2
    return hand
