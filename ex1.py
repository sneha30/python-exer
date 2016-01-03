def max2(m,n):
  if m>n:
	return m
  else:
    return n


print max2(9,5)

# exercise 2
def max_of_three(m,n,q):
  if m>n & m>q:
	return m
  elif n>m & n>q:
	return n
  else:
	return q

print max_of_three(25,26,27)
print max2(28,max2(24,32))
print max(28,24,32)
# length of a string 

a = 'Happy'
def length_of_string(y):
  
  c=0
  for _ in a:
  	c=c+1
  return c

print length_of_string(a)

# to predict if the character is an vowel


def vowel_is(g):
  if g in ('aeiou'):
   return True
  else:
   return False

print vowel_is('f')

# string translation

def trans(d):
  s = ''
  for g in d:
   if g not in ('aeiou'):
    s += g + "o" + g
   else:
   	s += g
  print s

trans("this is fun")

def sum_add(f,g,h,i):
  x=f+g+h+i
  print x
sum_add(1,2,3,4)

def mul_no(t):
  c=1
  for i in t:
  	 c *= i
  return c

print mul_no([1,2,3,4])

def string_rev(x):
  p = len(x)
  n = ''
  while p>0:
    n= n+x[p-1]
    p=p-1
  print n

string_rev('Happy')
  	
def repeat_print(c,n):
  print c*n

repeat_print(5,'s')
  	


def guess (x):
  guess_no = x
  while guess_no != 5:
    if (guess_no >5):
      print 'too high'
      guess_no = input('Enter new value')
    elif guess_no <5:
      print 'too low'
      guess_no = input('Enter new value')
    else:
      print 'you win'
      break
print 'Game Over'

#guess(8)

def his_star(x):
  for i in x:
     print i * '*'

his_star([4,9,7])

#histogram([4,7,9])



# max value in a list of numbers
def max_in_list(x):
  max1 = 0 
  for i in x:
    if i> max1:
      max1 = i
  print max1 

max_in_list([3,6,7,8])



def longest_word(x):
  len_word = 0
  long_word=""
  for i in x:
    if len(i)>len_word:
      len_word =len(i)
      long_word=i
      
  print long_word
  print len_word
longest_word(['happy','joy','fair'])



def sen_palindrome(x):
  x = x.lower()
  #x.isalpha()
  x = x.replace("  ':.","")
  y= x[::-1]
  print x
  print y 
  if x==y:
    print "It's a palindrome"
  else:
    print "It's not a palindrome"

sen_palindrome("Go hang a salami I'm a lasagna hog.")
    
