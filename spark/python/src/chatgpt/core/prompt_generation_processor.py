class PromptCreationProcessor:
    """Create prompt message from user input."""

    def __init__(self):
        pass

    def create_prompt(self, system_message, messages):
        """Create prompt message from user input."""

        prompt = system_message
        message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
        for message in messages:
            prompt += message_template.format(message['sender'], message['text'])
        prompt += "\n<|im_start|>assistant\n"
        return prompt