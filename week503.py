import streamlit as st
st.title("Mini quiz app")
st.write("Please answer the following 3 basic questions about Python and Streamlit:")

st.write("Question 1: Which keyword in Python is used to define a function?")
q1 = st.radio("Please select your answer:",["func", "define", "def", "function"],index=None,key="q1")
st.divider()

st.write("Question 2: In Streamlit, which component is best suited for multiple-choice questions?")
q2 = st.radio("Please select your answer:",["st.selectbox()", "st.checkbox()", "st.radio()", "st.button()"],index=None,key="q2")
st.divider()

st.write("Question 3: Which of the following is a built-in type in Python?")
q3 = st.radio("Please select your answer:",["list", "array", "vector", "matrix"],index=None,key="q3")
st.divider()

if st.button("Submit"):
    if q1 is None and q2 is None and q3 is None:
        st.warning("Please answer all the questions before clicking submit!")
    else:
        score = 0
        if q1 == "def":
            st.success("Your answer is correct!")
            score += 1
        else:
            st.error("Your answer is incorrect!")
        if q2 == "st.radio()":
            st.success("Your answer is correct!")
            score += 1
        else:
            st.error("Your answer is incorrect!")
        if q3 == "list":
            st.success("Your answer is correct!")
            score += 1
        else:
            st.error("Your answer is incorrect!")
        st.divider()

        if score == 3:
            st.success("You are perfect!")
        else:
            st.info(f"Your final score is:**{score}/3**")


