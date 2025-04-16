import subprocess
import os
import time
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError

def open_go():
    bat_path = r"E:\g93v\winvqp93\go.bat"
    work_dir = os.path.dirname(bat_path)

    # Start the batch file in a new terminal window
    subprocess.Popen(['cmd.exe', '/c', 'start', '', bat_path], cwd=work_dir, shell=True)

    # Wait for the app's window to appear
    print("Waiting for main app window...")

    app = Application(backend="uia")
    for _ in range(30):  # wait up to 30 seconds
        try:
            app.connect(title_re=".*W I N V Q P.*") 
            main_dlg = app.window(title_re=".*W I N V Q P.*")  # adjust to match your app title
            print("Connected to the app!")
            return main_dlg
        except ElementNotFoundError:
            time.sleep(1)

    print("App window not found.")
    return None
