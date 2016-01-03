def bottle_song(i):
    while i>1:
      print str(i) +'bottles of beer on the wall,'+ str(i)+' bottles of beer.'
      print  'Take one down, pass it around,'+ str(i-1) +' bottles of beer on the wall'
      i=i-1

bottle_song(99)
