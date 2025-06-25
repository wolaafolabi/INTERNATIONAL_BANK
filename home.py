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
        st.image(img, width=700, caption="BANKING IN IT'S FORM")
    except Exception as e:
        st.warning(f"sorry,Could NOT load banner: {e}")


    #the Three feature cards in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://scontent.fabv2-2.fna.fbcdn.net/o1/v/t0/f2/m340/AQPXvdPKQ44Y_6v19XuwzY2RykKVPc84OwH-moW-LWdrsKu0eptz_xQArrY2FO35zeDR_lkUaZCciNtrMbiTsFCfCCrsAqxBevSfyumGStTAUqbZeD3oHPJME3lbDP-RIFz5azL3VIMsyq2shWv3x0VvlL2zEw.jpeg?stp=s1440x1440&_nc_ht=scontent.fabv2-2.fna.fbcdn.net&_nc_gid=K2ztB4mGRg6IZ0ZaorllXQ&_nc_cat=100&_nc_oc=AdkNmibRjjavg0QHnXQZpYCZScEWJeGo05pVBaKgHN5Yq-RiDAwQ_r8NsqqkRI9xeE4&ccb=9-4&oh=00_AfObP27HgG-c6uwF-wz3yaxUfJemY2VVwduF5MbHlsYE_g&oe=68548DC3&_nc_sid=5b3566")
        st.subheader("Secure Savings")
        st.write("Kindly Deposit & watch your savings grow.")
    with col2:
        st.image("https://scontent.fabv2-2.fna.fbcdn.net/o1/v/t0/f2/m340/AQPhYLUyXgOZgyWPMU_RcB-eBk8rq7F-lVsSvPIxDOcD6nvTa3vSxk07hSrGxU-KJOTwmrp2quczEjtjgSarRZ5WB5mxnnAxMQOy8R3TRWHrDlbj-gVKGxfjw5NxIvbY1HZ3YA2EyT5_vHnWoaagrR0GTYc8KA.jpeg?stp=s1440x1440&_nc_ht=scontent.fabv2-2.fna.fbcdn.net&_nc_gid=zyWXvFJXYBi0RqCR5ZB84w&_nc_cat=104&_nc_oc=AdlxUVxO2Q67Ld8n0OMMsDR9fBZkBGJH06mwYOCCFuDz_b-PIAXKkBvTUkP7ufvYX9k&ccb=9-4&oh=00_AfONOPp8hitfCfGdju89Xt_-oGy3R6NwUTy8ks2gth8aRQ&oe=68548107&_nc_sid=5b3566")
        st.subheader("Easy Withdrawals")
        st.write("Fast access to your funds.")
    with col3:
        st.image("https://scontent.fabv2-2.fna.fbcdn.net/o1/v/t0/f2/m340/AQPjnGt-xGW-4q71XAtAFfR3VLRGZVkmEWPs01neHsSWdt1AMsCH9QvqQ5hHWPDVpZxImUErmF65SVh-zeoxGySJYcwgBzRX9RDg4IJgOH3qsh8oEcomZKC7FdBOZWgR2Y_43aNalEuqTUzKGW834oCh33R46g.jpeg?stp=s1440x1440&_nc_ht=scontent.fabv2-2.fna.fbcdn.net&_nc_gid=qEBzUGT9tVOAPV6VIgAzcQ&_nc_cat=111&_nc_oc=AdnGPJr-FaTDjNSgu6rEe8ruq33TgBTpq_8HdyI0KIfxtvHa6c9r1CYOPddCXevVOd4&ccb=9-4&oh=00_AfNQkq_hoYFBuL4UULNrMHpAflN3TwX0YRopwkUDchk3Kg&oe=68547FDA&_nc_sid=5b3566")
        st.subheader("Instant Alerts")
        st.write("Get notifications for every transaction you make.")
    st.markdown("---")
