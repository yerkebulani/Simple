from Question import Questions

from random import shuffle

class Test(Questions):
    '''
        String [] options
        int numOfOptions
        Char [] labels
    '''

    def __init__(self, **kwargs):
        super().setDescription(kwargs.get('description', ''))
        super().setAnswer(kwargs.get('answer', ''))

        self.options = self.shuffle_options(kwargs.get('options', []))
        self.numOfOptions = len(kwargs.get('options', []))
        self.labels = [chr(char) for char in range(65, 65 + len(kwargs.get('options', [])) + 1)]

    def setOptions(self, options):
        self.shuffle_options(options)
        self.options = options
        self.numOfOptions = len(options)
    
    def getOptionAt(self, k):
        return self.options[k]

    def __str__(self):
        string = super().getDescription()
        for i in range(0, self.numOfOptions):
            string += '\n' + self.labels[i] + ') ' + self.options[i]
        return string

    @staticmethod
    def shuffle_options(arr):
        shuffle(arr)
        return arr