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
#got it! each room has an 'inventory, as does the player, and the object stores which room it's in (or if it's in the player's
#inventory

global player_inventory
player_inventory = []


class room():
    #rooms are the basic unit, in a grid formation. movement only possible in straight lines.
    def __init__(self, name, direction, dir_N, dir_E, dir_S, dir_W, entry1, entry2):
        self.names = name
        self.directions = direction
        #if the direction is not available, then input the specific failure for each impossible direction
        #e.g., wall, cliff, etcetera
        self.north = dir_N
        self.east = dir_E
        self.south = dir_S
        self.west = dir_W
        self.long_description = entry1
        self.short_description = entry2
def setup():
    #make the roomz
    #first entry strings/look
    debris_string_1 = 'You are in '
    cliff_string = 'you fall down a cliff and break every bone in your body!'
    wall_string = 'you walk into a wall. Ouch!'
    start_string_1 = ''
    wilderness_string = 'you are in a wilderness'
    featureless_string = 'you are on a featureless plain'
    plains3_string = 'you are on a plain'
    forest3_string = 'you are in a forest
    #second entry strings
    debris_string_2 = 'your are in debris room'
    start_string_2 = ''
    home_string_2 = 'you are in the cabin'
    Hall_of_the_Mount = 'you are in the Hall of the Mount'
    #rooms
    debris_room = room('debris', 'ns', 'grill_room', 'wall', 'Hall_of_the_Mount', 'wall', debris_string_1, debris_string_2)
    wall = room('wall', '', '', '', '', '', wall_string, wall_string)
    cliff = room('cliff', '','','','', cliff_string, cliff_string)
    start_room = room('start', 'nesw', 'wilderness', 'wilderness', 'forest3', 'home', start_string_1, start_string_2)
    wilderness = room('wilderness', 'nesw', 'wilderness', 'wilderness', 'wilderness', 'forest3', wilderness_string, wilderness_string)
    forest3 = room('forest', 'nesw', 'start', 'wilderness', 'plains3', 'wilderness', forest3_string, forest3_string)
    plains3 = room('plains', 'nesw', 'forest3', 'featureless_plain', 'cave_entrance', 'featureless_plain', plains3_string, plains3_string)
    home = room('Cabin', 'e', 'wall', 'start', 'wall', 'wall', home_string_1, home_string_2)
    featureless_plain = room('featureless plain', 'nesw', 'featureless_plain', 'featureless_plain', 'plains3', 'featureless_plain', featureless_string, featureless_string)
    Hall_of_the_Mount = room('Hall of the Mount', 'ns', 'debris_room', 'wall', 'ain_King', 'wall', Hall_of_the_mount_string_1, Hall_of_the_Mount_string_2)
    ain_King = room('ain King', 'ne', 'Hall_of_the_Mount', 'Chasm1', 'wall', 'wall', ain_King_string_1, ain_King_string_2)
    cave_entrance = room('Cave entrance', 'nesw', 'plains3', 'featureless_plain', 'grill_room', 'featureless_plain', cave_entrance_string_1, cave_entrance_string_2)
    grill_room = room('grill room', 'ns', 'cave_entrance', 'wall', 'debris_room', 'wall', grill_room_string_1, grill_room_string_2)
    Chasm1 = room('north chasm', 'sw', 'wall', 'cliff', 'ain_King', 'Chasm2', Chasm1_string_1, Chasm1_string_2)
    Chasm2 = room('south chasm', 'ns', 'Chasm1', 'wall', 'Crystal_room', 'wall', Chasm2_string_2, chasm2_string_2)
    Crystal_Room = room('Crystal room', 'nesw', 'Chasm2', 'Big_Room4', 'Twilight_Zone', 'ugh', crystal_room_string_1, crystal_room_string_2)
    Twilight_Zone = room('Twilight Zone', 'nesw', 'ugh', 'ugh', 'ugh', 'ugh', Twilight_zone_string_1, Twilight_zone_string_2)
    ugh = room('ugh', 'nesw', 'Twilight_Zone', 'Twilight_Zone', 'Twilight_Zone', 'Maze5', ugh_string_1, ugh_string_2)
    
    
    
    
    

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
        
        
        
        
        
        
