1. File Compressor (File compressor.py)
A GUI application that compresses files using either GZIP or ZIP compression formats.

Features:
Graphical user interface built with Tkinter

Supports two compression methods:

GZIP (fast compression)

ZIP (standard compression)

Shows compression statistics (original size, compressed size, ratio)

Threaded compression to keep the GUI responsive

Status bar for operation feedback

How it works:
User selects a file via the browse button

Chooses compression type (GZIP or ZIP)

Clicks "Compress File" to start the process

Receives a summary of the compression results

Technical Details:
Uses gzip module for GZIP compression

Uses zipfile module for ZIP compression

Implements threading with Thread from the threading module

Calculates compression ratio for user feedback

2. Image Converter (Image converter.py)
A GUI tool for converting images between different formats.

Features:
Converts between multiple image formats: JPG, PNG, BMP, GIF, TIFF

Automatic handling of RGBA to RGB conversion for JPEG output

Shows conversion statistics (file sizes before/after)

Simple, intuitive interface with file browsing

Supported Formats:
Input: JPG, JPEG, PNG, BMP, GIF, TIFF

Output: JPG, PNG, BMP, GIF, TIFF

How it works:
User selects an input image file

Chooses output format from dropdown

Clicks "Convert" button

Receives conversion results with file size information

Technical Details:
Uses Pillow (PIL) library for image processing

Handles mode conversion for JPEG output (RGBA → RGB)

Provides detailed error messages for conversion failures

Clean interface with ttk.Combobox for format selection

3. Zip/Unzip Utility (Zip file & Unzip file.py)
A dual-function utility for compressing files/folders to ZIP and extracting ZIP archives.

Features:
Zip files or entire folders

Unzip files to specified locations

Preserves directory structure when zipping folders

Simple, clean interface with clear operations

How it works:
Zipping:

User selects a file or folder

Chooses output ZIP file location

Receives confirmation message

Unzipping:

User selects a ZIP file

Chooses extraction directory

Receives confirmation message

Technical Details:
Uses zipfile module for all ZIP operations

Implements recursive directory traversal for folder compression

Provides success/error messages for all operations

Smart default paths for output files based on input
