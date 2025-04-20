from function import *

def config():
    while True:
        try:
            num = int(input("1.修改称呼\n2.修改设定\n0.退出\n请选择对应功能："))
            #修改称呼
            if num == 1:
                #进入修改称呼菜单
                while True:
                    try:
                        num1 = int(input("1.修改AI名字\n2.修改AI称呼你的名字\n0.退出\n请选择对应功能："))
                        if num1 == 1:
                            ai()
                        if num1 == 2:
                            user()
                        if num1 == 0:
                            break
                    except ValueError:
                        print("输入无效, 请输入有效数字")

            #修改设定
            if num == 2:
                #获取当前设定
                try:
                    with open("sheding.txt", "r", encoding="utf-8") as f:
                        sheding = f.read()
                    if sheding:
                        print("当前的设定为：" + sheding)
                    else:
                        print("当前没有设定，请先去设置吧！")
                except FileNotFoundError:
                    print("未找到 sheding.txt 文件，请检查文件路径。")
                    exit(1)
                except Exception as e:
                    print(f"读取文件时出现错误: {e}")
                    exit(1)

                #进入设定修改菜单
                while True:
                    try:
                        num1 = int(input("1.添加设定\n2.重写设定\n0.退出\n请选择对应功能："))
                        if num1 == 1:
                            tianjiasheding()
                        if num1 == 2:
                            chongxiesheding()
                        if num1 == 0:
                            break
                    except ValueError:
                        print("输入无效, 请输入有效数字")

            #退出
            if num == 0:
                break
        except ValueError:
            print("输入无效, 请输入有效数字")