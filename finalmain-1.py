

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

