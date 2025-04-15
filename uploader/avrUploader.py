import subprocess
from tkinter import messagebox

def uploadFirmwareAvr(firmwareFile, port, boardVariant):

    if boardVariant == "Cortu gen1":
        
        boardVariant = "uno"
        message = "Uploading firmware to corTu Gen 1"

    else:
        
        boardVariant = "mega"
        message = "Uploading firmware to corTu Gen 2"

    """Upload firmware to an AVR microcontroller."""

    # Compile code

    try:
        
        avrd_compile = [

            "arduino-cli",  # Path to arduino-cli (make sure it's in your PATH)
            "compile",  # Command to upload the firmware
            "--fqbn", f"arduino:avr:{boardVariant}",  # Specify the board (e.g., arduino:avr:uno)
            "--port", port,  # Specify the serial port (e.g., /dev/ttyACM0 or COM3)
            firmwareFile  # Path to the firmware file (blink.ino)

        ]
        
        # Upload the firmware

        messagebox.showinfo("Firmware upload", message)
        subprocess.run(avrd_compile, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        messagebox.showinfo("Firmware upload", "Successfully uploaded")

    except subprocess.CalledProcessError as e:

        error_message = e.stderr
        
        # Display the upload error message in a messagebox
        messagebox.showerror("Upload Error", message=error_message)
    
    # Upload code
    try:

        avrd_upload = [

            "arduino-cli",  # Path to arduino-cli (make sure it's in your PATH)
            "upload",  # Command to upload the firmware
            "--fqbn", f"arduino:avr:{boardVariant}",  # Specify the board (e.g., arduino:avr:uno)
            "--port", port,  # Specify the serial port (e.g., /dev/ttyACM0 or COM3)
            firmwareFile  # Path to the firmware file (blink.ino)

        ]
        
        # Upload the firmware

        messagebox.showinfo("Firmware upload", message)
        subprocess.run(avrd_upload, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        messagebox.showinfo("Firmware upload", "Successfully uploaded")

    except subprocess.CalledProcessError as e:

        error_message = e.stderr
        
        # Display the upload error message in a messagebox
        messagebox.showerror("Upload Error", message=error_message)

