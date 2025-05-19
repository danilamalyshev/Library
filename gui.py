from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from manage_customers import user_login

def gui_login():
    result = user_login()

    if result['status'] == 'exit':
        messagebox.showinfo("Wyjście", "Zamykam logowanie.")
    elif result['status'] == 'wrong_password':
        messagebox.showerror("Błąd", "Nieprawidłowe hasło.")
    elif result['status'] == 'success':
        if result['admin']:
            answer = messagebox.askyesno("Administrator", f"Czy zalogować się jako administrator {result['username']}?")
            if answer:
                messagebox.showinfo("Witaj", f"Witaj administratorze {result['username']}!\nMożesz zarządzać użytkownikami i książkami.")
            else:
                messagebox.showinfo("Witaj", f"Witaj {result['username']}!")
        else:
            messagebox.showinfo("Witaj", f"Witaj {result['username']}!")
    else:
        messagebox.showerror("Błąd", "Nieprawidłowa nazwa użytkownika.")

def register():
    print("Register button clicked!")

def close_app():
    window.destroy()

# GUI

window = Tk()
window.title("E-Book")
window.resizable(False, False)

window_width = 550
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

icon = PhotoImage(file="ikona_ebook.png")
window.iconphoto(True, icon)

image = Image.open("logo.png")
scaled_image = image.resize((200, 200), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(scaled_image)

logo_label = Label(window, image=logo)
logo_label.image = logo
img_x = (window_width // 2) - 100
img_y = 50
logo_label.place(x=img_x, y=img_y)

button_frame = Frame(window)
button_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

login_button = Button(button_frame, text="Zaloguj się", command=gui_login)
login_button.pack(pady=10)

register_button = Button(button_frame, text="Zarejestruj się", command=register)
register_button.pack(pady=10)

close_button = Button(button_frame, text="Zamknij", command=close_app)
close_button.pack(pady=10)

window.mainloop()