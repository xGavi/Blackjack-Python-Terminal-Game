import functions as f
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 650, 350, 570, 360, False)

f.game()
input('Thanks for playing!')