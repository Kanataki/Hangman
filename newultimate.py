import random
words = [line.strip() for line in open("words.txt")]
word = random.choice(words)

def game():
    wordlist = list(word)
    dashes = list('_'*len(word))
    print "".join(wordlist)
    print "".join(dashes)
    #play = "yes"4
    dick_figures = 0
    hang_figures = [
        """
  ______
 |
 |
 |
 |
 |
""",
 """
  ______
 |      |
 |
 |
 |
 |
""",
 """
  ______
 |      |
 |      0
 |
 |
 |
""",
  """
  ______
 |      |
 |      0
 |     / \
 |
 |
""",
 """
  ______
 |      |
 |      0
 |     / \\
 |
 |
""",
  """
|      |      
|      0 
|     /|\\ 
|      
|
""",
  """
|      |      
|      0 
|     /|\\ 
|     /  
|
""",
        
  """ 
 ______
|      |      
|      0 
|     /|\\ 
|     / \\ 
|
"""






        ]
    trials = 0
    while trials <= 8:
        guess = raw_input("guess a letter in word: ")
        if guess in wordlist:
            i = len(wordlist) - 1
            while i >= 0:
                if wordlist[i] == guess:
                    dashes[i] = guess
                    print "".join(dashes)
                    print "voila! one guess down, more to go!"
                i -=1

        else:
            print dick_figures,"dick_figures"
            print hang_figures[trials]
            print "sorry mate, try again"
            
            trials += 1
        if trials== 8 or dashes == wordlist:
          print "Game over"
          print "the word is", word
          break

game()
            

            
            
