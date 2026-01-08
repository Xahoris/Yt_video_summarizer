"""
YouTube video handling module.
Extracts video IDs and retrieves transcripts.
"""
import re
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url: str) -> Optional[str]:
    """
    Extract YouTube video ID from various URL formats.
    
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/watch?v=VIDEO_ID&other_params
    
    Args:
        url: YouTube video URL
        
    Returns:
        Video ID if found, None otherwise
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([\w-]+)',
        r'(?:youtu\.be\/)([\w-]+)',
        r'(?:youtube\.com\/embed\/)([\w-]+)',
        r'(?:youtube\.com\/v\/)([\w-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def get_transcript(video_id: str, languages: list = ['en', 'fr']) -> str:
    """
    Retrieve transcript for a YouTube video.
    
    Args:
        video_id: YouTube video ID
        languages: List of preferred languages (default: ['en', 'fr'])
        
    Returns:
        Full transcript as a single string
        
    Raises:
        TranscriptsDisabled: When transcripts are disabled for the video
        NoTranscriptFound: When no transcript is available in specified languages
        Exception: For other errors during transcript retrieval
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, 
            languages=languages
        )
        
        # Combine all transcript segments into one string
        full_transcript = ' '.join([entry['text'] for entry in transcript_list])
        return full_transcript
        
    except TranscriptsDisabled:
        raise Exception(f"Transcripts are disabled for video {video_id}")
    except NoTranscriptFound:
        raise Exception(f"No transcript found in languages {languages} for video {video_id}")
    except Exception as e:
        raise Exception(f"Error retrieving transcript: {str(e)}")
