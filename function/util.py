import random 
import time

def checkIfExist(dlg, name, control_type = "Button"): 
    child = dlg.child_window(title=name, control_type=control_type)
    if(child.exists()):
        return True
    return False

def generate_random_number(digits: int) -> int:
    """Generate a random number with the specified number of digits."""
    if digits < 1:
        raise ValueError("Number of digits must be at least 1")
    
    lower_bound = 10**(digits - 1)  # Smallest number with given digits (e.g., 100 for 3 digits)
    upper_bound = (10**digits) - 1  # Largest number with given digits (e.g., 999 for 3 digits)

    return random.randint(lower_bound, upper_bound)


