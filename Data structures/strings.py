#Python Basics revision
#strings

model_summary = "This At model predicts stock trends"
predict_message = "AI is fun"

#Multi line printing
ai_response = """Hello there!
Im your AI assistant
"""

# \ is used to break a sentence
# \n new line
# \t tab

# Core String operations: Indexing, Slicing, Concatination
#Assessing strings
message = "GenAI is amazing!"
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
print("Version " + 4.0) #throws error
print("Version " + str(4.0)) # convert to string first


#Repeating strings
seperator = "🤖"
print(seperator * 5)
#🤖🤖🤖🤖🤖

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

#Strip method removes excess chars at beginning and end of a string
response = " 🤖Hello Human!🤖 "
print(response.strip())
print(response.strip(" 🤖")) # for specific chars
#lstrip for left
#rstrip for right

# Replace method
text = "ML is a critical component of modern AI. ML techniques are advancing rapidly"
updated_text = text.replace("ML", "machine learning")
print(updated_text)

text = "AI is the future, Embrace the future of AI!"
print(text.count("future")) # count displays how many times a a word occurs. It is case sensitive

statement = "AI breakthrough at every step"
words = statement.split() #Splits a string by spaces into list of different words
print(words)

terms = ["AI", "ML", "GenAI", "LLM", "NLP"]
buzzwords = ", ".join(terms)
print(buzzwords)

# Remove prefix
url = "https://example.com"
cleaned_url = url.removeprefix("https://") # remove defined suffix
print(cleaned_url)

filename  = "state_of_ai.pdf"
cleaned_filename = filename.removesuffix(".pdf")
print(cleaned_filename)


# Formatted strings: using F-strings for slean output
model_name = "GPT"
version = 4
print("Hello from " + model_name + "-" + str(version) + "!")
#Using this method is clunky and can cause confusion
#Using f string is better
print(f"Hello from {model_name}-{version}")

# Good for evaluating expressions as well
token_used = 123
cost_per_token = 0.001
total_cost = f"{token_used * cost_per_token:.4f}" #:.4f specifies 4 decimal places
print(f"Total cost for this message: {total_cost}")

# F-stringd for debbuging
name, age = "Alice", 30
print(f"Your name is {name} and your age is {age}")
print(f"Your name is {name=} and your age is {age=}") # = print variable and value
