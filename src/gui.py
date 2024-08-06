import tkinter as tk
import todo_list as todo
def main_window(todo_list):
    root = tk.Tk()
    root.title("TODO")
    root.geometry("300x700")
    root.configure(bg='lightblue')
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

def task_list(root,todo_list):
    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)
    for task in todo_list.tasks:
        listbox.insert(tk.END, f'{task.desc} ({"completed" if task.completed else "not completed"})')
    input_text = tk.Text(root,width=30,height=1)
    input_text.pack()
    thumbs_up = "\U0001F44D"
    plus ="\u002B"
    minus="\u2212"
    a_button = tk.Button(root,width=20, padx=2, pady=2, font=('Arial', 12), bg='lightgreen', fg='white', text=f"({plus}) Add ", command=lambda: add_button(todo_list, listbox,input_text.get("1.0", tk.END).strip()))
    a_button.pack()
    d_button=tk.Button(root,width=20, padx=2, pady=2,font=('Arial', 12), bg='red', fg='white',text=f"({minus}) Delete ",command=lambda: del_button(todo_list,listbox))
    d_button.pack()
    c_button = tk.Button(root,width=20, padx=2, pady=2,font=('Arial', 12), bg='orange', fg='white', text=f"({thumbs_up}) Complete", command=lambda: complete_button(todo_list, listbox))
    c_button.pack()

def del_button(todo_list,listbox):
    selected_index = listbox.curselection()
    if selected_index:
        todo_list.remove_task(selected_index[0])
        listbox.delete(selected_index)

def complete_button(todo_list,listbox):
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

def add_button(todo_list,listbox,text="debug"):
    if len(text)>0:
        task=todo_list.add_task(text)
        index=listbox.size()
        listbox.insert(tk.END,f'{text} (not complete)')
