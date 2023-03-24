# PoCforChatGPT

## Installation
openai

# Azure Resources
Azure Open AI
GPT Model Deployment

# Steps
Pass in configured open ai resource name, api key, and gpt model deployment name from main.py.
Pass in user input as parameter to main.py to start generate open ai response.
    1. Based on user input, get matching data content reponse. For this example, data object can be passed in directly from get_data_api_reponse() to test gpt features. This function can be customized based on requirements.
    2. Applying user input and data content response to create prompt message.
    3. Using prompt message to call get_openai_response() to get chat response.
 
