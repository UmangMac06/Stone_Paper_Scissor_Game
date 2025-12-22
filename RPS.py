
import random

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()
        return "R"

    opponent_history.append(prev_play)

    counter = {"R": "P", "P": "S", "S": "R"}

    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    last_5 = opponent_history[-5:]
    prediction = max(set(last_5), key=last_5.count)

    return counter[prediction]
