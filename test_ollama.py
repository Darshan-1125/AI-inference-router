from app.services.ollama import OllamaService


ollama = OllamaService()

response = ollama.generate("What is binary search?")

print(response)
