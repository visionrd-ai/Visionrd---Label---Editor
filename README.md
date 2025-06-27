# 🚀 Visionrd - Label Editor

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

### 📥 [Click to Download the Latest Version](https://github.com/visionrd-ai/Visionrd---Label---Editor/archive/refs/heads/main.zip)

[![Download](https://img.shields.io/badge/Download-ZIP-blue?style=for-the-badge&logo=github)](https://github.com/visionrd-ai/Visionrd---Label---Editor/archive/refs/heads/main.zip)

---

## 📌 Table of Contents

- [🔍 Overview](#-overview)
- [✨ Features](#-features)
- [⚙️ Prerequisites](#️-prerequisites)
- [📦 Installation](#-installation)
- [🚀 Getting Started](#-getting-started)
- [🧠 Usage](#-usage)
  - [📁 Loading Labels](#1-loading-labels)
  - [📂 Selecting Output Folder](#2-selecting-output-folder)
  - [✍️ Label Editing](#3-label-editing)
  - [🖼️ Image Controls](#4-image-controls)
  - [🔍 Search & Replace](#5-search--replace)
  - [↩️ Undo](#6-undo)
- [⌨️ Keyboard Shortcuts](#-keyboard-shortcuts)
- [📁 Application Structure](#-application-structure)
- [🚨 Error Handling](#-error-handling)
- [🎨 Customization](#-customization)
- [💾 Saving Labels](#-saving-labels)
- [🧰 Technologies Used](#-technologies-used)
- [🙏 Acknowledgements](#-acknowledgements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [💬 Support](#-support)

---

## 🔍 Overview

**Visionrd - Label Editor** is an intuitive and powerful GUI-based image label editor designed to streamline the process of visual data annotation. Built with PySide6, OpenCV, and PIL, it provides an efficient and user-friendly experience for annotating datasets with ease.

---

## ✨ Features

✅ Load and display images for labeling  
✅ Edit, update, and manage image labels  
✅ Zoom & grayscale view support  
✅ Live search and replace  
✅ Color picker for background customization  
✅ Auto-saving and undo support  
✅ Keyboard shortcuts for faster workflow

---

## ⚙️ Prerequisites

Ensure the following are installed:

- **Python**: `>=3.7`
- Required Python packages:
  ```bash
  pip install PySide6 opencv-python pillow numpy
  ```

---

## 📦 Installation

```bash
git clone https://github.com/visionrd-ai/Visionrd---Label---Editor.git
cd visionrd-label-editor
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, create it with:
> ```txt
> PySide6
> opencv-python
> pillow
> numpy
> ```

---

## 🚀 Getting Started

To launch the app, simply run:

```bash
python label_editor.py
```

Replace `label_editor.py` with your actual script name if different.

---

## 🧠 Usage

### 1. 📁 Loading Labels
Click **Load Labels** to select a `.txt` file (format: `image_path<TAB>label`).

### 2. 📂 Selecting Output Folder
Choose the output directory for storing updated annotations.

### 3. ✍️ Label Editing
Modify labels using the input field and press **Enter** or **Save**.

### 4. 🖼️ Image Controls
- Navigate: `←`/`→` or **Back**/**Next**
- Zoom: `↑`/`↓` or `+`/`-`
- Grayscale toggle & color picker available

### 5. 🔍 Search & Replace
Open the dialog, input terms, and apply across all labels.

### 6. ↩️ Undo
Press **Backspace** or click **Undo** to revert the last change.

---

## ⌨️ Keyboard Shortcuts

| Shortcut     | Action                        |
|--------------|-------------------------------|
| `→` Arrow     | Save and go to next image      |
| `←` Arrow     | Go back to previous image      |
| `↑` Arrow     | Zoom in                        |
| `↓` Arrow     | Zoom out                       |
| `Backspace`   | Undo last change               |
| `Delete`      | Delete current label           |
| `Enter`       | Save label and go to next image |

---

## 📁 Application Structure

```
visionrd-label-editor/
├── label_editor.py          # Main app file
├── visionrd_logo.png        # App icon (optional)
├── requirements.txt         # Dependencies
└── README.md                # You're here!
```

---

## 🚨 Error Handling

- ❌ Image load errors are displayed clearly
- ⚠️ Invalid actions produce warnings
- ⛔ Graceful fallback for missing inputs

---

## 🎨 Customization

- Modify `auto_save_interval` (ms)
- Adjust `zoom_factor`
- Use color picker to change background
- Extend features in `label_editor.py`

---

## 💾 Saving Labels

- Output file: `annotations_fix.txt`
- Make sure label file and output directory are selected

---

## 🧰 Technologies Used

| Technology | Purpose                     |
|------------|-----------------------------|
| PySide6    | GUI framework (Qt for Python) |
| OpenCV     | Image loading & manipulation |
| Pillow     | Image conversion              |
| NumPy      | Data handling                 |

---

## 🙏 Acknowledgements

Big thanks to these open-source projects:

- [PySide6](https://doc.qt.io/qtforpython/)
- [OpenCV](https://opencv.org/)
- [Pillow](https://python-pillow.org/)
- [NumPy](https://numpy.org/)

---

## 🤝 Contributing

1. Fork this repo  
2. Create a branch: `git checkout -b my-feature`  
3. Commit: `git commit -m "Add: feature"`  
4. Push: `git push origin my-feature`  
5. Submit a PR

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 💬 Support

- Found a bug? ➡️ [Open an issue](https://github.com/visionrd-ai/Visionrd---Label---Editor/issues)
- Need help fast? Reach out to the maintainer directly.
