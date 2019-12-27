import csv
file = open("Books.csv","w")
newrecord = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newrecord))
newrecord = "Rotten Milk, Slime. lego, 1900\n"
file.write(str(newrecord))
newrecord = "eye yam, stew. Peed, 1900\n"
file.write(str(newrecord))
newrecord = "Poopy Woopy, vs. SITX, 1900\n"
file.write(str(newrecord))
newrecord = "Blah, Wee. Pooey, 1900\n"
file.write(str(newrecord))
file.close()