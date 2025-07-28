import threading
import os
import customtkinter
from gtts import gTTS
from tkinter import messagebox
from tkinter import ttk
import pygame

def reproducir_sonido(archivo_audio, progreso_callback):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        progreso_callback()
        ventana.update()
    pygame.mixer.quit()

def crear_audio(text, archivo_audio):
    idioma = 'es'  # español
    tts = gTTS(text=text, lang=idioma, slow=False, tld='com.mx')  # com.mx da acento mexicano
    tts.save(archivo_audio)

def actualizar_progreso():
    progreso_barra.step(1)
    if progreso_barra['value'] >= 100:
        progreso_barra['value'] = 0

def generar_audio_y_reproducir():
    texto = entrada_textbox.get("1.0", "end-1c")
    nombre_archivo = titulo_entrada.get().strip()

    if not texto or not nombre_archivo:
        messagebox.showwarning("Advertencia", "Por favor ingresa texto y nombre del archivo.")
        return

    archivo_audio = f"{nombre_archivo}.mp3"
    
    crear_audio(texto, archivo_audio)

    respuesta = messagebox.askyesno("Reproducir audio", "¿Deseas reproducir el audio generado?")
    if respuesta:
        progreso_barra['value'] = 0
        reproducir_sonido(archivo_audio, actualizar_progreso)

def iniciar_hilo():
    hilo = threading.Thread(target=generar_audio_y_reproducir)
    hilo.start()

# === INTERFAZ ===
ventana = customtkinter.CTk()
ventana.title("Crear Audio")
ventana.geometry("500x450")
ventana.resizable(False, False)

label = customtkinter.CTkLabel(ventana, text="Texto a convertir a audio")
entrada_textbox = customtkinter.CTkTextbox(ventana, height=150, width=400)

titulo_audio = customtkinter.CTkLabel(ventana, text="Nombre del archivo de audio")
titulo_entrada = customtkinter.CTkEntry(ventana)

boton = customtkinter.CTkButton(ventana, text="Crear Audio", command=iniciar_hilo)

progreso_barra = ttk.Progressbar(ventana, orient="horizontal", length=400, mode="determinate", maximum=100)

# === PACKING ===
label.pack(padx=10, pady=10)
entrada_textbox.pack(padx=10, pady=10)
titulo_audio.pack(padx=10, pady=10)
titulo_entrada.pack(padx=10, pady=10)
boton.pack(padx=10, pady=10)
progreso_barra.pack(padx=10, pady=10)

ventana.mainloop()
