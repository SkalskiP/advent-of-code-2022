from argparse import ArgumentParser
from typing import List


def default_argument_parser(day_count: int) -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('--path', '-p', type=str, required=True, help=f'path to day {day_count} input file')
    return parser


def read_txt_file_lines(path: str) -> List[str]:
    with open(path) as f:
        lines = [line.rstrip() for line in f]
    return lines
