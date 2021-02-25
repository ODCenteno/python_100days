from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text_list = []
    plain_text_list = [letter for letter in text]
    len_alpha = len(alphabet)

    for letter in plain_text_list:
        letter_index_alpha = alphabet.index(letter) # obtenemos el índice de la letra en alfabeto
        if letter not in alphabet:
            cipher_text_list.append('X')
        elif letter == ' ':
            cipher_text_list.append()
        elif (letter_index_alpha + shift) > len_alpha:
            cipher_index = (letter_index_alpha + shift) - len_alpha
            cipher_letter = alphabet[cipher_index]
            cipher_text_list.append(cipher_letter)
        else:
            cipher_letter = alphabet[letter_index_alpha + shift]
            cipher_text_list.append(cipher_letter)
    
    cipher_text = "".join(cipher_text_list)
    print(f'The encoded text is: {cipher_text}')
    return cipher_text

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def decrypt(text, shift):
    len_alpha = len(alphabet)
    decode_text = ''

    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position < 0:
            decode_letter = alphabet[new_position]
            decode_text += decode_letter
        else:
            decode_letter = alphabet[new_position]
            decode_text += decode_letter
    print(f"The decoded text is {decode_text}")
    return decode_text

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'encode':
        cipher_text = encrypt(text, shift)
        decrypt(cipher_text, shift)
    elif cipher_direction == 'decode':
        decode_text = decrypt(text, shift)
        encrypt(decode_text, shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

if __name__ == '__main__':
    print(f'{logo}')
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    #/////////// Old unimproved code:
    # if direction == 'encode':
    #     text = input("Type your message:\n").lower()
    #     shift = int(input("Type the shift number:\n"))
    #     cipher_text = encrypt(text, shift)
    #     decrypt(cipher_text, shift)
    # elif direction == 'decode':
    #     text = input("Type your message:\n").lower()
    #     shift = int(input("Type the shift number:\n"))
    #     decode_text = decrypt(text, shift)
    #     encrypt(decode_text, shift)
