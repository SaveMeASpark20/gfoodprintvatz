from function.input import inputText
from function.clickButton import clickKeypad
from configuration.config import config
from function.util import checkIfExist
from function.clickButton import clickBtn

def managerSignon(dlg):
    manager = config.manager_cred
    while(checkIfExist(dlg, 'OPOS', control_type='Window')):
        clickBtn(dlg, 'OK')
    inputText(dlg, manager.manager_id, 'Manager')
    inputText(dlg, manager.manager_pass, 'Password')
    clickKeypad(dlg, 'check')