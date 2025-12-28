import google.generativeai as genai

class GeminiEngine:
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            if not response or not response.text:
                return "I couldn't generate a response."
            return response.text.strip()
        except Exception as e:
            return f" Error communicating with Gemini API: {str(e)}"
