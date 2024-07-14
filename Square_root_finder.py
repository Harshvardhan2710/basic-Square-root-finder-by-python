from tkinter import * 
root = Tk()
root.title("Square root Finder by Kamal sir")
root.geometry("1000x400+40+40")
f = ("century", 30, "bold")

def find():
	try:
		n = float(ent_num.get())
		r = n ** 0.5
		msg = "square root = " + str(round(r,2))
		lab_ans.configure(text=msg)
	except ValueError:
		msg = "u should enter numbers only"
		lab_ans.configure(text=msg)
	except TypeError:
		msg = "u should enter +ve numbers only"
		lab_ans.configure(text=msg)
lab_num = Label(root, text="Enter Number", font=f)
ent_num = Entry(root, font=f)
btn_find = Button(root, text="Find Square", font=f,command=find)
lab_ans = Label(root,font=f)

lab_num.place(x=50,y=50)
ent_num.place(x=400, y=50)
btn_find.place(x=400, y=130)
lab_ans.place(x=400, y=250)

root.mainloop()