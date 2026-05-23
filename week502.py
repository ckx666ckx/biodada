import streamlit as st
st.title("Calculator")
number1 = st.number_input("Enter first number",value=0.0)
number2 = st.number_input("Enter second number",value=0.0)
operation = st.selectbox("Select operation",["+","-","*","/"])
if st.button("Calculate"):
    result = None
    is_valid = True
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            is_valid = False
            st.error("The divisor cannot be 0")
        else:
            result = number1 / number2

    if result and is_valid is not None:
        st.success("The result is {}".format(result))
    else:
        st.error("No calculation results were found; the process may be incorrect.")


