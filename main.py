from tkinter import *
import tkinter as tk
import tkinter.messagebox
import mysql.connector as sqlcon
import random as rd
from tkcalendar import *
from datetime import date
con=sqlcon.connect(host="localhost",user="root",password="Koustav@3214")
cur=con.cursor()
cur=con.cursor(buffered=True)
t=tk.Tk()
t.geometry("1350x830")
t.resizable(False,False)
bgimg=tk.PhotoImage(file=r"background.png")

def main():
    def lst_doc():
        def back1():
            l1.destroy()
            l2.destroy()
            for i in list2:
                i.destroy( )
            l4.destroy()
            for i in list3:
                i.destroy( )
            for i in list1:
                i.destroy( )
            b5.destroy()
            main()
        limg.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5=Button(text="BACK",font="Impact 19 bold",bg='violet',command=back1)
        b5.place(x=30,y=30)
        li=["Dr. sharma","Dr. Verma","Dr. Kumar","Dr. Khan","Dr. Kohli","Dr. singh","Dr. Sidharth","Dr. tendulkar","Dr. Virat","Dr. Leo",'Dr. Irfan','Dr. John',
        'Dr. Sanjay','Dr. Shahid']
        m=["Orthopaedic surgeon","Orthopaedic surgeon","Nephrologist","Nephrologist","Gynaecologist","Gynaecologist","Physician","Physician","Neurologist",
        "Neurologist",'X-ray','X-ray','X-ray','X-ray']
        n=[10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        l1=Label(t,text='NAME OF DOCTORS',font=('Times_New_Roman',15)) 
        l1.place(x=380,y=120)
        list1=["a1","b1","c1","d1","e1","f1","g1","h1","i1","j1","k1","l1","m1","n1"]
        count=140
        c=0
        for i in li:
            count=count+30
            list1[c]=Label(t,text=i,font=('Times_New_Roman',15))
            list1[c].place(x=380,y=count)
            c=c+1

        l2=Label(t,text='DEPARTMENT',font=('Times_New_Roman',15))
        l2.place(x=600,y=120)
        list2=["a2","b2","c2","d2","e2","f2","g2","h2","i2","j2","k2","l2","m2","n2"]
        count1=140
        c=0
        for i in m:
            count1=count1+30
            list2[c]=Label(t,text=i,font=('Times_New_Roman',15))
            list2[c].place(x=600,y=count1)
            c=c+1

        l4=Label(t,text='ROOM NO',font=('Times_New_Roman',15))
        l4.place(x=820,y=120)
        list3=["a3","b3","c3","d3","e3","f3","g3","h3","i3","j3","k3","l3","m3","n3"]
        count2=140
        c=0
        for i in n:
            count2=count2+30
            list3[c]=Label(t,text=i,font=('Times_New_Roman',15))
            list3[c].place(x=820,y=count2)
            c=c+1

    def ser_avail():
        def back2():
            
            l6.destroy()
            for i in list4:
                i.destroy( )
            l8.destroy()
            for i in list5:
                i.destroy( )
            b5.destroy()
            main()

        limg.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy() 
        b5=Button(text="BACK",font="Impact 19 bold",bg='violet',command=back2)
        b5.place(x=30,y=30)
        l6=Label(t,text='SERVICES AVAILABLE',font=('Times_New_Roman',15))
        l6.place(x=460,y=260)
        f=["ULTRASOUND","X-RAY","CT Scan","MRI","BLOOD COLLECTION","DIALYSIS","ECG","CHEMIST","LAB"]
        list4=["a4","b4","c4","d4","e4","f4","g4","h4","i4"]
        count1=280
        c=0
        for i in f:
            count1=count1+30
            list4[c]=Label(t,text=i,font=('Times_New_Roman',15))
            list4[c].place(x=460,y=count1)
            c=c+1
        l8=Label(t,text='ROOM NO.',font=('Times_New_Roman',15))
        l8.place(x=710,y=260)
        g=[1,2,3,4,5,6,7,8,9]
        list5=["a5","b5","c5","d5","e5","f5","g5","h5","i5"]
        count2=280
        c=0
        for i in g:
            count2=count2+30
            list5[c]=Label(t,text=i,font=('Times_New_Roman',15))
            list5[c].place(x=710,y=count2)
            c=c+1
 
    def register():
        
        def back1():
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            en4.destroy()
            en5.destroy()
            en6.destroy()
            en7.destroy()
            label9.destroy()
            b5.destroy()
            b6.destroy()
            cal.destroy()
            main()

        def appointment():
            
            token=rd.randint(1000,9999)
            nm=en1.get()
            idno=en2.get()
            phn=en3.get()
            age=en4.get()
            gen=clicked.get()
            cal_date=cal.get_date()
            time=clicked2.get()
            dept=clicked3.get()
            li=["Dr. sharma","Dr. Verma","Dr. Kumar","Dr. Khan","Dr. Kohli","Dr. singh","Dr. Sidharth","Dr. tendulkar","Dr. Virat","Dr. Leo",'Dr. Irfan','Dr. John',
                'Dr. Sanjay','Dr. Shahid']
            m=["Orthopaedic Surgeon","Orthopaedic Surgeon","Nephrologist","Nephrologist","Gynaecologist","Gynaecologist","Physician","Physician","Neurologist",
                "Neurologist",'X-ray','X-ray','X-ray','X-ray']
            n=[10,11,12,13,14,15,16,17,18,19,20,21,22,23]
            o=[]
            p=[]
            
            for i in range(len(m)):
                if m[i]==dept:
                    o.append(li[i])
                    p.append(n[i])
                    
            dr=rd.choice(o)
            a=o.index(dr)
            room=p[a]
            print(token)
            
            cur.execute("create database if not exists Hospital")
            cur.execute("use Hospital")
            cur.execute("create table if not exists appointment"
                        "("
                        "idno varchar(12) primary key,"
                        "name char(50),"
                        "age char(3),"
                        "gender char(1),"
                        "phone varchar(10),"
                        "date varchar(12),"
                        "time varchar(15),"
                        "doctor varchar(50),"
                        "dept varchar(30),"
                        "room varchar(3),"
                        "token int(10))")
            query='insert into appointment values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(idno,nm,age,gen,phn,cal_date,time,dr,dept,room,token)
            cur.execute(query)
            con.commit()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            en4.destroy()
            en5.destroy()
            en6.destroy()
            en7.destroy()
            label9.destroy()
            b5.destroy()
            b6.destroy()
            cal.destroy()
            main()
            r1=str(room)
            c1=str(cal_date)
            t1=str(token)
            tkinter.messagebox.showinfo("APPOINTMENT BOOKED","YOUR APPOINTMENT IS CONFIRMED\nNAME:"+nm+"\nAADHAR NO.:"+idno+"\nPHONE NO.:"+phn+"\nDOCTOR'S NAME:"+dr+"\nROOM NO.:"+r1+"\nAPPOINTMENT DATE:"+c1+"\nAPPOINTMENT TIME:"+time+"\nSECURITY PIN:"+t1)

            
            
        limg.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        today_date=date.today()
        y=today_date.year
        m=today_date.month
        d=today_date.day
        label1=Label(t,text='BOOK AN APPOINTMENT',font=('Times_New_Roman',25),background="LIGHT BLUE")
        label1.place(x=480,y=30)
        label2=Label(t,text='NAME',font=('Times_New_Roman',20))
        label2.place(x=75,y=150)
        en1=tkinter.Entry(t,font=('Times_New_Roman',20))
        en1.place(x=175,y=150)
        label3=Label(t,text='AADHAR CARD NO.',font=('Times_New_Roman',20))
        label3.place(x=530,y=150)
        en2=tkinter.Entry(t,font=('Times_New_Roman',20))
        en2.place(width=480,x=810,y=150)
        label4=Label(t,text='PHONE',font=('Times_New_Roman',20))
        label4.place(x=75,y=250)
        en3=tkinter.Entry(t,font=('Times_New_Roman',20))
        en3.place(x=175,y=250)
        label5=Label(t,text='AGE',font=('Times_New_Roman',20))
        label5.place(x=530,y=250)
        en4=tkinter.Entry(t,font=('Times_New_Roman',20))
        en4.place(width=200,x=600,y=250)
        label6=Label(t,text='GENDER(M/F)',font=('Times_New_Roman',20))
        label6.place(x=835,y=250)
        clicked=StringVar()
        en5=OptionMenu(t,clicked,"M","F","OTHERS")
        en5.place(width=100,x=1080,y=250)
        label7=Label(t,text='SELECT DATE',font=('Times_New_Roman',20))
        label7.place(x=75,y=350)
        cal=Calendar(t,selectmode="day",year=y,month=m,day=d)
        cal.place(width=410,x=75,y=400)
        label8=Label(t,text="SELECT TIME",font=('Times_New_Roman',20))
        label8.place(x=530,y=350)
        clicked2=StringVar()
        en6=OptionMenu(t,clicked2,"10:00 A.M.","11:00 A.M.","12:00 P.M.","01:00 P.M.","02:00 P.M.","03:00 P.M.","04:00 P.M.","05:00 P.M.","06:00 P.M.","07:00 P.M.")
        en6.place(width=95,x=715,y=350)
        b5=Button(text="BACK",font="Impact 19 bold",bg='violet',command=back1)
        b5.place(x=30,y=30)
        label9=Label(t,text='SELECT DEPARTMENT',font=('Times_New_Roman',20))
        label9.place(x=835,y=350)
        clicked3=StringVar()
        en7=OptionMenu(t,clicked3,"Orthopaedic Surgeon","Physician","Nephrologist","Neurologist","Gynaecologist","X-ray")
        en7.place(width=150,x=1140,y=350)
        b6=Button(t,text="BOOK APPOINTMENT",font="Impact 19 bold",bg='sea green',command=appointment)
        b6.place(x=550,y=620)
        
    def details():
        def back1():
            l1.destroy()
            l2.destroy()
            box.destroy()
            b.destroy()
            b5.destroy()
            main()
          

        def check():
            def back3():
                label.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                label6.destroy()
                label7.destroy()
                label8.destroy()
                label9.destroy()
                label10.destroy()
                label11.destroy()
                label12.destroy()
                back.destroy()
                cancelb.destroy()
                details()
            a=box.get()
            cur.execute("use hospital")
            cur.execute("select * from appointment")
            l=cur.fetchall()
            m=[]
            for i in l:
                m.append(i[0])
            def cancel():
                cur.execute("delete from appointment where idno='{}'".format(a))
                con.commit()
                label.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                label6.destroy()
                label7.destroy()
                label8.destroy()
                label9.destroy()
                label10.destroy()
                label11.destroy()
                label12.destroy()
                back.destroy()
                cancelb.destroy()
                details()
                tkinter.messagebox.showinfo("DELETED","Appointment cancelled!!!")
            if a in m:
                l1.destroy()
                l2.destroy()
                box.destroy()
                b.destroy()
                b5.destroy()
                label=Label(text=" YOUR APPOINTMENT DETAILS -",font="algerian 28 bold",bg="green")
                label.pack()
                statement="select * from appointment where idno='{}'".format(a)
                cur.execute(statement)
                data=cur.fetchone()
                a1=data[0]
                a2=data[1]
                a3=data[2]
                a4=data[3]
                a5=data[4]
                a6=data[5]
                a7=data[6]
                a8=data[7]
                a9=data[8]
                a10=data[9]
                a11=data[10]
                
                

                label2=Label(text="NAME: "+a2,font="algerian 18 bold")
                label2.place(x=40,y=200)
                label3=Label(text="AADHAR NO.: "+a1,font="algerian 18 bold")
                label3.place(x=370,y=200)
                label4=Label(text="PHONE NO.: "+a5,font="algerian 18 bold")
                label4.place(x=750,y=200)
                label5=Label(text="AGE: "+a3,font="algerian 18 bold")
                label5.place(x=1065,y=200)
                label6=Label(text="SEX: "+a4,font="algerian 18 bold")
                label6.place(x=1190,y=200)
                label7=Label(text="DOCTOR: "+a8,font="algerian 18 bold")
                label7.place(x=40,y=300)
                label8=Label(text="DEPARTMENT: "+a9,font="algerian 18 bold")
                label8.place(x=315,y=300)
                label9=Label(text="ROOM: "+a10,font="algerian 18 bold")
                label9.place(x=700,y=300)
                label10=Label(text="DATE: "+a6,font="algerian 18 bold")
                label10.place(x=850,y=300)
                label11=Label(text="TIME: "+a7,font="algerian 18 bold")
                label11.place(x=1085,y=300)
                label12=Label(text="SECURITY PIN: "+str(a11),font="algerian 18 bold")
                label12.place(x=550,y=400)
                back=Button(text="BACK",font="Impact 19 bold",bg='violet',command=back3)
                back.place(x=30,y=0)
                cancelb=Button(text="CANCEL APPOINTMENT",font="Impact 19 bold",bg='light blue',command=cancel)
                cancelb.place(x=550,y=550)
                
            else:
                tkinter.messagebox.showinfo("ALERT","NO APPOINTMENTS BOOKED!!!")    
        limg.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        l1=Label(text="CHECK YOUR APPOINTMENT DETAILS -",font="algerian 28 bold",bg="cyan")
        l2=Label(text="Enter Aadhar no.: ",font="Times_New_Roman 26")
        box=Entry(font="Times_New_Roman 26")
        b=Button(text="check details",font="Impact 19 bold",bg="purple",command=check)
        b5=Button(text="BACK",font="Impact 19 bold",bg='violet',command=back1)
        b.place(x=570,y=460)
        box.place(x=620,y=240)
        l2.place(x=330,y=240)
        l1.pack()
        b5.place(x=30,y=10)
    
    limg=Label(t,i=bgimg)
    limg.pack()
    b1=Button(text="Book an Appointment",font="Impact 19 bold",bg='yellow',command=register)
    b2=Button(text="View List of Doctors",font="Impact 19 bold",bg='yellow',command=lst_doc)
    b3=Button(text="See available Services",font="Impact 18 bold",bg='yellow',command=ser_avail)
    b4=Button(text="See appointment details",font='Impact 17 bold',bg='yellow',command=details)
    b1.place(x=675,y=465)
    b2.place(x=1005,y=465)
    b3.place(x=675,y=565)
    b4.place(x=1005,y=565)
main()
t.mainloop()