from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText

def clickDiscount(dlg, disc_name, customer_id, customer_name, address, tin, bus_style, promo_amount=20 ):
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
                inputText(dlg, promo_amount)
                clickKeypad(dlg, "check")
                return
            if key in ("SENIOR DISC", "SOLO PARENT", "PWD DISC", "NACD", "MEDAL OF VALOR"):
                clickKeypad(dlg, "check")
                clickKeypad(dlg, "check")
                inputText(dlg, customer_id)
                clickKeypad(dlg, "check")
                inputText(dlg, customer_name)
                clickKeypad(dlg, "check")
                inputText(dlg, address)
                clickKeypad(dlg, "check")
                inputText(dlg, tin)
                clickKeypad(dlg, "check")
                inputText(dlg, bus_style)
                clickKeypad(dlg, "check")
                return
            return
    print(f"Warning: No matching discount found for '{disc_name}'")