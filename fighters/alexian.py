class AlexianMighty(core.StyleCard):
  name = 'Mighty'
  color = constants.RED
  range = bc.Range(0, 1)
  power = 1
  priority = 1
  armor = 1
  guard = 2
  
  def __init__(self, fighter):
    start.add(core.Optional(Retreat(1)))
    
for action in attack.start:
  action(acting_fighter, game_state)
  
class Action(object):
  def __call__(self, fighter, game):
    raise Exception('You need to override __call__ for this action to do anything!')
    
class Effect(object):
  def __call__(self, *args):
    raise Exception('You need to override __call__ for this action to do anything!')
    
