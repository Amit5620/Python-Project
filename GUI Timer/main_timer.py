import sys
from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar
from PyQt5.QtMultimedia import QSoundEffect

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Timer")
        self.setFixedSize(400, 200)

        # Create widgets
        self.hour_label = QLabel("Hours:")
        self.hour_edit = QLineEdit("00")
        self.minute_label = QLabel("Minutes:")
        self.minute_edit = QLineEdit("00")
        self.second_label = QLabel("Seconds:")
        self.second_edit = QLineEdit("00")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.end_button = QPushButton("End")
        self.timer_label = QLabel("00:00:00")
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)

        # Create layouts
        self.layout = QVBoxLayout()
        self.time_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()

        # Add widgets to layouts
        self.time_layout.addWidget(self.hour_label)
        self.time_layout.addWidget(self.hour_edit)
        self.time_layout.addWidget(self.minute_label)
        self.time_layout.addWidget(self.minute_edit)
        self.time_layout.addWidget(self.second_label)
        self.time_layout.addWidget(self.second_edit)
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.stop_button)
        self.layout.addLayout(self.time_layout)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.timer_label)

        # Set up timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        # Set up sound effect
        """ Optional play sound at the end of timer, uncommet both to use this, 
            but make sure you have timer_end.wav file in the same dir """
        #self.sound_effect = QSoundEffect()
        #self.sound_effect.setSource(QUrl.fromLocalFile("timer_end.wav"))

        # Connect signals and slots
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.end_button.clicked.connect(self.end_timer)
        self.stop_button.setEnabled(False)
        self.end_button.setEnabled(False)

        # Set window layout
        self.setLayout(self.layout)

    def start_timer(self):
        try:
            hours = int(self.hour_edit.text())
            minutes = int(self.minute_edit.text())
            seconds = int(self.second_edit.text())
        except ValueError:
            return
        if hours  != 0 or minutes != 0 or seconds != 0:
            self.timer.start()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.end_button.setEnabled(True)
            self.remaining_time = hours * 3600 + minutes * 60 + seconds
            self.progress_bar.setMaximum(self.remaining_time)
            self.progress_bar.setValue(0)
        else:
            return

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.end_button.setEnabled(True)
        self.remaining_time = 0
        self.timer_label.setText("00:00:00")
        self.progress_bar.setValue(0)

    def end_timer(self):
        self.sound_effect.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.end_button.setEnabled(False)

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.stop_timer()
            self.sound_effect.play()
            return
        hours = self.remaining_time // 3600
        minutes = (self.remaining_time % 3600) // 60
        seconds = self.remaining_time % 60
        self.timer_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
        self.progress_bar.setValue(self.progress_bar.maximum() - self.remaining_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer_widget = TimerWidget()
    timer_widget.show()
    sys.exit(app.exec_())