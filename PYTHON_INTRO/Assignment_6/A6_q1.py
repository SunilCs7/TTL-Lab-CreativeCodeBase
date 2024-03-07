def create_winner_dictionary():
  """
  Creates a dictionary containing names of competition winner students as keys and number of their wins as values.

  Returns:
    A dictionary with student names as keys and their win counts as values.
  """

  # Initialize an empty dictionary
  winners = {}

  # Get input for student names and their wins
  while True:
    name = input("Enter student name (or 'q' to quit): ")
    if name.lower() == 'q':
      break

    wins = int(input("Enter number of wins for {}: ".format(name)))

    # Add the student and their wins to the dictionary
    winners[name] = wins

  return winners

# Create the dictionary and print it
winner_dict = create_winner_dictionary()
print(winner_dict)

