import msvcrt

# Initialize an empty log to store keystrokes
key_log = []

print("Keylogger started. Press 'Esc' to stop logging and see what you've typed within the terminal.")
# Define the function to start the keylogger
def start_keylogger():
    while True:
        # Wait for a key press
        if msvcrt.kbhit():
            key = msvcrt.getch()  # Capture the key pressed

            # Check for special keys
            if key == b'\r':  # Enter key
                key_log.append('\n')
                print("[Enter]", end="")  # Optional display
            elif key == b'\x08':  # Backspace key
                if key_log:
                    key_log.pop()  # Remove last character
                    print("[Backspace]", end="")  # Optional display
            elif key == b'\x1b':  # Esc key
                break  # Stop the loop
            else:
                # Add regular key to the log
                try:
                    key_log.append(key.decode("utf-8"))
                    print(key.decode("utf-8"), end="")  # Print to show keystroke capture
                except UnicodeDecodeError:
                    # Handles any undecodable characters (for non-character keys like function keys)
                    pass

    # Print the captured keystrokes after stopping
    print("\nKeylogger stopped. Captured keystrokes:")
    print("".join(key_log))

# Start the keylogger function
start_keylogger()