import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.resizable(0,0)
root.config(bg="black")
root.geometry("400x450")
text= ""
def value(val):
    global text
    text = text+val
    output.set(text)
def clear():
    global text
    text = ""
    output.set(text)
def result():
    global text
    result = eval(text)
    
    output.set(result)

output = tk.StringVar()
screen = tk.Entry(root, font=("Arial", 40), textvariable=output).place(x=30, y=10, w=340, h=58)
b = tk.Button(root, text="C", font=('Arial', 40), bg="grey", fg="white", command=clear).place(x=30,y=80, w=70, h=60)
b = tk.Button(root, text="Del", font=('Arial',  30), bg="grey", fg="white").place(x=120,y=80, w=70, h=60)
b = tk.Button(root, text="%", font=('Arial',  40), bg="grey", fg="white", command=lambda:value("%")).place(x=210,y=80, w=70, h=60)
b = tk.Button(root, text="÷", font=('Arial', 40), bg="orange", fg="white", command=lambda:value("/")).place(x=300,y=80, w=70, h=60)

b = tk.Button(root, text="7", font=('Arial', 40), bg="#42474a", fg="white", command=lambda:value("7")).place(x=30,y=150, w=70, h=60)
b = tk.Button(root, text="8", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("8")).place(x=120,y=150, w=70, h=60)
b = tk.Button(root, text="9", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("9")).place(x=210,y=150, w=70, h=60)
b = tk.Button(root, text="X", font=('Arial', 40), bg="orange", fg="white", command=lambda:value("*")).place(x=300,y=150, w=70, h=60)
b = tk.Button(root, text="4", font=('Arial', 40), bg="#42474a", fg="white", command=lambda:value("4")).place(x=30,y=220, w=70, h=60)
b = tk.Button(root, text="5", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("5")).place(x=120,y=220, w=70, h=60)
b = tk.Button(root, text="6", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("6")).place(x=210,y=220, w=70, h=60)
b = tk.Button(root, text="-", font=('Arial', 40), bg="orange", fg="white", command=lambda:value("-")).place(x=300,y=220, w=70, h=60)
b = tk.Button(root, text="1", font=('Arial', 40), bg="#42474a", fg="white", command=lambda:value("1")).place(x=30,y=290, w=70, h=60)
b = tk.Button(root, text="2", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("2")).place(x=120,y=290, w=70, h=60)
b = tk.Button(root, text="3", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("3")).place(x=210,y=290, w=70, h=60)
b = tk.Button(root, text="+", font=('Arial', 40), bg="orange", fg="white", command=lambda:value("+")).place(x=300,y=290, w=70, h=60)
b = tk.Button(root, text="0", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value("0")).place(x=30,y=360, w=160, h=60)
b = tk.Button(root, text=".", font=('Arial',  40), bg="#42474a", fg="white", command=lambda:value(".")).place(x=210,y=360, w=70, h=60)
b = tk.Button(root, text="=", font=('Arial', 40), bg="orange", fg="white",command=result).place(x=300,y=360, w=70, h=60)
root.mainloop()
