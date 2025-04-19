import json
from openai import OpenAI
from config import *

# 初始化 OpenAI 客户端
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

try:
    # 读取系统设定文件
    with open("sheding.txt", "r", encoding="utf-8") as f:
        sheding = f.read()
except FileNotFoundError:
    print("未找到 sheding.txt 文件，请检查文件路径。")
    exit(1)

try:
    # 读取历史记录文件
    with open("lishi.json", "r", encoding="utf-8") as f:
        messages = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # 如果文件不存在或解析失败，初始化消息列表
    messages = [{"role": "system", "content": sheding}]

while True:
    user_input = input("You:")
    if user_input == "再见啦":
        print("(挥挥手)再见啦...")
        break

    # 添加用户消息到消息列表
    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)

    try:
        # 调用 OpenAI API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=1.3,
            stream=False
        )
        # 打印响应内容
        print(response.choices[0].message.content)
        # 添加响应消息到消息列表
        messages.append(response.choices[0].message.model_dump())
    except Exception as e:
        print(f"请求出错: {e}")
        continue

    try:
        # 将更新后的消息列表保存到历史记录文件
        with open("lishi.json", "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"保存历史记录出错: {e}")
    print(response.usage.total_tokens)