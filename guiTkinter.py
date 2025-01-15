import subprocess
import tkinter as tk
from tkinter import Menu, messagebox, filedialog, ttk  # module needed for combobox
import serial.tools.list_ports
from uploader.avrUploader import uploadFirmwareAvr

class mainWindow(tk.Tk):

    def __init__(self):

        super().__init__()

        # Initialize the window
        self.title("Firmware Uploader")
        self.geometry("600x400")  # Increased size for more space
        # self.resizable(False, False)  # Make window non-resizable for consistency

        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)

        toolsMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="Tools", menu=toolsMenu)
        toolsMenu.add_command(label="Get Board Info", command=self.boardInfo)
        

        self.boards = ["Select board", "Cortu gen1", "Cortu gen2", "Cortu gen3"]
        self.ports = ["Select Port"]
        self.selectedFirmwarePath = ""

        # Create list for board menu
        self.boardMenu = ttk.Combobox(self, values=self.boards, width=20, state="readonly")
        self.boardMenu.current(0)
        self.boardMenu.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        self.boardMenu.bind("<<ComboboxSelected>>", self.boardSelected)

        # Label for Board selection
        self.boardLabel = tk.Label(self, text="Select Board:", width=20, anchor="w")
        self.boardLabel.grid(row=0, column=0, padx=20, pady=10, sticky="e")

        # Combobox for selecting ports (initially hidden)
        self.selectPort = ttk.Combobox(self, values=self.ports, width=20, state="readonly")
        self.selectPort.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        self.selectPort.grid_forget()
        self.selectPort.bind("<<ComboboxSelected>>", self.portSelected)

        # Label for Port selection
        self.portLabel = tk.Label(self, text="Select Port:", width=20, anchor="w")
        self.portLabel.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        # Label for displaying selected firmware file
        self.firmwareLabel = tk.Label(self, text="No File Selected", width=40, anchor="w")
        self.firmwareLabel.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="w")

        # Button to select firmware (initially hidden)
        self.selectFirmware = tk.Button(self, text="Select Firmware File", command=self.selectFile, width=20)
        self.selectFirmware.grid(row=2, column=2, padx=20, pady=10, sticky="w")
        self.selectFirmware.grid_forget()

        # Upload button
        self.uploadButton = tk.Button(self, text="Upload", command=self.upload, width=20)
        self.uploadButton.grid(row=3, column=1, padx=20, pady=20)

    def boardSelected(self, event):
        """Called when a board is selected from the dropdown."""
        if self.boardMenu.get() != self.boards[0]:
            self.selectPort.grid_forget()
            self.update_ports()
        else:
            self.selectPort.grid_forget()

    def portSelected(self, event):
        """Called when a port is selected from the dropdown."""
        if self.selectPort.get() != self.ports[0]:
            self.selectFirmware.grid(row=2, column=2, padx=20, pady=10, sticky="w")
        else:
            self.selectFirmware.grid_forget()

    def update_ports(self):
        """Fetch available serial ports and update the combobox."""
        self.after(100, self.fetch_ports)

    def fetch_ports(self):
        """Fetch available serial ports and update the combobox."""
        retrievePort = subprocess.run(['arduino-cli', 'board', 'list'], capture_output=True, text=True)

        retrievedPortData = retrievePort.stdout.strip().splitlines()[1::]

        for line in retrievedPortData:

            columns = line.split()
            port = columns[0]

            self.ports.append(port)


        # Update the selectPort combobox with the new ports
        self.selectPort.config(values=self.ports)
        self.selectPort.current(0)
        self.selectPort.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    def selectFile(self):
        """Open file dialog to select .ino file."""
        filePath = filedialog.askopenfilename(
            title="Select Arduino .ino File",
            filetypes=[("Arduino Files", "*.ino"), ("CPP Files", "*.cpp")]
        )
        if filePath:
            self.selectedFirmwarePath = filePath
            self.firmwareLabel.config(text=f"Selected file: {self.selectedFirmwarePath}")

    def boardInfo(self):
        """Retrieve board info"""
        # Validate that port and board has been selected
        if self.boardMenu.get() == self.boards[0]:
            messagebox.showerror("Board Info", "Please Select board to retrieve board info")
            return

        if self.selectPort.get() == self.ports[0]:
            messagebox.showerror("Board Info", "Please select port to retrieve board info")
            return

        #Retrieve board info
        if self.boardMenu.get() == self.boards[1]:
            result = subprocess.run(['arduino-cli', 'board', 'details', '-b', 'arduino:avr:uno'], 
                            capture_output=True, text=True)
        
        # Print the output of the command
        if result.returncode == 0:
            print("Board details retrieved successfully:")
            print(result.stdout)
        else:
            print("Error retrieving board details:")
            print(result.stderr)

#  or self.boardMenu.get() == self.boards[2]:
#             uploadFirmwareAvr(self.selectedFirmwarePath, self.selectPort.get(), self.boardMenu.get())

    def upload(self):
        """Upload firmware to the selected board and port."""
        # Validate selected board
        if self.boardMenu.get() == self.boards[0]:
            messagebox.showerror("Board Selector", "No board selected")
            return

        if self.selectPort.get() == self.ports[0]:
            messagebox.showerror("Port Selector", "No port selected")
            return

        # Perform the upload action
        if self.boardMenu.get() == self.boards[1] or self.boardMenu.get() == self.boards[2]:
            uploadFirmwareAvr(self.selectedFirmwarePath, self.selectPort.get(), self.boardMenu.get())

        if self.boardMenu.get() == self.boards[3]:
            uploadFirmwareAvr(self.selectedFirmwarePath, self.selectPort.get(), self.boardMenu.get())

def main():
    window = mainWindow()
    window.mainloop()

if __name__ == "__main__":
    main()