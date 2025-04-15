# Folder-to-ZIP Converter

A simple Python script with a GUI that allows you to drag and drop folders and compress them into ZIP archives.

## Description

This script provides a user-friendly way to compress multiple folders into ZIP files.  You can drag and drop folders directly onto the application window, and then click a button to compress all the added folders.  The script uses the `zipfile` module for compression and `TkinterDnD2` for drag-and-drop functionality.

## Features

*   **Drag-and-Drop Support:**  Easily add folders to the list by dragging and dropping them onto the application window.
*   **Multiple Folder Compression:** Compress multiple folders at once.
*   **GUI Interface:**  Simple and intuitive graphical user interface built with `tkinter`.
*   **Error Handling:** Displays error messages if any issues occur during compression.
*   **Progress Indication:** Provides a message box to indicate when the compression is complete.

## Usage

1.  **Run the Script:** Execute the Python script `folder_to_zip.py` (or whatever you named it).
2.  **Drag and Drop Folders:** Drag and drop the folders you want to compress onto the listbox in the application window.
3.  **Compress All:** Click the "Compress All" button to compress all the folders in the list.
4.  **ZIP Files Created:** The ZIP files will be created in the same directory as the original folders, with the `.zip` extension appended to the folder name.

## Installation

1.  **Prerequisites:**  Make sure you have Python 3.6 or higher installed.
2.  **Install Dependencies:**
    ```bash
    pip install tkinter zipfile tkinterdnd2
    ```
    (You might need to use `pip3` instead of `pip` depending on your Python setup.)
3.  **Download the Script:** Download the `folder_to_zip.py` script (or whatever you named it).
4.  **Run the Application:**
    ```bash
    python folder_to_zip.py
    ```

## Dependencies

*   **tkinter:**  Standard Python GUI library (usually included with Python).
*   **zipfile:** Standard Python module for working with ZIP archives (usually included with Python).
*   **tkinterdnd2:**  A library that adds drag-and-drop functionality to Tkinter applications.  Install with `pip install tkinterdnd2`.

## Contributing

Contributions are welcome!  Here's how you can contribute:

1.  **Fork the Repository:** Create your own fork of the repository.
2.  **Create a Branch:** Create a new branch for your feature or bug fix.
3.  **Make Changes:** Implement your changes and commit them with descriptive messages.
4.  **Submit a Pull Request:** Submit a pull request to the main repository.

Please follow these guidelines when contributing:

*   Write clear and concise commit messages.
*   Test your changes thoroughly.
*   Follow the existing code style.

## License

This project is licensed under the MIT License.

## Acknowledgements

*   This project uses [tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
*   This project uses [zipfile](https://docs.python.org/3/library/zipfile.html) for ZIP archive creation.
*   This project uses [TkinterDnD2](https://github.com/Petasis/tkdnd) for drag-and-drop functionality.
