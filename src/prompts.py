"""
Prompt templates for LLM summarization.
"""

SYSTEM_PROMPT = """You are an expert at analyzing and summarizing video content. 
Your task is to create concise, well-structured summaries that capture the key points 
and main ideas of video transcripts."""

USER_PROMPT_TEMPLATE = """Please analyze the following video transcript and create a comprehensive summary.

The summary should:
- Be concise but capture all key points
- Be structured with clear sections or bullet points
- Highlight the main ideas and important details
- Be easy to read and understand

Transcript:
{transcript}

Please provide a well-structured summary:"""


def get_summary_prompt(transcript: str) -> tuple[str, str]:
    """
    Generate system and user prompts for video summarization.
    
    Args:
        transcript: The video transcript to summarize
        
    Returns:
        Tuple of (system_prompt, user_prompt)
    """
    user_prompt = USER_PROMPT_TEMPLATE.format(transcript=transcript)
    return SYSTEM_PROMPT, user_prompt
