from random import randint


class Sample_Text:
    def __init__(self):
        with open(file='samples.txt', mode='r') as file:
            content = file.readlines()
        self.text = content[randint(0, len(content) - 1)]

    def __str__(self):
        return self.text
