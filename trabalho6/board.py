


class Board:

    def left(self, i:int, j:int) -> bool:
        j = j-1
        if j < 0:
            return False
        return self.__board[i][j]

    def rigth(self, i:int, j:int) -> bool:
        if j+1 >= len(self.__board[i]):
            return False
        return self.__board[i][j+1]

    def up(self, i:int, j:int) -> bool:
        i = i-1
        if i < 0:
            return False
        return self.__board[i][j]

    def down(self, i:int, j:int) -> bool:
        if i+1 >= len(self.__board):
            return False
        return self.__board[i+1][j]

    def up_left(self, i:int, j:int ) -> bool:
        i = i-1
        j = j-1
        if i < 0 or j < 0:
            return False
        return self.__board[i][j]

    def up_rigth(self, i:int, j:int) -> bool:
        i = i-1
        if i < 0 or j+1 >= len(self.__board[i]):
            return False
        return self.__board[i][j+1]

    def down_left(self, i:int, j:int) -> bool:
        j = j-1
        if j < 0 or i+1 >= len(self.__board):
            return False
        return self.__board[i+1][j]

    def down_right(self, i:int, j:int) -> bool:
        if i+1 >= len(self.__board) or j+1 >= len(self.__board[i]):
            return False
        return self.__board[i+1][j+1]

    def get_neighbours(self, i:int, j:int) -> list[bool]:
        return [
            self.left(i,j),
            self.rigth(i,j),
            self.up(i,j),
            self.down(i,j),
            self.up_left(i,j),
            self.up_rigth(i,j),
            self.down_left(i,j),
            self.down_right(i,j),
        ]
        
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

    def check(self)->tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        relife_list = []
        kill_list = []
        for i in range(self.__rows):
            for j in range(self.__columns):
                neighbors = self.get_neighbours(i, j)
                sum_neighbours = sum(neighbors)
                if sum_neighbours < 2:
                    kill_list.append((i,j))
                elif sum_neighbours > 3:
                    kill_list.append((i,j))
                elif sum_neighbours == 3:
                    relife_list.append((i,j))
                elif sum_neighbours == 2:
                    pass
                    #keep
