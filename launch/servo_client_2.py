import pygame
import requests
import time

SERVER_URL = 'http://192.168.8.3:5000/move_servos'  # Use your Raspberry Pi IP

# Set initial positions
initial_position1 = 0  # Adjust if necessary
initial_position2 = 0  # Adjust if necessary

def move_servos(x, y):
    payload = {
        'servo1': x,
        'servo2': y
    }
    requests.post(SERVER_URL, json=payload)

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

try:
    while True:
        pygame.event.pump()  # Process event queue

        # Get right joystick axes values (usually axes 2 and 3)
        x = joystick.get_axis(3) * 100  # Right stick horizontal axis
        y = joystick.get_axis(4) * 100  # Right stick vertical axis

        # Invert directions if necessary
        x = -x
        y = y

        move_servos(x, y)
        time.sleep(0.1)  # Adjust as needed

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pygame.quit()
