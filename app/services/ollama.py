import requests


class OllamaService:

    def __init__(self):
        self.base_url = "http://localhost:11434"
        self.model = "gemma3:4b"

    def generate(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]