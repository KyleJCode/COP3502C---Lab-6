"""
Kyle Jeter and Phoenix Cushman
Lab 6 - Version Control
Due: 10/31/2023
"""

def decode(encoded_str):
    return_str = ""
    lookup_str = "7890123456"
    for i in encoded_str:
        return_str += str(lookup_str[int(i)])   # Looks up the decoded number based on the index of the string
    return return_str


def encode(decoded_str):
    return_str = ""
    nums = {0:3, 1:4, 2:5, 3:6, 4:7, 5:8, 6:9, 7:0, 8:1, 9:2, } # Dictionary with encoded nums
    for i in decoded_str:
        return_str += str(nums[int(i)])     # Uses the number to access dictionary element and decode
    return return_str


def main():
    password = ""
    menu_option = 0

    while menu_option != 3:
        print("Menu\n" + "-" * 13 + "\n1. Encode\n2. Decode\n3. Quit\n")    # Displays the menu
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")  # Encoder menu option
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_option == 2:
            decoded_password = decode(encoded_password)     # Decoder menu option
            print("The encoded password is " + encoded_password, end="")
            print(", and the original password is " + decoded_password + ".")
        elif menu_option == 3:
            break
        else:
            print("Please Enter a Valid Menu Option")   # Input validation


main()
