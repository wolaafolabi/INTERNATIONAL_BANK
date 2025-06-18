#mainapp.py is the streamlit UI that ties everything together
import streamlit as st
import random

from utility import notify_user, show_statement
from savings import SavingsAccount
from current import CurrentAccount
from home import render_home

# 1) Initialize accounts in session state
if 'savings_acc' not in st.session_state:
    st.session_state.savings_acc = SavingsAccount("Student Savings")
if 'current_acc' not in st.session_state:
    st.session_state.current_acc = CurrentAccount("Student Current")

savings = st.session_state.savings_acc
current = st.session_state.current_acc

# 2) Page config & home
st.set_page_config(page_title="D.A.K.A.P Bank App", layout="wide")
render_home()

# 3) Sidebar:for tip & hide/show balance # added many student tips just for fun
tips = [
    "Tip: Always keep some funds in your savings account for emergencies.",
    "Tip: Review your mini statement regularly to track expenses.",
    "Tip: Use 'Hide Balance' to protect your financial information.",
    "Tip: Set a savings goal and try to automate your deposits.",
    "Tip: Use mini statements to check for unexpected charges.",
    "Tip: Avoid withdrawing from your savings too often to build discipline.",
    "Tip: Transfer excess from current to savings monthly to grow faster."
]
st.sidebar.header("Tip of the Day")
st.sidebar.info(random.choice(tips))
st.sidebar.markdown("---")
hide_bal = st.sidebar.checkbox("Hide Balances")

# 4) Page navigation
page = st.selectbox("Navigate to", ["Savings", "Current", "Mini Statement"])

# 5) Savings/Current operations
if page in ["Savings", "Current"]:
    acc = savings if page == "Savings" else current

    st.subheader(f"{page} Deposit")
    amt_d = st.number_input("Amount", min_value=0, step=100, key=page+"d")
    if st.button(f"Deposit to {page}"):
        msg = acc.deposit(amt_d)
        notify_user(msg)

    st.subheader(f"{page} Withdraw")
    amt_w = st.number_input("Amount", min_value=0, step=100, key=page+"w")
    if st.button(f"Withdraw from {page}"):
        msg = acc.withdraw(amt_w)
        notify_user(msg)

    st.subheader("Balance")
    if not hide_bal:
        st.metric(label=f"{page} Balance", value=f"₦{acc.get_balance():,.2f}")
    else:
        st.write("Balance hidden")

# 6) Mini statement
elif page == "Mini Statement":
    st.subheader("Mini Statement (Last 5 Transactions)")
    choice = st.radio("Account", ["Savings", "Current"])
    acc = savings if choice == "Savings" else current
    show_statement(acc.get_statement(5))

# 7) Floating contact & branding
st.markdown(
    """
    <a href="tel:+2348050250057" style="
        position: fixed; bottom: 20px; right: 20px;
        background-color: #004B8D; color: white;
        padding: 12px 24px; border-radius: 30px;
        text-decoration: none; font-weight: bold;
    ">📞 +2348050250057</a>
    <a href="mailto:darasimisaac13@gmail.com?subject=Help%20with%20C.O.D.M%20Bank%20App" style="
        position: fixed; bottom: 20px; right: 180px;
        background-color: #4CAF50; color: white;
        padding: 12px 24px; border-radius: 30px;
        text-decoration: none; font-weight: bold;
    ">📧 Email Us</a>
    <div style="
        position: fixed; bottom: 70px; right: 20px;
        color: gray; font-size:12px;
    ">D.A.K.A.P. Bank © 2025</div>
    """,
    unsafe_allow_html=True,
)