from matplotlib import pyplot

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

base_location = ( 55, 91.0, -92 )
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
    print( base_location )
    mc.setBlock( x, y,   z, wool_block_type, wool_block_colors['violet'] )
    mc.setBlock( x, y+1, z, wool_block_type, wool_block_colors['indigo'] )
    mc.setBlock( x, y+2, z, wool_block_type, wool_block_colors['blue'] )
    mc.setBlock( x, y+3, z, wool_block_type, wool_block_colors['green'] )
    mc.setBlock( x, y+4, z, wool_block_type, wool_block_colors['yellow'] )
    mc.setBlock( x, y+5, z, wool_block_type, wool_block_colors['orange'] )
    mc.setBlock( x, y+6, z, wool_block_type, wool_block_colors['red'] )

def draw_wall( base_location, length ):
    for position in range( length ):
        x, y, z = base_location
        draw_totem_at_location( (x, y, z + position ) )

#draw_wall( base_location, 24 )

# simple -> x**2 + y**2 = r**2
# r => length / 2
# y = sqrt( (length / 2) ** 2 - x ** 2)
# plot on x, 0..length
# midpoint is base_location + offset (offset is half of the length)


def draw_20_rainbow( base_location ):
    length = 20
    x_coord, y_coord, z_coord = base_location
    for x_offset in range( length ):
        # x**2 + y**2 = r**2
        # y = ( r**2 - x**2 ) ** (1/2)
        # r = ( length / 2 )
        y_offset = (  ( length / 2 ) ** 2 - x_offset ** 2 ) ** ( 1 / 2 )
        totem_location = ( x_coord + x_offset, y_coord + y_offset, z_coord )
        draw_totem_at_location( totem_location )

# draw_20_rainbow( base_location )

def print_n_rainbow_coords( length, base_location ):
    x_coord, y_coord, z_coord = base_location
    for x_offset in range( length ):
        radius = length / 2
        y_offset = ( ( radius ) ** 2 - x_offset ** 2 ) ** ( 1 / 2 )
        print("x_offset: " + str(x_offset) )
        print("y_offset: " + str(y_offset) )
        totem_location = ( x_coord + x_offset, y_coord + y_offset, z_coord )
        print(totem_location)

#print_n_rainbow_coords( 20, base_location )

def y_function( x_value, length ):
    radius = length / 2
    y_offset_factor = ( ( radius ) ** 2 - x_value ** 2 ) ** ( 1 / 2 )
    # y_offset = radius - y_offset_factor
    y_offset = y_offset_factor
    print( "y offset: " + str(y_offset) )
    return int(y_offset)

length = 50
if length % 2 == 1:
    length = length - 1

x_end = int(length / 2 )
x_start = 0 - x_end

x_values = range(x_start, x_end + 1 )
y_values = [ y_function( x_value, length ) for x_value in x_values ]

print("x values: " + str(list(x_values) ) )
print("y values: " + str(y_values) )

pyplot.plot(x_values, y_values, "o-")
pyplot.show()
