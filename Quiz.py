
from Test import Test
from FillIn import FillIn


class Quiz:
    '''
        String name
        Question [] questions
    '''

    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addQuestion(self, q):
        self.questions.append(q)

    def loadFromFile(self, filename):
        self.questions = []
        txt = open(filename, 'r').read()
        self.setName(filename.split('.')[0])
        question_texts = [qt for qt in txt.split('\n\n')]
        
        for qt in question_texts:
            qt = qt.split('\n')

            if '{blank}' in qt[0]:  # If question is FillIn type
                q = FillIn(description=qt[0], answer=qt[1])
                self.addQuestion(q)
            else:                    # If question is Test type
                q = Test(description=qt[0], answer=qt[1], options=qt[1:])
                self.addQuestion(q)


    
    def start(self, filename):
        self.loadFromFile(filename)

        corrects = 0

        print('========================================================\n')
        print('Welcome to \"' + self.getName() + '\" QUIZ!\n')
        print('--------------------------------------------------------\n')

        i = 1
        
        for question in self.questions:
            print(str(i) + '.' + str(question))
            print('- - - - - - - - - - - - - - -')
            attempts = 0
            if isinstance(question, Test):
                ans = input('Enter the correct choice: ')
                is_correct = False
                correct_type = False

                while not correct_type:
                    if len(ans) == 1:
                        if ord(ans) >= 65 and ord(ans) <= 90:
                            correct_type = True
                            break
                    if not correct_type:
                        ans = input('Invalid choice! Try again (Ex: A, B, ...): ')
                if question.getOptionAt(ord(ans)-65) == question.getAnswer():
                    print('Correct!\n')
                    corrects += 1
                else:
                    print('Incorrect!\n')
            else:
                ans = input('Type your answer: ')
                if ans.lower() == question.getAnswer():
                    print('Correct!\n')
                    corrects += 1
                else:
                    print('Incorrect!\n')
            i += 1
            
            print('--------------------------------------------------------\n')
        print('Correct Answers: ' + str(corrects) + '/' + str(len(self.questions)) + ' (' + str(corrects*100/len(self.questions)) + '%)')
        f = open("Scores.txt", 'a')
        print("Thank you!\n")
        f.write('\n' + input('Enter your name: ') + ' ' +str(corrects*100/len(self.questions)))

if __name__ == '__main__':
    quiz = Quiz()
    quiz.start("Quiz.txt")
