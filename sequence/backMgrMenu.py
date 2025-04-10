from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickButton import clickDeliveryBtn
from function.input import inputText
from configuration.config import config

def clickBckMgrMenu(dlg, name, secondsToSleep=0) :
    mgrcred = config.manager_cred
    
    if(name =='x'):
        clickDeliveryBtn(dlg, name)
    else:
        clickBtn(dlg, name, secondsToSleep=secondsToSleep)
    inputText(dlg, mgrcred.manager_id)
    clickKeypad(dlg, 'check')
    inputText(dlg, mgrcred.manager_pass)
    clickKeypad(dlg, 'check')