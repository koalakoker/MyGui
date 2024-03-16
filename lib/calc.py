from lib.vars import populateVars, storeVars

def read(file_path):
    instructions = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                instructions.append(line)
    return instructions

def calc(file_path, vg):
    var = {}
    populateVars(var, vg)
    instructions = read(file_path)
    for instruction in instructions:
        try:
            exec(instruction, var)
        except Exception as e:
            print(f"Error executing instruction '{instruction}': {e}")
    storeVars(var, vg)
