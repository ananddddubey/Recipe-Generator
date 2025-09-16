# tools.py

import re

def parse_ingredients(user_input: str):
    """
    Takes raw user input like 'I have chicken, onion and garlic'
    Returns a clean list of ingredients: ['chicken', 'onion', 'garlic']
    """
    # Remove filler words
    clean_input = user_input.lower()
    clean_input = re.sub(r"\b(i have|with|and|some|a few|few)\b", "", clean_input)

    # Split by comma or space
    parts = re.split(r",|;|\.|\band\b", clean_input)
    ingredients = [p.strip() for p in parts if p.strip()]

    return ingredients

def build_recipe_prompt(ingredients, preferences=""):
    """
    Builds a structured prompt for Gemini using ingredients + preferences
    """
    ingredient_str = ", ".join(ingredients)
    prompt = f"""
    You are a world-class chef.
    Create a recipe using the following ingredients: {ingredient_str}.
    Preferences: {preferences if preferences else 'None'}.

    The recipe should include:
    - A creative recipe name
    - Ingredients list with amounts
    - Step-by-step instructions
    - Estimated cooking + prep time
    - Serving size
    """

    return prompt
