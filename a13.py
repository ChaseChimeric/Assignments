from gradedactivity import *


class Essay(GradedActivity):  #Extending GradedActivity

    def setGrammarPoints(self, grammar):  #Sets all passed through values into local variables
        self._grammar_points = grammar

    def setSpellingPoints(self, spelling):
        self._spelling_points = spelling

    def setLengthPoints(self, length):
        self._length_points = length

    def setContentPoints(self, content):
        self._content_points = content

    def gradeEssay(self):  #Adds all scores and initializes the grading process. (Calls setScore() from GradedActivity)
        _total_score = (self._grammar_points + self._spelling_points + self._length_points + self._content_points)
        self.setScore(_total_score)


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Main module for code
    """
    essay = Essay()  #Creating object essay based on class Essay()

    print('Please enter the student\'s points for grammar (up to 30 points): ')     #Gets values for each category
    essay.setGrammarPoints(int(input()))
    print('Please enter the student\'s points for spelling (up to 20 points): ')
    essay.setSpellingPoints(int(input()))
    print('Please enter the student\'s points for correct length (up to 20 points): ')
    essay.setLengthPoints(int(input()))
    print('Please enter the student\'s points for content (up to 30 points): ')
    essay.setContentPoints(int(input()))
    essay.gradeEssay()  #Initiates the grading methods of GradedActivity in Essay
    print(f'Student\'s overall points are: {essay.getScore()}\n')  #Prints score and letter grade
    print(f'Student\'s overall grade is: {essay.getGrade()}\n')    #Methods from GradedActivity


if __name__ == "__main__":
    main()
