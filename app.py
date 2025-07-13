import streamlit as st
from modules.transcript_extractor import get_transcript
from modules.summarizer import summarize_text
from modules.qa_system import answer_question

st.title("📺 AI-Powered YouTube Summarizer & QA Bot (Multi-Language)")

video_id = st.text_input("Enter YouTube Video ID (e.g., dQw4w9WgXcQ):")

# Language selection
lang = st.selectbox("Select Transcript Language:", 
                    ["en - English", "hi - Hindi", "ta - Tamil", "te - Telugu", "bn - Bengali"])

# Extract language code (e.g., "en" from "en - English")
lang_code = lang.split(" - ")[0]

if video_id:
    with st.spinner(f"Fetching {lang.split(' - ')[1]} transcript..."):
        transcript = get_transcript(video_id, lang=lang_code)
    st.subheader("Transcript")
    st.write(transcript)

    if not transcript.startswith("Error"):
        with st.spinner("Generating Summary..."):
            summary = summarize_text(transcript)
        st.subheader("Summary")
        st.write(summary)

        question = st.text_input("Ask a question about the video:")

        if question:
            with st.spinner("Finding answer..."):
                answer = answer_question(question, transcript)
            st.subheader("Answer")
            st.write(answer)
