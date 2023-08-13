from PIL import Image

IMAGE_PIXEL_HEIGHT = 1033
IMAGE_PIXEL_WIDTH = 947

print("vertical square size(pixels): {0}".format(IMAGE_PIXEL_HEIGHT/5))
print("horizontal square size(pixels): {0}".format(IMAGE_PIXEL_WIDTH/5))


# Open the image
im = Image.open("images/cat_cropped.jpg")

# Get the size of the image
width, height = im.size

# Set the size of the tiles
tile_width = width // 5
tile_height = height // 5

# Loop through each tile
for i in range(5):
    for j in range(5):
        # Crop the tile from the image
        left = j * tile_width
        upper = i * tile_height
        right = left + tile_width
        lower = upper + tile_height
        tile = im.crop((left, upper, right, lower))

        # Save the tile as a new image
        filename = f"tile_{i}_{j}.jpg"
        tile.save(filename)
