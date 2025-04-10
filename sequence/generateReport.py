from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from configuration.config import config

def generateReport(dlg, report_name) :
    mgrcred = config.manager_cred
    clickBtn(dlg, report_name)
    inputText(dlg, mgrcred.manager_id)
    clickKeypad(dlg, 'check')
    inputText(dlg, mgrcred.manager_pass)
    clickKeypad(dlg, 'check')
    clickBtn(dlg, 'PRINT')