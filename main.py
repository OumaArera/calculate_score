def calculate_score(participants):
    # Define points for each food item
    points = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}

    # Calculate score for each participant
    scores = []
    for participant in participants:
        score = 0
        for food, value in participant.items():
            if food != 'name':
                score += points[food] * value
        scores.append({'name': participant['name'], 'score': score})

    # Sort scores by score (descending) and name (ascending)
    scores.sort(key=lambda x: (-x['score'], x['name']))

    return scores

# Example usage:
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = calculate_score(participants)
print(scoreboard)
