import streamlit as st
import datetime

st.set_page_config(
    page_title="Simple Age Calculator",
    page_icon="🧮",
    layout="wide"
)

st.title("🧮 Simple Age Calculator")
st.caption("## This is a simple age calculator that calculates your age in years, months, and days.")

st.divider()

dob = st.date_input("Enter your date of birth", value=None)

if dob:
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"### Your age is {age} years, {abs(dob.month - today.month)} months, and {abs(today.day - dob.day)} days.")
    st.write(f"### You have {100 - age} years shot to your 100th birthday")
else:
    st.write("### Please enter your date of birth to calculate your age.")
