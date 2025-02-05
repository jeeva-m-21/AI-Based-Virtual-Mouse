# settings.py

class MouseSettings:
    def __init__(self):
        self.ai_mouse_enabled = True
        self.sensitivity = 7
        self.custom_shortcut_1 = "notepad.exe"
        self.custom_shortcut_2 = "calc.exe"

    def toggle_ai_mouse(self):
        self.ai_mouse_enabled = not self.ai_mouse_enabled

    def set_sensitivity(self, sensitivity):
        self.sensitivity = sensitivity

settings = MouseSettings()
