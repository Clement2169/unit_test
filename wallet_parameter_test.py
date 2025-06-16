import pytest
from wallet import Wallet, InsufficientAmount

@pytest.mark.parametrize(
    "init,earned,spent,expected",
    [(0,0,0,0),(0,10,10,0),(90,10,0,100),(90,10,80,20)])
def test_transactions(init,earned,spent,expected) :
    my_wallet= Wallet(init)
    my_wallet.add_cash(earned)
    if (spent <= init+earned ) :
        my_wallet.spend_cash(spent)
        assert my_wallet.deposit == expected
    else :    
        with pytest.raises(InsufficientAmount) :
            my_wallet.spend_cash(spent)
