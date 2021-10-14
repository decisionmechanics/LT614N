import pytest
import random
import cards


@pytest.fixture
def deck():
    return cards.create_deck()


def test_create_deck_returns_deck_of_52_cards(deck):
    # Arrange

    # Act

    # Asset
    assert len(deck) == 52


def test_create_deck_returns_deck_with_all_suits(deck):
    # Arrange
    expected_suits = {suit for suit in cards.Suit}

    # Act

    # Asset
    actual_suits = {card[0] for card in deck}
    assert actual_suits == expected_suits


def test_create_deck_returns_deck_with_all_values(deck):
    # Arrange
    expected_values = set(range(1, 14))

    # Act

    # Asset
    actual_values = {card[1] for card in deck}
    assert actual_values == expected_values


def test_shuffle_deck_shuffles_first_card(deck):
    # Arrange
    first_card = deck[0]

    random.seed(614)
    # Act
    cards.shuffle_deck(deck)

    # Asset
    assert deck[0] != first_card


def test_shuffle_deck_shuffles_last_card(deck):
    # Arrange
    last_card = deck[-1]

    random.seed(614)
    # Act
    cards.shuffle_deck(deck)

    # Asset
    assert deck[-1] != last_card


def test_deal_hand_returns_5_cards(deck):
    # Arrange

    # Act
    hand, _ = cards.deal_hand(deck)

    # Asset
    assert len(hand) == 5


def test_deal_hand_of_2_cards_returns_2_cards(deck):
    # Arrange

    # Act
    hand, _ = cards.deal_hand(deck, 2)

    # Asset
    assert len(hand) == 2


def test_deal_hand_returns_cards_from_top_of_deck(deck):
    # Arrange

    # Act
    hand, _ = cards.deal_hand(deck)

    # Asset
    assert hand == deck[:5]


def test_deal_hand_removes_n_cards_from_deck(deck):
    # Arrange

    # Act
    _, remaining_deck = cards.deal_hand(deck)

    # Asset
    assert len(remaining_deck) == 52 - 5
