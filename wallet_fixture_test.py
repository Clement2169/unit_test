import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet() :
    return Wallet()

@pytest.fixture
def wallet100() :
    return Wallet(100)

@pytest.fixture
def wallet10() :
    return Wallet(10)


def test_initial_deposit(empty_wallet) :
    assert (empty_wallet.deposit == 0)

def test_deposit_100(wallet100) :
    assert (wallet100.deposit == 100)

def test_deposit_10(wallet10) :
    wallet10.add_cash(90)
    assert (wallet10.deposit == 100)

def test_deposit_20 (wallet10):
    wallet10.add_cash(10)
    wallet10.spend_cash(10)
    assert (wallet10.deposit == 10)

def test_insufficient_amount(wallet10) :
    with pytest.raises(InsufficientAmount) :
        wallet10.spend_cash(20)
