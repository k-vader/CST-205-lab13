# Ken Vader
# Ngoan Nguyen
# Chris Pina
# Lab 11
# 12/1/2015
# LAB 13, MAD LIBS

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
    
# Input function 
#    
def getInput(inputCount):
  wordsRemaining = inputCount  
  while(wordsRemaining > 0):
    inputString = requestString("Enter a word (%d left), or enter 'Exit'" % wordsRemaining)
    if inputString.lower() == "exit":
      reset()
      return false
    elif len(inputString) > 0:
      wordsRemaining -= 1
      userArray.append(inputString)
  return true

# This method accepts text and randomly removes content, leaving a "[index]" in its place
# @param text - the input text
# @param minLength - Ignores words that are less than the specified length (good for ignoring a, is, or, etc...)
# @param percentCoverage - Frequency of replacement, IE: .1 would be 10% of the sentence is omitted
# Example, input "This is a very nice sentence"
# return, "This is a [0] nice [1]"
def blankOutText(text, minLength, percentCoverage):
  totalWords = text.split()
    
  # determines how many times we should iterate, depending on size of string
  timesToIterate = max(1, int(percentCoverage * len(totalWords)))
  
  global userInputCount
  didFindWord = false
  for i in range(0, timesToIterate):
    randomIndex = random.randint(0, len(totalWords)-1)
    word = totalWords[randomIndex]
    # if the word meets the min length, and does not start with [, we replace
    if len(word) >= minLength and word[0] != "[":
      totalWords[randomIndex] = "[" + str(randomIndex) + "]"
      userInputCount += 1
      didFindWord = true
      
  # if we couldn't find a word, error out
  if not didFindWord:
    printNow("Sample too short, try a longer sentence!")
    return "exit:"
    
  returnString = " " .join(totalWords)
  return returnString
  
# This method accepts a string and replaces the marked words with items from an array
# 
def replaceTextWithArrayOfWords(text, array):

  splitWords = text.split()
  currentIndex = 0 # keeps track of the index of our words
  wordCount = 0 # keeps track of the ocurrence of the found word
  for word in splitWords:
    if word[0:1] == "[":
      splitWords[currentIndex] = array[wordCount].upper()
      wordCount += 1
    currentIndex += 1

  return " " .join(splitWords)

def reset():
  global userInputCount
  userInputCount = 0
  global userArray
  userArray = []
      
def madLibs():

  minLength = 3 # Use this to filter out short words
  percentCoverage = .08 # percent replacement frequency, 1 is the most
  text = blankOutText(story, minLength, percentCoverage)          
  if text == "exit:":
    reset()
  else:
    printNow("\n------\nMad Lib Before:\n %s" % text)  
    inputSuccess = getInput(userInputCount)
    # now let's replace our text with the user's words
    if inputSuccess:
      final = replaceTextWithArrayOfWords(text, userArray)
      printNow("------\nMad Lib After:\n %s" % final)
      
  reset() # resets the global variables