import tkinter as tk
from tkinter import Menu

import todo_list as todo
def main_window(todo_list):
    root = tk.Tk()
    root.title("TODO")
    root.geometry("300x700")
    root.configure(bg='lightblue')
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Save CSV", command=lambda: todo_list.save_to_csv())
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    banner = tk.Label(root, text="TO-DO List",
                      font=('Arial', 24, 'bold'),
                      fg='white',
                      bg='lightblue',
                      padx=20, pady=10,
                      relief='raised',
                      bd=4)
    banner.pack(pady=20, fill='x', anchor='n')

    task_list(root,todo_list)
    root.mainloop()

def spacer(root,size):
    for s in range(size):
        tk.Label(root,bg="lightblue").pack()

def task_list(root,todo_list):
    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)
    for task in todo_list.tasks:
        listbox.insert(tk.END, f'{task.desc} ({"completed" if task.completed else "not completed"})')
    desc_label= tk.Label(root,text="description:",bg="lightblue",font=8)
    desc_label.pack()
    input_text = tk.Text(root,width=30,height=1)
    input_text.pack()
    spacer(root,1)
    thumbs_up = "\U0001F44D"
    plus ="\u002B"
    minus="\u2212"
    pencil = "\U0000270F"
    a_button = tk.Button(root,width=20, padx=2, pady=2, font=('Arial', 12), bg='lightgreen', fg='white', text=f"({plus}) Add ", command=lambda: add_button(todo_list, listbox,input_text.get("1.0", tk.END).strip()))
    a_button.pack()
    d_button=tk.Button(root,width=20, padx=2, pady=2,font=('Arial', 12), bg='red', fg='white',text=f"({minus}) Delete ",command=lambda: del_button(todo_list,listbox))
    d_button.pack()
    f_button = tk.Button(root,width=20, padx=2, pady=2,font=('Arial', 12), bg='orange', fg='white', text=f"({thumbs_up}) Finish", command=lambda: finish_button(todo_list, listbox))
    f_button.pack()
    c_button =tk.Button(root,width=20, padx=2, pady=2,font=('Arial', 12), bg='blue', fg='white', text=f"({pencil}) Change", command=lambda: change_button(todo_list, listbox,input_text.get("1.0", tk.END).strip()))
    c_button.pack()
    spacer(root,2)

def del_button(todo_list,listbox):
    selected_index = listbox.curselection()
    if selected_index:
        todo_list.remove_task(selected_index[0])
        listbox.delete(selected_index)
    else:
        show_popup("please select a task to delete")

def finish_button(todo_list,listbox):
    selected_index = listbox.curselection()
    if selected_index:
        task=todo_list.tasks[selected_index[0]]
        if task.completed:
            todo_list.mark_as_uncomplete(selected_index[0])
            listbox.delete(selected_index)
            listbox.insert(selected_index, f'{task.desc} (not complete)')

        else:
            todo_list.mark_as_complete(selected_index[0])
            listbox.delete(selected_index)
            listbox.insert(selected_index,f'{task.desc} (complete)')
    else:
        show_popup("please select a task to complete")
def add_button(todo_list,listbox,text="debug"):
    if len(text)>0:
        todo_list.add_task(text)
        listbox.insert(tk.END,f'{text} (not complete)')
    else:
        show_popup("fill description input")
def change_button(todo_list,listbox,text="debug"):
    selected_index = listbox.curselection()
    if selected_index:
        if len(text) > 0:
            todo_list.change_desc(selected_index[0],text)
            listbox.delete(selected_index)
            listbox.insert(selected_index, f'{text} (not complete)')
        else:
            show_popup("fill description input")
    else:
        show_popup("please select a task to edit")


def show_popup(text="error"):
    popup = tk.Toplevel()
    popup.title("Error")

    popup.geometry("200x100")

    label = tk.Label(popup, text=text)
    label.pack(pady=10)

    close_button = tk.Button(popup, text="Ok", command=popup.destroy)
    close_button.pack(pady=5)