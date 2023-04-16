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
        self.master.geometry("200x200")
        self.master.minsize(200, 200)
        self.master.maxsize(400, 400)
        self.pack()
        self.create_widgets()
        self.count = 0

    def create_widgets(self):
        self.button = tk.Button(self, text="Click me!", command=self.create_ranNum)
        self.button.pack(side="top", fill="both", expand=True)

        self.display = tk.Label(self, text="", bg="light gray", height=self.button.winfo_height(), justify="center")
        self.display.pack(side="top", fill="both", expand=True)

        self.upper_limit_label = tk.Label(self, text="Upper Limit:")
        self.upper_limit_label.pack(side="top")

        self.upper_limit_entry = tk.Entry(self)
        self.upper_limit_entry.pack(side="top")

        self.lower_limit_label = tk.Label(self, text="Lower Limit:")
        self.lower_limit_label.pack(side="top")

        self.lower_limit_entry = tk.Entry(self)
        self.lower_limit_entry.pack(side="top")

        self.counter = tk.Label(self, text="0", font=("Arial", 16))
        self.counter.pack(side="bottom", padx=10, pady=10, anchor="se")

    def create_ranNum(self):
        upper_limit_input = self.upper_limit_entry.get()
        lower_limit_input = self.lower_limit_entry.get()

        if upper_limit_input and lower_limit_input:
            upper_limit = int(upper_limit_input)
            lower_limit = int(lower_limit_input)
        else:
            upper_limit = 99
            lower_limit = 0

        if upper_limit < lower_limit:
            self.display.configure(text="Upper limit should be greater than lower limit.", fg="red")
        else:
            random_num = random.randint(lower_limit, upper_limit)
            self.display.configure(text=str(random_num), fg="black")

            self.count += 1
            self.counter.configure(text=str(self.count))


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
