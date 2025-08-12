from PIL import Image

def to_bin(data):
    return ''.join(format(ord(c), '08b') for c in data)

def hide_message(img_path, message, output_path):
    img = Image.open(img_path)
    img = img.convert('RGB')
    img = img.rotate(90, expand=True)
    pixels = img.load()

    message += '||END||'
    binary_msg = to_bin(message)
    msg_len = len(binary_msg)

    width, height = img.size
    capacity = width * height * 3

    if msg_len > capacity:
        print("Message too long for this image!")
        return

    idx = 0
    for y in range(height):
        for x in range(width):
            if idx >= msg_len:
                break
            r, g, b = pixels[x, y]
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')

            if idx < msg_len:
                r_bin = r_bin[:-1] + binary_msg[idx]
                idx += 1
            if idx < msg_len:
                g_bin = g_bin[:-1] + binary_msg[idx]
                idx += 1
            if idx < msg_len:
                b_bin = b_bin[:-1] + binary_msg[idx]
                idx += 1

            pixels[x, y] = (int(r_bin, 2), int(g_bin, 2), int(b_bin, 2))

    img.save(output_path)
    print(f"Message hidden in {output_path}")

if __name__ == "__main__":
    img_path = input("Enter path to source image: ")
    message = input("Enter your secret message: ")
    output_path = input("Enter output image name (e.g. output.png): ")
    hide_message(img_path, message, output_path)
