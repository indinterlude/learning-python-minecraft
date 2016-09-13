from mcpi.minecraft import Minecraft
mc = Minecraft.create()

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

def construct_a_hut_v1():
    wall_block_type = 43
    wall_block_color = 5
    floor_block_type = 125
    floor_block_color = 2
    roof_block_type = 125
    roof_block_color = 1
    window_block_type = 20
    window_block_color = None
    door_block_type = 64
    door_block_color = None
    air_block = [ 0 ]
    bed_block = [ 26 ]
    # Wall rows
    wall_block = [ wall_block_type, wall_block_color ]
    window_block = [ window_block_type ]
    door_block = [ door_block_type ]
    solid_wall = [ wall_block, wall_block, wall_block, wall_block , wall_block ]
    solid_wall_with_windows = [ wall_block, wall_block, window_block, wall_block, wall_block ]
    solid_wall_with_door_1 = [ wall_block, wall_block, door_block, wall_block, wall_block ]
    solid_wall_with_door_2 = [ wall_block, wall_block, air_block, wall_block, wall_block ]
    middle_wall = [ wall_block, air_block, air_block, air_block, wall_block ]
    middle_wall_with_bed = [ wall_block, air_block, bed_block, air_block, wall_block ]
    middle_wall_with_windows = [ window_block, air_block, air_block, air_block, window_block ]
    # Floor row
    floor_block = [ floor_block_type, floor_block_color ]
    floor_row_end = solid_wall
    floor_row_middle = [ wall_block, floor_block, floor_block, floor_block, wall_block ]
    # Roof block
    roof_block = [ roof_block_type, roof_block_color ]
    roof_row = [ roof_block, roof_block, roof_block, roof_block, roof_block ]
    # Slices ( slice0 is the floor, slice 1-3 walls, slice4 is the roof)
    # need to add windows and door rows and slices
    slice0 = [ floor_row_end, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_end ]
    slice1 = [ solid_wall_with_door_1, middle_wall, middle_wall, middle_wall, middle_wall, middle_wall, solid_wall ]
    slice2 = [ solid_wall_with_door_2, middle_wall, middle_wall_with_windows, middle_wall, middle_wall_with_windows, middle_wall, solid_wall ]
    slice3 = [ solid_wall, middle_wall, middle_wall, middle_wall, middle_wall, middle_wall, solid_wall ]
    slice4 = [ roof_row, roof_row, roof_row, roof_row, roof_row, roof_row, roof_row ]
    cabin_matrix = [ slice0, slice1, slice2, slice3, slice4 ]
    return cabin_matrix

def construct_a_hut_v2():
    wall_block_type = 43
    wall_block_color = 5
    floor_block_type = 125
    floor_block_color = 2
    roof_block_type = 125
    roof_block_color = 1
    window_block_type = 20
    window_block_color = None
    door_block_type = 64
    door_block_color = None
    air_block = [ 0 ]
    bed_block = [ 26 ]
    # Wall rows
    wall_block = [ wall_block_type, wall_block_color ]
    window_block = [ window_block_type ]
    door_block = [ door_block_type ]
    solid_wall = [ wall_block, wall_block, wall_block, wall_block , wall_block ]
    solid_wall_with_windows = [ wall_block, wall_block, window_block, wall_block, wall_block ]
    solid_wall_with_door_1 = [ wall_block, wall_block, air_block, wall_block, wall_block ]
    solid_wall_with_door_2 = [ wall_block, wall_block, air_block, wall_block, wall_block ]
    middle_wall = [ wall_block, air_block, air_block, air_block, wall_block ]
    middle_wall_with_bed = [ wall_block, air_block, bed_block, air_block, wall_block ]
    middle_wall_with_windows = [ window_block, air_block, air_block, air_block, window_block ]
    # Floor row
    floor_block = [ floor_block_type, floor_block_color ]
    floor_row_end = solid_wall
    floor_row_middle = [ wall_block, floor_block, floor_block, floor_block, wall_block ]
    # Roof block
    roof_block = [ roof_block_type, roof_block_color ]
    roof_row = [ roof_block, roof_block, roof_block, roof_block, roof_block ]
    # Slices ( slice0 is the floor, slice 1-3 walls, slice4 is the roof)
    slice0 = [ floor_row_end, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_end ]
    slice1 = [ solid_wall_with_door_1, middle_wall, middle_wall, middle_wall, middle_wall, middle_wall, solid_wall ]
    slice2 = [ solid_wall_with_door_2, middle_wall, middle_wall_with_windows, middle_wall, middle_wall_with_windows, middle_wall, solid_wall ]
    slice3 = [ solid_wall, middle_wall, middle_wall, middle_wall, middle_wall, middle_wall, solid_wall ]
    slice4 = [ roof_row, roof_row, roof_row, roof_row, roof_row, roof_row, roof_row ]
    cabin_matrix = [ slice0, slice1, slice2, slice3, slice4 ]
    return cabin_matrix

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
                x_coord = x_ref + x_offset
                y_coord = y_ref + y_offset
                z_coord = z_ref + z_offset
                if len( column ) > 1:
                    block_type = column[0]
                    block_color = column[1]
                    manifest_block_tuple = ( x_coord, y_coord, z_coord, block_type, block_color )
                else:
                    block_type = column[0]
                    manifest_block_tuple = ( x_coord, y_coord, z_coord, block_type )
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
    special_tuples = []
    for block_tuple in build_manifest_tuple_list:
        if len( block_tuple ) == 5:
            x, y, z, block_type, block_color = block_tuple
            mc.setBlock( x, y, z, block_type, block_color )
        else:
            x, y, z, block_type = block_tuple
            if block_type == 64: #door_block_type
                special_tuples.append( block_tuple )
            else:
                mc.setBlock( x, y, z, block_type )
    for special_tuple in special_tuples:
        if len( block_tuple ) == 5:
            x, y, z, block_type, block_color = block_tuple
            mc.setBlock( x, y, z, block_type, block_color )
        else:
            x, y, z, block_type = block_tuple
            mc.setBlock( x, y, z, block_type )

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

def print_a_hut_v1( location ):
    my_hut_matrix = construct_a_hut_v1()
    my_build_manifest = get_matrix_build_manifest( location, my_hut_matrix )
    minecraft_build_manifest( my_build_manifest )

def print_a_hut_v2( location ):
    my_hut_matrix = construct_a_hut_v2()
    my_build_manifest = get_matrix_build_manifest( location, my_hut_matrix )
    minecraft_build_manifest( my_build_manifest )

#Run a full test
# print_a_monolith( wool_block_type, wool_block_colors['green'], near_me )

# The door is still not working with the special tuple queue
print_a_hut_v1( near_me )
# print_a_hut_v2( near_me )

# def mine_print( base_location, matrix_of_objects ):
#     x_ref, y_ref, z_ref = base_location
#
