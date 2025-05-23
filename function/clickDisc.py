from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from configuration.config import config
from function.util import checkIfExistWithRegex

def clickDiscount(dlg, disc_name, customer_id, customer_name, address, tin, bus_style, promo_amount=20, restaurant_type='FASTFOOD'):
    restaurant_type = config.restaurant_type
    available_discounts = {
        "EMPLOYEE DISC": "EMPLOYEE\r\nDISC",
        "PROMO AMOUNT": "PROMO\r\nAMOUNT",
        "SENIOR DISC": "SENIOR\r\nDISC 20%",
        "SOLO PARENT" : "SOLO\r\nPARENT",
        "PWD DISC" : "PWD DISC\r\n20%",
        "NACD" : "NACD",
        "MEDAL OF VALOR" : "MEDAL OF\r\nVALOR",
    }
    
    # Find the best match in the available discounts
    for key, button_name in available_discounts.items():
        if key in disc_name.upper():  # Convert input to uppercase to allow case-insensitive matching
            clickBtn(dlg, button_name)
            if key == "PROMO AMOUNT":
                inputText(dlg, promo_amount, 'Disc Amount:')
                clickKeypad(dlg, "check")
                return
            if key in ("SENIOR DISC", "SOLO PARENT", "PWD DISC", "NACD", "MEDAL OF VALOR"):
                while(checkIfExistWithRegex(dlg, 'PAX')):
                    clickKeypad(dlg, "check")
                inputText(dlg, customer_id, "ID")
                # clickKeypad(dlg, "check")
                inputText(dlg, customer_name, "Name")
                # clickKeypad(dlg, "check")
                inputText(dlg, address, "Address")
                # clickKeypad(dlg, "check")
                inputText(dlg, tin, "TIN")
                # clickKeypad(dlg, "check")
                inputText(dlg, bus_style, "Bus Style")
                clickKeypad(dlg, "check")
                return
            return
    print(f"Warning: No configure  discount found for '{disc_name}'")