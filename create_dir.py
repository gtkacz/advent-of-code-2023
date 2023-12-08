import os

def main():
    day_to_create = int(input('Which day do you want to create? '))

    day_to_create = day_to_create if day_to_create > 9 else f'0{day_to_create}'

    os.mkdir(f'./day_{day_to_create}')
    
    open(f'./day_{day_to_create}/__init__.py', 'w').close()
    open(f'./day_{day_to_create}/input.in', 'w').close()

    with open(f'./day_{day_to_create}/main.py', 'w') as f:
        f.write('# Path: day_{day_to_create}/main.py\n')
        f.write('def main():\n')
        f.write('    print(\'Hello, World!\')\n')
        f.write('\n')
        f.write('\n')
        f.write('if __name__ == \'__main__\':\n')
        f.write('    main()')

if __name__ == '__main__':
    main()