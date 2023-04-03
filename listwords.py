colors = ["green", "purple", "yellow", "red", "blue", "black", "fuchsia", "white", "olive", "orange"]

# List Comprehensio to create a new List of Words with odd number of characters
newlist = [len(color) for color in colors if len(color) % 2 != 0]

print(list(newlist))

  