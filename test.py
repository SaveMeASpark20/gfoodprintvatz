from pywinauto import Application
import time
from configuration.config import config

from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from function.input import inputTextByIndex
from function.util import checkIfExist
from function.util import checkIfExistWithRegex
from sequence.trasanctions import delivery
from configuration.config import config
from sequence.openGo import openGo
"""Connects to the FASTFOOD application and clicks a button."""
restaurant_type = config.restaurant_type
listToRun = config.run_main
app = Application(backend='uia').connect(title_re=".*" + restaurant_type + ".*")
dlg = app.window(title_re=".*" + restaurant_type + ".*")
dlg.print_control_identifiers()

# app = open_go()
# main_dlg = app.window(title_re=".*W I N V Q P.*")
# main_dlg.print_control_identifiers()

# while(checkIfExist(main_dlg, 'OPOS', control_type='Window')):
#     clickBtn(main_dlg, 'OK')

# inputText(main_dlg, '11', 'Manager')
# inputText(main_dlg, 'qwerqwer1', 'Password')
# clickKeypad(main_dlg, 'check')