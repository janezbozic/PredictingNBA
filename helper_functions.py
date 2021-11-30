def calculate_elo(elo_team1, elo_team2, win_lose, point_difference, win_away):

    e_team = 1 / (1 + 10 ** ((elo_team2 - elo_team1) / 400))
    s_team = win_lose
    k = 20 * ((point_difference + (3.5 * win_away * win_lose)) ** 0.8) / (7.5 + 0.006*(abs(elo_team1 - elo_team2)))

    new_elo = elo_team1 + k * (s_team - e_team)

    return new_elo
