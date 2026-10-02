cat << 'EOF' > tkinter_text_editor.pyw
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog, messagebox

current_filename = ""

def New():
    global current_filename
    editArea.delete('1.0', tk.END)
    current_filename = ""

def Open():
    global current_filename
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        editArea.delete('1.0', tk.END)
        with open(file, 'r', encoding='utf-8') as f:
            editArea.insert(tk.INSERT, f.read())
        current_filename = file

def Save_As():
    global current_filename
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(editArea.get('1.0', tk.END))
        current_filename = file

def Save():
    global current_filename
    if current_filename == "":
        Save_As()
    else:
        with open(current_filename, 'w', encoding='utf-8') as f:
            f.write(editArea.get('1.0', 'end-1c'))

win = tk.Tk()
win.title("Tkinter Text Editor")

menu1 = tk.Menu(win)
win.config(menu=menu1)

filemenu = tk.Menu(menu1, tearoff=0)
menu1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=New)
filemenu.add_command(label="Open", command=Open)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Save As", command=Save_As)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)

frame1 = tk.Frame(win)
frame1.pack(fill=tk.BOTH, expand=True)

# 这里已经彻底修复了大小写和命名空间问题
editArea = scrolledtext.ScrolledText(
    master=frame1,
    wrap=tk.WORD,
    undo=True
)
editArea.pack(fill=tk.BOTH, expand=True)

win.mainloop()
EOF
