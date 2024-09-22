import pygame

# Inicializar Pygame
pygame.mixer.init()

def reproducir_sonido(archivo_audio):
    # Cargar el archivo de audio
    pygame.mixer.music.load(archivo_audio)

    # Reproducir el audio
    pygame.mixer.music.play()

    # Mantener el programa en ejecución mientras se reproduce el audio
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
