import openai

# Set up the OpenAI API client
openai.api_key = "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"
# model_engine = "gpt-3.5-turbo" 

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "i have a questiion"

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
print(response)
