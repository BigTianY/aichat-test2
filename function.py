def ai():
    ainame = input("请输入要修改的内容")
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
    user_name = input("请输入要修改的内容")
    user_name = input("请输入要修改的内容")
    try:
        with open("user_name.txt", "w", encoding="utf-8") as f:
            f.write(user_name)
    except FileNotFoundError:
        print("未找到 user_name.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        exit(1)


def tianjiasheding():
    content = input("请输入你想要添加的内容：")
    try:
        with open("sheding.txt", "a", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError:
        print("未找到 sheding.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"追加内容时出错: {e}")


def chongxiesheding():
    content = input("请输入你想要的内容：")
    try:
        with open("sheding.txt", "w", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError:
        print("未找到 sheding.txt 文件，请检查文件路径。")
        exit(1)
    except Exception as e:
        print(f"追加内容时出错: {e}")
