# Slicing strings
text = "Hello my name is Anakin"
print(text[1:5])      # Prints characters from index 1 to 4 → "ello"
print(text[-5:-1])    # Prints characters from the 5th last to the 2nd last → "naki"
      
#-----------------------------------
# Concatenation (joining strings)
text1 = "RTX"
text2 = "A2000"
result = text1 + " " + text2
print(result)         # Prints "RTX A2000"

#-----------------------------------
# Splitting strings
splitext = "Hi, my name is Anakin! Skywalker"
result = splitext.split(",")
print(result)         # Splits the string at commas → ['Hi', ' my name is Anakin! Skywalker']
result = splitext.split("!")
print(result)         # Splits the string at exclamation marks → ['Hi, my name is Anakin', ' Skywalker']
#-------------------------------------
