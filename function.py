def ai():
    # 读取当前名字
    try:
        with open("ainame.txt", "r", encoding="utf-8") as f:
            ainame = f.read()
            if ainame:
                print("当前的名字为：" + ainame)
    except FileNotFoundError:
        print("未找到 ainame.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)
    ainame = input("请输入要修改的内容：(输入exit取消修改)")
    if ainame == "exit":
        return
    try:
        with open("ainame.txt", "w", encoding="utf-8") as f:
            f.write(ainame)
    except FileNotFoundError:
        print("未找到 ainame.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)


def user():
    # 读取当前名字
    try:
        with open("username.txt", "r", encoding="utf-8") as f:
            username = f.read()
            if username:
                print("当前的名字为：" + username)
    except FileNotFoundError:
        print("未找到 ainame.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)
    user_name = input("请输入要修改的内容：(输入exit取消修改)")
    if user_name == "exit":
        return
    try:
        with open("username.txt", "w", encoding="utf-8") as f:
            f.write(user_name)
    except FileNotFoundError:
        print("未找到 username.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)


def tianjiasheding():
    content = input("请输入要添加的内容：(输入exit取消修改)")
    if content == "exit":
        return
    try:
        with open("sheding.txt", "a", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError:
        print("未找到 sheding.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"追加内容时出错: {e}")


def chongxiesheding():
    content = input("请输入：(输入exit退出)")
    if content == "exit":
        return
    try:
        with open("sheding.txt", "w", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError:
        print("未找到 sheding.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"追加内容时出错: {e}")