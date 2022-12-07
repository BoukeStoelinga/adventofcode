from read_input import read_input
input_7 = read_input('input7.txt')
class Dir:
    def __init__(self,name,parent=None):
        self.files = []
        self.name = name
        self.computed = False
        self.size = 0
        self.parent = parent


    def compute_size(self):
        # Recursive compute size. Use top level only
        self.computed = True
        for item in self.files:
            if not item.computed:
                item.compute_size()
            self.size += item.size

    def __eq__(self,other):
        if isinstance(other,Dir):
            return self.name == other.name
        else:
            return self.name == other
    def __repr__(self):
        return str(self.files)

class File:
    def __init__(self,name,size,parent=None):
        self.computed = True
        self.name = name
        self.size = size
        self.parent = parent
    def __eq__(self, other):
        # ugly, but easy to check if directory names match
        return False
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return f"f: {self.name}: {self.size}"

home = Dir('/')
current_dir = home
# Split based on ls commands
line_input = [lst.split("\n") for lst in input_7.split('\n$ ls\n')]
cd_commands = []
dir_list = []
# iterate over ls commands
for line in line_input:
    for command in line:

        # create new directory, add to current directory
        if command.split(" ")[0] == 'dir':
            direct = Dir(command.split(" ")[1], parent=current_dir)
            dir_list.append(direct)
            current_dir.files.append(direct)

        # change current directory
        elif command.split(" ")[0] == "$":
            dir_to_change = command.split(" ")[2]
            # level up
            if dir_to_change == "..":
                current_dir = current_dir.parent

            # search in current subdirectories
            else:
                for item in current_dir.files:
                    if item == dir_to_change:
                        current_dir = item

        # add item to directory
        else:
            current_dir.files.append(File(command.split(" ")[1],int(command.split(" ")[0]),parent=current_dir))
home.compute_size()
count = 0
total_size = 0
# part 1
for direct in dir_list:
    # print(direct.name)
    # print(direct.size)
    total_size += direct.size
    if direct.size <= 100000:
        count += direct.size
print(count)

# print(home.size-40000000)
big_enough_directs = []
dir_sizes = []
for direct in dir_list:
    if direct.size > home.size-40000000:
        big_enough_directs.append(direct)
        dir_sizes.append(direct.size)
print(big_enough_directs[dir_sizes.index(min(dir_sizes))].size)

