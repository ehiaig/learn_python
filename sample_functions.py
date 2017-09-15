team_name = ["Team1", "Team2", "Team3", "Team4", "Team5", "Team6", "Team7", "Team8", "Team9"]
team_amount = [476, 1000, 675, 879, 765, 7655, 677.7, 76433, 76.988]

team_message = """Hi {name}!

Thank you for the BBB on {date}.
At the end, the team made {total}Ghc.

Have a great date!
"""

def message_function(names, amounts):
    messages=[]
    if len(names) == len(amounts):
        i = 0
        for name in names:
            new_msg = team_message.format(
                    name = name,
                    date = "some date",
                    total = amounts[i]

                )
            i = i+1
            print(new_msg)
message_function(team_name, team_amount)
