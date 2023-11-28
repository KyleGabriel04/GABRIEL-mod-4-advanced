'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {
        "@bongolpoc": {"first_name": "Joselito",
                       "last_name": "Olpoc",
                       "following": [
                       ]
                       },
        "@joaquin": {"first_name": "Joaquin",
                     "last_name": "Gonzales",
                     "following": [
                         "@chums", "@jobenilagan"
                     ]
                     },
        "@chums": {"first_name": "Matthew",
                   "last_name": "Uy",
                   "following": [
                       "@bongolpoc", "@miketan", "@rudyang", "@joeilagan"
                   ]
                   },
        "@jobenilagan": {"first_name": "Joben",
                         "last_name": "Ilagan",
                         "following": [
                             "@eeebeee", "@joeilagan", "@chums", "@joaquin"
                         ]
                         },
        "@joeilagan": {"first_name": "Joe",
                       "last_name": "Ilagan",
                       "following": [
                           "@eeebeee", "@jobenilagan", "@chums"
                       ]
                       },
        "@eeebeee": {"first_name": "Elizabeth",
                     "last_name": "Ilagan",
                     "following": [
                         "@jobenilagan", "@joeilagan"
                     ]
                     },
    }
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            relationship = " is friends with"
        else:
            relationship = " is followed by"
    else:
        if from_member in social_graph[to_member]["following"]:
            relationship = " is a follower of"
        else:
            relationship = " has no relationship with"

    return relationship



def tic_tac_toe(board):
    '''Tic Tac Toe.
    15 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tictactoe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    board1 = [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['O', '', 'X'],
    ]

    board2 = [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['', 'O', 'X'],
    ]

    board3 = [
        ['O', 'X', 'O'],
        ['', 'O', 'X'],
        ['X', 'X', 'O'],
    ]

    board4 = [
        ['X', 'X', 'X'],
        ['O', 'X', 'O'],
        ['O', '', 'O'],
    ]

    board5 = [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['X', '', 'O'],
    ]

    board6 = [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['X', '', ''],
    ]

    board7 = [
        ['X', 'X', 'O', ''],
        ['O', 'X', 'O', 'O'],
        ['X', '', '', 'O'],
        ['O', 'X', '', '']
    ]
        # Check horizontal lines
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            print(f"{set(row)} is the winner")
            return

        # Check vertical lines
    for col in zip(*board):
        if len(set(col)) == 1 and col[0] != '-':
            print(f"{set(col)} is the winner")
            return

        # Check main diagonal
    if len(set(board[i][i] for i in range(len(board)))) == 1 and board[0][0] != '-':
        print(f"{set(board[i][i] for i in range(len(board)))} is the winner")
        return

        # Check anti-diagonal
    if len(set(board[i][len(board) - 1 - i] for i in range(len(board)))) == 1 and board[0][len(board) - 1] != '-':
        print(f"{set(board[i][len(board) - 1 - i] for i in range(len(board)))} is the winner")
        return

    print("There is no winner")



def eta(first_stop, second_stop, route_map):
    '''ETA.
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

    legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
    travel_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        leg = (current_stop, second_stop)

        if leg not in route_map:
            print("Error: Invalid route.")
            return

        travel_time += route_map[leg]["travel_time_mins"]
        current_stop = leg[1]

    return f"Estimated Time of Arrival: {travel_time} mins"