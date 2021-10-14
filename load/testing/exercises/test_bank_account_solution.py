import datetime as dt
import pytest
import bank_account


@pytest.fixture
def savings_account():
    return bank_account.create_bank_account(100)


def test_create_bank_account_with_initial_deposit_of_50_returns_a_balance_of_50():
    # Arrange

    # Act
    savings_account = bank_account.create_bank_account(50)

    # Assert
    assert savings_account() == 50


@pytest.mark.parametrize("amount, expected_balance", [(-50, 50), (0, 100), (50, 150)])
def test_deposits(savings_account, amount, expected_balance):
    # Arrange

    # Act
    savings_account.deposit(amount)

    # Assert
    assert savings_account() == expected_balance


@pytest.mark.parametrize("amount, expected_balance", [(0, 100), (50, 50), (75, 25)])
def test_withdrawals(savings_account, amount, expected_balance):
    # Arrange

    # Act
    savings_account.withdraw(amount)

    # Assert
    assert savings_account() == expected_balance


def test_withdrawing_too_much_raises_bank_account_exception(savings_account):
    with pytest.raises(bank_account.BankAccountError):
        savings_account.withdraw(150)


@pytest.mark.skip(reason="too slow")
def test_fetch_special_offers_only_returns_current_offers():
    # Arrange
    today = dt.date.today()

    # Act
    special_offers = bank_account.fetch_special_offers()
    expiry_dates = [special_offer["expires"] for special_offer in special_offers]

    # Assert
    for expires in expiry_dates:
        assert today <= expires
