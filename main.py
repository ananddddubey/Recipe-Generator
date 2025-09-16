# main.py
import os
from dotenv import load_dotenv
from tools import parse_ingredients, build_recipe_prompt
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_recipe(user_input: str, preferences: str = ""):
    # Step 1: Parse ingredients
    ingredients = parse_ingredients(user_input)

    # Step 2: Build recipe prompt
    prompt = build_recipe_prompt(ingredients, preferences)

    # Step 3: Call Gemini
    response = model.generate_content(prompt)

    return response.text

if __name__ == "__main__":
    print("🍳 Welcome to Recipe Generator Agent!")
    user_ingredients = input("Enter the ingredients you have: ")
    user_preferences = input("Any preferences? (e.g. spicy, vegan, Italian): ")

    recipe = generate_recipe(user_ingredients, user_preferences)
    print("\n--- Generated Recipe ---\n")
    print(recipe)
