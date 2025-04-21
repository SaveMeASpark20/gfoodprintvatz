from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from sequence.cashierSignon import cashierSignon
from sequence.trasanctions import dineIn
from sequence.trasanctions import takeOut
from sequence.trasanctions import delivery
from sequence.trasanctions import bulk
from sequence.trasanctions import misc
from sequence.trasanctions import free
from sequence.backMgrMenu import clickBckMgrMenu
from sequence.generateReport import generateReport
from sequence.openGo import openGo
from sequence.managerSignon import managerSignon
from function.util import checkIfExistWithTitleRe
from configuration.config import config

def main(backend="uia"):
    """Connects to the FAST FOOD/FINE DINING application and clicks a button."""
    app=None
    dlg=None
    try:
        app = Application(backend=backend).connect(title_re=".*" +  "W I N V Q P" + ".*")
        dlg = app.window(title_re=".*" + "W I N V Q P" + ".*")
    except ElementNotFoundError:
        dlg = openGo()
        managerSignon(dlg)

    restaurant_type = config.restaurant_type
    
    # Mapping action strings to corresponding functions
    actions = {
        "CASHIER_SIGNON": cashierSignon,
        "DINE IN": dineIn,
        "TAKE OUT": takeOut,
        "DELIVERY": delivery,
        "FREE": free,
        "GENERATE_REPORT": generateReport,
        "GO_BACK_TO_MGR": clickBckMgrMenu,
        "BULK": bulk,
        "MISC": misc
    }
    print("restaurant_type :", restaurant_type)
    def whatIsTransaction():
        for transaction in ["DINE IN", "TAKE OUT", "DELIVERY", "MISC", "FREE", "BULK ORDER"]:
            if(checkIfExistWithTitleRe(dlg, transaction, 'HeaderItem')):
                return transaction
        return None
    for step in config.run_main:
        if not hasattr(step, 'action'):
            print(f"Comment: {getattr(step, '_comment', 'No comment provided')}")
            continue

        action = step.action
        if action in actions:
            if action == "GENERATE_REPORT":
                generateReport(dlg, 'CASHIER\r\nREADING')
            elif action == "GO_BACK_TO_MGR":
                currentTransaction = whatIsTransaction()
                if(currentTransaction == None):
                    print("Can't find Transaction")
                    continue
                if currentTransaction == "DELIVERY":
                    backToMgr = "x"
                elif restaurant_type == "FINE DINING" and currentTransaction in ["TAKE OUT", "DINE IN"]:
                    backToMgr = "bacchusx"
                    print("restaurant_type :", restaurant_type)
                    print("Current_Transaction :", currentTransaction )
                else:
                    backToMgr = "MGR MENU"
                clickBckMgrMenu(dlg, backToMgr)
            else:
                actions[action](dlg)
                


                    
if __name__ == "__main__":
    main()
    

