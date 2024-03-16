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