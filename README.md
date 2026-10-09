# ♾️ Infinity Stones — Multi-Model AI Router

A Python CLI tool that simultaneously queries OpenAI GPT, 
Anthropic Claude, and Google Gemini — then merges their 
responses using the **Ghost engine** based on task type.

## How it works
- **Code** queries → GPT leads
- **Creative** queries → Claude leads  
- **Analytical** queries → Gemini leads
- **General** queries → all three synthesized

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env  # add your API keys
python main.py
```

## Tech Stack
Python · OpenAI API · Anthropic Claude API · Google Gemini API

## Ghost Engine
The Ghost engine is the core orchestrator — it classifies 
each query by task type and weights model responses 
accordingly, merging outputs into one unified answer.