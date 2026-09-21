# financial-services-ai-assistant

An AI-powered chatbot that helps customers with common financial-services questions related to banking, credit cards, loans, EMI, fees, eligibility, payments, and financial security.

## Features

* 🏦 Banking-related support
* 💳 Credit card information
* 💰 Loans and EMI guidance
* 💵 Fees and charges information
* 📋 Eligibility and document-related questions
* 💳 Payment and repayment guidance
* 🔐 Financial security guidance
* 🧠 Conversation memory for follow-up questions
* 💬 Chat history displayed in the Streamlit interface
* 🛡️ Domain guardrails to keep responses within financial services

## Technologies Used

* Python
* OpenAI API
* LangChain
* Streamlit
* Python-dotenv

## Project Structure

financial-services-ai-assistant/
│
├── app.py
├── Financial Chatbot.txt
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## How to Run

### 1. Clone the repository

git clone <your-repository-url>
cd financial-services-ai-assistant

### 2. Create and activate a virtual environment

python -m venv myvenv
myvenv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add your OpenAI API key

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

### 5. Run the application

streamlit run app.py

## Example Questions

* What is an EMI?
* What is a credit card?
* What is a loan processing fee?
* What are the eligibility criteria for a personal loan?
* How can I make my loan payment?
* What happens if I miss an EMI?

https://github.com/user-attachments/assets/50cc74e0-bab4-4716-a004-d355b20238ba





## Scope & Safety

This chatbot provides general financial-services information. It does not provide personalized investment advice and does not request or handle passwords, PINs, OTPs, CVV, or card numbers.

## Future Enhancement

After implementing RAG, the chatbot can be extended to provide answers grounded in specific bank and financial-product documents.

## Author

**Rudra**
