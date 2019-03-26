"""
Sprites are simply filtered emojis.
Explore this file for a complete list.
All emoji codes from: https://unicode.org/emoji/charts/full-emoji-list.html

The complete list of aliased emojis is:
    * COWBOY = '\U0001F920'
    * DEAMON_HAPPY = '\U0001F608'
    * DAEMON_ANGRY = '\U0001F47F'
    * SKULL = '\U0001F480'
    * SKULL_CROSSBONES = '\U00002620'
    * POO = '\U0001F4A9'
    * CLOWN = '\U0001F921'
    * OGRE = '\U0001F479'
    * HAPPY_GHOST = '\U0001F47B'
    * ALIEN = '\U0001F47D'
    * ALIEN_MONSTER = '\U0001F47E'
    * ROBOT = '\U0001F916'
    * CAT = '\U0001F408'
    * CAT_FACE = '\U0001F63A'
    * CAT_LOVE = '\U0001F63B'
    * CAT_WEARY = '\U0001F640'
    * CAT_CRY = '\U0001F63F'
    * CAT_ANGRY = '\U0001F63E'
    * HEART = '\U00002764'
    * HEART_SPARKLING = '\U0001F496'
    * HEART_BROKEN = '\U0001F494'
    * HEART_ORANGE = '\U0001F9E1'
    * HEART_YELLOW = '\U0001F49B'
    * HEART_GREEN = '\U0001F49A'
    * HEART_BLUE = '\U0001F499'
    * EXPLOSION = '\U0001F4A5'
    * DIZZY = '\U0001F4AB'
    * DASH = '\U0001F4A8'
    * HOLE = '\U0001F573'
    * BOMB = '\U0001F4A3'
    * BRAIN = '\U0001F9E0'
    * BOY = '\U0001F466'
    * GIRL = '\U0001F467'
    * MAN = '\U0001F468'
    * MAN_BEARD = '\U0001F9D4'
    * WOMAN = '\U0001F469'
    * WOMAN_BLOND = '\U0001F471'
    * MAN_OLD = '\U0001F474'
    * WOMAN_OLD = '\U0001F475'
    * POLICE = '\U0001F46E'
    * SUPER_HERO = '\U0001F9B8'
    * SUPER_VILAIN = '\U0001F9B9'
    * MAGE = '\U0001F9D9'
    * FAIRY = '\U0001F9DA'
    * VAMPIRE = '\U0001F9DB'
    * MERMAID = '\U0001F9DC'
    * ELF = '\U0001F9DD'
    * GENIE = '\U0001F9DE'
    * ZOMBIE = '\U0001F9DF'
    * PERSON_RUNNING = '\U0001F469'
    * PERSON_WALKING = '\U0001F6B6'
    * PERSON_FENCING = '\U0001F93A'
    * PERSON_SLEEPING = '\U0001F6CC'
    * PERSON_YOGA = '\U0001F9D8'
    * PERSON_BATHING = '\U0001F6C0'
    * MONKEY = '\U0001F435'
    * GORILLA = '\U0001F98D'
    * DOG = '\U0001F415'
    * DOG_FACE = '\U0001F436'
    * WOLF_FACE = '\U0001F43A'
    * FOX_FACE = '\U0001F98A'
    * RACCOON_FACE = '\U0001F99D'
    * LION_FACE = '\U0001F981'
    * TIGER_FACE = '\U0001F42F'
    * HORSE_FACE = '\U0001F434'
    * HORSE = '\U0001F40E'
    * UNICORN_FACE = '\U0001F984'
    * DEER_FACE = '\U0001F98C'
    * COW_FACE = '\U0001F42E'
    * COW = '\U0001F404'
    * OX = '\U0001F402'
    * BUFFALO = '\U0001F403'
    * PIG = '\U0001F416'
    * PIG_FACE = '\U0001F437'
    * RAM = '\U0001F40F'
    * SHEEP = '\U0001F411'
    * GOAT = '\U0001F410'
    * LLAMA = '\U0001F999'
    * GIRAFFE = '\U0001F992'
    * ELEPHANT = '\U0001F418'
    * RHINOCEROS_FACE = '\U0001F98F'
    * MOUSE = '\U0001F401'
    * RABBIT = '\U0001F407'
    * CHIPMUNK = '\U0001F43F'
    * BAT = '\U0001F987'
    * PANDA_FACE = '\U0001F43C'
    * TURKEY = '\U0001F983'
    * CHICKEN = '\U0001F414'
    * CHICK = '\U0001F425'
    * EAGLE = '\U0001F985'
    * DUCK = '\U0001F986'
    * OWL = '\U0001F989'
    * FROG_FACE = '\U0001F438'
    * CROCODILE = '\U0001F40A'
    * TURTLE = '\U0001F422'
    * LIZARD = '\U0001F98E'
    * SNAKE = '\U0001F40D'
    * DRAGON = '\U0001F409'
    * DINOSAUR = '\U0001F995'
    * TREX = '\U0001F996'
    * WHALE = '\U0001F433'
    * DOLPHIN = '\U0001F42C'
    * SHARK = '\U0001F988'
    * OCTOPUS = '\U0001F419'
    * SPIDER = '\U0001F577'
    * SPIDER_WEB = '\U0001F578'
    * SCORPION = '\U0001F982'
    * MICROBE = '\U0001F9A0'
    * SUNFLOWER = '\U0001F33B'
    * CHERRY_BLOSSOM = '\U0001F338'
    * FLOWER = '\U0001F33C'
    * ROSE = '\U0001F339'
    * TREE_PINE = '\U0001F332'
    * TREE = '\U0001F333'
    * TREE_PALM = '\U0001F334'
    * CACTUS = '\U0001F335'
    * CLOVER = '\U00002618'
    * CLOVER_LUCKY = '\U0001F340'
    * CHEESE = '\U0001F9C0'
    * MEAT_BONE = '\U0001F356'
    * MEAT = '\U0001F969'
    * BACON = '\U0001F953'
    * EGG = '\U0001F95A'
    * CRAB = '\U0001F980'
    * LOBSTER = '\U0001F99E'
    * SHRIMP = '\U0001F990'
    * SQUID = '\U0001F991'
    * KNIFE = '\U0001F52A'
    * AMPHORA = '\U0001F3FA'
    * EARTH_GLOBE = '\U0001F30D'
    * WALL = '\U0001F9F1'
    * HOUSE = '\U0001F3E0'
    * CASTLE = '\U0001F3F0'
    * MON = '\U000026E9'
    * FOUNTAIN = '\U000026F2'
    * ROCKET = '\U0001F680'
    * FLYING_SAUCER = '\U0001F6F8'
    * HOURGLASS = '\U000022F3'
    * CYCLONE = '\U0001F300'
    * RAINBOW = '\U0001F308'
    * ZAP = '\U000026A1'
    * SNOWMAN = '\U00002603'
    * COMET = '\U00002604'
    * FIRE = '\U0001F525'
    * WATER_DROP = '\U0001F4A7'
    * JACK_O_LANTERN = '\U0001F383'
    * DYNAMITE = '\U0001F9E8'
    * SPARKLES = '\U00002728'
    * GIFT = '\U0001F381'
    * TROPHY = '\U0001F3C6'
    * CROWN = '\U0001F451'
    * GEM_STONE = '\U0001F48E'
    * CANDLE = '\U0001F56F'
    * LIGHT_BULB = '\U0001F4A1'
    * BOOK_OPEN = '\U0001F4D6'
    * SCROLL = '\U0001F4DC'
    * MONEY_BAG = '\U0001F4B0'
    * BANKNOTE_DOLLARS = '\U0001F4B5'
    * BANKNOTE_EUROS = '\U0001F4B6'
    * BANKNOTE_WINGS = '\U0001F4B8'
    * DOLLAR = '\U0001F4B2'
    * LOCKED = '\U0001F512'
    * UNLOCKED = '\U0001F513'
    * KEY = '\U0001F5DD'
    * PICK = '\U000026CF'
    * SWORD = '\U0001F5E1'
    * SWORD_CROSSED = '\U00002694'
    * PISTOL = '\U0001F52B'
    * BOW = '\U0001F3F9'
    * SHIELD = '\U0001F6E1'
    * COFFIN = '\U000026B0'
    * RADIOACTIVE = '\U00002622'
    * FLAG_GOAL = '\U0001F3C1'
        
"""

COWBOY = '\U0001F920'
DEAMON_HAPPY = '\U0001F608'
DAEMON_ANGRY = '\U0001F47F'
SKULL = '\U0001F480'
SKULL_CROSSBONES = '\U00002620'
POO = '\U0001F4A9'
CLOWN = '\U0001F921'
OGRE = '\U0001F479'
HAPPY_GHOST = '\U0001F47B'
ALIEN = '\U0001F47D'
ALIEN_MONSTER = '\U0001F47E'
ROBOT = '\U0001F916'
CAT = '\U0001F408'
CAT_FACE = '\U0001F63A'
CAT_LOVE = '\U0001F63B'
CAT_WEARY = '\U0001F640'
CAT_CRY = '\U0001F63F'
CAT_ANGRY = '\U0001F63E'
HEART = '\U00002764'
HEART_SPARKLING = '\U0001F496'
HEART_BROKEN = '\U0001F494'
HEART_ORANGE = '\U0001F9E1'
HEART_YELLOW = '\U0001F49B'
HEART_GREEN = '\U0001F49A'
HEART_BLUE = '\U0001F499'
EXPLOSION = '\U0001F4A5'
DIZZY = '\U0001F4AB'
DASH = '\U0001F4A8'
HOLE = '\U0001F573'
BOMB = '\U0001F4A3'
BRAIN = '\U0001F9E0'
BOY = '\U0001F466'
GIRL = '\U0001F467'
MAN = '\U0001F468'
MAN_BEARD = '\U0001F9D4'
WOMAN = '\U0001F469'
WOMAN_BLOND = '\U0001F471'
MAN_OLD = '\U0001F474'
WOMAN_OLD = '\U0001F475'
POLICE = '\U0001F46E'
SUPER_HERO = '\U0001F9B8'
SUPER_VILAIN = '\U0001F9B9'
MAGE = '\U0001F9D9'
FAIRY = '\U0001F9DA'
VAMPIRE = '\U0001F9DB'
MERMAID = '\U0001F9DC'
ELF = '\U0001F9DD'
GENIE = '\U0001F9DE'
ZOMBIE = '\U0001F9DF'
PERSON_RUNNING = '\U0001F469'
PERSON_WALKING = '\U0001F6B6'
PERSON_FENCING = '\U0001F93A'
PERSON_SLEEPING = '\U0001F6CC'
PERSON_YOGA = '\U0001F9D8'
PERSON_BATHING = '\U0001F6C0'
MONKEY = '\U0001F435'
GORILLA = '\U0001F98D'
DOG = '\U0001F415'
DOG_FACE = '\U0001F436'
WOLF_FACE = '\U0001F43A'
FOX_FACE = '\U0001F98A'
RACCOON_FACE = '\U0001F99D'
LION_FACE = '\U0001F981'
TIGER_FACE = '\U0001F42F'
HORSE_FACE = '\U0001F434'
HORSE = '\U0001F40E'
UNICORN_FACE = '\U0001F984'
DEER_FACE = '\U0001F98C'
COW_FACE = '\U0001F42E'
COW = '\U0001F404'
OX = '\U0001F402'
BUFFALO = '\U0001F403'
PIG = '\U0001F416'
PIG_FACE = '\U0001F437'
RAM = '\U0001F40F'
SHEEP = '\U0001F411'
GOAT = '\U0001F410'
LLAMA = '\U0001F999'
GIRAFFE = '\U0001F992'
ELEPHANT = '\U0001F418'
RHINOCEROS_FACE = '\U0001F98F'
MOUSE = '\U0001F401'
RABBIT = '\U0001F407'
CHIPMUNK = '\U0001F43F'
BAT = '\U0001F987'
PANDA_FACE = '\U0001F43C'
TURKEY = '\U0001F983'
CHICKEN = '\U0001F414'
CHICK = '\U0001F425'
EAGLE = '\U0001F985'
DUCK = '\U0001F986'
OWL = '\U0001F989'
FROG_FACE = '\U0001F438'
CROCODILE = '\U0001F40A'
TURTLE = '\U0001F422'
LIZARD = '\U0001F98E'
SNAKE = '\U0001F40D'
DRAGON = '\U0001F409'
DINOSAUR = '\U0001F995'
TREX = '\U0001F996'
WHALE = '\U0001F433'
DOLPHIN = '\U0001F42C'
SHARK = '\U0001F988'
OCTOPUS = '\U0001F419'
SPIDER = '\U0001F577'
SPIDER_WEB = '\U0001F578'
SCORPION = '\U0001F982'
MICROBE = '\U0001F9A0'
SUNFLOWER = '\U0001F33B'
CHERRY_BLOSSOM = '\U0001F338'
FLOWER = '\U0001F33C'
ROSE = '\U0001F339'
TREE_PINE = '\U0001F332'
TREE = '\U0001F333'
TREE_PALM = '\U0001F334'
CACTUS = '\U0001F335'
CLOVER = '\U00002618'
CLOVER_LUCKY = '\U0001F340'
CHEESE = '\U0001F9C0'
MEAT_BONE = '\U0001F356'
MEAT = '\U0001F969'
BACON = '\U0001F953'
EGG = '\U0001F95A'
CRAB = '\U0001F980'
LOBSTER = '\U0001F99E'
SHRIMP = '\U0001F990'
SQUID = '\U0001F991'
KNIFE = '\U0001F52A'
AMPHORA = '\U0001F3FA'
EARTH_GLOBE = '\U0001F30D'
WALL = '\U0001F9F1'
HOUSE = '\U0001F3E0'
CASTLE = '\U0001F3F0'
MON = '\U000026E9'
FOUNTAIN = '\U000026F2'
ROCKET = '\U0001F680'
FLYING_SAUCER = '\U0001F6F8'
HOURGLASS = '\U000022F3'
CYCLONE = '\U0001F300'
RAINBOW = '\U0001F308'
ZAP = '\U000026A1'
SNOWMAN = '\U00002603'
COMET = '\U00002604'
FIRE = '\U0001F525'
WATER_DROP = '\U0001F4A7'
JACK_O_LANTERN = '\U0001F383'
DYNAMITE = '\U0001F9E8'
SPARKLES = '\U00002728'
GIFT = '\U0001F381'
TROPHY = '\U0001F3C6'
CROWN = '\U0001F451'
GEM_STONE = '\U0001F48E'
CANDLE = '\U0001F56F'
LIGHT_BULB = '\U0001F4A1'
BOOK_OPEN = '\U0001F4D6'
SCROLL = '\U0001F4DC'
MONEY_BAG = '\U0001F4B0'
BANKNOTE_DOLLARS = '\U0001F4B5'
BANKNOTE_EUROS = '\U0001F4B6'
BANKNOTE_WINGS = '\U0001F4B8'
DOLLAR = '\U0001F4B2'
LOCKED = '\U0001F512'
UNLOCKED = '\U0001F513'
KEY = '\U0001F5DD'
PICK = '\U000026CF'
SWORD = '\U0001F5E1'
SWORD_CROSSED = '\U00002694'
PISTOL = '\U0001F52B'
BOW = '\U0001F3F9'
SHIELD = '\U0001F6E1'
COFFIN = '\U000026B0'
RADIOACTIVE = '\U00002622'
FLAG_GOAL = '\U0001F3C1'

