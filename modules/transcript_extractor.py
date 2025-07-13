from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, lang="en"):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        text = " ".join([item['text'] for item in transcript])
        return text
    except Exception as e:
        return f"Error fetching transcript: {e}"

