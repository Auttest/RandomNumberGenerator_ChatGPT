import tkinter as tk
import random

#这个程序完全由ChatGPT完成
#我一点也不会python

#Auttest_20230416_0132
#ChatGPT Mar 23 Version

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("200x200")  # 设置窗口大小为200x200
        self.master.minsize(200, 200)  # 设置窗口最小大小为200x200
        self.master.maxsize(400, 400)  # 设置窗口最大大小为400x400
        self.pack()  # 调用Frame的pack方法，使组件展示在界面上
        self.create_widgets()  # 调用自定义的create_widgets方法
        self.count = 0  # 初始化计数器count为0

    def create_widgets(self):
        self.button = tk.Button(self, text="Click me!",
                                command=self.create_ranNum)  # 创建按钮组件，文本为“Click me!”，点击时调用create_ranNum方法
        self.button.pack(side="top", fill="both", expand=True)  # 按钮组件打包，并填满顶部

        self.display = tk.Label(self, text="", bg="light gray", height=self.button.winfo_height(),
                                justify="center")  # 创建标签组件，初始文本为空字符串，背景颜色为浅灰色，高度与按钮组件相同，文本居中
        self.display.pack(side="top", fill="both", expand=True)  # 标签组件打包，并填满顶部

        self.upper_limit_label = tk.Label(self, text="Upper Limit:")  # 创建标签组件，文本为“Upper Limit:”
        self.upper_limit_label.pack(side="top")  # 标签组件打包，并填满顶部

        self.upper_limit_entry = tk.Entry(self)  # 创建输入框组件
        self.upper_limit_entry.pack(side="top")  # 输入框组件打包，并填满顶部

        self.lower_limit_label = tk.Label(self, text="Lower Limit:")  # 创建标签组件，文本为“Lower Limit:”
        self.lower_limit_label.pack(side="top")  # 标签组件打包，并填满顶部

        self.lower_limit_entry = tk.Entry(self)  # 创建输入框组件
        self.lower_limit_entry.pack(side="top")  # 输入框组件打包，并填满顶部

        self.counter = tk.Label(self, text="0", font=("Arial", 16))  # 创建标签组件，初始文本为“0”，字体为Arial，大小为16
        self.counter.pack(side="bottom", padx=10, pady=10, anchor="se")  # 标签组件打包，并位于底部，距离x轴和y轴各有10个像素，靠右对齐

    def create_ranNum(self):
        # 获取上下限输入的内容
        upper_limit_input = self.upper_limit_entry.get()
        lower_limit_input = self.lower_limit_entry.get()

        # 判断输入是否为空，若不为空则将字符串类型的输入转为整数类型
        if upper_limit_input and lower_limit_input:
            upper_limit = int(upper_limit_input)
            lower_limit = int(lower_limit_input)
        # 若为空则默认上限为99，下限为0
        else:
            upper_limit = 99
            lower_limit = 0

        # 判断上限是否小于下限，若是则提示错误信息，否则生成一个随机数并显示在标签上
        if upper_limit < lower_limit:
            self.display.configure(text="上限应该大于下限", fg="red")
        else:
            random_num = random.randint(lower_limit, upper_limit)
            self.display.configure(text=str(random_num), fg="black")

            # 点击次数自增1，并显示在标签上
            self.count += 1
            self.counter.configure(text=str(self.count))

#创建主窗口并运行应用
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
