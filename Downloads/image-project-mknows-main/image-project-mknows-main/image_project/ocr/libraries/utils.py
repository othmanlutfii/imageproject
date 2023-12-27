"""
Module: utils.py

This module contains utility functions
for handling images and other tasks.

Author: [Your Name]
Date: [Current Date]
"""
import os

def delete_uploaded_image(img_path):
    """
    Delete the uploaded image at the specified path.

    Args:
        img_path (str): The path of the image to be deleted.

    Returns:
        remove uploaded image
    """
    return os.remove(img_path)
