from mycroft import MycroftSkill, intent_file_handler


class Spinturtleright(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spinturtleright.intent')
    def handle_spinturtleright(self, message):
        self.speak_dialog('spinturtleright')


def create_skill():
    return Spinturtleright()

