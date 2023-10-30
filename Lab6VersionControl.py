def decode(encoded_str):
    return_str = ""
    lookup_str = "7890123456"
    for i in encoded_str:
        return_str += str(lookup_str[int(i)])
    return return_str


def encode(decoded_str):
    pass


def main():
    print("Menu\n" + "-" * 13 + "\n1. Encode\n2. Decode\n3. Quit\n")
    menu_option = int(input("Please enter an option: "))
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!")

main()
