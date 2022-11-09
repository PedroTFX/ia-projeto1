

class JogoBT_XX:

    NO_PIECE = "."
    WHITE_PIECE = "W"
    BLACK_PIECE = "B"

    default_initial =[[2,2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2,2],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1],[1]]

    def JogoBT_XX(self, to_move = 1, initial = default_initial):
        self.board_state = initial

    def actions(self, state):
        columns = "abcdefgh"
        actions = []
        pieces_pos = []

        print(state[0][0])

        x = 0
        y = 0
        while(y < 8):
            while(x < 8):
                if state[y][x] == self.WHITE_PIECE:
                    print(state[y + 1][x] == self.NO_PIECE)
                    if y < 7 and state[y + 1][x] == self.NO_PIECE:                      #forward                
                        actions.append(columns[x] + str(y + 1) + "-" + columns[x] + str(y + 2))
                    if y < 7 and x < 7 and not state[y + 1][x + 1] == self.WHITE_PIECE: #right
                        actions.append(columns[x] + str(y + 1) + "-" + columns[x + 1] + str(y + 2))
                    if y < 7 and x > 0 and not state[y + 1][x - 1] == self.WHITE_PIECE: #left
                        actions.append(columns[x] + str(y + 1) + "-" + columns[x - 1] + str(y + 2))
                x += 1
            x = 0
            y += 1
        
        return sorted(actions)

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        
        print("--------------------------")
        x = 0
        y = 8
        while(y > 0):
            print(y,"|", end = '')
            while(x < 8):
                if x < 7:
                    print(state[y - 1][x]," ", end = '')
                else:
                    print(state[y - 1][x])
                x += 1
            x = 0
            y -= 1   
        print("--------------------------")
        print(" |a b c d e f g h ")
        #print("--NEXT PLAYER: ", ("W" if(state[8] == 1)else "B"))

 

j = JogoBT_XX()
default_initial =[["W","W","W","W","W","W","W","W"],
                  ["W","W","W","W","W","W","W","W"],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  ["B","B","B","B","B","B","B","B"],
                  ["B","B","B","B","B","B","B","B"]]
print(j.actions(default_initial))
j.display(default_initial)

