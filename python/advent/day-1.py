from advent.utils import default_argument_parser, read_txt_file_lines

from typing import List


def group_lines(lines: List[str]) -> List[List[str]]:
    groups = []
    group = []
    for index, line in enumerate(lines):
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
        if index == len(lines) - 1:
            groups.append(group)
    return groups


def process_group(group: List[str]) -> int:
    return sum([int(element) for element in group])


def main():
    parser = default_argument_parser(day_count=1).parse_args()
    lines = read_txt_file_lines(path=parser.path)
    groups = group_lines(lines=lines)
    results = [
        process_group(group=group)
        for group
        in groups
    ]
    print(f"part 1: {max(results)}")

    top = sum(list(reversed(sorted(results)))[:3])
    print(f"part 2: {top}")


if __name__ == '__main__':
    main()
