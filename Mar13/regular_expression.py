import re

# the string to search with regex:
user_email = "pr34efix@domain.erte436-"

# the regex to find if the userEmail contains '@' symbol:
regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# do the match test:
if regex.search(user_email):
  print("Match!")
else:
  print("No match!")