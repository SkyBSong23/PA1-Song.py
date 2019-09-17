print ("Have you ever wondered how manny sheets of standard 4a paper you could fit on your wall?\n")
print ("Lets start by plugging in the height and length of your wall\n")

height = int(input ("enter the height of the wall: "))
length = int(input ("enter the length of the wall: "))
NumOfPaper = (height * length)/ 636.7
print ("Your wall can fit", NumOfPaper, "sheets of paper ont he wall!" )

