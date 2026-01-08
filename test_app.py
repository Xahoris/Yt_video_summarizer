"""
Simple test script for YouTube Video Summarizer
Tests core functionality without requiring manual UI interaction
"""
import os
from dotenv import load_dotenv
from src.youtube import extract_video_id, get_transcript
from src.summarizer import Summarizer

# Load environment variables
load_dotenv()

def test_video_id_extraction():
    """Test YouTube video ID extraction from various URL formats."""
    print("Testing Video ID Extraction...")
    
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=share",
        "https://www.youtube.com/embed/dQw4w9WgXcQ"
    ]
    
    expected_id = "dQw4w9WgXcQ"
    
    for url in test_urls:
        video_id = extract_video_id(url)
        status = "✓" if video_id == expected_id else "✗"
        print(f"  {status} {url} -> {video_id}")
    
    print()

def test_invalid_url():
    """Test that invalid URLs return None."""
    print("Testing Invalid URL Handling...")
    
    invalid_urls = [
        "https://www.google.com",
        "not a url",
        ""
    ]
    
    for url in invalid_urls:
        video_id = extract_video_id(url)
        status = "✓" if video_id is None else "✗"
        print(f"  {status} Invalid URL: '{url}' -> {video_id}")
    
    print()

def test_transcript_retrieval():
    """Test transcript retrieval for a known video."""
    print("Testing Transcript Retrieval...")
    
    # Using a popular tech video that should have transcripts
    # Example: "What is Python?" by Programming with Mosh (short video)
    test_video_id = "Y8Tko2YC5hA"  # Replace with a known video with transcript
    
    try:
        transcript = get_transcript(test_video_id)
        print(f"  ✓ Retrieved transcript: {len(transcript)} characters")
        print(f"  Preview: {transcript[:100]}...")
        return transcript
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None
    
    print()

def test_summarization(transcript=None):
    """Test AI summarization."""
    print("Testing AI Summarization...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("  ✗ OpenAI API key not found")
        return
    
    if not transcript:
        # Use a sample transcript if none provided
        transcript = """
        Hello everyone, welcome to this tutorial on Python programming.
        Today we'll learn about variables and data types.
        Python is a high-level programming language that's easy to learn.
        Variables in Python don't need explicit declaration.
        You can store numbers, strings, and other data types.
        Let's start with some examples.
        """
    
    try:
        summarizer = Summarizer(api_key)
        summary = summarizer.summarize(transcript)
        print(f"  ✓ Summary generated: {len(summary)} characters")
        print(f"  Summary:\n{summary}")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    print()

def main():
    """Run all tests."""
    print("=" * 60)
    print("YouTube Video Summarizer - Test Suite")
    print("=" * 60)
    print()
    
    # Run tests
    test_video_id_extraction()
    test_invalid_url()
    transcript = test_transcript_retrieval()
    
    # Only test summarization if we successfully got a transcript
    if transcript:
        test_summarization(transcript[:1000])  # Use first 1000 chars to save API costs
    else:
        print("Skipping summarization test (no transcript available)\n")
    
    print("=" * 60)
    print("Tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
