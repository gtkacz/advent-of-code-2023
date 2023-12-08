def main():
    with open('day_01/input.in', 'r') as f:
        raw_lines = f.readlines()

    # Part 1
    lines = [tuple(map(int, filter(str.isdigit, line))) for line in raw_lines]

    output_1 = sum(tuple(map(lambda x: int(str(x[0]) + str(x[-1])), lines)))

    print(f'Part 1 output: {output_1}')

    # Part 2
    def number_replace(input_str: str) -> str:
        typed_numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

        replace_idx = sorted([(input_str.find(number) + len(number) - 1, number) for number in typed_numbers if input_str.find(number) != -1])

        if len(replace_idx) > 0:
            for enum, (idx, number) in enumerate(replace_idx):
                input_str = input_str[:idx+enum] + str(typed_numbers.index(number) + 1) + input_str[idx+enum:]

        return input_str

    lines = [tuple(map(int, filter(str.isdigit, number_replace(line)))) for line in raw_lines]

    output_2 = sum(tuple(map(lambda x: int(str(x[0]) + str(x[-1])), lines)))

    print(f'Part 2 output: {output_2}')

    with open('day_01/output.out', 'w') as f:
        f.write(f'{output_1}\n{output_2}')
