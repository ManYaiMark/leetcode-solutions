class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.' :
                    continue
                if f"row {r} has {board[r][c]}" in seen:
                    return False
                if f"col {c} has {board[r][c]}"  in seen:
                    return False
                if f"box {r//3}-{c//3} has {board[r][c]}"  in seen:
                    return False

                seen.add(f"row {r} has {board[r][c]}")
                seen.add(f"col {c} has {board[r][c]}")
                seen.add(f"box {r//3}-{c//3} has {board[r][c]}")

        return True