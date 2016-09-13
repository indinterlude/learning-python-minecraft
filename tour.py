# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Set x, y, and z variables to represent coordinates
x = 139.839# Fill in
y = 79# Fill in
z = 224.772# Fill in

lookout_tower = ( 139.839, 79, 224.772 )

# Change the player's position
mc.player.setTilePos(x, y, z)

# Wait 10 seconds
time.sleep(5)

# Set x, y, and z variables to represent coordinates
x = 10# Fill in
y = 100# Fill in
z = 10# Fill in

cliff = ( 38.256, 90, -101.986 )    

# Change the player's position
mc.player.setTilePos(x, y, z)

# Wait 10 seconds
time.sleep(5)

# Set x, y, and z variables to represent coordinates
x = 20# Fill in
y = 100# Fill in
z = 20# Fill in

# Change the player's position
mc.player.setTilePos(x, y, z)

# Wait 10 seconds
time.sleep(5)

# Set x, y, and z variables to represent coordinates
x = 100# Fill in
y = 100# Fill in
z = 100# Fill in

# Change the player's position
mc.player.setTilePos(x, y, z)
