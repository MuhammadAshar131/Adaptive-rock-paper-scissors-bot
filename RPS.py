def player(prev_play, opponentHistory=[], myHistory=[]):

    if not prev_play:
        opponentHistory.clear()
        myHistory.clear()
        return "R"
        
    opponentHistory.append(prev_play)
    
    if len(opponentHistory) > len(myHistory):
        myHistory.append("R") 

    combinedPairs = [f"{m}{o}" for m, o in zip(myHistory, opponentHistory)]
    
    n = 2
    if len(combinedPairs) < n:
        myHistory.append("P")
        return "P"

    currentContext = "".join(combinedPairs[-n:])
    predictionCounts = {"R": 0, "P": 0, "S": 0}

    for i in range(len(combinedPairs) - n):
        context = "".join(combinedPairs[i : i + n])
        if context == currentContext:
            nextOppMove = opponentHistory[i + n]
            predictionCounts[nextOppMove] += 1
            
    predictedMove = max(predictionCounts, key=predictionCounts.get)
    if predictionCounts[predictedMove] == 0:
        predictedMove = max(set(opponentHistory), key=opponentHistory.count)

    idealResponse = {"R": "P", "P": "S", "S": "R"}
    nextMove = idealResponse[predictedMove]
    
    myHistory.append(nextMove)
    return nextMove
