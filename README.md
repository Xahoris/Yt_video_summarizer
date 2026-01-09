# YouTube Video Summarizer

An AI-powered web application that automatically generates concise summaries of YouTube videos based on their transcripts.

## 🎯 Features

- Extract video information from YouTube URLs
- Retrieve video transcripts (English and French)
- Generate AI-powered summaries using OpenAI GPT-4o mini
- Clean and intuitive web interface built with Streamlit
- Docker support for easy deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.9.7
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Local Installation

1. **Clone the repository**
   ```bash
   cd Yt_video_summarizer
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will open in your browser at `http://localhost:8501`

### Docker Execution

1. **Build the Docker image**
   ```bash
   docker build -t yt-summarizer .
   ```

2. **Run the container**
   Use docker desktop, extensions to run the container  or type : 
   ```bash
   docker run -p 8501:8501 --env OPENAI_API_KEY=your_api_key_here yt-summarizer
   ```


3. **Access the application**
   
   Open your browser and go to `http://localhost:8501`

## 📖 Usage

1. Open the application in your browser
2. Paste a YouTube video URL in the input field
3. Click the **Summarize** button
4. Wait for the AI to generate the summary
5. Read the concise summary and optionally view the full transcript

### Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

## 🏗️ Project Structure

```
Yt_video_summarizer/
├── app.py                 # Main Streamlit application
├── src/
│   ├── __init__.py        # Package initialization
│   ├── youtube.py         # YouTube URL and transcript handling
│   ├── summarizer.py      # OpenAI summarization logic
│   └── prompts.py         # LLM prompt templates
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .env.example          # Environment variables template
└── README.md             # This file
```

## ⚠️ Limitations

- Only works with videos that have transcripts enabled
- Currently supports English and French transcripts
- Requires an active OpenAI API key
- Very long videos may take longer to process
- No persistent storage of summaries

## 📧 Support

For issues please check that:
- Your OpenAI API key is valid and has credits
- The YouTube video has transcripts enabled
- Your URL format is supported

##  Miscs

Your can put your own prompt insite the prompts.py file 

---

**Made by Xahoris**

