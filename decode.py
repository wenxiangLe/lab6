def decode(decode_password):

    password = list(decode_password)
    list_password = []
    for digit in password:
        digit = int(digit)
        digit = digit - 3
        list_password.append(digit)
    encoded_password = "".join(str(digit) for digit in list_password)
    return encoded_password