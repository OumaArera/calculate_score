# **Score Calculator**

### How it works:

This Python script `calculate_score` is designed to calculate the scores of participants in a competitive eating competition based on the quantities of different types of food they consume. It then generates a scoreboard listing participants' names along with their scores, sorted first by score in descending order and then by name in ascending order.

The function `calculate_score` takes a list of dictionaries representing participants as input. Each dictionary contains the name of the participant along with the quantities of chicken wings, hamburgers, and hotdogs they consumed.

It assigns point values to each type of food item:
- Chickenwings: 5 points
- Hamburgers: 3 points
- Hotdogs: 2 points

For each participant, it calculates the score by multiplying the quantity of each food item consumed by its corresponding point value, and then summing up the total score.

The scores are then sorted first by score (in descending order) and then by name (in ascending order) using Python's `sort` method and a custom sorting key.

Finally, it returns a list of dictionaries containing each participant's name and their corresponding score.

### Example usage:

```python
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = calculate_score(participants)
print(scoreboard)
```

This will output a scoreboard with participants' names and their calculated scores, sorted as described above.

### Developer and License:

- Developed by John Ouma
- This project is licensed under the MIT License.