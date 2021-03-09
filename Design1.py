from datetime import datetime
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from tkinter import ttk
import time
import sys
import math,random
import win32api
import win32print
import matplotlib.pyplot as plt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email import encoders
from email.mime.base import MIMEBase
import smtplib
import ssl
import os
import requests
f=''
flag=''
flags=''
con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
cur=con.cursor()
cur.execute("select * from sales_bill")



class Login1:
    def __init__(self,root):
        self.root=root
        self.root.title("SELF MART MANAGEMENT SYSTEM")
        self.root.geometry("1366x768+100+50")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="mesh.png")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0,relwidth=1,relheight=1)
        today=str(time.localtime()[2])+'/'+str(time.localtime()[1])+'/'+str(time.localtime()[0])
        mc=Label(self.root,text='Date :-  '+today,bg="thistle",fg="black",font=("times new roman",18,"bold"))
        mc.place(x=1160,y=50,width=200,height=40)
    
    
    

   
        
        ###### Frame 1 #######

        Frame_login=Frame(self.root,bg="dark slate blue",bd=9,relief=GROOVE)
        Frame_login.place(x=410,y=50,height=85,width=540)


        ###### Design ########
        bc=Label(Frame_login,text="Self Mart Management System",font=("Impat",25,"bold"),fg="light blue",bg="dark slate blue")
        bc.place(x=19,y=12)
        #Label(self.root, text='*'*100,bg="white",font=("Impat",25,"bold")).place(x=45,y=140,height=25)
        bc1=Label(self.root, text="Stock Maintenance",bd=6,relief=GROOVE,bg="dark slate gray",fg="light cyan",font=("Impat",25,"bold"))
        bc1.place(x=20,y=200,height=60,width=360)
        bc2=Label(self.root, text="Access Database",bd=10,relief=GROOVE,bg="dark slate gray",fg="light cyan",font=("Impat",25,"bold"))
        bc2.place(x=450,y=200,height=60,width=360)
        bc3=Label(self.root, text="Handle Cash Flows",bd=10,relief=GROOVE,bg="dark slate gray",fg="light cyan",font=("Impat",25,"bold"))
        bc3.place(x=880,y=200,height=60,width=360)
        Rc_btn=Button(self.root,text="New V.C.",command=self.new_window,cursor="hand2",bg="slate gray",fg="light cyan",bd=5,font=("times new roman",18,"bold"))
        Rc_btn.place(x=20,y=290,width=380,height=40)
        Addpc_btn=Button(self.root,text="Add product to Stock",command=self.register_window,cursor="hand2",bg="slate gray",fg="light cyan",bd=5,font=("times new roman",18,"bold"))
        Addpc_btn.place(x=20,y=350,width=380,height=40)
        delpc_btn=Button(self.root,text="Delete product from Stock",command=self.delete_update,cursor="hand2",bg="slate gray",fg="light cyan",bd=5,font=("times new roman",18,"bold"))
        delpc_btn.place(x=20,y=410,width=380,height=40)


        ##### Design 2 ########

        modify_btn=Button(self.root,text="Valuations",command=self.Valuations,cursor="hand2",bg="slate gray",fg="black",bd=5,font=("times new roman",18,"bold"))
        modify_btn.place(x=450,y=290,width=380,height=40)
        Search_btn=Button(self.root,text="Expiry Check",command=self.search_window,cursor="hand2",bg="slate gray",fg="black",bd=5,font=("times new roman",18,"bold"))
        Search_btn.place(x=450,y=410,width=380,height=40)
        


        ####### Design 3 ##########

        Billing_btn=Button(self.root,text="Billing",command=self.billing,cursor="hand2",bg="slate gray",fg="black",bd=5,font=("times new roman",18,"bold"))
        Billing_btn.place(x=880,y=290,width=380,height=40)
        Revenue_btn=Button(self.root,text="Check Today's Revenue",command=self.show_rev,cursor="hand2",bg="slate gray",fg="black",bd=5,font=("times new roman",18,"bold"))
        Revenue_btn.place(x=880,y=410,width=380,height=40)
        Logout_btn=Button(self.root,text="Log Out",command=self.logout_window,cursor="hand2",bg="slate gray",fg="black",bd=5,font=("times new roman",18,"bold"))
        Logout_btn.place(x=1100,y=820,width=280,height=40)










    def register_window(self):
        self.root2=Toplevel()
        self.root2.title("SELF MART MANAGEMENT SYSTEM")
        self.root2.geometry("1366x768+100+50")
        self.fg=ImageTk.PhotoImage(file="mesh.png")
        self.bg_image1=Label(self.root2,image=self.fg)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)
        
        
         ###### Frame 2 #######

        Frame1_login=Frame(self.root2,bg="light blue",bd=10,relief=GROOVE)
        Frame1_login.place(x=0,y=0,height=450,width=440)

        

         ###### Design ########

    
        title=Label(Frame1_login,text="Add New Product Here",font=("Impat",18,"bold"),fg="crimson",bg="light blue",justify=CENTER)
        title.place(x=10,y=10)
        self.n_label=Label(self.root2,text="ID : ",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        self.n_label.place(x=15,y=82)
        self.n_var=StringVar()
        self.n_var.set(str(random.randint(1,199)))
        n=Entry(self.root2,textvariable=self.n_var,font=("Times new roman",15),bg="white")
        n.place(x=173,y=88,width=250)
        
        type_label=Label(self.root2,text="Name :",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        type_label.place(x=15,y=135)
        self.type_label_var=StringVar()
        type_label=Entry(self.root2,textvariable=self.type_label_var,font=("Times new roman",15),bg="white")
        type_label.place(x=173,y=141,width=250)

        QuantityLeft_label=Label(self.root2,text="Type :",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        QuantityLeft_label.place(x=15,y=188)
        self.Quantity_label_var=StringVar()
        Quantity_label=Entry(self.root2,textvariable=self.Quantity_label_var,font=("Times new roman",15),bg="white")
        Quantity_label.place(x=173,y=194,width=250)

        COST_label=Label(self.root2,text="QuantityLeft  :",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        COST_label.place(x=15,y=243)
        self.cost_label_var=StringVar()
        self.cost_label=Entry(self.root2,textvariable=self.cost_label_var,font=("Times new roman",15),bg="white")
        self.cost_label.place(x=173,y=248,width=250)

        purposr_label=Label(self.root2,text="Cost  :",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        purposr_label.place(x=15,y=296)
        self.purpose_label_var=StringVar()
        self.purpose_label=Entry(self.root2,textvariable=self.purpose_label_var,font=("Times new roman",15),bg="white")
        self.purpose_label.place(x=173,y=302,width=250)


        ExpiryDate_label=Label(self.root2,text="Expiry Date :",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        ExpiryDate_label.place(x=15,y=349)
        self.expiry_label_var=StringVar()
        self.expiry_label=Entry(self.root2,textvariable=self.expiry_label_var,font=("Times new roman",15),bg="white")
        self.expiry_label.place(x=173,y=355,width=250)

        Manufacture_label=Label(self.root2,text="Manufacture :",font=("Impat",16,"bold"),fg="indigo",bg="light blue")
        Manufacture_label.place(x=15,y=402)
        self.manu_label_var=StringVar()
        self.manu_label=Entry(self.root2,textvariable=self.manu_label_var,font=("Times new roman",15),bg="white")
        self.manu_label.place(x=173,y=407,width=250)
        submit1=Button(self.root2,text="Submit",command=self.submit,cursor="hand2",bg="#FF8C00",font=("times New roman",16))
        submit1.place(x=30,y=500,width=130)
        clear=Button(self.root2,text="Clear",command=self.clear,cursor="hand2",bg="#FF8C00",font=("times New roman",16))
        clear.place(x=180,y=500,width=130)
        r=Frame(self.root2,bd=7,relief=GROOVE,bg="slate gray")
        r.place(x=550,y=500,width=250,height=70)
        
        
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from rst2")
        rows1=cur.fetchall()
        
        rishit=len(rows1)
        undata=Label(self.root2,text="Total Products = "+str(rishit),bg="slate gray",fg="indigo",font=("times new roman",18,"bold"))
        undata.place(x=570,y=520)
       



        Table_Frame=Frame(self.root2,bd=4,relief=GROOVE,bg="#EC7B51")
        Table_Frame.place(x=500,y=40,width=850,height=370)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                background="white",
                foreground="blue",
                rowheight=45,
                fieldbackground="white")
        style.map('Treeview',
            background=[('selected', 'indigo')])


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.login1_table=ttk.Treeview(Table_Frame,columns=("ID","Name","Type","QuantityLeft","Cost","ExpiryDate","Manufacture"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.login1_table.heading("ID",text="ID.")
        self.login1_table.heading("Name",text="Name.")
        self.login1_table.heading("Type",text="Type.")
        self.login1_table.heading("QuantityLeft",text="QuantityLeft.")
        self.login1_table.heading("Cost",text="Cost.")
        self.login1_table.heading("ExpiryDate",text="ExpiryDate")
        self.login1_table.heading("Manufacture",text="Manufacture.")
        self.login1_table['show']='headings'
        self.login1_table.column("ID",width=40)
        self.login1_table.column("Name",width=80)
        self.login1_table.column("Type",width=50)
        self.login1_table.column("QuantityLeft",width=50)
        self.login1_table.column("Cost",width=60)
        self.login1_table.column("ExpiryDate",width=60)
        self.login1_table.column("Manufacture",width=60)


        self.login1_table.pack(fill=BOTH,expand=1)
        self.login1_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        
        

       
        


    def submit(self):
        if self.n_var.get()=="" or self.type_label_var.get()=="" or self.Quantity_label_var.get()=="" or self.cost_label.get()=="" or self.purpose_label.get()=="" or self.expiry_label.get()=="" or self.manu_label.get()==""  :
            messagebox.showerror("error","All Fields Are Required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
                cur=con.cursor()
                cur.execute("insert into rst2 (Id,Name,Type,QuantityLeft,Cost,ExpiryDate,Manufacture) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.n_var.get(),
                                self.type_label_var.get(),
                                self.Quantity_label_var.get(),
                                self.cost_label.get(),
                                self.purpose_label.get(),
                                self.expiry_label.get(),
                                self.manu_label.get()
                                ))
                con.commit()
                
                self.fetch_data()
                self.clear()
                con.close()
            except Exception as es:
                messagebox.showerror("error",f"Error due to: {str(es)}",parent=self.root)




    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from rst2")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.login1_table.delete(*self.login1_table.get_children())
            for row in rows:
                self.login1_table.insert('',END,values=row)
            
            con.commit()
        con.close()


    def clear(self):
        self.n_var.set("")
        self.type_label_var.set("")
        self.Quantity_label_var.set("")
        self.cost_label.delete(0,END)
        self.purpose_label.delete(0,END)
        self.expiry_label.delete(0,END)
        self.manu_label.delete(0,END) 
        self.txt_search_var.set("")
            
       

    def logout_window(self):
        self.root.destroy()
        import login

    def new_window(self):
        self.root3=Toplevel()
        self.root3.title("SELF MART MANAGEMENT SYSTEM")
        self.root3.geometry("1366x768+100+50")
        self.root3.resizable(False,False)
        self.fg=ImageTk.PhotoImage(file="ali.png")
        self.bg_image1=Label(self.root3,image=self.fg)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)
        title=Label(self.root3,text="Customer Details",font=("Impat",35,"bold"),fg="indigo",bg="dark khaki")
        title.place(x=550,y=20)


        Frame1_login=Frame(self.root3,bg="light gray",bd=10,relief=GROOVE)
        Frame1_login.place(x=0,y=40,height=500,width=440)

        title=Label(Frame1_login,text="Add Details",font=("Impat",18,"bold"),fg="crimson",bg="light gray",justify=CENTER)
        title.place(x=130,y=15)

        self.id_label=Label(self.root3,text="id : ",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        self.id_label.place(x=15,y=140)
        self.id_var=StringVar()
        id=Entry(self.root3,textvariable=self.id_var,font=("Times new roman",15),bg="white")
        id.place(x=173,y=140,width=250)

        f_name_label=Label(self.root3,text="f_name :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        f_name_label.place(x=15,y=190)
        self.f_name_label_var=StringVar()
        f_name_label=Entry(self.root3,textvariable=self.f_name_label_var,font=("Times new roman",15),bg="white")
        f_name_label.place(x=173,y=190,width=250)

        l_name_label=Label(self.root3,text="l_name :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        l_name_label.place(x=15,y=240)
        self.i_name_label_var=StringVar()
        i_name_label=Entry(self.root3,textvariable=self.i_name_label_var,font=("Times new roman",15),bg="white")
        i_name_label.place(x=173,y=240,width=250)

        contact_label=Label(self.root3,text="Contact  :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        contact_label.place(x=15,y=290)
        self.contact_label_var=StringVar()
        self.contact_label=Entry(self.root3,textvariable=self.contact_label_var,font=("Times new roman",15),bg="white")
        self.contact_label.place(x=173,y=290,width=250)

        email_label=Label(self.root3,text="email  :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        email_label.place(x=15,y=340)
        self.email_label_var=StringVar()
        self.email_label=Entry(self.root3,textvariable=self.email_label_var,font=("Times new roman",15),bg="white")
        self.email_label.place(x=173,y=340,width=250)


        question_label=Label(self.root3,text="question :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        question_label.place(x=15,y=390)
        self.question_label_var=StringVar()
        self.question_label=Entry(self.root3,textvariable=self.question_label_var,font=("Times new roman",15),bg="white")
        self.question_label.place(x=173,y=390,width=250)

        answer_label=Label(self.root3,text="answer :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        answer_label.place(x=15,y=440)
        self.answer_label_var=StringVar()
        self.answer_label=Entry(self.root3,textvariable=self.answer_label_var,font=("Times new roman",15),bg="white")
        self.answer_label.place(x=173,y=440,width=250)

        password_label=Label(self.root3,text="password :",font=("Impat",16,"bold"),fg="indigo",bg="light gray")
        password_label.place(x=15,y=490)
        self.password_label_var=StringVar()
        self.password_label=Entry(self.root3,textvariable=self.password_label_var,font=("Times new roman",15),bg="white")
        self.password_label.place(x=173,y=490,width=250)

        delete=Button(self.root3,text="Delete",command=self.delete_data1,cursor="hand2",bg="#FF8C00",font=("times New roman",16))
        delete.place(x=40,y=600,width=130)
        update=Button(self.root3,text="update",command=self.update_data1,cursor="hand2",bg="#FF8C00",font=("times New roman",16))
        update.place(x=210,y=600,width=130)
        search=Button(self.root3,text="Search",command=self.search_data1,cursor="hand2",bg="#FF8C00",font=("times New roman",16))
        search.place(x=380,y=600,width=130)
        r=Frame(self.root3,bd=7,relief=GROOVE,bg="dark khaki")
        r.place(x=600,y=600,width=600,height=70)
        lblsearch=Label(self.root3,text="Search By",font=("Impat",16,"bold"),fg="dark blue",bg="dark khaki")
        lblsearch.place(x=610,y=620)

        self.cmb_search=ttk.Combobox(self.root3,font=("Times new roman",16),state='readonly',justify=CENTER)
        self.cmb_search['values']=("Select","f_name","contact")
        self.cmb_search.place(x=750,y=620,width=130,height=30)
        self.cmb_search.current(0)

        self.txt_search_var=StringVar()
        self.txt_search=Entry(self.root3,textvariable=self.txt_search_var,font=("Times new roman",15),bg="white",bd=5,relief=GROOVE)
        self.txt_search.place(x=900,y=620,width=250,height=30)





        Table_Frame=Frame(self.root3,bd=4,relief=GROOVE,bg="#EC7B51")
        Table_Frame.place(x=550,y=100,width=850,height=370)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.login2_table=ttk.Treeview(Table_Frame,columns=("id","f_name","l_name","contact","email","question","answer","password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.login2_table.xview)
        scroll_y.config(command=self.login2_table.yview)

          
        self.login2_table.heading("id",text="id.")
        self.login2_table.heading("f_name",text="f_name.")
        self.login2_table.heading("l_name",text="l_name.")
        self.login2_table.heading("contact",text="contact.")
        self.login2_table.heading("email",text="email.")
        self.login2_table.heading("question",text="question.")
        self.login2_table.heading("answer",text="answer")
        self.login2_table.heading("password",text="password.")
        self.login2_table['show']='headings'
        self.login2_table.column("id",width=50)
        self.login2_table.pack(fill=BOTH,expand=1)
        self.login2_table.bind("<ButtonRelease-1>",self.get_cursor1)
        self.fetch1_data()


    def get_cursor1(self,ev):
        cursor_row=self.login2_table.focus()
        contents=self.login2_table.item(cursor_row)
        row=contents['values']

        self.id_var.set(row[0])
        self.f_name_label_var.set(row[1])
        self.i_name_label_var.set(row[2])
        self.contact_label_var.set(row[3])
        self.email_label_var.set(row[4])
        self.question_label_var.set(row[5])
        self.answer_label_var.set(row[6])
        self.password_label_var.set(row[7])



    def update_data1(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("update rst set f_name=%s,l_name=%s,contact=%s,email=%s,question=%s,answer=%s,password=%s where id=%s",(
                                                                                                            self.f_name_label_var.get(),
                                                                                                            self.i_name_label_var.get(),
                                                                                                            self.contact_label_var.get(),
                                                                                                            self.email_label_var.get(),
                                                                                                            self.question_label_var.get(),
                                                                                                            self.answer_label_var.get(),
                                                                                                            self.password_label_var.get(),
                                                                                                            self.id_var.get()
                                                                                                            ))
        con.commit()
        self.fetch1_data()
        self.clear()
        con.close()


    def delete_data1(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("delete from rst where f_name=%s",self.f_name_label_var.get())
        con.commit()
        con.close()
        self.fetch1_data()
        self.clear()


    def search_data1(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from rst where "+str(self.cmb_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.login2_table.delete(*self.login2_table.get_children())
            for row in rows:
                self.login2_table.insert('',END,values=row)
            con.commit()
        con.close()
   







    def delete_update(self):
        self.root4=Toplevel()
        self.root4.title("SELF MART MANAGEMENT SYSTEM")
        self.root4.geometry("1366x768+100+50")
        self.fg=ImageTk.PhotoImage(file="roman.png")
        self.bg_image1=Label(self.root4,image=self.fg)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)

        ######## ############ ############# ########
        Frame1_login=Frame(self.root4,bg="slate gray",bd=10,relief=GROOVE)
        Frame1_login.place(x=0,y=0,height=450,width=440)


        title=Label(Frame1_login,text="Add New Product Here",font=("Impat",18,"bold"),fg="maroon",bg="slate gray",justify=CENTER)
        title.place(x=80,y=15)
        self.n_label=Label(self.root4,text="ID : ",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        self.n_label.place(x=15,y=82)
        self.n_var=StringVar()
        n=Entry(self.root4,textvariable=self.n_var,font=("Times new roman",15),bg="white")
        n.place(x=173,y=88,width=250)

        type_label=Label(self.root4,text="Name :",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        type_label.place(x=15,y=135)
        self.type_label_var=StringVar()
        type_label=Entry(self.root4,textvariable=self.type_label_var,font=("Times new roman",15),bg="white")
        type_label.place(x=173,y=141,width=250)

        QuantityLeft_label=Label(self.root4,text="Type :",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        QuantityLeft_label.place(x=15,y=188)
        self.Quantity_label_var=StringVar()
        Quantity_label=Entry(self.root4,textvariable=self.Quantity_label_var,font=("Times new roman",15),bg="white")
        Quantity_label.place(x=173,y=194,width=250)


        COST_label=Label(self.root4,text="QuantityLeft  :",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        COST_label.place(x=15,y=243)
        self.cost_label_var=StringVar()
        self.cost_label=Entry(self.root4,textvariable=self.cost_label_var,font=("Times new roman",15),bg="white")
        self.cost_label.place(x=173,y=248,width=250)

        purposr_label=Label(self.root4,text="Cost  :",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        purposr_label.place(x=15,y=296)
        self.purpose_label_var=StringVar()
        self.purpose_label=Entry(self.root4,textvariable=self.purpose_label_var,font=("Times new roman",15),bg="white")
        self.purpose_label.place(x=173,y=302,width=250)


        ExpiryDate_label=Label(self.root4,text="Expiry Date :",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        ExpiryDate_label.place(x=15,y=349)
        self.expiry_label_var=StringVar()
        self.expiry_label=Entry(self.root4,textvariable=self.expiry_label_var,font=("Times new roman",15),bg="white")
        self.expiry_label.place(x=173,y=355,width=250)


        Manufacture_label=Label(self.root4,text="Manufacture :",font=("Impat",16,"bold"),fg="indigo",bg="slate gray")
        Manufacture_label.place(x=15,y=402)
        self.manu_label_var=StringVar()
        self.manu_label=Entry(self.root4,textvariable=self.manu_label_var,font=("Times new roman",15),bg="white")
        self.manu_label.place(x=173,y=407,width=250)
        submit1=Button(self.root4,text="Submit",command=self.submit,cursor="hand2",bg="cadet blue",font=("times New roman",16))
        submit1.place(x=30,y=500,width=130)
        clear=Button(self.root4,text="Clear",command=self.clear,cursor="hand2",bg="cadet blue",font=("times New roman",16))
        clear.place(x=180,y=500,width=130)
        delete=Button(self.root4,text="Delete",command=self.delete_data,cursor="hand2",bg="cadet blue",font=("times New roman",16))
        delete.place(x=320,y=500,width=130)
        update=Button(self.root4,text="update",command=self.update_ddat,cursor="hand2",bg="cadet blue",font=("times New roman",16))
        update.place(x=480,y=500,width=130)
        search=Button(self.root4,text="Search",command=self.search_data,cursor="hand2",bg="cadet blue",font=("times New roman",16))
        search.place(x=640,y=500,width=130)
        r=Frame(self.root4,bd=7,relief=GROOVE,bg="slate gray")
        r.place(x=10,y=580,width=600,height=70)
        lblsearch=Label(self.root4,text="Search By",font=("Impat",16,"bold"),fg="dark blue",bg="slate gray")
        lblsearch.place(x=20,y=600)

       

        
        self.cmb_search=ttk.Combobox(self.root4,font=("Times new roman",16),state='readonly',justify=CENTER)
        self.cmb_search['values']=("Select","Name","Type")
        self.cmb_search.place(x=140,y=600,width=130,height=30)
        self.cmb_search.current(0)

        

        self.txt_search_var=StringVar()
        self.txt_search=Entry(self.root4,textvariable=self.txt_search_var,font=("Times new roman",15),bg="white",bd=5,relief=GROOVE)
        self.txt_search.place(x=291,y=600,width=250,height=30)



        Table_Frame=Frame(self.root4,bd=4,relief=GROOVE,bg="#EC7B51")
        Table_Frame.place(x=500,y=40,width=850,height=370)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                background="white",
                foreground="blue",
                rowheight=45,
                fieldbackground="white")
        style.map('Treeview',
            background=[('selected', 'indigo')])



        self.login1_table=ttk.Treeview(Table_Frame,columns=("ID","Name","Type","QuantityLeft","Cost","ExpiryDate","Manufacture"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.login1_table.heading("ID",text="ID.")
        self.login1_table.heading("Name",text="Name.")
        self.login1_table.heading("Type",text="Type.")
        self.login1_table.heading("QuantityLeft",text="QuantityLeft.")
        self.login1_table.heading("Cost",text="Cost.")
        self.login1_table.heading("ExpiryDate",text="ExpiryDate")
        self.login1_table.heading("Manufacture",text="Manufacture.")
        self.login1_table['show']='headings'
        self.login1_table.column("ID",width=50)
        self.login1_table.column("Name",width=80)
        self.login1_table.column("Type",width=50)
        self.login1_table.column("QuantityLeft",width=50)
        self.login1_table.column("Cost",width=60)
        self.login1_table.column("ExpiryDate",width=60)
        self.login1_table.column("Manufacture",width=60)


        self.login1_table.pack(fill=BOTH,expand=1)
        self.login1_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def search_window(self):
        self.root5=Toplevel()
        self.root5.title("SELF MART MANAGEMENT SYSTEM")
        self.root5.geometry("1440x900+100+50")
        self.fg=ImageTk.PhotoImage(file="Design.png")
        self.bg_image1=Label(self.root5,image=self.fg)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)

        Table_Frame=Frame(self.root5,bd=4,relief=GROOVE,bg="#EC7B51")
        Table_Frame.place(x=10,y=40,width=850,height=370)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                background="white",
                foreground="indigo",
                rowheight=45,
                fieldbackground="white")
        style.map('Treeview',
            background=[('selected', 'indigo')])



        self.login1_table=ttk.Treeview(Table_Frame,columns=("ID","Name","Type","QuantityLeft","Cost","ExpiryDate","Manufacture"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.login1_table.heading("ID",text="ID.")
        self.login1_table.heading("Name",text="Name.")
        self.login1_table.heading("Type",text="Type.")
        self.login1_table.heading("QuantityLeft",text="QuantityLeft.")
        self.login1_table.heading("Cost",text="Cost.")
        self.login1_table.heading("ExpiryDate",text="ExpiryDate")
        self.login1_table.heading("Manufacture",text="Manufacture.")
        self.login1_table['show']='headings'
        self.login1_table.column("ID",width=50)
        self.login1_table.column("Name",width=80)
        self.login1_table.column("Type",width=50)
        self.login1_table.column("QuantityLeft",width=50)
        self.login1_table.column("Cost",width=60)
        self.login1_table.column("ExpiryDate",width=60)
        self.login1_table.column("Manufacture",width=60)


        self.login1_table.pack(fill=BOTH,expand=1)
        self.login1_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        r=Frame(self.root5,bd=7,relief=GROOVE,bg="slate gray")
        r.place(x=10,y=480,width=630,height=70)
        lblsearch=Label(self.root5,text="Search By",font=("Impat",16,"bold"),fg="dark blue",bg="slate gray")
        lblsearch.place(x=20,y=500)

       

        
        self.cmb_search=ttk.Combobox(self.root5,font=("Times new roman",16),state='readonly',justify=CENTER)
        self.cmb_search['values']=("Select","Name","Type")
        self.cmb_search.place(x=140,y=500,width=130,height=30)
        self.cmb_search.current(0)

        

        self.txt_search_var=StringVar()
        self.txt_search=Entry(self.root5,textvariable=self.txt_search_var,font=("Times new roman",15),bg="white",bd=5,relief=GROOVE)
        self.txt_search.place(x=291,y=500,width=250,height=30)
        search=Button(self.root5,text="Search",command=self.search_data,cursor="hand2",bg="#FF8C00",font=("times New roman",20))
        search.place(x=240,y=600,width=160)

        








    def fetch1_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from rst")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.login2_table.delete(*self.login2_table.get_children())
            for row in rows:
                self.login2_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row=self.login1_table.focus()
        contents=self.login1_table.item(cursor_row)
        row=contents['values']
        
        self.n_var.set(row[0])
        self.type_label_var.set(row[1])
        self.Quantity_label_var.set(row[2])
        self.cost_label_var.set(row[3])
        self.purpose_label_var.set(row[4])
        self.expiry_label_var.set(row[5])
        self.manu_label_var.set(row[6])


    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("delete from rst2 where ID=%s",self.n_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def update_ddat(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("update rst2 set Name=%s,Type=%s,QuantityLeft=%s,Cost=%s,ExpiryDate=%s,Manufacture=%s where ID=%s",(
                                                                                                            self.type_label_var.get(),
                                                                                                            self.Quantity_label_var.get(),
                                                                                                            self.cost_label_var.get(),
                                                                                                            self.purpose_label_var.get(),
                                                                                                            self.expiry_label_var.get(),
                                                                                                            self.manu_label_var.get(),
                                                                                                            self.n_var.get()
                                                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()




    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from rst2 where "+str(self.cmb_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.login1_table.delete(*self.login1_table.get_children())
            for row in rows:
                self.login1_table.insert('',END,values=row)
            con.commit()
        con.close()
    


    def billing(self):
        self.root6=Toplevel()
        self.root6.geometry("1440x900+100+50")
        self.root6.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root6,bd=12,relief=GROOVE,bg=bg_color,fg="white",text="Billing Software",font=("times new roman",30,"bold"),pady=2).pack(fill=X)


        #=============Variables==================#
        #=========Search Field=============#
        self.search_item_no=StringVar()
        self.search_item_no.set("")

        #========Item Details============#
        self.item_name1=StringVar()
        self.item_name=StringVar()  
        self.item_price=IntVar()
        self.item_quantity=IntVar()
        self.item_quantity.set(1)

        #===========Customer===========#
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set(str(random.randint(1000,9999)))



        #=========Creating Menus for rishit=======================

      

        #==========Menu ends here===================================
    
        ##-------------Customer Detail Frame-------------##
        F1=LabelFrame(self.root6,bd=10,relief=GROOVE, text="Customer Details",font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,bg=bg_color,fg="white",text="Customer Name",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,textvariable=self.c_name,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,bg=bg_color,fg="white",text="Phone No.",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_lbl=Entry(F1,textvariable=self.c_phon,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,bg=bg_color,fg="white",text="Bill No.",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_lbl=Entry(F1,textvariable=self.search_bill,width=20,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,command=self.find_bill,text="Search",width=10,bd=7,font="arial 15 bold").grid(row=0,column=6,padx=20,pady=10)

        #============Search Items===============#

        F2=LabelFrame(self.root6,bd=10,relief=GROOVE, text="Search Items",font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=200,width=325,height=480)

        item_no_lbl=Label(F2,text="Item No.",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").place(x=10,y=40)
        #item_no_txt=Entry(F2,width=10,textvariable=self.search_item_no,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).place(x=100,y=40)

        #Button for search using item no.
        search_no_btn=Button(F2,command=self.search_item,bg="gold",text="Search",fg="Black",width=7,bd=5,font="arial 18 bold").place(x=110,y=320)
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select Name from rst2")
        li = cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
       
        
        e = Entry(F2,width=10,textvariable=self.search_item_no,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        e.place(x=100,y=40) 
        e.bind('<KeyRelease>', self.checkkey) 
        
        self.l = a

        #creating list box 
        self.lb = Listbox(F2,bd=10,relief=GROOVE,bg=bg_color,fg="gold") 
        self.lb.place(x=95,y=100) 
        self.update(self.l)
        #============Item Details===============#

        F3=LabelFrame(self.root6,bd=10,relief=GROOVE, text="Item Details",font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=200,width=325,height=380)

        g1_lbl=Label(F3,text="Item No:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        g1_txt=Label(F3,textvariable=self.item_name1,font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=1,padx=10,pady=10,stick="w")

        g2_lbl=Label(F3,text="Item Name:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=0,pady=10,sticky="w")
        g2_txt=Label(F3,textvariable=self.item_name,font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=1,padx=10,pady=10,stick="w")

    
        g3_lbl=Label(F3,text="Price:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=0,pady=10,sticky="w")
        g3_txt=Label(F3,textvariable=self.item_price,font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=1,padx=10,pady=10,stick="w")

        item_qty_lbl=Label(F3,text="Item Quantity.",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=0,pady=10,sticky="w")
        item_qty_txt=Entry(F3,width=10,textvariable=self.item_quantity,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        search_name_btn=Button(F3,bg="gold",text="Add",command=self.add_item,fg="Black",width=7,bd=5,font="arial 18 bold").grid(row=4,column=1,padx=5,pady=5)


        #============Shopping Cart===============#

        F4=LabelFrame(self.root6,bd=10,relief=GROOVE, text="Shopping Cart",font=("times new roman",16,"bold"),fg="gold",bg=bg_color)
        F4.place(x=680,y=200,width=325,height=380)

        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.Stock_Table=ttk.Treeview(F4, column=("item_no","item_name","qty","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("item_no",text="Item No")
        self.Stock_Table.heading("item_name",text="Item Name")
        self.Stock_Table.heading("qty",text="Qty")
        self.Stock_Table.heading("price",text="Price")
        self.Stock_Table['show']='headings'
        self.Stock_Table.column("item_no",width=30)
        self.Stock_Table.column("item_name",width=140)
        self.Stock_Table.column("qty",width=30)
        self.Stock_Table.column("price",width=20)
        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.Stock_Table.bind("<ButtonRelease-1>",self.work_on_focus)


        #=================Bill Area==================#

        F5=LabelFrame(self.root6,bd=10,relief=GROOVE)
        F5.place(x=1030,y=200,width=380,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold", bd=7,relief=GROOVE).pack(fill=X)

        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        F6=LabelFrame(self.root6,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",18,"bold"),bg=bg_color,fg="gold")
        F6.place(x=680,y=600,width=660,height=110)

        total_btn=Button(F6,bg="gold",command=self.print_bill,text="Print",fg="Black",width=7,bd=5,font="arial 18 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(F6,bg="gold",command=self.bill_area,text="Generate Bill",fg="Black",width=13,bd=5,font="arial 18 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(F6,bg="gold",command=self.clear12,text="Clear",fg="Black",width=7,bd=5,font="arial 18 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(F6,bg="gold",text="Exit",fg="Black",width=7,bd=5,font="arial 18 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
         
        

        #===============New functions==============

    def checkkey(self,event): 
       
        value = event.widget.get() 
        
       
        # get data from l 
        if value == '': 
            data = self.l 
        else: 
            data = [] 
            for item in self.l: 
                if value.lower() in item.lower(): 
                    data.append(item)                 
   
        # update data in listbox 
        self.update(data)
    def update(self,data): 
      
        # clear previous data 
        self.lb.delete(0, 'end') 
    
        # put new data 
        for item in data: 
            self.lb.insert('end', item)
    def search_item(self):
        if self.search_item_no.get()=="":
            messagebox.showerror("Error","No input entered")
            return
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute(f"select * from rst2 where Name='{self.search_item_no.get()}'")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Alert","No Item found")
        for row in rows:
            self.item_name1.set(row[0])
            self.item_name.set(row[1])
            self.item_price.set(row[4])
        con.commit()
        con.close()

    def add_item(self):

        ###########
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute(f"select * from rst2 where ID='{self.item_name1.get()}'")
        rows23=cur.fetchall()
        available_quantity=rows23[0][3]
        #########

        listOfEntriesInTreeView=self.Stock_Table.get_children()
        for each in listOfEntriesInTreeView:
            if int(self.Stock_Table.item(each)['values'][0])==int(self.item_name1.get()):
                new_quantity=int(self.Stock_Table.item(each)['values'][2])+int(self.item_quantity.get())
                if new_quantity<available_quantity or new_quantity==available_quantity:
                    self.Stock_Table.detach(each)
                    new_item=(self.item_name1.get(),self.item_name.get(),new_quantity,self.item_price.get()*new_quantity)
                    self.Stock_Table.insert('',END, values=new_item)
                    return
                else:
                    messagebox.showinfo("Alert","Available quantity is less.",parent=self.root6)
                    return
        if int(self.item_quantity.get())<available_quantity or int(self.item_quantity.get())==available_quantity:
            new_item=(self.item_name1.get(),self.item_name.get(),self.item_quantity.get(),self.item_price.get()*self.item_quantity.get())
            self.Stock_Table.insert('',END, values=new_item)

    def bill_area(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        total=0
        if self.c_phon.get()=='' or self.c_name.get()=='':
            messagebox.showinfo("Alert","Enter Customer details first",parent=self.root6)
            return

        elif self.calculateItemInCart()==0:
            messagebox.showinfo("Alert","Add items to cart",parent=self.root6)
            return

        self.welcome_bill()
        listOfEntriesInTreeView=self.Stock_Table.get_children()
        i=1

        cur.execute(f"select * from rst where f_name='{self.c_name.get()}' and contact={self.c_phon.get()}")
        rows=cur.fetchall()
        if len(rows)!=0:
            customer_id=rows[0][0] 
            messagebox.showinfo("Alert","Valued Customer",parent=self.root6)
            for each in listOfEntriesInTreeView:
                statement=f"insert into sales_stocks values ({self.bill_no.get()},{self.Stock_Table.item(each)['values'][0]},{self.Stock_Table.item(each)['values'][2]})"
                cur.execute(statement)
                con.commit()
                statement=f"update rst2 set QuantityLeft=QuantityLeft-{self.Stock_Table.item(each)['values'][2]} where ID={self.Stock_Table.item(each)['values'][0]}"
                cur.execute(statement)
                con.commit()
                total=total+int(self.Stock_Table.item(each)['values'][3])
                self.txtarea.insert(END,f"\n{i}\t{self.Stock_Table.item(each)['values'][1]}\t\t     {self.Stock_Table.item(each)['values'][2]}\t {self.Stock_Table.item(each)['values'][3]}")
                self.Stock_Table.detach(each)
                i=i+1
            self.txtarea.insert(END,f"\n=======================================")
            self.txtarea.insert(END,f"\n\t\t     Subtotal Rs. {total}")
            self.txtarea.insert(END,f"\n\t\t     Sales Tax Rs. {0.10*total}")
            self.txtarea.insert(END,f"\n\t\t     Discount Rs. {-0.10*total}")
            self.txtarea.insert(END,"\n---------------------------------------")
            self.txtarea.insert(END,f"\n\t\t\tTotal Rs.  {total+0.10*total-0.10*total}")
            self.txtarea.insert(END,"\n---------------------------------------")
            self.txtarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------Thanks for shopping------------")
            self.save_bill()

        #==============Save the bill to database================

            statement=f"insert into sales_bill values ({self.bill_no.get()},'{datetime.today().strftime('%Y-%m-%d')}',{total+0.1*total},{customer_id}) "
            cur.execute(statement)
            con.commit()
            con.close()
        else:
            customer_id=random.randint(1,1000)
            cur.execute(f"insert into customer values ({customer_id},'{self.c_name.get()}',{self.c_phon.get()})")
            messagebox.showinfo("Alert","New Customer",parent=self.root6)
            con.commit()  


            for each in listOfEntriesInTreeView:
                statement=f"insert into sales_stocks values ({self.bill_no.get()},{self.Stock_Table.item(each)['values'][0]},{self.Stock_Table.item(each)['values'][2]})"
                cur.execute(statement)
                con.commit()
                statement=f"update rst2 set QuantityLeft=QuantityLeft-{self.Stock_Table.item(each)['values'][2]} where ID={self.Stock_Table.item(each)['values'][0]}"
                cur.execute(statement)
                con.commit()
                total=total+int(self.Stock_Table.item(each)['values'][3])
                self.txtarea.insert(END,f"\n{i}\t{self.Stock_Table.item(each)['values'][1]}\t\t     {self.Stock_Table.item(each)['values'][2]}\t {self.Stock_Table.item(each)['values'][3]}")
                self.Stock_Table.detach(each)
                i=i+1
            self.txtarea.insert(END,f"\n=======================================")
            self.txtarea.insert(END,f"\n\t\t     Subtotal Rs. {total}")
            self.txtarea.insert(END,f"\n\t\t     Sales Tax Rs. {0.10*total}")
            
            self.txtarea.insert(END,"\n---------------------------------------")
            self.txtarea.insert(END,f"\n\t\t\tTotal Rs.  {total+0.10*total}")
            self.txtarea.insert(END,"\n---------------------------------------")
            self.txtarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------Thanks for shopping------------")
            self.save_bill()
            self.mail()

        #==============Save the bill to database================

            statement=f"insert into sales_bill values ({self.bill_no.get()},'{datetime.today().strftime('%Y-%m-%d')}',{total+0.1*total},{customer_id}) "
            cur.execute(statement)
            con.commit()
            con.close()

            

    def save_bill(self):
        self.bill_data=self.txtarea.get('1.0',END)
        B=self.bill_no.get()+".txt"
        f1=open(B,'w')
        f1.write(self.bill_data)
        f1.close()
        messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} saved Successfully.",parent=self.root6)
     

    def print_bill(self):
        B=self.bill_no.get()+".txt"
        win32api.ShellExecute (0,"print",B,'/d:"%s"' % win32print.GetDefaultPrinter (),".",0)
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to My Shop")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\nS.No  \tItem Name\t\t   Qty \tPrice")
        self.txtarea.insert(END,f"\n=======================================")

    def calculateItemInCart(self):
        listOfEntriesInTreeView=self.Stock_Table.get_children()
        i=0
        for each in listOfEntriesInTreeView:
            i=i+1
        return (i)


    def work_on_focus(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.item_name1.set(row[0])
        self.item_name.set(row[1])
        self.item_quantity.set(row[2])
        self.item_price.set(row[3])

    def clear12(self):
        self.Stock_Table.delete(*self.Stock_Table.get_children())
        self.item_name1.set("")
        self.item_name.set("")
        self.item_price.set(0)
        self.item_quantity.set(1)
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set(str(random.randint(1000,9999)))
        self.welcome_bill()

    def find_bill(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute(f"select * from sales_bill where inv_id={self.search_bill.get()}")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Not Found",f"Bill No. :{self.search_bill.get()} not found.",parent=self.root6)
            return
        inv_date=rows[0][1]
        inv_amount=rows[0][2]
        inv_id=rows[0][0]
        cur.execute(f"select * from customer where customer_id1={rows[0][3]}")
        rows=cur.fetchall()
        c_name=rows[0][1]
        c_phone=rows[0][2]
        self.txtarea.delete('1.0',END)
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to My Shop")
        self.txtarea.insert(END,f"\n Bill Number: {inv_id}")
        self.txtarea.insert(END,f"\n Bill Date: {inv_date}")
        self.txtarea.insert(END,f"\n Customer Name: {c_name}")
        self.txtarea.insert(END,f"\n Phone Number: {c_phone}")
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\nS.No  \tItem Name\t\t   Qty \tPrice")
        self.txtarea.insert(END,f"\n=======================================")

        cur.execute(f"select * from sales_stocks where inv_id={inv_id}")
        rows=cur.fetchall()
        i=1
        total=0
        for row in rows:
            cur.execute(f"select * from rst2 where ID={row[1]}")
            temp=cur.fetchall()
            self.txtarea.insert(END,f"\n{i}\t{temp[0][1]}\t\t     {row[2]}\t {temp[0][4]}")
            total=total+row[2]*temp[0][4]
            i=i+1
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\n\t\t     Subtotal Rs. {total}")
        self.txtarea.insert(END,f"\n\t\t     Sales Tax Rs. {0.10*total}")
        self.txtarea.insert(END,"\n---------------------------------------")
        self.txtarea.insert(END,f"\n\t\t\tTotal Rs.  {total+0.10*total}")
        self.txtarea.insert(END,"\n---------------------------------------")
        self.txtarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------Thanks for shopping------------")

    def show_rev(self):
        self.root7=Toplevel()
        self.root7.title("SELF MART MANAGEMENT SYSTEM")
        self.root7.geometry("1440x900+100+50")
        self.fg12=ImageTk.PhotoImage(file="Design.png")
        self.bg_image1=Label(self.root7,image=self.fg12)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)
        

        total=0.0
        today=(datetime.today().strftime('%Y-%m-%d'))
        print(str(time.localtime()[1]))
        
        
        Label(self.root7,bd=12,relief=GROOVE,bg="#074463",fg="white",text="REVENUE DETAILS",font=("times new roman",20,"bold")).pack(fill=X)
        title=Label(self.root7,bd=12,relief=GROOVE,bg="#074463",fg="white",text='Today: '+today,font=("times new roman",20,"bold")).place(x=150,y=80)
        month_btn=Button(self.root7,text="Current Month Revenue",command=self.month,cursor="hand2",bg="#FABA0A",fg="indigo",bd=5,font=("times new roman",18,"bold")).place(x=950,y=80)

        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from sales_bill")
        
        for i in cur:
          
            if i[1]==today:
                
                
                
                total+=float(i[2])
        
        Label(self.root7,bd=12,relief=GROOVE,text='Total Revenue Of Today: Rs '+str(total), bg='indigo',fg='white',font=("times new roman",20,"bold")).place(x=450,y=80)
        cx=0
        vsb=Scrollbar(self.root7,orient='vertical')
        lb1=Listbox(self.root7,width=30, yscrollcommand=vsb.set,bg="#2E4053",fg="white",font=("times new roman",20,"bold"),bd=12,relief=GROOVE)
        vsb.pack(side = RIGHT, fill = BOTH) 
        lb1.place(x=250,y=200)
        
        vsb.config( command = lb1.yview )
        cur.execute("select * from sales_bill")
        for i in cur:
            if i[1]==today:
                cx+=1
                lb1.insert(cx,'Bill No.  -  '+str(i[0])+'    : Rs '+str(i[2]))
        con.commit()

    def month(self):
        self.root7=Toplevel()
        self.root7.title("SELF MART MANAGEMENT SYSTEM")
        self.root7.geometry("1440x900+100+50")
        self.fg15=ImageTk.PhotoImage(file="Design.png")
        self.bg_image1=Label(self.root7,image=self.fg15)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)
        total=0.0
        today=str(time.localtime()[1])
        Label(self.root7,bd=12,relief=GROOVE,bg="#074463",fg="white",text="Current Month Details",font=("times new roman",20,"bold")).pack(fill=X)
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select * from sales_bill")
        for i in cur:
            if i[1][6]==today:
                total+=float(i[2])
        Label(self.root7,bd=12,relief=GROOVE,text='Total Revenue Of Month: Rs '+str(total), bg='indigo',fg='white',font=("times new roman",20,"bold")).place(x=450,y=80)
        cx=0
        vsb=Scrollbar(self.root7,orient='vertical')
        lb1=Listbox(self.root7,width=50, yscrollcommand=vsb.set,bg="#2E4053",fg="white",font=("times new roman",20,"bold"),bd=12,relief=GROOVE)
        vsb.pack(side = RIGHT, fill = BOTH) 
        lb1.place(x=250,y=200)
        vsb.config( command = lb1.yview )
        cur.execute("select * from sales_bill")
        for i in cur:
           
            if i[1][6]==today:
                cx+=1
                lb1.insert(cx,'Bill No.  -  '+str(i[0])+'    : Rs '+str(i[2])+'     : Date  -   '  +  str(i[1]))
        con.commit()

    def mail(self):

        msg = MIMEMultipart()
        msg['To'] = "parikhrishit20@gmail.com"
        msg['From'] = "parikhrishit20@gmail.com"
        msg['Subject'] = "Mail for Email Validation"
        from_email = "parikhrishit20@gmail.com"
        to_email = "parikhrishit20@gmail.com"
        password = "jbreefpeygxnswpz"
        ####filename=self.bill_no.get()+".txt"
        file=self.bill_no.get()+".txt"
        msg.attach(MIMEText("Labour"))
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(open(file, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(attachment)

                    
        
        #this is object of MIMEText which defined the type of content which you are going to send through mail
       
       
        
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())
        except Exception as error:
            print(error)
            
        else:
            print("Please Check your email....")
    def Valuations(self):     
        self.root8=Toplevel() 
        self.root8.geometry("1440x900+100+50")
        self.fg15=ImageTk.PhotoImage(file="Design.png")
        self.bg_image1=Label(self.root8,image=self.fg15)
        self.bg_image1.place(x=0,y=0,relwidth=1,relheight=1)
        Table_Frame=Frame(self.root8,bd=4,relief=GROOVE,bg="#EC7B51")
        Table_Frame.place(x=40,y=40,width=850,height=370)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                background="white",
                foreground="blue",
                rowheight=45,
                fieldbackground="white")
        style.map('Treeview',
            background=[('selected', 'indigo')])


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.login1_table=ttk.Treeview(Table_Frame,columns=("ID","Date","Amount","Customer ID","Customer_Name","Customer_Phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.login1_table.heading("ID",text="ID.")
        self.login1_table.heading("Date",text="Date")
        self.login1_table.heading("Amount",text="Amount.")
        self.login1_table.heading("Customer ID",text="Customer ID")
        self.login1_table.heading("Customer_Name",text="Customer_Name")
        self.login1_table.heading("Customer_Phone",text="Customer_Phone")

        self.login1_table['show']='headings'
        self.login1_table.column("ID",width=40)
        self.login1_table.column("Date",width=80)
        self.login1_table.column("Amount",width=50)
        self.login1_table.column("Customer ID",width=50)
        self.login1_table.column("Customer_Name",width=60)
        self.login1_table.column("Customer_Phone",width=60)
        


        self.login1_table.pack(fill=BOTH,expand=1)
        self.login1_table.bind("<ButtonRelease-1>")
        self.fetch5_data()
        
    def fetch5_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="rishit")
        cur=con.cursor()
        cur.execute("select inv_id, date, amount, customer_id1, customer_name, customer_phone from sales_bill inner join customer on customer_id = customer_id1")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.login1_table.delete(*self.login1_table.get_children())
            for row in rows:
                self.login1_table.insert('',END,values=row)
            
            con.commit()
        con.close()
         
   

        
        


       
    


root=Tk()
obj=Login1(root)
root.mainloop()    
















#Frame_login2=Frame(home,bg="dark slate gray",bd=10,relief=GROOVE)
#Frame_login2.place(x=500,y=650,height=350,width=380)
#Label(Frame_login2,text='**when moving to other windows, do not close this main window!',bg='#49A').grid(row=5,column=3)
#Label(Frame_login2,text='**sign in/create account to Start',bg='#49A').grid(row=6,column=3)
#Label(Frame_login2,text='GitHub: https://github.com/andrew-geeks',bg='#49A').grid(row=7,column=3)
#Label(Frame_login2,text='Twitter: https://twitter.com/andrewissac20',bg='#49A').grid(row=8,column=3)
#Label(Frame_login2,text='Instagram: https://www.instagram.com/_andrewissac',bg='#49A').grid(row=9,column=3)
#Label(Frame_login2,text='Read the tutorialin github on how to get around. Enjoy!!😀',bg='#49A').grid(row=10,column=3)
#home.mainloop()


