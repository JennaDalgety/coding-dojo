import re
def matchGame(regex):
  words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
  return [word for word in words if re.search(regex, word)]
print "1 - 'v': ",(matchGame(r'v'))
print "2 - 'ss': ",(matchGame(r'ss'))
print "3 - ends with 'e': ",(matchGame(r'e$'))
print "4 - contains two 'b's: ",(matchGame(r'(b\w)b'))
print "5 - contains two 'b's: ",(matchGame(r'b(\w)+b'))
print "6 - contains two 'b's: ",(matchGame(r'.*b.*b.*'))
print "7 - contains all vowels: ",(matchGame(r'(.?a.?e.?i.?o.?u.*)'))
print "8 - letters in 'regular expression': ",(matchGame(r'[a-z]+'))




# import re

# email regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+$)"