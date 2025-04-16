from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickButton import clickDeliveryBtn
from function.input import inputText
from configuration.config import config

def clickBckMgrMenu(dlg, name, secondsToSleep=0) :
    mgrcred = config.manager_cred
    cashier_cred = config.cashier_cred
    if(name =='x'):
        clickDeliveryBtn(dlg, name)
    elif(name =='bacchusx') :
        inputText(dlg, cashier_cred.cashier_id, "Server")
        clickKeypad(dlg, 'check')
        clickBtn(dlg, 'MAIN MENU')
    else:
        clickBtn(dlg, name, secondsToSleep=secondsToSleep)
    inputText(dlg, mgrcred.manager_id, "Manager")
    # clickKeypad(dlg, 'check')
    inputText(dlg, mgrcred.manager_pass, "Password")
    clickKeypad(dlg, 'check')