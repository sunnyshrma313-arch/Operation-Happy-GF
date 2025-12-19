import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="To My Favorite Person", page_icon="❤️")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("Hi [mere pyar RUBINA jisne abhi tk to mera use nai kiya age bhi na kre]! ❤️")
st.subheader("I made this little corner of the internet just for you.")

# The Interactive Part
st.write("---")
st.write("### A few reasons why you're amazing:")
reasons = [
    "The way you make me laugh even on bad days.",
    "Your kindness towards everyone around you.",
    "The way you light up every room you walk into.",
    "You're my best friend and my biggest supporter."
]

for reason in reasons:
    st.markdown(f"✨ {reason}")

st.write("---")

# The Big Surprise Button
if st.button('Click here for a surprise!'):
    st.balloons(0)
    st.snow(100)  # Looks like confetti!
    st.success("I love you more than words can say!")
    st.confetti() # Note: standard streamlit uses balloons, but you can add more logic here

col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/400x300.png?text=Our+First+Date", caption="The day it all started")
    
with col2:
    st.image("https://via.placeholder.com/400x300.png?text=Favorite+Memory", caption="I'll never forget this day")

# Footer
st.write("---")
st.write("🏠 Always here for you, [your love manjot]")
