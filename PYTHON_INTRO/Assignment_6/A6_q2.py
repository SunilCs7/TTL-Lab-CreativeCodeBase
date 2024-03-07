def create_phone_directory():
  """
  Creates a phone directory by prompting the user for names and numbers,
  and returns a dictionary containing the data.
  """
  phone_directory = {}
  while True:
    name = input("Enter a friend's name (or 'q' to quit): ")
    if name.lower() == 'q':
      break
    number = input("Enter their phone number: ")
    phone_directory[name] = number
  return phone_directory

def print_phone_directory(phone_directory):
  """
  Prints the phone directory in a sorted format.
  """
  print("**Phone Directory:**")
  for name, number in sorted(phone_directory.items()):
    print(f"{name}: {number}")

# Create the phone directory
phone_directory = create_phone_directory()

# Print the phone directory
print_phone_directory(phone_directory)
