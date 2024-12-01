from pathlib import Path


def parse_puzzle_input(file_name: str) -> list[tuple[int, int]]:
    puzzle_lines = [
        list(map(int, line.split()))
        for line in ((Path(__file__).parent) / file_name).open("r").readlines()
    ]
    lists = list(zip(*puzzle_lines))
    list1 = sorted(lists[0])
    list2 = sorted(lists[1])
    return list(zip(list1, list2))


def list_distance(lists: list[tuple[int, int]]) -> int:
    distance = 0
    for list_pair in lists:
        distance += abs(list_pair[0] - list_pair[1])
    return distance


def list_similarity(lists: list[tuple[int, int]]) -> int:
    transposed_lists: list[tuple[int]] = list(zip(*lists))
    similarity = 0
    for i in transposed_lists[0]:
        similarity += i * transposed_lists[1].count(i)
    return similarity


def main() -> None:
    puzzle_input = parse_puzzle_input("example.txt")
    assert list_distance(puzzle_input) == 11
    assert list_similarity(puzzle_input) == 31

    puzzle_input = parse_puzzle_input("puzzle_input.txt")
    print(list_distance(puzzle_input))
    print(list_similarity(puzzle_input))


if __name__ == "__main__":
    main()
