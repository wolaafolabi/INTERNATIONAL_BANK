#  This holds the base Bank Account classes(encapsulation, transaction history) and other helper functions
import uuid
import datetime
import streamlit as st

class BankAccount:
    def __init__(self, account_name):
        self.account_number = str(uuid.uuid4())[:8]
        self.account_name = account_name
        self._balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount." # cant deposit any amount less than or equal to 0 naira
        self._balance += amount
        self.transactions.append({
            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Type": "Deposit",
            "Amount": amount,
            "Balance": self._balance
        })
        return f"Deposited ₦{amount:,}."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transactions.append({
                "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Type": "Withdrawal",
                "Amount": amount,
                "Balance": self._balance
            })
            return f"you Withdrew ₦{amount:,}."
        return "you have Insufficient funds."

    def get_balance(self):
        return self._balance

    def get_statement(self, n=5):
        return list(reversed(self.transactions))[:n]

def notify_user(message):
    """Display a message in Streamlit."""
    st.info(message)

def show_statement(statement):
    """gives a mini bank-statement as a table."""
    if statement:
        st.table(statement)
    else:
        st.write("you haven't made any transactions yet.")

