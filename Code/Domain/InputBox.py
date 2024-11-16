import pygame as pg

class InputBox:

    def __init__(self, screen, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color_inactive = (50, 50, 50)
        self.color_active = (0, 0, 0)
        self.color = self.color_inactive
        self.text = text
        self.font = pg.font.Font(None, 30)  # Initialize a font object
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.screen = screen

        self.active = False

    def handle_event(self, event):
        print(event.type, event.value)
        if event.type == pg.MOUSEBUTTONDOWN:
            print("salut2")
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            print("salut3")
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def render(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 2)
