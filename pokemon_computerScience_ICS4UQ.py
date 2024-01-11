# Import necessary modules
import pygame
from enum import Enum
from random import randint
from random import seed
import random
import math

# Define constants
GRASS_TYPE_START = 1
GRASS_TYPE_END = 5
# Defines a list of all Monsters used to call later when generating monster for users monster
MONSTERS = [
     {
        "name" : "unknown",
        "index" : 0,
        "level_start" : 1,
        "base_health" : 5,
        "base_attack" : 5,
        "monster_type" : "G",
    },  
    {
        "name" : "Python",
        "index" : 1,
        "level_start" : 1,
        "base_health" : 5,
        "base_attack" : 5,
        "monster_type" : "W",
        "evolves_to" : 2,
    },
    {
        "name": "Java",
        "index": 2,
        "level_start": 5,
        "base_health": 5,
        "base_attack": 5,
        "monster_type": "W",
        "evolves_to": 3,
    },
    {
        "name": "Homework",
        "index": 3,
        "level_start": 15,
        "base_health": 5,
        "base_attack": 5,
        "monster_type": "W",
        "evolves_to": None,
    },
    {
        "name": "C#",
        "index": 4,
        "level_start": 1,
        "base_health": 5,
        "base_attack": 5,
        "monster_type": "W",
        "evolves_to": 5,
    },
    {
        "name": "Test",
        "index": 5,
        "level_start": 5,
        "base_health": 5,
        "base_attack": 5,
        "monster_type": "W",
        "evolves_to": 6,
    },
]

# Define a list of moves to use in battles
MOVES = [
    {
        "move_name" : "pullup",
        "effective_against" : "G",
        "base_attack" : 5,
    },
    {
        "move_name" : "killer",
        "effective_against" : "G",
        "base_attack" : 10,
    }
]

# Define colors for background use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (106, 229, 153)
YELLOW = (237, 208, 33)
RED = (251, 87, 60)

# Define a scale for graphics
SCALE = 32

# Define screen dimensions
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640

# Define battle health bar width
BATTLE_HEALTH_BAR_WIDTH = 102

# Define map tile types to use to load maps from created grids
MAP_TILE_GRASS = "G"
MAP_TILE_BASKETBALL = "B"
MAP_TILE_CLOUDT = "*"
MAP_TILE_CLOUDRT = ")"
MAP_TILE_CLOUDLT = "("
MAP_TILE_CLOUDL = "{"
MAP_TILE_CLOUDR = "}"
MAP_TILE_CLOUDM = "+"
MAP_TILE_CLOUDLB = "["
MAP_TILE_CLOUDRB = "]"
MAP_TILE_CLOUDB = "_"
MAP_TILE_NULL = "?"
MAP_TILE_SHRUB = "g"
MAP_TILE_WATER = "W"
MAP_TILE_ROAD = "R"
MAP_TILE_ROCK = "T"
MAP_TILE_BOULDER = "t"
MAP_TILE_1 = "1"
MAP_TILE_2 = "2"
MAP_TILE_3 = "3"
MAP_TILE_4 = "4"
MAP_TILE_5 = "5"
MAP_TILE_6 = "6"
MAP_TILE_7 = "7"
MAP_TILE_8 = "8"
MAP_TILE_DOORS = ["1", "2", "3", "4", "5", "6", "7", "8"]
MAP_TILE_FLOOR = "L"
MAP_TILE_STONE_FLOOR = "S"
MAP_TILE_MATRIX = "M"
MAP_TILE_WOOD_FLOOR = "O"
MAP_TILE_ASPHALT = "A"
MAP_TILE_LOCKER = "F"
MAP_TILE_WALL = "l"
MAP_TILE_STONE_WALL = "s"
MAP_TILE_WOOD_WALL = "o"
MAP_TILE_ROOM_EXIT = "X"
MAP_TILE_BUILDING = "."
MAP_TILE_BIG_BUILDING = ","

# Define monster types
MONSTER_TYPES = ["G"]

# Define impassable tiles that player cannot walk through
IMPASSIBLE = [MAP_TILE_WATER, MAP_TILE_WALL, MAP_TILE_BUILDING, MAP_TILE_LOCKER, MAP_TILE_BIG_BUILDING, MAP_TILE_SHRUB, MAP_TILE_WOOD_WALL, MAP_TILE_NULL, MAP_TILE_BOULDER, MAP_TILE_CLOUDRB,MAP_TILE_CLOUDB, MAP_TILE_CLOUDLB, MAP_TILE_CLOUDT, MAP_TILE_STONE_WALL]

MAP_CONFIG = { #define all maps so code knows what to load when the number is called
    "01" : { #map 1 (spawn map/aldershot)
        "start_position": [7, 29],
        "exits" : [
        {
            "map" : "02",
            "position" : [13, 38],
            "new_start_position": [10, 0],
        }],
        "npcs": [],
        "buildings": [
            {
                "sprite": "Aldershot",
                "name": "School",
                "position": [0, 0],
                "size" : [40, 18]
            },
            {
                "sprite": "house",
                "name": "house",
                "position": [4.6, 24],
                "size" : [5, 5]
            },
        ],
    },
    "02" : {#map 2 (forest/lasalle)
        "start_position": [10, 0],
        "exits" : [
            {
            "map" : "01",
            "position" : [10, 0],
            "new_start_position" : [7, 29],
            },
            {
            "map" : "03",
            "position" : [21, 22],
            "new_start_position" : [9, 17],
            },

        ],
        "buildings": [
            {
                "sprite": "cavex",
                "name": "CAVE",
                "position": [20.5, 22],
                "size" : [2, 2]
            },
        ],
    },
    "03" : {#map 3 (cave maze)
        "start_position": [9, 16],
        "exits" : [
            {
            "map" : "02",
            "position" : [9, 18],
            "new_start_position" : [21, 21],
            },
            {
            "map" : "04",
            "position" : [10, 0],
            "new_start_position" : [1, 27],
            },
        ],
        "buildings":[
            {
                "sprite": "cave",
                "name": "CAVE",
                "position": [9.5, -1],
                "size" : [2, 2]
            },
            {
                "sprite": "cavex",
                "name": "CAVExit",
                "position": [8.5, 18],
                "size" : [2, 2]
            },],
    },
        "04" : {#map 4 (hayden/alton villiage)
        "start_position": [9, 16],
        "exits" : [
            {
            "map" : "03",
            "position" : [1, 28],
            "new_start_position" : [10, 1],
            },
            {
            "map" : "05",
            "position" : [15, 7],
            "new_start_position" : [10, 13],
            },
        ],
        "buildings":[
            {
                "sprite": "cavex",
                "name": "CAVExit",
                "position": [0.5, 28],
                "size" : [2, 2]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [0.5, 14],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [5.5, 14],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [10.5, 14],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [15.5, 14],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [20.5, 14],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [25.5, 14],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [35.5, 16],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [40.5, 16],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [45.5, 16],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [50.5, 16],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [40.5, 7],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [45.5, 7],
            "size" : [5, 5]
            },
            {
            "sprite": "house",
            "name": "house",
            "position": [50.5, 7],
            "size" : [5, 5]
            },
        ],
    },
    "05" : { #map 5 (nitish battle)
        "start_position": [10, 13],
        "exits" : [
            {
            "map" : "04",
            "position" : [10, 14],
            "new_start_position" : [15, 8],
            },
            {
            "map" : "06",
            "position" : [10, 5],
            "new_start_position" : [3, 6],
            },
        ],
        "npcs": [
            {
            "name" : "Nitish",
            "image" : "Trainer",
            "start_position" : [10,6]
            },
            {
            "name" : "cloudCPU",
            "image" : "computer",
            "start_position": [10, 4]
            },
        ],
        "buildings": [
        ],
    },
    "06" : { #map 6 (mainframe
        "start_position": [10, 13],
        "exits" : [
            {
            "map" : "07",
            "position" : [3, 0],
            "new_start_position" : [9, 13],
            },
        ],
        "npcs": [],
        "buildings": [],
    },
    "07" : {#map 7 (the cloud)
        "start_position": [9, 13],
        "exits" : [
            {
            "map" : "08",
            "position" : [9, 12],
            "new_start_position" : [9, 13],
            },
        ],
        "npcs": [],
        "buildings": [
            {
            "sprite": "Castle",
            "name": "Castle",
            "position": [3, 0],
            "size" : [13, 13]
            },
        ],
    },
    "08" : {#map 8 (Elite 4 rest area)
        "start_position": [9, 13],
        "exits" : [
            {
            "map" : "07",
            "position" : [9, 14],
            "new_start_position" : [10, 13],
            },
            {
            "map" : "09",
            "position" : [9, 1],
            "new_start_position" : [10, 13],
            },
        ],
        "npcs": [
            {
            "name" : "Nurse",
            "image" : "Nurse",
            "start_position" : [1,1]
            },
        ],
        "buildings": [],
    },
    "09" : {#map 9 (sam Map)
        "start_position": [9, 13],
        "exits" : [
            {
            "map" : "10",
            "position" : [9, 1],
            "new_start_position" : [9, 13],
            },
        ],
        "npcs": [
            {
            "name" : "Nurse",
            "image" : "Nurse",
            "start_position" : [1,1]
            },
            {
            "name" : "Trainer",
            "image" : "Trainer",
            "start_position" : [10,6]
            },
        ],
        "buildings": [],
    },
    "10" : {#map 10 (michael map)
        "start_position": [9, 13],
        "exits" : [
            {
            "map" : "11",
            "position" : [9, 1],
            "new_start_position" : [9, 13],
            },
        ],
        "npcs": [
            {
            "name" : "Nurse",
            "image" : "Nurse",
            "start_position" : [1,1]
            },
            {
            "name" : "Trainer",
            "image" : "Trainer",
            "start_position" : [10,6]
            },
        ],
        "buildings": [],
    },
    "11" : {#map 11 (nick map)
        "start_position": [9, 13],
        "exits" : [
            {
            "map" : "12",
            "position" : [9, 1],
            "new_start_position" : [9, 13],
            },
        ],
        "npcs": [
            {
            "name" : "Nurse",
            "image" : "Nurse",
            "start_position" : [1,1]
            },
            {
            "name" : "Trainer",
            "image" : "Trainer",
            "start_position" : [10,6]
            },
        ],
        "buildings": [],
    },
    "12" : {#map 12 (curtis map)
        "start_position": [9, 13],
        "exits" : [
            {
            "map" : "13",
            "position" : [9, 1],
            "new_start_position" : [9, 13],
            },
        ],
        "npcs": [
            {
            "name" : "Nurse",
            "image" : "Nurse",
            "start_position" : [1,1]
            },
            {
            "name" : "Trainer",
            "image" : "Trainer",
            "start_position" : [10,6]
            },
        ],
        "buildings": [],
    },
    "13" : {#map 13(final battle)
        "start_position": [9, 13],
        "exits" : [],
        "npcs": [
            {
            "name" : "Owen2",
            "image" : "Trainer",
            "start_position" : [10,6]
            },
        ],
        "buildings": [],
    },
}

ROOM_CONFIG = { #this configs all rooms
    "01" : {
        "01" : { #aldershot
            "start_position" : [10,13],
            "exit_position" : [18, 9],
            "npcs" : [
                {
                    "name" : "Bhinder",
                    "image" : "Bhinder",
                    "start_position" : [18,4]
                },
                {
                    "name" : "computer_1",
                    "image" : "computer_1",
                    "start_position": [20, 4]
                },
                {
                    "name" : "computer_2",
                    "image": "computer_2",
                    "start_position": [21, 4]
                },
                {
                    "name" : "computer_3",
                    "image": "computer_3",
                    "start_position": [22, 4]
                },
                {
                    "name" : "Owen1",
                    "image" : "Trainer",
                    "start_position" : [4,4]
                },
            ]
        },
        "02" : { #house
            "start_position" : [10,13],
            "exit_position" : [7, 29],
            "npcs" : [],
        }
    },
    "04" : {
        "01" : { #house
            "start_position" : [10,13],
            "exit_position" : [3, 19],
            "npcs" : [],
        },
    },
}


class TBattle:
    def __init__(self, screen, monster, player):
        # Initialize the battle screen, monster, and player
        self.screen = screen
        self.monster = monster
        self.player = player
        self.message = "Press 1 to pullup!"

    def load(self):
        pass

    def render(self):
        # Fill the screen with white color
        self.screen.fill(WHITE)

        # Load the font
        font = pygame.font.Font("Assets/PokemonGb.ttf", 16)

        # Render the monster's image, name card, and health bar
        self.screen.blit(battle_images["monster_pad"], (0, 300))
        self.screen.blit(battle_images["name_card"], (310, 300))
        self.screen.blit(battle_images["hp_bar"], (340, 335))

        # Render the player's monster's image
        self.screen.blit(self.player.monsters[0].image, (70, 250))

        # Render the opponent's monster's image, name card, and health bar
        self.screen.blit(battle_images["monster_pad"], (300, 100))
        self.screen.blit(battle_images["name_card"], (15, 100))
        self.screen.blit(battle_images["hp_bar"], (50, 135))
        self.screen.blit(battle_images["menu"], (0, 388))

        # Render the message
        img = font.render(self.message, True, WHITE)
        self.screen.blit(img, (30, 430))

        # Render the monster's image and name
        self.screen.blit(self.monster.image, (370, 30))
        img = font.render(str(self.monster.name), True, BLACK)
        self.screen.blit(img, (25, 110))

        # Render the monster's level
        img = font.render("Lv" + str(self.monster.level), True, BLACK)
        self.screen.blit(img, (260, 110))

        # Render the player's monster's name
        img = font.render(str(self.player.monsters[0].name), True, BLACK)
        self.screen.blit(img, (323, 311))

        # Render the player's monster's level
        img = font.render("Lv" + str(self.player.monsters[0].level), True, BLACK)
        self.screen.blit(img, (555, 311))

        # Calculate the monster's health percentage and determine its color
        monster_percent = self.monster.health / self.monster.base_health
        monster_color = self.determine_health_color(monster_percent)

        # Render the monster's health bar
        pygame.draw.rect(self.screen, monster_color, pygame.Rect(91, 137, BATTLE_HEALTH_BAR_WIDTH * monster_percent, 16))

        # Calculate the player's monster's health percentage and determine its color
        player_monster_percent = self.player.monsters[0].health / self.player.monsters[0].base_health
        player_monster_color = self.determine_health_color(player_monster_percent)

        # Render the player's monster's health bar
        pygame.draw.rect(self.screen, player_monster_color, pygame.Rect(381, 337, BATTLE_HEALTH_BAR_WIDTH * player_monster_percent, 16))

        # Render the monster's health and attack
        img = font.render("health: " + str(self.monster.health) + " Attack: " + str(self.monster.attack), True, BLACK)
        self.screen.blit(img, (25, 155))

        move = 1 #Inits move counter
        self.attack = Monster(MOVES[0]['base_attack'], 1) #inits monster base attack

    def opponentDamage(self): #opponent damage control
                opponent_move = random.choice(MOVES) #opponent picks randome move from MOVES array

                opponent_multiplier = 1 #inits multipliyer

                opponent_critical_hit = generate_random_number(1, 50) #inits probability of a crit
                opponent_miss = generate_random_number(1, 90) #inits probability of a miss

                #increases multipliyer if probability of crit is reached
                if opponent_critical_hit <= 2: 
                    opponent_multiplier += 1 
                    print("Opponent Critical hit")
                    self.message == "Opponent Critical hit"

                #zeroes multipliyer if probability of miss is reached
                elif opponent_miss <= 2:
                    opponent_multiplier *= 0
                    print("Opponent miss")
                    self.message == "Opponent Miss"

                # multiplys base attack by multipliyer to decide damage in hp.
                opponent_damage = opponent_move["base_attack"] * opponent_multiplier
                print(opponent_damage)
                print(opponent_multiplier)
                self.message == f"Opponent used {opponent_move['move_name']}"
                self.player.monsters[0].health -= opponent_damage #DAMAGES OPPONENT
    
    def damage(self,move):
        multiplier = 1 #INITS MULTIPLIYER   

        if move["effective_against"] == self.monster.type: #decides if move is effective by refrencing move effectivity chart versus oponent type
            multiplier += 0.5 #adds to multiplyer
            print("super")
            self.message == "Super"

        critical_hit = generate_random_number(1, 50) #crit probability
        miss = generate_random_number(1, 90)#miss probability

        #increases multipliyer if probability of crit is reached
        if critical_hit <= 2: 
            opponent_multiplier += 1 
            print("Opponent Critical hit")
            self.message == "Opponent Critical hit"

        #zeroes multipliyer if probability of miss is reached
        elif miss <= 2:
            opponent_multiplier *= 0
            print("Opponent miss")
            self.message == "Opponent Miss"

        damage = move["base_attack"] * multiplier #multiplis move base attack by multiplyer
        print(damage)
        self.message == damage
        print(multiplier)
        self.message == multiplier
        print(f"You used {move['move_name']}")
        self.message == f"You used {move['move_name']}"
        self.monster.health -= damage #damages opponent

        if self.monster.health >= 0: #if opponent still has health its opponents turn to damage
            self.opponentDamage()
    def update(self): #this is the part that is being called when in battle mode
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #if plaer closes screen ends code
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #if player tries to leave battle ends code
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_1: #1 is used as button map for pullup
                    for move in MOVES:
                        if move["move_name"] == "pullup":
                            self.damage(move) #calls damage  with pullup move

                if event.key == pygame.K_2: #2 is used as button map for insta kill
                    for move in MOVES:
                        if move["move_name"] == "killer":
                            self.damage(move) #calls damage with insta kill move

    #inits colours of health bar depending on halth percentage
    def determine_health_color(self, monster_percent):
        if monster_percent < .25:
            return RED
        if monster_percent < .7:
            return YELLOW
        return GREEN

#inits all images used in Battle
battle_images = {
    "monster_pad": pygame.transform.scale(pygame.image.load("Assets/monster_pad.png"), (300, 88)),
    "name_card": pygame.transform.scale(pygame.image.load("Assets/name_card.png"), (300, 80)),
    "hp_bar": pygame.transform.scale(pygame.image.load("Assets/hp_bar.png"), (250, 20)),
    "menu": pygame.image.load("Assets/menu.png"),
}


class Battle:
    def __init__(self, screen, monster, player):
        # Initialize the battle screen, monster, and player
        self.screen = screen
        self.monster = monster
        self.player = player
        self.message = "Press 1 to pullup!"

    def load(self):
        pass

    def render(self):
        # Fill the screen with white color
        self.screen.fill(WHITE)

        # Load the font
        font = pygame.font.Font("Assets/PokemonGb.ttf", 16)

        # Render the monster's image, name card, and health bar
        self.screen.blit(battle_images["monster_pad"], (0, 300))
        self.screen.blit(battle_images["name_card"], (310, 300))
        self.screen.blit(battle_images["hp_bar"], (340, 335))

        # Render the player's monster's image
        self.screen.blit(self.player.monsters[0].image, (70, 250))

        # Render the opponent's monster's image, name card, and health bar
        self.screen.blit(battle_images["monster_pad"], (300, 100))
        self.screen.blit(battle_images["name_card"], (15, 100))
        self.screen.blit(battle_images["hp_bar"], (50, 135))
        self.screen.blit(battle_images["menu"], (0, 388))

        # Render the message
        img = font.render(self.message, True, WHITE)
        self.screen.blit(img, (30, 430))

        # Render the monster's image and name
        self.screen.blit(self.monster.image, (370, 30))
        img = font.render(str(self.monster.name), True, BLACK)
        self.screen.blit(img, (25, 110))

        # Render the monster's level
        img = font.render("Lv" + str(self.monster.level), True, BLACK)
        self.screen.blit(img, (260, 110))

        # Render the player's monster's name
        img = font.render(str(self.player.monsters[0].name), True, BLACK)
        self.screen.blit(img, (323, 311))

        # Render the player's monster's level
        img = font.render("Lv" + str(self.player.monsters[0].level), True, BLACK)
        self.screen.blit(img, (555, 311))

        # Calculate the monster's health percentage and determine its color
        monster_percent = self.monster.health / self.monster.base_health
        monster_color = self.determine_health_color(monster_percent)

        # Render the monster's health bar
        pygame.draw.rect(self.screen, monster_color, pygame.Rect(91, 137, BATTLE_HEALTH_BAR_WIDTH * monster_percent, 16))

        # Calculate the player's monster's health percentage and determine its color
        player_monster_percent = self.player.monsters[0].health / self.player.monsters[0].base_health
        player_monster_color = self.determine_health_color(player_monster_percent)

        # Render the player's monster's health bar
        pygame.draw.rect(self.screen, player_monster_color, pygame.Rect(381, 337, BATTLE_HEALTH_BAR_WIDTH * player_monster_percent, 16))

        # Render the monster's health and attack
        img = font.render("health: " + str(self.monster.health) + " Attack: " + str(self.monster.attack), True, BLACK)
        self.screen.blit(img, (25, 155))

        move = 1 #Inits move counter
        self.attack = Monster(MOVES[0]['base_attack'], 1) #inits monster base attack

    def opponentDamage(self): #opponent damage control
                opponent_move = random.choice(MOVES) #opponent picks randome move from MOVES array

                opponent_multiplier = 1 #inits multipliyer

                opponent_critical_hit = generate_random_number(1, 50) #inits probability of a crit
                opponent_miss = generate_random_number(1, 90) #inits probability of a miss

                #increases multipliyer if probability of crit is reached
                if opponent_critical_hit <= 2: 
                    opponent_multiplier += 1 
                    print("Opponent Critical hit")
                    self.message == "Opponent Critical hit"

                #zeroes multipliyer if probability of miss is reached
                elif opponent_miss <= 2:
                    opponent_multiplier *= 0
                    print("Opponent miss")
                    self.message == "Opponent Miss"

                # multiplys base attack by multipliyer to decide damage in hp.
                opponent_damage = opponent_move["base_attack"] * opponent_multiplier
                print(opponent_damage)
                print(opponent_multiplier)
                self.message == f"Opponent used {opponent_move['move_name']}"
                self.player.monsters[0].health -= opponent_damage #DAMAGES OPPONENT
    
    def damage(self,move):
        multiplier = 1 #INITS MULTIPLIYER   

        if move["effective_against"] == self.monster.type: #decides if move is effective by refrencing move effectivity chart versus oponent type
            multiplier += 0.5 #adds to multiplyer
            print("super")
            self.message == "Super"

        critical_hit = generate_random_number(1, 50) #crit probability
        miss = generate_random_number(1, 90)#miss probability

        #increases multipliyer if probability of crit is reached
        if critical_hit <= 2: 
            opponent_multiplier += 1 
            print("Opponent Critical hit")
            self.message == "Opponent Critical hit"

        #zeroes multipliyer if probability of miss is reached
        elif miss <= 2:
            opponent_multiplier *= 0
            print("Opponent miss")
            self.message == "Opponent Miss"

        damage = move["base_attack"] * multiplier #multiplis move base attack by multiplyer
        print(damage)
        self.message == damage
        print(multiplier)
        self.message == multiplier
        print(f"You used {move['move_name']}")
        self.message == f"You used {move['move_name']}"
        self.monster.health -= damage #damages opponent

        if self.monster.health >= 0: #if opponent still has health its opponents turn to damage
            self.opponentDamage()

    def update(self): #this is the part that is being called when in battle mode
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #if plaer closes screen ends code
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #if player tries to leave battle ends code
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_1: #1 is used as button map for pullup
                    for move in MOVES:
                        if move["move_name"] == "pullup":
                            self.damage(move) #calls damage  with pullup move

                if event.key == pygame.K_2: #2 is used as button map for insta kill
                    for move in MOVES:
                        if move["move_name"] == "killer":
                            self.damage(move) #calls damage with insta kill move

    #inits colours of health bar depending on halth percentage
    def determine_health_color(self, monster_percent):
        if monster_percent < .25:
            return RED
        if monster_percent < .7:
            return YELLOW
        return GREEN

#inits all images used in Battle
battle_images = {
    "monster_pad": pygame.transform.scale(pygame.image.load("Assets/monster_pad.png"), (300, 88)),
    "name_card": pygame.transform.scale(pygame.image.load("Assets/name_card.png"), (300, 80)),
    "hp_bar": pygame.transform.scale(pygame.image.load("Assets/hp_bar.png"), (250, 20)),
    "menu": pygame.image.load("Assets/menu.png"),
}

class Map:
    def __init__(self, screen):
        # Initialize the Map object with a screen
        self.screen = screen
        self.map_array = []
        # Initialize the camera position to [0, 0]
        self.camera = [0, 0]
        self.file_name = None
        self.player_exit_position = None
        self.objects = []
        self.exit_positions = []

    def load(self, file_name, player):
        # Load a map from a file
        self.file_name = file_name

        self.player = player
        self.objects = [player]

        # Open the map file and read its contents
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)

        # Load the map configuration
        map_config = MAP_CONFIG[file_name]

        # Create NPC objects based on the map configuration
        for npc_data in map_config.get('npcs', []):
            npc = Npc(npc_data['name'], npc_data['image'], npc_data['start_position'][0], npc_data['start_position'][1])
            self.objects.append(npc)

        # Create Building objects based on the map configuration
        for building_data in map_config["buildings"]:
            building = Building(building_data['sprite'], building_data['position'], building_data['size'])
            self.objects.append(building)

        # Load the exit positions based on the map configuration
        for exit_position in map_config['exits']:
            self.exit_positions.append(exit_position)

    def load_room(self, map_name, room_name, player):
        # Load a room in a map
        self.player = player
        self.objects = [player]

        room_config = ROOM_CONFIG[map_name][str(room_name).zfill(2)]
        self.player.position = room_config['start_position'][:]
        self.player.player_exit_position = room_config['exit_position'][:]
        self.player_exit_position = room_config['exit_position'][:]

        # Create NPC objects based on the room configuration
        for npc_data in room_config['npcs']:
            npc = Npc(npc_data['name'], npc_data['image'], npc_data['start_position'][0], npc_data['start_position'][1])
            self.objects.append(npc)

        # Open the room file and read its contents
        with open('rooms' + map_name + '/' + str(room_name).zfill(2) + ".txt") as room_file:
            for line in room_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)

    def render(self, screen, player):
        # Render the map on the screen
        self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                if tile not in map_tile_image:
                    x_pos = x_pos + 1
                    continue
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * SCALE - (self.camera[0] * SCALE), y_pos * SCALE - (self.camera[1] * SCALE), SCALE, SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

        # draw all objects on map
        for object in self.objects:
            object.render(self.screen, self.camera)

    def determine_camera(self, player):
        # y axis
        max_y_position = len(self.map_array) - SCREEN_HEIGHT / SCALE
        y_position = player.position[1] - math.ceil(round(SCREEN_HEIGHT/ SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

        # x axis
        max_x_position = len(self.map_array[0]) - SCREEN_WIDTH / SCALE
        x_position = player.position[0] - math.ceil(round(SCREEN_WIDTH / SCALE / 2))

        if x_position <= max_x_position and x_position >= 0:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position

map_tile_image = { #Inits images for MapTiles for use when loading Tiles
    MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("Assets/grass.png"), (SCALE, SCALE)),
    MAP_TILE_STONE_FLOOR : pygame.transform.scale(pygame.image.load("Assets/Floor2.png"), (SCALE, SCALE)),
    MAP_TILE_STONE_WALL : pygame.transform.scale(pygame.image.load("Assets/BrickGrey.png"), (SCALE, SCALE)),
    MAP_TILE_BASKETBALL : pygame.transform.scale(pygame.image.load("Assets/Basketball.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDRT : pygame.transform.scale(pygame.image.load("Assets/CloudRT.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDT : pygame.transform.scale(pygame.image.load("Assets/CloudT.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDLT : pygame.transform.scale(pygame.image.load("Assets/CloudLT.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDL : pygame.transform.scale(pygame.image.load("Assets/CloudL.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDM : pygame.transform.scale(pygame.image.load("Assets/CloudM.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDR : pygame.transform.scale(pygame.image.load("Assets/CloudR.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDRB : pygame.transform.scale(pygame.image.load("Assets/CloudRB.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDB : pygame.transform.scale(pygame.image.load("Assets/CloudB.png"), (SCALE, SCALE)),
    MAP_TILE_CLOUDLB : pygame.transform.scale(pygame.image.load("Assets/CloudLB.png"), (SCALE, SCALE)),
    MAP_TILE_SHRUB : pygame.transform.scale(pygame.image.load("Assets/shrub.png"), (SCALE, SCALE)),
    MAP_TILE_WATER: pygame.transform.scale(pygame.image.load("Assets/water.png"), (SCALE, SCALE)),
    MAP_TILE_ROAD: pygame.transform.scale(pygame.image.load("Assets/road.png"), (SCALE, SCALE)),
    MAP_TILE_ROCK: pygame.transform.scale(pygame.image.load("Assets/rock.png"), (SCALE, SCALE)),
    MAP_TILE_BOULDER: pygame.transform.scale(pygame.image.load("Assets/Boulder.png"), (SCALE, SCALE)),
    MAP_TILE_MATRIX: pygame.transform.scale(pygame.image.load("Assets/Matrix.png"), (SCALE, SCALE)),
    MAP_TILE_FLOOR: pygame.transform.scale(pygame.image.load("Assets/FloorTile1.png"), (SCALE, SCALE)),
    MAP_TILE_WOOD_FLOOR: pygame.transform.scale(pygame.image.load("Assets/Floor1.png"), (SCALE, SCALE)),
    MAP_TILE_WALL: pygame.transform.scale(pygame.image.load("Assets/Brick1.png"), (SCALE, SCALE)),
    MAP_TILE_ASPHALT: pygame.transform.scale(pygame.image.load("Assets/Asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_WOOD_WALL: pygame.transform.scale(pygame.image.load("Assets/Wood.png"), (SCALE, SCALE)),
    MAP_TILE_LOCKER: pygame.transform.scale(pygame.image.load("Assets/Locker.png"), (SCALE, SCALE)),
    MAP_TILE_ROOM_EXIT: pygame.transform.scale(pygame.image.load("Assets/door.jpeg"), (SCALE, SCALE)),
    MAP_TILE_BUILDING : pygame.transform.scale(pygame.image.load("Assets/grass.png"), (SCALE, SCALE)),
    MAP_TILE_BIG_BUILDING : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_1 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_2 : pygame.transform.scale(pygame.image.load("Assets/grass.png"), (SCALE, SCALE)),
    MAP_TILE_3 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_4 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_5 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_6 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_7 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE)),
    MAP_TILE_8 : pygame.transform.scale(pygame.image.load("Assets/asphalt.png"), (SCALE, SCALE))
}

# Define a new class named Building
class Building:
    
    # Define the constructor method for the Building class
    def __init__(self, image_name, position, size):
        print("npc created")
        self.position = position[:]
        self.size = size[:]
        # Load the image for the building using the image_name argument
        self.image = pygame.image.load("Assets/" + str(image_name) + ".png")
        # Scale the image to the desired size using the SCALE constant
        self.image = pygame.transform.scale(self.image, (self.size[0] * SCALE, self.size[1] * SCALE))

    def update(self):
        pass

    # Define the render method for the Building class
    def render(self, screen, camera):
        # Calculate the position of the building on the screen, taking into account the camera position
        self.rect = pygame.Rect(self.position[0] * SCALE - (camera[0] * SCALE), self.position[1] * SCALE - (camera[1] * SCALE), SCALE, SCALE)
        # Draw the building image on the screen at the calculated position
        screen.blit(self.image, self.rect)

class MonsterFactory:
    def __init__(self):
        self.count = 0 #inits count of monster list

    def create_monster_index(self, index):
        monster = Monster(MONSTERS[index]['monster_type'], index) #indexes monster
        self.count = self.count + 1 #adds one to count
        return monster

    #function to create pokemon
    def create_monster(self, monster_type): 
        random_number = -1 

        if monster_type == "G": #if desired pokemon is grass type
            #generates random number in relaion to amount of grass pokemon in index
            random_number = generate_random_number(GRASS_TYPE_START, GRASS_TYPE_END) 
        
        #sends monster type and random pokemon generated to Monster class
        monster = Monster(monster_type, random_number)
        self.count = self.count + 1 # adds one to count

        return monster #returns monster created
    
#init function used for generating random num
def generate_random_number(range1, range2): 
    seed()
    return randint(range1, range2)

#function used to check if player walking on map_tile, otherwise error.(exception handeling)
def test_if_int(map_tile):
    try:
        int(map_tile)
        return True
    except ValueError:
        return False

#inits everything used for Monster
class Monster:
    def __init__(self, monster_type, id):
        self.type = monster_type
        self.health = 10
        self.attack = 10
        self.id = id
        self.image = pygame.image.load("Assets/" + f"{self.id:03d}" + ".png") #used for creating image of monster
        self.name = MONSTERS[id]['name']
        self.level = MONSTERS[id]['level_start']
        self.base_health = MONSTERS[id]['base_health']

#used to indicate Game State and toggeling between Menu/Running/Quit
class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2

#used to indicate Game State when running and toggeling between Map and battle types
class CurrentGameState(Enum):
    MAP = 0,
    BATTLE = 1
    TBATTLE = 2

#Class used for creating event used to pick begginer monster
class PickMonsterEvent:
    def __init__(self, screen, game, player, monster):
        self.screen = screen
        self.game = game
        self.player = player
        self.dialog = pygame.image.load("Assets/dialog.png")
        self.monster_factory = MonsterFactory()

        #if player walks into computer creates corresponding pokemon from index
        if monster.name == "computer_1":
            self.monster = self.monster_factory.create_monster_index(1)
        elif monster.name == "computer_2":
            self.monster = self.monster_factory.create_monster_index(2)
        elif monster.name == "computer_3":
            self.monster = self.monster_factory.create_monster_index(4)

        self.cut = 0
        self.max_cut = 0

    def load(self):
        pass

    #when initial interact rednersc scene 0
    def render(self):
        if self.cut == 0:
            self.render_scene_0()

    #scene zero shows player pokemon choen + Asks if player would like to pick pokemon
    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        self.screen.blit(self.monster.image, (100, 100))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("you picked.... " + str(self.monster.name), True, BLACK)
        self.screen.blit(img, (40, 350))
        img = font.render("are you sure? (y/n)", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    #waits till all scenes are over
    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        #monitors input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_y: #if player picks y then corresponding pokemon is attached to player type and ends dialogue
                    self.player.monsters.append(self.monster)
                    self.game.event = None
                elif event.key == pygame.K_n: #if player says n then ends dialogue with no furtehr action
                    self.game.event = None

#Event for initial interaction with Mr.Bhinder
class ProfPickMonsterEvent:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        self.prof_image = pygame.image.load("Assets/Bhinder.png")#Describes expected image of the proffesor
        self.dialog = pygame.image.load("Assets/dialog.png")#inits dialogue

        #inits current cut
        self.cut = 0 
        #inits max number of scenes
        self.max_cut = 3

    def load(self):
        pass
    
    #renders all scens based on cut value
    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        elif self.cut == 2:
            self.render_scene_2()
        elif self.cut == 3:
            self.render_scene_3()

    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("hello, I am Mr.Bhinder", True, BLACK)
        self.screen.blit(img, (40, 400))


        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("pick your monster!", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("chose wisely...!", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_3(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Once you pick one talk to owen.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                # when player clicks return key advances to next cut and scene
                if event.key == pygame.K_RETURN: 
                    self.cut = self.cut + 1


#Trainer event (calls TBatte)
class Trainer:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.TBattle = TBattle
        self.Tbattle = None

        self.monsterfight = game.monster_factory.create_monster("G") #shows which pokemon should be created for monster fight
        self.trainer_image = pygame.image.load("Assets/Trainer.png")
        self.dialog = pygame.image.load("Assets/dialog.png")

        self.cut = 0
        self.max_cut = 2

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        #on the second cut (3rd scene) player battles Trainer
        elif self.cut == 2:
            self.Tbattle = TBattle(self.screen, self.monsterfight , self.player) #Tbattle is called to init fight
            game.current_game_state = CurrentGameState.TBATTLE
            
            
    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("YOU WANNA FIGHT BRO?", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("DIE!", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1

#owen1 is first interaction with rival. Exact same as Trainer but with dialogue options to advance player through the game
class Owen1:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.TBattle = TBattle
        self.Tbattle = None

        self.monsterfight = game.monster_factory.create_monster("G")
        self.trainer_image = pygame.image.load("Assets/Trainer.png")
        self.dialog = pygame.image.load("Assets/dialog.png")

        self.cut = 0
        self.max_cut = 4

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        elif self.cut == 2:
            self.render_scene_2()
        elif self.cut == 3:
            self.Tbattle = TBattle(self.screen, self.monsterfight , self.player)
            game.current_game_state = CurrentGameState.TBATTLE
        elif self.cut == 4:
            self.render_scene_3()
            
    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Oh hey Ibrahim. You got a pokemnon?", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Let's Battle!", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("I bet 5$ I will beat you.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_3(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Damn! Go to Alton Villiage through the forest.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1

#Same as Trainer but with Dialogue to advance player to final battles
class Nitish:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.TBattle = TBattle
        self.Tbattle = None

        self.monsterfight = game.monster_factory.create_monster("G")
        self.trainer_image = pygame.image.load("Assets/Trainer.png")
        self.dialog = pygame.image.load("Assets/dialog.png")

        self.cut = 0
        self.max_cut = 5

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        elif self.cut == 2:
            self.render_scene_2()
        elif self.cut == 3:
            self.Tbattle = TBattle(self.screen, self.monsterfight , self.player)
            game.current_game_state = CurrentGameState.TBATTLE
        elif self.cut == 4:
            self.render_scene_3()
        elif self.cut == 5:
            game.game_state == GameState.NONE
            
    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Ibrahim? Your tryit to be champion?", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Well you have to beat me first.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Good Luck, you need it", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_3(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("GG. Walk in front of Computer to continue.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1

#Final battle
class Owen2:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.TBattle = TBattle
        self.Tbattle = None

        self.monsterfight = game.monster_factory.create_monster("G")
        self.trainer_image = pygame.image.load("Assets/Trainer.png")
        self.dialog = pygame.image.load("Assets/dialog.png")

        self.cut = 0
        self.max_cut = 5

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        elif self.cut == 2:
            self.render_scene_2()
        elif self.cut == 3:
            self.Tbattle = TBattle(self.screen, self.monsterfight , self.player)
            game.current_game_state = CurrentGameState.TBATTLE
        elif self.cut == 4:
            self.render_scene_3()
        #Once Owen is defeated loads menu as a game over indentifiying the player has complete the game
        elif self.cut == 5:
            game.game_state == GameState.NONE
            
    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Oh hey Ibrahim. Wow you are strong.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Let's decide whos stronger once and for all.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Lets do this", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_3(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Wow...You won. Thanks for playing.", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1

#Heal class often seen throught the game to heal players pokemon 
class Heal:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player

        self.prof_image = pygame.image.load("Assets/Nurse.png")
        self.dialog = pygame.image.load("Assets/dialog.png")

        self.cut = 0
        self.max_cut = 2

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        elif self.cut == 2:
            self.render_scene_2()

    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Welcome Back", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("Let me heal your monster", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('Assets/PokemonGb.ttf', 20)
        img = font.render("I healed it!", True, BLACK)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1

        self.player.monsters[0].health = 10 # ensures players health is back to its initial stary health

#Handles heal event
def handle_heal_event(game, player):
    if len(player.monsters) == 0: #if player has no pokemon does not allow heal to take place (exception handeling)
        return
    
    event = Heal(game.screen, game, player)#otherwisee game event calls Heal class
    game.event = event #loads event state in game class
#handles i itial talk to bhinder
def handle_prof_event(game, player, npc):
    if len(player.monsters) != 0:
        return
    event = ProfPickMonsterEvent(game.screen, game)#calls ProfPickMonsterEvent class
    game.event = event

def handle_pick_monster_event(game, player, npc):
    if len(player.monsters) != 0: # esures event only runs if player has no pokemon to ensure no duplicate clauses
        return

    event = PickMonsterEvent(game.screen, game, player, npc) #calls pick monster event
    game.event = event

def handle_owen1_event(game, player, npc):
    if len(player.monsters) == 0: #Ensures event only runs if player has pokemon
        return
    
    event = Owen1(game.screen, game, player)#loads Owen 1 Class
    game.event = event

def handle_owen2_event(game, player, npc):
    if len(player.monsters) == 0:
        return
    
    event = Owen2(game.screen, game, player)
    game.event = event

def handle_nitish_event(game, player, npc):
    if len(player.monsters) == 0:
        return
    
    event = Nitish(game.screen, game, player)
    game.event = event


def handle_trainer_event(game, player, npc):
    if len(player.monsters) == 0:
        return
    
    event = Trainer(game.screen, game, player)
    game.event = event

#Handle class checks if player on same tile as NPC to call corresponding handle_event
def handle(game, player, npc): 
    player.position = player.last_position
    
    if npc.name == 'Trainer': #if players position on npc Trainer then Handle Trainer event function is called to run Trainer event class
        handle_trainer_event(game, player, npc)
    pass

    if npc.name == 'Owen1':
        handle_owen1_event(game, player, npc)
    pass

    if npc.name == 'Owen2':
        handle_owen2_event(game, player, npc)
    pass

    if npc.name == 'Nitish':
        handle_nitish_event(game, player, npc)
    pass

    if npc.name == 'Bhinder':# multiple events atrubuted to depend on if player has pokemon or not
        handle_heal_event(game, player)
        handle_prof_event(game, player, npc)
    pass

    if npc.name == 'Nurse':
        handle_heal_event(game, player)
    pass

    if npc.name.startswith("computer_"):
        handle_pick_monster_event(game, player, npc)

    pass


class Npc:
    def __init__(self, name, image, x_postition, y_position):
 # Initialize the Npc object with a name, image, and starting position
        print("npc created")
        self.name = name
        self.position = [x_postition, y_position]
        self.image = pygame.image.load("Assets/" + str(image) + ".png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)
        self.monster = None
        self.monsters = []

    def update(self):
        # Update the Npc object
        print("npc updated")

    def update_position(self, new_position):
        #inits NPC position
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def render(self, screen, camera):
        # Render the Npc on the screen
        self.rect = pygame.Rect(self.position[0] * SCALE - (camera[0] * SCALE), self.position[1] * SCALE - (camera[1] * SCALE), SCALE, SCALE)#create NPC on tile and scale accordingly
        screen.blit(self.image, self.rect)


class Player:
    #Initilising function iwth parameters
    def __init__(self, x_postition, y_position):
        self.position = [x_postition, y_position] #inits spawn position
        self.last_position = [x_postition, y_position] #variable that holds last known position of player
        self.image = pygame.image.load("Assets/IbrahimSprite.png") #photo asset used when spawning player
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))#inits Image scaling
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)#creates box for position and scale of player
        self.monster = None #inits the pokemon that the Player has
        self.monsters = []

    #update function
    def update(self):
        print("player updated")

    #update position function alowing for movement mechanics
    def update_position(self, new_position):
        self.last_position = self.position[:]
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    #render function to render the players view point(camera)
    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * SCALE - (camera[0] * SCALE), self.position[1] * SCALE - (camera[1] * SCALE), SCALE, SCALE)
        screen.blit(self.image, self.rect)

#Menu event class
class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def set_up(self):
        self.menu_image = pygame.image.load("Assets/menu.png")#Image for menu on start

    #update of menu +meny background function
    def update(self):
        self.screen.fill(BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.menu_image, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_RETURN: # Starts game 
                    self.game.set_up()
                    self.game.game_state = GameState.RUNNING

#Game class (where all processing originates to)
class Game:
    #inits gamstates, monsters, Map, etc
    def __init__(self, screen):
        self.screen = screen
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()
        self.map = Map(screen)
        self.maps = [self.map]
        self.battle = None
        self.player = None
        self.event = None

    #sets up player and start map
    def set_up(self):
        player = Player(7, 29)
        self.player = player
        print("do set up")
        self.game_state = GameState.RUNNING

        self.map.load("01", self.player)

#updates depending on player input
    def update(self):
        if self.current_game_state == CurrentGameState.MAP: #when running on map
            self.player_has_moved = False #checks for player movement
            self.screen.fill(BLACK)
            # print("update")
            self.handle_events()#checks for events activated

            if self.player_has_moved:
                self.determine_game_events()#when player moves checks for events

            self.map.render(self.screen, self.player)

        elif self.current_game_state == CurrentGameState.BATTLE: #when on Battle sate
            self.battle.update()#update Battle
            self.battle.render()#render battle scene

            if self.battle.monster.health <= 0:#if pokemon halth of opponent = 0 back to map
                self.current_game_state = CurrentGameState.MAP

        elif self.current_game_state == CurrentGameState.TBATTLE:
            self.event.Tbattle.update()
            self.event.Tbattle.render()

            # Check and set Trainer Monster's health
            if self.event.Tbattle.monster.health <= 0:
                self.current_game_state = CurrentGameState.MAP
                

            # Check and set Player's Monster's health
            if self.event.Tbattle.player.monsters[0].health <= 0:
                self.current_game_state = CurrentGameState.MAP


        #if event none
        if self.event is not None:
            self.event.render()#render menu
            self.event.update()#update menu

    def determine_game_events(self):#determies any events that happen
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]] #checks for event tiles
        print(map_tile)

        if map_tile == MAP_TILE_ROOM_EXIT: #if on Room exit tile
            self.player.position = self.map.player_exit_position[:] #moves player to exit position specified in config
            self.maps.pop()
            self.map = self.maps[-1]
            return

        # if the map tile is a door, we need a room
        if test_if_int(map_tile):
            room = Map(self.screen) #creates object in Map class
            room.load_room(self.map.file_name, map_tile, self.player) #loads room
            self.map = room
            self.maps.append(room)#appends room s configured
            return

        for npc in self.map.objects:
            if npc == self.map.player:
                continue

            if npc.position[:] == self.map.player.position[:]: #if player stood on the position of NPC chekcs which event to handle
                handle(self, self.player, npc)

        for exit_position in self.map.exit_positions: #if player moves on exit map tile
            if self.player.position[:] == exit_position['position'][:]:
                map_file = exit_position['map']
                map = Map(self.screen)

                MAP_CONFIG[map_file]['start_position'] = exit_position['new_start_position'][:] #chekcs for new starting posiition in Congifurator

                map.load(map_file, self.player)#loads map
                self.player.position = MAP_CONFIG[map_file]['start_position']#moves player to start position
                self.maps.pop()
                self.map = map
                self.maps.append(map)#appends new map

        if self.player.monsters:
            self.determine_monster_found(map_tile)

    def determine_monster_found(self, map_tile):
        if map_tile not in MONSTER_TYPES: #if player stands on tile capable of spawning pokemon
            return

        random_number = generate_random_number(1, 10)

        # 20 percent chance of hitting monster
        if random_number <= 2:
            found_monster = self.monster_factory.create_monster(map_tile)
            print("you found a monster!")
            print("Monster Type: " + found_monster.type)
            print("Attack: " + str(found_monster.attack))
            print("Health: " + str(found_monster.health))

            self.battle = Battle(self.screen, found_monster, self.player)
            self.current_game_state = CurrentGameState.BATTLE

    def handle_events(self): #handle events (player input)
        if self.event is not None:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.NONE
                elif event.key == pygame.K_w: # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s: # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a: # left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d: # right
                    self.move_unit(self.player, [1, 0])

    #moves entire map when player moves torwards direction not loaded in
    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # check if off map
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return

        # check for valid movement
        if self.map.map_array[new_position[1]][new_position[0]] in IMPASSIBLE:
            return

        self.player_has_moved = True

        unit.update_position(new_position)

#initilises pygame
pygame.init()

#initislising pygame box screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Monster")

#tick clock from pygame library (FPS)
clock = pygame.time.Clock()

#creates game pbject in Game class
game = Game(screen)

menu = Menu(screen, game)
menu.set_up()

#chekcs 50 rimes a second for Quit of pygame, pause(menu), or running to update game 50 times a second
while game.game_state != GameState.ENDED:
    clock.tick(50)

    if game.game_state == GameState.NONE:
        menu.update()

    if game.game_state == GameState.RUNNING:
        game.update()

    pygame.display.flip()#updates display 50 times a second
