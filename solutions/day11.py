from read_input import read_input

input_11 = read_input('input11.txt')
monkey_stringlist = [monkey.split("\n") for monkey in input_11.split("Monkey")]
monkey_stringlist = [list(filter(None, lst)) for lst in monkey_stringlist][1:]
print(monkey_stringlist)


class Monkey:
    def __init__(self, monkey_list):
        self.monkey_number = int(monkey_list[0].strip()[0])
        self.current_items = [int(item) for item in monkey_list[1].split(":")[1].split(",")]
        self.operation_string = monkey_list[2].split(":")[1].strip().split("=")[1]
        self.test_divisible = int(monkey_list[3].split("by")[1].strip())
        self.true_monkey = int(monkey_list[4].split("monkey")[1].strip())
        self.false_monkey = int(monkey_list[5].split("monkey")[1].strip())
        self.output_items = []
        self.inspect_count = 0

    def process_items(self):
        items = self.current_items
        for item in items:
            # print(self.current_items)
            output = self.process_item(item)
            self.output_items.append(output)
        self.current_items = []

    def process_item(self, item):
        old = item
        # print(f"item to process = {old}")
        # print("process = " + self.operation_string)
        new = eval(self.operation_string)
        # print(f"after operation = {new}")
        new = new % 9699690
        self.inspect_count +=1
        # print(f"after div3 = {new}")
        if new % self.test_divisible == 0:
            return self.true_monkey, new
        else:
            return self.false_monkey, new
    def take_output(self):
        output = self.output_items
        self.output_items = []
        return output
    def add_item(self,item):
        self.current_items.append(item)
    def __repr__(self):
        return \
        f"""Monkey number {self.monkey_number}
        current inventory: {self.current_items}
        inspection count: {self.inspect_count}"""



monkey_list = []
for monkey in monkey_stringlist:
    monkey_list.append(Monkey(monkey))
for round in range(1,10001):
    # print(round)
    item_redistribution = []
    for monkey in monkey_list:
        # print(f"monkey number {monkey.monkey_number}")
        monkey.process_items()
        monkey_output = monkey.take_output()
        for item in monkey_output:
            monkey_list[item[0]].add_item(item[1])
        # item_redistribution.extend(monkey.take_output())
inspec_counter = []
test_div_list = []
for monkey in monkey_list:
    test_div_list.append(monkey.test_divisible)
    print(monkey)
    inspec_counter.append(monkey.inspect_count)
print(test_div_list)
div_number = 1
for div in test_div_list:
    div_number *= div
print(div_number)
v1 = max(inspec_counter)
inspec_counter.remove(v1)
v2 = max(inspec_counter)
monkey_buisness = v1*v2
print(monkey_buisness)
