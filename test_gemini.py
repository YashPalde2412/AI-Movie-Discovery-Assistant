from llm.gemini import GeminiClient

gemini = GeminiClient()

response = gemini.generate(
    "Say hello in one sentence."
)

print(response)