for beer in range(99, 0, -1):
  if beer > 1:
     print (beer, "bottles of beer on the wall,", beer, "bottles of beer.")
     if beer > 2:
        s = str(beer - 1) + " bottles of beer on the wall."
     else:
        s = "1 bottle of beer on the wall."
  elif beer == 1:
     print ("1 bottle of beer on the wall, 1 bottle of beer.")
     s = "no more beer on the wall!"
  print ("Take one down, pass it around,", s)
  print ("--")