# ASCII Cam 🎥➡️🔤

A Python program that converts your **live webcam feed into real-time ASCII art** directly in the terminal.

This project captures frames from your camera, processes them using OpenCV, and maps pixel brightness to ASCII characters to create a live text-based video feed.

---

## Demo

Run the program and you’ll see your camera feed transformed into moving ASCII characters in real time.

---

## Requirements

All required Python dependencies are listed in `requirements.txt`.

Install them using:

```bash
pip install -r requirements.txt
```

---

## How to Run

Simply open `runner.bat`.  

Press `q` in the camera window to exit.

---

## How It Works (Brief)

1. Captures frames from the webcam
2. Converts each frame to grayscale
3. Resizes the frame for terminal rendering
4. Maps pixel brightness to ASCII characters
5. Continuously updates the terminal output

---

## Notes

* Performance depends on terminal size and camera resolution
* Works best in terminals that support fast text refresh
* Webcam access permission is required
