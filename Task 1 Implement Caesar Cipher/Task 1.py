#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:14:29 2024

@author: mahsa
"""

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (a positive integer): "))
    
    if choice == 'encrypt':
        encrypted_message = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
