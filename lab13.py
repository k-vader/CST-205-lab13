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

# Create a dictionary to use with input function. We can use the keys
# from the dictionary to prompt the user for specific word types in the
# input function
userWords = {"adjective": "", "number": ""} 
    		
# Input function 

    
def getInput(dict):
  # TODO: Add some validation to prevent empty strings
  for key in dict:
    dict[key] = requestString("Enter a " + key)
    
