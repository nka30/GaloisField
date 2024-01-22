
import tkinter as tk
from tkinter import *

#GF(2^m) 2<=m<=8
#add,mult,sub,div
#add same as sub since additive inverse of A=A
#div same as mult with multiplicative inverse
def xor(y,k):
    s=''
    for i in range(len(y)):
        x=int(y[i:i+1])^int(k[i:i+1])
        s+=str(x)
    return s
def mult(p1,p2,m):
    l=[]
    p=p1
    last=0
    x=len(p2)
    
    if p2[x-1:x]=="1":
        l.append(p1)
    for i in range(1,x):
        if p2[x-i-1:x-i]=="1":
            for j in range(last,i):
                p=p1[1:x]+"0"
                
                if p1[0:1]=="1":
                    p=xor(p,m)
                    #print("p="+p)
                p1=p
            l.append(p)
            last=i

        
    #p=l[len(l)-1]
    for i in range(2,len(l)+1):
        p=xor(p,l[len(l)-i])
    
    return p
        

def add(p1,p2):
    p=xor(p1,p2)
    return p
def inverse(p2,m):
    inverse=p2
    one="1"
    while len(one)<len(p2):
            one="0"+one
    for i in range(2**len(p2)):
        x=bin(i)
        x=x[2:]
        while len(x)<len(p2):
            x="0"+x
        multinv=mult(x,p2,m)

        if multinv==one:
            
            inverse=x
            break
    return inverse
def div(p1,p2,m):

    return mult(p1,inverse(p2,m),m)

def sub(p1,p2):
    return add(p1,p2)
def mod(p1,m):
    x=len(m)
    p1=int(p1,2)
    m=int(m,2)
    s=bin(p1%m)[2:]
    while len(s)<x:
        s="0"+s
    return s

def submit():
        p1=entry.get()
        p2=entry2.get()
        operation=entry3.get()
        x=len(p1);
        if x==2: m="11" 
        elif x==3: m="101" 
        elif x==4: m="1001"
        elif x==5: m="00101"
        elif x==6: m="000011"
        elif x==7: m="0000011"
        elif x==8: m="00011011"
        s=0
        if operation=="add":
            s=add(p1,p2)
        elif operation=="mult":
            s=mult(p1,p2,m)
        elif operation=="sub":
            s=sub(p1,p2)
        elif operation=="inverse":
            s=inverse(p1,m)
        elif operation=="mod":
            s=mod(p1,m)
        else:
            s=div(p1,p2,m)
        window1=Tk()
        window1.title("Polynomial Arithmetic")
        #print("Result of "+ operation+":" +s)
        window.destroy()
        resultlabel=Label(window1,text="Result of "+ operation+": "+s,font=('Times',25)).pack()
        window1.mainloop()
        
window=Tk()
window.title("Polynomial Arithmetic")
firstlabel=Label(window,text="Enter the first polynomial as a 2,3,4,5,6,7, or 8 bit string:",font=('Times',12)).pack()
entry=Entry()
entry.pack()
secondlabel=Label(window,text="Enter the second polynomial as a bit string of the same length of the first polynomial:",font=('Times',12)).pack()
entry2=Entry()
entry2.pack()
thirdlabel=Label(window,text="Choose operation (add, mult, div, sub,inverse or mod(for first number only)):",font=('Times',12)).pack()
entry3=Entry()
entry3.pack()
E1=""
submit=Button(window,text="submit",command=submit)
submit.pack(side= 'bottom')
entry.config(font=('Times',30))
entry2.config(font=('Times',30))
entry3.config(font=('Times',30))
window.withdraw
window.mainloop()

