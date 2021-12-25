from tkinter import *
from tkinter import ttk
import json
from tkinter import font

# open file
try:
    file_one = open("grade.json", 'r')
except:
    raise FileNotFoundError
else:
    json_obj = json.load(file_one)
    #print(json_obj['A'])
    
    l = []
    # function to calculate total
    def calculate_total():
        global l
        total = 0
        for value in l:
            total += float(json_obj[(value.upper())])
        total /= len(l)
        return total
    
finally:
    file_one.close()
        
        
# create object
root = Tk()

# title
root.title('GPA Calculator')

# adjust size
root.geometry("500x600")

# create treeview
my_tree = ttk.Treeview(root)

# define our columns
my_tree['columns'] = ("Name of Class", "Grade")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name of Class", anchor=CENTER, width=350)
my_tree.column("Grade", anchor=CENTER, width=100)

# Create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name of Class", text="Name of Class", anchor=CENTER)
my_tree.heading("Grade", text="Grade", anchor=W)


# Pack to the screen
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# Labels
nc = ttk.Label(add_frame, text="Name of Class")
nc.grid(row=1, column=0)

gd = ttk.Label(add_frame, text="Grade")
gd.grid(row=1, column=1)


# Entry boxes
name_box = ttk.Entry(add_frame, width=50)
name_box.grid(row=2, column=0)

grade_box = ttk.Entry(add_frame)
grade_box.grid(row=2, column=1)

# function section
# add function
count = 0
def add_record():
    global count, l
    
    my_tree.insert(parent='', index='end', iid= count, text="", values=(name_box.get(), grade_box.get()))
    count += 1
    
    l.append(grade_box.get())
    
    name_box.delete(0, END)
    grade_box.delete(0, END)
    

# remove all funtion
def remove_all():
    global l
    l = []
    for record in my_tree.get_children():
        my_tree.delete(record)
        
        
# remove one
def remove_one():
    global l
    for record in my_tree.selection():
        curItem = my_tree.focus()
        l.remove(my_tree.item(curItem)['values'][1])
        my_tree.delete(record)
        

# creating pop up for the gpa
def pop_up():
    top = Toplevel(root)
    top.geometry("200x200")
    top.title("Hello")
    
    # calling function
    gpa = calculate_total()
    
    Label(top, text=f"Your Gpa is: {format(gpa, '.3f')}", font=("Arial", 16)).place(x=10, y=50)

# Buttons
# add 
add_record = ttk.Button(root, text="Add record", command=add_record)
add_record.pack(pady=10)

# Remove all
remove_all = ttk.Button(root, text="Remove All", command=remove_all)
remove_all.pack(pady=10)

# Remove one
remove_one = ttk.Button(root, text="Remove selected", command=remove_one)
remove_one.pack(pady=10)

# Find accumalitive GPA
acg_showinfo = ttk.Button(root, text="Get Accumalitive GPA", command=pop_up)
acg_showinfo.pack(pady=10)

# set up for tkinter
root.mainloop()