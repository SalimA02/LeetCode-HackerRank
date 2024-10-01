def climbingLeaderboard(ranked, player):
    unique_ranked = sorted(set(ranked), reverse=True)
    result = []
    n = len(unique_ranked)
    i = n - 1
    
    for score in player:
        while i >= 0 and score >= unique_ranked[i]:
            i -= 1
        result.append(i + 2)
    
    return result
