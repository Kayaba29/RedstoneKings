import pygame
import pyvjoy

# Checkliste im Terminal ausgeben
print("Checkliste für die Konfiguration:")
print("1. Überprüfe vJoy-Installation...")

# Überprüfen, ob vJoy installiert und aktiviert ist
try:
    joy = pyvjoy.VJoyDevice(1)
    print("   vJoy ist installiert und aktiviert.")
except pyvjoy.exceptions.vJoyNotEnabledException:
    print("   vJoy ist nicht aktiviert oder nicht richtig installiert. Bitte überprüfe die vJoy-Installation.")
    exit(1)

print("2. Initialisiere pygame...")

# Initialisiere pygame
pygame.init()
pygame.joystick.init()
print("   pygame ist initialisiert.")

print("3. Überprüfe Joystick-Verfügbarkeit...")

# Prüfe, ob Joysticks verfügbar sind
if pygame.joystick.get_count() == 0:
    print("   Kein Joystick gefunden. Bitte schließe einen Joystick an.")
    exit(1)

print("   Joystick gefunden.")

# Wähle den ersten verfügbaren Joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"   Joystick '{joystick.get_name()}' ist initialisiert und bereit.")

# Konfiguration für HOTAS X56
HOTAS_X56_AXIS_MIN = -1
HOTAS_X56_AXIS_MAX = 1
XBOX_AXIS_MIN = 0
XBOX_AXIS_MAX = 32767

def scale_value(value, src_min, src_max, dst_min, dst_max):
    # Skaliert einen Wert von einem Bereich in einen anderen
    src_range = src_max - src_min
    dst_range = dst_max - dst_min
    scaled_value = ((value - src_min) * dst_range) / src_range + dst_min
    return int(scaled_value)

print("4. Starte Ereignisverarbeitung...\n")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value
            xbox_value = None

            # Konvertiere die Achsen des Joysticks in Xbox-Controller-Achsen
            if axis == 0:  # X-Achse
                xbox_value = scale_value(value, HOTAS_X56_AXIS_MIN, HOTAS_X56_AXIS_MAX, XBOX_AXIS_MIN, XBOX_AXIS_MAX)
                joy.set_axis(pyvjoy.HID_USAGE_X, xbox_value)
            elif axis == 1:  # Y-Achse
                xbox_value = scale_value(value, HOTAS_X56_AXIS_MIN, HOTAS_X56_AXIS_MAX, XBOX_AXIS_MIN, XBOX_AXIS_MAX)
                joy.set_axis(pyvjoy.HID_USAGE_Y, xbox_value)
            elif axis == 3:  # Z-Achse (Drehachse)
                xbox_value = scale_value(value, HOTAS_X56_AXIS_MIN, HOTAS_X56_AXIS_MAX, XBOX_AXIS_MIN, XBOX_AXIS_MAX)
                joy.set_axis(pyvjoy.HID_USAGE_RX, xbox_value)
            elif axis == 4:  # RZ-Achse (Schubhebel oder andere Achse)
                xbox_value = scale_value(value, HOTAS_X56_AXIS_MIN, HOTAS_X56_AXIS_MAX, XBOX_AXIS_MIN, XBOX_AXIS_MAX)
                joy.set_axis(pyvjoy.HID_USAGE_RY, xbox_value)

            # Ausgabe der Achsenbewegung im Terminal
            if xbox_value is not None:
                print(f"Achse {axis} bewegt auf {value}, konvertiert zu Xbox-Wert {xbox_value}")

        elif event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            xbox_button = None

            # Beispiel für die Tastenbelegung
            if button == 0:  # Beispiel-Taste 1 auf HOTAS
                joy.set_button(1, 1)  # Entsprechende Taste auf dem Xbox-Controller drücken
                xbox_button = 1
            elif button == 1:
                joy.set_button(2, 1)
                xbox_button = 2
            elif button == 2:
                joy.set_button(3, 1)
                xbox_button = 3
            elif button == 3:
                joy.set_button(4, 1)
                xbox_button = 4

            # Ausgabe der Tastendrucks im Terminal
            if xbox_button is not None:
                print(f"Taste {button} gedrückt, zugeordnet zu Xbox-Taste {xbox_button}")

        elif event.type == pygame.JOYBUTTONUP:
            button = event.button
            xbox_button = None

            if button == 0:
                joy.set_button(1, 0)
                xbox_button = 1
            elif button == 1:
                joy.set_button(2, 0)
                xbox_button = 2
            elif button == 2:
                joy.set_button(3, 0)
                xbox_button = 3
            elif button == 3:
                joy.set_button(4, 0)
                xbox_button = 4

            # Ausgabe der Tastenfreigabe im Terminal
            if xbox_button is not None:
                print(f"Taste {button} losgelassen, zugeordnet zu Xbox-Taste {xbox_button}")

pygame.quit()
