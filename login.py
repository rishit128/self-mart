from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="image.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #=====login Frame=-=====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impat",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Account Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Email Address",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_user=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,show='*',font=("times new roman",15),bg="lightgrey")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="White",fg="#d77337",font=("times new roman",12)).place(x=90,y=280)
        register_btn=Button(Frame_login,text="Rgister new Account?",cursor="hand2",command=self.register1_window,bg="White",fg="#d77337",font=("times new roman",12)).place(x=250,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="White",bg="#d77337",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

    def register1_window(self):
        self.root.destroy()
        import Register   
    
        
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
                cur=con.cursor()
                r=self.txt_user.get()
                v=self.txt_pass.get()
                cur.execute("select * from rst")
                for i in cur:
                    if i[4]==r and i[7]==v and r=="dwdwdd" :
                        messagebox.showinfo("Success",f"welcome {r}",parent=self.root)
                        self.root.destroy()
                        import Design1
                    else:
                        i[4]==r and i[7]==v
                        messagebox.showinfo("Success",f"welcome {r}",parent=self.root)
                        self.root.destroy()
                        import Design1
                con.commit()
         
                

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

        con.close()


    
       

       
    

root=Tk()
obj=Login(root)
root.mainloop()    