from tkinter import *
from tkinter import messagebox


click=True
class tic:
    def __init__(self,master):
        
        self.buttons=StringVar()
        self.L0=Label(root,text="Enter The Name",font=("Lucida Console",12),fg="#40bf40")
        self.L1=Label(root,text="Player 1",pady=-6,padx=12,bg="#b3d9ff")
        self.L2=Label(root,text="Player 2",pady=-6,padx=12,bg="#b3d9ff")

        self.L3=Label(root,text="",padx=-20)
        self.L4=Label(root,text="",padx=-20)

        self.L3.grid(row=1,column=2)
        self.L4.grid(row=2,column=2)
        
        self.e1=Entry(root,width=15)
        self.e2=Entry(root,width=15)
        
        self.L0.grid(row=0,column=0)
        self.L1.grid(row=1,column=0)
        self.L2.grid(row=2,column=0)
        
        self.e1.grid(row=1,column=1)
        self.e2.grid(row=2,column=1)
        
        self.lbl=Label(root,text="",font=(14))
        self.lbl.grid(row=3,column=1,pady=10,padx=5)

        self.b0=Button(root,text="ENTER",font=("Rockwell",11),command=self.clicked)
        self.b0.grid(row=3,column=2)

        self.b1=Button(root,text=" ",font=(15),height=6,width=8,command=lambda:self.checker(self.b1))
        self.b1.grid(row=4,column=0,sticky=S+N+E+W)

        self.b2=Button(root,text=" ",font=(15),height=6,width=8,command=lambda:self.checker(self.b2))
        self.b2.grid(row=4,column=1,sticky=S+N+E+W)

        self.b3=Button(root,text=" ",font=(15),height=6,width=8,command=lambda:self.checker(self.b3))
        self.b3.grid(row=4,column=2,sticky=S+N+E+W)

        self.b4=Button(root,text=" ",font=(15),height=6,width=8,command=lambda:self.checker(self.b4))
        self.b4.grid(row=5,column=0,sticky=S+N+E+W)

        self.b5=Button(root,text=" ",font=(15),height=6,width=8,command=lambda:self.checker(self.b5))
        self.b5.grid(row=5,column=1,sticky=S+N+E+W)

        self.b6=Button(root,text=" ",font=(15),height=6,width=8,command=lambda:self.checker(self.b6))
        self.b6.grid(row=5,column=2,sticky=S+N+E+W)

        self.b7=Button(root,text=" ",font=(15),height=6,width=15,command=lambda:self.checker(self.b7))
        self.b7.grid(row=6,column=0,sticky=S+N+E+W)

        self.b8=Button(root,text=" ",font=(15),height=6,width=15,command=lambda:self.checker(self.b8))
        self.b8.grid(row=6,column=1,sticky=S+N+E+W)

        self.b9=Button(root,text=" ",font=(15),height=6,width=15,command=lambda:self.checker(self.b9))
        self.b9.grid(row=6,column=2,sticky=S+N+E+W)

        
    def checker(self,buttons):
        global click
        count=0
        if buttons["text"]==" " and click==True:
            self.lbl.config(text="Player 2 "+self.e2.get())
            buttons["text"]="x"
        
            click= False
        elif buttons["text"]==" " and click == False:
            self.lbl.config(text="Player 1 "+self.e1.get())
            buttons["text"]="o"
        
            click= True
        elif(self.b1["text"]== "x" and self.b2["text"]=="x" and self.b3["text"]=="x" or
             self.b4["text"]== "x" and self.b5["text"]=="x" and self.b6["text"]=="x" or
              self.b7["text"]== "x" and self.b8["text"]=="x" and self.b9["text"]=="x" or
              self.b1["text"]== "x" and self.b4["text"]=="x" and self.b7["text"]=="x" or
             self.b2["text"]== "x" and self.b5["text"]=="x" and self.b8["text"]=="x" or
             self.b3["text"]== "x" and self.b6["text"]=="x" and self.b9["text"]=="x" or
             self.b1["text"]== "x" and self.b5["text"]=="x" and self.b9["text"]=="x" or
             self.b3["text"]== "x" and self.b5["text"]=="x" and self.b7["text"]=="x" ):
            res=messagebox.askokcancel("winner x",self.e1.get()+" have won a game.\r\n Do you want to play again")
            count=count+1
            p=self.e1.get()+": "+str(count)
            self.L3.config(text=p)


            if(res==True):
               self.b1.config(text=" ")
               self.b2.config(text=" ")
               self.b3.config(text=" ")
               self.b4.config(text=" ")
               self.b5.config(text=" ")
               self.b6.config(text=" ")
               self.b7.config(text=" ")
               self.b8.config(text=" ")
               self.b9.config(text=" ")
               break               

               

        elif(self.b1["text"]== "o" and self.b2["text"]=="o" and self.b3["text"]=="o" or
          self.b4["text"]== "o" and self.b5["text"]=="o" and self.b6["text"]=="o" or
         self.b7["text"]== "o" and self.b8["text"]=="o" and self.b9["text"]=="o" or
         self.b1["text"]== "o" and self.b4["text"]=="o" and self.b7["text"]=="o" or
         self.b2["text"]== "o" and self.b5["text"]=="o" and self.b8["text"]=="o" or
         self.b3["text"]== "o" and self.b6["text"]=="o" and self.b9["text"]=="o" or
         self.b1["text"]== "o" and self.b5["text"]=="o" and self.b9["text"]=="o" or
         self.b3["text"]== "o" and self.b5["text"]=="o" and self.b7["text"]=="o" ):
           res=messagebox.askokcancel("winner o",self.e2.get()+" you have won a game.\r\n Do you want to play again ")
           count=count+1
           p=self.e2.get()+": "+str(count)
           self.L4.config(text=p)
           
           if(res==True):
               self.b1.config(text=" ")
               self.b2.config(text=" ")
               self.b3.config(text=" ")
               self.b4.config(text=" ")
               self.b5.config(text=" ")
               self.b6.config(text=" ")
               self.b7.config(text=" ")
               self.b8.config(text=" ")
               self.b9.config(text=" ")
               break
               
               


    def clicked(self):
        res="player 1 : "+self.e1.get()
        self.lbl.config(text=res)
        self.L3.config(text=self.e1.get()+": ")
        self.L4.config(text=self.e2.get()+": ")
        

root=Tk()
root.title("tic tac toe")
b=tic(root)
    
root.mainloop()

