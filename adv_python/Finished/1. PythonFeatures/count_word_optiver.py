
from typing import List

def countOptiverOccurences(grid):
    """

    Args:
        grid:

    Returns:

    """
    word_to_search = "OPTIVER"
    rev_search_word = word_to_search[::-1]
    ret_occurence_count = 0
    n = len(grid)
    m = len(grid[0])
    w_len = len(word_to_search)

    # let us have loop to search through row - Horizontal search
    for row in grid:
        search_string = "".join(row)
        ret_occurence_count += search_string.count(word_to_search) + search_string.count(rev_search_word)

    # --- diagonal: top-left to bottom-right ---
    for i in range(n):
        for j in range(m):
            if i + w_len <= n and j + w_len <= m:
                diag = "".join(grid[i + k][j + k] for k in range(w_len))
                ret_occurence_count += diag.count(word_to_search) + diag.count(rev_search_word)

    # --- diagonal: top-right to bottom-left ---
    for i in range(n):
        for j in range(m):
            if i + w_len <= n and j - w_len + 1 >= 0:
                diag = "".join(grid[i + k][j - k] for k in range(w_len))
                ret_occurence_count += diag.count(word_to_search) + diag.count(rev_search_word)

    # extend the search to whole grid - vertical search
    for col in zip(*grid):
        search_string = "".join(col)
        ret_occurence_count += search_string.count(word_to_search) + search_string.count(rev_search_word)

    print(ret_occurence_count)
    return ret_occurence_count


def countOptiverOccurrences(grid: List[str]) -> int:
    """
    Count occurrences of the word 'OPTIVER' in a 2D grid of characters.
    Matches can be horizontal, vertical, or diagonal (both directions).
    """
    word = "OPTIVER"
    rev = word[::-1]
    targets = {word, rev}

    # normalize grid: strip spaces, uppercase
    grid = [row.replace(" ", "").upper() for row in grid]
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < n and 0 <= c < m

    # directions: →, ←, ↓, ↑, ↘️, ↖️, ↙️, ↗️
    directions = [
        (0, 1), (0, -1),  # horizontal
        (1, 0), (-1, 0),  # vertical
        (1, 1), (-1, -1),  # main diagonal
        (1, -1), (-1, 1),  # anti diagonal
    ]

    count = 0
    for r in range(n):
        for c in range(m):
            for dr, dc in directions:
                seq = []
                rr, cc = r, c
                for _ in range(len(word)):
                    if not in_bounds(rr, cc):
                        break
                    seq.append(grid[rr][cc])
                    rr += dr
                    cc += dc
                if "".join(seq) in targets:
                    count += 1

    return count


# Example usage
if __name__ == "__main__":
    n = int(input().strip())
    grid = [input().strip() for _ in range(n)]
    print(countOptiverOccurrences(grid))

grid = ["SJQLFPQK", "JDDPQDMD", "AQEROBPT", "FOPTIVER", "BJDLQPFK", "VJFPQIEF", "PQKDIQDP", "AERIDQPL"]
countOptiverOccurences(grid)



def countOptiverOccurrences(grid: List[int]) -> int:
    """

    Args:
        grid:

    Returns:

    """
    word_to_search = "OPTIVER"
    rev_search_word = word_to_search[::-1]
    w_len = len(word_to_search)

    # normalize grid
    grid = [row.replace(" ", "").upper() for row in grid]
    len_grid = len(grid)
    if len_grid == 0:
        return 0
    len_row = len(grid[0])
    ret_occurence_count = 0

    # helper to check sequence in a direction
    def check(i, j, di, dj):
        for k in range(w_len):
            ni, nj = i + di * k, j + dj * k
            if ni < 0 or ni >= len_grid or nj < 0 or nj >= len_row:
                return 0
        seq = "".join(grid[i + di * k][j + dj * k] for k in range(w_len))
        return int(seq == word_to_search or seq == rev_search_word)

    # scan all positions in all 4 directions
    for i in range(len_grid):
        for j in range(len_row):
            # horizontal right
            ret_occurence_count += check(i, j, 0, 1)
            # vertical down
            ret_occurence_count += check(i, j, 1, 0)
            # diagonal down-right
            ret_occurence_count += check(i, j, 1, 1)
            # diagonal down-left
            ret_occurence_count += check(i, j, 1, -1)

    return ret_occurence_count
