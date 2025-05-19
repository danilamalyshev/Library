from tkinter import *
from PIL import Image, ImageTk
from decorators import style_button

@style_button
def create_button(*args, **kwargs):
    return Button(*args, **kwargs)

def login():
    print("Login button clicked!")


def register():
    print("Register button clicked!")


def close_app():
    window.destroy()


# Główne okno aplikacji
window = Tk()
window.title("E-Book")
window.resizable(False, False)

# Wymiary okna
window_width = 550
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Ikona okna
icon = PhotoImage(file="ikona_ebook.png")
window.iconphoto(True, icon)

# Logo
image = Image.open("logo.png")
scaled_image = image.resize((200, 200), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(scaled_image)

logo_label = Label(window, image=logo)
logo_label.image = logo

# Pozycjonujemy logo w wyznaczonym miejscu
img_x = (window_width // 2) - 100  # Wyśrodkowane poziomo, szerokość obrazka to 200 px
img_y = 50  # Odległość od góry
logo_label.place(x=img_x, y=img_y)

# Ramka na przyciski
button_frame = Frame(window)
button_frame.place(relx=0.5, rely=0.6, anchor=CENTER)  # Ramka wyśrodkowana w pionie i poziomie

# Przyciski korzystające z dekoratora
login_button = create_button(button_frame, text="Zaloguj się", command=login)
login_button.pack(pady=10)

register_button = create_button(button_frame, text="Zarejestruj się", command=register)
register_button.pack(pady=10)

close_button = create_button(button_frame, text="Zamknij", command=close_app)
close_button.pack(pady=10)

# Uruchomienie głównej pętli Tkinter
window.mainloop()
