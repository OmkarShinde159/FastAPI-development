from app.calculations import add,sub,mul,div,BankAccount,InsufficientFunds
import pytest


@pytest.fixture
def zero_bank_account():
    print("Running fixture function ...")
    return BankAccount()

@pytest.fixture
def bank_account():
    print("Running fixture function ...")
    return BankAccount(50)



@pytest.mark.parametrize("num1,num2,expected",[
    (5,2,7),
    (7,1,8),
    (10,2,12)
])
def test_add(num1,num2,expected):
    print("Testing add function")
    assert add(num1,num2) == expected
  
def test_sub():
    print("Testing sub function")
    assert sub(5,3) == 2

def test_mul():
    print("Testing mul function")
    assert mul(5,3) == 15

def test_div():
    print("Testing div function")
    assert div(15,3) == 5

def test_bank_set_initial_amount(bank_account):
    print("Running test function ...")
    # bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("Running test function ...")
    # bank_account = BankAccount()
    assert zero_bank_account.balance == 0

def test_deposite():
    bank_account = BankAccount(99)
    bank_account.deposite(10)
    assert bank_account.balance == 109

def test_withdraw():
    bank_account = BankAccount(99)
    bank_account.withdraw(10)
    assert bank_account.balance == 89

def test_collect_interest(bank_account):
    print("Running test function ...")
    # bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55

@pytest.mark.parametrize("amt1,amt2,total",[
    (50,20,30),
    (700,100,600),
    (10,2,8),
    (120,50,70)
])
def test_bank_transaction(zero_bank_account,amt1,amt2,total):
    zero_bank_account.deposite(amt1)
    zero_bank_account.withdraw(amt2)
    assert zero_bank_account.balance == total

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
            bank_account.withdraw(200)









