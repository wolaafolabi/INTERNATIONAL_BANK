 #this renders your landing page with bank name (D.A.K.A.P) and feature cards
import streamlit as st

def render_home():
    st.title("🏦 Welcome to D.A.K.A.P Bank")
    st.markdown("### Your trusted, digital bank")
    st.markdown("---")

    # a banner
    banner_url = (
        "https://scontent.fabb1-1.fna.fbcdn.net/o1/v/t0/f2/m340/AQNgxqY6A76mCso2MM4BzoUquKr6gxobUTmvGcFwlUP_07nCPEc3GD68KaPUDVg-k8ZYxXslH_DvIuLdHfx0ecQai_LrpX9NPDE5e-YPGC4OKw3u9YYkS4-3n7YhpUwCwkfjhDHou8ReJ2vjOZFVerb4Dk_-6w.jpeg?_nc_ht=scontent.fabb1-1.fna.fbcdn.net&_nc_gid=5u6u0FCj__4MsFtebsTYrQ&_nc_cat=110&_nc_oc=AdmAugNU865LjtGMHiH1ZiNy9fPmwbDU2EdU5cm5u3t5qYi6aIk7RbHmRnb0cEMwo8I&ccb=9-4&oh=00_AfO0Rb9sK_ZesEe5VBgPUmoT4lIrAQMnjdjN0KSuiCYSEA&oe=68545C4D&_nc_sid=5b3566"
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