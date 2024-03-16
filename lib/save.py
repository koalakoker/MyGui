from lib.vars import populateVars
import json

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
  var = {}
  populateVars(var, vg)
  write_to_file("save.txt",var)