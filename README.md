# 📁 File Read & Write Challenge – Python Project

## 📝 Description

This Python program reads the content of a file, modifies it by adding line numbers to each line, and writes the modified content into a new file. It also includes error handling to manage cases where the input file is missing or unreadable.

## 🚀 Features

- Reads a user-specified file
- Adds line numbers to each line
- Saves the result to a new file named `modified_<original_filename>`
- Gracefully handles:
  - FileNotFound errors
  - IOErrors (reading or writing issues)

## 🛠 How to Run

1. Save the script as `file_handler.py`
2. Make sure you have a text file in the same folder (e.g., `example.txt`)
3. Run the program using:
   ```bash
   python file_handler.py
