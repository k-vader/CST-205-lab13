import time
import random

userInputCount = 0

story = """
		As more than 100 stout and bearded men, all dressed in various shades of red and green,
		board a train to go rattling through the Michigan countryside for no apparent reason, I
		turn to Tom Valent and ask, "Why?"
		It's a loaded question. One that has been percolating for days.
		Why, in mid-October, would Valent load his entire Santa school onto charter buses and drive
		them 45 minutes to Huckleberry Railroad, a tourist attraction that is still very obviously 
		in the midst of celebrating Halloween?
		Why, the day before, had his student Santas spent hours learning about the legend of Santa 
		Claus -- from his birth in Patara to the names of all his elves? Why did Valent have them 
		practice reindeer-handling and sleigh-driving and toy-making?
		I mean, come on. Doesn't Santa Claus use Amazon like the rest of us?
		"Do you know the movie 'The Polar Express'?" Tom asks, answering my question with a question.
		"""
userArray = []
    
# Create a dictionary to use with input function. We can use the keys
# from the dictionary to prompt the user for specific word types in the
# input function
userWords = {"adjective": "", "number": ""} 
    		
# Input function 
#    
def getInput(dict):
  # TODO: Add some validation to prevent empty strings
  for key in dict:
    dict[key] = requestString("Enter a " + key)

# This method accepts text and randomly removes content, leaving a "[index]" in its place
# @param text - the input text
# @param minLength - Ignores words that are less than the specified length (good for ignoring a, is, or, etc...)
# @param percentCoverage - Frequency of replacement, IE: .1 would be 10% of the sentence was omitted
# Example, input "This is a very nice sentence"
# return, "This is a [0] nice [1]"
def replaceText(text, minLength, percentCoverage):
  totalWords = text.split()
    
  # determines how many times we should iterate, depending on size of string
  timesToIterate = max(1, int(percentCoverage * len(totalWords)))
  
  global userInputCount
    
  for i in range(0, timesToIterate):
    randomIndex = random.randint(0, len(totalWords)-1)
    word = totalWords[randomIndex]
    
    # if the word meets the min length, and does not start with [, we replace
    if len(word) >= minLength and word[0] != "[":
      totalWords[randomIndex] = "[" + str(randomIndex) + "]"
      userInputCount += 1
 
  returnString = " " .join(totalWords)
  return returnString
  
# This method accepts a string and replaces the marked words with items from an array
# 
def replaceTextWithArrayOfWords(text, array):

  newString = ""
  foundIndex = 0
  
  splitWords = text.split()
  currentIndex = 0 # keeps track of the index of our words
  wordCount = 0 # keeps track of the ocurrence of the found word
  for word in splitWords:
    if word[0:1] == "[":
      splitWords[currentIndex] = array[wordCount]
      wordCount += 1
    currentIndex += 1

  return " " .join(splitWords)

def reset():
  global userInputCount
  userInputCount = 0
  global userArray
  userArray = []
      
def test():
  text = replaceText("The quick brown fox jumped over the big and lazy cat", 3, .25)
  printNow("Mad Lib: %s" % text)
  for i in range(0, userInputCount):
    inputString = requestString("Enter a word")
    userArray.append(inputString)

  # now let's replace our text with the user's words
  final = replaceTextWithArrayOfWords(text, userArray)
  printNow(final)
  reset() # resets the global variables