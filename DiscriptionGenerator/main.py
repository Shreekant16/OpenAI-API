import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = "Our-key"

# Define Streamlit app
def main():
    st.title("Description Generator")

    # Input field for user to provide a small description
    description = st.text_area("Enter a small description:")

    if st.button("Generate Description"):
        if description:
            # Generate a longer description using OpenAI API
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"Generate the description of 250-300 characters for the following small description: {description}",
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            generated_description = response.choices[0].text.strip()

            # Display the generated description
            st.subheader("Generated Description")
            st.write(generated_description)
        else:
            st.warning("Please enter a small description first.")

if __name__ == "__main__":
    main()