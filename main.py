from pywinauto import Application
from sequence.cashierSignon import cashierSignon
from sequence.trasanctions import dineIn
from sequence.trasanctions import takeOut
from sequence.trasanctions import delivery
from sequence.trasanctions import bulk
from sequence.trasanctions import misc
from sequence.trasanctions import free
from sequence.backMgrMenu import clickBckMgrMenu
from sequence.generateReport import generateReport

def main(backend="uia"):
    """Connects to the FASTFOOD application and clicks a button."""
    app = Application(backend=backend).connect(title_re=".*FASTFOOD.*")
    dlg = app.window(title_re=".*FASTFOOD.*")
    cashierSignon(dlg)
    dineIn(dlg)
    clickBckMgrMenu(dlg, 'MGR MENU')
    generateReport(dlg, 'CASHIER\r\nREADING')
    takeOut(dlg)
    clickBckMgrMenu(dlg, 'MGR MENU')
    generateReport(dlg, 'CASHIER\r\nREADING')
    delivery(dlg)
    clickBckMgrMenu(dlg, 'x')
    generateReport(dlg, 'CASHIER\r\nREADING')
    misc(dlg)
    clickBckMgrMenu(dlg, 'MGR MENU')
    generateReport(dlg, 'CASHIER\r\nREADING')
    free(dlg)
    clickBckMgrMenu(dlg, 'MGR MENU')
    generateReport(dlg, 'CASHIER\r\nREADING')
    bulk(dlg)
    clickBckMgrMenu(dlg, 'MGR MENU')
    generateReport(dlg, 'CASHIER\r\nREADING')
    
if __name__ == "__main__":
    main()

