# Caesar Cipher Program

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            # Check uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')

            # Shift character
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)

            result += encrypted_char

        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher Program =====")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_message = encrypt(message, shift)

print("\nEncrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)

print("Decrypted Message:", decrypted_message)