from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()
    key_index = 0
    encrypted_message = []
    for char in text:
            if not char.isalpha():
                encrypted_message += char
            elif char.isalpha():
                rot = alphabet_position(key[key_index])
                encrypted_message += rotate_character(char, rot)
                if key_index == (len(key) - 1):
                    key_index = 0
                else:
                    key_index += 1
    return ''.join(encrypted_message)
            
def main():
    from sys import argv
    print("This is what the user typed on the command line:", argv)
    message = input("Type a message: ")
    keyword = input("Encryption key: ")
    print(encrypt(message, keyword))

if __name__ == "__main__":
    main()


    
   
