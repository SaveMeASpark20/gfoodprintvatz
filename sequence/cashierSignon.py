
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from function.util import checkIfExist
from configuration.config import config
import time
def cashierSignon(dlg) :
    cashier_config = config.cashier_signon
    clickBtn(dlg, cashier_config.btn_name)
    time.sleep(5)
    while(checkIfExist(dlg, 'VQP', control_type='Window')):
        clickBtn(dlg, 'OK')
    inputText(dlg, cashier_config.cashier_id, "Cashier")
    # clickKeypad(dlg, 'check')
    time.sleep(5)
    inputText(dlg, cashier_config.cashier_pass, "Password")
    if(checkIfExist(dlg, 'Enter Fund:')):
        inputText(dlg, '20000')
        clickKeypad(dlg, 'check')
    clickKeypad(dlg, 'check')
    if(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')