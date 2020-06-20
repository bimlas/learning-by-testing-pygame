import pygame


def loop(update, event_handler):
    screen_width = 800
    screen_height = 600
    max_fps = 9999
    should_print_fps = True

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        clock.tick(max_fps)
        if should_print_fps:
            print('FPS: {}'.format(clock.get_fps()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            event_handler(event)

        update(screen)
        # Call pygame.display.flip() from the callback!

    pygame.quit()