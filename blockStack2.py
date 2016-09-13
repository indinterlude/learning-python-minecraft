from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#base_location = ( 47.396, 91.0, -95.123 )
base_location = ( 45.474, 91.0, -92.192 )

x, y, z = base_location

blockType = 103

#single instance
#mc.setBlock(x, y, z, blockType)

#loop instances
for y_position_offset in range(5):
    y = base_location[1] + y_position_offset
    mc.setBlock(x, y, z, blockType)
