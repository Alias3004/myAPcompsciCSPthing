#narrator will be sarcastic sometimes (if you keep trying to go north when you can't
#suddenly says 'fine. you go north' (alternatives between falling and dying and
#walking into a wall and etc)
global command_string_help
command_string_help = ''' 
#list of commands 
a - apply (use)? 
b - backstab? back?
c - cheat? climb?
d - drop (followed by 'drop what' prompt)
e - east 
f - fail? 
g - get (followed by 'get what' prompt, only will be so many objects) 
h - help (list commands) 
i - inventory 
j - jump 
k - attack (kill)
l - look 
m - message log?
n - conditional, either works as no (when prompted for a yn answer) or north 
o - open 
p - place?
q - question (talk function? hint?) 
r - repeat? 
s - south 
t - talk (allows you to input a string that isn't a command, which you will say)
u - use
v - IDK 
w - west 
x - xyzzy or extended command (room specific?)
y - yes 
z - sleep or skip turn? 
? - help (list commands)
'''
instructions = '''
'''
global player_room
player_room = 'start'
#I hope I can make the inventory less complicated... 
global player_inventory
player_inventory = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class room():
    #rooms are the basic unit, in a grid formation. movement only possible in straight lines.
    def __init__(self, name, direction, dir_N, dir_E, dir_S, dir_W):
        self.names = name
        self.directions = direction
        #if the direction is not available, then input the specific failure for each impossible direction
        #e.g., wall, cliff, etcetera
        self.north = dir_N
        self.east = dir_E
        self.south = dir_S
        self.west = dir_W
def setup():
    #make the roomz
    debris_room = room('debris', 'ns', 'grill_room', 'wall', 'Hall_of_the_Mount', 'wall')
    wall = room('wall', '', '', '', '', '')
    cliff = room('cliff', '','','','')
    start_room = room('start', 'nesw', 'wilderness', 'wilderness', 'forest3', 'home')
    wilderness = room('wilderness', 'nesw', 'wilderness', 'wilderness', 'wilderness', 'forest3')
    forest3 = room('forest', 'nesw', 'start', 'wilderness', 'plains3', 'wilderness')
    plains3 = room('plains', 'nesw', 'forest3', 'featureless_plain', 'cave_entrance', 'featureless_plain')
    home = room('Cabin', 'e', 'wall', 'start', 'wall', 'wall')
    featureless_plain = room('featureless plain', 'nesw', 'featureless_plain', 'featureless_plain', 'plains3', 'featureless_plain')
    Hall_of_the_Mount = room('Hall of the Mount', 'ns', 'debris_room', 'wall', 'ain_King', 'wall')
    ain_King = room('ain King', 'ne', 'Hall_of_the_Mount', 'Chasm1', 'wall', 'wall')
    cave_entrance = room('Cave entrance', 'nesw', 'plains3', 'featureless_plain', 'grill_room', 'featureless_plain')
    grill_room = room('grill room', 'ns', 'cave_entrance', 'wall', 'debris_room', 'wall')
    Chasm1 = room('north chasm', 'sw', 'wall', 'cliff', 'ain_King', 'Chasm2')
    Chasm2 = room('south chasm', 'ns', 'Chasm1', 'wall', 'Crystal_room', 'wall')
    Crystal_Room = room('Crystal room', 'nesw', 'Chasm2', 'Big_Room4', 'Twilight_Zone', 'ugh')
    Twilight_Zone = room('Twilight Zone', 'nesw', 'ugh', 'ugh', 'ugh', 'ugh')
    ugh = room('ugh', 'nesw', 'Twilight_Zone', 'Twilight_Zone', 'Twilight_Zone', 'Maze5')
    
    
    
    
    

def room_change(direction):
    #this is what controls where goes to where
    global player_room
    room = player_room
    if direction == 'n':
        whichway = 'north'
    elif direction== 'e':
        whichway = 'east'
    elif dirction == 's':
        whichway = 'south'
    elif direction == 'w':
        whichway = 'west'
    else:
        print 'program failure'
    player_room = getattr(room, whichway)

def object_status(room):
    #controls where the objects are
    return 0 #placeholder
    
def startup():
#display commands at startup
    print(command_string_help)
    if raw_input('Do you want instructions?') == 'y':
        print instructions
    else:
        return 0 #placeholder
        #start game
        
    
def help():
#the help thing, called by h or ?
    if raw_input('list commands? y n')== 'y':
        print command_string_help
    else:
        print 'Then why did you ask?'


def movement (room, times, direction):
    #retrieve possible directions from the room
    
    iteration = times
    derp = False
    if direction in getattr(room, directions):
        iteration = 0
        if direction == 'w':
            print 'you go west'
            
        elif direction == 's':
            print 'you go south'
        elif direction == 'n':
            print 'you go north'
        else:
            print 'you go east'
        room_change(direction)
    elif iteration < 5:
        iteration = iteration + 1
        print "you can't go that way"
    else:
        if direction == 'w':
            print 'fine. you go west'
        elif direction == 's':
            print 'fine. you go south'
        elif direction == 'n':
            print 'fine. you go north'
        else:
            print 'fine. you go east'
        derp = True
    return derp

        
            
        
    
    
    
        
   
def possible_answer(answer, state):
    #checks whether the player's response is valid
    #state 0 is true/false, state 1 is direction or other
    #may add extended commands later
    if state == 0: #true/false
        if answer == 'y' or answer == 'n':
            return 1
        else:
            return 0
    elif state == 1: #normal answer
        return 1
    else:
        return 1
        
def Xyzzy_Xyzzy(room):
    #Xyzzy teleport function
    if room == 'debris':
        return 'home'
    elif room == 'home':
        return 'debris'
    else:
        print 'nothing happens'
        
        
        
        
        
        
