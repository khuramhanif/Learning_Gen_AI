import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, time

st.write("Most objects")  # df, err, func, keras!
st.write(["st", "is <", 3])  # see *
# st.write_stream(my_generator)
# st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("_Markdown_")  # see *
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")


with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(300, 3))

# Display a chat input widget at the bottom of the app.
st.chat_input("Say something")


st.success("Success")
st.info("Information")
st.warning("warning")
st.error("Error")
err = ZeroDivisionError("Divide by Zero")
st.exception(err)


if st.checkbox("Show/Hide"):
    st.write("Show something")


status = st.radio("Select Gender:", ("Male", "Female", "Trans-Gender"))
if (status == "Male"):
    st.success("Male")
elif (status == "Female"):
    st.success("Female")
else:
    st.success("Trans-gender")


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


st.button("click me for no reson")


if (st.button("PIAIC")):
    st.text("Welcome to the World of generative AI")


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)


start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)