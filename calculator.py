import tkinter
cal = tkinter.Tk()
cal.title("calculator")
cal.minsize(width=570, height=600)
cal.resizable(False,False)
cal.config(background="Black")

equation = ""


def show(value):
    global equation
    equation += value
    lable_result.config(text=equation)


def clear():
    global equation
    equation = ""
    lable_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""

    lable_result.config(text=result)


lable_result = tkinter.Label(text="",font=("arial",30),width=25,height=2)
lable_result.pack()

tkinter.Button(text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#3697f5",command=lambda: clear()).place(x=10,y=100)
tkinter.Button(text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
tkinter.Button(text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
tkinter.Button(text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("*")).place(x=430,y=100)

tkinter.Button(text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
tkinter.Button(text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
tkinter.Button(text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
tkinter.Button(text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("-")).place(x=430,y=200)

tkinter.Button(text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
tkinter.Button(text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
tkinter.Button(text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
tkinter.Button(text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("+")).place(x=430,y=300)

tkinter.Button(text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
tkinter.Button(text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
tkinter.Button(text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
tkinter.Button(text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show("0")).place(x=10,y=500)

tkinter.Button(text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",background="#2a2d36",command=lambda: show(".")).place(x=290,y=500)
tkinter.Button(text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",background="#fe9037",command=lambda: calculate()).place(x=430,y=400)

cal.mainloop()

