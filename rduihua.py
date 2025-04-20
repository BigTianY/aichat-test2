import json
from openai import OpenAI
from config import *



def rduihua():
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

    # 获取ainame
    try:
        with open("ainame.txt", "r", encoding="utf-8") as f:
            ainame = f.read()

    except FileNotFoundError:
        print("未找到 ainame.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)

    # 获取username
    try:
        with open("username.txt", "r", encoding="utf-8") as f:
            username = f.read()

    except FileNotFoundError:
        print("未找到 username.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)

    while True:
        user_input = input(username + "：")
        if user_input == "再见啦":
            # 退出前保存历史记录（保持原逻辑）
            print("(挥挥手)再见啦...")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            # 关键修改：启用流式传输
            stream = client.chat.completions.create(
                model="deepseek-reasoner",
                messages=messages,
                #此项目在思考模型中无法使用
                #temperature=1.3,
                stream=True  # 启用流式
            )

            # 流式接收响应
            full_response = []
            print("<think>", end="", flush=True)
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta:
                    if chunk.choices[0].delta.reasoning_content:
                        rcontent = chunk.choices[0].delta.reasoning_content
                        print(rcontent, end="", flush=True)  # 实时输出
                        # reasoning_content.append(rcontent)
                    if chunk.choices and chunk.choices[0].delta.content:
                        print("<think>\n" + ainame + ": ", end="")
                        content = chunk.choices[0].delta.content
                        print(content, end="", flush=True)
                        break
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta:
                    if chunk.choices[0].delta.content:  # 检查是否有内容
                        content = chunk.choices[0].delta.content
                        print(content, end="", flush=True)  # 实时输出
                        full_response.append(content)
            ai_content = "".join(full_response)
            print()  # 换行
            messages.append({"role": "assistant", "content": ai_content})
        except Exception as e:
            print(f"\n请求出错: {e}")
            continue

        # 添加历史记录截断逻辑
        max_history = 50 * 2  # 50轮用户+助手消息
        if len(messages) > max_history + 1:  # +1 保留系统消息
            messages = [messages[0]] + messages[-max_history:]

        try:
            # 将更新后的消息列表保存到历史记录文件
            with open("lishi.json", "w", encoding="utf-8") as f:
                json.dump(messages, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存历史记录出错: {e}")