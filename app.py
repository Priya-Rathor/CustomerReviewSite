from fastapi import FastAPI, Query
from pydantic import BaseModel
import pandas as pd
from textblob import TextBlob
from openai import OpenAI
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Create FastAPI app
app = FastAPI(title="Review Insight API")

# Allow local dev frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV
df = pd.read_csv("cleaned_customer_reviews.csv")

# Clean and preprocess
df = df.dropna(subset=["Product_Category", "Rating", "Shipping_Country", "Fulfillment_Status", "Order_Value", "Review_Content"])
df["sentiment"] = df["Review_Content"].apply(lambda t: TextBlob(t).sentiment.polarity)

# API input model
class QuestionRequest(BaseModel):
    question: str

# GPT query function
def ask_gpt(question, context_text):
    prompt = f"""
You are a skilled data analyst.

Using the following customer reviews dataset, answer the question.

DATA SAMPLE:
{context_text}

QUESTION:
{question}

Answer clearly and concisely. Use bullet points or summaries where appropriate.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.post("/ask")
def ask_user_question(request: QuestionRequest):
    # Sample data passed to GPT
    sample_df = df.copy()
    context = sample_df[["Product_Category", "Rating", "Shipping_Country", "Fulfillment_Status", "Order_Value", "Review_Content"]].to_csv(index=False)

    result = ask_gpt(request.question, context)
    return {"answer": result}
