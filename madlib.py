print("""Welcome to Madlibs
Leave while you can""")
print("")
plural_noun = raw_input("Plural Noun: ")
noun1 = raw_input("Place: ")
name = raw_input("Name: ")
game = raw_input("Video Game: ")
adjective = raw_input("Adjective: ")
madlibs = ("""Hello! my name is %s and I love %s! Every day after work, I go to %s to play %s with the %s. We always have a %s time!""")
print (madlibs %(name,plural_noun,noun1,game,plural_noun,adjective))