import subprocess
from tkinter import messagebox
def upload_firmware_avr(firmware_file, port, board_variant):
    """Upload firmware to an AVR microcontroller."""
    # Define the `avrdude` command based on the selected board variant
    # avrdude_command = [
    #     "avrdude", "-c", "arduino", "-p", board_variant, "-P", port, "-U", f"flash:w:{firmware_file}:i"
    # ]

    # avrd = "arduino-cli compile --fqbn arduino:avr:uno /home/n1lby73/corskinter/arduino/blink/blink.ino"

    avrd = [
        "arduino-cli",  # Path to arduino-cli (make sure it's in your PATH)
        "compile",
        "--fqbn", "arduino:avr:uno",  # Specify the board (change if needed)
        "/home/n1lby73/corskinter/arduino/blink/blink.ino",  # Path to the firmware file
        "--output-dir", "/home/n1lby73/corskinter/arduino"
    ]

    
    # Run the `avrdude` command to upload firmware
    try:
        print("here")
        subprocess.run(avrd, check=True)

         # Step 2: Upload the firmware to the Arduino
        avrd_upload = [
            "arduino-cli",  # Path to arduino-cli (make sure it's in your PATH)
            "upload",  # Command to upload the firmware
            "--fqbn", f"arduino:avr:uno",  # Specify the board (e.g., arduino:avr:uno)
            "--port", port,  # Specify the serial port (e.g., /dev/ttyACM0 or COM3)
            "/home/n1lby73/corskinter/arduino/blink/blink.ino"  # Path to the firmware file (blink.ino)
        ]
        
        # Upload the firmware
        print(f"Uploading firmware to {port}...")
        subprocess.run(avrd_upload, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print("Firmware uploaded successfully.")

    except subprocess.CalledProcessError as e:

        error_message = e.stderr
        print(f"Error: {error_message}")
        
        # Display the error message in a messagebox
        messagebox.showerror("Upload Error", message=error_message)

        print(f"Error: {e}")
        raise  # Re-raise the error for handling higher up
