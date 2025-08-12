# StegoHide — LSB Image Encoder & Decoder

StegoHide is a simple **Least Significant Bit (LSB)** steganography tool written in Python.  
It allows you to **hide secret text messages** inside image files and later **extract** them, using minimal visual changes that are nearly undetectable to the human eye.

> 💡 You can also check out **StegoScanner** to analyze images for hidden messages:  
> [https://github.com/bax082024/StegoScanner-PY.git](https://github.com/bax082024/StegoScanner-PY.git)

---

## ✨ Features

- **Encoder** — Hide any text message inside a PNG or other lossless image format.
- **Decoder** — Retrieve hidden messages from stego images.
- Uses **RGB LSB manipulation** for data embedding.
- Built-in **END marker** (`||END||`) ensures clean message extraction.
- Minimal distortion to original image.

---

## 📦 Requirements

- Python **3.8+**
- `Pillow`

Install dependencies with:

  - `pip install pillow`

---

## Installation

1. Clone or download this repository
2. Place encoder.py and decoder.py in the same directory.
3. Install dependencies.

---

## How to use 

**Encoding**

`python encoder.py`

You will be prompted for:

1. Source image path 

2. Secret message — the text you want to hide.

3. Output file name — example: stego.png.

The script embeds the message into the image’s LSBs and saves the new image.


**Decoding**

`python decoder.py`

You will be prompted for:

1. Image path — the stego image containing the hidden message.

The script will scan pixel LSBs and reconstruct the hidden message until it finds the ||END|| marker.

---

## Notes

- Works best with lossless image formats (PNG, BMP).
JPEG compression will destroy LSB-encoded data.

- Message capacity depends on image size × 3 channels.
For example, a 1000×1000 image can store 3,000,000 bits (~375 KB).

- This tool is for educational purposes and should not be used for illegal activity.

---

## Contact

For questions or feedback, please contact :
- **bax082024@gmail.com**