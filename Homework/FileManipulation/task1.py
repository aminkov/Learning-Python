import time;

# def backup(src, dest):
#   """Backup files in src folder into dest folder.
#     Do not remove the files in source folder.
#     To each file attach suffix with curent timestamp in the form
#     '2018-04-12_18-30-45'

#   Args:
#       src (string): Source folder
#       dest (string): Destination folder

#   Example:
#     /src/track5.mp3 => /dest/track5.mp3_2018-04-12_18-30-45
#   """



def get_timestamp():
  #get the current local date-time
  cldt = datetime.datetime.today()
  # get the timestamp as a string with given format
  timestamp = datetime.datetime.strftime(cldt, '%Y-%m-%d_%H_%M_%S')
  return timestamp


