from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, \
    QPushButton, QRadioButton, QTextEdit, QGridLayout, QMessageBox
from PyQt6.QtGui import QIcon, QIntValidator

import socket
import sys
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_message():
    """receiving message from server"""
    while True:
        #we need a try except so that our program doesn't crash
        try:
            # receiving information from the server (buffer size is 1024)
            message = client_socket.recv(1024).decode("utf-8")
            return message
        #if there was an error
        except:
            client_socket.close()
            break


def send_message(message):
    """sending message to server"""
    while True:
        #getting the message and send it
        if message == "/exit":
            client_socket.close()
            break
        client_socket.send(message.encode("utf-8"))


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure main window properties
        self.setWindowTitle("Chat Application")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(650, 700)

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        """Initialize and setup all UI components."""
        self.setup_main_window()
        self.create_connection_panel()
        self.create_chat_display()
        self.create_message_input()
        self.apply_styles()

    def setup_main_window(self):
        """Configure main window properties."""
        # Central widget and main layout
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("centralWidget")
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

    def apply_styles(self):
        """Apply a modern stylesheet to the application."""
        self.setStyleSheet("""
            /* Main window styling */
            QWidget {
                background-color: #f5f5f5;
                font-family: 'Segoe UI', Arial, sans-serif;
            }

            /* Group boxes */
            QGroupBox {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                font-weight: bold;
                color: #333333;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }

            /* Labels */
            QLabel {
                color: #555555;
                padding: 2px;
            }

            /* Input fields */
            QLineEdit, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 8px;
                background: white;
                selection-background-color: #4CAF50;
                selection-color: white;
            }

            QLineEdit:focus, QTextEdit:focus {
                border: 1px solid #4CAF50;
            }

            /* Buttons */
            QPushButton {
                background-color: #df3131;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 80px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #a81818;
            }

            QPushButton:pressed {
                background-color: #3d8b40;
            }

            QPushButton:disabled {
                background-color: #cccccc;
                color: #888888;
            }

            /* Radio buttons */
            QRadioButton {
                padding: 4px;
                spacing: 8px;
            }

            QRadioButton::indicator {
                width: 16px;
                height: 16px;
            }

            /* Text color radio buttons */
            #blackRadio {
                color: #000000;
            }

            #redRadio {
                color: #ff0000;
            }

            #greenRadio {
                color: #00aa00;
            }

            #blueRadio {
                color: #0000ff;
            }

            /* Scroll bars */
            QScrollBar:vertical {
                width: 12px;
                background: #f1f1f1;
                margin: 0px;
            }

            QScrollBar::handle:vertical {
                background: #c1c1c1;
                min-height: 20px;
                border-radius: 6px;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar:horizontal {
                height: 12px;
                background: #f1f1f1;
                margin: 0px;
            }

            QScrollBar::handle:horizontal {
                background: #c1c1c1;
                min-width: 20px;
                border-radius: 6px;
            }
        """)

    def create_connection_panel(self):
        """Create the connection settings panel with right-aligned buttons."""
        connection_group = QGroupBox("Connection Settings")
        connection_layout = QGridLayout()

        # Server address
        self.server_label = QLabel("Server IP:")
        self.server_input = QLineEdit()
        self.server_input.setText(f"{socket.gethostbyname(socket.gethostname())}")
        self.server_input.setPlaceholderText(f"{socket.gethostbyname(socket.gethostname())}")

        # Port
        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()
        self.port_input.setText("12345")
        self.port_input.setPlaceholderText("12345")
        self.port_input.setValidator(QIntValidator(1, 65535))

        # Username
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        # Add widgets to layout
        connection_layout.addWidget(self.server_label, 0, 0)
        connection_layout.addWidget(self.server_input, 0, 1)
        connection_layout.addWidget(self.port_label, 0, 2)
        connection_layout.addWidget(self.port_input, 0, 3)
        connection_layout.addWidget(self.username_label, 1, 0)
        connection_layout.addWidget(self.username_input, 1, 1, 1, 3)

        # Text color radio buttons (left side)
        self.text_color_label = QLabel("Text Color:")

        self.black_radio = QRadioButton("Black")
        self.black_radio.setObjectName("blackRadio")
        self.black_radio.setChecked(True)

        self.red_radio = QRadioButton("Red")
        self.red_radio.setObjectName("redRadio")

        self.green_radio = QRadioButton("Green")
        self.green_radio.setObjectName("greenRadio")

        self.blue_radio = QRadioButton("Blue")
        self.blue_radio.setObjectName("blueRadio")

        # Color selection layout (left-aligned)
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.text_color_label)
        color_layout.addWidget(self.black_radio)
        color_layout.addWidget(self.red_radio)
        color_layout.addWidget(self.green_radio)
        color_layout.addWidget(self.blue_radio)
        color_layout.addStretch()  # Push everything to the left

        # Action buttons (right-aligned)
        self.connect_button = QPushButton("Connect")
        self.connect_button.setStyleSheet("""QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 80px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #0f972e;
            }

            QPushButton:pressed {
                background-color: #3d8b40;
            }

            QPushButton:disabled {
                background-color: #cccccc;
                color: #888888;
            }""")
        self.disconnect_button = QPushButton("Disconnect")
        self.disconnect_button.setStyleSheet("""QPushButton {
                background-color: #df3131;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 80px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #a81818;
            }

            QPushButton:pressed {
                background-color: #3d8b40;
            }

            QPushButton:disabled {
                background-color: #cccccc;
                color: #888888;
            }""")

        self.connect_button.clicked.connect(
            lambda: self.start_connection(self.server_input.text(), self.port_input.text(),self.username_input.text()))

        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Push buttons to the right
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)

        # Combine both layouts in a container
        bottom_row_layout = QHBoxLayout()
        bottom_row_layout.addLayout(color_layout)
        bottom_row_layout.addLayout(button_layout)

        connection_layout.addLayout(bottom_row_layout, 2, 0, 1, 4)

        connection_group.setLayout(connection_layout)
        self.main_layout.addWidget(connection_group)

    def create_chat_display(self):
        """Create the chat message display area."""
        chat_group = QGroupBox("Chat Messages")
        chat_layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 8px;
                font-family: 'Consolas', 'Courier New', monospace;
            }
        """)

        chat_layout.addWidget(self.chat_display)
        chat_group.setLayout(chat_layout)
        self.main_layout.addWidget(chat_group, 1)

    def create_message_input(self):
        """Create the message input area."""
        input_group = QGroupBox("Send Message")
        input_layout = QHBoxLayout()

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message here...")

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""QPushButton {
                background-color: #3ac1ec;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 80px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1d8eb2;
            }""")

        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)
        input_group.setLayout(input_layout)
        self.main_layout.addWidget(input_group)

    def start_connection(self, ip_address, port_number, username):
        # connecting to the server with specified ip address (your computer ip) and port number
        if len(username) == 0 or len(ip_address) == 0 or len(port_number) == 0:
            QMessageBox.warning(self, "Warning", "Please fill the fields.")
            return
        port_number = int(port_number)
        client_socket.connect((ip_address, port_number))
        if receive_message() == "username":
            send_message(username)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    window = ChatWindow()
    window.show()

    app.exec()