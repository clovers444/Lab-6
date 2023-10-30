# Alicia Ellis

# Prints the menu
def print_menu():
    print("Menu"
          "\n-------------"
          "\n1. Encode"
          "\n2. Decode"
          "\n3. Quit"
          )

# Encodes the password
def encode(password):
    # Variables
    password_digits = [*password] # Creates a list with the digits in the password
    # A dictionary with the password digits and their corresponding encoded values
    encoded_digits = {
        "0": "3",
        "1": "4",
        "2": "5",
        "3": "6",
        "4": "7",
        "5": "8",
        "6": "9",
        "7": "0",
        "8": "1",
        "9": "2"
    }
    encoded_password = "" # Creates an empty string to store the password

    for digit in password_digits: # Goes through every digit in the list containing the password digits
        if digit in encoded_digits:
            # If the digit is in the dictionary it is encoded and added to the empty string
            encoded_password += encoded_digits[digit]

    return encoded_password

# Decodes the password
def decode(password):
    pass

def main():
    while True:
        print_menu()

        menu_choice = int(input("\nPlease enter an option: ")) # Asks user to enter a menu option

        if menu_choice == 1:
            password = input("\nPlease enter your password to encode: ") # Asks the user to input a password to encode
            if (len(password) == 8) and (password.isnumeric()): # Checks if the password is valid
                encoded_password = encode(password) # Encodes the password and stores it
                print("Your password has been encoded and stored!\n")
            else:
                print("\nInvalid input.\n") # Prints an error message if the password input is invalid
        elif menu_choice == 2:
            decoded_password = decode(encoded_password) # Decodes the password and stores it
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif menu_choice == 3:
            break # Exits loop
        else:
            print("\nInvalid input.\n") # Prints an error message if the menu input is invalid


if __name__ == '__main__':
    main()
