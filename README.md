# 🧠 Customer Review Insight Assistant

This project is an **AI-powered system** that analyzes customer review data from e-commerce platforms. It uses Python for data cleaning and preprocessing, GPT-4 for intelligent insights, FastAPI for backend services, and a responsive TailwindCSS frontend to interact with the AI assistant.

---

## 🚀 Key Features

- ✅ **Data Cleaning & Validation**: Handles missing values, fixes typos, standardizes categories and timestamps.
- 📊 **Data Exploration & Visualization**: Plots ratings, categories, fulfillment status, and monthly review trends.
- 🤖 **AI-Powered Q&A**: GPT-4 answers business questions about customer reviews with context-aware responses.
- 🌐 **FastAPI Backend**: Efficient, production-ready API to serve questions and return GPT answers.
- 💡 **Interactive Frontend**: User-friendly interface built with Tailwind CSS to query insights using filters.

---

## 📁 Project Structure


.
├── cleaned_customer_reviews.csv   # Final cleaned dataset
├── app.py                         # FastAPI backend with OpenAI integration
├── index.html                     # Frontend (HTML + TailwindCSS + JS)
├── customer_cleaning_analysis.ipynb # Jupyter notebook for EDA, cleaning, and visualization
├── .env                           # Stores OpenAI API key (not shared)
└── README.md                      # Project documentation
🔍 Data Workflow
Raw Input: sample_customer.csv with reviews, ratings, timestamps, etc.

Cleaning:

Fixes categories (e.g., 'Cocktail Dreses' → 'Cocktail Dresses')

Corrects fulfillment typos (e.g., 'Delaye' → 'Delayed')

Fills missing values (rating, order value)

Flags empty or very short reviews

Visualization:

Ratings distribution

Product category trends

Fulfillment status breakdown (pie chart)

Monthly review activity

Export:

Final clean dataset saved as cleaned_customer_reviews.csv

🤖 AI Assistant Overview
The backend uses GPT-4 to answer questions like:

“Which product category has the most 1-star reviews in Canada?”

It extracts a sample of cleaned data and sends it with your question to OpenAI.

The AI replies with bullet points, trends, or summaries.

You can query by country, product, or rating from the frontend.

🌐 Frontend Demo
Built using HTML, TailwindCSS, and FontAwesome icons.

Features:
Input custom questions

Filter by:

📍 Country

⭐ Rating

📦 Product Category

Get structured GPT responses

Follow-up options: Refine, Copy, Export (coming soon)

⚠️ Currently simulates API responses — you can connect to /ask endpoint in production.

🔧 Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/your-username/review-insight-assistant.git
cd review-insight-assistant
2. Create .env File
env
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run FastAPI Server
bash
Copy
Edit
uvicorn app:app --reload
5. Open index.html
Open index.html in your browser and interact with the assistant.

📊 Sample Summary Stats
Metric	Value
Total Reviews	72
Avg Rating	2.81
Top Category	Prom Dresses
Avg Order Value	$287.64
Fulfillment Issues	Delayed, Cancelled

🛠️ Technologies Used
Python, Pandas, Matplotlib, Seaborn — Data Cleaning & EDA

FastAPI, OpenAI GPT-4, TextBlob — Backend AI logic

TailwindCSS, JavaScript, HTML — Frontend UI

.env, CORS, dotenv — Environment management

📌 Future Enhancements
Add PDF/CSV Export in frontend

Connect live GPT-4 model via OpenAI API

Add LangChain/LLM agents for advanced insights

Store chat logs and insights in MongoDB

Sentiment-based recommendations

