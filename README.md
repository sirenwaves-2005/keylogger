# Keylogger (Educational Project)

## Overview

This project is an educational Python-based activity monitoring tool built to understand:

* Event-driven programming
* Keyboard and mouse listeners
* Logging systems
* Multithreading with listeners
* Timestamped activity tracking
* Python desktop input handling using `pynput`

The project captures:

* Keyboard key press/release events
* Mouse movement
* Mouse clicks
* Mouse scroll actions
* Real-time timestamps for all recorded events

The generated logs are written to a local text file for analysis and learning purposes.

> **Note:** This repository is intended strictly for educational, defensive security, and research purposes inside controlled environments.

---

# Features

* Real-time keyboard event monitoring
* Mouse movement tracking
* Mouse click detection
* Scroll event tracking
* Timestamped logging system
* Immediate disk flushing for live logs
* Graceful listener shutdown using `Ctrl + K`
* Separate keyboard and mouse listener threads

---

# Technologies Used

* Python 3
* `pynput`
* `datetime`

---

# Project Structure

```text
.
├── c1.py
├── activity_log.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```


## 2. Install Dependencies

```bash
pip install pynput
```

---

# Running the Project

```bash
python c1.py
```

When execution starts:

* Keyboard events are monitored
* Mouse events are monitored
* Logs are continuously written into:

```text
activity_log.txt
```

---

# Example Log Output

```text
[20:11:54.121] Session started. Press ctrl+k to stop
[20:11:55.412] Pointer moved to (921, 515)
[20:11:56.018] Key pressed h
[20:11:56.118] 'h' released
[20:11:58.552] Pressed at (1041, 602)
[20:11:58.720] Released at (1041, 602)
[20:12:01.130] Scrolled down at (1002, 540)
```

---

# How It Works

## Mouse Listener

The mouse listener captures:

* Cursor movement
* Click events
* Scroll events

Implemented using:

```python
mouse.Listener()
```

---

## Keyboard Listener

The keyboard listener captures:

* Key press events
* Key release events
* Special keys
* Alphanumeric keys

Implemented using:

```python
keyboard.Listener()
```

---

## Logging System

Each event is:

1. Timestamped
2. Printed to console
3. Written into a log file
4. Immediately flushed to disk

This ensures logs are preserved even if the application exits unexpectedly.

---

# Graceful Shutdown

The application can be stopped safely using:

```text
Ctrl + K
```

This:

* Stops keyboard listener
* Stops mouse listener
* Flushes pending logs
* Closes the log file cleanly

---

# Learning Objectives

This project was built to explore:

* System-level event monitoring
* Python callbacks
* Event listeners
* Input handling
* Concurrent listeners
* Logging architecture
* Desktop activity instrumentation

---

# Future Improvements

Currently thoughts are being put into it

---

# Security & Ethics

This repository is maintained strictly for:

* Educational purposes
* Security research
* Defensive experimentation
* Understanding system event handling

Do not deploy or use this software on systems, devices, or accounts without explicit authorization.

Unauthorized monitoring may violate:

* Privacy laws
* Institutional policies
* Computer misuse regulations

The author does not support malicious or unauthorized usage.

---

# Author Notes

This project was created as part of personal cybersecurity learning and experimentation with Python-based system monitoring concepts.

---

# License

This project is intended for private educational use.
