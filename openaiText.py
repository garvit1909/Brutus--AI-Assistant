import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a letter to the editor of a local newspaper",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

# 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
# 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
'''
{
  "id": "cmpl-7aj9eLj9HPdYo6JEpqXRUTM9XO344",
  "object": "text_completion",
  "created": 1688987738,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nDear Editor,\n\nI am writing to express my concern about the lack of public transportation in our community. As a resident of this area, I have noticed that there are very few options for people who do not have access to a car. This is especially true for those who are elderly",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 60,
    "total_tokens": 70
  }
}
'''
