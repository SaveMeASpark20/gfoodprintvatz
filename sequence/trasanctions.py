from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickDisc import clickDiscount
from function.clickButton import clickDeliveryBtn
from function.clickButton import doubleClickDateArrow
from function.util import checkIfExist
from function.util import generate_random_number
from function.input import inputText
from sequence.bacchus import inputServerAndTable
from configuration.config import config
from datetime import datetime
import time
import random

def dineIn(dlg, transaction_type = "DINE IN",  ):
    restaurant_type = config.restaurant_type
    if(restaurant_type == 'FINE DINING'):
        bacchusDineIn(dlg)
    elif(restaurant_type == 'FASTFOOD'):
        foodDineIn(dlg)
    else :
        print('Neither Fine Dining or FastFood')
    # dine_in = config.transact
    # clickBtn(dlg, transaction_type)
    # for disc in dine_in.disc :
    #     print(disc)
    #     clickBtn(dlg, dine_in.prod_group)
    #     clickBtn(dlg, dine_in.product)
    #     clickKeypad(dlg, "check")
    #     clickBtn(dlg, "DISC")
    #     inputText(dlg, dine_in.manager_id)
    #     clickKeypad(dlg, "check")
    #     inputText(dlg, dine_in.manager_pass)
    #     clickKeypad(dlg, "check")
    #     clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style)
    #     clickBtn(dlg, "CASH")
    #     clickKeypad(dlg, "exact amount")
    #     if(disc == "EMPLOYEE DISC" or disc == "PROMO AMOUNT"): 
    #         clickKeypad(dlg, 1)
    #         clickKeypad(dlg, "check")
    #         clickBtn(dlg, "YES")
    #     clickBtn(dlg, "OK")
    #     if(checkIfExist(dlg,'RE-ROUTE')) :
    #         clickBtn(dlg, 'RE-ROUTE')
    #         clickBtn(dlg, 'P O S')

def takeOut(dlg, transaction_type = "TAKE OUT", ):
    restaurant_type = config.restaurant_type
    if(restaurant_type == 'FINE DINING'):
        bacchusTakeOut(dlg)
    elif(restaurant_type == 'FASTFOOD'):
        foodTakeOut(dlg)
    else :
        print('Neither Fine Dining or Fast Food')
    # take_out = config.transact
    # clickBtn(dlg, transaction_type)
    # for disc in take_out.disc :
    #     clickBtn(dlg, take_out.prod_group)
    #     clickBtn(dlg, take_out.product)
    #     clickKeypad(dlg, "check")
    #     clickBtn(dlg, "DISC")
    #     inputText(dlg, take_out.manager_id)
    #     clickKeypad(dlg, "check")
    #     inputText(dlg, take_out.manager_pass)
    #     clickKeypad(dlg, "check")
    #     clickDiscount(dlg, disc, take_out.customer_id, take_out.customer_name, take_out.address, take_out.tin, take_out.bus_style)
    #     clickBtn(dlg, "CASH")
    #     clickKeypad(dlg, "exact amount")
        
    #     clickKeypad(dlg, 1)
    #     clickKeypad(dlg, "check")
    #     clickBtn(dlg, "YES")
    #     clickBtn(dlg, "OK")
    #     if(checkIfExist(dlg,'RE-ROUTE')) :
    #         clickBtn(dlg, 'RE-ROUTE')
    #         clickBtn(dlg, 'P O S')


def delivery(dlg, transaction_type ="DELIVERY") :
    delivery = config.delivery_transact
    clickBtn(dlg, transaction_type)
    for disc in delivery.disc :
        print(disc)
        clickDeliveryBtn(dlg, "new") #new 
        inputText(dlg, delivery.phone)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.loc)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.name)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.address)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.address2)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.grid)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.comment)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.note)
        clickKeypad(dlg, "check")
        clickBtn(dlg, delivery.prod_group)
        clickBtn(dlg, delivery.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText(dlg, delivery.manager_id)
        clickKeypad(dlg, "check")
        inputText(dlg, delivery.manager_pass)
        clickKeypad(dlg, "check")
        clickDiscount(dlg, disc, delivery.customer_id, delivery.customer_name, delivery.address, delivery.tin, delivery.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        # clickBtn(dlg, "OK")
        clickDeliveryBtn(dlg, "driver")
        inputText(dlg, '33')
        clickKeypad(dlg, "check")
        clickDeliveryBtn(dlg, "check")
        now = datetime.now()
        seconds_to_wait = 60 - now.second  # Calculate seconds until next minute

        print(f"Current Time: {now.strftime('%H:%M:%S')}")
        time.sleep(seconds_to_wait)  # Sleep until next minute

        updated_time = datetime.now().strftime("%H:%M")
        print(f"New Time: {updated_time}")
        inputTime =updated_time.replace(":", "")
        print(f"Update new Time: {inputTime}")
        inputText(dlg, inputTime)
        clickKeypad(dlg, "check")
        clickKeypad(dlg, "check")
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def misc(dlg, transaction_type = "MISC", ):
    misc = config.transact
    clickBtn(dlg, transaction_type)
    for disc in misc.disc :
        clickBtn(dlg, misc.prod_group)
        clickBtn(dlg, misc.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText(dlg, misc.manager_id)
        clickKeypad(dlg, "check")
        inputText(dlg, misc.manager_pass)
        clickKeypad(dlg, "check")
        clickDiscount(dlg, disc, misc.customer_id, misc.customer_name, misc.address, misc.tin, misc.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def free(dlg, transaction_type = "FREE" ):
    clickBtn(dlg, transaction_type)
    free = config.free_transact
    for tender in free.free_tender:
        clickBtn(dlg, free.prod_group)
        clickBtn(dlg, free.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, tender)
        inputText(dlg, free.charge_to)
        clickKeypad(dlg, "check")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')



def bulk(dlg, transaction_type = 'BULK\r\nORDER'):
    clickBtn(dlg, transaction_type)
    bulk = config.bulk_transact
    for disc in bulk.disc :
        clickBtn(dlg, bulk.prod_group)
        clickBtn(dlg, bulk.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, bulk.deposit_name)
        duplicate_exists = True  # Set initial flag

        while duplicate_exists:
            inputText(dlg, generate_random_number(6))  # Input the random number
            clickKeypad(dlg, 'check')
            #Check if the contract number is a duplicate
            duplicate_exists = checkIfExist(dlg, 'Duplicate Contract Number!', "Text")
            if duplicate_exists:
                clickBtn('OK')  
        inputText(dlg, bulk.name)
        clickKeypad(dlg, 'check')
        inputText(dlg, generate_random_number(7))
        clickKeypad(dlg, 'check')
        doubleClickDateArrow(dlg)
        clickKeypad(dlg, 'check')
        inputText(dlg, bulk.time)
        clickKeypad(dlg, 'check')
        inputText(dlg, bulk.funcRoom)
        clickKeypad(dlg, 'check')
        clickBtn(dlg, 'DISC')
        inputText(dlg, bulk.manager_id)
        clickKeypad(dlg, 'check')
        inputText(dlg, bulk.manager_pass)
        clickKeypad(dlg, 'check')
        clickDiscount(dlg, disc, bulk.customer_id, bulk.customer_name, bulk.address, bulk.tin, bulk.bus_style, promo_amount=20)
        clickBtn(dlg, 'CASH')
        clickKeypad(dlg, "exact amount")
        clickBtn(dlg, 'RECALL', secondsToSleep=5)
        button = dlg.child_window(control_type="Button",found_index=6)
        button.click()
        clickKeypad(dlg, 'check')
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickBtn(dlg, 'CASH')
        clickBtn(dlg, 'OK')
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def foodDineIn(dlg, transaction_type='DINE IN'):
    dine_in = config.transact
    clickBtn(dlg, transaction_type)
    for disc in dine_in.disc :
        print(disc)
        clickBtn(dlg, dine_in.prod_group)
        clickBtn(dlg, dine_in.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText(dlg, dine_in.manager_id)
        clickKeypad(dlg, "check")
        inputText(dlg, dine_in.manager_pass)
        clickKeypad(dlg, "check")
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        if(disc == "EMPLOYEE DISC" or disc == "PROMO AMOUNT"): 
            clickKeypad(dlg, 1)
            clickKeypad(dlg, "check")
            clickBtn(dlg, "YES")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def foodTakeOut(dlg, transaction_type = "TAKE OUT"):
    take_out = config.transact
    clickBtn(dlg, transaction_type)
    for disc in take_out.disc :
        clickBtn(dlg, take_out.prod_group)
        clickBtn(dlg, take_out.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText(dlg, take_out.manager_id)
        clickKeypad(dlg, "check")
        inputText(dlg, take_out.manager_pass)
        clickKeypad(dlg, "check")
        clickDiscount(dlg, disc, take_out.customer_id, take_out.customer_name, take_out.address, take_out.tin, take_out.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        
        clickKeypad(dlg, 1)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "YES")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def bacchusDineIn(dlg, transaction_type='DINE IN') :
    dine_in = config.transact
    clickBtn(dlg, transaction_type)
    for disc in dine_in.disc :
        #----server and table----#
        inputText(dlg, dine_in.cashier_id)
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.table)
        inputText(dlg, '1')
        #----server and table----#
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.prod_group)
        clickBtn(dlg, dine_in.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'STORE\r\nORDER')
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')
        #----recall----#
        inputText(dlg, dine_in.cashier_id)
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.table)
        #----recall----#
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickBtn(dlg, 'DISC')
        inputText(dlg, dine_in.manager_id)
        clickKeypad(dlg, 'check')
        inputText(dlg, dine_in.manager_pass)
        clickKeypad(dlg, 'check')
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20
                    )
        clickBtn(dlg, 'CASH')
        clickKeypad(dlg, 'exact amount')
        clickBtn(dlg, "OK")

def bacchusTakeOut(dlg, transaction_type='TAKE OUT') :
    dine_in = config.transact
    clickBtn(dlg, transaction_type)
    for disc in dine_in.disc :
        #----server and table----#
        inputText(dlg, dine_in.cashier_id)
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.table)
        inputText(dlg, '1')
        #----server and table----#
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.prod_group)
        clickBtn(dlg, dine_in.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'STORE\r\nORDER')
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')
        #----recall----#
        inputText(dlg, dine_in.cashier_id)
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.table)
        #----recall----#
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickBtn(dlg, 'DISC')
        inputText(dlg, dine_in.manager_id)
        clickKeypad(dlg, 'check')
        inputText(dlg, dine_in.manager_pass)
        clickKeypad(dlg, 'check')
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20
                    )
        clickBtn(dlg, 'CASH')
        clickKeypad(dlg, 'exact amount')
        clickBtn(dlg, "OK")