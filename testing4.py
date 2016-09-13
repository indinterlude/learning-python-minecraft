from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
mc = Minecraft.create()

# mc.player.setTilePos(0, 72, 0)

def standingLocation():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    highestBlockY = mc.getHeight(x, z)
    mc.postToChat( str(highestBlockY) )
    standingLocation = ( x, highestBlockY, z )

# Where am I on the map? (x,y,z) coordinate
my_location = mc.player.getTilePos()

# What tile am I over? (x,z) coordinate
x, y, z = mc.player.getTilePos()
flat_location = (x,z)

# # Elevation at (x,z) coordinate
elevation = mc.getHeight(x,z)

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


# x         # a block

# columns on Z axis
# xxx   # a column of blocks

# rows on X axis
#[0,0]
# xox       # a row of columns
# xxx
# xox
#    [2,2]

# slices on Y axis (zero is on ground)

def construct_a_cube( type, color ):
    #Creates a 3x3x3 cube of blocks in a matrix
    size = 3
    cube_block_type = type
    cube_block_color = color
    cube_block_tuple = ( cube_block_type, cube_block_color )
    one_block = cube_block_tuple
    cube_column = [ one_block, one_block, one_block ]
    cube_row = [ cube_column, cube_column, cube_column ]
    cube_slice = [ cube_row ]
    cube_matrix = [ cube_slice, cube_slice, cube_slice ]
    return cube_matrix
    # one line - [[[[(35, 1), (35, 1), (35, 1)], [(35, 1), (35, 1), (35, 1)], [(35, 1), (35, 1), (35, 1)]]], [[[(35, 1), (35, 1), (35, 1)], [(35, 1), (35, 1), (35, 1)], [(35, 1), (35, 1), (35, 1)]]], [[[(35, 1), (35, 1), (35, 1)], [(35, 1), (35, 1), (35, 1)], [(35, 1), (35, 1), (35, 1)]]]]
    # expanded -
# test_matrix =[
#     [
#         [
#             [(35, 1), (35, 1), (35, 1)],
#             [(35, 1), (35, 1), (35, 1)],
#             [(35, 1), (35, 1), (35, 1)]
#         ]
#     ],
#     [
#         [
#             [(35, 1), (35, 1), (35, 1)],
#             [(35, 1), (35, 1), (35, 1)],
#             [(35, 1), (35, 1), (35, 1)]
#         ]
#     ],
#     [
#         [
#             [(35, 1), (35, 1), (35, 1)],
#             [(35, 1), (35, 1), (35, 1)],
#             [(35, 1), (35, 1), (35, 1)]
#         ]
#     ]
# ]

# def count_blocks_in_matrix( matrix ):
#     #do something
#
# def count_blocks_in_column( column ):
#     # cube_column = [ one_block, one_block, one_block ]
#     # num_blocks = len(cube_column)
#     len( column )
#
# def count_columns_in_row( row ):
#     # cube_row = [ cube_column, cube_column, cube_column ]
#     # num_columns = len(cube_row)
#     len( row )
#
# def count_rows_in_slice( slice ):
#     # cube_slice = [ cube_column, cube_column, cube_column ]
#     # num_rows = len( cube_slice )
#     len( slice )
#
# def count_slices_in_matrix( matrix ):
#     # cube_matrix = [ cube_slice, cube_slice, cube_slice ]
#     # num_slices = len( cube_matrix )
#     len( matrix )

def build_matrix_inventory( matrix, base_location ):
    #take a matrix and a base location and build a list
    #of blocks to place to build the object described by the matrix
    # X-axis: columns (left to right)
    # Y-axis: slices (bottom to top)
    # Z-axis: rows (front to back)
    x_ref, y_ref, z_ref = base_location
    build_inventory = []
    # build_inventory[0] = ( x, y, z, type, color )
    slice_counter = 0
    for slice in matrix:
        row_counter = 0
        for row in slice:
            column_counter = 0
            for column in row:
                # print(column)
                block_type = column[0]
                block_color = column[1]
                x_coord = x_ref + column_counter
                y_coord = y_ref + slice_counter
                z_coord = z_ref + row_counter

                loc_adjustment = ( column_counter, slice_counter, row_counter )
                loc_new = ( x_coord, y_coord, z_coord )
                # print( 'base_location: {}, adjustment: {}, new_location: {} '.format(base_location, loc_adjustment, loc_new) )
                block_tuple = ( x_coord, y_coord, z_coord, block_type, block_color )
                build_inventory.append( block_tuple )
                # print("added: " + str(block_tuple) )
                column_counter += 1
            row_counter += 1
        slice_counter += 1
    return build_inventory

# my_test_location = ( 100, 0, 200 )
my_test_location = my_location

print("my_test_location: " + str(my_test_location) )
my_orange_cube_matrix = construct_a_cube( wool_block_type, wool_block_colors['orange'] )
print("my_orange_cube_matrix: " + str(my_orange_cube_matrix) )
my_build_manifest = build_matrix_inventory( my_orange_cube_matrix, my_test_location )

print("my_build_manifest: ")
for item in my_build_manifest:
    print( "item: " + str(item) )

def minecraft_build_manifest( build_manifest_tuple_list ):
    for block_tuple in build_manifest_tuple_list:
        x, y, z, block_type, block_color = block_tuple
        # mc.setBlock( x, y, z, block_type, block_color )
        location = (x,y,z)
        test_block(location)

old_x_coord = my_location.x
old_y_coord = my_location.y
old_z_coord = my_location.z

near_me = ( 1 + float(old_x_coord), float(old_y_coord), 1 + float(old_z_coord))

def test_block( location ):
    test_block_type = 35 # 35=wool
    test_block_color = 1 # 35/1 is orange
    x, y, z = location
    mc.postToChat( str(location) )
    mc.setBlock( x, y, z, test_block_type, test_block_color )

# test_block( near_me )

minecraft_build_manifest( my_build_manifest )

# def mine_print( base_location, matrix_of_objects ):
#     x_ref, y_ref, z_ref = base_location
#
# def mine_simple_one_block_print_matrix( base_location ):
#     simple_matrix = contruct_a_block( wool_block_type, wool_block_colors['orange'] )



    #mc.setBlock( x, y, z + thickness, wool_block_type, wool_block_colors['orange'] )
