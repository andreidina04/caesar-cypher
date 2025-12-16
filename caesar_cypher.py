alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % 26
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % 26
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the decoded result: {cipher_text}")

def main():
    print("Welcome to Caesar Cipher!")
    while True:
        try:
            choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            if choice == "encode":
                encrypt(text, shift)
            elif choice == "decode":
                decrypt(text, shift)
            else:
                print("Invalid choice!")

            restart = input("Type 'yes' to continue, 'no' to exit:\n").lower()
            if restart != "yes":
                break

        except ValueError:
            print("Shift must be a number!")

main()
