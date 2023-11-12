import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Joystick Tester")

# Initialize the joystick
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() < 1:
    print("Please connect a joystick and run again.")
    sys.exit()

# Use the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Get joystick information
    axis_count = joystick.get_numaxes()
    button_count = joystick.get_numbuttons()

    # Display joystick information
    font = pygame.font.Font(None, 36)

    # Display axis information
    for i in range(axis_count):
        axis_value = joystick.get_axis(i)
        text = font.render(f"Axis {i}: {axis_value:.2f}", True, (255, 255, 255))
        screen.blit(text, (10, 10 + (i * 30)))

    # Display button information
    for i in range(button_count):
        button_value = joystick.get_button(i)
        text = font.render(f"Button {i}: {'Pressed' if button_value else 'Released'}", True, (255, 255, 255))
        screen.blit(text, (10, 10 + ((axis_count + i) * 30)))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
pygame.quit()
sys.exit()
