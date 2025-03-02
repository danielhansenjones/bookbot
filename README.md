**Disclaimer:** This is just a simple learning project from Boot.dev and is not meant to represent production-level quality. I may choose to make this repository private in the future as it is still a work in progress.

## Overview
BookBot reads a book file provided via a command‑line argument and generates simple statistics such as:
- **Word Count:** Total number of words in the book.
- **Character Count:** Frequency of each alphabetical character (case-insensitive) sorted in descending order.

## Project Structure
``` 
project_root/
│
├── main.py            # Main script to load a book file and display its statistics
├── stats.py           # Module containing functions for counting words and characters
└── books/             # Directory containing book text files:
    ├── frankenstein.txt
    ├── mobydick.txt
    └── prideandprejudice.txt
```
## Usage
To run the program, navigate to the project root directory and run the following command (adjust the file name as needed):
``` bash
python3 main.py books/frankenstein.txt
```
For example, you can also run:
- `python3 main.py books/mobydick.txt `
``` 
- ```bash
  python3 main.py books/prideandprejudice.txt
```
If no file is provided, the program will display a usage message and exit.
## Requirements
- **Python Version:** 3.13.1
- **Dependencies:** There are no external packages required; the project only uses standard Python modules.

## About This Project
This project was created as part of the [Boot.dev](https://www.boot.dev) course to experiment with file I/O, command-line arguments, and basic data analysis. It provides a foundation for further development and additional features, such as more detailed text analysis or support for different file formats.
## Acknowledgments
- **Boot.dev:** For the course content and challenges that inspired the project.
- **Project Gutenberg:** For providing free texts used in this project.

