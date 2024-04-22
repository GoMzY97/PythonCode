import tkinter as tk

def save_file():
    open_file = open("text_editor_file.txt","w")
    open_file.write(text_area.get(1.0, tk.END))
    open_file.close()

root = tk.Tk()
text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)

root.mainloop()
