from lib.vars import populateVars, storeVars

def read(file_path):
    with open(file_path, 'r') as file:
        external_code = file.read()
    return external_code

def calc(file_path, vg):
    var = {}
    populateVars(var, vg)
    instruction = read(file_path)
    try:
        exec(instruction, var)
    except Exception as e:
        print(f"Error executing instructions: {e}")
    storeVars(var, vg)
