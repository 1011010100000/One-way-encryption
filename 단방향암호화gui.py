from tkinter import *
import hashlib as hb

password = ""
password2 = ""
result = ""
result2 = ""

tk = Tk()
tk.title('단방향암호화gui프로그램')

def button1():
    global password, result, text4
    password = input1.get()
    result = hb.sha256(password.encode())
    text4 = Label(tk,text=result).grid(row=3,column=0)

def button2():
    global result, password2, result2, text3, text5
    password2 = input2.get()
    result2 = hb.sha256(password2.encode())
    text5 = Label(tk,text=result2).grid(row=8,column=0)

    if result.hexdigest() == result2.hexdigest():
        text3 = Label(tk,text='성공').grid(row=9,column=0)

    else:
        text3 = Label(tk,text='실패').grid(row=9,column=0)

text1 = Label(tk,text='암호를 정하십시오.').grid(row=0,column=0)
text2 = Label(tk,text='암호를 입력십시오.').grid(row=6,column=0)

input1 = Entry(tk)
input1.grid(row=0,column=1)
input2 = Entry(tk)
input2.grid(row=6,column=1)

button1 = Button(tk,text='완료',bg='green',fg='white',command=button1).grid(row=2,column=0)
button1 = Button(tk,text='완료',bg='green',fg='white',command=button2).grid(row=7,column=0)

tk.mainloop()