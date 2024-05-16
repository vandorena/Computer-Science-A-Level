import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)
import numpy as np

class DiagramWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Define sizes and angles
        bar_width = 200
        bar_height = 20
        theta = 36.9 / 180 * np.pi  # Convert to radians
        phi = 53.1 / 180 * np.pi

        # Create labels
        mass_label = QLabel("m")
        t1_label = QLabel("T_1")
        t2_label = QLabel("T_2")
        theta_label = QLabel(f"$\\theta$")
        phi_label = QLabel(f"$\\phi$")
        x_label = QLabel("$x$")

        # Layout for bar and labels
        bar_layout = QHBoxLayout()
        bar_layout.addWidget(mass_label, alignment=Qt.AlignCenter)
        bar_layout.addWidget(QLabel(" "), stretch=1)
        bar_layout.addWidget(x_label, alignment=Qt.AlignRight)

        # Layout for entire widget
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel(" "))  # Add some space
        main_layout.addLayout(bar_layout)

        # Create lines for bar, ropes, and right angles
        bar_line = self.addLine(0, bar_height / 2, bar_width, bar_height / 2)
        rope1_line = self.addLine(
            0, bar_height / 2, bar_width * np.cos(theta), bar_height / 2 - bar_height * np.sin(theta)
        )
        rope2_line = self.addLine(
            bar_width, bar_height / 2, bar_width - bar_width * np.cos(phi), bar_height / 2 + bar_height * np.sin(phi)
        )
        right_angle1 = self.addRightAngle(bar_width, bar_height / 2, 0, bar_height / 2 - bar_height * np.sin(theta))
        right_angle2 = self.addRightAngle(0, bar_height / 2, bar_width, bar_height / 2 + bar_height * np.sin(phi))

        # Add labels to the layout
        main_layout.addWidget(t1_label, Qt.AlignLeft | Qt.AlignTop, Qt.NoFocus)
        main_layout.addWidget(t2_label, Qt.AlignRight | Qt.AlignTop, Qt.NoFocus)
        main_layout.addWidget(theta_label, Qt.AlignCenter, Qt.NoFocus)
        main_layout.addWidget(phi_label, Qt.AlignCenter, Qt.NoFocus)

        # Set layout and window properties
        self.setLayout(main_layout)
        self.setFixedSize(bar_width + 40, 150)  # Adjust size as needed
        self.setWindowTitle("Non-uniform Bar Diagram")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DiagramWidget()
    sys.exit(app.exec())
