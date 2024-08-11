'''
Task-01
Implementing Caesar Cipher
'''

def Encryption(message,shift):
    result = ""

    for x in range(len(message)):
        char = message[x]
        
        if char==" ":
            result+=" "

        elif (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)

        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    
    return result

def Decryption(message,shift):
    return Encryption(message, -shift)

message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value: "))

encrypted_message = Encryption(message, shift)
decrypted_message = Decryption(encrypted_message, shift)

print("\nEncrypted message:", encrypted_message)
print("\nDecrypted message:", decrypted_message)
print("\n\n")