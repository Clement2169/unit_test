import pytest
from wallet import Wallet, InsufficientAmount

def test_initial_deposit() :
    my_wallet = Wallet()
    assert (my_wallet.deposit == 0)

def test_deposit_100() :
    my_wallet = Wallet(100)
    assert (my_wallet.deposit == 100)

def test_deposit_10() :
    my_wallet = Wallet(10)
    my_wallet.add_cash(90)
    assert (my_wallet.deposit == 100)

def test_deposit_20 ():
    my_wallet = Wallet(20)
    my_wallet.spend_cash(10)
    assert (my_wallet.deposit == 10)

def test_insufficient_amount() :
    with pytest.raises(InsufficientAmount) :
        my_wallet = Wallet(10)
        my_wallet.spend_cash(20)
