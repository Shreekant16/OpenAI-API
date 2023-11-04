import streamlit as st
import openai

st.title("Input Form")

age = st.number_input("Enter your age", min_value=0, max_value=120, step=1, value=30, format="%d")
height_inches = st.number_input("Enter your height (in inches)", min_value=0, max_value=120, step=1, value=65,
                                format="%d")
weight = st.number_input("Enter your weight (in kg)", min_value=0.0, max_value=500.0, step=0.1, value=70.0)
openai.api_key = 'key'
if st.button('Submit'):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"my age is {age}, height is {height_inches} and weight is {weight}kg give me a proper workout plan to follow for weeks"
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    workout_plan = response.choices[0].text.strip()
    st.write(workout_plan)
