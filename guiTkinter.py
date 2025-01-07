import tkinter as tk
from tkinter import messagebox, ttk #module needed for combobox
import serial.tools.list_ports
from uploader.avrUploader import upload_firmware_avr

class mainWindow(tk.Tk):

    def __init__(self):

        super().__init__()
        
        #Initialize the window

        self.title("Firmware Uploader")
        # self.iconbitmap('/images/corsFavicon.ico')
        self.geometry("500x500")

        self.boards = ["Select board", "Cortu gen1", "Cortu gen2", "Cortu gen3"]
        self.ports = ["Select Port"]


        #Create list for board menu

        self.boardMenu = ttk.Combobox(self, values=self.boards)
        self.boardMenu.current(0)
        self.boardMenu.grid(row=0, column=0)
        self.boardMenu.bind("<<ComboboxSelected>>", self.on_board_selected)

        #Combobox for selecting ports (initially hidden)

        self.selectPort = ttk.Combobox(self, values=self.ports)
        self.selectPort.grid(row=0, column=1)
        self.selectPort.grid_forget()

        #Upload button

        button = tk.Button(self, text="Upload", command=self.upload)
        button.grid(row=1, column=1)

    def on_board_selected(self, event):

        """Called when a board is selected from the dropdown."""
        if self.boardMenu.get() != self.boards[0]:

            self.selectPort.grid_forget()
            self.update_ports()

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
        
        if self.boardMenu.get() == self.boards[1]:

            upload_firmware_avr("arduino/blink/blink.ino", self.selectPort.get(), "m328p")


def main():

    window = mainWindow()
    window.mainloop()

if __name__ == "__main__":
    main()