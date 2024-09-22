
# Visionrd - Label Editor

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [Loading Labels](#1-loading-labels)
  - [Selecting Output Folder](#2-selecting-output-folder)
  - [Label Editing](#3-label-editing)
  - [Image Controls](#4-image-controls)
  - [Search & Replace](#5-search--replace)
  - [Undo](#6-undo)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Application Structure](#application-structure)
- [Error Handling](#error-handling)
- [Customization](#customization)
- [Saving Labels](#saving-labels)
- [Technologies Used](#technologies-used)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview

**Visionrd - Label Editor** is a user-friendly, graphical label editing tool designed to simplify image labeling tasks. It allows you to load a set of images, apply or modify labels, and save your work efficiently. This tool is built using PySide6, OpenCV, and PIL for image processing and provides a variety of features to enhance the labeling process.

## Features

- Load and display images for labeling
- Edit, update, and manage image labels
- Zoom in/out functionality for images
- Grayscale image viewing
- Search and replace functionality for labels
- Background color customization using a color picker
- Keyboard shortcuts for efficient navigation
- Auto-saving at regular intervals
- Undo recent changes

## Prerequisites

Ensure you have the following installed:
- **Python**: Version 3.7 or later
- Python packages:
  - `PySide6`
  - `OpenCV` (`cv2`)
  - `Pillow` (`PIL`)
  - `NumPy`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/visionrd-ai/Visionrd---Label---Editor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd visionrd-label-editor
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` file if you don't have one with the following content)*
   ```
   PySide6
   opencv-python
   pillow
   numpy
   ```

## Getting Started

To start the application, run the following command:
```bash
python label_editor.py
```
Replace `label_editor.py` with your actual script's filename if different.

## Usage

### 1. Loading Labels
- Click on **"Load Labels"** and select a label file (e.g., `labels.txt`).
- The file should have each line formatted as: `image_path	label`.

### 2. Selecting Output Folder
- Click **"Select Output Folder"** and choose the folder where you want to save the edited labels.

### 3. Label Editing
- Enter or modify the label in the input field.
- Click **"Save"** or press `Enter` to save the label and proceed to the next image.

### 4. Image Controls
- Use **Next** and **Back** buttons to navigate through images or use arrow keys.
- Adjust zoom using the `+` or `-` buttons, or `Up`/`Down` arrow keys.
- Toggle grayscale mode using the **Grayscale** button.
- Change the background color using the **Pick Color** button.

### 5. Search & Replace
- Click **"Search & Replace"** to open the dialog.
- Enter the search term and the replacement term to update all matching labels.

### 6. Undo
- Click **"Undo"** or press `Backspace` to revert recent changes.

## Keyboard Shortcuts

| Shortcut        | Action                               |
|-----------------|--------------------------------------|
| `Right Arrow`   | Save and move to next image          |
| `Left Arrow`    | Move back to the previous image      |
| `Up Arrow`      | Zoom in                              |
| `Down Arrow`    | Zoom out                             |
| `Delete`        | Delete the current label             |
| `Backspace`     | Undo the last change                 |
| `Enter/Return`  | Save the label and move to the next image |

## Application Structure

The main files and folders in the project:
```
visionrd-label-editor/
│
├── label_editor.py        # Main application script
├── visionrd_logo.png      # Application icon (optional)
├── README.md              # Project documentation
└── requirements.txt       # Python package requirements
```

## Error Handling

- An error message is displayed if an image fails to load.
- Warning messages appear if invalid actions are attempted (e.g., entering an out-of-range index).

## Customization

You can modify certain aspects of the application:
- Adjust `auto_save_interval` (default is 5000 ms) to change the auto-save frequency.
- Change `zoom_factor` to modify the zooming behavior.
- Customize the background color using the color picker feature.

## Saving Labels

- Labels are saved to a file named `annotations_fix.txt` in the output folder you selected.
- Ensure you’ve loaded a label file and chosen an output folder before starting your editing.

## Technologies Used

- **PySide6**: For creating the GUI application
- **OpenCV**: For image loading and processing
- **Pillow (PIL)**: For image conversion
- **NumPy**: For efficient data handling

## Acknowledgements

- **PySide6**: Providing the Python bindings for the Qt toolkit
- **OpenCV**: Enabling advanced image processing capabilities
- **Pillow (PIL)**: Offering image manipulation functionalities

## Contributing

Contributions are welcome! If you have suggestions or improvements, please follow these steps:
1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have any questions, please open an issue on the GitHub repository or contact the project maintainer.
