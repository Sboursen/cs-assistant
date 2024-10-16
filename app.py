from services.open_ai_api import OpenAiApiClient
from services.open_web_ui_api import OpenWebUiApiClient

prompt = "The capital of France"
print(f"prompt: {prompt}")

# open_ai_client = OpenAiApiClient()
# response = open_ai_client.get_completion("The capital of France")
# print(f"OPENAI: {response}")

open_web_ui_client = OpenWebUiApiClient()
response = open_web_ui_client.get_completion("The capital of France")
print(f"OPEN WEBUI: {response}")
