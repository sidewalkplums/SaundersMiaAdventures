import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
mc = minecraft.Minecraft.create()

#SKY HUNT CODE
score = 0
RANGE = 5
treasure_x = None # the x coordinate of the treasure
treasure_y = None
treasure_z = None
bridge = []

def placeTreasure():
    global treasure_x, treasure_y, treasure_z
    pos = mc.player.getTilePos()
    treasure_x = random.randint (pos.x, pos.x + RANGE)
    treasure_y = random.randint (pos.y + 2, pos.y + RANGE)
    treasure_z = random.randint (pos.z, pos.z + RANGE)
    mc.setBlock (treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)


def buildBridge():
    global score
    pos = mc.player.getTilePos()
    b = mc.getBlock (pos.x, pos.y - 1, pos.z)

    if  treasure_x == None:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate [0], coordinate [1], coordinate [2], block.AIR.id)
            mc.postToChat("bridge:" + str(len(bridge)))
            time.sleep(0.25)

    elif b != block.GOLD_BLOCK.id:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GOLD_BLOCK.id)
        coordinate = [pos.x, pos.y-1, pos.z]
        bridge.append(coordinate)
        score = score - 1

def checkHit():
    global score
    global treasure_x
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == treasure_x and pos.y == treasure_y and pos.z == treasure_z:
            mc.postToChat ("Hit!")
            score = score + 10
            mc.setBlock(treasure_x, treasure_y, treasure_z, block.AIR.id)
            treasure_x = None

TIMEOUT = 10
timer = TIMEOUT 

def homingBeacon():
    global timer
    if treasure_x != None:
        timer = timer - 1
        if timer == 0:
            timer = TIMEOUT 
            pos = mc.player.getTilePos()
            diffx = abs(pos.x - treasure_x)
            diffy = abs(pos.y - treasure_y)
            diffz = abs(pos.z - treasure_z)
            diff = diffx + diffy + diffz
            mc.postToChat ("score: " + str(score) + "treasure: " + str(diff)) 

while True:
    time.sleep(1)

    if treasure_x == None and len(bridge) == 0:
        placeTreasure()
    
    checkHit()
    homingBeacon()
    buildBridge()

 
#SAFE FEET CODE:
'''def safeFeet():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.postToChat("Unsafe waters, do not proceed")
    else:
        mc.PostToChat("Safe")
while True:
    time.sleep(0.5)
    safeFeet()'''

#BUILD BRIDGE CODE:
'''def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GLASS.id)
while True:
    buildBridge()

a = [] # empty list
print (a)
a.append("hi")
print (a)
print (len(a))
print (a[0]) # the [0] is the index of the first item
print (a[1]) # the index of the second item
word = a.pop()
print(word)
print(a)
print(len(a))
print(len(word))
word = a.pop()
print(word)
print(a)
print(len(a))'''

#VANISHING BRIDGE CODE:
'''bridge = []
def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)

    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id or b == block.LAVA_FLOWING.id or b == block.LAVA_STATIONARY.id:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GLASS.id)
        coordinate = [pos.x, pos.y - 1, pos.z]
        bridge.append(coordinate)
    elif b != block.GLASS.id:
        if len (bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate [1], coordinate [2], block.AIR.id)
        time.sleep(0.25)

while True:
    buildBridge()'''

#BLOCK HIT CODE:
'''diamond_pos = mc.player.getTilePos()
diamond_pos.x = diamond_pos.x + 1
mc.setBlock(diamond_pos.x, diamond_pos.y, diamond_pos.z, block.DIAMOND_BLOCK.id)
def checkHit():
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
            mc.postToChat("Hit!")
while True:
    time.sleep(1)
    checkHit()'''