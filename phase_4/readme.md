```markdown
# Multi-Client Chat App with GUI and Color Support

A real-time multi-client chat system built in Python using `socket` for networking and `PyQt6` for the GUI. Each client joins with a username and a preferred message color. Messages are broadcast to all users in styled format, with support for private messages via `/pm`.

---

## 📸 Screenshots

> Replace with actual images in your `images/` folder

| Login & Setup | Chat Interface |
|---------------|----------------|
| ![Login](images/login.png) | ![Chat UI](images/chat_ui.png) |

---

## 🚀 Features

- User-defined nickname
- Color-coded messages (Black, Red, Green, Blue)
- Private messaging via `/pm <username> <message>`
- Real-time broadcasted messages
- GUI-based client (PyQt6)
- Threaded server for multiple clients
- Clean disconnect handling

---

## 🛠️ Technologies Used

- Python 3.x
- PyQt6
- socket (networking)
- threading (concurrency)
- datetime (timestamps)

---

## 📁 Folder Structure

```
chat-app/
│
├── server.py               # The server-side logic
├── client.py               # The GUI-based client application
├── images/                 # Folder for screenshots
│   ├── login.png
│   └── chat_ui.png
├── README.md               # Project documentation
```

---

## 🧪 Getting Started

### ✅ Prerequisites

Install PyQt6:
```bash
pip install PyQt6
```

### ▶️ Run Instructions

![Alt text](<phase_4 server-1.png>)

![Alt text](<phase_4 clients-1.png>)

1. **Start the Server:**
```bash
python server.py
```

2. **Start the Client:**

just open the client.exe

3. **Connect & Chat:**
   - Enter your **username** and select a **color**.
   - Start messaging with others.
   - To send a **private message**, use:  
     ```
     /pm username message
     ```
   - To leave the chat, use:
     ```
     /exit
     ```

---

## 🧩 Message Format (Protocol)

Messages between clients and server are exchanged using this pattern:

```
<username>|<color>|<message>
```

The client GUI parses this structure to format each message with proper color and display.

---

## 📌 To-Do (Ideas)

- [ ] Save chat history locally
- [ ] Dark mode theme toggle
- [ ] File sharing support
- [ ] Emoji and rich media support
- [ ] Online status indicators

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙌 Credits

Inspired by foundational socket programming projects and GUI application design using PyQt.
```