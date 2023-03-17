import openai

def print_chatgpt_response(prompt="Generate 20 Multiple Choice Questions on Data Science with correct answers and wrong answers"):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {prompt}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Set up the OpenAI API client
    openai.api_key = "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"
    # openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    # prompt = "Generate 20 Multiple Choice Questions on Data Science with correct answers and wrong answers"

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
    # [response.split("\n")]
    gptResponse = [x for x in response.split("\n") if x.strip()]
    print("gptResponse", response)
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_chatgpt_response()

