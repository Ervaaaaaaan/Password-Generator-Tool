import tkinter as tk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk  

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return
    if not (use_upper or use_lower or use_numbers or use_symbols):
        messagebox.showerror("Error", "Select at least one character type")
        return

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = "".join(random.choice(chars) for _ in range(length))
    password_entry.config(state='normal')
    password_entry.delete("1.0", tk.END)
    password_entry.insert(tk.END, password)
    password_entry.config(state='disabled')

def copy_password():
    password = password_entry.get("1.0", tk.END).strip()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

root = tk.Tk()
root.title("Password Generator - Ervan 'Atlas Dev'")
root.geometry("520x590")
root.config(bg="#2c3e50")
root.resizable(False, False)

font_title = ("Segoe UI", 20, "bold")
font_label = ("Segoe UI", 11)
font_entry = ("Consolas", 20)
btn_color = "#2980b9"
btn_hover_color = "#3498db"
fg_color = "#ecf0f1"
bg_color = "#2c3e50"

length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


img = Image.open("groupe_lfa7ixa-removebg-preview.png")
img = img.resize((100, 100))  
logo_img = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_img, bg=bg_color)
logo_label.pack(pady=(15,5))

title_label = tk.Label(root, text="Password Generator", font=font_title, fg=fg_color, bg=bg_color)
title_label.pack(pady=(0,10))

length_frame = tk.Frame(root, bg=bg_color)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:", font=font_label, fg=fg_color, bg=bg_color)
length_label.pack(side="left", padx=(0,10))

length_scale = tk.Scale(length_frame, from_=4, to=32, orient=tk.HORIZONTAL, variable=length_var,
                        length=200, bg=bg_color, fg=fg_color, troughcolor="#34495e",
                        highlightthickness=0)
length_scale.pack(side="left")

checkbox_frame = tk.Frame(root, bg=bg_color)
checkbox_frame.pack(pady=10, padx=20, fill="x")

tk.Checkbutton(checkbox_frame, text="Include Uppercase (A-Z)", variable=upper_var, font=font_label,
               bg=bg_color, fg=fg_color, selectcolor="#2980b9", activebackground=bg_color).pack(anchor="w", pady=2)
tk.Checkbutton(checkbox_frame, text="Include Lowercase (a-z)", variable=lower_var, font=font_label,
               bg=bg_color, fg=fg_color, selectcolor="#2980b9", activebackground=bg_color).pack(anchor="w", pady=2)
tk.Checkbutton(checkbox_frame, text="Include Numbers (0-9)", variable=numbers_var, font=font_label,
               bg=bg_color, fg=fg_color, selectcolor="#2980b9", activebackground=bg_color).pack(anchor="w", pady=2)
tk.Checkbutton(checkbox_frame, text="Include Symbols (!@#$)", variable=symbols_var, font=font_label,
               bg=bg_color, fg=fg_color, selectcolor="#2980b9", activebackground=bg_color).pack(anchor="w", pady=2)

def on_enter(e):
    generate_btn['bg'] = btn_hover_color

def on_leave(e):
    generate_btn['bg'] = btn_color

generate_btn = tk.Button(root, text="Generate Password", font=font_label, bg=btn_color, fg=fg_color,
                         activebackground=btn_hover_color, activeforeground=fg_color, relief="flat",
                         command=generate_password, padx=10, pady=6, cursor="hand2")
generate_btn.pack(pady=15)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

password_entry = tk.Text(root, font=font_entry, width=50, height=2, wrap="word", bd=2, relief="sunken")
password_entry.pack(pady=(0,10))
password_entry.config(state='disabled')

def on_enter_copy(e):
    copy_btn['bg'] = btn_hover_color

def on_leave_copy(e):
    copy_btn['bg'] = btn_color

copy_btn = tk.Button(root, text="Copy to Clipboard", font=font_label, bg=btn_color, fg=fg_color,
                     activebackground=btn_hover_color, activeforeground=fg_color, relief="flat",
                     command=copy_password, padx=10, pady=6, cursor="hand2")
copy_btn.pack()
copy_btn.bind("<Enter>", on_enter_copy)
copy_btn.bind("<Leave>", on_leave_copy)

credit_label = tk.Label(root, text="Made by Ervan 'Atlas Dev'", font=("Segoe UI", 9),
                        fg="#95a5a6", bg=bg_color)
credit_label.pack(side="bottom", pady=8)

root.mainloop()
