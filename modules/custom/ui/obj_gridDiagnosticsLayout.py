

class Obj_gridDiagnosticsLayout():
    """
    This class trackes the indices of grid layouts assuming that the grid either has a maximum number of columns or rows. The current logic will not account for grids who dimensions are either both bounded or unbounded.
    """
    def __init__(self, n_cols: int = 2):
        """

        """
        super().__init__()
        assert(n_cols > 0)

        self.n_cols = n_cols

        self.curr_row = 1
        self.curr_col = 0
    

    def get_index_row(self):
        """
        This method gets the index of the next row in the grid assuming that if there is a maximum number of columns and that value equals the current column index, then increment the current row index and reset the current column index.
        """
        if self.n_cols:
            if self.curr_col >= self.n_cols:
                self.curr_col = 0
                self.curr_row += 1
        return self.curr_row - 1


    def get_index_col(self):
        """
        This method gets the index of the next column in the grid assuming that if there is a maximum number of columns and that value equals the current column index, then increment the current row index and reset the current column index.
        """
        self.curr_col += 1
        return self.curr_col


    def __reset__(self):
        """
        Resets the current instance's row and column indices.
        """
        self.curr_row = 1
        self.curr_col = 0
