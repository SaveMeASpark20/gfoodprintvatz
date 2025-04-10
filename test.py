from pywinauto import Application
import time

# Connect to the application
app = Application(backend="uia").connect(title_re=".*FASTFOOD.*")
dlg = app.window(title_re=".*FASTFOOD.*")

# Ensure the window is in focus
dlg.set_focus()

# Click at the coordinates (418, 388)
dlg.click_input(coords=(418, 348))
dlg.click_input(coords=(418, 348))

print("Clicked at coordinates (318, 388)")
