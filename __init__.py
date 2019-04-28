from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'jj2020'
LOGGER = getLogger(__name__)

class GoodMorningSkill(MycroftSkill):

  def __init__(self):
    super(GoodMorningSkill, self).__init__(name="GoodMorningSkill")
    
  def initialize(self):
    super(GoodMorningSkill, self).initialize()

  def handle_GoodMorning_intent(self, message):
    self.speak_dialog("goodmorning")

def create_skill():
return GoodMorningSkill()
