from duihua import *
from caidan import *
from rduihua import *

def main():
    while True:
        try:
            num = int(input("1.开始对话\n2.设置\n0.退出\nTip：首次对话请先设置称呼，否则对话内将使用默认称呼\n请选择对应的功能：\n"))
            if num == 1:
                num1 = int(input("1.普通模型\n2.思考模型\n0.退出\n请选择对应的功能：\n"))
                if num1 == 1:
                    duihua()
                if num1 == 2:
                    rduihua()
                if num == 0:
                    break
            if num == 2:
                config()
            if num == 0:
                break
            else:
                print("输入无效")
        except ValueError:
            print("输入无效, 请输入有效数字")

if __name__ == "__main__":
    main()