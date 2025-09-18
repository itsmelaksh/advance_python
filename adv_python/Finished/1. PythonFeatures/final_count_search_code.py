# Enter your code here. Read input from STDIN. Print output to STDOUT

from typing import List


def countOptiverOccurences(grid: List[str]) -> int:
    word_to_search = "OPTIVER"
    rev_search_word = word_to_search[::-1]
    ret_occurence_count = 0
    w_len = len(word_to_search)
    len_grid = len(grid)
    len_row = len(grid[0])

    # let us have loop to search through row - Horizontal search
    for row in grid:
        search_string = "".join(row)
        ret_occurence_count += search_string.count(word_to_search) + search_string.count(rev_search_word)

    # extend the search to whole grid - vertical search
    for col in zip(*grid):
        search_string = "".join(col)
        ret_occurence_count += search_string.count(word_to_search) + search_string.count(rev_search_word)

    # --- diagonal: top-left to bottom-right ---
    for i in range(len_grid):
        for j in range(len_row):
            if i + w_len <= len_grid and j + w_len <= len_row:
                diag = "".join(grid[i + k][j + k] for k in range(w_len))
                ret_occurence_count += diag.count(word_to_search) + diag.count(rev_search_word)

    # --- diagonal: top-right to bottom-left ---
    for i in range(len_grid):
        for j in range(len_row):
            if i + w_len <= len_grid and j - w_len + 1 >= 0:
                diag = "".join(grid[i + k][j - k] for k in range(w_len))
                ret_occurence_count += diag.count(word_to_search) + diag.count(rev_search_word)

    return ret_occurence_count


if __name__ == "__main__":
    n = int(input().strip())
    if n != 0:
        grid = [input().strip() for _ in range(n)]
        print(countOptiverOccurences(grid))
    else:
        print(0)

