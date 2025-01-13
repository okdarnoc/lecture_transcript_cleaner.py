#!/usr/bin/env python3
"""
Text File Processor

This script processes text files in a specified folder by:
1. Removing the first line of each file
2. Removing content after specific Chinese markers ('講者備註' or '講著備註')
3. Preserving the modified content while maintaining UTF-8 encoding

Author: [Your Name]
Date: January 13, 2025
"""

import os
import glob
from typing import List, Optional

def get_valid_folder_path() -> str:
    """
    Prompts the user for a valid folder path and validates its existence.
    
    Returns:
        str: A validated folder path that exists in the system
    """
    while True:
        # Prompt user for the folder path
        folder_path = input("Please enter the folder path containing .txt files: ").strip()
        
        # Remove quotes if the user included them
        folder_path = folder_path.strip('"\'')
        
        # Validate if the path exists
        if os.path.exists(folder_path):
            return folder_path
        else:
            print(f"Error: The path '{folder_path}' does not exist. Please try again.")

def find_text_files(folder_path: str) -> List[str]:
    """
    Finds all .txt files in the specified folder path.
    
    Args:
        folder_path (str): Path to the folder containing text files
        
    Returns:
        List[str]: List of paths to all .txt files found
    """
    # Use glob to find all .txt files in the specified folder
    return glob.glob(os.path.join(folder_path, "*.txt"))

def find_split_point(content: str) -> Optional[int]:
    """
    Finds the earliest occurrence of Chinese markers for speaker notes.
    
    Args:
        content (str): The text content to search within
        
    Returns:
        Optional[int]: Index where the split should occur, or -1 if no markers found
    """
    # Define the Chinese markers to look for
    markers = ['講者備註', '講著備註']
    
    # Find the position of each marker
    positions = [content.find(marker) for marker in markers]
    
    # Filter out -1 values (not found)
    valid_positions = [pos for pos in positions if pos != -1]
    
    # Return the earliest position if any markers were found
    return min(valid_positions) if valid_positions else -1

def process_text_files(folder_path: str) -> None:
    """
    Processes all text files in the specified folder by removing the first line
    and any content after speaker notes markers.
    
    Args:
        folder_path (str): Path to the folder containing text files to process
    """
    # Get list of text files
    txt_files = find_text_files(folder_path)
    
    # Track processing statistics
    processed_count = 0
    error_count = 0
    
    for file_path in txt_files:
        try:
            # Open and read the file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Skip empty files
            if not lines:
                print(f"Warning: Empty file found - {file_path}")
                continue
                
            # Skip first line and join remaining lines
            if len(lines) > 1:
                content = ''.join(lines[1:])
                
                # Find split point for speaker notes
                split_index = find_split_point(content)
                
                # Remove content after split point if found
                if split_index != -1:
                    content = content[:split_index].rstrip()
                
                # Write modified content back to file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                processed_count += 1
                print(f"Successfully processed: {file_path}")
                
        except Exception as e:
            error_count += 1
            print(f"Error processing {file_path}: {str(e)}")
    
    # Print summary statistics
    print(f"\nProcessing complete!")
    print(f"Files processed successfully: {processed_count}")
    print(f"Files with errors: {error_count}")
    print(f"Total files attempted: {len(txt_files)}")

def main():
    """
    Main function to execute the text file processing workflow.
    """
    print("Text File Processor")
    print("==================")
    print("This script will process .txt files by removing the first line and")
    print("any content after speaker notes markers (講者備註 or 講著備註).\n")
    
    # Get validated folder path from user
    folder_path = get_valid_folder_path()
    
    # Process the files
    process_text_files(folder_path)

if __name__ == "__main__":
    main()
