# Format string
name = "Armitage"
surname = "Hux"
rank = "General"

# Using format() method to insert variables into a string
text = ''' 
{0} {1} {2}:
Today is the end of the Republic. The end of a regime that acquiesces to disorder. 
At this very moment in a system far from here, 
the New Republic lies to the galaxy while secretly supporting the treachery of the rogues of the Resistance. 
This fierce machine which you have built, 
upon which we stand will bring an end to the Senate, to their cherished fleet.
All remaining systems will bow to the First Order and will remember this as 
The last day of the Republic!'''.format(rank, name, surname)

print(text)   # Prints the full formatted speech

#-----------------------------------

# Taking user input for exam grades
midtermExam = float(input("Enter your Midterm grade: "))   # Input for midterm exam
finalExam = float(input("Enter your Final grade: "))       # Input for final exam
averageScore = (midtermExam + finalExam) / 2               # Calculating average

print(averageScore)   # Prints the average score
