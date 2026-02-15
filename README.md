# taskTracker-CLI
Here’s a clean, complete **README.md** you can directly paste into your project 👇

---

# 📝 Task Tracker (CLI To-Do Manager)

A simple command-line Task Tracker built with Python that lets you add, view, update, and delete tasks.
Tasks are stored in a JSON file so your data persists between runs.

This project is designed as a beginner-friendly utility while demonstrating practical Python concepts like file handling, JSON manipulation, and command parsing.

---

# 🚀 Features

* Add new tasks with descriptions
* View all saved tasks
* Update existing tasks
* Delete tasks
* Persistent storage using JSON
* Simple command-line interface

---

# 🛠️ Tech Stack

* Python 3
* JSON (for storage)
* Command Line Interface (CLI)

---

# 📂 Project Structure

```
taskTracker/
│
├── taskTracker.py   # Main Python program
└── tasks.json       # Task storage file (auto-created)
```

---

# ▶️ How to Run

1. Install Python (3.x)
2. Download or clone this project
3. Open terminal in the project folder
4. Run:

```
python taskTracker.py
```

---

# 💻 Commands

Type commands in the terminal after running the program:

### Add a task

```
add study dsa
```

### View all tasks

```
view
```

### Update a task

```
update 1 study graphs
```

*(updates task with ID 1)*

### Delete a task

```
delete 1
```

### Exit program

```
exit
```

---

# 📁 Data Storage

Tasks are stored in `tasks.json`.

Example structure:

```json
[
  {"id": 1, "task": "study dsa"},
  {"id": 2, "task": "finish assignment"}
]
```

The file is automatically created when you first add a task — no manual setup required.

---

# 🎯 Learning Objectives

This project demonstrates:

* File handling in Python
* JSON read/write operations
* Command parsing
* CRUD operations
* Basic CLI application design

---

# 📌 Future Improvements

* Mark tasks as completed
* Due dates & priorities
* Search tasks
* GUI version

---

# 👨‍💻 Author

Ryan Cherian

---

If you'd like, I can also help you push this to GitHub or add screenshots 👍

