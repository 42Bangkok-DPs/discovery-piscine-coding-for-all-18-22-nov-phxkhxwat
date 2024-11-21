def find_king(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "K":
                return (row, col)
    return None


def is_square_attacked(board, row, col, attackers):
    """Check if a square is attacked by any piece."""
    size = len(board)
    
    # Pawn attacks (assume pawns move upwards for simplicity)
    if "P" in attackers:
        for dr, dc in [(-1, -1), (-1, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == "P":
                return True

    # Rook and Queen horizontal/vertical attacks
    if "R" in attackers or "Q" in attackers:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row, col
            while 0 <= nr < size and 0 <= nc < size:
                nr, nc = nr + dr, nc + dc
                if 0 <= nr < size and 0 <= nc < size:
                    if board[nr][nc] == "R" or board[nr][nc] == "Q":
                        return True
                    elif board[nr][nc] != "":  # Blocked by another piece
                        break

    # Bishop and Queen diagonal attacks
    if "B" in attackers or "Q" in attackers:
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = row, col
            while 0 <= nr < size and 0 <= nc < size:
                nr, nc = nr + dr, nc + dc
                if 0 <= nr < size and 0 <= nc < size:
                    if board[nr][nc] == "B" or board[nr][nc] == "Q":
                        return True
                    elif board[nr][nc] != "":  # Blocked by another piece
                        break

    return False


def is_king_in_check(board):
    """Determine if the King is in check."""
    king_pos = find_king(board)
    if not king_pos:
        return None  # No King on the board

    row, col = king_pos
    return is_square_attacked(board, row, col, {"P", "R", "B", "Q"})


def main():
    # Example board
    board = [
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "R", "", ""],
        ["", "", "", "", "K", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
    ]

    # Check if King is in check
    result = is_king_in_check(board)
    if result:
        print("Success")
    elif result is False:
        print("Fail")
    else:
        pass  # Handle invalid boards gracefully


if __name__ == "__main__":
    main()
