
def construct_a_box( block_type, block_color ):
    block_info = [ block_type, block_color ]

    rowB = [ block_info, block_info, block_info, block_info ]
    row14 = ['o0', 'o1', 'o2', 'o3' ]
    row13 = ['n0', 'n1', 'n2', 'n3' ]
    row12 = ['m0', 'm1', 'm2', 'm3' ]

    row11 = ['l0', 'l1', 'l2', 'l3' ]
    row10 = ['k0', 'k1', 'k2', 'k3' ]
    row9 = [ 'j0', 'j1', 'j2', 'j3' ]

    row8 = ['i0', 'i1', 'i2', 'i3']
    row7 = ['h0', 'h1', 'h2', 'h3']
    row6 = ['g0', 'g1', 'g2', 'g3']

    row5 = ['f0', 'f1', 'f2', 'f3']
    row4 = ['e0', 'e1', 'e2', 'e3']
    row3 = ['d0', 'd1', 'd2', 'd3']

    row2 = ['c0', 'c1', 'c2', 'c3']
    row1 = ['b0', 'b1', 'b2', 'b3']
    row0 = ['a0', 'a1', 'a2', 'a3']

    sliceB = [ rowB, rowB, rowB ]
    slice4 = [ row12, row13, row14 ]
    slice3 = [ row9, row10, row11 ]
    slice2 = [ row6, row7, row8 ]
    slice1 = [ row3, row4, row5 ]
    slice0 = [ row0, row1, row2 ]

    # matrixB = [ sliceB, sliceB, sliceB, sliceB, sliceB ]
    matrixB = [ sliceB, sliceB ]
    # matrix = [ slice0, slice1, slice2, slice3, slice4 ]
    matrix = [ slice0, slice1 ]
    return matrix



def get_matrix_element( matrix, column, row, slice ):
    slice_of_matrix = matrix[slice]
    row_of_slice = slice_of_matrix[row]
    column_of_row = row_of_slice[column]
    return column_of_row

def matrix_slice_length( matrix ):
    return len( matrix )

def matrix_row_length( matrix ):
    return len( matrix[0] )

def matrix_column_length( matrix ):
    return len( matrix[0][0] )

def get_slice_of_matrix( matrix, slice ):
    slice_of_matrix = matrix[slice]
    return slice_of_matrix

def get_row_of_slice( matrix, slice, row ):
    slice_of_matrix = matrix[slice]
    row_of_slice = slice_of_matrix[row]
    return row_of_slice

def get_column_of_slice( matrix, slice, column ):
    column_of_slice = []
    slice_of_matrix = matrix[slice]
    for row in slice_of_matrix:
        column_of_slice.append( row[column] )
    return column_of_slice

def get_closest_element_in_matrix( matrix ):
    return get_matrix_element( matrix, 0, 0, 0 )

def get_matrix_size( matrix ):
    num_slices = len( matrix ) + 1
    num_rows = len( matrix[0] ) + 1
    num_columns = len( matrix[0][0] ) + 1
    size = num_slices * num_rows * num_columns
    return size

def get_farthest_element_in_matrix( matrix ):
    farthest_slice = len( matrix ) - 1
    print( 'farthest_slice: {}'.format(farthest_slice) )
    farthest_row = len( matrix[0] ) - 1
    print( 'farthest_row: {}'.format(farthest_row) )
    farthest_column = len( matrix[0][0] ) - 1
    print( 'farthest_column: {}'.format(farthest_column) )
    farthest_element = get_matrix_element( matrix, farthest_column, farthest_row, farthest_slice )
    return farthest_element

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
                # --- New magic ---

                # Don't forget to switch block_type and block_color assignments
                fake_block_type = contents
                block_type = fake_block_type
                # block_type = column[0]
                fake_block_color = contents
                block_color = fake_block_color
                # block_color = column[1]

                x_coord = x_ref + x_offset
                y_coord = y_ref + y_offset
                z_coord = z_ref + z_offset

                manifest_block_tuple = ( x_coord, y_coord, z_coord, block_type, block_color )
                build_manifest.append( manifest_block_tuple )

                # --- end of new magic ---
                # content_message = 'content: {}'.format( contents )
                # offset_message = 'block offset x:{}, y:{}, z:{}'.format( x_offset, y_offset, z_offset )
                # print( content_message, offset_message )
                column_counter += 1
            row_counter += 1
        slice_counter += 1
    return build_manifest


my_matrix = construct_a_box( 'wool', 'orange' )
my_base_location = ( 0, 0, 0 )
my_build_manifest = get_matrix_build_manifest( my_base_location, my_matrix )
for job in my_build_manifest:
    print(job)
