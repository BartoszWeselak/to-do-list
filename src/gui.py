import tkinter as tk
import todo_list as todo
def main_window(todo_list):
    root = tk.Tk()
    root.title("TODO")
    root.geometry("300x700")
    root.configure(bg='lightblue')

    task_list(root,todo_list)
    root.mainloop()


def task_list(root,todo_list):


    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    for task in todo_list.tasks:
        listbox.insert(tk.END, f'{task.desc} ({"completed" if task.completed else "not completed"})')

    input_text = tk.Text(root,width=30,height=1)
    input_text.pack()
    a_button = tk.Button(root,width=20, padx=0, pady=5, font=('Arial', 10), bg='lightgreen', fg='white', text="add", command=lambda: add_button(todo_list, listbox,input_text.get("1.0", tk.END).strip()))
    a_button.pack()
    d_button=tk.Button(root,width=20, padx=0, pady=5,font=('Arial', 10), bg='red', fg='white',text="delete",command=lambda: del_button(todo_list,listbox))
    d_button.pack()
    c_button = tk.Button(root,width=20, padx=0, pady=5,font=('Arial', 10), bg='orange', fg='white', text="complete", command=lambda: complete_button(todo_list, listbox))
    c_button.pack()



def del_button(todo_list,listbox):
    selected_index = listbox.curselection()
    print(selected_index[0])
    if selected_index:
        todo_list.remove_task(selected_index[0])
        listbox.delete(selected_index)


def complete_button(todo_list,listbox):
    selected_index = listbox.curselection()
    if selected_index:
        task=todo_list.tasks[selected_index[0]]
        if task.completed:
            print("debug")
            todo_list.mark_as_uncomplete(selected_index[0])
            listbox.delete(selected_index)
            listbox.insert(selected_index, f'{task.desc} (not complete)')

        else:
            todo_list.mark_as_complete(selected_index[0])
            listbox.delete(selected_index)
            listbox.insert(selected_index,f'{task.desc} (complete)')



def add_button(todo_list,listbox,text="debug"):
    task=todo_list.add_task(text)
    index=listbox.size()
    listbox.insert(tk.END,f'{text} (not complete)')
