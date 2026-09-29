import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import ImageTk


def create_qr():
    link = entry.get()

    if link == "":
        messagebox.showwarning("Помилка", "Введіть посилання!")
        return

    qr = qrcode.make(link)
    qr.save("qr_code.png")

    image = ImageTk.PhotoImage(qr)
    qr_label.config(image=image)
    qr_label.image = image

    save_button.config(state="normal")

    messagebox.showinfo("Готово", "QR-код успішно створено!")


def save_qr():
    link = entry.get()

    qr = qrcode.make(link)

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if file_path:
        qr.save(file_path)
        messagebox.showinfo("Готово", "QR-код збережено!")


window = tk.Tk()
window.title("Link to QR")
window.geometry("500x600")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Link to QR",
    font=("Arial", 28, "bold")
)
title.pack(pady=25)

subtitle = tk.Label(
    window,
    text="Створіть QR-код з будь-якого посилання",
    font=("Arial", 12)
)
subtitle.pack(pady=5)

entry = tk.Entry(
    window,
    width=45,
    font=("Arial", 13)
)
entry.pack(pady=20)

create_button = tk.Button(
    window,
    text="Створити QR",
    font=("Arial", 12, "bold"),
    command=create_qr
)
create_button.pack(pady=10)

qr_label = tk.Label(window)
qr_label.pack(pady=20)

save_button = tk.Button(
    window,
    text="Зберегти QR-код",
    font=("Arial", 12),
    command=save_qr,
    state="disabled"
)
save_button.pack(pady=10)

window.mainloop()