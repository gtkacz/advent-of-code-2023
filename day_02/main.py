from numpy import prod

def main():
    with open('day_02/input.in', 'r') as f:
        raw_lines = f.readlines()

    # Part 1
    output_1 = 0

    def parse_1(line: str) -> int:
        target = {'red': 12, 'green': 13, 'blue': 14}

        l_split = line.replace('\n', '').split(': ')

        line_id = int(l_split[0].split(' ')[-1])

        games = l_split[1].split('; ')

        parsed_data: list[dict[str, int]] = [{color: int(quantity) for quantity, color in (item.split(' ') for item in obj.split(', '))} for obj in games]

        if any(obj.get(color, 0) > target[color] for color in target.keys() for obj in parsed_data):
            return 0
        
        return line_id

    for line in raw_lines:
        output_1 += parse_1(line)

    print(f'Part 1 output: {output_1}')

    # Part 2
    output_2 = 0

    def parse_2(line: str) -> int:
        games = line.replace('\n', '').split(': ')[1].split('; ')

        parsed_data: list[dict[str, int]] = [{color: int(quantity) for quantity, color in (item.split(' ') for item in obj.split(', '))} for obj in games]

        return prod(tuple({color: max(obj.get(color, 1) for obj in parsed_data) for color in set(color for dictionary in parsed_data for color in dictionary.keys())}.values()))

    for line in raw_lines:
        output_2 += parse_2(line)

    print(f'Part 2 output: {output_2}')

    with open('day_02/output.out', 'w') as f:
        f.write(f'{output_1}\n{output_2}')

if __name__ == '__main__':
    main()