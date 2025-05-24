import pygame

kleur_slang = (0, 255, 0)
kleur_slang2 = (255, 0, 0)
veld_grootte = 20

class Snake:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.lijst_slang = [[startx, starty]]
        self.lengte_slang = 1
        self.x_verandering = 0
        self.y_verandering = 0

    def beweeg(self):
        self.x += self.x_verandering
        self.y += self.y_verandering
        slang_kop = [self.x, self.y]
        self.lijst_slang.append(slang_kop)
        # Verwijder de staart als dat nodig is:
        if len(self.lijst_slang) > self.lengte_slang:
            del self.lijst_slang[0]

    def teken(self, venster):
        for segment in self.lijst_slang:
            pygame.draw.rect(venster, kleur_slang, pygame.Rect(segment[0], segment[1], veld_grootte, veld_grootte))
            pygame.draw.rect(venster, kleur_slang2, pygame.Rect(segment[0] + 4, segment[1] + 4, veld_grootte - 8, veld_grootte - 8))

    def is_buiten_veld(self, breedte, hoogte):
        return self.x >= breedte or self.x < 0 or self.y >= hoogte or self.y < 0

    def raakt_zichzelf(self):
        game_over = False
        for segment in self.lijst_slang[:-1]:  # alle segmenten zonder de kop
            if segment == [self.x, self.y]:    # één van de segmenten is gelijk aan de kop
                game_over = True
        return game_over
