alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    coded_word = ""
    for letters in original_text:
        new_position = alphabet.index(letters) + shift_amount
        new_position %= len(alphabet) #I original duplicated alphabet toa void out of range but this more elegant
        coded_word += alphabet[new_position]
    print(f"Here is the encoded result: {coded_word}")

encrypt(text, shift)