import os.path
def read_input(filename):
    with open(os.path.dirname(os.path.dirname(__file__))+ "/inputs/"+filename) as f:
        var = f.read()
    return var
