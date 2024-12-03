import re

def find_and_exec_all_mul(filename):
    with open(filename) as f:
        file_content = ''.join(f.readlines())
        matches = re.findall(r'mul\(\d+,\d+\)', file_content)
        total = 0
        for instr in matches:
            instr = instr.replace('mul(', '').replace(')', '')
            instr = instr.split(',')
            instr = [int(n) for n in instr]
            total += instr[0] * instr[1]
        print(total)

def find_and_exec_all_mul_conditional(filename):
    with open(filename) as f:
        file_content = ''.join(f.readlines())
        matches = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', file_content)
        total = 0
        enabled = True
        for instr in matches:
            if instr == 'do()':
                enabled = True
            elif instr == 'don\'t()':
                enabled = False
            elif enabled:
                instr = instr.replace('mul(', '').replace(')', '')
                instr = instr.split(',')
                instr = [int(n) for n in instr]
                total += instr[0] * instr[1]
        print(total)


def main():
    find_and_exec_all_mul('day3/input.txt')
    find_and_exec_all_mul_conditional('day3/input.txt')

if __name__ == "__main__":
    main()