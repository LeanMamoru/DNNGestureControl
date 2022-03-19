import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(f"screenWidth: {screenWidth}, screenHeight: {screenHeight}")

currentMouseX, currentMouseY = pyautogui.position()
print(f"currentMouseX: {currentMouseX}, currentMouseY: {currentMouseY}")


