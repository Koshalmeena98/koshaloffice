from tkinter import*
root=Tk()
import math

i=""

 
a=""
op=0

p1=PhotoImage(file='475497.png')
root.iconphoto(False,p1)
root.title("Rkoshal")


def items_selected(event):
    global a
    global i
    selected_indices=listbox.curselection()
    print(selected_indices)
    print(listbox.get(selected_indices))
    Text=listbox.get(selected_indices)
    T=""
    for k in range(0,len(Text),1):
        if(Text[k]=="="):
            break
    k=k+1
    for j in range(k,len(Text),1):
        T=T+Text[j]

    print(T)
    T=float(T)
    a=T
    i=T
    Label(root,text=str(a),width=32,height=5).grid(row=1,columnspan=4)
    


def my_exp():
    global i
    i=int(i)
    print(math.exp(i))
    Label(root, text=(math.exp(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

def my_red():
    global i
    i=int(i)
    print(math.radians(i))
    Label(root, text=(math.radians(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

    
def my_deg():
    global i
    i=int(i)
    print(math.degrees(i))
    Label(root, text=(math.degrees(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

    
def power():
    global i
    global a
    global op
    op=6
    a=i
    Label(root,text=str(a)+"^",width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)

    
  
def fact():
    global i
    i=int(i)
    print(math.factorial(i))
    Label(root, text=(math.factorial(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

def pi():
    global i
    #i=int(i)
    print(math.pi)
    Label(root, text=str(math.pi),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

def sqrt():
    global i
    i=int(i)
    print(math.sqrt(i))
    Label(root, text=(math.sqrt(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

    
                                                    
def log_my():
    global i
    i=int(i)
    print( math.log10(i))
    Label(root, text=(math.log10(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)
def ln_my():
    global i
    i=int(i)
    print(math.log(i))
    Label(root, text=(math.log(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)
    
def e_my():
    global i
    i=int(i)
    print(math.e(i))
    Label(root, text=(math.e(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)

    
    
def sin_my():
    global i
    i=int(i)
    print(math.sin(i))
    Label(root, text=(math.sin(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)
    
def cos_my():
    global i
    i=int(i)
    print(math.cos(i))
    Label(root, text=(math.cos(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)
    
def tan_my():
    global i
    i=int(i)
    print(math.tan(i))
    Label(root, text=(math.tan(i)),width=32,height=5,font=("Arial",20)).grid(row=1,columnspan=4)



    
def Ac():
    global i
    global a
    a=i
    a=""
    Label(root,text=str(a),width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)

def c():

    global i
    t=""
    for a in range(0,len(i)-1,1):
        t=t+i[a]

    i=t
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)




def p():
    global i
    global a
    global op
    op=5
    a=i
    Label(root,text=str(a)+"%",width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)

    



def div():
    global i
    global a
    global op
    op=4
    a=i
    Label(root,text=str(a)+"/",width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)

    
def add():
    global i
    global a
    global op
    op=1
    a=i
    a=i
    Label(root,text=str(a)+"+",width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)

    
def sub():
    global i
    global a
    global op
    op=2
    a=i
    Label(root,text=str(a)+"-",width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=0,columnspan=4)



def mul():
    global i
    global a
    global op
    op=3
    a=i
    Label(root,text=str(a)+"*",width=32,height=5).grid(row=1,columnspan=4)

    print(a)
    i=""
    Label(root,text=str(i),width=32,height=5).grid(row=1,columnspan=4)


def equal():
    global op
    global a
    global i
    if op==1:
        a=float(a)
        i=float(i)
        Label(root,text=str(i+a),width=32,height=5).grid(row=1,columnspan=4)
        listbox.insert(0,str(i)+"+"+str(a)+"="+str(i+a))
        i=str(i+a)
    if op==2:
        a=float(a)
        i=float(i)
        Label(root,text=str(a-i),width=32,height=5).grid(row=1,columnspan=4)
        listbox.insert(0,str(i)+"-"+str(a)+"="+str(i-a))
        i=str(i-a)


    if op==3:
        a=float(a)
        i=float(i)
        Label(root,text=str(a*i),width=32,height=5).grid(row=1,columnspan=4)
        listbox.insert(0,str(i)+"*"+str(a)+"="+str(i*a))
        i=(i*a)

    if op==4:
        a=float(a)
        i=float(i)
        Label(root,text=str(a/i),width=32,height=5).grid(row=1,columnspan=4)
        listbox.insert(0,str(i)+"/"+str(a)+"="+str(i*a/100))
        i=(i/a)

    if op==5:
        a=float(a)
        i=float(i)
        Label(root,text=str((i*a)/100),width=32,height=5).grid(row=1,columnspan=4)
        listbox.insert(0,str(i)+"%"+str(a)+"="+str(i+a))

    if op==6:
        a=int(a)
        i=int(i)
        print(i)
        print(a)
        t=1
        for b in range(0,i,1):
            t=t*a
        Label(root,text=str(t),width=32,height=5).grid(row=1,columnspan=4)
        listbox.insert(0,str(i)+"^"+str(a)+"="+str(i+a))

def A0():
    global i
    i=i+"0"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


    
def A7():
    global i
    i=i+"7"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


def A8():
    global i
    i=i+"8"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


def A9():
    global i
    i=i+"9"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


def A4():
    global i
    i=i+"4"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


def A5():
    global i
    i=i+"5"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)

def A6():
    global i
    i=i+"6"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)

def A3():
    global i
    i=i+"3"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


def A2():
    global i
    i=i+"2"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


def A1():
    global i
    i=i+"1"
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)
    
def dot():
    global i
    t=0
    for a in range(0,len(i),1):
        if(i[a]=="."):
            t=1
            print("Yes We have . in String")
            messagebox.askokcancel("message","we have already")
            break
        else:
            print("We don't have . in string")



    if(t==0):
        i=i+"."
    print(i)
    Label(root,text=str(i),width=32,height=5,font=("Arial",20)).grid(row=0,columnspan=4)


    


def exi():
    x=messagebox.askokcancel("to exit","do u want exit ")
    print(x)
    if(x==True):
        print("yes")
        exit()
    else:
        print("no")
    

def new():
    print("new file")

def open():
    print("open file")

def help():
    print("help")

def add_label(e):
    if(e.char=='0'):
        A0()
    if(e.char=='1'):
        A1()
    if(e.char=='2'):
        A2()
    if(e.char=='3'):
        A3()
    if(e.char=='4'):
        A4()
    if(e.char=='5'):
        A5()
    if(e.char=='6'):
        A6()
    if(e.char=='7'):
        A7()
    if(e.char=='8'):
        A8()
    if(e.char=='9'):
        A9()
    if(e.char=='+'):
        add()
    if(e.char=='-'):
        sub()
    if(e.char=='*'):
        mul()
    if(e.char=='/'):
        div()
    if(e.char=='.'):
        dot()
    if(e.char=='%'):
        p()
    if(e.char=='^'):
        power()
        
    
   
for cp in range(10):
    root.bind(str(cp),add_label)
    root.bind(str("+"),add_label)
    root.bind(str("-"),add_label)
    root.bind(str("*"),add_label)
    root.bind(str("/"),add_label)
    root.bind(str("."),add_label)
    root.bind(str("%"),add_label)
    root.bind(str("^"),add_label)  
root.bind('<Return>',lambda event:equal())
root.bind('<BackSpace>',lambda event:c())


    


menu=Menu()
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='new',command=new)
filemenu.add_command(label='open...',command=open)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exi)
helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='Help',command=help)


listbox=Listbox(root,height=23,width=40,bg="WHITE",activestyle='dotbox',font="Helvetica",fg="BLACK")
listbox.grid(rowspan=6,column=6)
scrollbar=Scrollbar(root)
scrollbar.grid(row=0,column=7,rowspan=6)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command= listbox.yview)
    

Label(root,text="0",width=20,height=3,bg="WHITE").grid(row=0,columnspan=4)

    
Label(root,text="0",width=20,height=3,bg="WHITE").grid(row=1,columnspan=4)


Button(root, text="Red",width=8,height=2,fg="RED", command=my_red).grid(row=2,column=0)
Button(root, text="Deg",width=8,height=2,fg="RED",command=my_deg).grid(row=2,column=1)
Button(root, text="x!",width=8,height=2,fg="RED",command=fact).grid(row=2,column=2)
Button(root, text="/",width=8,height=2,fg="RED",command=div).grid(row=2,column=3)
Button(root, text="inv",width=8,height=2, fg="BLUE",command="inv").grid(row=3,column=0)
Button(root, text="sin",width=8,height=2,fg="BLUE",command=sin_my).grid(row=3,column=1)
Button(root, text="ln",width=8,height=2,fg="BLUE",command=ln_my).grid(row=3,column=2)
Button(root, text=" *",width=8,height=2,fg="RED",command=mul).grid(row=3,column=3)
Button(root, text=" π",width=8,height=2,fg="BLUE",command=pi).grid(row=4,column=0)
Button(root, text="cos",width=8,height=2,fg="BLUE",command=cos_my).grid(row=4,column=1)
Button(root, text="log",width=8,height=2,fg="BLUE",command=log_my).grid(row=4,column=2)
Button(root, text="-",width=8,height=2,fg="RED",command=sub).grid(row=4,column=3)
Button(root, text="e",width=8,height=2,fg="BLUE",command=e_my).grid(row=5,column=0)
Button(root, text="tan",width=8,height=2,fg="BLUE",command=tan_my).grid(row=5,column=1)
Button(root, text="√ ",width=8,height=2,fg="BLUE",command=sqrt).grid(row=5,column=2)
Button(root, text="Ans",width=8,height=2,fg="RED",command="Ans").grid(row=5,column=3)
Button(root, text="Exp",width=8,height=2,fg="RED",command=my_exp).grid(row=6,column=0)
Button(root, text="^",width=8,height=2,fg="BLUE",command=power).grid(row=6,column=1)
Button(root, text="(",width=8,height=2,fg="BLUE",command="A").grid(row=6,column=2)
Button(root, text=")",width=8,height=2,fg="GREEN",command="a").grid(row=6,column=3)
Button(root, text="AC",width=8,height=2,fg="RED", command=Ac).grid(row=7,column=0)
Button(root, text="+",width=8,height=2,fg="RED",command=add).grid(row=7,column=1)
Button(root, text="%",width=8,height=2,fg="RED",command="p").grid(row=7,column=2)
Button(root, text="[",width=8,height=2,fg="RED",command="b").grid(row=7,column=3)
Button(root, text="7",width=8,height=2, fg="BLUE",command=A7).grid(row=8,column=0)
Button(root, text="8",width=8,height=2,fg="BLUE",command=A8).grid(row=8,column=1)
Button(root, text="9",width=8,height=2,fg="BLUE",command=A9).grid(row=8,column=2)
Button(root, text="]",width=8,height=2,fg="RED",command="B").grid(row=8,column=3)
Button(root, text="4",width=8,height=2,fg="BLUE",command=A4).grid(row=9,column=0)
Button(root, text="5",width=8,height=2,fg="BLUE",command=A5).grid(row=9,column=1)
Button(root, text="6",width=8,height=2,fg="BLUE",command=A6).grid(row=9,column=2)
Button(root, text="{",width=8,height=2,fg="RED",command="c").grid(row=9,column=3)
Button(root, text="1",width=8,height=2,fg="BLUE",command=A1).grid(row=10,column=0)
Button(root, text="2",width=8,height=2,fg="BLUE",command=A2).grid(row=10,column=1)
Button(root, text="3",width=8,height=2,fg="BLUE",command=A3).grid(row=10,column=2)
Button(root, text="}",width=8,height=2,fg="RED",command="A").grid(row=10,column=3)
Button(root, text="C",width=8,height=2,fg="RED",command=c).grid(row=11,column=0)
Button(root, text="0",width=8,height=2,fg="BLUE",command=A0).grid(row=11,column=1)
Button(root, text=".",width=8,height=2,fg="BLUE",command=dot).grid(row=11,column=2)
Button(root, text="=",width=8,height=2,fg="GREEN",command=equal).grid(row=11,column=3)

listbox.bind('<<ListboxSelect>>',items_selected)

root.mainloop()
