from function.clickButton import clickBtn
from function.clickButton import clickKeypad

def inputText(dlg, text):
    for char in str(text):
        if char.isdigit():  # If the character is a number (0-9)
            clickKeypad(dlg, int(char))
        elif char.isalpha():  # If the character is a letter (a-z, A-Z)
            clickBtn(dlg, char.upper())  # Convert to uppercase for consistency
        elif char.isspace():  # If the character is a space
            clickBtn(dlg, "space bar")  # Adjust this based on your system
        else:
            clickBtn(dlg, char)
            #print(f"Warning: Unsupported character '{char}' ignored.")