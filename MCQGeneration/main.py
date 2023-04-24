import openai
from utils import SQLiteDBOps
from textFileParser import gptResponseParser


# def print_chatgpt_response(prompt="Generate 5 easy, medium and hard Multiple Choice Questions on Data Science with correct answers and wrong answers with difficulty level"):
def print_chatgpt_response(prompt="Generate 5 medium Multiple Choice Questions on Data Science with correct answers and wrong answers"):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {prompt}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Set up the OpenAI API client
    openai.api_key = "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"
    # openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    # prompt = "Generate 20 Multiple Choice Questions on Data Science with correct answers and wrong answers"
    level = "medium"
    topic = "data science"
    prompt = "Generate 5 " + level + "Multiple Choice Questions on " + topic + " with correct answers and wrong answers"
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print("Actual Response = ", response)
    gptResponseParser(response, topic, level)
    print("gptResponse", response)
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_chatgpt_response()

