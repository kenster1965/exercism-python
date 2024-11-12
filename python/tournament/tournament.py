"""
Tally the results of a small football competition.
"""


def tally(rows):
    """
    Create a table of the game results

    :param rows: list - A list of strings representing the game results.
    :return: list - A list of strings representing the table of the game results.
    """
    teams = {}
    print(f"{rows=}")
    # Loop through the rows and update the teams dictionary
    for row in rows:
        team1, team2, result = row.split(";")
        # print(f"{team1=}, {team2=}, {result=}")
        # Add the teams to the dictionary if they are not already there
        if team1 not in teams:
            teams[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if team2 not in teams:
            teams[team2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        # Update the teams dictionary with the results
        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1
        if result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1
        elif result == "loss":
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
            teams[team1]["L"] += 1
        elif result == "draw":
            teams[team1]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["D"] += 1
            teams[team2]["P"] += 1

    # Sort the teams dictionary by points then alphabetically
    teams = dict(sorted(
        teams.items(),
        key=lambda item: (-item[1]['P'], item[0])
    ))

    # Loop through each team and format the table
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in teams.items():
        row = (
            f"{team:<30} | "
            f"{stats['MP']:>2} | "
            f"{stats['W']:>2} | "
            f"{stats['D']:>2} | "
            f"{stats['L']:>2} | "
            f"{stats['P']:>2}"
        )
        table.append(row)
    return table
