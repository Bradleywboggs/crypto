from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_message = ''
    for char in text:
        new_char = rotate_character(char, rot)
        encrypted_message += new_char
    return encrypted_message

def main():
    message = input("Type a message: ")
    rotation = int(input("Rotate by (integer): "))
    print(encrypt(message, rotation))

if __name__ == "__main__":
    main()