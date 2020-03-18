from tkinter import *
ventana =Tk()
ventana.config(bg="#3CB371")
miFrame = Frame (ventana,width=200,height=200)
miFrame.pack()

la1=Label(miFrame,text="Usuario")
la1.grid(row=0,column=0,pady=10,padx=10)
##padx el espacion que vamos a dejar de la principal
la2=Label(miFrame,text="Password")
la2.grid(row=1,column=0,pady=10,padx=10)
txt1=Entry(miFrame,justify="center")
txt1.grid(row=0,column=1,pady=10,padx=10)
txt2=Entry(miFrame,show="*")
txt2.grid(row=1,column=1,pady=10,padx=10)
btnaceptar=Button(miFrame,text="login")
btnaceptar.grid(row=2,column=0,pady=10,padx=10,columnspan=2)
btnaceptar.config(width=30)
ventana.mainloop()