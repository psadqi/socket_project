# Import necessary PyQt6 modules for GUI components
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, \
    QPushButton, QRadioButton, QTextEdit, QGridLayout, QMessageBox
from PyQt6.QtGui import QIcon, QIntValidator  # For icons and input validation
from PyQt6.QtCore import pyqtSignal, QObject  # For custom signals and QObject base class

# Import standard library modules
import socket  # For network communication
import threading  # For running network operations in separate threads
from datetime import datetime

# Create a TCP socket for client-server communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Communicate(QObject):
    """
    Custom communication class that inherits from QObject.
    This enables signal-slot communication between threads safely.
    """
    # Define a custom signal that carries a string payload
    message_received = pyqtSignal(str)


class ChatWindow(QMainWindow):
    """
    Main application window class that inherits from QMainWindow.
    Handles all GUI components and network communication.
    """

    def __init__(self):
        super().__init__()
        # Create communication object and connect its signal to display method
        self.comm = Communicate()
        self.comm.message_received.connect(self.display_message)

        # Configure main window properties
        self.setWindowTitle("Chat Application")  # Window title
        self.setWindowIcon(QIcon("icon.png"))  # Window icon (assuming icon.png exists)
        self.setFixedSize(550, 600)  # Fixed window size

        # Initialize all UI components
        self.init_ui()

    def init_ui(self):
        """Initialize and setup all UI components in proper order."""
        self.setup_main_window()  # Set up the main window structure
        self.create_connection_panel()  # Create connection settings panel
        self.create_chat_display()  # Create chat message display area
        self.create_message_input()  # Create message input area
        self.apply_styles()  # Apply CSS-like styling to components

    def setup_main_window(self):
        """Configure main window's central widget and main layout."""
        # Create central widget that holds all other widgets
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("centralWidget")  # Set object name for CSS styling
        self.setCentralWidget(self.central_widget)  # Set as central widget

        # Create main vertical layout for the central widget
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)  # Set margins
        self.main_layout.setSpacing(10)  # Set spacing between widgets

    def apply_styles(self):
        """
        Apply a modern stylesheet to the application using CSS-like syntax.
        This styles all widgets consistently throughout the application.
        """
        self.setStyleSheet("""
        /* Main window styling - sets default background and font */
        QWidget {
            background-color: #f5f5f5;
            font-family: 'Segoe UI', Arial, sans-serif;
        }

        /* Group boxes - gives them a clean bordered look */
        QGroupBox {
            background-color: #fffffff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            margin-top: 10px;
            padding-top: 15px;
            font-weight: bold;
            color: #333333;
        }

        /* Group box titles - positions them properly */
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px;
        }

        /* Labels - basic styling */
        QLabel {
            color: #555555;
            padding: 2px;
        }

        /* Input fields - styling for both line edits and text edits */
        QLineEdit, QTextEdit {
            border: 1px solid #ccccccc;
            border-radius: 4px;
            padding: 8px;
            background: white;
            selection-background-color: #4CAF50;
            selection-color: white;
        }

        /* Focus state for input fields */
        QLineEdit:focus, QTextEdit:focus {
            border: 1px solid #4CAF50;
        }

        /* Buttons - base styling */
        QPushButton {
            background-color: #df3131;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            min-width: 80px;
            font-weight: bold;
        }

        /* Button hover state */
        QPushButton:hover {
            background-color: #a81818;
        }

        /* Button pressed state */
        QPushButton:pressed {
            background-color: #3d8b40;
        }

        /* Disabled button state */
        QPushButton:disabled {
            background-color: #ccccccc;
            color: #888888;
        }

        /* Radio buttons - basic styling */
        QRadioButton {
            padding: 4px;
            spacing: 8px;
        }

        /* Radio button indicator (the actual radio circle) */
        QRadioButton::indicator {
            width: 16px;
            height: 16px;
        }

        /* Custom text colors for radio buttons using their object names */
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

        /* Vertical scroll bar styling */
        QScrollBar:vertical {
            width: 12px;
            background: #flflfl;
            margin: 0px;
        }

        QScrollBar::handle:vertical {
            background: #clclcl;
            min-height: 20px;
            border-radius: 6px;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }

        /* Horizontal scroll bar styling */
        QScrollBar:horizontal {
            height: 12px;
            background: #flflfl;
            margin: 0px;
        }

        QScrollBar::handle:horizontal {
            background: #clclcl;
            min-width: 20px;
            border-radius: 6px;
        }
        """)

    def create_connection_panel(self):
        """Create the connection settings panel with server, port, username inputs and action buttons."""
        # Create a group box to contain all connection-related widgets
        connection_group = QGroupBox("Connection Settings")
        connection_layout = QGridLayout()  # Use grid layout for precise widget placement

        # Server IP address input
        self.server_label = QLabel("Server IP:")
        self.server_input = QLineEdit()
        # Set default value to local IP address
        self.server_input.setText(f"{socket.gethostbyname(socket.gethostname())}")
        self.server_input.setPlaceholderText(f"{socket.gethostbyname(socket.gethostname())}")

        # Port number input
        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()
        self.port_input.setText("12345")  # Default port
        self.port_input.setPlaceholderText("12345")
        # Restrict input to valid port numbers (1-65535)
        self.port_input.setValidator(QIntValidator(1, 65535))

        # Username input
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        # Add widgets to the grid layout
        connection_layout.addWidget(self.server_label, 0, 0)
        connection_layout.addWidget(self.server_input, 0, 1)
        connection_layout.addWidget(self.port_label, 0, 2)
        connection_layout.addWidget(self.port_input, 0, 3)
        connection_layout.addWidget(self.username_label, 1, 0)
        connection_layout.addWidget(self.username_input, 1, 1, 1, 3)

        # Text color selection components
        self.text_color_label = QLabel("Text Color:")

        # Create radio buttons for color selection
        self.black_radio = QRadioButton("Black")
        self.black_radio.setObjectName("blackRadio")  # Set object name for CSS styling
        self.black_radio.setChecked(True)  # Set as default selection

        self.red_radio = QRadioButton("Red")
        self.red_radio.setObjectName("redRadio")

        self.green_radio = QRadioButton("Green")
        self.green_radio.setObjectName("greenRadio")

        self.blue_radio = QRadioButton("Blue")
        self.blue_radio.setObjectName("blueRadio")

        # Create horizontal layout for color selection widgets
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.text_color_label)
        color_layout.addWidget(self.black_radio)
        color_layout.addWidget(self.red_radio)
        color_layout.addWidget(self.green_radio)
        color_layout.addWidget(self.blue_radio)
        color_layout.addStretch()  # Add stretch to push widgets to the left

        # Create action buttons (Connect/Disconnect)
        self.connect_button = QPushButton("Connect")
        # Custom styling for connect button (green color)
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
            background-color: #ccccccc;
            color: #888888;
        }""")

        self.disconnect_button = QPushButton("Disconnect")
        # Custom styling for disconnect button (red color)
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

        # Connect button signals to their respective slots
        self.connect_button.clicked.connect(self.start_connection)
        self.disconnect_button.clicked.connect(self.disconnect_from_server)
        self.disconnect_button.setEnabled(False)  # Disabled by default

        # Create layout for action buttons (right-aligned)
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Add stretch to push buttons to the right
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)

        # Combine color selection and button layouts in a horizontal layout
        bottom_row_layout = QHBoxLayout()
        bottom_row_layout.addLayout(color_layout)
        bottom_row_layout.addLayout(button_layout)

        # Add the combined layout to the grid
        connection_layout.addLayout(bottom_row_layout, 2, 0, 1, 4)

        # Set the layout for the connection group and add to main layout
        connection_group.setLayout(connection_layout)
        self.main_layout.addWidget(connection_group)

    def create_chat_display(self):
        """Create the chat message display area with a read-only text edit."""
        chat_group = QGroupBox("Chat Messages")
        chat_layout = QVBoxLayout()

        # Create text edit for displaying chat messages
        self.chat_display = QTextEdit()
        # Custom styling for the chat display
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 8px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 18px;
            }
        """)
        self.chat_display.setReadOnly(True)  # Make it read-only

        # Add to layout and main window
        chat_layout.addWidget(self.chat_display)
        chat_group.setLayout(chat_layout)
        self.main_layout.addWidget(chat_group, 1)  # Add with stretch factor 1

    def create_message_input(self):
        """Create the message input area with a line edit and send button."""
        input_group = QGroupBox("Send Message")
        input_layout = QHBoxLayout()

        # Create message input field
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message here...")
        # Connect returnPressed signal to send message functionality
        self.message_input.returnPressed.connect(self.send_message)

        # Create send button
        self.send_button = QPushButton("Send")
        # Custom styling for send button (blue color)
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
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setEnabled(False)  # Disabled until connected

        # Add widgets to layout and main window
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)
        input_group.setLayout(input_layout)
        self.main_layout.addWidget(input_group)

    def start_connection(self):
        """Handle the connection process to the chat server."""
        # Get input values
        ip_address = self.server_input.text()
        port_number = self.port_input.text()
        username = self.username_input.text()

        # Validate inputs
        if (len(username) == 0 or len(ip_address) == 0 or len(port_number) == 0 or
                ip_address != socket.gethostbyname(socket.gethostname()) or port_number != "12345"):
            QMessageBox.warning(self, "Warning", "Please fill the fields correctly.")
            return

        try:
            port_number = int(port_number)
            # Attempt to connect to server
            client_socket.connect((ip_address, port_number))

            # Determine selected text color
            color = "black"  # Default
            if self.red_radio.isChecked():
                color = "red"
            elif self.green_radio.isChecked():
                color = "green"
            elif self.blue_radio.isChecked():
                color = "blue"

            # Disable color selection after connection
            self.black_radio.setEnabled(False)
            self.red_radio.setEnabled(False)
            self.green_radio.setEnabled(False)
            self.blue_radio.setEnabled(False)
            self.username_input.setEnabled(False)
            self.server_input.setEnabled(False)
            self.port_input.setEnabled(False)

            # Send username and color to server (separated by pipe)
            client_socket.send(f"{username}|{color}".encode('utf-8'))

            # Start a thread to receive messages from server
            receive_thread = threading.Thread(target=self.receive_message)
            receive_thread.daemon = True  # Daemonize thread so it exits with main program
            receive_thread.start()

            # Update UI state
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
            self.send_button.setEnabled(True)

        except Exception as e:
            # Show error message if connection fails
            QMessageBox.critical(self, "Error", f"Failed to connect: {str(e)}")

    def disconnect_from_server(self):
        """Handle disconnection from the chat server."""
        try:
            # Send exit command to server
            client_socket.send("/exit".encode('utf-8'))
            client_socket.close()  # Close socket
            self.chat_display.append("Disconnected from server")
        except:
            pass  # Ignore errors during disconnection
        finally:
            # Update UI state
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
            self.send_button.setEnabled(False)
            # Re-enable color selection
            self.black_radio.setEnabled(True)
            self.red_radio.setEnabled(True)
            self.green_radio.setEnabled(True)
            self.blue_radio.setEnabled(True)

    def send_message(self):
        """Send a message to the chat server."""
        message = self.message_input.text()
        if message:  # Only send non-empty messages
            try:
                # Send message to server
                client_socket.send(message.encode('utf-8'))
                self.message_input.clear()  # Clear input field
            except Exception as e:
                # If sending fails, disconnect
                self.disconnect_from_server()

    def receive_message(self):
        """
        Continuously receive messages from server in a separate thread.
        Emits signals to update the UI thread safely.
        """
        while True:
            try:
                # Receive message from server
                message = client_socket.recv(1024).decode('utf-8')
                if not message or message.lower() == "/exit":
                    break  # Exit loop if connection closed
                # Emit signal to update UI (thread-safe)
                self.comm.message_received.emit(message)
            except Exception as e:
                break  # Exit loop on error

        # Disconnect if loop exits
        self.disconnect_from_server()

    def display_message(self, message):
        self.chat_display.setAcceptRichText(True)

        # Handle private messages (format: "[PM from someone] Hello")
        if message.startswith("[PM from "):
            sender = message.split("]")[0][9:]
            msg = message.split("]")[1].strip()
            html = f'<span style="color:purple"><b>[Private from {sender}]:</b> {msg}</span> ({datetime.now().strftime("%H:%M")})'
            self.chat_display.append(html)
            return

        # Replace newlines with HTML line breaks (<br>)
        message = message.replace("\n", "<br>")

        if "|" in message:
            parts = message.split("|", 2)
            if len(parts) == 3:
                username, color, msg = parts
                html = f'<span style="color:{color}"><b>{username}:</b> {msg}</span> ({datetime.now().strftime("%H:%M")})'
                self.chat_display.append(html)
                return

        # Ensure plain text messages use HTML for proper line breaks
        self.chat_display.append(f"<pre>{message}</pre>")  # <pre> preserves formatting


# Create QApplication instance
app = QApplication([])
app.setStyle("fusion")  # Use Fusion style for consistent cross-platform look

# Create and show main window
window = ChatWindow()
window.show()

# Start event loop
app.exec()
