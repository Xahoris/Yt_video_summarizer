"""
YouTube video handling module.
Extracts video IDs and retrieves transcripts.
"""
import re
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi


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

def get_transcript(video_id: str) -> str:
    """
    Retrieve transcript for a YouTube video.
    
    Args:
        video_id: YouTube video ID
        languages: List of preferred languages (default: ['en', 'fr'])
        
    Returns:
        Full transcript as a single string

"""
    #create instance of YouTubeTranscriptApi
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)

    # try fetching french 
    try:
        transcript = transcript_list.find_transcript(['fr'])
    except:
        print("No French transcript available")
    
    # try fetching english 
    try:
        transcript = transcript_list.find_transcript(['en'])
    except:
        print("No English transcript available")
        
    # Combine all transcript segments into one string
    transcript = transcript.fetch()
    transcript = transcript.to_raw_data()
    full_transcript = ' '.join([item['text'] for item in transcript])
    return full_transcript
        
