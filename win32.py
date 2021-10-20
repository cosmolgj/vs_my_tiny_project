from win32 import win32gui
#import win32gui

# from win32.win32gui import FindWindow, GetWindowRect, MoveWindow, GetWindowText, EnumWindows

def window_enumeration_handler(hwnd, top_windows):
#    top_windows.append((hwnd, GetWindowText(hwnd)))
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

top_windows = []
#EnumWindows(window_enumeration_handler, top_windows)
win32gui.EnumWindows(window_enumeration_handler, top_windows)

for hwnd, title in top_windows:
    print(hwnd, title)