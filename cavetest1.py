from mcpi.minecraft import Minecraft
mc = Minecraft.create()



block_library = {}
block_library[ 'bed' ] = ( 26, None )
block_library[ 'air' ] = ( 0, None )
block_library[ 'redstone_dust' ] = ( 331, None )
block_library[ 'redstone_lamp' ] = ( 123, None )
block_library[ 'stone_pressure_plate' ] = ( 70, None )
block_library[ 'polished_andesite' ] = ( 1, 6 )
block_library[ 'red_wool' ] = ( 35, 14 )
block_library[ 'yellow_wool' ] = ( 35, 4 )
block_library[ 'green_wool' ] = ( 35, 5 )
block_library[ 'white_wool' ] = ( 35, None )

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
# near_me = ( 1 + float(old_x_coord), float(old_y_coord), 1 + float(old_z_coord))
near_me = ( float(old_x_coord + 1), float(old_y_coord), float(old_z_coord + 1) )

# my_test_location = ( 100, 0, 200 )
my_test_location = my_location

# What tile am I over? (x,z) coordinate
x, y, z = mc.player.getTilePos()
flat_location = (x,z)

# # Elevation at (x,z) coordinate
elevation = mc.getHeight(x,z)

def construct_a_cave_v1():
    testing_run = True
    # --- Define blocks ---
    air_block = block_library[ 'air' ]
    floor_block = block_library[ 'polished_andesite' ]
    wall_block = block_library[ 'polished_andesite' ]
    if testing_run:
        lamp_block = block_library[ 'yellow_wool' ]
        wire_block = block_library[ 'red_wool' ]
        bed_block = block_library[ 'white_wool' ]
        pressure_plate_block = block_library[ 'green_wool' ]
    else:
        lamp_block = block_library[ 'redstone_lamp' ]
        wire_block = block_library[ 'redstone_dust' ]
        bed_block = block_library[ 'bed' ]
        pressure_plate_block = block_library[ 'stone_pressure_plate' ]
    roof_block = block_library[ 'polished_andesite' ]
    # --- Wall rows ---
    solid_wall = [ wall_block, wall_block, wall_block, wall_block , wall_block ]
    solid_wall_with_lamp = [ wall_block, wall_block, lamp_block, wall_block , wall_block ]
    middle_wall = [ wall_block, air_block, air_block, air_block, wall_block ]
    middle_wall_with_bed_head_s1 = [ wall_block, wall_block, air_block, air_block, wall_block ]
    middle_wall_with_bed_head_s2 = [ wall_block, wall_block, air_block, air_block, wall_block ]
    middle_wall_with_bed_foot = [ wall_block, wire_block, air_block, air_block, wall_block ]
    middle_wall_with_pressure_plate = [ wall_block, wire_block, pressure_plate_block, air_block, wall_block ]
    # --- Floor rows ---
    floor_row_end = solid_wall
    floor_row_middle = [ wall_block, floor_block, floor_block, floor_block, wall_block ]
    # --- Roof block ---
    roof_row = [ roof_block, roof_block, roof_block, roof_block, roof_block ]
    roof_row_with_opening = [ roof_block, roof_block, air_block, roof_block, roof_block ]
    # --- Slices ---
    # ( slice0 is the floor, slice 1-3 walls, slice4 is the roof)
    slice0 = [ floor_row_end, floor_row_middle, floor_row_middle, floor_row_middle, floor_row_end ]
    slice1 = [ solid_wall, middle_wall_with_pressure_plate, middle_wall_with_bed_foot, middle_wall_with_bed_head_s1, solid_wall ]
    slice2 = [ solid_wall, middle_wall, middle_wall, middle_wall_with_bed_head_s2, solid_wall ]
    slice3 = [ solid_wall, middle_wall, middle_wall, middle_wall, solid_wall ]
    slice4 = [ roof_row, roof_row, roof_row, roof_row_with_opening, roof_row ]
    cave_matrix = [ slice0, slice1, slice2, slice3, slice4 ]
    # print( 'cave_matrix:/n{}'.format(cave_matrix) )
    return cave_matrix

def get_location_cave_v1( location ):
    x, y, z = location
    offset = 6
    return ( x, y - offset, z )

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

def set_block_v1( block_tuple ):
    # print('block_tuple: {}'.format( block_tuple ))
    # Check for valid tuple
    # Rule #1: tuples have 5 elements
    if len(block_tuple) == 5:
        # Do Stuff
        x, y, z, block_type, block_color = block_tuple
        x_coord = float( x )
        y_coord = float( y )
        z_coord = float( z )
        flt_block_type = float( block_type )
        if block_tuple[ -1 ] == None:
            # print('block_tuple, len = 4: {}'.format( block_tuple[0:-1] ))
            # print('block_type: {}'.format( block_tuple[-2] ))
            mc.setBlock( x_coord, y_coord, z_coord, flt_block_type )
        else:
            # print('block_tuple, len = 5: {}'.format( block_tuple ))
            flt_block_color = float( block_color )
            mc.setBlock( x_coord, y_coord, z_coord, flt_block_type, flt_block_color )
    else:
        # Raise error
        print( 'Invalid block_tuple, len != 5: {}'.format( block_tuple ) )

def minecraft_build_manifest( build_manifest_tuple_list ):
    special_tuples = []
    for block_tuple in build_manifest_tuple_list:
        x, y, z, block_type, block_color = block_tuple
        if block_type == 64: #door_block_type
            special_tuples.append( block_tuple )
        else:
            # mc.setBlock( x, y, z, block_type, block_color )
            set_block_v1( block_tuple )
    for special_tuple in special_tuples:
        # x, y, z, block_type, block_color = block_tuple
        # mc.setBlock( x, y, z, block_type, block_color )
        set_block_v1( block_tuple )

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

def print_a_cave_v1_t1( location ):
    my_cave_matrix = construct_a_cave_v1()
    my_build_manifest = get_matrix_build_manifest( location, my_cave_matrix )
    minecraft_build_manifest( my_build_manifest )

def print_a_cave_v1_t2( location ):
    my_cave_matrix = construct_a_cave_v1()
    my_cave_location = get_location_cave_v1( location )
    my_build_manifest = get_matrix_build_manifest( my_cave_location, my_cave_matrix )
    minecraft_build_manifest( my_build_manifest )

#Run a full test
# print_a_monolith( wool_block_type, wool_block_colors['green'], near_me )

# The door is still not working with the special tuple queue
# print_a_hut_v1( near_me )
# print_a_hut_v2( near_me )


# It's backwards and the white wool test blocks for the bed aren't showing up, also not surewhy there are two random blocks stacked and no light
print_a_cave_v1_t1( near_me )

# def mine_print( base_location, matrix_of_objects ):
#     x_ref, y_ref, z_ref = base_location
#
