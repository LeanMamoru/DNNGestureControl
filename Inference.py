import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(f"screenWidth: {screenWidth}, screenHeight: {screenHeight}")

currentMouseX, currentMouseY = pyautogui.position()
print(f"currentMouseX: {currentMouseX}, currentMouseY: {currentMouseY}")

pyautogui.moveTo(100, 150)  # https://pyautogui.readthedocs.io/en/latest/
