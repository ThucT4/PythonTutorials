def substitution_cipher(message, letter_map):
    encoded_mess = ''

    for char in message:
        code = ord(char)

        # Skip non-alphabetical characters
        if not char.isalpha():
            encoded_mess += char
            continue

        if char.isupper():
            encoded_mess += letter_map[code - 65]

        if char.islower():
            encoded_mess += letter_map[code - 97].lower()

    return encoded_mess


def decode(message, letter_map):
    decode_mess = ''

    for char in message:
        # Skip non-alphabetical characters
        if not char.isalpha():
            decode_mess += char
            continue

        for idx in range(len(letter_map)-1):
            if char == letter_map[idx] or char == letter_map[idx].lower():
                if char.isupper():
                    decode_mess += chr(idx + 65)

                if char.islower():
                    decode_mess += chr(idx + 97).lower()

    return decode_mess


if __name__ == "__main__":
    encode = substitution_cipher("Introduction to Programming 3rd sems 2022", "QTGABCDEFHIJKSUVXLMNOPRYZW")
    print(encode)

    mess = decode(encode, "QTGABCDEFHIJKSUVXLMNOPRYZW")
    print(mess)
