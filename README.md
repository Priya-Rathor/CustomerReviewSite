# 🧠 Customer Review Insight Assistant

This project is an **AI-powered customer review analysis tool** that cleans, processes, and transforms raw e-commerce reviews into actionable insights. It combines **data cleaning**, **exploratory analysis**, **FastAPI backend**, **GPT-4 analysis**, and a **responsive frontend** built with Tailwind CSS.

---

## 📊 Features

- 🧹 **Automated Data Cleaning** (Ratings, Categories, Timestamps, Fulfillment Status)
- 📈 **Visual Analysis** using Matplotlib and Seaborn
- 🧠 **Natural Language Question Answering** via GPT-4 API
- 🖼️ **Sentiment Scoring** using TextBlob
- ⚙️ **FastAPI Backend** to serve insights
- 🌐 **Interactive Frontend UI** (TailwindCSS + JavaScript)
- 📝 Filters for country, rating, and product category
- 📤 Clean dataset ready for ML/LLM input

---

## 🛠️ Tech Stack

| Component      | Technology                         |
|----------------|-------------------------------------|
| Backend        | Python, FastAPI, OpenAI API         |
| Data Cleaning  | Pandas, NumPy, Matplotlib, Seaborn  |
| Sentiment      | TextBlob                            |
| Frontend       | HTML, Tailwind CSS, Vanilla JS      |
| API Integration| Axios-like fetch logic (Mocked / Real) |
| AI Model       | GPT-4 via OpenAI API                |
| Deployment     | Localhost / Deployable via Render/Vercel |

---

## 🚀 How It Works

### 1. 🔍 Data Cleaning & Exploration
- Handled typos in `Product Category` and `Fulfillment Status`
- Imputed missing `Rating` and `Order Value` fields
- Filtered out low-quality or empty reviews
- Created a high-quality dataset (`cleaned_customer_reviews.csv`)
- Performed EDA: ratings, product distribution, trends

### 2. 🧠 AI Integration via FastAPI
- Users ask questions like:
  > “Which category has the most 1-star reviews in Canada?”
- GPT-4 processes a contextual sample of the cleaned dataset and returns a structured answer.
- Sentiment scores are also calculated using TextBlob.

### 3. 🌐 Frontend Web App
- Clean, responsive UI built with TailwindCSS
- Input fields for question, product, country, and rating filters
- Simulated GPT answers (replaceable with actual backend integration)
- Actions: refine question, show details, copy/export result

---

## 🖼️ Screenshots

### 🔎 Ask Insights
![screenshot1](docs/screenshot-question.png)

### 📊 Sample Insights
![screenshot2](docs/screenshot-answer.png)

---

## 🗂️ Project Structure

```

project/
├── app.py                       # FastAPI backend (AI Q\&A API)
├── index.html                   # Tailwind CSS UI
├── cleaned\_customer\_reviews.csv # Final clean dataset
├── sample\_customer.csv          # Raw sample data
├── analysis.ipynb               # Full data cleaning + visualization
├── .env                         # OpenAI API key

````

---

## 🧪 Sample Questions

Try asking:
- *"Which product categories have the most returns?"*
- *"Average order value for 5-star reviews in the US?"*
- *"Trends in delayed orders over months?"*

---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourname/customer-review-assistant.git
cd customer-review-assistant
````

2. **Install backend dependencies**

```bash
pip install -r requirements.txt
```

3. **Add OpenAI API key**

```bash
echo OPENAI_API_KEY=your_key_here > .env
```

4. **Run FastAPI backend**

```bash
uvicorn app:app --reload
```

5. **Open `index.html` in browser**

> For full integration, replace mock responses in `simulateApiCall()` with a real `fetch("/ask", ...)` call.

---

## ✅ Final Summary

| Metric                    | Value    |
| ------------------------- | -------- |
| Total Original Reviews    | 100      |
| Cleaned High-Quality Data | 72       |
| Avg Rating                | 2.81     |
| Avg Order Value           | \$287.64 |
| Categories Standardized   | 6        |
| Sentiment Analysis Ready  | ✅        |
| LLM Analysis Ready        | ✅        |

---

