from repo.repo import BoardException
from repo.repo import WinException
from repo.repo import Repository

"""
The code here focuses on providing a representation of the "connect four" game board
"""


def start():
    connect4 = Repository()
    while True:
        try:
            print(connect4)
            x = input("Player step x=")
            connect4.player_step(int(x))
            if connect4.board_filled_checker():
                print("Board is filled! Game is over.")
                return
            ai_x = connect4.ai_step()
            print("AI moved on column " + str(ai_x))
            if connect4.board_filled_checker():
                print("Board is filled! Game is over.")
                return
        except BoardException as be:
            print(be)
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)
        except WinException as we:
            print(we)
            print(connect4)
            return


start()
