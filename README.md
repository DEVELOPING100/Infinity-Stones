<<<<<<< HEAD
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
=======
# Infinity-Stones
>>>>>>> 313d17edc00a3c73755a4b2e85856472e6153d6a
# ♾️ Infinity Stones — Multi-Model AI Router

> *What if you didn't have to choose between AI models?*

Infinity Stones is a Python CLI tool that routes your queries across **OpenAI GPT**, **Anthropic Claude**, and **Google Gemini** simultaneously — then merges their responses into one unified answer using the **Ghost engine**.

Instead of switching between AI platforms manually, Infinity Stones picks the best model for your task and synthesizes the results automatically.

---

## 🧠 How the Ghost Engine Works

The **Ghost engine** is the core orchestrator of Infinity Stones. It classifies each query by task type and weights model responses based on each model's known strengths:

| Task Type | Primary Model | Why |
|-----------|--------------|-----|
| 💻 Code | GPT-4o | Strong at structured logic and syntax |
| ✍️ Creative | Claude | Nuanced, expressive writing |
| 📊 Analytical | Gemini | Strong at research and reasoning |
| 🌐 General | All three | Synthesized for balanced output |

Ghost doesn't just pick one model — it queries all three in parallel and merges the outputs, giving you the best of each.

---

## ⚡ Features

- Routes queries across 3 LLMs simultaneously
- Classifies task type automatically
- Ghost engine merges responses based on model strengths
- Clean CLI interface with labeled outputs
- Graceful error handling if any model is unavailable

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| LLM APIs | OpenAI API, Anthropic Claude API, Google Gemini API |
| Orchestration | Ghost Engine (custom) |
| Config | python-dotenv |

---

## 🚀 Setup

```bash
# 1. Clone the repo
git clone https://github.com/DEVELOPING100/Infinity-Stones.git
cd Infinity-Stones

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API keys
cp .env.example .env

# 4. Run it
python main.py
```

---

## 🔑 Environment Variables

Create a `.env` file based on `.env.example`:

OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GEMINI_API_KEY=your_gemini_key


Get your keys here:
- OpenAI → [platform.openai.com](https://platform.openai.com)
- Anthropic → [console.anthropic.com](https://console.anthropic.com)
- Gemini → [aistudio.google.com](https://aistudio.google.com)

---

## 📁 Project Structure

infinity-stones/
├── main.py # CLI entry point
├── ghost.py # Ghost engine — routing and merging logic
├── requirements.txt # Dependencies
├── .env.example # Environment variable template
└── README.md


---

## 💡 Motivation

Most AI tools lock you into one model. Infinity Stones was built on a simple idea — different models have different strengths, and the best answer often lives across all of them. The Ghost engine makes that seamless.

---

## 🔮 Planned Features

- [ ] Slider UI to manually weight model responses (Infinity Stones concept)
- [ ] Save and export session outputs
- [ ] Web interface
- [ ] Token usage and cost tracking per query

---

## 👤 Author

**David Oyedepo**
[linkedin.com/in/david-oyedepo](https://linkedin.com/in/david-oyedepo) · [github.com/DEVELOPING100](https://github.com/DEVELOPING100)