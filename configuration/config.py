from types import SimpleNamespace


config_dict = {
    "manager_cred": {
        "manager_id": "11",
        "manager_pass": "QWERQWER1",
    },

    "cashier_signon": {
        "btn_name": "CASHIER\r\nSIGNON",
        "cashier_id": "22",
        "cashier_pass": "QWERQWER2",
    },
    "transact": { 
        "prod_group": "MAIN DISH",
        "product": "BRAISED\r\nBEEF",
        "manager_id": "11",
        "manager_pass": "QWERQWER1",
        "disc": [
            "EMPLOYEE DISC",
            "PROMO AMOUNT",
            "SENIOR DISC",
            "SOLO PARENT",
            "PWD DISC",
            "NACD",
            "MEDAL OF VALOR"
        ],
        "customer_name" : 'CHRISTIAN LEGUIZ',
        "customer_id" : '123131313',
        "address" : "758 Delpan",
        "tin" : "1231312",
        "bus_style" : "12313131"
    },
    "delivery_transact" : {
        "prod_group": "MAIN DISH",
        "product": "BRAISED\r\nBEEF",
        "manager_id": "11",
        "manager_pass": "QWERQWER1",
        "disc": [
            "EMPLOYEE DISC",
            "PROMO AMOUNT",
            "SENIOR DISC ",
            "SOLO PARENT",
            "PWD DISC",
            "NACD",
            "MEDAL OF VALOR"
        ],
        "customer_name" : 'CHRISTIAN LEGUIZ',
        "customer_id" : '12313 1313',
        "address" : "758 Delpan",
        "tin" : "1231 312",
        "bus_style" : "123 13131",
        "phone" : "123131312",
        "loc" : "123",
        "name" : "christian leguiz",
        "address" : "123 delpan",
        "address2" : "123 delpan",
        "grid" : "123",
        "comment" : "add sauce",
        "note" : "fast del"
    },
    "free_transact": {
        "prod_group": "MAIN DISH",
        "product": "BRAISED\r\nBEEF",
        "free_tender" : [
            "MARKETING",
            "REPRESENTA\r\nTION"
        ],
        "charge_to" : "758"
    },
    "bulk_transact": { 
        "prod_group": "MAIN DISH",
        "product": "BRAISED\r\nBEEF",
        "deposit_name" : "DEPOSIT",
        "manager_id": "11",
        "manager_pass": "QWERQWER1",
        "disc": [
            "EMPLOYEE DISC",
            "PROMO AMOUNT",
            "SENIOR DISC",
            "SOLO PARENT",
            "PWD DISC",
            "NACD",
            "MEDAL OF VALOR"
        ],
        "customer_name" : 'CHRISTIAN LEGUIZ',
        "customer_id" : '1231313',
        "address" : "758 Delpan",
        "tin" : "1231312",
        "bus_style" : "12313131",
         #bulk deposit info
        "name" : "CHRISTIAN LEGUIZ",
        "time" : "7:00PM", #make sure the format is like this 7:00PM
        "funcRoom" : "NB1"
    },
}

# Convert all nested dicts to objects (dot-accessible)
def dict_to_namespace(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{key: dict_to_namespace(value) for key, value in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    return d

config = dict_to_namespace(config_dict)
