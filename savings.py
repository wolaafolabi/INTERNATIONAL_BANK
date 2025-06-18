# savings account with one time and daily withdrawal limit
from utility import BankAccount
import datetime

class SavingsAccount(BankAccount):
    def __init__(self, account_name):
        super().__init__(account_name)
        self.one_time_limit = 20000   # ₦20,000 naira limit per transaction
        self.daily_limit = 50000      # ₦50,000 naira limit per day
        self.daily_withdrawn = {}

    def withdraw(self, amount):
        today = datetime.date.today().isoformat()
        used = self.daily_withdrawn.get(today, 0)

        if amount > self.one_time_limit:
            return f"❌sorry,your withdrawal Exceeds your one‑time limit of ₦{self.one_time_limit:,}."
        if used + amount > self.daily_limit:
            return f"❌your withdrawal Exceeds your daily limit of ₦{self.daily_limit:,} (used: ₦{used:,})."
        if amount > self.get_balance():
            return "❌You have Insufficient funds."

        result = super().withdraw(amount)
        if result.startswith("✅"):
            self.daily_withdrawn[today] = used + amount
            return f"{result} (Today: ₦{self.daily_withdrawn[today]:,})"
        return result