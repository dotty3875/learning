"""In this exercise you will write a program for printing out grade statistics for a university course.

The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. 
The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there 
are two integers on each line, or the line is empty.

When the user types in an empty line, the program prints out statistics. They are formulated as follows:

The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, 
and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

The grade for the course is determined based on the following table:

exam points + exercise points	grade
0–14	0 (i.e. fail)
15–17	1
18–20	2
21–23	3
24–27	4
28–30	5
There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

Floating point numbers should be printed out with one decimal precision.

NB: this exercise doesn't ask you to write any specific functions, so you should not place any code within an if __name__ == "__main__" block. If any 
functionality in your program is e.g. in the main function, you should include the code calling this function normally, and not contain it in an if block 
like in the exercises which specify certain functions."""

# Write your solution here
def examScores(): # takes the initial exam scores
    scores = " "
    helper = 0
    scoreTotal = []
    while scores != "":
        scores = input("Exam points and exercises completed: ") # str at the moment, need to convert
        scoreTotal += scores.split()
    for i in scoreTotal: # converts each value in list into int value instead of string
        scoreTotal[helper] = int(i)
        helper += 1

    return scoreTotal

def totalPoints(scoreTotal): 
    helper = 1
    scoreSum = []
    scoreSum += scoreTotal
    for i in scoreSum[1::2]: # divides exercise points into 10% of what was input
        scoreSum[helper] = i // 10 # list[] = "something" - replaces it with that. replacing old pre-divided value with divided value (real value of exercise points)
        helper += 2
    helper = 0
    for i in scoreSum: # adds the divided exercises points to the exam points to get the real test values
        scoreSum[helper] += scoreSum[helper + 1]
        scoreSum.pop(helper + 1)
        helper += 1
        
    return scoreSum

def statistics(realScores, scoreTotal): # finds the average and pass percentage 
    average = sum(realScores) / len(realScores) 
    average = f"{average:.1f}" # rounded to 1 decimal point
    fail = 0
    passes = 0 
    helper = 0
    for i in realScores:
        if i < 15 or scoreTotal[helper] < 10:  # instant fail if less than 10 exam points
            fail += 1
        else: 
            passes += 1
        helper += 2 # helper tracks only exam points not exercise points
    passPercent = (passes / (passes + fail)) * 100 # does the % calculation
    passPercent = f"{passPercent:.1f}" # rounded to 1 decimal point

    return average, passPercent

def distribution(realScores, scoreTotal): # function for the visual grading distribution
    helper = 0
    grade5 = "5: "
    grade4 = "4: "
    grade3 = "3: "
    grade2 = "2: "
    grade1 = "1: "
    grade0 = "0: "
    for i in realScores: # iterates through all scores, grades accordingly 
        if i <= 14 or scoreTotal[helper] < 10: # instant fail if less than 10 exam points
            grade0 += "*"
        elif i <= 17 and i >= 15: 
            grade1 += "*"
        elif i <= 20 and i >=18:
            grade2 += "*"
        elif i <= 23 and i >= 21:
            grade3 += "*"
        elif i <= 27 and i >= 24:
            grade4 += "*"
        elif i >= 28: 
            grade5 += "*"
        helper += 2 # helper tracks only exam points not exercise points

    print("Grade distribution:\n", grade5, "\n", grade4, "\n", grade3, "\n", grade2, "\n", grade1, "\n", grade0 )

def main():
    scoreTotal = examScores()
    realScores = totalPoints(scoreTotal)
    average, passPercent = statistics(realScores, scoreTotal) # tuple 
    print("Statistics:") # these 3 prints could fit in printIntro() function to shorten main() block but not required
    print("Points average:", average)
    print("Pass percentage:", passPercent)
    distribution(realScores, scoreTotal)

main()