import tkinter as tk
from tkinter import messagebox
import json
from openai import OpenAI
from config import *

# 原有的功能函数
def ai():
    try:
        with open("config/ainame.txt", "r", encoding="utf-8") as f:
            ainame = f.read()
            if ainame:
                messagebox.showinfo("当前名字", f"当前的名字为：{ainame}")
    except FileNotFoundError:
        messagebox.showerror("错误", "未找到 ainame.txt 文件，请检查文件路径。")
        return
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时出现错误: {e}")
        return
    new_ainame = input_box_ai.get()
    if new_ainame:
        try:
            with open("config/ainame.txt", "w", encoding="utf-8") as f:
                f.write(new_ainame)
            messagebox.showinfo("成功", "AI 名字修改成功！")
        except FileNotFoundError:
            messagebox.showerror("错误", "未找到 ainame.txt 文件，请检查文件路径。")
        except Exception as e:
            messagebox.showerror("错误", f"读取文件时出现错误: {e}")

def user():
    try:
        with open("config/username.txt", "r", encoding="utf-8") as f:
            username = f.read()
            if username:
                messagebox.showinfo("当前名字", f"当前的名字为：{username}")
    except FileNotFoundError:
        messagebox.showerror("错误", "未找到 username.txt 文件，请检查文件路径。")
        return
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时出现错误: {e}")
        return
    new_username = input_box_user.get()
    if new_username:
        try:
            with open("config/username.txt", "w", encoding="utf-8") as f:
                f.write(new_username)
            messagebox.showinfo("成功", "用户名字修改成功！")
        except FileNotFoundError:
            messagebox.showerror("错误", "未找到 username.txt 文件，请检查文件路径。")
        except Exception as e:
            messagebox.showerror("错误", f"读取文件时出现错误: {e}")

def tianjiasheding():
    content = input_box_add_setting.get()
    if content:
        try:
            with open("config/sheding.txt", "a", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("成功", "设定添加成功！")
        except FileNotFoundError:
            messagebox.showerror("错误", "未找到 sheding.txt 文件，请检查文件路径。")
        except Exception as e:
            messagebox.showerror("错误", f"追加内容时出错: {e}")

def chongxiesheding():
    content = input_box_rewrite_setting.get()
    if content:
        try:
            with open("config/sheding.txt", "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("成功", "设定重写成功！")
        except FileNotFoundError:
            messagebox.showerror("错误", "未找到 sheding.txt 文件，请检查文件路径。")
        except Exception as e:
            messagebox.showerror("错误", f"追加内容时出错: {e}")

def duihua():
    # 初始化 OpenAI 客户端
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    try:
        with open("config/sheding.txt", "r", encoding="utf-8") as f:
            sheding = f.read()
    except FileNotFoundError:
        messagebox.showerror("错误", "未找到 sheding.txt 文件，请检查文件路径。")
        return

    try:
        with open("config/lishi.json", "r", encoding="utf-8") as f:
            messages = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = [{"role": "system", "content": sheding}]

    try:
        with open("config/ainame.txt", "r", encoding="utf-8") as f:
            ainame = f.read()
    except FileNotFoundError:
        messagebox.showerror("错误", "未找到 ainame.txt 文件，请检查文件路径。")
        return
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时出现错误: {e}")
        return

    try:
        with open("config/username.txt", "r", encoding="utf-8") as f:
            username = f.read()
    except FileNotFoundError:
        messagebox.showerror("错误", "未找到 username.txt 文件，请检查文件路径。")
        return
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时出现错误: {e}")
        return

    user_input = input_box_chat.get()
    if user_input:
        messages.append({"role": "user", "content": user_input})
        try:
            stream = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=1.3,
                stream=True
            )
            full_response = []
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response.append(content)
            ai_content = "".join(full_response)
            messages.append({"role": "assistant", "content": ai_content})
            chat_history.insert(tk.END, f"{username}：{user_input}\n")
            chat_history.insert(tk.END, f"{ainame}：{ai_content}\n")

            max_history = 50 * 2
            if len(messages) > max_history + 1:
                messages = [messages[0]] + messages[-max_history:]

            try:
                with open("config/lishi.json", "w", encoding="utf-8") as f:
                    json.dump(messages, f, ensure_ascii=False, indent=4)
            except Exception as e:
                messagebox.showerror("错误", f"保存历史记录出错: {e}")
        except Exception as e:
            messagebox.showerror("错误", f"\n请求出错: {e}")

# 创建主窗口
root = tk.Tk()
root.title("AI 聊天应用")

# 标签和输入框 - 修改 AI 名字
label_ai = tk.Label(root, text="修改 AI 名字：")
label_ai.pack()
input_box_ai = tk.Entry(root)
input_box_ai.pack()
button_ai = tk.Button(root, text="确认修改", command=ai)
button_ai.pack()

# 标签和输入框 - 修改用户名字
label_user = tk.Label(root, text="修改用户名字：")
label_user.pack()
input_box_user = tk.Entry(root)
input_box_user.pack()
button_user = tk.Button(root, text="确认修改", command=user)
button_user.pack()

# 标签和输入框 - 添加设定
label_add_setting = tk.Label(root, text="添加设定：")
label_add_setting.pack()
input_box_add_setting = tk.Entry(root)
input_box_add_setting.pack()
button_add_setting = tk.Button(root, text="确认添加", command=tianjiasheding)
button_add_setting.pack()

# 标签和输入框 - 重写设定
label_rewrite_setting = tk.Label(root, text="重写设定：")
label_rewrite_setting.pack()
input_box_rewrite_setting = tk.Entry(root)
input_box_rewrite_setting.pack()
button_rewrite_setting = tk.Button(root, text="确认重写", command=chongxiesheding)
button_rewrite_setting.pack()

# 聊天输入框和按钮
label_chat = tk.Label(root, text="聊天输入：")
label_chat.pack()
input_box_chat = tk.Entry(root)
input_box_chat.pack()
button_chat = tk.Button(root, text="发送", command=duihua)
button_chat.pack()

# 聊天历史显示框
chat_history = tk.Text(root, height=10, width=50)
chat_history.pack()

# 运行主循环
root.mainloop()