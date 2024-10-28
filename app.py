from services.open_web_ui_api import OpenWebUiApiClient

# open_ai_client = OpenAiApiClient()
# response = open_ai_client.get_completion("The capital of France")
# print(f"OPENAI: {response}")

open_web_ui_client = OpenWebUiApiClient()
DELIMITER = "######"
system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{DELIMITER} characters.
Classify each query into a primary category \
and a secondary category.
Provide your output in json format with the \
keys: primary and secondary.

# Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

# Secondary categories for each primary category:
## Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

## Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

## Account Management secondary categories:
Password reset
Update personal information
Close account
Account security

## General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human

"""
USER_MESSAGE = "I want you to delete my profile and all of my user data"
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"{DELIMITER}{USER_MESSAGE}{DELIMITER}"},
]
response = open_web_ui_client.get_completion_from_messages(
    messages
)
print(response)
