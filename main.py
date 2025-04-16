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
from sequence.open_go import open_go
from sequence.managerSignon import managerSignon
from configuration.config import config

def main(backend="uia"):
    """Connects to the FAST FOOD/FINE DINING application and clicks a button."""
    main_dlg = open_go()
    managerSignon(main_dlg)

    restaurant_type = config.restaurant_type
    app = Application(backend=backend).connect(title_re=".*" + restaurant_type + ".*")
    dlg = app.window(title_re=".*" + restaurant_type + ".*")
    
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
    prev_action = None
    for step in config.run_main:
        if not hasattr(step, 'action'):
            print(f"Comment: {getattr(step, '_comment', 'No comment provided')}")
            continue

        action = step.action
        if action in actions:
            if action == "GENERATE_REPORT":
                generateReport(dlg, 'CASHIER\r\nREADING')
            elif action == "GO_BACK_TO_MGR":
                if prev_action == "DELIVERY":
                    backToMgr = "x"
                elif restaurant_type == "FINE DINING" and prev_action in ["TAKE OUT", "DINE IN"]:
                    backToMgr = "bacchusx"
                    print("restaurant_type :", restaurant_type)
                    print("prev_action :", prev_action )
                else:
                    backToMgr = "MGR MENU"
                clickBckMgrMenu(dlg, backToMgr)
            else:
                actions[action](dlg)
                prev_action = action
                print(prev_action)


                    
if __name__ == "__main__":
    main()
    

