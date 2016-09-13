from mcpi.minecraft import Minecraft
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
old_x_coord = my_location.x
old_y_coord = my_location.y
old_z_coord = my_location.z
near_me = ( 1 + float(old_x_coord), float(old_y_coord), 1 + float(old_z_coord))

# my_test_location = ( 100, 0, 200 )
my_test_location = my_location

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
def construct_a_box( block_type, block_color ):
    block_info = [ block_type, block_color ]
    rowB = [ block_info, block_info, block_info, block_info ]
    sliceB = [ rowB, rowB, rowB ]
    matrixB = [ sliceB, sliceB, sliceB, sliceB, sliceB ]
    # matrixB = [ sliceB, sliceB ]
    return matrixB

def get_matrix_build_manifest( base_location, matrix ):
    x_ref, y_ref, z_ref = base_location
    build_manifest = []
    slice_counter = 0
    for slice in matrix:
        row_counter = 0
        for row in slice:
            column_counter = 0
            for column in row:
                contents = column
                x_offset = column_counter
                y_offset = slice_counter
                z_offset = row_counter
                block_type = column[0]
                block_color = column[1]
                x_coord = x_ref + x_offset
                y_coord = y_ref + y_offset
                z_coord = z_ref + z_offset
                manifest_block_tuple = ( x_coord, y_coord, z_coord, block_type, block_color )
                build_manifest.append( manifest_block_tuple )
                column_counter += 1
            row_counter += 1
        slice_counter += 1
    return build_manifest

def print_a_build_manifest( build_manifest ):
    print("build_manifest: ")
    for item in build_manifest:
        print( "item: " + str(item) )

def minecraft_build_manifest( build_manifest_tuple_list ):
    for block_tuple in build_manifest_tuple_list:
        x, y, z, block_type, block_color = block_tuple
        mc.setBlock( x, y, z, block_type, block_color )

def test_block( location ):
    test_block_type = 35 # 35=wool
    test_block_color = 1 # 35/1 is orange
    x, y, z = location
    mc.postToChat( str(location) )
    mc.setBlock( x, y, z, test_block_type, test_block_color )

# test_block( near_me )

def print_a_monolith( block_type, block_color, location ):
    my_monolith_matrix = construct_a_box( block_type, block_color )
    my_build_manifest = get_matrix_build_manifest( location, my_monolith_matrix )
    minecraft_build_manifest( my_build_manifest )

#Run a full test
print_a_monolith( wool_block_type, wool_block_colors['green'], near_me )

# def mine_print( base_location, matrix_of_objects ):
#     x_ref, y_ref, z_ref = base_location
#
