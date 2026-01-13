

class BankAccount:
    """Bank Account protected by a pin number."""

    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        self.balance = 0.0
        self.pin = pin

    def _verify_pin(self, pin):
        """Internal helper to verify the PIN."""
        if pin != self.pin:
            raise ValueError("Wrong pin number")

    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        self._verify_pin(pin)
        self.balance += amount
        return self.balance

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        self._verify_pin(pin)
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return amount

    def get_balance(self, pin):
        """Return account balance."""
        self._verify_pin(pin)
        return self.balance

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        self._verify_pin(oldpin)
        self.pin = newpin


class SavingsAccount(BankAccount):
    """A BankAccount that earns interest."""

    def __init__(self, pin, interest_rate):
        """Initialize with parent attributes plus interest rate."""
        super().__init__(pin)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Increase the balance by the interest rate."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance


class FeeSavingsAccount(SavingsAccount):
    """A SavingsAccount that charges a fee for every withdrawal."""

    def __init__(self, pin, interest_rate, fee):
        """Initialize with parent attributes plus a withdrawal fee."""
        super().__init__(pin, interest_rate)
        self.fee = fee

    def withdraw(self, pin, amount):
        """Deduct fee before performing withdrawal."""
        self._verify_pin(pin)
        total_deduction = amount + self.fee
        if total_deduction > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= total_deduction
        return amount

if __name__ == "__main__":
    """Test all branches of the bank account system."""
    print("Starting tests...")

    # Test BankAccount
    acc = BankAccount("1234")
    acc.deposit("1234", 100)
    assert acc.get_balance("1234") == 100.0

    # Test withdrawal success
    acc.withdraw("1234", 40)
    assert acc.get_balance("1234") == 60.0

    # Test withdrawal failure (Insufficient balance)
    try:
        acc.withdraw("1234", 100)
        assert False, "Should have raised Insufficient balance Exception"
    except Exception as e:
        assert str(e) == "Insufficient balance"

    # Test PIN failure
    try:
        acc.get_balance("0000")
        assert False, "Should have raised Wrong pin number Exception"
    except Exception as e:
        assert str(e) == "Wrong pin number"

    # Test PIN change
    acc.change_pin("1234", "5678")
    assert acc.get_balance("5678") == 60.0

    # Test SavingsAccount
    sav = SavingsAccount("1111", 0.1)  # 10% interest
    sav.deposit("1111", 200)
    sav.apply_interest()
    assert sav.get_balance("1111") == 220.0

    # Test FeeSavingsAccount
    fee_acc = FeeSavingsAccount("9999", 0.05, 2.0)
    fee_acc.deposit("9999", 100)

    # Test withdrawal with fee (10 + 2 fee = 12 total)
    fee_acc.withdraw("9999", 10)
    assert fee_acc.get_balance("9999") == 88.0

    # Test withdrawal failure due to fee
    try:
        fee_acc.withdraw("9999", 87)
        assert False, "Should have raised Exception for fee covering"
    except Exception as e:
        assert str(e) == "Insufficient balance"

    print("All tests passed successfully!")