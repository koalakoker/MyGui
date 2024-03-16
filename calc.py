def read(file_path):
    instructions = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                instructions.append(line)
    return instructions

def iterateVars(var, vg, f):
    for key, value in vg.items():
        for key2, value2 in value.fields.items():
            f(var, vg, key, value, key2, value2)     

def fpv(var, vg, key, value, key2, value2):
    var[key2] = vg[key].fields[key2].value.get()

def populateVars(var, vg):
    iterateVars(var, vg, fpv)

def fsv(var, vg, key, value, key2,value2):
    vg[key].fields[key2].value.set(var[key2])

def storeVars(var,vg):
    iterateVars(var, vg, fsv)

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
