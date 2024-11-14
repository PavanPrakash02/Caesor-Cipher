alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
             'y', 'z']
n = len(alphabet)
while True:
    directions = input("Type 'encode' to encrypt, type 'decode' to decrypt or type q to exit:\n")
    if directions == 'q':
        break
    text = input("Type your message:\n").lower()
    key = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift):
        cipher_text = ''
        for char in plain_text:
            position = alphabet.index(char)
            new_position = (position + shift) % n
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")

    def decrypt(cipher_text, shift):
        plain_text = ''
        for  char in cipher_text:
            position = alphabet.index(char)
            new_position = (position - shift) % n
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"The decoded text is {plain_text}")

    if directions == 'encode':
        encrypt(text, key)
    elif  directions == 'decode':
        decrypt(text, key)




