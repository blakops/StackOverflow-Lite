class Answers():

    answers = []

    def __init__(self, id, owner, topic, title, desc):
        self.id = id
        self.owner =owner
        self.topic = topic
        self.title = title
        self.desc = desc

    def add_answer(self, Answer):
        self.answers.append(Answer)


    def delete_answers(self, Answer):
        self.answers.remove(Answer)