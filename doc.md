### **Documentation for Firmware Uploader Code**

---

#### **Overview:**

This Python program is a **firmware uploader tool** built using the `tkinter` GUI library and the `serial` module for serial communication with microcontrollers. It allows users to select a board type, choose a serial port, upload firmware, and open a serial monitor to interact with the connected device. The program communicates with Arduino-compatible boards (such as Uno, Mega) via serial connections.

---

### **1. Import Statements:**

```python
import subprocess
import tkinter as tk
import serial, threading
from tkinter import Menu, messagebox, filedialog, ttk  # module needed for combobox
import serial.tools.list_ports
from uploader.avrUploader import uploadFirmwareAvr
```

- **subprocess**: Used to run system commands (e.g., fetching available serial ports).
- **tkinter**: GUI framework for creating the user interface.
- **serial**: Handles serial communication with the connected device.
- **threading**: Allows background tasks such as serial data reading without freezing the GUI.
- **uploader.avrUploader.uploadFirmwareAvr**: Custom module for uploading firmware to AVR boards.

---

### **2. Main Window Class (`mainWindow`):**

This class handles the GUI creation and user interaction. It is inherited from `tk.Tk`, making it the main window of the application.

#### **Constructor (`__init__`):**

- **Title & Geometry**: Sets the window title and initial size.
- **Menu Bar**: Defines the menu with two options:
  - **Get Board Info**: Retrieves information about the connected board.
  - **Open Serial Monitor**: Opens a window to monitor serial communication.
- **Widgets**: Comboboxes for selecting board type and serial port, labels for displaying information, and buttons for selecting firmware files and initiating the upload process.

#### **Attributes:**
- `boards`: List of available board options (e.g., "Cortu gen1", "Cortu gen2").
- `ports`: List of available serial ports (initialized with "Select Port").
- `selectedFirmwarePath`: Stores the path of the selected firmware file.
- `connectedBoards`: Dictionary storing the mapping of ports to their corresponding board types.

---

### **3. Methods:**

#### **`boardSelected(self, event)`**:
Handles board selection changes. When a board is selected, it updates the serial port options based on available ports.

#### **`portSelected(self, event)`**:
Handles port selection changes. It displays the firmware selection button once a port is chosen.

#### **`update_ports(self)`**:
Updates the list of available serial ports and refreshes the port combobox.

#### **`fetch_ports(self)`**:
Uses the `arduino-cli` to list available boards and their corresponding serial ports. It populates the `ports` list and determines which board is connected to which port.

#### **`selectFile(self)`**:
Opens a file dialog to select an `.ino` or `.cpp` file as the firmware to be uploaded. Updates the `firmwareLabel` with the selected file path.

#### **`boardInfo(self)`**:
Displays a message box showing information about the connected board based on the selected port. If no port is selected, it prompts the user to select one.

#### **`upload(self)`**:
Validates the board and port selections and calls `uploadFirmwareAvr` to upload the selected firmware to the connected board.

#### **`openSerialMonitor(self)`**:
Opens a new window for monitoring serial data from the selected port. It allows the user to choose a baud rate and reads incoming serial data in a background thread. The serial output is displayed in a text widget.

---

### **4. Serial Monitor Functionality:**

The **serial monitor** allows you to interact with the microcontroller via serial communication. It supports:
- **Dynamic Baud Rate**: The baud rate can be changed via a combobox.
- **Threading**: A background thread reads data from the serial port without blocking the GUI.
- **Text Display**: Received serial data is displayed in a scrollable text box.

---

### **5. Supporting Functions:**

#### **`main()`**:
Starts the Tkinter application by creating an instance of `mainWindow` and calling `mainloop()`.

#### **`uploadFirmwareAvr(self.selectedFirmwarePath, self.selectPort.get(), self.boardMenu.get())`**:
This function, imported from `uploader.avrUploader`, is responsible for uploading the selected firmware to the AVR board connected via the selected serial port.

---

### **6. GUI Widgets:**

- **Comboboxes**: Used for selecting board types and serial ports.
- **Labels**: Display information such as the selected board, serial port, and firmware file.
- **Buttons**: Trigger actions like selecting a firmware file or uploading it to the board.
- **Text Widget**: Used in the serial monitor window to display serial data.
- **Menu**: Provides options for interacting with the connected board and opening the serial monitor.

---

### **7. Example Workflow:**

1. **Select Board**: Choose a board type (e.g., "Cortu gen1").
2. **Select Port**: The program automatically fetches available serial ports and populates the port combobox.
3. **Select Firmware**: Click "Select Firmware File" to choose an `.ino` or `.cpp` file to upload.
4. **Upload**: Click "Upload" to start uploading the firmware to the connected board.
5. **Open Serial Monitor**: Open a new window to view real-time serial data from the board.

---

### **8. Error Handling:**
- **Board Info**: If no port is selected, an error message prompts the user to select a port.
- **Upload**: If no board or port is selected, an error message is shown.
- **Serial Monitor**: If no port is selected, the user is prompted to select a port before opening the monitor.

---

### **9. Dependencies:**

- `tkinter`: Used for GUI components.
- `serial`: Used for serial communication with the microcontroller.
- `subprocess`: Used to execute external commands like `arduino-cli` for fetching port information.
- `threading`: Allows background serial data reading without freezing the UI.

---

### **10. Conclusion:**

This firmware uploader tool provides a simple and interactive GUI for users to upload firmware to AVR-based microcontroller boards and monitor serial data. It integrates serial communication, file handling, and real-time data display, making it an efficient tool for embedded development.