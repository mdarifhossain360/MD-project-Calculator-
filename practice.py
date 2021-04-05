import tkinter
from tkinter import*
from tkinter.messagebox import*
from tkinter.ttk import*
window=Tk()
window.config(
	bg="#EFC9AF"
)
window.geometry("1370x700+0+0")
window.title("MD Calculator")
#====================Welcome to my Calculator============================

#====================This project created by MD Arif Hossain===============

#=================================label=====================================
l1=tkinter.Label(
	window,
	text="Alhamdulillah ,this project created by MD Arif Hossain ",
	font=("verdana",20,"bold")
)
l1.pack(fill=X,pady=20)
#============================frame=========================================
frame=tkinter.Frame(window,width=500,height=454,bd=5,relief=GROOVE,bg="black")
frame.place(x=350,y=200)

#===========================important_funtion==============================
def clear():
	length=len(e_1.get())
	e_1.delete(length-1,END)

def enter1(event):
	b1.config(
		bg="#DF678C",
		fg="white"
	)
def gone1(event):
	b1.config(
		bg="#3D155F",
		fg="white"
	)
def enter2(event):
	b2.config(
		bg="#DF678C",
		fg="white"
	)
def gone2(event):
	b2.config(
		bg="#3D155F",
		fg="white"
	)
def enter3(event):
	b3.config(
		bg="#DF678C",
		fg="white"
	)
def gone3(event):
	b3.config(
		bg="#3D155F",
		fg="white"
	)
def enter4(event):
	b4.config(
		bg="#DF678C",
		fg="white"
	)
def gone4(event):
	b4.config(
		bg="#3D155F",
		fg="white"
	)
def enter5(event):
	b5.config(
		bg="#DF678C",
		fg="white"
	)
def gone5(event):
	b5.config(
		bg="#3D155F",
		fg="white"
	)
def enter6(event):
	b6.config(
		bg="#DF678C",
		fg="white"
	)
def gone6(event):
	b6.config(
		bg="#3D155F",
		fg="white"
	)
def enter7(event):
	b7.config(
		bg="#DF678C",
		fg="white"
	)
def gone7(event):
	b7.config(
		bg="#3D155F",
		fg="white"
	)
def enter8(event):
	b8.config(
		bg="#DF678C",
		fg="white"
	)
def gone8(event):
	b8.config(
		bg="#3D155F",
		fg="white"
	)
def enter9(event):
	b9.config(
		bg="#DF678C",
		fg="white"
	)
def gone9(event):
	b9.config(
		bg="#3D155F",
		fg="white"
	)
def enter0(event):
	b0.config(
		bg="#DF678C",
		fg="white"
	)
def gone0(event):
	b0.config(
		bg="#3D155F",
		fg="white"
	)
def enter_pluse(event):
	b_plu.config(
		bg="#DF678C",
		fg="white"
	)
def gone_pluse(event):
	b_plu.config(
		bg="#3D155F",
		fg="white"
	)
def enter_minus(event):
	b_min.config(
		bg="#DF678C",
		fg="white"
	)
def gone_minus(event):
	b_min.config(
		bg="#3D155F",
		fg="white"
	)
def enter_divi(event):
	b_div.config(
		bg="#DF678C",
		fg="white"
	)
def gone_divi(event):
	b_div.config(
		bg="#3D155F",
		fg="white"
	)
def enter_multi(event):
	b_mul.config(
		bg="#DF678C",
		fg="white"
	)
def gone_multi(event):
	b_mul.config(
		bg="#3D155F",
		fg="white"
	)
def enter_dot(event):
	b_dot.config(
		bg="#DF678C",
		fg="white"
	)
def gone_dot(event):
	b_dot.config(
		bg="#3D155F",
		fg="white"
	)
def enter_clear(event):
	b_clear.config(
		bg="#DF678C",
		fg="white"
	)
def gone_clear(event):
	b_clear.config(
		bg="#3D155F",
		fg="white"
	)
def enter_equal(event):
	b_equ.config(
		bg="#DF678C",
		fg="white"
	)
def gone_equal(event):
	b_equ.config(
		bg="#3D155F",
		fg="white"
	)
def click(event):
	b=event.widget
	text=b["text"]
	if text=="x":
		e_1.insert(END,"*")
		return
	if text=="÷":
		e_1.insert(END,"/")
		return
	    
	if text=="=":
		try:
			ex=e_1.get()
			result=eval(ex)
			e_1.delete(0,END)
			e_1.insert(0,result)
			return
		except Exception as e:
			showerror("Invalid Syntax")
			
			
	e_1.insert(END,text)

#============================Entry_label===============================
e_1=tkinter.Entry(window,width=34,font=("verdana",20,"bold"),justify=RIGHT,bg="white",fg="black",relief=SUNKEN)
e_1.place(x=350,y=130)

#==============================Button==================================
b1=tkinter.Button(frame,text="1",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b1.grid(row=0,column=0)
b1.bind("<Button-1>",click)
b1.bind("<Enter>",enter1)
b1.bind("<Leave>",gone1)


b2=tkinter.Button(frame,text="2",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b2.grid(row=0,column=1)
b2.bind("<Button-1>",click)
b2.bind("<Enter>",enter2)
b2.bind("<Leave>",gone2)


b3=tkinter.Button(frame,text="3",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b3.grid(row=0,column=2)
b3.bind("<Button-1>",click)
b3.bind("<Enter>",enter3)
b3.bind("<Leave>",gone3)


b4=tkinter.Button(frame,text="4",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b4.grid(row=0,column=3)
b4.bind("<Button-1>",click)
b4.bind("<Enter>",enter4)
b4.bind("<Leave>",gone4)


b5=tkinter.Button(frame,text="5",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b5.grid(row=1,column=0)
b5.bind("<Button-1>",click)
b5.bind("<Enter>",enter5)
b5.bind("<Leave>",gone5)


b6=tkinter.Button(frame,text="6",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b6.grid(row=1,column=1)
b6.bind("<Button-1>",click)
b6.bind("<Enter>",enter6)
b6.bind("<Leave>",gone6)


b7=tkinter.Button(frame,text="7",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b7.grid(row=1,column=2)
b7.bind("<Button-1>",click)
b7.bind("<Enter>",enter7)
b7.bind("<Leave>",gone7)



b8=tkinter.Button(frame,text="8",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b8.grid(row=1,column=3)
b8.bind("<Button-1>",click)
b8.bind("<Enter>",enter8)
b8.bind("<Leave>",gone8)


b9=tkinter.Button(frame,text="9",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b9.grid(row=2,column=0)
b9.bind("<Button-1>",click)
b9.bind("<Enter>",enter9)
b9.bind("<Leave>",gone9)



b0=tkinter.Button(frame,text="0",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b0.grid(row=2,column=1)
b0.bind("<Button-1>",click)
b0.bind("<Enter>",enter0)
b0.bind("<Leave>",gone0)


b_plu=tkinter.Button(frame,text="+",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b_plu.grid(row=0,column=4)
b_plu.bind("<Button-1>",click)
b_plu.bind("<Enter>",enter_pluse)
b_plu.bind("<Leave>",gone_pluse)


b_min=tkinter.Button(frame,text="-",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b_min.grid(row=0,column=5)
b_min.bind("<Button-1>",click)
b_min.bind("<Enter>",enter_minus)
b_min.bind("<Leave>",gone_minus)



b_div=tkinter.Button(frame,text="÷",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b_div.grid(row=1,column=4)
b_div.bind("<Button-1>",click)
b_div.bind("<Enter>",enter_divi)
b_div.bind("<Leave>",gone_divi)



b_mul=tkinter.Button(frame,text="x",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b_mul.grid(row=1,column=5)
b_mul.bind("<Button-1>",click)
b_mul.bind("<Enter>",enter_multi)
b_mul.bind("<Leave>",gone_multi)


b_dot=tkinter.Button(frame,text=".",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b_dot.grid(row=2,column=4)
b_dot.bind("<Button-1>",click)
b_dot.bind("<Enter>",enter_dot)
b_dot.bind("<Leave>",gone_dot)



b_clear=tkinter.Button(frame,text="C",width=5,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,command=clear,activebackground="#FFBB00",activeforeground="black",bg="#293250",fg="white")
b_clear.grid(row=2,column=5)
#b_clear.bind("<Button-1>",click)
b_clear.bind("<Enter>",enter_clear)
b_clear.bind("<Leave>",gone_clear)



b_equ=tkinter.Button(frame,text="=",width=11,height=3,font=("Helbetica",20,"bold"),padx=6,pady=6,relief=SOLID,activebackground="#a7d9d5",activeforeground="black",bg="#293250",fg="white")
b_equ.grid(row=2,column=2,columnspan=2)
b_equ.bind("<Button-1>",click)
b_equ.bind("<Enter>",enter_equal)
b_equ.bind("<Leave>",gone_equal)


#==============================mainloop=============================
window.mainloop()