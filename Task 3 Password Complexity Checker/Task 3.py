#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:16:20 2024

@author: mahsa
"""

def check_password_strength(password):
    # Criteria for password strength
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    special_error = not any(char in '!@#$%^&*()-+' for char in password)

    # Determine the strength based on criteria
    if length_error:
        return 'Password is too short, it should be at least 8 characters.'
    elif digit_error or uppercase_error or lowercase_error or special_error:
        feedback = []
        if digit_error:
            feedback.append('Password should contain at least one digit (0-9).')
        if uppercase_error:
            feedback.append('Password should contain at least one uppercase letter (A-Z).')
        if lowercase_error:
            feedback.append('Password should contain at least one lowercase letter (a-z).')
        if special_error:
            feedback.append('Password should contain at least one special character (!@#$%^&*()-+).')
        return ' '.join(feedback)
    else:
        return 'Password is strong.'

def main():
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()
