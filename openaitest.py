import openai
import os
from config import apikey

openai.api_key = apikey

import openai
import os
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are an AI assistant that helps users write resignation emails to their bosses."
    },
    {
      "role": "user",
      "content": "Write an email to the boss for my resignation."
    }
  ],
  temperature=0.7,  # Adjust temperature as needed for desired randomness.
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Print the generated email content
print(response)
'''
"choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Resignation - [Your Name]\n\nDear [Boss's Name],\n\nI hope this email finds you well. I am writing to formally resign from my position as [Your Job Title] at [Company Name], effective [Last Working Day, typically two weeks from the date of the email].\n\nI have thoroughly considered this decision and it was not an easy one to make. However, after careful thought and reflection, I have decided that it is time for me to explore new opportunities and challenges in my career.\n\nI want to express my gratitude for the opportunities and experiences I have gained while working at [Company Name]. The past [duration of employment] has been invaluable in terms of professional growth, skill development, and personal achievements. I am grateful for the support, guidance, and mentorship provided by you and the entire team. The knowledge and insights I have gained during my time here will undoubtedly contribute to my future endeavors.\n\nI am committed to ensuring a smooth transition during my departure. I am more than willing to assist in training my replacement or any other tasks that will help facilitate the transition process. Please let me know how I can be of assistance during this time.\n\nI would also like to take this opportunity to express my sincere appreciation for the positive work environment, camarader"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 36,
    "completion_tokens": 256,
    "total_tokens": 292
  }
}

'''
