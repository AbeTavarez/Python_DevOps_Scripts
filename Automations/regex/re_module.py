import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# NORMAL SERACH STRING LITERAL
print(re.search(r"aza", "plaza"))
print(re.search(r"aza", "bazaar"))

# ^ THE CARET SEARCH FOR  BEGGINING OF STRING
print(re.search(r"^x", "xenon"))

# SEARCH FOR (ANY CHAR) IN BETWEEN p.ng pattern
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

# case insensitive
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# * character classes
print("Pp ->", re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go!"))

# combinding ranges
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))

# * non letter characters

# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points
print(re.search(r"[^a-zA-Z ]", 'The sentence with spaces.'))

# * Search for two either or case
print(re.search(r"cat|dog", 'I like dogs'))
# match first case
print(re.search(r"cat|dog", 'I like both cats dogs.'))

# * find all
print(re.findall(r'cat|dog', "I like both cats and dogs."))
