import os
import re
import timeit
from typing import Callable, Union

# from numba import jit


class AdventOfCodeSolution:
    def __init__(self, day: int):
        self.__location__: str = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.__discover_days()
        self.main(day)

    def __discover_days(self):
        result: list[str] = []

        for _, dirnames, _ in os.walk('./'):
            result = result + [dirname for dirname in dirnames if  re.compile('day_*').match(dirname)]

        self.days = [int(day.replace('day_', '').removeprefix('0')) for day in result]

    def main(self, day: int) -> Union[str, int]:
        if day not in self.days:
            raise NotImplementedError(f'Day {day} has not been implemented yet.')
        
        else:
            module = __import__(f'day_{day if day > 9 else f"0{day}"}.main', fromlist=[f'day_{day if day > 9 else f"0{day}"}.main'])
            day_solution = getattr(module, 'main')
            self.run_day(day_solution)

    def run_day(self, day_solution: Callable) -> None:
        start_time = timeit.default_timer()
        day_solution()
        delta = timeit.default_timer() - start_time
        print(f'\nRan in: {delta}s\n\n')


if __name__ == '__main__':
    day_input = int(input('Which day do you want to run? '))
    AdventOfCodeSolution(day_input)
