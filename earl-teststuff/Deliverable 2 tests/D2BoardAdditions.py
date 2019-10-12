    def setBoardToState(self, tiles, movecount,addcount):

        rows = config.BOARDHEIGHT
        columns = config.BOARDWIDTH
        self.board = np.zeros(shape=(rows, columns))
        self.board = self.board.astype(int)
        for tile in tiles:
            self.setTile(tile[1],tile[0])
        self.moveCounter = movecount
        self.addCounter = addcount

    def aiSetTile(self,entry,x,y):
        letter = self.LETTERS[y]
        num = str(config.BOARDHEIGHT -x)
        pos = letter+num
        if(self.board[x][y] != 0):
            return False
        self.board[x][y] = entry
        self.used_tiles.append((pos,entry))
        self.addCounter -= 1
        return True #to remove

    
    def aiRemoveTile(self,x,y):
        self.board[x][y] = 0
        self.used_tiles.pop() 

        self.addCounter += 1 

    def getNeighbours(self,position):
        row = self.LETTERS.index(position[0].upper())
        column = config.BOARDHEIGHT - int(position[1:])
        open_cell_list = []
        for y in range(-1, 2):
            relative_column = column + y
            if(relative_column >= config.BOARDHEIGHT or
                    relative_column < 0):
                continue
            for x in range(-1, 2):
                relative_row = row + x
                if(relative_row >= config.BOARDWIDTH or
                        relative_row < 0):
                    continue
                if self.board[relative_column][relative_row] == 0:
            
                    open_cell_list.append(self.LETTERS[relative_row] + str(config.BOARDHEIGHT - relative_column))
        return open_cell_list


        