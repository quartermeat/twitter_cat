from PIL import Image
import random

# Open the image
im = Image.open("images/cat_cropped.jpg")

# Get the size of the image
width, height = im.size

# Set the size of the tiles
tile_width = width // 5
tile_height = height // 5

# List to hold all shuffled images for gif creation
shuffled_images = []

for _ in range(50):  # Create 50 shuffled images
    tiles = []

    # Loop through each tile
    for i in range(5):
        for j in range(5):
            # Crop the tile from the image
            left = j * tile_width
            upper = i * tile_height
            right = left + tile_width
            lower = upper + tile_height
            tile = im.crop((left, upper, right, lower))

            # Save the tile to the tiles list
            if not tile.getbbox():
                continue

            tiles.append(tile)

    # Shuffle the tiles
    random.shuffle(tiles)

    # Create a new blank canvas to place the shuffled tiles
    new_image = Image.new("RGB", (width, height))

    # Place the shuffled tiles on the canvas
    for i in range(5):
        for j in range(5):
            # Get the next tile from the shuffled list
            tile = tiles.pop(0)

            # Define where to paste the tile on the canvas
            left = j * tile_width
            upper = i * tile_height

            new_image.paste(tile, (left, upper))

    new_image.save(f"debug_image_{_}.jpg")

    shuffled_images.append(new_image)

# Save the shuffled images as an animated gif
shuffled_images[0].save("shuffled_cat_animation.gif",
                        save_all=True, append_images=shuffled_images[1:], optimize=False, duration=100, loop=0)
