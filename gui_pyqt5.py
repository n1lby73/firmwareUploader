# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon, QFont

# class MainWindow(QMainWindow):

#     def __init__(self):

#         super().__init__()
#         self.setWindowTitle("Firmware uploader")
#         self.setGeometry(0,0,500,500) #x,y,width,height
#         self.setWindowIcon(QIcon("images/corsFavicon.png"))

# def main():

#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()

# Open the file in read mode
with open('gui_pyqt5.py', 'r') as file:
    content = file.read()

# Modify the content (e.g., replacing 'old' with 'new')
modified_content = content.replace('import', 'boy')

# Open the file in write mode and overwrite with modified content
with open('gui_pyqt5.py', 'w') as file:
    file.write(modified_content)
    print("done")