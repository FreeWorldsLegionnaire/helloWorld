last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Creating list subject filled with classes

subjects = ["physics", "calculus", "poetry", "history"]

# list of grades for each class

grades = [98, 97, 85, 88]

#create a 2D list to combine subjects and grades

gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]
print(gradebook)

#Adding more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#Accessing a sublist in 2D list to change its index 1

gradebook[-1][-1] = 93 + 5
#print(gradebook)

#Using .remove() method

gradebook[2].remove(85)
#print(gradebook)

#Using .append() method
gradebook[2].append("Pass")
#print(gradebook)

#Using + operator to concatenate two 2D lists

last_semester_gradebook = [["drama", 50], ["math", 94]]

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
