#Python Basics revision
#strings

model_summary = "This At model predicts stock trends"
predict_message = "AI is fun"

#Multi line printing
ai_response = """Hello there!
Im your AI assistant
"""

#\ is used to break a sentence

# Core String operations: Indexing, Slicing, Concatination
#Assessing strings
message = "GenAI is amazind!"
print(message[0])
print(message[5])
print(message[-1])
print(message[7])

#Becareful of index out of bounds error
print(message[30])
#Use bounds checking
n = len(message)
print(message[n-1])

#Concatination
greeting = "Hello"
role = "AI enthusiast"
print(greeting + role)

#Cannot concat a string with a number
print("Version " + 4.0) #throw erroe
print("Version " + str(4.0)) # convert to string first


#Repeating strings
seperator = "🤖"
print(seperator * 5)

#Slicing
tech = "Machine learning"
print(tech[0:7])

#string[start:stop]
#string[start:stop:step]

print(tech[:7])
print(tech[8:])
print(tech[-4:])
print(tech[8:100]) # does not throw an error
print(tech[0:14:2]) # Adds step to skip over characters
print(tech[::-1]) # Reverse string

#COMMON String METHODs

x = 10
s = "abc" 
print(type(x), type(s))
#x and s are members of string method

model_output = "ai is the future"
print(model_output.upper())
print(model_output.lower())
#Since strings are immutable, both methods dont modify the original string but create a new copy
print(model_output)

#Strip method removes access chars at beginning and end of a string
response = " 🤖Hello Human!🤖 "
print(response.strip())
print(response.strip(" 🤖")) # for specific chars

text = "ML is a critical component of modern AI. ML techniques are advancing rapidly"
updated_text = text.replace("ML", "machine learning")

text = "AI is the future, Embrace the future of AI!"
print(text.count("future")) # count displays how many times a a word occurs. It is case sensitive