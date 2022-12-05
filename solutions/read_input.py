import os.path
def read_input(filename):
    with open(os.path.dirname(os.path.dirname(__file__))+ "/inputs/"+filename) as f:
        var = f.read()
    return var
def gen_new_pyfiles():
    for n in range(6,26):
        with open(os.path.dirname(__file__)+ "/day"+str(n)+".py",'w') as f:
            f.write(f"""from read_input import read_input\ninput_{n} = read_input('input{n}.txt')""")
