"""
--- Advent of Code 2023 ---
--- Day 11: Cosmic Expansion ---
"""

from time import perf_counter

TEST = False


def main():
    """Main program"""
    input_file = open_input_file()

    universe = []
    for line in input_file:
        universe.append([char for char in line])

    empty_rows = find_empty_rows(universe)
    empty_cols = find_empty_cols(universe)

    galaxies = find_galaxies(universe)

    galaxies_part1 = recalculate_galaxies_coordinates(
        galaxies, empty_rows, empty_cols, 2
    )
    total_distance = dist_between_all_galaxies(galaxies_part1)

    print()
    print("Part 1 result:")
    print(f"Total distance between galaxies = {total_distance}")
    print()

    galaxies_part2 = recalculate_galaxies_coordinates(
        galaxies, empty_rows, empty_cols, 1000000
    )
    total_distance = dist_between_all_galaxies(galaxies_part2)

    print("Part 2 result:")
    print(f"Total distance between galaxies = {total_distance}")
    print()


def find_empty_rows(universe: list) -> list:
    """Finds empty rows in the universe map"""
    empty_rows = []

    for i, row in enumerate(universe):
        if "#" not in set(row):
            empty_rows.append(i)

    return empty_rows


def find_empty_cols(universe: list) -> list:
    """Finds empty columns in the universie map"""
    empty_cols = []

    for i, _ in enumerate(universe[0]):
        if "#" not in set(universe[j][i] for j in range(len(universe))):
            empty_cols.append(i)

    return empty_cols


def dist_between_two_galaxies(galaxy1: tuple, galaxy2: tuple) -> int:
    """Returns the factor between galaxy1 and galaxy2"""

    x = abs(galaxy1[0] - galaxy2[0])
    y = abs(galaxy1[1] - galaxy2[1])

    return x + y


def dist_between_all_galaxies(galaxies):
    """Returns the total distance between all galaxies"""
    total_distance = 0

    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            total_distance += dist_between_two_galaxies(galaxies[i], galaxies[j])

    return total_distance


def find_galaxies(universe: list) -> list:
    """Returns a list of galaxies (represented by '#') within a 2D map"""
    galaxies = []

    for i, _ in enumerate(universe):
        for j, _ in enumerate(universe[0]):
            if universe[i][j] == "#":
                galaxies.append((i, j))

    return galaxies


def recalculate_galaxies_coordinates(
    galaxies: list, empty_rows, empty_cols, factor
) -> list:
    """
    Recalculates galaxies coordinates based on empty rows and columns
    in the universe map and the expansion factor
    """
    new_galaxies = []

    for galaxy in galaxies:
        row_offset = sum(1 for row in empty_rows if row < galaxy[0])
        col_offset = sum(1 for col in empty_cols if col < galaxy[1])

        new_galaxy = (
            galaxy[0] - row_offset + row_offset * factor,
            galaxy[1] - col_offset + col_offset * factor,
        )
        new_galaxies.append(new_galaxy)

    return new_galaxies


def open_input_file():
    """Opens input file and returns it as a list of lines"""
    if TEST:
        with open("input_test.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]

    with open("input.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")
