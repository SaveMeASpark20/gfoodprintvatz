
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from function.util import checkIfExist
from configuration.config import config

def cashierSignon(dlg) :
    cashier_config = config.cashier_signon
    clickBtn(dlg, cashier_config.btn_name)
    inputText(dlg, cashier_config.cashier_id)
    clickKeypad(dlg, 'check')
    inputText(dlg, cashier_config.cashier_pass)
    clickKeypad(dlg, 'check')
    if(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')