#!/usr/bin/python3
"""
creates the storage variable and call the reload() method
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
