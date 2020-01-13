import pyautogui
import random
import time
import math

import pyautogui

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()
print("Largeur du moniteur: ", screenWidth)
print("Hauteur du moniteur: ", screenWidth)

currentMouseX, currentMouseY = pyautogui.position()
print("Coordonnée X de la souris: ", currentMouseX)
print("Coordonnée Y de la souris: ", currentMouseY)
