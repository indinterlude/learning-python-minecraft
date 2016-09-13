# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

def standingLocation():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    highestBlockY = mc.getHeight(x, z)
    mc.postToChat( str(highestBlockY) )
    standingLocation = ( x, highestBlockY, z )

# Where am I on the map? (x,y,z) coordinate
# my_location = mc.player.getTilePos()

# What tile am I over? (x,z) coordinate
# x, y, z = mc.player.getTilePos()
# flat_location = (x,z)

# # Elevation at (x,z) coordinate
# elevation = mc.getHeight(x,z)

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


# Try building a cabin encoded in slices
b = 'block'
o = 'air'

#slice 0
# xxxxxxx
# x     x
# x     x
# x     x
# x     x
# x     x
# xxxx xx
cabin_slice_0 = [ [b,b,b,b,b,b,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,b,b,b,o,b,b],
]

#slice 1
# xx x xx
# x     x
#
# x     x
#
# x     x
# xx x xx
cabin_slice_1 = [ [b,b,b,b,b,b,b],
  [b,o,o,o,o,o,b],
  [o,o,o,o,o,o,o],
  [b,o,o,o,o,o,b],
  [o,o,o,o,o,o,o],
  [b,o,o,o,o,o,b],
  [b,b,o,b,o,b,b],
]

#slice 2
# xxxxxxx
# x     x
# x     x
# x     x
# x     x
# x     x
# xxxxxxx
cabin_slice_2 = [ [b,b,b,b,b,b,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,o,o,o,o,o,b],
  [b,b,b,b,b,b,b],
]

#slice 3
# xxxxxxx
# xxxxxxx
# xxxxxxx
# xxxxxxx
# xxxxxxx
# xxxxxxx
# xxxxxxx
cabin_slice_3 = [ [b,b,b,b,b,b,b],
  [b,b,b,b,b,b,b],
  [b,b,b,b,b,b,b],
  [b,b,b,b,b,b,b],
  [b,b,b,b,b,b,b],
  [b,b,b,b,b,b,b],
  [b,b,b,b,b,b,b],
]

#slice 4
#
#  xxxxx
#  xxxxx
#  xxxxx
#  xxxxx
#  xxxxx
#
cabin_slice_4 = [ [o,o,o,o,o,o,o],
  [o,b,b,b,b,b,o],
  [o,b,b,b,b,b,o],
  [o,b,b,b,b,b,o],
  [o,b,b,b,b,b,o],
  [o,b,b,b,b,b,o],
  [o,o,o,o,o,o,o],
]

#slice 5
#
#
#   xxx
#   xxx
#   xxx
#
#
cabin_slice_5 = [ [o,o,o,o,o,o,o],
  [o,o,o,o,o,o,o],
  [o,o,b,b,b,o,o],
  [o,o,b,b,b,o,o],
  [o,o,b,b,b,o,o],
  [o,o,o,o,o,o,o],
  [o,o,o,o,o,o,o],
]

#slice 6
#
#
#
#    x
#
#
#
cabin_slice_6 = [ [o,o,o,o,o,o,o],
  [o,o,o,o,o,o,o],
  [o,o,o,o,o,o,o],
  [o,o,o,b,o,o,o],
  [o,o,o,o,o,o,o],
  [o,o,o,o,o,o,o],
  [o,o,o,o,o,o,o],
]

cabin_in_code = [
    cabin_slice_0,
    cabin_slice_1,
    cabin_slice_2,
    cabin_slice_3,
    cabin_slice_4,
    cabin_slice_5,
    cabin_slice_6
]

def contruct_a_block( type, color ):
    #Creates a single block unit in a matrix
    simple_block_type = type
    simple_block_color = color
    simple_block_tuple = ( simple_block_type, simple_block_color )
    one_block = simple_block_tuple
    simple_column = [ one_block ]
    simple_row = [ simple_column ]
    simple_matrix = [ simple_row ]
    # simple_matrix = [simple_row]
    # simple_matrix = [ [simple_column] ]
    # simple_matrix = [ [ [ one_block ] ] ]
    # simple_matrix = [ [ [ simple_block_tuple ] ] ]
    # simple_matrix = [ [ [ ( simple_block_type, simple_block_color ) ] ] ]

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

    x_ref, y_ref, z_ref = base_location
    build_inventory = []
    # build_inventory[0] = ( x, y, z, type, color )

    slice_counter = 0
    for slice in matrix:
        row_counter = 0
        for row in slice:
            column_counter = 0
            for column in row:
                block_counter = 0
                for block in column:
                    # to 'print' a block, we need location, type, and color
                    block_type = block[0]
                    block_color = block[1]
                    x_coord = x_ref + row_counter
                    y_coord = y_ref + slice_counter
                    z_coord = z_ref + column_counter
                    loc_adjustment = (row_counter, slice_counter, column_counter)
                    loc_new = ( x_coord, y_coord, z_coord )
                    print( 'base_location: {}, adjustment: {}, new_location: {} '.format(base_location, loc_adjustment, loc_new) )
                    block_tuple = ( x_coord, y_coord, z_coord, block_type, block_color )
                    build_inventory.append( block_tuple )
                    print("added: " + str(block_tuple) )
                    column_counter += 1
                row_counter += 1
            slice_counter += 1
    return build_inventory

my_test_location = ( 100, 0, 200 )
print("my_test_location: " + str(my_test_location) )
my_orange_cube_matrix = construct_a_cube( wool_block_type, wool_block_colors['orange'] )
print("my_orange_cube_matrix: " + str(my_orange_cube_matrix) )
my_build_manifest = build_matrix_inventory( my_orange_cube_matrix, my_test_location )

print("my_build_manifest: ")
for item in my_build_manifest:
    print( "item: " + str(item) )




# def mine_print( base_location, matrix_of_objects ):
#     x_ref, y_ref, z_ref = base_location
#
# def mine_simple_one_block_print_matrix( base_location ):
#     simple_matrix = contruct_a_block( wool_block_type, wool_block_colors['orange'] )



    #mc.setBlock( x, y, z + thickness, wool_block_type, wool_block_colors['orange'] )
