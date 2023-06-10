import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 600

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Ejemplo de juego con Pygame")

# Funciones personalizadas
def dibujar_nave(x, y):
    pygame.draw.rect(pantalla, blanco, (x, y, 50, 50))

def dibujar_enemigo(x, y):
    pygame.draw.rect(pantalla, (255, 0, 0), (x, y, 30, 30))

def mostrar_puntuacion(puntuacion):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render("Puntuación: " + str(puntuacion), True, blanco)
    pantalla.blit(texto, (10, 10))

def mostrar_menu():
    fuente_grande = pygame.font.Font(None, 72)
    fuente_pequena = pygame.font.Font(None, 36)
    texto_titulo = fuente_grande.render("Juego de Disparos", True, blanco)
    texto_instrucciones = fuente_pequena.render("Presiona ESPACIO para jugar", True, blanco)
    pantalla.blit(texto_titulo, (ancho_pantalla // 2 - texto_titulo.get_width() // 2, alto_pantalla // 2 - texto_titulo.get_height() // 2))
    pantalla.blit(texto_instrucciones, (ancho_pantalla // 2 - texto_instrucciones.get_width() // 2, alto_pantalla // 2 + texto_titulo.get_height() // 2))

# Función principal del juego
def juego():
    # Variables del juego
    jugando = True
    puntuacion = 0
    nave_x = ancho_pantalla // 2 - 25
    nave_y = alto_pantalla - 50
    enemigos = []
    for _ in range(10):
        enemigo_x = random.randint(0, ancho_pantalla - 30)
        enemigo_y = random.randint(-500, -50)
        enemigos.append([enemigo_x, enemigo_y])

    # Bucle principal del juego
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        # Actualizar la posición de la nave
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            nave_x -= 5
        if teclas[pygame.K_RIGHT]:
            nave_x += 5

        # Actualizar la posición de los enemigos
        for enemigo in enemigos:
            enemigo[1] += 2
            if enemigo[1] > alto_pantalla:
                enemigo[0] = random.randint
                

