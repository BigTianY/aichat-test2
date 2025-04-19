# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from config import *

client = OpenAI(api_key=DEEKSEEP_API_KEY, base_url="https://api.deepseek.com")

with open("sheding.txt", "r", encoding="utf-8") as f:
    sheding = f.read()

messages = [{"role": "system", "content": sheding}]

while True:
    user_input = input("You:")
    if user_input == "再见啦":
        print("(挥挥手)再见啦...")
        break
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=1.3,
        stream=False
    )

    print(response.choices[0].message.content)
    messages.append(response.choices[0].message)