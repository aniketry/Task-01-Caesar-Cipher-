# Encryption of user given message

def encrypt(text, shift):
    encrypted_text = ""

    for char in text:

        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)   #ASCII OF lowercase 'a' is 97

        elif char.isupper():

            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)   #ASCII OF uppercase 'A' is 65

        else:
            encrypted_text += char

    return encrypted_text

# Decryption of user given message

def decrypt(text, shift):
    decrypted_text = ""

    for char in text:

        if char.islower():

            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)

        elif char.isupper():

            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)

        else:
            decrypted_text += char

    return decrypted_text

# Taking input from the user

originalMessage = input("Enter the message: ")

shiftValue = int(input("Assign shift value: "))

encryptedMessage = encrypt(originalMessage, shiftValue)

print("\nEncrypted Message:", encryptedMessage)

decryptedMessage = decrypt(encryptedMessage, shiftValue)

print("Decrypted Message:", decryptedMessage)