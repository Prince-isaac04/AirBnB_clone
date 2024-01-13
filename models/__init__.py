#!/usr/bin/python3
"""Initialization for the FileStorage class"""

# Importing the FileStorage class from the models.engine.file_storage module
from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class
storage = FileStorage()

# Reload data from storage using the reload method
storage.reload()
