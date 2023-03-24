import json
import openai

def get_data_api_response():
    """Get data Object from data api response"""

    # data object. Pass Json Data Object getting from Data Response used to test chat gpt scnearios.
    data_obj = {} 
        
    # Convert JSON object to string  
    json_str = json.dumps(data_obj)

    return json_str

def create_prompt(system_message, messages):
    """Created Prompt message from User Input."""

    prompt = system_message
    message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
    for message in messages:
            prompt += message_template.format(message['sender'], message['text'])
    prompt += "\n<|im_start|>assistant\n"
    return prompt

def get_openai_response(deployment_name, system_mesage, messages):
    """Get Chat Response based on chat message User Provided."""

    # create prompt from system message and user messages.
    promp_message = create_prompt(system_mesage, messages)

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

def main(chat_input):
    """Get Chat Response based on Chat Input from OpenAI"""

    # setting open ai configurations. Pass in open ai api key, resource name, and model deployment name.
    openai.api_key = ""
    openai.api_base =  f"https://{api_resource_name}.openai.azure.com/"
    openai.api_type = 'azure'
    openai.api_version = '2022-12-01'
    deployment_name= ""

    # configure system message & usage message.
    system_message_template = "<|im_start|>Assistant\n{}\n<|im_end|>"
    system_message = system_message_template.format(f"{system_message}")

    # get data response based on user input used to format messages passing into creating open ai response.
    data_response = get_data_api_response()

    # format use message to pass into openAi and generate chat response.
    messages = [{"sender":"user","text": f"{chat_input} from {data_response}"}]

    # generate chat reponse.
    response = get_openai_response(deployment_name, system_message, messages)

    return response

if __name__ == "__main__":
    # user message input.
    chat_input = f"{user_input}"

    # get chat output and return to user.
    chat_output = main(chat_input)
    print(chat_output)





