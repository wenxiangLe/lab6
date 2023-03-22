def encode(password):
    password = list(password)
    list_password = []
    for digit in password:
        digit = int(digit)
        digit = digit + 3
        list_password.append(digit)
    encoded_password = "".join(str(digit) for digit in list_password)
    return encoded_password



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("RLE Menu\n--------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = input("Please enter an option: ")
        if user_input == "3":
            # print("Exiting...")
            break
        elif user_input == "1":
            password = input("Please enter your password to encode: ")
            password1 = encode(password)
            print(password1)
            print("Your password has been encoded and stored!")
            # print("File loaded.")
        elif user_input == "2":
            break




