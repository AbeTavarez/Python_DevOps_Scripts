import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    new_file = open(filename, "w")
    path = os.path.join(os.getcwd(), filename)
    timestamp = os.path.getmtime(path)
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp)
    str_date = str(date)
    date_list = str_date.split(" ")
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(date_list[0]))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
