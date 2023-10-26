def decode(encoded_str):
    return_str = ""
    lookup_str = "7890123456"
    for i in encoded_str:
        return_str += str(lookup_str[int(i)])
    return return_str

def main():
    print("Hi")

main()
