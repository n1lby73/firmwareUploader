import tkinter as tk
from tkinter import messagebox, filedialog, ttk #module needed for combobox
import serial.tools.list_ports
from uploader.avrUploader import uploadFirmwareAvr

class mainWindow(tk.Tk):

    def __init__(self):

        super().__init__()
        
        #Initialize the window

        self.title("Firmware Uploader")
        # self.iconbitmap('/images/corsFavicon.ico')
        self.geometry("500x500")

        self.boards = ["Select board", "Cortu gen1", "Cortu gen2", "Cortu gen3"]
        self.ports = ["Select Port"]
        self.selectedFirmwarePath = ""


        #Create list for board menu

        self.boardMenu = ttk.Combobox(self, values=self.boards)
        self.boardMenu.current(0)
        self.boardMenu.grid(row=0, column=0)
        self.boardMenu.bind("<<ComboboxSelected>>", self.boardSelected)

        #Combobox for selecting ports (initially hidden)

        self.selectPort = ttk.Combobox(self, values=self.ports)
        self.selectPort.grid(row=0, column=1)
        self.selectPort.grid_forget()
        self.selectPort.bind("<<ComboboxSelected>>", self.portSelected)

        # Label for displaying selected .ino file
        self.firmwareLabel = tk.Label(self, text="No file selected", width=40, anchor="w")
        self.firmwareLabel.grid(row=7, column=0, columnspan=2)

        # Button to select firmware (initially hidden)
        self.selectFirmware = tk.Button(self, text="Select .ino File", command=self.selectFile)
        self.selectFirmware.grid(row=7, column=4)
        self.selectFirmware.grid_forget()

        #Upload button

        button = tk.Button(self, text="Upload", command=self.upload)
        button.grid(row=1, column=1)

    def boardSelected(self, event):

        """Called when a board is selected from the dropdown."""
        if self.boardMenu.get() != self.boards[0]:

            self.selectPort.grid_forget()
            self.update_ports()

        else:

            self.selectPort.grid_forget()

    def portSelected(self, event):

        """Called when a board is selected from the dropdown."""
        if self.selectPort.get() != self.ports[0]:
            print ("hereeeeeeeeeeeee")
            self.selectFirmware.grid(row=7, column=4)
            # self.update_ports()

        else:

            self.selectPort.grid_forget()

    def update_ports(self):

        """Fetch available serial ports and update the combobox."""
        # This runs asynchronously, without blocking the main event loop
        self.after(100, self.fetch_ports)

    def fetch_ports(self):

        """Fetch available serial ports and update the combobox."""
        ports = serial.tools.list_ports.comports()

        for port in ports:
            self.ports.append(port.device)

        # Update the selectPort combobox with the new ports
        self.selectPort.config(values=self.ports)
        self.selectPort.current(0)
        self.selectPort.grid(row=0, column=1)
       
    def selectFile(self):
        """Open file dialog to select .ino file."""
        filePath = filedialog.askopenfilename(
            title="Select Arduino .ino File",
            filetypes=[("Arduino Files", "*.ino"), ("CPP Files","*.cpp")]
        )
        if filePath:
            self.selectedFirmwarePath = filePath
            self.firmwareLabel.config(text=f"Selected file: {self.selectedFirmwarePath}")

    def upload(self):

        #Validate selected board

        if self.boardMenu.get() not in self.boards:

            messagebox.showerror("Board Selector", "Unidentified board selected")

        if self.boardMenu.get() == self.boards[0]:

            messagebox.showerror("Board Selector", "No board selected")

        if self.selectPort.get() not in self.ports:

            messagebox.showerror("Port Selector", "Unidentified port selected")

        if self.selectPort.get() == self.ports[0]:

            messagebox.showerror("Port Selector", "No port selected")

        # After validating board, show the serial port combobox if not already shown

        if self.boardMenu.get() != self.boards[0]:

            if self.selectPort.winfo_ismapped() == False:

                self.selectPort.grid(row=0, column=2)
        
        if self.boardMenu.get() == self.boards[1] or self.boardMenu.get() == self.boards[2]:

            uploadFirmwareAvr(self.selectedFirmwarePath, self.selectPort.get(), self.boardMenu.get())

def main():

    window = mainWindow()
    window.mainloop()

if __name__ == "__main__":
    main()