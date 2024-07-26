# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

def encrypt_image(image_path):
    img = cv2.imread(image_path)

    # Example of encryption: bitwise XOR operation with a mask
    mask = np.random.randint(0, 256, img.shape, dtype=np.uint8)  # Generate random mask
    encrypted_img = cv2.bitwise_xor(img, mask)

    encrypted_image_path = image_path.replace('.png', '_encrypted.png')  # Adjust file extension if necessary
    cv2.imwrite(encrypted_image_path, encrypted_img)
    print(f"Image encrypted and saved as: {encrypted_image_path}")

def decrypt_image(encrypted_image_path):
    encrypted_img = cv2.imread(encrypted_image_path)

    # Example of decryption: apply bitwise XOR operation with the same mask
    mask = np.random.randint(0, 256, encrypted_img.shape, dtype=np.uint8)  # Same mask used in encryption
    decrypted_img = cv2.bitwise_xor(encrypted_img, mask)

    decrypted_image_path = encrypted_image_path.replace('_encrypted.png', '_decrypted.png')  # Adjust file extension
    cv2.imwrite(decrypted_image_path, decrypted_img)
    print(f"Image decrypted and saved as: {decrypted_image_path}")

def main():
    choice = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt): ").lower()
    
    if choice == 'encrypt':
        image_path = input("Enter the path to the image file (.png format recommended): ")
        encrypt_image(image_path)
    elif choice == 'decrypt':
        encrypted_image_path = input("Enter the path to the encrypted image file (.png format): ")
        decrypt_image(encrypted_image_path)
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
