
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from function.util import checkIfExist
from function.util import checkIfExistWithTitleRe
from configuration.config import config
import time
def cashierSignon(dlg) :
    cashier_config = config.cashier_signon
    clickBtn(dlg, cashier_config.btn_name)
    isNewDate=False
    time.sleep(10)
    while(checkIfExist(dlg, 'VQP', control_type='Window')):
        if(checkIfExistWithTitleRe(dlg, "Opened", 'Text')):
            clickBtn(dlg, 'OK')
        elif(checkIfExistWithTitleRe(dlg, "Cashier", 'Text')):
            clickBtn(dlg, 'OK')
            return
    inputText(dlg, cashier_config.cashier_id, "Cashier")
    # clickKeypad(dlg, 'check')
    inputText(dlg, cashier_config.cashier_pass, "Password")
    clickKeypad(dlg, 'check')
    if(isNewDate):
        time.sleep(5)
        inputText(dlg, '20000')
        clickKeypad(dlg, 'check')
    clickKeypad(dlg, 'check')
    if(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')