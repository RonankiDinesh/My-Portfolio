import tkinter as tk
from tkinter import messagebox,ttk
from datetime import datetime
from tkcalendar import DateEntry

class Task :
    def __init__(self,name,priority,due_date) :
        self.name = name
        self.priority = priority
        self.due_date = due_date

class manager_app:
    def __init__(self,root) :
        self.root = root
        self.root.title('Task Manager')
        self.tasks= []

        self.task_name_var = tk.StringVar()
        self.task_priority_var= tk.StringVar()
        self.task_duedate_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root,text = "Task Name",bg ='#99FFFF').grid(row=0, column = 0 ,sticky="w")

        task_name_entry = tk.Entry(self.root,textvariable= self.task_name_var)
        task_name_entry.grid(row=0 , column = 1,padx = 10,pady=5)

        tk.Label(self.root, text = "Priority",bg ='#99FFFF').grid(row=1, column=0,sticky="w")

        priority_values= ["Not So Important", "Moderate","Very Important"]
        priority_entry = ttk.Combobox(self.root,textvariable=self.task_priority_var,values=priority_values)
        priority_entry.grid(row=1,column=1,padx=10,pady=5)

        tk.Label(self.root , text="Due Date : " ,bg ='#99FFFF').grid(row=2,column=0,sticky="w")

        due_date_entry = DateEntry(self.root,bg ='#99FFFF',textvariable= self.task_duedate_var,date_pattern = "yyyy-mm-dd")
        due_date_entry.grid(row= 2 , column = 1,padx = 10 ,pady=5)

        add_task_button=tk.Button(self.root,bg ='#99FFFF',text= "Add Task" ,command = self.add_task)
        add_task_button.grid(row = 3 , column = 0, columnspan = 2,padx=10,pady=5)

        self.task_list = ttk.Treeview(self.root, columns = ("Priority","Due Date"))
        self.task_list.grid(row=4,column=0,columnspan=2,padx=10,pady=5)
        self.task_list.heading("#0",text ="Task Name")
        self.task_list.heading("Priority",text= "Priority")
        self.task_list.heading("Due Date",text="Due Date")

        delete_task = tk.Button(self.root,bg ='#99FFFF',text= "Delete Task",command=self.delete_task)
        delete_task.grid(row=5,column=0,padx=10,pady=5,sticky="w")
        
        clear_task = tk.Button(self.root ,bg ='#99FFFF', text = "Clear Task",command = self.clear_task)
        clear_task.grid(row = 5,column=1 , padx=10,pady=5,sticky="e")

    def add_task(self):
        name = self.task_name_var.get()
        priority = self.task_priority_var.get()
        due_date = self.task_duedate_var.get()

        if name and priority and due_date:
            task = Task(name,priority,due_date)

            self.tasks.append(task)
          
            self.task_list.insert("",tk.END,text = task.name,values = (task.priority,task.due_date))
            
            self.task_name_var.set("")
            self.task_priority_var.set("")
            self.task_duedate_var.set("")

        else :
            messagebox.showerror("Error", "Please Fill in all the fields")

    def delete_task(self):
        selected_item = self.task_list.selection()

        if selected_item:
            task_name = self.task_list.item(selected_item)["text"]

            for task in self.tasks:
                if task.name == task_name:
                    self.tasks.remove(task)
                    self.task_list.delete(selected_item)                   
                    break
   
    def clear_task(self):
        self.task_name_var.set("")
        self.task_priority_var.set("")
        self.task_duedate_var.set("")

if __name__ == "__main__":
    root=tk.Tk()
    root.configure(bg="#FF9999") 
    app = manager_app(root)
    root.mainloop()