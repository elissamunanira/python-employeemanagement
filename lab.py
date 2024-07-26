import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('Employee Management System')
app.geometry('840x400')
app.config(bg='#161C25')
app.resizable(False, False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

def add_to_treeview():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

def insert():
    id = id_entry.get()
    name = name_entry.get()
    role = role_entry.get()
    gender = variable1.get()
    status = status_entry.get()
    if not (id and name and role and gender and status):
        messagebox.showerror('Error', 'Enter all fields.')
    elif database.id_exists(id):
        messagebox.showerror('Error', 'ID already exists')
    else:
        database.insert_employee(id, name, role, gender, status)
        add_to_treeview()
        messagebox.showinfo('Success', 'Data inserted successfully')

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    role_entry.delete(0, END)
    variable1.set('Male')
    status_entry.delete(0, END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        role_entry.insert(0, row[2])
        variable1.set(row[3])
        status_entry.insert(0, row[4])
    else:
        pass

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an employee to delete')
    else:
        id = id_entry.get()
        database.delete_employee(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Employee deleted successfully')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an employee to update')
    else:
        id = id_entry.get()
        name = name_entry.get()
        role = role_entry.get()
        gender = variable1.get()
        status = status_entry.get()
        database.update_employee(name, role, gender, status, id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Employee updated successfully')

# Define column names for the Treeview
column_names = ['ID', 'Name', 'Role', 'Gender', 'Status']

def search():
    search_term = search_entry.get().lower().strip() 
    search_column = search_column_var.get()

    employees = database.fetch_employees()
    tree.delete(*tree.get_children())

    for employee in employees:
        # Search across all columns if is selected
        if search_column == "All":
            if any(search_term in str(value).lower() for value in employee):
                tree.insert('', END, values=employee)
        # Search within a specific column
        else:
            column_index = column_names.index(search_column) 
            if search_term in str(employee[column_index]).lower():
                tree.insert('', END, values=employee)

id_label = customtkinter.CTkLabel(app, font=font1, text='ID:', text_color='#fff', bg_color='#161c25')
id_label.place(x=20, y=20)

id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
id_entry.place(x=100, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text='Name:', text_color='#fff', bg_color='#161c25')
name_label.place(x=20, y=80)

name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
name_entry.place(x=100, y=80)

role_label = customtkinter.CTkLabel(app, font=font1, text='Role:', text_color='#fff', bg_color='#161c25')
role_label.place(x=20, y=140)

role_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
role_entry.place(x=100, y=140)

gender_label = customtkinter.CTkLabel(app, font=font1, text='Gender:', text_color='#fff', bg_color='#161c25')
gender_label.place(x=20, y=200)

options = ['Male', 'Female']
variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', button_hover_color='#09c295', width=180, variable=variable1, values=options, state='readonly')
gender_options.set('Male')
gender_options.place(x=100, y=200)

status_label = customtkinter.CTkLabel(app, font=font1, text='Status:', text_color='#fff', bg_color='#161c25')
status_label.place(x=20, y=260)

status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
status_entry.place(x=100, y=260)

# Define Buttons for actions
add_button = customtkinter.CTkButton(app, command=insert, font=font1, text_color='#fff', text='Add Employee', fg_color='#008CBA', bg_color='#161C25', corner_radius=15, width=180)
add_button.place(x=20, y=310)

clear_button = customtkinter.CTkButton(app, command=lambda: clear(TRUE), font=font1, text_color='#fff', text='New Employee', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=180)
clear_button.place(x=210, y=310)

update_button = customtkinter.CTkButton(app, command=update, font=font1, text_color='#fff', text='Update Employee', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=180)
update_button.place(x=400, y=310)

delete_button = customtkinter.CTkButton(app, command=delete, font=font1, text_color='#fff', text='Delete Employee', fg_color='#AE0000', hover_color='#AE0000', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=180)
delete_button.place(x=600, y=310)

# Treeview setup for displaying employees
style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#fff', background='#000')
style.map('Treeview', background=[('selected', '#1A8F2D')])

tree = ttk.Treeview(app, height=15)
tree['columns'] = ('ID', 'Name', 'Role', 'Gender', 'Status')

# Define columns in the Treeview
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=120)
tree.column('Name', anchor=tk.CENTER, width=120)
tree.column('Role', anchor=tk.CENTER, width=120)
tree.column('Gender', anchor=tk.CENTER, width=100)
tree.column('Status', anchor=tk.CENTER, width=100)

# Define headings for the Treeview
tree.heading('#0', text='', anchor=tk.CENTER)
tree.heading('ID', text='ID', anchor=tk.CENTER)
tree.heading('Name', text='Name', anchor=tk.CENTER)
tree.heading('Role', text='Role', anchor=tk.CENTER)
tree.heading('Gender', text='Gender', anchor=tk.CENTER)
tree.heading('Status', text='Status', anchor=tk.CENTER)

tree.bind('<ButtonRelease-1>', display_data)  # Bind click event for row selection
tree.place(x=600, y=80)  # Adjusted placement for Treeview

# # Scrollbar setup for the Treeview
# tree_scroll = ttk.Scrollbar(app)
# tree_scroll.configure(command=tree.yview)
# tree.configure(yscrollcommand=tree_scroll.set)
# tree_scroll.place(x=800, y=80, height=310)

# Add search functionality
search_label = customtkinter.CTkLabel(app, font=font2, text='', text_color='#fff', bg_color='#161C25')
search_label.place(x=400, y=20)

search_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
search_entry.place(x=400, y=20)

search_column_var = StringVar(value='All')  # Default to "All" columns

search_column_label = customtkinter.CTkLabel(app, font=font2, text='', text_color='#fff', bg_color='#161C25')
search_column_label.place(x=300, y=20)

# Dropdown for selecting search column
search_column_menu = customtkinter.CTkOptionMenu(
    app,
    variable=search_column_var,
    values=["All", "ID", "Name", "Role", "Gender", "Status"],
    font=font2,
    text_color='#000',
    width=100
)
search_column_menu.place(x=590, y=20)

search_button = customtkinter.CTkButton(app, command=search, font=font2, text_color='#fff', text='Search', fg_color='#008CBA', bg_color='#161C25', corner_radius=5, width=80)
search_button.place(x=700, y=20)

# Populate Treeview with initial data
add_to_treeview()

# Start the application
app.mainloop()
