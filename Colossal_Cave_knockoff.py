#narrator will be sarcastic sometimes (if you keep trying to go north when you can't
#suddenly says 'fine. you go north' (alternatives between falling and dying and
#walking into a wall and etc)
#note: This code is heavily based off of the game by Will Crowther, and the maze by that made by adam woods 
global command_string_help
command_string_help = ''' 
list of commands 
a - apply  
b - blast
c - coke
d - drop (followed by 'drop what' prompt)
e - east 
f - fate 
g - get (followed by 'get what' prompt) 
h - help (list commands) 
i - inventory 
j - jump 
k - attack (kill)
l - look 
m - ???
n - conditional, either works as no (when prompted for a yn answer) or north 
o - open 
p - place
q - quiz 
r - repeat 
s - south 
t - talk (allows you to input a string that isn't a command, which you will say)
u - use (followed by 'use what' prompt)
v - ??? 
w - west 
x - ???
y - yes 
z - ???
? - help (list commands)
'''
instructions = '''
This is an unnamed knockoff of the text-based adventure game 'colossal cave adventure,' created by william crowther, and later 
edited by don woods. i am the narrator, your eyes, ears, etcetera. in order to take action, tell me what you would like to do. 
however, i can only take single-letter commands, as this is not the full game. basic commands are directions, as well as 'use'
commands. use commands will be followed by a query of what to use. please keep your arms and legs inside the program at all times.
'''
global player_room
player_room = 'start_room'
#I hope I can make the inventory less complicated... 
#got it! each room has an 'inventory, as does the player, and the object stores which room it's in (or if it's in the player's
#inventory

global player_inventory
player_inventory = []
global lamp_on
lamp_on = False
class item():
    def __init__(self, name, letter, there_is, there_is_2, ID_shortcut):
        self.names = name
        self.call = letter
        self.description = there_is
        self.alternate_description = there_is_2
        self.label = ID_shortcut
lamp = item.llamp('lamp', 'l', 'there is a lamp here', 'there is a lamp shining nearby', 'lamp')
rod = item.rrod('rod', 'r', 'there is a 3-foot steel rod here', '', 'rod')
silver = item.ssilver('silver bars', 's', 'there are bars of silver here!', '', 'silver')
gold = item.nugget('gold', 'g', 'there is a gold nugget here!', '', 'gold')
coke_can = item.coke_zero('black cylinder', 'c', 'there is a mysterious black cylinder here', '', 'coke_can')
quarter = item.qquarter('silver coin', 'q', 'there is a quarter here!', '', 'quarter')


def item_setup():
    #sets up the items - where they go at first.
    lamp_loc = 'start_room'
    rod_loc = 'debris_room'
    silver_loc = ''
    gold_loc = ''
    coke_can_loc = ''
    quarter_loc = ''
    

def item_location_1(answer, room_or_item):
    #there are two variables for item location - a variable for each room storing which items are in it 
    #(in this circumstance the player counts as a room), and a variable for each object storing where it is.
    #this means that when the player enters a room, there is a fast check, and when the player cites a specific
    #object, again, fast check. This function also controls the movement of items, not just the reference of them.
    a = ''
    b = ''
    c = 'coke_can_loc'
    d = 'dynamite_loc'
    e = 'emerald_loc'
    f = ''
    g = 'gold_loc'
    h = ''
    i = ''
    j = ''
    k = 'keys_loc'
    l = 'lamp_loc'
    m = ''
    n = ''
    o = ''
    p = 'pocketwatch_loc'
    q = 'quarter_loc'
    r = 'rod_loc'
    s = 'silver_loc'
    t = 'thingimajig_loc'
    u = ''
    v = ''
    w = 'western_loc'
    x = 'xylophone_loc'
    y = 'yo-yo_loc'
    z = ''
    
    
    
class room():
    #rooms are the basic unit, in a grid formation. movement only possible in straight lines.
    def __init__(self, name, direction, dir_N, dir_E, dir_S, dir_W, entry1, entry2, aboveground = False):
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
        self.aboveground = aboveground
        
def setup():
    #make the roomz
    #first entry strings/look
    debris_string_1 = 'You are in a room full of junk and debris. There is an awkward slope to the north, and a widening passage to the south. There is a rock here with the letters XYZZY'
    cliff_string = 'you fall down a cliff and break every bone in your body!'
    wall_string = 'you walk into a wall. Ouch!'
    start_string_1 = 'You are in a small clearing next to a stream. West of you is a small cabin. There is a wilderness to the north and east, and a more natural forest to the south'
    wilderness_string = 'you are in a wilderness, stretching in all directions'
    featureless_string = 'you are on a featureless plain, stretching in all directions'
    plains3_string_1 = 'you are on a plain. There is a featureless plain to the east and west, a forest to the north, and what looks like a rock pile to the south'
    forest3_string_1 = 'you are in a forest. There is a wilderness to the east and west, and what looks to be a clearing to the south. North of you is the stream and the cabin.'
    home_string_1 = 'you are in a small cabin, with three walls and a door on the east side. There is a small fountain here.'
    Hall_of_the_mount_string_1 = 'You are in a large, long hallway stretching to the south. North of you is a narrowing passage. Above you is a sign stretching into the distance. You can read "Hall of the Mount"'
    ain_King_string_1 = 'You are in a large, long hallway stretching to the north. To the west there is a small gateway leading to a chasm. Above you is a sign stretching into the distance. You can read "ain king"'
    entrance_string_1 = 'You are at a large pile of rocks leading to a cave, with a large grill. Fortunately, it has a hole in it. There is a featureless plain to the east and west, and a plains to the north.'
    grill_string_1 = 'You are in the room inside of the grill. There is light here, but to the south it is dark.'
    chasm1_string_1 = 'you are at the north edge of a gaping chasm, too wide to jump. The bottom is out of sight. There is a sign here depicting what appears to be a tribal shaman performing a ritual with a stick - it is very crude. To the east is a portal to "ain King"'
    chasm2_string_1 = 'you are at the south edge of a gaping chasm, too wide to jump. To the south is a cave which appears to glitter faintly.'
    Twilight_zone_string_1 = 'welcome to the Twilight Zone'
    death_string_1 = "Now you've done it! You've gone and got yourself killed! I can't believe this! Now, I haven't done this before, so be cautious - but would you like me to try and reincarnate you?"
    #second entry strings
    debris_string_2 = 'your are in debris room'
    plains3_string_2 = 'you are on a plain'
    forest3_string_2 = 'you are in a forest'
    start_string_2 = 'You are in a small clearing near a stream'
    home_string_2 = 'you are in the cabin'
    Hall_of_the_Mount_string_2 = 'you are in the Hall of the Mount'
    ain_king_string_2 = 'you are in "ain King"'
    entrance_string_2 = 'you are at the cave entrance'
    grill_string_2 = 'You are in the grill room'
    Twilight_zone_string_2 = 'you are in the Twilight Zone'
    death_string_2 = "You did it again. Seriously, you need to be more careful if you're going to survive here! Would you like me to try and reincarnate you?"
    ugh_string = 'Ugh'
    #rooms
    pit_death = room('death', '', '', '', '', '', death_string_1, death_string_2)
    debris_room = room('debris', 'ns', 'grill_room', 'wall', 'Hall_of_the_Mount', 'wall', debris_string_1, debris_string_2)
    wall = room('wall', '', '', '', '', '', wall_string, wall_string)
    cliff = room('cliff', '','','','', cliff_string, cliff_string)
    start_room = room('start', 'nesw', 'wilderness', 'wilderness', 'forest3', 'home', start_string_1, start_string_2, aboveground = True)
    wilderness = room('wilderness', 'nesw', 'wilderness', 'wilderness', 'wilderness', 'forest3', wilderness_string, wilderness_string, aboveground = True)
    forest3 = room('forest', 'nesw', 'start_room', 'wilderness', 'plains3', 'wilderness', forest3_string_1, forest3_string_2, aboveground = True)
    plains3 = room('plains', 'nesw', 'forest3', 'featureless_plain', 'cave_entrance', 'featureless_plain', plains3_string_1, plains3_string_2, aboveground = True)
    home = room('Cabin', 'e', 'wall', 'start_room', 'wall', 'wall', home_string_1, home_string_2, aboveground = True)
    featureless_plain = room('featureless plain', 'nesw', 'featureless_plain', 'featureless_plain', 'plains3', 'featureless_plain', featureless_string, featureless_string, aboveground = True)
    Hall_of_the_Mount = room('Hall of the Mount', 'ns', 'debris_room', 'wall', 'ain_King', 'wall', Hall_of_the_mount_string_1, Hall_of_the_Mount_string_2)
    ain_King = room('ain King', 'ne', 'Hall_of_the_Mount', 'Chasm1', 'wall', 'wall', ain_King_string_1, ain_King_string_2)
    cave_entrance = room('Cave entrance', 'nesw', 'plains3', 'featureless_plain', 'grill_room', 'featureless_plain', entrance_string_1, entrance_string_2, aboveground = True)
    grill_room = room('grill room', 'ns', 'cave_entrance', 'wall', 'debris_room', 'wall', grill_string_1, grill_string_2, aboveground = True)
    Chasm1 = room('north chasm', 'sw', 'wall', 'cliff', 'ain_King', 'Chasm2', Chasm1_string_1, Chasm1_string_2)
    Chasm2 = room('south chasm', 'ns', 'Chasm1', 'wall', 'Crystal_room', 'wall', Chasm2_string_2, chasm2_string_2)
    Crystal_Room = room('Crystal room', 'nesw', 'Chasm2', 'Big_Room4', 'Twilight_Zone', 'ugh', crystal_string_1, crystal_string_2)
    Twilight_Zone = room('Twilight Zone', 'nesw', 'ugh', 'ugh', 'ugh', 'ugh', Twilight_zone_string_1, Twilight_zone_string_2)
    ugh = room('ugh', 'nesw', 'Twilight_Zone', 'Twilight_Zone', 'Twilight_Zone', 'Maze5', ugh_string, ugh_string)
    
    
    
    

def room_change(direction):
    #this is what controls where goes to where
    global player_room
    global lamp_room
    room = player_room
    if getattr(room, aboveground) == True or (lamp_on == True and (lamp_room == room or lamp_room == 'player')):
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
    else:
        player_room = 'pit_death'

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

def check_inventory(call_type, subject_item):
    #checks if the object being referenced is in the inventory
    #or lists the inventory 
    if call_type == 0:
        print player_inventory
    else:
        if subject_item in player_inventory:
            return True
        else:
            return False
        
def use_place_drop(answer):
    subject_item_var = raw_input('what do you want to do this with?')
    if check_inventory(1, subject_item_var) == True:
        if answer == 'u':
            return 'u'
        elif answer == 'd':
            return 'd'
        elif answer == 'p':
            return 'p'
        else:
            print 'program failure'
    else:
        print "you don't have that"
        
def get_action():
    #ugh
    return 0
        
    
def action(answer):
    #which action (not T/F)
    if answer in 'nesw':
        movement(player_room, 1, answer)
    elif answer in 'upd':
        use_place_drop(answer)
    elif answer == 'g':
        get_action()
    elif answer == 'x':
        #continue with possibilities
        return 0
    else:
        print 'program failure'
        
        

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
        if answer == 'xyzzy':
            Xyzzy_Xyzzy(player_room)
        elif len(answer)==1:
            action(answer)
        else:
            print "I didn't understand that"
    else:
        print 'program failure'
        
def Xyzzy_Xyzzy(room):
    #Xyzzy teleport function
    if room == 'debris':
        return 'home'
    elif room == 'home':
        return 'debris'
    else:
        print 'nothing happens'
        
        
        
        
        
        
