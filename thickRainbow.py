#from matplotlib import pyplot
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

base_location = ( 50, 91.0, -92 )
#heading Z towards positive

#block type 35?
wool_block_type = 35
wool_block_colors = {
    'red': 14,
    'orange': 1,
    'yellow': 4,
    'green': 5,
    'blue': 9,
    'indigo': 3,
    'violet': 10,
    }

def draw_totem_at_location( base_location ):
    x, y, z = base_location
    # print( base_location )
    for thickness in range(5):
        mc.setBlock( x, y, z + thickness, wool_block_type, wool_block_colors['violet'] )
        mc.setBlock( x, y+1, z + thickness, wool_block_type, wool_block_colors['indigo'] )
        mc.setBlock( x, y+2, z + thickness, wool_block_type, wool_block_colors['blue'] )
        mc.setBlock( x, y+3, z + thickness, wool_block_type, wool_block_colors['green'] )
        mc.setBlock( x, y+4, z + thickness, wool_block_type, wool_block_colors['yellow'] )
        mc.setBlock( x, y+5, z + thickness, wool_block_type, wool_block_colors['orange'] )
        mc.setBlock( x, y+6, z + thickness, wool_block_type, wool_block_colors['red'] )



def draw_wall( base_location, length ):
    for position in range( length ):
        x, y, z = base_location
        draw_totem_at_location( (x, y, z + position ) )

def y_function( x_value, length ):
    radius = length / 2
    y_offset_factor = ( ( radius ) ** 2 - x_value ** 2 ) ** ( 1 / 2 )
    # y_offset = radius - y_offset_factor
    y_offset = y_offset_factor
    # print( "y offset: " + str(y_offset) )
    return int(y_offset)

length = 40


#pyplot.plot(x_values, y_values, "o-")
#pyplot.show()

def print_n_rainbow_coords( length, base_location ):
    x_coord, y_coord, z_coord = base_location
    if length % 2 == 1:
        length = length - 1

    x_end = int(length / 2 )
    x_start = 0 - x_end

    x_values = range(x_start, x_end + 1 )
    y_values = [ y_function( x_value, length ) for x_value in x_values ]
    # print("x values: " + str(list(x_values) ) )
    # print("y values: " + str(y_values) )

    for x_offset in x_values:
        y_offset = y_function( x_offset, length )
        # if x_offset < 0:
        #     x_offset = x_offset * -1
        totem_location = ( x_coord + x_offset, y_coord + y_offset, z_coord )
        # print( "totem_location: " + str(list(totem_location)))
        # mc.postToChat( str(totem_location) )
        draw_totem_at_location( totem_location )

def standingLocation():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    highestBlockY = mc.getHeight(x, z)
    mc.postToChat( str(highestBlockY) )
    standingLocation = ( x, highestBlockY, z )



my_location = mc.player.getTilePos()
# my_location = standingLocation()
print_n_rainbow_coords( 100, my_location )
