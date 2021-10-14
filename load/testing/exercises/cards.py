from enum import IntEnum
import random
from typing import List, Tuple


class Suit(IntEnum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3


CardType = Tuple[Suit, int]
CardsType = List[CardType]


def create_deck() -> CardsType:
    return [(suit, value) for value in range(1, 14) for suit in Suit]


def shuffle_deck(deck: CardsType) -> None:
    random.shuffle(deck)


def deal_hand(deck: CardsType, n: int = 5) -> Tuple[CardsType, CardsType]:
    hand = deck[:n]
    remaining_deck = deck[n:]

    return hand, remaining_deck


def main() -> None:
    deck = create_deck()
    shuffle_deck(deck)

    print(f"The initial deck contains {len(deck)} cards.")

    hand, deck = deal_hand(deck)
    print(hand)

    hand, deck = deal_hand(deck)
    print(hand)

    print(f"The remaining deck contains {len(deck)} cards.")


if __name__ == "__main__":
    main()
