 from utility import BankAccount
import datetime

class CurrentAccount(BankAccount):
    def __init__(self, account_name):
        super().__init__(account_name)
        self.overdraft_limit = 50000

    def withdraw(self, amount):
        available = self.get_balance() + self.overdraft_limit
        if amount > available:
            return f"withdrawal Exceeds overdraft limit (available: ₦{available:,})."

        # Allow negative balance for overdraft
        new_bal = self.get_balance() - amount
        self._balance = new_bal  #this helps update the encapsulated balance
        self.transactions.append({
            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Type": "Withdrawal",
            "Amount": amount,
            "Balance": new_bal
        })
        used = max(0, -new_bal)
        return f"you Withdrew ₦{amount:,} (Overdraft used: ₦{used:,})."