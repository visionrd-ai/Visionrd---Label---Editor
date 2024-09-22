from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, 
                               QHBoxLayout, QFormLayout, QDialog, QColorDialog, QCompleter, QFileDialog)
from PySide6.QtGui import QPixmap, QImage, QIcon, QKeySequence, QColor
from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtGui import QShortcut
import cv2
from PIL import Image
import numpy as np
import os

class ImageLoader(QThread):
    image_loaded = Signal(QPixmap)
    error_occurred = Signal(str)
    
    def __init__(self, image_path, zoom_factor=1.0, grayscale=False):
        super().__init__()
        self.image_path = image_path
        self.zoom_factor = zoom_factor
        self.grayscale = grayscale
    
    def resize_proper(self, height, width, target_height=736, target_width=1280):
        aspect_ratio = width / height
        if height > target_height or width > target_width:
            if (target_width / width) < (target_height / height):
                new_width = target_width
                new_height = int(target_width / aspect_ratio)
            else:
                new_height = target_height
                new_width = int(target_height * aspect_ratio)
        else:
            new_width, new_height = width, height
        return new_height, new_width
    
    def run(self):
        try:
            image = cv2.imread(self.image_path)
            if image is None:
                raise Exception(f"Could not load image {self.image_path}")
            
            if self.grayscale:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            new_h, new_w = self.resize_proper(image.shape[0], image.shape[1], 720, 1280)
            new_w = int(new_w * self.zoom_factor)
            new_h = int(new_h * self.zoom_factor)
            image = cv2.resize(image, (new_w, new_h))
            
            if self.grayscale:
                q_image = QImage(image.data, image.shape[1], image.shape[0], image.shape[1], QImage.Format_Grayscale8)
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(image)
                q_image = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.width * 3, QImage.Format_RGB888)
            
            q_pixmap = QPixmap.fromImage(q_image)
            self.image_loaded.emit(q_pixmap)
        except Exception as e:
            self.error_occurred.emit(str(e))

class LabelEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.label_file = None
        self.output_folder = None
        self.output_file = None
        self.labels = []
        self.index = 0
        self.updated_labels = []
        self.history = []
        self.auto_save_interval = 5000
        self.zoom_factor = 1.0
        self.grayscale = False

        self.image_label = QLabel(self)
        self.label_entry = QLineEdit(self)
        self.label_entry.setPlaceholderText("Enter label...")

        self.next_button = QPushButton('Next', self)
        self.back_button = QPushButton('Back', self)
        self.delete_button = QPushButton('Delete', self)
        self.save_button = QPushButton('Save', self)
        self.undo_button = QPushButton('Undo', self)
        self.counter_label = QLabel(self)

        self.zoom_in_button = QPushButton('+', self)
        self.zoom_out_button = QPushButton('-', self)
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        self.color_picker_button = QPushButton('Pick Color', self)
        self.color_picker_button.clicked.connect(self.pick_color)

        self.search_replace_button = QPushButton('Search & Replace', self)
        self.search_replace_button.clicked.connect(self.open_search_replace_dialog)

        self.grayscale_button = QPushButton('Grayscale', self)
        self.grayscale_button.setCheckable(True)
        self.grayscale_button.clicked.connect(self.toggle_grayscale)

        self.index_entry = QLineEdit(self)
        self.index_entry.setPlaceholderText("Enter index...")
        self.goto_button = QPushButton('Go To', self)
        self.goto_button.clicked.connect(self.go_to_index)

        self.load_file_button = QPushButton('Load Labels', self)
        self.load_file_button.clicked.connect(self.load_label_file)

        self.select_output_folder_button = QPushButton('Select Output Folder', self)
        self.select_output_folder_button.clicked.connect(self.select_output_folder)

        self.set_layout()
        self.set_window_properties()

    def set_layout(self):
        completer = QCompleter([label for _, label in self.labels])
        self.label_entry.setCompleter(completer)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.undo_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.next_button)
        button_layout.addWidget(self.zoom_in_button)
        button_layout.addWidget(self.zoom_out_button)
        button_layout.addWidget(self.color_picker_button)
        button_layout.addWidget(self.search_replace_button)
        button_layout.addWidget(self.grayscale_button)
        button_layout.addWidget(self.index_entry)
        button_layout.addWidget(self.goto_button)
        button_layout.addWidget(self.select_output_folder_button)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.label_entry)
        layout.addWidget(self.counter_label)
        layout.addLayout(button_layout)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_file_button)

        self.setLayout(layout)

    def set_window_properties(self):
        self.setMinimumSize(640, 360)
        self.setMaximumSize(1280, 720)
        self.auto_save_timer = QTimer(self)
        self.auto_save_timer.timeout.connect(self.auto_save)
        self.auto_save_timer.start(self.auto_save_interval)

        self.shortcut_next = QShortcut(QKeySequence("Right"), self)
        self.shortcut_next.activated.connect(self.save_and_next)

        self.shortcut_back = QShortcut(QKeySequence("Left"), self)
        self.shortcut_back.activated.connect(self.go_back)

        self.shortcut_zoom_in = QShortcut(QKeySequence("Up"), self)
        self.shortcut_zoom_in.activated.connect(self.zoom_in)

        self.shortcut_zoom_out = QShortcut(QKeySequence("Down"), self)
        self.shortcut_zoom_out.activated.connect(self.zoom_out)

        self.shortcut_delete = QShortcut(QKeySequence("Delete"), self)
        self.shortcut_delete.activated.connect(self.delete_current_label)

        self.shortcut_undo = QShortcut(QKeySequence("Backspace"), self)
        self.shortcut_undo.activated.connect(self.undo)

        self.shortcut_save = QShortcut(QKeySequence("Return"), self)
        self.shortcut_save.activated.connect(self.save_and_next)

    def load_label_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.label_file = selected_files[0]
                if self.output_folder:
                    self.output_file = os.path.join(self.output_folder, 'annotations_fix.txt')
                    self.labels = self.load_labels()
                    self.update_image_and_label()
                else:
                    QMessageBox.warning(self, "Warning", "Please select an output folder.")

    def select_output_folder(self):
        folder_dialog = QFileDialog(self)
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly)

        if folder_dialog.exec():
            selected_folders = folder_dialog.selectedFiles()
            if selected_folders:
                self.output_folder = selected_folders[0]
                if self.label_file:
                    self.output_file = os.path.join(self.output_folder, 'annotations_fix.txt')
                    self.update_image_and_label()
                else:
                    QMessageBox.warning(self, "Warning", "Please load a label file.")

    def load_labels(self):
        with open(self.label_file, 'r') as file:
            lines = file.readlines()
        
        labels = []
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                labels.append(tuple(parts))
            else:
                print(f"Invalid line: {line.strip()}")
        return labels

    def save_labels(self):
        if self.output_file:
            with open(self.output_file, 'w') as file:
                for image_path, label in self.updated_labels:
                    file.write(f"{image_path}\t{label}\n")

    def update_image_and_label(self):
        if self.index >= len(self.labels):
            self.save_labels()
            QMessageBox.information(self, "Finished", "All labels are updated.")
            QApplication.quit()
            return

        image_path, label = self.labels[self.index]
        self.load_image(image_path)
        self.label_entry.setText(label)
        self.update_counter()

    def load_image(self, image_path):
        self.image_loader = ImageLoader(image_path, self.zoom_factor, self.grayscale)
        self.image_loader.image_loaded.connect(self.on_image_loaded)
        self.image_loader.error_occurred.connect(self.on_image_load_error)
        self.image_loader.start()

    def on_image_loaded(self, q_image):
        self.image_label.setPixmap(q_image)
        self.image_label.setAlignment(Qt.AlignCenter)

    def zoom_in(self):
        self.zoom_factor += 0.1
        self.update_image_and_label()

    def zoom_out(self):
        self.zoom_factor = max(0.1, self.zoom_factor - 0.1)
        self.update_image_and_label()

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()}")

    def update_counter(self):
        total = len(self.labels)
        remaining = total - self.index
        self.counter_label.setText(f"Total: {total}, Remaining: {remaining}")

    def save_and_next(self):
        new_label = self.label_entry.text().strip()
        image_path, _ = self.labels[self.index]
        self.updated_labels.append((image_path, new_label))
        self.index += 1
        self.update_image_and_label()

    def go_back(self):
        if self.index > 0:
            self.index -= 1
            self.update_image_and_label()

    def go_to_index(self):
        try:
            index = int(self.index_entry.text().strip())
            if 0 <= index < len(self.labels):
                self.index = index
                self.update_image_and_label()
            else:
                QMessageBox.warning(self, "Warning", "Index out of range.")
        except ValueError:
            QMessageBox.warning(self, "Warning", "Invalid index. Please enter a valid number.")

    def undo(self):
        if self.history:
            last_action = self.history.pop()
            self.index, self.updated_labels = last_action
            self.update_image_and_label()

    def delete_current_label(self):
        if 0 <= self.index < len(self.labels):
            if 0 <= self.index < len(self.updated_labels):
                del self.updated_labels[self.index]

            self.labels.pop(self.index)

            if not self.labels:
                QMessageBox.information(self, "Finished", "No more labels to display.")
                QApplication.quit()
                return

            if self.index >= len(self.labels):
                self.index = len(self.labels) - 1

            self.update_image_and_label()
        else:
            QMessageBox.warning(self, "Warning", "Invalid index for deletion.")

    def open_search_replace_dialog(self):
        dialog = SearchReplaceDialog(self)
        if dialog.exec():
            search_term = dialog.search_term
            replace_term = dialog.replace_term
            if search_term and replace_term:
                self.perform_search_replace(search_term, replace_term)

    def perform_search_replace(self, search_term, replace_term):
        self.history.append((self.index, list(self.updated_labels)))
        replacement_count = 0
        for i in range(len(self.labels)):
            image_path, label = self.labels[i]
            if search_term in label:
                new_label = label.replace(search_term, replace_term)
                self.labels[i] = (image_path, new_label)
                replacement_count += 1
        self.update_image_and_label()  
        QMessageBox.information(self, "Search & Replace", f"Replaced {replacement_count} instances of '{search_term}' with '{replace_term}'.")

    def auto_save(self):
        self.save_labels()
        
    def on_image_load_error(self, error_message):
        QMessageBox.critical(self, "Error", f"Failed to load image: {error_message}")
        
    def toggle_grayscale(self):
        self.grayscale = self.grayscale_button.isChecked()
        self.update_image_and_label()

class SearchReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search & Replace")

        self.search_term = ""
        self.replace_term = ""

        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search term")

        self.replace_input = QLineEdit(self)
        self.replace_input.setPlaceholderText("Replace with")

        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.accept)

        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.reject)

        layout = QFormLayout()
        layout.addRow("Search:", self.search_input)
        layout.addRow("Replace:", self.replace_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addRow(button_layout)

        self.setLayout(layout)

    def accept(self):
        self.search_term = self.search_input.text().strip()
        self.replace_term = self.replace_input.text().strip()
        super().accept()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = LabelEditor()
    window.setWindowTitle("Visionrd - Label Editor")
    window.setWindowIcon(QIcon("visionrd_logo.png"))  
    window.show()

    sys.exit(app.exec())
