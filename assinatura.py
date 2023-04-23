import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import os
import webcolors

def create_signature(cargo, color_name, name, email, phone):
    # Define o fonte e tamanho para cada campo
    name_font = ImageFont.truetype("arial.ttf", 40)
    cargo_font = ImageFont.truetype("arial.ttf", 25)
    email_font = ImageFont.truetype("arial.ttf", 30)
    phone_font = ImageFont.truetype("arial.ttf", 35)
    # Converte o nome da cor para uma tupla de valores RGB
    color = webcolors.hex_to_rgb(color_name)
    # Cria uma imagem em branco com a cor dada
    signature = Image.new("RGB", (1000, 270), color)
    # Cria um contexto de desenho
    draw = ImageDraw.Draw(signature)
    # Desenha o texto na imagem
    draw.text((10, 10), name, font=name_font)
    draw.text((10, 60), cargo, font=cargo_font)
    draw.text((10, 110), email, font=email_font)
    draw.text((10, 160), phone, font=phone_font)
    return signature

def create_signature_and_save():
    cargo = cargo_entry.get()
    color_name = color_var.get()
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Verifica se algum campo está vazio
    if not cargo or not name or not email or not phone:
        messagebox.showerror("Erro", "Faltou informação em um dos campos!")
        return

    signature = create_signature(cargo, color_name, name, email, phone)
    signature_path = os.path.expanduser('~/Downloads/assinatura.png')
    signature.save(signature_path)
    root.destroy()

# Corpo 
root = tk.Tk()
root.title("Gerador de assinaturas")
root.geometry("400x500")
root.config(background='#212121')
# Cor OP
color_options = {
    'Azul': '#1E88E5',
    'Verde': '#43A047',
    'Roxo': '#8E24AA'
}

color_var = tk.StringVar(value='#1E88E5')
# Nome
name_label = tk.Label(root, text="Nome completo:", font=("Helvetica", 11), foreground='white', background='#212121')
name_label.pack(pady=10)

name_entry = tk.Entry(root, width=40, background='#424242', foreground='white', borderwidth=0)
name_entry.pack()

# Cargo 
cargo_label = tk.Label(root, text="Cargo:", font=("Helvetica", 11), foreground='white', background='#212121')
cargo_label.pack(pady=10)

cargo_entry = tk.Entry(root, width=40, background='#424242', foreground='white', borderwidth=0)
cargo_entry.pack()

# Email
email_label = tk.Label(root, text="Seu endereço de email:", font=("Helvetica", 11), foreground='white', background='#212121')
email_label.pack(pady=10)

email_entry = tk.Entry(root, width=40, background='#424242', foreground='white', borderwidth=0)
email_entry.pack()

# Tell
phone_label = tk.Label(root, text="Seu numero de contato:", font=("Helvetica", 11), foreground='white', background='#212121')
phone_label.pack(pady=10)

phone_entry = tk.Entry(root, width=40, background='#424242', foreground='white', borderwidth=0)
phone_entry.pack()

# Cor
color_label = tk.Label(root, text="Qual cor de cartão:", font=("Helvetica", 11), foreground='white', background='#212121')
color_label.pack(pady=20)

frame = tk.Frame(root, background='#212121')
frame.pack(pady=10)
for color_text, color in color_options.items():
    btn = tk.Radiobutton(frame, text=color_text, variable=color_var, value=color, font=("Helvetica", 11), background='#212121', foreground='white', highlightthickness=0, indicatoron=0, selectcolor='black', activebackground=color, activeforeground='white')
    btn.pack(side='left', padx=10)

create_button = tk.Button(root, text="Gerar assinatura", command=create_signature_and_save, font=("Helvetica", 11), background=color_var.get(), foreground='white', padx=10, pady=5, borderwidth=0)
create_button.pack(pady=20)

root.mainloop()


