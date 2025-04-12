from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon


class ChatWindowUI:
    """Modern chat application UI with text color options and right-aligned buttons."""

    def setup_ui(self, main_window):
        """Initialize and setup all UI components."""
        self.setup_main_window(main_window)
        self.set_icons(main_window)  # Add this line
        self.create_connection_panel()
        self.create_chat_display()
        self.create_message_input()
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def set_icons(self, main_window):
        """Set application and window icons."""
        # Set application icon (shown in taskbar/dock)
        app_icon = QtGui.QIcon("icon.png")  # Replace with your icon path
        QtWidgets.QApplication.setWindowIcon(app_icon)

        # Set window icon (shown in title bar)
        main_window.setWindowIcon(app_icon)

    def setup_main_window(self, main_window):
        """Configure main window properties."""
        main_window.setObjectName("ChatWindow")
        main_window.resize(800, 600)
        main_window.setWindowTitle("Chat Application")

        # Central widget and main layout
        self.central_widget = QtWidgets.QWidget(parent=main_window)
        self.central_widget.setObjectName("centralWidget")
        main_window.setCentralWidget(self.central_widget)

        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        # Apply modern styling
        self.set_stylesheet(main_window)

    def set_stylesheet(self, main_window):
        """Apply a modern stylesheet to the application."""
        main_window.setStyleSheet("""
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
        connection_group = QtWidgets.QGroupBox("Connection Settings")
        connection_layout = QtWidgets.QGridLayout()

        # Server address
        self.server_label = QtWidgets.QLabel("Server:")
        self.server_input = QtWidgets.QLineEdit()
        self.server_input.setPlaceholderText("Server IP")

        # Port
        self.port_label = QtWidgets.QLabel("Port:")
        self.port_input = QtWidgets.QLineEdit()
        self.port_input.setPlaceholderText("12345")
        self.port_input.setValidator(QtGui.QIntValidator(1, 65535))

        # Username
        self.username_label = QtWidgets.QLabel("Username:")
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        # Add widgets to layout
        connection_layout.addWidget(self.server_label, 0, 0)
        connection_layout.addWidget(self.server_input, 0, 1)
        connection_layout.addWidget(self.port_label, 0, 2)
        connection_layout.addWidget(self.port_input, 0, 3)
        connection_layout.addWidget(self.username_label, 1, 0)
        connection_layout.addWidget(self.username_input, 1, 1, 1, 3)

        # Text color radio buttons (left side)
        self.text_color_label = QtWidgets.QLabel("Text Color:")

        self.black_radio = QtWidgets.QRadioButton("Black")
        self.black_radio.setObjectName("blackRadio")
        self.black_radio.setChecked(True)

        self.red_radio = QtWidgets.QRadioButton("Red")
        self.red_radio.setObjectName("redRadio")

        self.green_radio = QtWidgets.QRadioButton("Green")
        self.green_radio.setObjectName("greenRadio")

        self.blue_radio = QtWidgets.QRadioButton("Blue")
        self.blue_radio.setObjectName("blueRadio")

        # Color selection layout (left-aligned)
        color_layout = QtWidgets.QHBoxLayout()
        color_layout.addWidget(self.text_color_label)
        color_layout.addWidget(self.black_radio)
        color_layout.addWidget(self.red_radio)
        color_layout.addWidget(self.green_radio)
        color_layout.addWidget(self.blue_radio)
        color_layout.addStretch()  # Push everything to the left

        # Action buttons (right-aligned)
        self.connect_button = QtWidgets.QPushButton("Connect")
        self.disconnect_button = QtWidgets.QPushButton("Disconnect")
        self.disconnect_button.setStyleSheet("""
            QPushButton {
                background-color: #df3131;
                color: white;
            }
            QPushButton:hover {
                background-color: #a81818;
            }
        """)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()  # Push buttons to the right
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)

        # Combine both layouts in a container
        bottom_row_layout = QtWidgets.QHBoxLayout()
        bottom_row_layout.addLayout(color_layout)
        bottom_row_layout.addLayout(button_layout)

        connection_layout.addLayout(bottom_row_layout, 2, 0, 1, 4)

        connection_group.setLayout(connection_layout)
        self.main_layout.addWidget(connection_group)

    def create_chat_display(self):
        """Create the chat message display area."""
        chat_group = QtWidgets.QGroupBox("Chat Messages")
        chat_layout = QtWidgets.QVBoxLayout()

        self.chat_display = QtWidgets.QTextEdit()
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
        input_group = QtWidgets.QGroupBox("Send Message")
        input_layout = QtWidgets.QHBoxLayout()

        self.message_input = QtWidgets.QLineEdit()
        self.message_input.setPlaceholderText("Type your message here...")

        self.send_button = QtWidgets.QPushButton("Send")
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

    def retranslate_ui(self, main_window):
        """Set text for UI elements (for translation purposes)."""
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("ChatWindow", "Chat room"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Set application-wide style
    app.setStyle("Fusion")

    # Create and show window
    window = QtWidgets.QMainWindow()
    ui = ChatWindowUI()
    ui.setup_ui(window)
    window.show()

    sys.exit(app.exec())