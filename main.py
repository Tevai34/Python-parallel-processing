def average_blocks(cube):
    # Get the dimensions of the cube
    depth = len(cube)
    rows = len(cube[0])
    cols = len(cube[0][0])
    
    # Validate the dimensions
    if depth % 2 != 0 or rows % 2 != 0 or cols % 2 != 0:
        raise ValueError("Cube dimensions must be divisible by 2 in each dimension.")

    # Each block will be half of the original dimensions in each axis
    half_depth = depth // 2
    half_rows = rows // 2
    half_cols = cols // 2
    
    blocks = []

    # Loop through each of the 8 blocks
    for i in range(2):
        for j in range(2): 
            for k in range(2):  
                # Collect the elements for the current 2x2x2 block
                block = []
                for d in range(i * half_depth, (i + 1) * half_depth):
                    for r in range(j * half_rows, (j + 1) * half_rows):
                        for c in range(k * half_cols, (k + 1) * half_cols):
                            block.append(cube[d][r][c])
                blocks.append(block)

    averages = [sum(block) / len(block) for block in blocks]

    return averages
