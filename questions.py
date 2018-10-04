class Question():


    questions = []

    def __init__(self, id, topic, title, desc):
        self.id = id
        self.topic = topic
        self.title = title
        self.desc = desc

    def ask_question(self, Question):
        self.questions.append(Question)


    def delete_question(self, Question):
        self.questions.remove(Question)
