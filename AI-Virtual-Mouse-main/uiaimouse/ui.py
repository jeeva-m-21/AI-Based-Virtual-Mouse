# ui.py
import sys
from PyQt6 import QtWidgets, QtCore
from settings import settings  # Import shared settings

class VirtualMouseUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AI Virtual Mouse Settings")
        self.setFixedSize(250, 220)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        # Enable/Disable AI Mouse Checkbox
        self.ai_mouse_checkbox = QtWidgets.QCheckBox("Enable AI Mouse")
        self.ai_mouse_checkbox.setChecked(settings.ai_mouse_enabled)
        self.ai_mouse_checkbox.setStyleSheet("color: white;")
        self.ai_mouse_checkbox.stateChanged.connect(self.toggle_ai_mouse)
        layout.addWidget(self.ai_mouse_checkbox)

        # Sensitivity Slider
        sensitivity_layout = QtWidgets.QHBoxLayout()
        sensitivity_label = QtWidgets.QLabel("Sensitivity")
        sensitivity_label.setStyleSheet("color: white;")
        self.sensitivity_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.sensitivity_slider.setMinimum(1)
        self.sensitivity_slider.setMaximum(10)
        self.sensitivity_slider.setValue(settings.sensitivity)
        self.sensitivity_slider.setStyleSheet("color: white;")
        self.sensitivity_slider.valueChanged.connect(self.set_sensitivity)
        sensitivity_layout.addWidget(sensitivity_label)
        sensitivity_layout.addWidget(self.sensitivity_slider)
        layout.addLayout(sensitivity_layout)

        self.setLayout(layout)

    def toggle_ai_mouse(self):
        settings.toggle_ai_mouse()  # Toggle AI mouse state

    def set_sensitivity(self):
        settings.set_sensitivity(self.sensitivity_slider.value())  # Update sensitivity

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VirtualMouseUI()
    window.show()
    sys.exit(app.exec())
