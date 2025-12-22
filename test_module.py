
import random

def quincy(prev_play):
    return "R"

def abbey(prev_play, counter=[0]):
    counter[0] += 1
    return ["R","P","S"][counter[0] % 3]

def kris(prev_play):
    return random.choice(["R","P","S"])

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    return random.choice(["R","P","S"])
