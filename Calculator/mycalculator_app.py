import streamlit as st
import math

st.set_page_config(page_title="My Calculator", page_icon="🔢")

st.title("🔢 My Advance Calculator")
st.markdown("---")

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

# layout - two columns
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operator selection
operator = st.selectbox("Select operator", [
    "+ (Addition)",
    "- (Subtraction)",
    "* (Multiplication)",
    "/ (Division)",
    "% (Percentage)",
    "√ (Square Root of first number)",
    "x^n (Power of first number)"
])

st.markdown("---")

if st.button("Calculate", use_container_width=True):
    result = None

    if operator == "+ (Addition)":
        result = num1 + num2
        expression = f"{num1} + {num2}"

    elif operator == "- (Subtraction)":
        result = num1 - num2
        expression = f"{num1} - {num2}"

    elif operator == "* (Multiplication)":
        result = num1 * num2
        expression = f"{num1} x {num2}"

    elif operator == "/ (Division)":
        if num2 == 0: 
            st.error("❌ Error: Cannot divide by zero")
        else:
            result = num1 / num2
            expression = f"{num1} ➗ {num2}"

    elif operator == "% (Percentage)":
        result = (num1 / 100) * num2
        expression = f"{num1}% of {num2}" 

    elif operator == "√ (Square Root of first number)":
        if num1 < 0:
            st.error("❌ Error: Cannot find square root of negative number")
        else: 
            result = math.sqrt(num1)
            expression = f"√{num1}"

    elif operator == "x^n (Power of first number)":
            result = num1 ** num2
            expression = f"{num1} ^ {num2}"

    if result is not None:
            st.success(f"✅ Answer: {result}")
            st.session_state.history.append(f"{expression} = {result}")

st.markdown("---")

# History section
st.subheader("📋 Calculation History")

if len(st.session_state.history) == 0:
    st.info("No calculatios yet")
else:
    for item in reversed(st.session_state.history):
        st.write("▶︎", item)

if st.button("Clear History"):
    st.session_state.history = []
    st.rerun()            



