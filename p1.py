from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import random
import requests
from bs4 import BeautifulSoup

s = requests.Session()
url = 'https://randomwordgenerator.com/json/inspirational-quote.json'
response = s.get(url)
# print(response)

data = response.json()['data']
while True:
    random_quote = random.sample(data, 1)
    quote = random_quote[0]['inspirational_quote']
    quote = BeautifulSoup(quote, 'lxml').text
    if len(quote)<=60:
        break

#print(quote)



def f1():
	mw.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	mw.deiconify()
def f3():
	mw.withdraw()
	vw.deiconify()
	
	vw_emp_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect("abc.db")
		cursor = con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " id =  " + str(d[0]) + ": name=  " + str(d[1]) + ": salary=  " + str(d[2]) +"\n"
		vw_emp_data.insert(INSERT, info)
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close()
def f4():
	vw.withdraw()
	mw.deiconify()
def f5():
	mw.withdraw()
	uw.deiconify()

def f6():
	uw.withdraw()
	mw.deiconify()
def f7():
	mw.withdraw()
	dw.deiconify()
def f8():
	dw.withdraw()
	mw.deiconify()
def f9():
	
	con = None
	try:
		con = connect("abc.db")
		id = aw_ent_id.get()
		name = aw_ent_name.get()
		salary = aw_ent_salary.get()
		if (len(id)==0 and len(name)==0 and len(salary)==0):
					messagebox.showerror("Error","Id, Name and Salary are not entered\nPlease fill the details properly")
		else:
			id = aw_ent_id.get()
			if len(id) == 0:
				messagebox.showerror("Mistake","Id can't be empty")
				aw_ent_id.delete(0, END)
				aw_ent_id.focus()
				return


			elif not id.isdigit():
				messagebox.showerror("Mistake","Id should have only Positive integers")    
				aw_ent_id.delete(0, END)
				aw_ent_id.focus()
				return

			elif int(id)<=0 :
				messagebox.showerror("Mistake","Id should have only Positive integers")
				aw_ent_id.delete(0, END)
				aw_ent_id.focus()
				return

			
			else:
				id=int(id)
		
	
		

			name = aw_ent_name.get()
			if len(name)==0:
				messagebox.showerror("Mistake","Name can't be empty")
				aw_ent_name.delete(0, END)
				aw_ent_name.focus()
				return

				
			elif not str(name).isalpha():
				messagebox.showerror("Mistake","Name should be alphabets")
				aw_ent_name.delete(0, END)
				aw_ent_name.focus()
				return
    

			elif len(name)<=1:
				messagebox.showerror("Mistake","Name should be more than 2 alphabets,eg.om")
				aw_ent_name.delete(0, END)
				aw_ent_name.focus()
				return

			else:
				name=name

			salary = aw_ent_salary.get()
			if len(salary) == 0:
				messagebox.showerror("Mistake","Salary can't be empty")
				aw_ent_salary.delete(0, END)
				aw_ent_salary.focus()
				return

			elif not salary.isdigit():
				messagebox.showerror("Mistake","Salary should have only Positive integers")  
				aw_ent_salary.delete(0, END)
				aw_ent_salary.focus()
				return

		
			elif(float(salary) < 8000) :
				messagebox.showerror("Mistake","Salary should be more than 8k")
				aw_ent_salary.delete(0, END)
				aw_ent_salary.focus()
				return

  
			else:
				salary=float(salary)
	
		
		
	


		
			cursor = con.cursor()
			sql = "insert into employee values('%s', '%s' ,'%s')"
			cursor.execute(sql % (id, name,salary))
			con.commit()
			showinfo("Success", "record saved")	
			aw_ent_id.delete(0, END)
			aw_ent_name.delete(0, END)	
			aw_ent_salary.delete(0, END)
			aw_ent_id.focus()


	except DatabaseError as e:
		messagebox.showerror("Error","Id already exists")
		aw_ent_id.delete(0, END)
		aw_ent_id.focus()
		con.rollback()
	
	finally:
		if con is not None:
			con.close()



		
def f10():
	
	con = None
	try:
		con = connect("abc.db")
		id = uw_ent_id.get()
		name = uw_ent_name.get()
		salary = uw_ent_salary.get()
		if (len(id)==0 and len(name)==0 and len(salary)==0):
					messagebox.showerror("Error","Id, Name and Salary are not entered\nPlease fill the details properly")
		else:
			id = uw_ent_id.get()
			if len(id) == 0:
				messagebox.showerror("Mistake","Id can't be empty")
				uw_ent_id.delete(0, END)
				uw_ent_id.focus()
				return


			elif not id.isdigit():
				messagebox.showerror("Mistake","Id should have only Positive integers")    
				uw_ent_id.delete(0, END)
				uw_ent_id.focus()
				return

			elif int(id)<=0 :
				messagebox.showerror("Mistake","Id should have only Positive integers")
				uw_ent_id.delete(0, END)
				uw_ent_id.focus()
				return

			
			else:
				id=int(id)
		
	
		

			name = uw_ent_name.get()
			if len(name)==0:
				messagebox.showerror("Mistake","Name can't be empty")
				uw_ent_name.delete(0, END)
				uw_ent_name.focus()
				return

				
			elif not str(name).isalpha():
				messagebox.showerror("Mistake","Name should be alphabets")
				uw_ent_name.delete(0, END)
				uw_ent_name.focus()
				return
    

			elif len(name)<=1:
				messagebox.showerror("Mistake","Name should be more than 2 alphabets,eg.om")
				uw_ent_name.delete(0, END)
				uw_ent_name.focus()
				return

			else:
				name=name

			salary = uw_ent_salary.get()
			if len(salary) == 0:
				messagebox.showerror("Mistake","Salary can't be empty")
				uw_ent_salary.delete(0, END)
				uw_ent_salary.focus()
				return

			elif not salary.isdigit():
				messagebox.showerror("Mistake","Salary should have only Positive integers")  
				uw_ent_salary.delete(0, END)
				uw_ent_salary.focus()
				return

		
			elif(float(salary) < 8000) :
				messagebox.showerror("Mistake","Salary should be more than 8k")
				uw_ent_salary.delete(0, END)
				uw_ent_salary.focus()
				return

  
			else:
				salary=float(salary)
	
		
		

		
			cursor = con.cursor()
			sql = "update employee set name='%s', salary='%s' where id='%s'"
			cursor.execute(sql % (name,salary,id))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Success", "record updated")
				uw_ent_id.delete(0, END)
				uw_ent_name.delete(0, END)	
				uw_ent_salary.delete(0, END)
				uw_ent_id.focus()

			else:
				raise Exception("record dose not exists")	
				uw_ent_id.delete(0, END)
				uw_ent_name.delete(0, END)	
				uw_ent_salary.delete(0, END)
				uw_ent_id.focus()


	except Exception as e:
		showerror("Mistake", e)
		uw_ent_id.delete(0, END)
		uw_ent_id.focus()

	finally:
		if con is not None:
			con.close()



def f11():
	id = dw_ent_id.get()
	con = None
	try:
		
		if len(id) == 0:
			raise Exception("id can't be empty")

		if not str(id).isnumeric():
			raise Exception("id should have only Positive integers")    
		else:
			id=int(id)
		
		if id <=0 :
			raise Exception("id should have only Positive integers")
		
		con = connect("abc.db")
		cursor = con.cursor()
		sql = "delete from employee where id='%s'"
		cursor.execute(sql%(id))
		if cursor.rowcount==1:
			con.commit()
			showinfo("Success", "record deleted")
		else:
			raise Exception("record dose not exists")
		dw_ent_id.delete(0, END)
		dw_ent_id.focus()
	except Exception as e:
		showerror("Mistake", e)
		dw_ent_id.delete(0, END)
		dw_ent_id.focus()
	finally:
		if con is not None:
			con.close()

def f12():
		
	mydb =connect(database="abc.db")
	mycursor = mydb.cursor()
	mycursor.execute("select distinct salary,name from employee order by salary desc limit 5; ")

	result = mycursor.fetchall
	Names = []
	Salary = []
 

	for i in mycursor:
		Salary.append(i[0])
		Names.append(i[1])

	print("Name of employee = ", Names)
	print("Salary of employee = ", Salary)
	plt.bar(Names, Salary)

	plt.ylim(0, 500000)

	plt.xlabel("Name of Employee")

	plt.ylabel("Salary of Employee")

	plt.title("Top 5 Salary employee")
	plt.show()
	
mw=Tk()
mw.title("E.M.S")
mw.geometry("800x600+100+100")
f=("Times New Roman",20,"bold")
mw.resizable(False,False)
mw_btn_add=Button(mw,text="Add",font=f,width=15,command=f1)
mw_btn_view=Button(mw,text="View",font=f,width=15,command=f3)
mw_btn_update=Button(mw,text="Update",font=f,width=15,command=f5)
mw_btn_delete=Button(mw,text="Delete",font=f,width=15,command=f7)
mw_btn_chart=Button(mw,text="Chart",font=f,width=15,command=f12)
lblQuote=Label(mw,text="Quote:"+quote,font=("Times New Roman",20,'bold'),bg="light yellow")

mw.configure(bg="light yellow")

y=10
mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)
mw_btn_update.pack(pady=y)
mw_btn_delete.pack(pady=y)
mw_btn_chart.pack(pady=y)
lblQuote.pack(pady=y)

aw=Toplevel(mw)
aw.title("Add Emp")
aw.geometry("800x600+100+100")
aw.configure(bg="light gray")
aw.resizable(False,False)
aw_lab_id=Label(aw,text="enter id:",font=f,bg="light gray")
aw_ent_id=Entry(aw,font=f,bd=4)
aw_lab_name=Label(aw,text="enter name:",font=f,bg="light gray")
aw_ent_name=Entry(aw,font=f,bd=4)
aw_lab_salary=Label(aw,text="enter salary:",font=f,bg="light gray")
aw_ent_salary=Entry(aw,font=f,bd=4)
aw_btn_save=Button(aw,text="Save",font=f,command=f9)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)

y=10
aw_lab_id.pack(pady=y)
aw_ent_id.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_ent_name.pack(pady=y)
aw_lab_salary.pack(pady=y)
aw_ent_salary.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_btn_back.pack(pady=y)

aw.withdraw()

vw = Toplevel(mw)
vw.title("View Emp")
vw.geometry("800x600+100+100")
vw.configure(bg="pink")
vw.resizable(False,False)
vw_emp_data = ScrolledText(vw, width=40, height=10, font=f,bg="pink")
vw_btn_back = Button(vw, text="Back", font=f,command=f4)

vw_emp_data.pack(pady=y)
vw_btn_back.pack(pady=y)
vw.withdraw()

uw = Toplevel(mw)
uw.title("Update Emp")
uw.geometry("800x600+100+100")
uw.configure(bg="peach puff")
uw.resizable(False,False)
uw_lab_id=Label(uw,text="enter id:",font=f,bg="peach puff")
uw_ent_id=Entry(uw,font=f,bd=4)
uw_lab_name=Label(uw,text="enter name:",font=f,bg="peach puff")
uw_ent_name=Entry(uw,font=f,bd=4)
uw_lab_salary=Label(uw,text="enter salary:",font=f,bg="peach puff")
uw_ent_salary=Entry(uw,font=f,bd=4)
uw_btn_save=Button(uw,text="Save",font=f,command=f10)
uw_btn_back=Button(uw,text="Back",font=f,command=f6)

y=10
uw_lab_id.pack(pady=y)
uw_ent_id.pack(pady=y)
uw_lab_name.pack(pady=y)
uw_ent_name.pack(pady=y)
uw_lab_salary.pack(pady=y)
uw_ent_salary.pack(pady=y)
uw_btn_save.pack(pady=y)
uw_btn_back.pack(pady=y)

uw.withdraw()

dw = Toplevel(mw)
dw.title("Delete Emp")
dw.geometry("800x600+100+100")
dw.configure(bg="light blue")
dw.resizable(False,False)
dw_lab_id=Label(dw,text="enter id:",font=f,bg="light blue")
dw_ent_id=Entry(dw,font=f,bd=4)

dw_btn_save=Button(dw,text="Save",font=f,command=f11)
dw_btn_back=Button(dw,text="Back",font=f,command=f6)

y=10
dw_lab_id.pack(pady=y)
dw_ent_id.pack(pady=y)

dw_btn_save.pack(pady=y)
dw_btn_back.pack(pady=y)

dw.withdraw()

mw.mainloop()