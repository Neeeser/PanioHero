import pygame

# Write me a Game class that creates a panio of n number of keys
# and plays a sound when the key is pressed
# The sound should be a different sound for each key
class Panio():
    def __init__(self, n):
        self.n = n
        self.keys = []
        self.sounds = []
        self.load_sounds()
        self.create_keys()

    def load_sounds(self):
        for i in range(self.n):
            self.sounds.append(pygame.mixer.Sound("sounds/key{}.mp3".format(i)))

    def create_keys(self):
        for i in range(self.n):
            self.keys.append(Key(i, self.sounds[i]))

    def play_sound(self, key):
        self.sounds[key].play()

    def draw(self, screen):
        for key in self.keys:
            key.draw(screen)


class Key():
    def __init__(self, key, sound):
        self.key = key
        self.sound = sound
        self.width = 99
        self.height = 100
        self.x = 100 * key
        self.y = 0
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def play_sound(self):
        self.sound.play()

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

# Write me a main function that creates a panio of 10 keys
# and plays a sound when the key is pressed
# The sound should be a different sound for each key
def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    panio = Panio(10)
    running = True
    while running:
        screen.fill((0, 0, 0))
        panio.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for key in panio.keys:
                    if key.is_clicked(mouse_pos):
                        key.play_sound()
    pygame.quit()

if __name__ == "__main__":
    main()


