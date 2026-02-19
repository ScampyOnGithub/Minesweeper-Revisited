import tkinter as tk
import random

window = tk.Tk()
window.title("Minesweeper Reworked")


indicator_1 = tk.PhotoImage(file='assets/indicator_1.png')
indicator_2 = tk.PhotoImage(file='assets/indicator_2.png')
indicator_3 = tk.PhotoImage(file='assets/indicator_3.png')
indicator_4 = tk.PhotoImage(file='assets/indicator_4.png')
indicator_5 = tk.PhotoImage(file='assets/indicator_5.png')
indicator_6 = tk.PhotoImage(file='assets/indicator_6.png')
indicator_7 = tk.PhotoImage(file='assets/indicator_7.png')
indicator_8 = tk.PhotoImage(file='assets/indicator_8.png')
mine = tk.PhotoImage(file='assets/mine.png')

window.iconphoto(False, mine)

asset_dict = {1: indicator_1, 2: indicator_2, 3: indicator_3, 4: indicator_4, 5: indicator_5, 6: indicator_6, 7: indicator_7, 8: indicator_8, 9: mine}

def generate_board(initial_click_coordinates: list[int], geometry: list[int] = [10,5], mines: int = 20, ) -> list[list[int]]:
    """
    A function that generates a valid minesweeper board such that the player never starts on a mine tile. It is intended to be called after the initial click of each game

    :param geometry: - The size of the board in the form [width, height]
    :param mines:  - The number of mines in the board
    :param initial_click_coordinates: - The coordinates of the initial click on the board
    :return: - The board as a list
    """

    # Preventative measure for when the number of mines entered exceeds the maximum possible number of mines
    if mines > geometry[0] * geometry[1] - 9:
        return []

    board = [[0 for _ in range(geometry[1])] for _ in range(geometry[0])]    # generates a 2-dimensional board for the mines to be added to
    mines_on_board = 0

    print(geometry)
    while mines_on_board < mines:
        mine_attempt = [random.randint(0, geometry[0]-1), random.randint(0, geometry[1]-1)]     # selects a random tile within the board area
        print(mine_attempt)
        if board[mine_attempt[0]][mine_attempt[1]] != 9 and (abs(mine_attempt[0] - initial_click_coordinates[0]) > 1 or abs(mine_attempt[1] - initial_click_coordinates[1]) > 1):
            print("Mine attempt passed")
            board[mine_attempt[0]][mine_attempt[1]] = 9
            mines_on_board += 1

            # update surrounding tiles
            if mine_attempt[0] > 0:

                # x-1
                if board[mine_attempt[0]-1][mine_attempt[1]] != 9:
                    board[mine_attempt[0]-1][mine_attempt[1]] += 1

                # x-1, y-1
                if mine_attempt[1] > 0:
                    if board[mine_attempt[0]-1][mine_attempt[1]-1] != 9:
                        board[mine_attempt[0]-1][mine_attempt[1]-1] += 1

                # x-1, y+1
                if mine_attempt[1] < geometry[1]-1:
                    if board[mine_attempt[0]-1][mine_attempt[1] + 1] != 9:
                        board[mine_attempt[0]-1][mine_attempt[1] + 1] += 1

            if mine_attempt[0] < geometry[0]-1:

                # x+1
                if board[mine_attempt[0] + 1][mine_attempt[1]] != 9:
                    board[mine_attempt[0] + 1][mine_attempt[1]] += 1

                # x+1, y-1
                if mine_attempt[1]-1 > 0:
                    if board[mine_attempt[0] + 1][mine_attempt[1]-1] != 9:
                        board[mine_attempt[0] + 1][mine_attempt[1]-1] += 1

                # x+1, y+1
                if mine_attempt[1] < geometry[1]-1:
                    if board[mine_attempt[0] + 1][mine_attempt[1] + 1] != 9:
                        board[mine_attempt[0] + 1][mine_attempt[1] + 1] += 1

            # y+1
            if mine_attempt[1] < geometry[1] - 1:
                if board[mine_attempt[0]][mine_attempt[1] + 1] != 9:
                    board[mine_attempt[0]][mine_attempt[1] + 1] += 1

            # y-1
            if mine_attempt[1]-1 > 0:
                if board[mine_attempt[0]][mine_attempt[1]-1] != 9:
                    board[mine_attempt[0]][mine_attempt[1]-1] += 1


    for row in board:
        print(row)

    return board

def render_board(board: list[list[int]], master: tk.Tk | tk.Frame) -> None:
    global asset_dict
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell == 0:
                tk.Button(master).grid(row=cell_index, column=row_index, sticky=tk.NSEW)
            if cell != 0:
                tk.Button(master, text=str(cell), image=asset_dict[cell]).grid(row=cell_index, column=row_index, sticky=tk.NSEW)

def main() -> None:
    global window
    generate_board([4,2], [20,10], 50)
    render_board(generate_board([4,2], [20,10], 50), window)
    window.mainloop()
    return

if __name__ == '__main__':
    main()
