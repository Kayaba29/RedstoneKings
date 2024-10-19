import pygame

# Initialisiere pygame
pygame.init()
pygame.joystick.init()

# Überprüfe, ob Joysticks verfügbar sind
if pygame.joystick.get_count() == 0:
    print("Kein Joystick gefunden. Bitte schließe einen Joystick an.")
    exit(1)

# Wähle den ersten verfügbaren Joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick-Name: {joystick.get_name()}")
print(f"Anzahl Achsen: {joystick.get_numaxes()}")
print(f"Anzahl Tasten: {joystick.get_numbuttons()}")
print(f"Anzahl Hats: {joystick.get_numhats()}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Achse {event.axis} bewegt auf {event.value}")
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Taste {event.button} gedrückt")
        elif event.type == pygame.JOYBUTTONUP:
            print(f"Taste {event.button} losgelassen")

pygame.quit()
