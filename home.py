 #this renders your landing page with bank name (C.O.D.E.) and feature cards
import streamlit as st

def render_home():
    st.title("🏦 Welcome to C.O.D.E. Bank")
    st.markdown("### Your trusted, student digital bank")
    st.markdown("---")

    # a banner
    banner_url = (
        "https://images.unsplash.com/photo-1521791136064-7986c2920216"
        "?ixlib=rb-4.0.3&auto=format&fit=crop&w=700&q=80"
    )
    try:
        from PIL import Image
        import requests
        from io import BytesIO

        resp = requests.get(banner_url)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))
        st.image(img, width=700, caption="Banking in its best form")
    except Exception as e:
        st.warning(f"sorry,Could NOT load banner: {e}")


    #the Three feature cards in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://img.icons8.com/fluency/96/000000/money-bag-euro.png")
        st.subheader("Secure Savings")
        st.write("Kindly Deposit & watch your savings grow.")
    with col2:
        st.image("https://img.icons8.com/color/96/000000/withdraw.png")
        st.subheader("Easy Withdrawals")
        st.write("Fast access to your funds.")
    with col3:
        st.image("https://img.icons8.com/color/96/000000/real-time-claims.png")
        st.subheader("Instant Alerts")
        st.write("Get notifications for every transaction you make.")
    st.markdown("---")