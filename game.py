class JogoBT_XX(Game):
    default_initial =[[2,2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2,2],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1]]

    def JogoBT_XX(self, to_move = 1, initial = default_initial):
        self.board_state = initial

    def actions(self, board_state):
        avail_actions = []


        #move

        #eat


        return avail_actions

    def result():

        #return board state

        return None

    def display(board):
        print("-----------------")
        print("8|", )

        return board

    def goal_test():
        return None



