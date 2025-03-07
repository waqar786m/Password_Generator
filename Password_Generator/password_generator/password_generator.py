import streamlit as st # Importing the streamlit library for creating the web app
import random # Importing the random library for generating random passwords
import string # Importing the string library for using string characters

# Function to generate a  password based on the user's preferences
def generate_password(length , use_digits , use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits # add numbers (0-9) if selected
    if use_special:
        characters += string.punctuation # add special characters (!,@,#,$,%,^,&,*)

    # Generate a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI setup

st.title("Password Generator") # Title of the web app

length = st.slider("Select Password length" , min_value=6 , max_value=32 , value=12) # Slider to select the length of the password

use_digits = st.checkbox("Include Digits") # Checkbox to include digits in the password

use_special = st.checkbox("Include Special Characters") # Checkbox to include special characters in the password

if st.button("Generate Password"):
    password = generate_password(length , use_digits , use_special)
    st.write(f"Generated Password: {password}")

st.write("--------------------------------")

st.write("build with ❤️ by [Waqar Ahmed](https://github.com/waqar786m)")

