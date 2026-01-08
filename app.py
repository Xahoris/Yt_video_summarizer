"""
YouTube Video Summarizer
A Streamlit web application to summarize YouTube videos using AI.
"""
import os
import streamlit as st
from dotenv import load_dotenv
from src.youtube import extract_video_id, get_transcript
from src.summarizer import Summarizer

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥",
    layout="centered"
)

def main():
    """Main application logic."""
    
    # Title and description
    st.title("🎥 YouTube Video Summarizer")
    st.markdown("""
    Get AI-powered summaries of YouTube videos in seconds.  
    Simply paste a YouTube URL and click **Summarize**.
    """)
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        st.stop()
    
    # Initialize summarizer
    summarizer = Summarizer(api_key)
    
    # URL input
    st.markdown("---")
    url = st.text_input(
        "YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste any YouTube video URL here"
    )
    
    # Summarize button
    if st.button("Summarize"):
        if not url:
            st.warning("⚠️ Please enter a YouTube URL")
            return
        
        # Extract video ID
        with st.spinner("Extracting video ID..."):
            video_id = extract_video_id(url)
            if not video_id:
                st.error("❌ Invalid YouTube URL. Please check and try again.")
                return
        
        st.success(f"✅ Video ID: {video_id}")
        
        # Get transcript
        try:
            with st.spinner("Fetching transcript..."):
                transcript = get_transcript(video_id)
                st.success(f"✅ Transcript retrieved ({len(transcript)} characters)")
        except Exception as e:
            st.error(f"❌ {str(e)}")
            return
        
        # Generate summary
        try:
            with st.spinner("Generating summary with AI... This may take a moment."):
                summary = summarizer.summarize(transcript)
            
            # Display summary
            st.markdown("---")
            st.subheader("📝 Summary")
            st.markdown(summary)
            
            # Show transcript in expander
            with st.expander("📄 View Full Transcript"):
                st.text_area("Transcript", transcript, height=300, disabled=True)
                
        except Exception as e:
            st.error(f"❌ {str(e)}")
            return
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
        Powered by OpenAI GPT-4o mini | Built with Streamlit
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
