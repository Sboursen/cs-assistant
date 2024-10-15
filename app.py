from services.open_ai_api import OpenAiApiClient

open_ai_client = OpenAiApiClient()
response = open_ai_client.get_completion("What is the capital of France?")
print(response)
