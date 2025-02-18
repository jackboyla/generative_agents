import pygame
from pytmx import load_pygame

def main():
    pygame.init()
    
    # temporary display mode to allow image conversion
    pygame.display.set_mode((1, 1))
    
    tmx_data = load_pygame("the_ville.tmx")
    
    # calculate the size of the window based on the map dimensions
    map_width = tmx_data.width * tmx_data.tilewidth
    map_height = tmx_data.height * tmx_data.tileheight

    screen = pygame.display.set_mode((map_width, map_height))
    pygame.display.set_caption("Tiled Map Renderer")
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Render each visible layer from the TMX data
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                for x, y, gid in layer:
                    tile_image = tmx_data.get_tile_image_by_gid(gid)
                    if tile_image:
                        screen.blit(tile_image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
        
        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
