from tkinter import *
from tkinter import filedialog, messagebox
root = Tk()
root.title("My Notepad")
root.geometry("700x500")
text = Text(root, font=("Arial", 12), undo=True)
text.pack(fill=BOTH, expand=True)
def new_file():
    text.delete("1.0", END)
def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            text.delete("1.0", END)
            text.insert("1.0", f.read())
def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file:
        with open(file, "w") as f:
            f.write(text.get("1.0", END))
        messagebox.showinfo("Saved", "File saved successfully!")
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
root.mainloop()
