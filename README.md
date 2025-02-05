# AI Virtual Mouse

This project implements an AI-powered virtual mouse that uses hand gestures to control the computer's mouse pointer, perform clicks, scrolling, and zooming. It also provides a settings interface where users can customize the mouse behavior, such as enabling/disabling the AI mouse, adjusting sensitivity, and more.

## Features

- **AI Mouse Control**: Control the mouse with hand gestures.
  - **Left Click & Drag**: Pinch the thumb and index finger.
  - **Right Click**: Pinch the index and middle fingers.
  - **Cursor Movement**: Move the cursor using the index finger.
  - **Scrolling**: Use three fingers to scroll.
  - **Zooming**: Use the thumb and index finger distance with the pinky finger up.
- **Settings Window**: Customize the behavior of the AI mouse using a GUI.
  - **Enable/Disable AI Mouse**: Toggle the AI mouse functionality.
  - **Sensitivity Slider**: Adjust the sensitivity of the mouse control.
  - **Run on Startup**: Option to run the AI mouse on system startup.
- **Keyboard Shortcut**: Trigger the settings window using `Ctrl+Alt+S`.

## Requirements

The following libraries are required to run the project. You can install them using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Required Libraries:
- **PyQt6**: For building the settings GUI.
- **OpenCV**: For hand detection and webcam integration.
- **Numpy**: For mathematical calculations, such as distances.
- **Keyboard**: For listening to keyboard shortcuts.
- **PyAutoGUI**: For simulating mouse and keyboard actions.
- **PyCaw**: For controlling system volume.
- **Autopy**: For controlling the mouse and simulating clicks.

## Installation

1. Clone or download the repository:
    ```bash
    git clone https://github.com/yourusername/ai-virtual-mouse.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ai-virtual-mouse
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the program:
    ```bash
    python main.py
    ```

5. **Settings Window**: To open the settings window, press the keyboard shortcut `Ctrl + Alt + S`.

## Usage

- Once the program is running, the AI mouse will start detecting your hand gestures using the webcam.
- Use the gestures to control the mouse:
  - **Left-click and drag**: Pinch the thumb and index finger.
  - **Right-click**: Pinch the index and middle fingers.
  - **Cursor movement**: Move the index finger.
  - **Scrolling**: Use three fingers.
  - **Zoom**: Use the thumb and index finger for zooming in and out (with pinky finger up).
- Press `Ctrl + Alt + S` to open the settings window where you can:
  - Toggle the AI mouse on or off.
  - Adjust sensitivity.
  - Set preferences for startup.

## Contributing

Feel free to fork the repository and submit pull requests. Any contributions are welcome!

## License

This project is open-source and available under the MIT License.

---

### Usage:
1. **Settings Window**: Open the settings by pressing `Ctrl + Alt + S`. This will launch the GUI to configure the AI Mouse behavior.
2. **AI Mouse Control**: After launching the program, the AI mouse will be active. Hand gestures are detected to control mouse movement, clicks, scrolling, and zooming.

---
