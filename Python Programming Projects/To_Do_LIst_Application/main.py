# importing the required modules  
import tkinter as tk                   
from tkinter import ttk                  
from tkinter import messagebox        
import sqlite3 as sql                    
  
# defining the function to add tasks to the list  
def create_task():  
    task_string = task_field.get()  
    # checking whether the string is empty or not  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))   
        list_update()   
        task_field.delete(0, 'end')  
  
# defining the function to update the list  
def list_update():   
    clear_list()  
    # iterating through the strings in the list  
    for task in tasks:  
        task_listbox.insert('end', task)  
  
# defining the function to delete a task from the list  
def delete_task():    
    try:  
        the_value = task_listbox.get(task_listbox.curselection())   
        if the_value in tasks:   
            tasks.remove(the_value)   
            list_update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# function to delete all tasks from the list  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')   
    if message_box == True:  
        # using while loop to iterate through the tasks list until it's empty   
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')   
        list_update()  
  
# function to clear the list  
def clear_list():  
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():  
    print(tasks)  
    # using the destroy() method to close the application  
    guiWindow.destroy()  
  
# function to retrieve data from the database  
def retrieve_database():  
    # using the while loop to iterate through the elements in the tasks list  
    while(len(tasks) != 0):  
        tasks.pop()  
    # iterating through the rows in the database table to append 
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  
# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class and giving it title and geomatry 
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List Manager - JAVATPOINT")   
    guiWindow.geometry("500x450+750+250")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
  
    # using the connect() method to connect to the database and creating cursor object to create SQL statement
    the_connection = sql.connect('TaskList.db')    
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
   
    tasks = []  
      
    # defining frames using the tk.Frame() widget
    header_frame = tk.Frame(guiWindow, bg="#6495ED")  
    functions_frame = tk.Frame(guiWindow, bg="#6495ED")  
    listbox_frame = tk.Frame(guiWindow, bg="#6495ED")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List Application",  
        font = ("Brush Script MT", "30"),  
        background = "#008CBA",  
        foreground = "#FFFFFF"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#008CBA",  
        foreground = "#FFFFFF"  
    )  
    # using the place() method to place the label in the application  
    task_label.place(x = 30, y = 40)  
      
    # defining an entry field using the ttk.Entry() widget  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    # using the place() method to place the entry field in the application  
    task_field.place(x = 30, y = 80)  
  
    # adding buttons to the application using the ttk.Button() widget  
    create_button = ttk.Button(  
        functions_frame,  
        text = "Create Task",  
        width = 24,  
        command = create_task,
        style="TButton"
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task, 
        style="TButton" 
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks,
        style="TButton"  
    )  
    close_button = ttk.Button(  
        functions_frame,  
        text = "Close",  
        width = 24,  
        command = close,
        style="TButton"  
    )  

    # Customize the style of the buttons
    guiWindow.style = ttk.Style()
    guiWindow.style.configure("TButton",
                            background="#008CBA",  
                            foreground="#FFFFFF", 
                            font=("Helvetica", 12, "bold"))  

    # using the place() method to set the position of the buttons in the application  
    create_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    close_button.place(x = 30, y = 240)  

    # defining a list box using the tk.Listbox() widget  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    # using the place() method to place the list box in the application  
    task_listbox.place(x = 10, y = 20)  
  
    # calling some functions  
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close()  