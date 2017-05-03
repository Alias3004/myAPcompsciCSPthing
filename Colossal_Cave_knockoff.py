#narrator will be sarcastic sometimes (if you keep trying to go north when you can't
#suddenly says 'fine. you go north' (alternatives between falling and dying and
#walking into a wall and etc)
#note: This code is heavily based off of the game by Will Crowther, and the maze by that made by adam woods 
global iterations
iterations = 0
global cave_array
global command_string_help
command_string_help = ''' 
list of commands 
a - apply  
b - blast
c - cancel
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

#I hope I can make the inventory less complicated... 
#got it! each room has an 'inventory, as does the player, and the object stores which room it's in (or if it's in the player's
#inventory
class player():
    def __init__(self):
        self.player_inventory = []
        self.player_room = 4
        self.player_status = 'alive'
    def room_change(self, destination):
        self.player_room = destination
    def get_item(self, item):
        self.player_inventory.append(item)
    def drop_item(self, item):
        self.player_inventory.remove(item)
    def die(self):
        self.player_status = 'dead'
    def live(self):
        self.player_status = 'alive'
    def go_west(self):
        self.player_room = room_finder(cave_array[player1.player_room].west)
    def go_east(self):
        self.player_room = room_finder(cave_array[player1.player_room].east)
    def go_north(self):
        self.player_room = room_finder(cave_array[player1.player_room].north)
    def go_south(self):
        self.player_room = room_finder(cave_array[player1.player_room].south)
        
player1 = player()

global lamp_on
lamp_on = False
class item():
    def __init__(self, name, letter, there_is, ID_shortcut, start_location):
        self.names = name
        self.call = letter
        self.description = there_is
        self.label = ID_shortcut
        self.location = start_location
    def item_location(self, new_location):
        self.location = new_location
        
lamp = item('lamp', 'l', 'there is a lamp here', 'lamp', '')
rod = item('rod', 'r', 'there is a 3-foot steel rod here', 'rod', '')
silver = item('silver bars', 's', 'there are bars of silver here!', 'silver', '')
gold = item('gold', 'g', 'there is a gold nugget here!', 'gold', '')
coke_can = item('black cylinder', 'c', 'there is a mysterious black cylinder here', 'coke_can', '')
quarter = item('silver coin', 'q', 'there is a quarter here!', 'quarter', '')
keys = item('rusty keys', 'k', 'there are some keys here', 'keys', '')

   
    
    

        
def setup():
    #make the roomz
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
            self.entered = False
            self.room_inventory = []
            self.placeholder = 1
        def entered_true(self, entered):
            self.entered = True
        def room_inventory_add(self, item):
            self.room_inventory.append(item)
        def room_inventory_remove(self, item):
            self.room_inventory.remove(item)
        def make_bridge(self):
            if self.names == 'north chasm' or self.names == 'south chasm':
                self.long_description.append('a bridge now spans the chasm')
                if self.names == 'north chasm':
                    self.south = 'chasm2'
                else:
                    self.north = 'chasm1'
            else:
                self.placeholder = 1
    #first entry strings/look
    
    debris_string_1 = 'You are in a room full of junk and debris. There is an awkward slope to the north, and a widening passage to the south. There is a rock here with the letters XYZZY'
    cliff_string = 'you fall down a cliff and break every bone in your body!'
    wall_string = 'you walk into a wall. Ouch! you broke your skull!'
    start_string_1 = 'You are in a small clearing next to a stream. West of you is a small cabin. There is a wilderness to the north and east, and a more natural forest to the south'
    wilderness_string = 'you are in a wilderness, stretching in all directions'
    featureless_string = 'you are on a featureless plain, stretching in all directions'
    plains3_string_1 = 'you are on a plain. There is a featureless plain to the east and west, a forest to the north, and what looks like a rock pile to the south'
    forest3_string_1 = 'you are in a forest. There is a wilderness to the east and west, and what looks to be a clearing to the south. North of you is the stream and the cabin.'
    home_string_1 = 'you are in a small cabin, with three walls and a door on the east side. There is a small fountain here.'
    hall_of_the_mount_string_1 = 'You are in a large, long hallway stretching to the south. North of you is a narrowing passage. Above you is a sign stretching into the distance. You can read "Hall of the Mount"'
    ain_king_string_1 = 'You are in a large, long hallway stretching to the north. To the west there is a small gateway leading to a chasm. Above you is a sign stretching into the distance. You can read "ain king"'
    entrance_string_1 = 'You are at a large pile of rocks leading to a cave, with a large grill. Fortunately, it has a hole in it. There is a featureless plain to the east and west, and a plains to the north.'
    grill_string_1 = 'You are in the room inside of the grill. There is light here, but to the south it is dark.'
    chasm1_string_1 = 'you are at the north edge of a gaping chasm, too wide to jump. The bottom is out of sight. There is a sign here depicting what appears to be a tribal shaman performing a ritual with a stick - it is very crude. To the east is a portal to "ain King"'
    chasm1_string_2 = 'you are at the north chasm'
    chasm2_string_2 = 'you are at the south chasm'
    chasm2_string_1 = 'you are at the south edge of a gaping chasm, too wide to jump. To the south is a cave which appears to glitter faintly.'
    twilight_zone_string_1 = 'welcome to the Twilight Zone'
    death_string_1 = "Now you've done it! You've gone and got yourself killed! I can't believe this! Now, I haven't done this before, so be cautious - but would you like me to try and reincarnate you?"
    #second entry strings
    debris_string_2 = 'your are in debris room'
    plains3_string_2 = 'you are on a plain'
    forest3_string_2 = 'you are in a forest'
    start_string_2 = 'You are in a small clearing near a stream'
    home_string_2 = 'you are in the cabin'
    hall_of_the_mount_string_2 = 'you are in the Hall of the Mount'
    ain_king_string_2 = 'you are in "ain King"'
    entrance_string_2 = 'you are at the cave entrance'
    grill_string_2 = 'You are in the grill room'
    twilight_zone_string_2 = 'you are in the Twilight Zone'
    death_string_2 = "You did it again. Seriously, you need to be more careful if you're going to survive here! Would you like me to try and reincarnate you?"
    ugh_string = 'Ugh'
    big_room_string = 'you are in a big room'
    junction_string_1 = 'you are at a junction. to the north is a thin passage. to the south is the big room. to your west is a strange light'
    junction_string_2 = 'you are at a n/s/w junction'
    strange_room_string = 'you are in a strange room'
    map_room_string_1 = 'you are in a room with a sign that says map room. there are the remains of a map on the wall, but most of it has been scratched out. you can make out some writing - it reads "beware of maze"'
    map_room_string_2 = 'you are in the map room'
    maze_string = 'you are in a maze of many passages, all alike'
    crystal_string_1 = 'you are in a room made of sparkling crystals. there are passages to the north, south, east, and west.'
    crystal_string_2 = 'you are in the crystal room'
    global cave_array
    cave_array = []
    #rooms
    pit_death = room('death', '', '', '', '', '', death_string_1, death_string_2)
    cave_array.append(pit_death)
    debris_room = room('debris', 'ns', 'grill room', 'wall', 'hall of the mount', 'wall', debris_string_1, debris_string_2)
    cave_array.append(debris_room)
    wall = room('wall', '', '', '', '', '', wall_string, wall_string)
    cave_array.append(wall)
    cliff = room('cliff', '','','','','', cliff_string, cliff_string)
    cave_array.append(cliff)
    start_room = room('start', 'nesw', 'wilderness', 'wilderness', 'forest', 'cabin', start_string_1, start_string_2, aboveground = True)
    cave_array.append(start_room)
    wilderness = room('wilderness', 'nesw', 'wilderness', 'wilderness', 'wilderness', 'forest3', wilderness_string, wilderness_string, aboveground = True)
    cave_array.append(wilderness)
    forest3 = room('forest', 'nesw', 'start_room', 'wilderness', 'plains3', 'wilderness', forest3_string_1, forest3_string_2, aboveground = True)
    cave_array.append(forest3)
    plains3 = room('plains', 'nesw', 'forest3', 'featureless_plain', 'cave_entrance', 'featureless_plain', plains3_string_1, plains3_string_2, aboveground = True)
    cave_array.append(plains3)
    home = room('cabin', 'e', 'wall', 'start_room', 'wall', 'wall', home_string_1, home_string_2, aboveground = True)
    cave_array.append(home)
    featureless_plain = room('featureless plain', 'nesw', 'featureless_plain', 'featureless_plain', 'plains3', 'featureless_plain', featureless_string, featureless_string, aboveground = True)
    cave_array.append(featureless_plain)
    hall_of_the_mount = room('hall of the mount', 'ns', 'debris_room', 'wall', 'ain_king', 'wall', hall_of_the_mount_string_1, hall_of_the_mount_string_2)
    cave_array.append(hall_of_the_mount)
    ain_king = room('ain king', 'ne', 'hall_of_the_mount', 'chasm1', 'wall', 'wall', ain_king_string_1, ain_king_string_2)
    cave_array.append(ain_king)
    cave_entrance = room('Cave entrance', 'nesw', 'plains3', 'featureless_plain', 'grill_room', 'featureless_plain', entrance_string_1, entrance_string_2, aboveground = True)
    cave_array.append(cave_entrance)
    grill_room = room('grill room', 'ns', 'cave_entrance', 'wall', 'debris_room', 'wall', grill_string_1, grill_string_2, aboveground = True)
    cave_array.append(grill_room)
    chasm1 = room('north chasm', 'sw', 'wall', 'cliff', 'cliff', 'ain_King', chasm1_string_1, chasm1_string_2)
    cave_array.append(chasm1)
    chasm2 = room('south chasm', 'ns', 'Cliff', 'wall', 'Crystal_room', 'wall', chasm2_string_2, chasm2_string_2)
    cave_array.append(chasm2)
    crystal_room = room('crystal room', 'nesw', 'Chasm2', 'Big_Room4', 'Twilight_Zone', 'ugh', crystal_string_1, crystal_string_2)
    cave_array.append(crystal_room)
    twilight_zone = room('twilight zone', 'nesw', 'ugh', 'ugh', 'ugh', 'ugh', twilight_zone_string_1, twilight_zone_string_2)
    cave_array.append(twilight_zone)
    ugh = room('ugh', 'nesw', 'twilight_zone', 'twilight_zone', 'twilight_zone', 'maze_5', ugh_string, ugh_string)
    cave_array.append(ugh)
    Big_room = room('Big room', 'junction', 'wall', '', 'wall', 'crystal_room', big_room_string, big_room_string)
    cave_array.append(Big_room)
    junction = room('junction', 'nsw', 'strange room', 'big_room', 'map_room', 'wall', junction_string_1, junction_string_2)
    cave_array.append(junction)
    strange_room = room('chem lab', 's', 'wall', 'wall', 'junction', 'wall', strange_room_string, strange_room_string)
    cave_array.append(strange_room)
    map_room = room('map room', 'ew', 'wall', 'junction', 'wall', 'maze_1', map_room_string_1, map_room_string_2)
    cave_array.append(map_room)
    maze_1 = room('maze entrance', 'nesw', 'maze_1', 'map_room', 'maze_4', 'maze_2', maze_string, maze_string)
    cave_array.append(maze_1)
    maze_2= room('maze 2', 'nesw', 'maze_1', 'maze_5', 'maze_2', 'maze_3', maze_string, maze_string)
    cave_array.append(maze_2)
    maze_3= room('maze 3', 'nesw', 'maze_2', 'maze_3', 'maze_6', 'maze_4', maze_string, maze_string)
    cave_array.append(maze_3)
    maze_4= room('maze 4', 'nesw', 'maze_2', 'maze_3', 'maze_1', 'maze_4', maze_string, maze_string)
    cave_array.append(maze_4)
    maze_5= room('maze 5', 'nesw', 'maze_12', 'maze_5', 'maze_2', 'maze_5', maze_string, maze_string)
    cave_array.append(maze_5)
    maze_6= room('maze 6', 'nesw', 'maze_3', 'maze_7', 'maze_6', 'maze_8', maze_string, maze_string)
    cave_array.append(maze_6)
    maze_7= room('maze 7', 'nesw', 'maze_7', 'maze_7', 'maze_7', 'maze_6', maze_string, maze_string)
    cave_array.append(maze_7)
    maze_8= room('maze 8', 'nesw', 'maze_14', 'maze_9', 'maze_6', 'maze_8', maze_string, maze_string)
    cave_array.append(maze_8)
    maze_9= room('maze 9', 'nesw', 'maze_12', 'maze_10', 'maze_13', 'maze_8', maze_string, maze_string)
    cave_array.append(maze_9)
    maze_10= room('maze 10', 'nesw', 'maze_9', 'maze_9', 'maze_11', 'maze_10', maze_string, maze_string)
    cave_array.append(maze_10)
    maze_11= room('maze 11', 'nesw', 'maze_10', 'maze_13', 'maze_11', 'maze_11', maze_string, maze_string)
    cave_array.append(maze_11)
    maze_12= room('maze 12', 'nesw', 'maze_12', 'maze_9', 'maze_9', 'maze_13', maze_string, maze_string)
    cave_array.append(maze_12)
    maze_13= room('maze 13', 'nesw', 'maze_18', 'maze_7', 'maze_9', 'maze_12', maze_string, maze_string)
    cave_array.append(maze_13)
    maze_14= room('maze 14', 'nesw', 'maze_8', 'maze_16', 'maze_17', 'maze_8', maze_string, maze_string)
    cave_array.append(maze_14)
    maze_15= room('maze 15', 'nesw', 'maze_17', 'maze_15', 'maze_16', 'maze_16', maze_string, maze_string)
    cave_array.append(maze_15)
    maze_16= room('maze 16', 'nesw', 'maze_15', 'maze_14', 'maze_16', 'maze_17', maze_string, maze_string)
    cave_array.append(maze_16)
    maze_17= room('maze 17', 'nesw', 'maze_17', 'maze_14', 'maze_16', 'maze_15', maze_string, maze_string)
    cave_array.append(maze_17)
    maze_18 = room('maze 18', 'nesw', 'maze_14', 'maze_17', 'maze_6', 'maze_15', maze_string, maze_string)
    cave_array.append(maze_18)
    #set up initial inventory
    cave_array[room_finder('home')].room_inventory_add(['lamp', 'keys'])
    cave_array[room_finder('maze 18')].room_inventory_add('silver')
    cave_array[room_finder('debris')].room_inventory_add('rod')
    cave_array[room_finder('crystal room')].room_inventory_add('gold')
    cave_array[room_finder('chem lab')].room_inventory_add('coke_can')
    cave_array[room_finder('junction')].room_inventory_add('quarter')

def room_finder(answer):
    #searches cave_array for destination room, if not found, return 0 (-> room 0)
    global cave_array
    found=False
    count = 0
    while found==False and count < len(cave_array):
        if cave_array[count].names == answer:
            found = True
        else:
            count = count+1
    if found == True:
        return count
    else:
        return 0


                              
    
def enter_room(derp=False):
    if player1.player_room == 0:
        death_instance = raw_input()
        if death_instance == 'y':
            
            cave_array[player1.player_room].room_inventory_remove('lamp')
            player1.room_change(9)
            lamp.item_location('start_room')
            start_room.room_inventory_add('lamp')
            enter_room()
        else:
            print('you died')
            player1.die
            
    else:        
        if derp==False:
            if cave_array[player1.player_room].entered == False:
                print_instance_enter = cave_array[player1.player_room].long_description
                print(print_instance_enter)
            else:
                print_instance_enter = cave_array[player1.player_room].short_description
                print(print_instance_enter)
            for items in cave_array[player1.player_room].room_inventory:
                print_instance_items = item.description
                print(print_instance_items)
        elif derp==True:
            cave_array[player1.player_room].short_description
            player1.room_change(0)
            enter_room()
        else:
            print ('program failure')
    

def room_change(direction, derp=False):
    global iterations
    #this is what controls where goes to where
    room = player1.player_room
    global lamp_on
    if lamp_on == True and lamp.location== room:
        light_instance = True
    elif lamp in player1.player_inventory and lamp_on == True:
        light_instance = True
    else:
        light_instance = False
        
    if cave_array[player1.player_room].aboveground == True or light_instance == True:
        if direction in cave_array[player1.player_room].directions:
            derp_yes = False
            iterations = 0
            if direction == 'n':
                print ('you go north')
                player1.go_north()
            elif direction== 'e':
                print ('you go east')
                player1.go_east()
            elif direction == 's':
                print ('you go south')
                player1.go_south()
            elif direction == 'w':
                print ('you go west')
                player1.go_west()
            else:
                print ('program failure')                                     
        elif iterations < 5:
            iterations = iterations + 1
        else:
            derp_yes = True
            if direction == 'w':
                print ('fine. you go west')
                player1.go_west()
            elif direction == 's':
                print ('fine. you go south')
                player1.go_south()
            elif direction == 'n':
                print ('fine. you go north')
                player1.go_north()
            else:
                print ('fine. you go east')
                player1.go_east()
        enter_room(derp = derp_yes)
            
            
    else:
        player1.room_change('pit_death')
    

    
def startup():
#display commands at startup
    player1.live()
    print(command_string_help)
    global instructions
    testing = False
    while testing != True:
        instance = raw_input('Do you want instructions?')
        if instance == 'y' or instance == 'n':
            testing = True
        else:
            testing = False
    
    if instance == 'y':
        print (instructions)
    else:
        print ('starting')
        
                                              
    
def help():
#the help thing, called by h or ?
    global command_string_help                                          
    if raw_input('list commands? y n')== 'y':
        print (command_string_help)
    else:
        print ('Then why did you ask?')

        
def place_drop():
    drop_instance = raw_input('what do you want to place/drop?')
    if drop_instance in player1.player_inventory:
        drop_instance.location(player1.player_room)
        player1.player_inventory_remove(drop_instance)
        cave_array[player1.player_room].room_inventory_add(drop_instance)
    else:
        print ("you don't have that")
        
def use_item():
    use_instance = raw_input('what do you want to use?')
    if use_instance in player1.player_inventory:
        if use_instance == 'lamp':
            global lamp_on
            lamp_on = True
        elif use_instance == 'rod':
            if player1.player_room == 14 or player1.player_room == 15: #14 = chasm1, 15 = chasm2
                chasm1.make_bridge()
                chasm2.make_bridge()
        else:
            print ("you can't use that")
    else:
        print ("you don't have that")
                             
        
def get_action():
    #ugh
    get_instance = raw_input('what would you like to get?')
    if get_instance == 'c' and len(get_instance)== 1:
        print ('nevermind')
    elif get_instance in cave_array[player1.player_room].room_inventory:
        get_instance.location('player_inventory')
        player1.player_inventory_add(get_instance)
        cave_array[player1.player_room].room_inventory_remove(get_instance)
    elif get_instance in player1.player_inventory:
        print ('you already have that!')
    else:
        print ('what?')
        
        
        
    
def action(answer):
    #which action (not T/F)
    if answer == 'xyzzy':
        xyzzy_xyzzy()
    elif len(answer) != 1:
        print ("i don't understand that!")
    elif answer in 'nesw':
        room_change(answer)
    elif answer in 'pd':
        place_drop()
    elif answer == 'g':
        get_action()
    elif answer == 'u':
        use_item()
    elif answer == '?' or answer == 'h':
        help()
    elif answer == 't':
        print ("sorry, you can't talk yet")
    elif answer == 'b':
        print ('blasting requires dynamite')
    elif answer == 'r':
        enter_room()
    elif answer == 'l':
        enter_room()
    else:
        print ("sorry, that hasn't been implemented yet")
        
        


def xyzzy_xyzzy():
    #Xyzzy teleport function
    room = player1.player_room
    if room == room_finder('debris'):
        player1.room_change(room_finder('home'))
    elif room == room_finder('home'):
        player1.room_change(room_finder('debris'))
    else:
        print ('nothing happens')
        
        
def colossal_cave_knockoff():
    setup()
    startup()
    enter_room()
    while player1.player_status == 'alive':
        answer_instance = raw_input()
        action(answer_instance)
    restart = raw_input('play again?')
    if restart == 'y':
        colossal_cave_knockoff()
    else:
        print ('goodbye') 
