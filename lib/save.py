from lib.vars import populateVars
from lib.config import cfg
import json
from tkinter import filedialog
import os

def write_to_file(file_path, var):
  try:
    # Open the file in write mode
    with open(file_path, 'w') as file:
      # Write content to the file
      json.dump(var, file, indent=2)
    print(f"Content successfully written to {file_path}")
  except Exception as e:
    print(f"Error writing to file: {e}")

def save(vg):
  current_directory = os.getcwd()
  file_path = filedialog.asksaveasfilename(initialdir = current_directory, defaultextension = cfg["defExt"], filetypes=[(cfg["fileType"], cfg["defExt"])])
  if (file_path != ""):
    var = {}
    populateVars(var, vg)
    write_to_file(file_path,var)
  