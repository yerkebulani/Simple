from Question import Questions

class FillIn(Questions):
    '''
        No own fields
    '''

    def __init__(self, **kwargs):
        super().setDescription(self.clear_description(kwargs.get('description', '')))
        super().setAnswer(kwargs.get('answer', '').lower())

    def __str__(self):
        string = super().getDescription()
        return string

    @staticmethod
    def clear_description(desc):
        '''
            Clears the string from '{blank}'
        '''

        sep = desc.find('{blank}')
        new_description = desc[:sep] + '_______' + desc[sep + 7:]
        return new_description