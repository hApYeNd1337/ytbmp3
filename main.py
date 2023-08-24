import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import os
import re

def clean_filename(filename):
    # Eliminăm caracterele speciale din nume
    cleaned_filename = re.sub(r'[\\/*?:"<>|]', '', filename)
    return cleaned_filename

def download_mp3():
    try:
        url = link.get()
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        
        title = yt.title
        cleaned_title = clean_filename(title)
        
        # Descarcă cu extensia .mp4
        stream.download(filename=cleaned_title + ".mp4")
        
        # Redenumirea fișierului descărcat cu extensia MP3
        original_file = cleaned_title + ".mp4"
        new_file = cleaned_title + ".mp3"
        
        # Verificăm dacă fișierul există înainte de a-l redenumi
        if os.path.exists(original_file):
            os.rename(original_file, new_file)
        
        finish_label.configure(text="Descarcare completa", text_color="green")
    except Exception as e:
        print("Download failed:", str(e))
        finish_label.configure(text="Descarcare esuata", text_color="red")

# Configurarea ferestrei principale
app = ctk.CTk()
app.geometry("720x480")
app.title("hApYeNd mp3 downloader")

# Etichetă pentru introducerea link-ului
title_label = ctk.CTkLabel(app, text="Baga link-ul:(CTRL +V) ")
title_label.pack(padx=10, pady=10)

# Câmp pentru introducerea link-ului
url = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Buton pentru descărcare
download_button = ctk.CTkButton(app, text="Descarca", command=download_mp3)
download_button.pack(padx=10, pady=10)

# Etichetă pentru afișarea stării descărcării
finish_label = ctk.CTkLabel(app, text="")
finish_label.pack()

app.mainloop()
