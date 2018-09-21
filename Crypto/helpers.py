def alphabet_position(char):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()
    if char in alphabet_lower:
        alpha_index = alphabet_lower.find(char)
    else:
        if char in alphabet_upper:
            alpha_index = alphabet_upper.find(char)
    return alpha_index

def rotate_character(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()
    if char in alphabet_lower:
        orig_index = alphabet_position(char)
        new_char = alphabet_lower[(orig_index + rot) % 26]
    elif char in alphabet_upper:
         orig_index = alphabet_position(char)
         new_char = alphabet_upper[(orig_index + rot) % 26]
    else:
        new_char = char
    return new_char
