import openai
from chatgpt.core.prompt_generation_processor import PromptCreationProcessor

class OpenAPIResponseGenerationProcessor:
    """Get chat response based on chat message User Provided."""

    def __init__(self):
        pass

    def get_openai_response(self, deployment_name, system_mesage, messages):
        """Get Chat Response based on chat message User Provided."""

        # create prompt from system message and user messages.
        create_prompt = PromptCreationProcessor()
        promp_message = create_prompt.create_prompt(system_mesage, messages)

        # creating list of response messages to track chat conversation.
        response = openai.Completion.create(
                    engine=deployment_name,
                    prompt= promp_message,
                    temperature=0.2,
                    max_tokens=2046,
                    top_p=0.95,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=["<|im_end|>"])

        # return response text to user.
        return response['choices'][0]['text'].strip()