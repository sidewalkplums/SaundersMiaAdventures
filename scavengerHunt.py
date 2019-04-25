#IMPORT STATEMENTS
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
from mcpi.vec3 import Vec3


#CLEAR AREA CODE
RADIUS = 60
#number of diamonds to find
NUM_DIAMONDS = 5   

#variables
mc = minecraft.Minecraft.create()
position = mc.player.getTilePos()
score = 0
diamondPositions = []

#clears area by setting any block within radius to air
def clearArea(radius):
    mc.setBlocks(position.x - radius,
    position.y, 
    position.z - radius,
    position.x + radius,
    position.y + radius,
    position.z + radius,
    block.AIR)

#PLACE DIAMONDS CODE
def placeDiamonds():
    #sets 5 diamond blocks in random positions    
    for i in range(NUM_DIAMONDS):
        pos = mc.player.getTilePos()
        treasure_x = random.randint (pos.x - RADIUS, pos.x + RADIUS)
        treasure_y = random.randint (pos.y, pos.y + RADIUS)
        treasure_z = random.randint (pos.z - RADIUS, pos.z + RADIUS)
        mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)
        blockPos = Vec3(treasure_x, treasure_y, treasure_z)
        diamondPositions.append(blockPos)

#CHECK TREASURE CODE
def checkTreasure():
    global score
    #checks to see if blocks have been hit and their positions
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        for diamond in diamondPositions:
            if pos.x == diamond.x and pos.y == diamond.y and pos.z == diamond.z:
                score = score + 1
                #displays how many diamonds are left to find
                mc.postToChat("Hit! Score: " + str(score)) 
                #replaces diamond with air
                mc.setBlock(diamond.x, diamond.y, diamond.z, block.AIR.id) 

            if score == NUM_DIAMONDS:
                #winning game message is displayed if all blocks are found
                mc.postToChat("No, diamonds left to find. Congrats, you have won the game!") 
            
            




#clears area (radius of 60)
clearArea(RADIUS) 
mc.postToChat("Area cleared!")
placeDiamonds() 

while score < NUM_DIAMONDS: 
    time.sleep(.1)
    checkTreasure()

mc.postToChat("END")