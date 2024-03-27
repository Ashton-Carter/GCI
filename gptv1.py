from openai import OpenAI


api_key = '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'
prompt = 'Given the following paragraph, please read through each sentence. For each sentence, determine if it contains a claim. If a sentence contains a claim, state whether the claim is true or false based on general knowledge. If the claim is false, please provide a reason why it is false. If there isn\'t a claim in the sentence, state \"Not a claim.\" '
inp = "Harry Potter is the main character in the film Harry Potter.  Voldemort is Harrys companion. Severous is a bad guy."
client = OpenAI(api_key=api_key)

print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt + inp,
        },
    ],
)
print(completion.choices[0].message.content)