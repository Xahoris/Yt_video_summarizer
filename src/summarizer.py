"""
AI summarization module using OpenAI API.
"""
import os
from openai import OpenAI
from src.prompts import get_summary_prompt


class Summarizer:
    """Handles video transcript summarization using OpenAI's GPT-4o mini."""
    
    def __init__(self, api_key: str):
        """
        Initialize the summarizer with OpenAI API key.
        
        Args:
            api_key: OpenAI API key
        """
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        self.temperature = 0.3  # Low temperature for deterministic output
    
    def summarize(self, transcript: str) -> str:
        """
        Generate a summary of the video transcript.
        
        Args:
            transcript: Full video transcript text
            
        Returns:
            Generated summary
            
        Raises:
            Exception: If API call fails
        """
        try:
            system_prompt, user_prompt = get_summary_prompt(transcript)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=self.temperature
            )
            
            summary = response.choices[0].message.content
            return summary
            
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")
