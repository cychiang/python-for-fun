import dis
import random
from time import time

def evaluate_time(function):
    def warp(*arg):
        start = time()
        function(*arg)
        end = time()
        print('{}: {} ms'.format(
            function.__name__, (end - start) * 1000
        ))
    return warp

test_func_type = [
    'add', 'sub', 'mul', 'div', 'boom'
]
support_func_type = [
    'add', 'sub', 'mul', 'div'
]
func = {
    'add': lambda x: x['value_1'] + x['value_2'],
    'sub': lambda x: x['value_1'] - x['value_2'],
    'mul': lambda x: x['value_1'] * x['value_2'],
    'div': lambda x: x['value_1'] / x['value_2']
}

def data_generator(iterations):
    return [{
        'ops': test_func_type[random.randint(0, 4)],
        'value_1': random.randint(1, 10),
        'value_2': random.randint(1, 10)
    } for idx in range(iterations)]

def if_else_statement(data):
    # ignore ops we don't supported
    ans = None
    if data["ops"] == "add":
        ans = data["value_1"] + data["value_2"]
    if data["ops"] == "sub":
        ans = data["value_1"] - data["value_2"]
    if data["ops"] == "mul":
        ans = data["value_1"] * data["value_2"]
    if data["ops"] == "div":
        ans = data["value_1"] / data["value_2"]
    return ans

def if_elif_statement(data):
    # cache ops we don't supported
    ans = None
    if data["ops"] == "add":
        ans = data["value_1"] + data["value_2"]
    elif data["ops"] == "sub":
        ans = data["value_1"] - data["value_2"]
    elif data["ops"] == "mul":
        ans = data["value_1"] * data["value_2"]
    elif data["ops"] == "div":
        ans = data["value_1"] / data["value_2"]
    else:
        # print("ops: {ops} not support".format(ops=data["ops"]))
        pass

    return ans

def try_except_dict_func_statement(data):
    ans = None
    try:
        ans = func[data['ops']](data)
    except KeyError:
        # print("ops: {ops} not support".format(ops=data["ops"]))
        pass
    return ans

def if_else_dict_func_statement(data):
    ans = None
    if data['ops'] in support_func_type:
        ans = func[data['ops']](data)
    else:
        # print("ops: {ops} not support".format(ops=data["ops"]))
        pass
    return ans

@evaluate_time
def time_if_else_statement(tasks):
    for task in tasks:
        if_else_statement(task)

@evaluate_time
def time_if_elif_statement(tasks):
    for task in tasks:
        if_elif_statement(task)

@evaluate_time
def time_try_except_dict_func_statement(tasks):
    for task in tasks:
        try_except_dict_func_statement(task)

@evaluate_time
def time_if_else_dict_func_statement(tasks):
    for task in tasks:
        if_else_dict_func_statement(task)

def process(input):
    # evaluate assembly code
    # if_else_statement
    # print('if_else_statement')
    # dis.dis(if_else_statement)
    # if_elif_statement
    # print('if_elif_statement')
    # dis.dis(if_elif_statement)
    # try_except_dict_func_statement
    # print('try_except_dict_func_statement')
    # dis.dis(try_except_dict_func_statement)
    # if_else_dict_func_statement
    # print('if_else_dict_func_statement')
    # dis.dis(if_else_dict_func_statement)
    # evaluate time
    time_if_else_statement(input)
    time_if_elif_statement(input)
    time_try_except_dict_func_statement(input)
    time_if_else_dict_func_statement(input)

if __name__ == "__main__":
    # code analysis with disassembler
    test_case = data_generator(50000)
    process(test_case)
    