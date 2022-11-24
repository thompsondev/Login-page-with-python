from cProfile import label
from dis import code_info
from string import hexdigits
from tkinter import *
from tkinter import messagebox
from turtle import Screen, width
from unicodedata import name

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        root=Tk()
        root.title('App')
        root.geometry('925x500+300+200')
        root.configure(bg='#fff')
        root.resizable(False,False)
        
        
        Label(root,text='Welcome THOMPSON',bg='#fff', font=('calibri(Body)',50,'bold')).pack(expand=True)
    else:
        label=Label(Frame,text="Incorrect Password, Please Try Again?",fg='red',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=70,y=180)

    

        root.mainloop()
    


        
    

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

Frame=Frame(root,width=350,height=350,bg='white')
Frame.place(x=480,y=70)

heading=Label(Frame, text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##########--------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')


user =  Entry(Frame,width=35, fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0 ,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

#####--------------------------------------------

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')


code =  Entry(Frame,width=35, fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0 ,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)



#####################################---------------------

Button(Frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(Frame,text="Dont have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(Frame,width=6,text='Sign up',border=0, bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)



root.mainloop()