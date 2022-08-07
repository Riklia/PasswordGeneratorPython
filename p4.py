import random
from tkinter import *
from tkinter import messagebox

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
allS = lowercase + uppercase + digits

tk = Tk()
tk.title("Генератор паролів")
tk.geometry("800x500")
tk.minsize(800, 500)


def check():
    first, second, third, fourth = False, False, False, False
    userpass = userPass.get()
    if 8 <= len(userpass) <= 20:
        for i in range(len(userpass)):
            first = userpass[i] in lowercase
            if first == True:
                break
        for i in range(len(userpass)):
            second = userpass[i] in uppercase
            if second == True:
                break
        for i in range(len(userpass)):
            third = userpass[i] in digits
            if third == True:
                break
        for i in range(len(userpass)):
            fourth = userpass[i] in allS
            if fourth == False:
                break
        if first == True and second == True and third == True and fourth == True:
            lbl4.config(fg = "green")
            lbl4.place(relx=.36)
            textInLbl4.set("Пароль задовольняє заданим критеріям.")
        else:
            lbl4.config(fg = "red")
            lbl4.place(relx=.32)
            textInLbl4.set("Пароль не задовольняє заданим критеріям, а саме:")
            if fourth == False:
                textInLbl4.set(textInLbl4.get()+"\nПароль складається із заборонених символів.")
            else:
                if first == False:
                    textInLbl4.set(textInLbl4.get()+"\nПароль не містить жодної малої літери.")
                if second == False:
                    textInLbl4.set(textInLbl4.get()+"\nПароль не містить жодної великої літери.")
            if third == False:
                textInLbl4.set(textInLbl4.get()+"\nПароль не містить жодної цифри.")
    else:
        lbl4.config(fg = "red")
        lbl4.place(relx=.27)
        textInLbl4.set("Пароль не задовольняє заданим критеріям. Його довжина < 8 або > 20")

def generate():
    passw = []
    passwStr = ""
    try:
        l = int(lengthPass.get())
    except ValueError:
        l = 0
        messagebox.showinfo("Увага!", "Уведіть довжину")
    if 8<=l<=20:
        t1.configure(state="normal")
        t1.delete("1.0","end")
        passw.clear()
        passwStr = ""
        passw.append(lowercase[random.randint(0, len(lowercase)-1)])
        passw.append(uppercase[random.randint(0, len(uppercase)-1)])
        passw.append(digits[random.randint(0, len(digits)-1)])
        for i in range(2, l-1):
            passw.append(allS[random.randint(0, len(allS)-1)])
        random.shuffle(passw)
        for i in passw:
            passwStr += i
        t1.insert(1.0, passwStr)
        t1.place(relx=.474 - .003*l)
        t1.configure(state="disabled", width = l+2)
    elif l != 0:
         messagebox.showinfo("Увага!", "Довжина пароля повинна бути >=8 і <=20")

#генерація паролю
lbl1 = Label(text = "Генерація паролю",  font = ("Times New Roman", 16), fg = "#e31010")
lbl1.place(relx=.41, rely = .03)
lbl2 = Label(text = "Довжина паролю:")
lbl2.place(relx=.37, rely = .11)
lengthPass = StringVar()
lengthPassEntry = Entry(textvariable=lengthPass)
lengthPassEntry.place(relx=.52, rely = .11)
but1 = Button(text = "Згенерувати пароль", fg = "red", bg = "black", font = ("Times New Roman", 12), command = generate)
but1.place(relx=.42, rely = .18)
lbl3 = Label(text = "Ваш пароль:")
lbl3.place(relx=.46, rely = .27)
t1 = Text(tk, height=1, width=11, exportselection=0)
t1.place(relx=.45, rely = .32)
t1.configure(state="disabled")
#перевірка паролю
lbl1 = Label(text = "Перевірка паролю", font = ("Times New Roman", 16), fg = "#e31010")
lbl1.place(relx=.4, rely = .45)
userPass = StringVar()
userPassEntry = Entry(textvariable=userPass)
userPassEntry.place(relx=.39, rely=.53, width = 190)
but2 = Button(text = "Перевірити пароль", fg = "red", bg = "black", font = ("Times New Roman", 12), command = check)
but2.place(relx=.415, rely = .59)
textInLbl4 = StringVar()
lbl4 = Label(text = "", textvariable=textInLbl4)
lbl4.place(relx=.32, rely = .67)


tk.mainloop()