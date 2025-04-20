DEEPSEEK_API_KEY = "sk-6304c16981934da99f301329fffa2c56"

#获取AINAME
try:
    with open("ainame.txt", "r", encoding="utf-8") as f:
        AINAME = f.read()

except FileNotFoundError:
    print("未找到 ainame.txt 文件，请检查文件路径。")
    exit(1)
except Exception as e:
    print(f"读取文件时出现错误: {e}")
    exit(1)

#获取USERNAME
try:
    with open("username.txt", "r", encoding="utf-8") as f:
        USERNAME = f.read()

except FileNotFoundError:
    print("未找到 username.txt 文件，请检查文件路径。")
    exit(1)
except Exception as e:
    print(f"读取文件时出现错误: {e}")
    exit(1)