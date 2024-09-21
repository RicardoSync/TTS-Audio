from gtts import gTTS
import os
import customtkinter

def crear_audio(text, archivo_audio):
    texto = text

    idioma = 'es'
    
    tts = gTTS(text=texto, lang=idioma, slow=False, tld='com.mx')
    
    tts.save(archivo_audio)

def datos():
    text = entrada_textbox.get("1.0", "end-1c")  
    archivo = titulo_entrada.get()  
    archivo_audio = archivo + ".mp3"
    crear_audio(text, archivo_audio)  



ventana = customtkinter.CTk()
ventana.title("Crear Audio")  
ventana.geometry("500x400")  
ventana.resizable(False, False) 


idioma = ["Ingles","French","Mandarin","Portugues","Espanol"]


label = customtkinter.CTkLabel(ventana, text="Texto a convertir a audio")
entrada_textbox = customtkinter.CTkTextbox(ventana, height=150, width=400)  # Cuadro de texto grande

titulo_audio = customtkinter.CTkLabel(ventana, text="Nombre del archivo de audio")
titulo_entrada = customtkinter.CTkEntry(ventana)  # Cuadro de texto para el nombre del archivo

boton = customtkinter.CTkButton(ventana, text="Crear Audio", command=datos)

label.pack(padx=10, pady=10)
entrada_textbox.pack(padx=10, pady=10)
titulo_audio.pack(padx=10, pady=10)
titulo_entrada.pack(padx=10, pady=10)
boton.pack(padx=10, pady=10)
ventana.mainloop()