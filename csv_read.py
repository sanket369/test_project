import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QHeaderView

class CSVViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Dropdown menu for selecting CSV file
        self.file_dropdown = QComboBox(self)
        self.layout.addWidget(self.file_dropdown)

        # Table for displaying CSV data
        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.table_widget)

        # Load button
        self.load_button = QPushButton("Load CSV", self)
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

        # Set layout
        self.central_widget.setLayout(self.layout)

        # Populate dropdown with CSV files in the same folder
        self.populate_dropdown()

    def populate_dropdown(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        csv_files = [f for f in os.listdir(current_directory) if f.endswith(".csv")]

        self.file_dropdown.addItems(csv_files)

    def load_csv(self):
        selected_file = self.file_dropdown.currentText()

        if selected_file:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, selected_file)

            # Load CSV file into a DataFrame
            try:
                df = pd.read_csv(file_path)
            except Exception as e:
                print(f"Error loading CSV file: {e}")
                return

            # Display DataFrame in the table
            self.display_data(df)

    def display_data(self, data_frame):
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(len(data_frame.columns))

        self.table_widget.setHorizontalHeaderLabels(data_frame.columns)

        for row_index, row_data in data_frame.iterrows():
            self.table_widget.insertRow(row_index)

            for col_index, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row_index, col_index, item)

        # Set resize mode for headers
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        v_header = self.table_widget.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.ResizeToContents)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CSVViewer()
    viewer.show()
    sys.exit(app.exec_())
