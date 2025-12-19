import streamlit as st

# Page Configuration
st.set_page_config(page_title="To My Favorite Person RUBINA ji", page_icon="❤️")

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
st.title("Hi there! ❤️")
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
    st.balloons()
    st.snow(50) 
    st.success("I never knew what true happiness was until I met you. You've filled my life with a love so deep and beautiful that I can't imagine a single day without you")

# Footer
st.write("unwavering support, and recognizing her strength/beauty, like "You're capable of amazing things, I believe in you!" or "I'm so proud of you, stay strong!" or "You're my sunshine, go spread your magic!")
st.write("🏠 Always there for you. Apka long distance realtionship wala pyar MANJOT.")
