import streamlit as st


class savingsAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            st.error("insufficient balance")
        else:
            self.balance -= amount
            self.transaction_history.append(f"withdrew {amount}")

    def calculate_interest(self):
        interest_rate = 0.05  # 5% interest rate
        interest = self.balance * interest_rate
        self.balance += interest
        self.transaction_history.append(f"interest added: {interest}")

    def display_transaction_history(self):
        st.write("Transaction History:")
        for transaction in self.transaction_history:
            st.write(transaction)


class currentAccount:
    def _init_(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
        self.transaction_history = []
        self.overdraft_limit = 1000  # overdraft limit

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit :
            st.error ("insufficient balance and overdraft limit exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
        def display_transaction_history(self):
            st.write("transaction History:")
            for transaction in self.transaction_history:
                st.write(transaction)


def main():
    st.title("Banking App")
    account_type = st.selectbox("select account type", ["savings", "current"])

    if account_type == "savings":
        savings_account = savingsAccount()
        st.subheader("savings Account")
        deposit_amount = st.number_input("Deposit amount")
        if st.button("Deposit"):
            savings_account.deposit(deposit_amount)
        withdraw_amount = st.number_input("Withdraw amount")
        if st.button("Withdraw"):
            savings_account.withdraw(withdraw_amount)
        st.write(f"Account balance: {savings_account.balance}")
        st.write("Transaction history:")
        for transaction in savings_account.transaction_history:
            st.write(transaction)


if "_name_" == "__main__":
    main()
