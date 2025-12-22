
import random

def play(player1, player2, num_games, verbose=False):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0

    for _ in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        if p1 == p2:
            result = "Tie"
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_score += 1
            result = "Player 1 wins"
        else:
            p2_score += 1
            result = "Player 2 wins"

        if verbose:
            print(p1, p2, result)

        p1_prev, p2_prev = p1, p2

    print("Player 1:", p1_score, "Player 2:", p2_score)
    return p1_score, p2_score
