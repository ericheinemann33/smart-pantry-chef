import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Smart Pantry Chef", page_icon="🧑‍🍳")

st.title("🧑‍🍳 The Smart Pantry Chef")
st.write("Tell me what ingredients you have, and I'll create a recipe for you!")

# Security best practice: Ask for the API key in a sidebar so it isn't saved in GitHub!
st.sidebar.header("Setup")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")
st.sidebar.markdown("[Get an API key here](https://aistudio.google.com/) if you don't have one.")

# User Input
ingredients = st.text_area("What's in your pantry? (e.g., chicken, rice, broccoli, soy sauce)")

# The "Generate" Button
if st.button("Generate Recipe"):
    if not api_key:
        st.warning("Please enter your Gemini API Key in the sidebar first!")
    elif not ingredients:
        st.warning("Please enter some ingredients!")
    else:
        try:
            # 1. Connect to Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 2. Write the Prompt
            prompt = f"You are an expert chef. Create a tasty, easy-to-follow recipe using mostly these ingredients: {ingredients}. Provide a fun title, a list of ingredients with measurements, and step-by-step instructions."
            
            # 3. Get the Response
            with st.spinner("Chef Gemini is thinking..."):
                response = model.generate_content(prompt)
                
            # 4. Show the Recipe
            st.success("Bon Appétit!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Oops! Something went wrong: {e}")
