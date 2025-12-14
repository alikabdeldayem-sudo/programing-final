

def to_binary(text):
#Convert text to binary
    return ''.join(format(ord(c), '08b') for c in text)


def from_binary(binary_data):
#Convert binary back to text
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i + 8]
        message += chr(int(byte, 2))
    return message

def encode_message(image_path, message):
#Hide a message inside an image
    with open(image_path, 'rb') as img:
        image_bytes = bytearray(img.read())

    binary_message = to_binary(message) + '00000000'

    if len(binary_message) > (len(image_bytes) - 54):
        print("Error: Message is too large for the image.")
        return

    index = 0
    for i in range(54, len(image_bytes)):
        if index < len(binary_message):
            image_bytes[i] = (image_bytes[i] & 0xFE) | int(binary_message[index])
            index += 1

    output_path = "encoded_image.bmp"
    with open(output_path, 'wb') as out:
        out.write(image_bytes)

    print("Message encrypted and saved as:", output_path)

def decode_message(image_path, correct_password):
    #Extract a message from an image (3 attempts allowed for password)
    attempts = 3

    while attempts > 0:
        entered = input("Enter password to decrypt: ")

        if entered == correct_password:
            with open(image_path, 'rb') as img:
                image_bytes = bytearray(img.read())


            binary_data = ""
            for i in range(54, len(image_bytes)):
                binary_data += str(image_bytes[i] & 1)


            end_index = binary_data.find('00000000')
            if end_index != -1:
                message = from_binary(binary_data[:end_index])
                print("Decrypted message:", message)
            else:
                print("No hidden message found.")
            return
        else:
            attempts -= 1
            print(f"Wrong password. Attempts left: {attempts}")

    print("Access denied.")


def is_strong_password(password):
#this is to test for the passwords strength
        if len(password) < 8:
            return False

        has_upper = has_lower = has_digit = has_symbol = False
        symbols = "!@#$%^&*(),.?\":{}|<>"

        for c in password:
            if c.isupper():
                has_upper = True
            elif c.islower():
                has_lower = True
            elif c.isdigit():
                has_digit = True
            elif c in symbols:
                has_symbol = True
        return has_upper and has_lower and has_digit and has_symbol


print("Image Steganography Program Encrypter and Decrypter")
print("1. Encrypt (Hide a message)")
print("2. Decrypt (Extract a message)")


choice = input("Choose an option (1 or 2): ")

if choice == "1":
    image_path = input("Enter the path to the BMP image(ONLY BMP!): ")

    password = input("Create a password: ")
    while not is_strong_password(password):
        print("Password must contain uppercase, lowercase, number, and symbol.")
        password = input("Create a password: ")

    message = input("Enter message to hide: ")
    encode_message(image_path, message)

elif choice == "2":
    image_path = input("Enter path to encoded BMP image: ")
    password = input("Enter password to decrypt: ")
    decode_message(image_path, password)

else:
    print("Invalid option. Please restart the program.")