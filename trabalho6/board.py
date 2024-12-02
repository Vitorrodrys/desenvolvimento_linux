


class Board:

    def __init__(
        self,
        rows: int,
        columns: int,
    ) -> None:
        self.__board = [[False]*columns]*rows
        self.__rows = rows
        self.__columns = columns

    def swap_value(self, i:int, j:int):
        self.__board[i][j] = not self.__board[i][j]
