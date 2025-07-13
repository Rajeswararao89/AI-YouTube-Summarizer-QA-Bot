🎥 AI-Powered YouTube Summarizer & Question Answering Bot
AI-Youtube-Summarizer-QA-Bot is an NLP-powered tool that allows users to:

Extract transcripts from YouTube videos (supports multiple languages)

Summarize long-form content into concise highlights

Ask questions about the video and get precise answers

This project combines LLMs, extractive QA, and summarization pipelines to make YouTube content easily accessible.

🚀 Features
✅ YouTube Transcript Extraction
✅ Multi-language Support (English, Hindi, Tamil, Telugu, Bengali)
✅ AI Summarization using facebook/bart-large-cnn
✅ Question Answering via distilbert-base-cased-distilled-squad
✅ Streamlit-based User Interface

🛠️ Tech Stack
Task	Technology
Transcript Fetching	youtube-transcript-api
Summarization	transformers - BART
QA System	transformers - DistilBERT
UI	Streamlit
Optional Enhancements	LangChain, FAISS

🔧 Installation
Clone the Repository
bash
Copy
Edit
git clone https://github.com/Rajeswararao89/AI-YouTube-Summarizer-QA-Bot.git
cd AI-YouTube-Summarizer-QA-Bot
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
💻 Usage
Run Locally
bash
Copy
Edit
streamlit run app.py
🌐 Streamlit Cloud Deployment
You can deploy this project easily on Streamlit Cloud:

Push this repo to GitHub

Go to Streamlit Cloud and click New App

Select your repo and set app.py as the entry point

Deploy in one click

🎯 How It Works
User inputs YouTube video ID

Select transcript language (English, Hindi, Tamil, Telugu, Bengali)

Pipeline fetches transcript using youtube-transcript-api

Summarization happens using BART (facebook/bart-large-cnn)

User asks questions → Bot answers using DistilBERT QA pipeline

📄 Example
Input:
YouTube Video ID: dQw4w9WgXcQ

Language: English

Question: "What is the main topic of the video?"

Output:
Transcript: Fetched

Summary: Short version of the video content

Answer: Accurate response based on transcript

🗂️ Project Structure
bash
Copy
Edit
AI-YouTube-Summarizer-QA-Bot/
│
├── app.py               # Streamlit app entry point
├── requirements.txt     # Python dependencies
├── modules/
│   ├── transcript_extractor.py
│   ├── summarizer.py
│   └── qa_system.py
⚙️ Future Enhancements
Automatic language detection

Long video chunking with LangChain

Vector search with FAISS for better QA

Docker deployment

📢 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss your ideas.

📄 License
This project is licensed under the MIT License.

🔗 GitHub Repo:
https://github.com/Rajeswararao89/AI-YouTube-Summarizer-QA-Bot

🔗 Live App:
https://ai-youtube-summarizer-app-bot-lh6jdtugr9o5b7j4ldgv5v.streamlit.app/
