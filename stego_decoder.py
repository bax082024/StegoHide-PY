from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    pixels = img.load()

    binary_data = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += bin(r)[-1]
            binary_data += bin(g)[-1]
            binary_data += bin(b)[-1]

    # binary to 8-bit chunks
    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""

    for i, byte in enumerate(bytes_data):
        try:
            char = chr(int(byte, 2))
        except ValueError:
            print(" Invalid byte encountered, stopping decode.")
            break
        message += char

        if "||END||" in message:
            break

        if i % 100 == 0:
            print(f" Decoded {i} characters...")

        if i > 5000:
            print(" Reached 5000 characters without finding END marker.")
            break

    return message.replace("||END||", "")

if __name__ == "__main__":
    path = input("Enter path to image with hidden message: ")
    secret = decode_message(path)
    print("\n Hidden Message:")
    print(secret if secret else "(No message found)")
