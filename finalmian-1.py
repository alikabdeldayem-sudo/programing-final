

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