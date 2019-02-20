from mycroft import MycroftSkill, intent_file_handler
import subprocess


class Spinturtleright(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spinturtleright.intent')
    def handle_spinturtleright(self, message):
        self.speak_dialog('spinturtleright')
        s = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 1.0]' '[0.0, 0.0, -0.5]'"
        subprocess.call([s],shell=True)

def create_skill():
    return Spinturtleright()

