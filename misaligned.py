def create_color_map():
    primary_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    secondary_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    color_map = [
        (index, primary, secondary)
        for index, primary in enumerate(primary_colors, start=1)
        for secondary in secondary_colors
    ]
    
    return color_map

def display_color_map(color_map):
    for index, primary_color, secondary_color in color_map:
        print(f'{index} | {primary_color} | {secondary_color}')

# Generate and verify the color map
color_map = create_color_map()
expected_color_map = [
    (1, 'White', 'Blue'), (2, 'White', 'Orange'), (3, 'White', 'Green'), (4, 'White', 'Brown'), (5, 'White', 'Slate'),
    (6, 'Red', 'Blue'), (7, 'Red', 'Orange'), (8, 'Red', 'Green'), (9, 'Red', 'Brown'), (10, 'Red', 'Slate'),
    (11, 'Black', 'Blue'), (12, 'Black', 'Orange'), (13, 'Black', 'Green'), (14, 'Black', 'Brown'), (15, 'Black', 'Slate'),
    (16, 'Yellow', 'Blue'), (17, 'Yellow', 'Orange'), (18, 'Yellow', 'Green'), (19, 'Yellow', 'Brown'), (20, 'Yellow', 'Slate'),
    (21, 'Violet', 'Blue'), (22, 'Violet', 'Orange'), (23, 'Violet', 'Green'), (24, 'Violet', 'Brown'), (25, 'Violet', 'Slate')
]

assert color_map == expected_color_map, "Color map does not match expected values"
display_color_map(color_map)
assert len(color_map) == 25, "Color map length is incorrect"
print("All checks passed successfully!\n")
