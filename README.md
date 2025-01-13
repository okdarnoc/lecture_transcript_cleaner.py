# Lecture Transcript Cleaner Documentation

Welcome to the documentation for the Lecture Transcript Cleaner, a purpose-built Python tool designed to streamline and standardize Chinese lecture transcripts. This document will guide you through understanding, installing, and effectively using the tool to process your transcript files.

## Introduction

The Lecture Transcript Cleaner addresses two common challenges in lecture transcript processing: removing metadata headers and cleaning up speaker notes. When working with transcribed lectures, files often contain administrative information in the first line and speaker annotations that aren't needed in the final transcript. This tool automates the removal of these elements while preserving the core lecture content.

### Key Features

The tool has been carefully designed to handle the specific needs of Chinese lecture transcript processing:

First, it removes the initial line of each transcript file, which typically contains metadata such as date, lecture number, or administrative details. This standardizes the beginning of each transcript to start directly with the lecture content.

Second, it identifies and removes speaker notes sections marked with either '講者備註' or '講著備註'. These annotations, while valuable during the transcription process, are usually not needed in the final document. The tool carefully preserves all content before these markers while removing everything after them.

Throughout the entire process, the tool maintains proper UTF-8 encoding to ensure Chinese characters are handled correctly, preventing any potential character corruption that could occur during processing.

## Getting Started

### System Requirements

Before installing the tool, ensure your system meets these basic requirements:

- Python 3.6 or higher installed
- Basic familiarity with command-line operations
- Sufficient disk space for processing files
- Read and write permissions for the target directories

### Installation Process

The installation process has been kept intentionally simple to ensure easy deployment across different systems:

```bash
git clone https://github.com/yourusername/lecture-transcript-cleaner.git
cd lecture-transcript-cleaner
```

No additional Python packages are required as the tool utilizes only standard library modules. This design choice ensures maximum compatibility and eliminates dependency-related issues.

## Using the Tool

### Basic Usage

The tool is designed to be straightforward to use while providing clear feedback about its operations. To begin processing your transcripts:

1. Open your terminal or command prompt
2. Navigate to the tool's directory
3. Execute the following command:

```bash
python lecture_transcript_cleaner.py
```

When prompted, provide the complete path to your transcript files:

```bash
Please enter the folder path containing .txt files: C:\Lectures\Transcripts
```

### Understanding the Output

As the tool processes your files, it provides real-time feedback:

```bash
Lecture Transcript Cleaner
=========================
Processing started...

Successfully processed: lecture_week1.txt
Successfully processed: lecture_week2.txt
Warning: Empty file found - lecture_week3.txt

Processing complete!
Files processed successfully: 2
Files with errors: 0
Total files attempted: 3
```

This output helps you track the progress and identify any issues that might need attention.

## Technical Details

### Processing Workflow

The tool follows a carefully designed workflow to ensure reliable processing:

1. Input Validation Phase:
   - Verifies the existence of the specified folder
   - Checks for appropriate file permissions
   - Identifies all .txt files in the directory

2. Content Processing Phase:
   - Opens each file with UTF-8 encoding
   - Removes the first line containing metadata
   - Searches for speaker note markers
   - Removes content after these markers
   - Preserves the cleaned content

3. Quality Control Phase:
   - Validates the processed content
   - Ensures proper file saving
   - Generates processing statistics

### Error Handling

The tool includes comprehensive error handling to manage common scenarios:

1. File System Errors:
   - Invalid paths
   - Permission issues
   - Missing files
   
2. Content Processing Errors:
   - Encoding problems
   - Empty files
   - Malformed content

3. System Resource Errors:
   - Insufficient memory
   - Disk space limitations

## Troubleshooting Guide

### Common Issues and Solutions

File Access Problems:
- Verify you have both read and write permissions for the target directory
- Ensure no other programs have the files locked
- Check that the path doesn't contain unsupported special characters

Encoding Issues:
- Confirm your files are saved in UTF-8 format
- Look for and remove any byte-order marks (BOM)
- Check for invalid or corrupted characters in the source files

Processing Errors:
- Ensure sufficient disk space for processing
- Close files in other applications before processing
- Verify file names don't contain special characters

## Best Practices

To get the most out of the Lecture Transcript Cleaner:

1. Organize your transcripts into dedicated folders for easier processing
2. Maintain consistent file naming conventions
3. Keep regular backups of your original files
4. Process files in manageable batches
5. Review processed files to ensure desired outcomes

## Contributing

We welcome contributions to improve the tool. If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure your contributions maintain:
- Clear documentation
- Comprehensive error handling
- Type hints for Python functions
- UTF-8 compatibility throughout

## License

This project is licensed under the MIT License, allowing for both personal and commercial use while maintaining attribution requirements. See the LICENSE file for complete details.

---

*Documentation maintained by [Your Name]*  
*Last Updated: January 13, 2025*
