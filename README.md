# 🍳 AI Recipe Generator (Gemini-powered)

This project is a simple **Recipe Generator Agent** built with **Google Gemini** and **FastAPI**.  
It takes a list of ingredients and dietary preferences as input, then generates a complete recipe including ingredients list, steps, prep time, and serving size.  

---

## 🚀 Features
- Input your available ingredients  
- Add preferences (e.g. *spicy, vegan, Italian*)  
- AI generates a unique recipe using **Gemini**  
- API-based backend (FastAPI) → easy to connect with frontend (React, V0, Lovable, etc.)  

---

## 📂 Project Structure
recipe_agent/
│── main.py # CLI version (for quick testing)
│── api.py # FastAPI backend
│── tools.py # Helper functions
│── requirements.txt # Python dependencies
│── .env.example # Environment variable template

yaml
Copy code

---

## 🔑 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/recipe-generator.git
cd recipe-generator
2. Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure API Key
Copy .env.example → .env

Replace your_api_key_here with your Google Gemini API Key

Example .env:

ini
Copy code
GEMINI_API_KEY=your_api_key_here
▶️ Running the Project
Option A: Run CLI Version
bash
Copy code
python main.py
Example interaction:

pgsql
Copy code
🍳 Welcome to Recipe Generator Agent!
Enter the ingredients you have: potato, tomato, salt, oil
Any preferences? (e.g. spicy, vegan, Italian): spicy
Output:

markdown
Copy code
--- Generated Recipe ---
Spicy Potato & Tomato Curry
Ingredients:
- ...
Steps:
1. ...
Option B: Run API Server
bash
Copy code
uvicorn api:app --reload
API will be available at:

arduino
Copy code
http://127.0.0.1:8000/generate-recipe
Example request:

bash
Copy code
curl -X POST "http://127.0.0.1:8000/generate-recipe" \
-H "Content-Type: application/json" \
-d '{"ingredients": "potato, tomato, onion", "preferences": "spicy"}'
Example response:

json
Copy code
{
  "recipe": "Spicy Potato & Tomato Curry ... full recipe ..."
}
