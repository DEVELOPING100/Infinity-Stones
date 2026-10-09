import os
from dotenv import load_dotenv

load_dotenv()

class Ghost:
    def __init__(self):
        self._setup_clients()

    def _setup_clients(self):
        # OpenAI
        import openai
        self.openai_client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Anthropic
        import anthropic
        self.anthropic_client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        # Gemini
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")

    def _ask_openai(self, query: str) -> str:
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": query}],
                max_tokens=400
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[GPT unavailable: {e}]"

    def _ask_anthropic(self, query: str) -> str:
        try:
            response = self.anthropic_client.messages.create(
                model="claude-haiku-5-5",
                max_tokens=400,
                messages=[{"role": "user", "content": query}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            return f"[Claude unavailable: {e}]"

    def _ask_gemini(self, query: str) -> str:
        try:
            response = self.gemini_model.generate_content(query)
            return response.text.strip()
        except Exception as e:
            return f"[Gemini unavailable: {e}]"

    def _merge(self, responses: dict, task_type: str) -> str:
        """
        Ghost Engine — merges model outputs based on task type.
        Each task type weights a different model as the primary source.
        """
        if task_type == "code":
            return (
                f"[Ghost — Code Mode: Leading with GPT]\n\n"
                f"{responses['openai']}\n\n"
                f"Claude adds: {responses['anthropic'][:150]}..."
            )
        elif task_type == "creative":
            return (
                f"[Ghost — Creative Mode: Leading with Claude]\n\n"
                f"{responses['anthropic']}\n\n"
                f"Gemini adds: {responses['gemini'][:150]}..."
            )
        elif task_type == "analytical":
            return (
                f"[Ghost — Analytical Mode: Leading with Gemini]\n\n"
                f"{responses['gemini']}\n\n"
                f"GPT adds: {responses['openai'][:150]}..."
            )
        else:
            return (
                f"[Ghost — General Mode: Synthesized]\n\n"
                f"GPT: {responses['openai'][:200]}...\n\n"
                f"Claude: {responses['anthropic'][:200]}...\n\n"
                f"Gemini: {responses['gemini'][:200]}..."
            )

    def route(self, query: str, task_type: str) -> dict:
        responses = {
            "openai":    self._ask_openai(query),
            "anthropic": self._ask_anthropic(query),
            "gemini":    self._ask_gemini(query),
        }
        responses["merged"] = self._merge(responses, task_type)
        return responses