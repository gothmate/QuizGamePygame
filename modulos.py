import pygame as pg
import pandas as pd
from time import sleep

class Game(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        # Definições dos objetos (variáveis)
        self.id_planilha = '1CRPIwP0vOf9rjTRw-TFnTzCV0vHWhoMuQuqxnCPxBxo'
        self.data_frame = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{self.id_planilha}/export?format=csv')
        self.c = 0
        self.cor_player = (255, 255, 255)
        self.amarelo = (200, 200, 0)
        self.r1 = (f'{self.data_frame["R1"][self.c]}')
        self.r2 = (f'{self.data_frame["R2"][self.c]}')
        self.r3 = (f'{self.data_frame["R3"][self.c]}')
        self.r4 = (f'{self.data_frame["R4"][self.c]}')
        self.correta = (f'{self.data_frame["CORRETA"][self.c]}')
        self.pergunta = (f'{self.c + 1}.{self.data_frame["PERGUNTA"][self.c]}')


    def escolhe(self, pointer, resposta, tela, x_pos, y_pos):
        if pointer.colliderect(resposta):
            self.sombra = pg.image.load('button_shadow.png')
            self.amarelo = pg.image.load('button_yellow.png')
            self.tela.blit(self.sombra, (x_pos - 3, y_pos - 3))
            self.tela.blit(self.amarelo, (x_pos, y_pos))

    def resposta_escolha(self, rect, r_, c, quest, data_frame, pt, vida):

        if event.type == pg.MOUSEBUTTONDOWN:
            c += 1
            if rect.colliderect(r_) == correta:
                pt = int(pt)
                pt += 100
                pt = str(pt)
                quest = pg.image.load('q_green.png')
                sleep(1)
            else:
                vida = int(vida)
                vida -= 1
                vida = str(vida)
                quest = pg.image.load('q_red.png')
                sleep(1)

    def frame1(self):
        global event
        pg.font.init()
        pg.init()
        self.tela = pg.display.set_mode([800, 600])
        pg.display.set_caption("Testanto PyGame")
        self.clock = pg.time.Clock()
        self.fundo = pg.image.load('bground.png')

        self.sair = False
        self.r_a = pg.Rect(30, 300, 360, 60)
        self.r_b = pg.Rect(410, 300, 360, 60)
        self.r_c = pg.Rect(30, 400, 360, 60)
        self.r_d = pg.Rect(410, 400, 360, 60)

        self.pointer = pg.image.load('pointer.png')
        self.rect = pg.Rect(0, 0, 1, 1)
        self.vidas = '3'
        self.pontos = '0'
        self.score = pg.image.load('button_pt.png')

        self.texto_score = pg.font.SysFont('Franklin Gothic', 40, bold=True)
        self.texto_perg = pg.font.SysFont('Franklin Gothic', 40, bold=True)
        self.texto_resp = pg.font.SysFont('Franklin Gothic', 30, bold=True)

        while self.sair != True:
            # fechar tela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair = True
            # FPS
            self.clock.tick(40)
            # Background
            self.tela.blit(self.fundo, (0, 0))

            # Textos
            self.text = self.texto_perg.render(self.pergunta, 1, (200, 200, 0))
            self.texto_vidas = self.texto_score.render('Vidas: ', 1, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, 1, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, 1, (200, 200, 0))

            # posicionamento do texto
            self.tela.blit(self.score, (600, 30))
            self.tela.blit(self.score, (55, 30))
            self.tela.blit(self.pontuacao, (100, 45))
            self.tela.blit(self.text, (30, 150))
            self.tela.blit(self.texto_vidas, (615, 45))
            self.tela.blit(self.vida, (720, 45))

            # botões de resposta
            self.azul = pg.image.load('button_blue.png')
            self.tela.blit(self.azul, (30, 300))
            self.tela.blit(self.azul, (410, 300))
            self.tela.blit(self.azul, (30, 400))
            self.tela.blit(self.azul, (410, 400))

            self.quest = pg.image.load('q_blue.png')
            self.tela.blit(self.quest, (630, 480))

            # Colisões
            if self.rect.colliderect(self.r_a) or self.rect.colliderect(self.r_b) \
                    or self.rect.colliderect(self.r_c) or self.rect.colliderect(self.r_d):
                self.escolhe(self.rect, self.r_a, self.tela, 30, 300)
                self.escolhe(self.rect, self.r_b, self.tela, 410, 300)
                self.escolhe(self.rect, self.r_c, self.tela, 30, 400)
                self.escolhe(self.rect, self.r_d, self.tela, 410, 400)

                if event.type == pg.MOUSEBUTTONDOWN:
                    self.escolhe(self.rect, self.r_a, self.tela, 30, 300)
                    self.escolhe(self.rect, self.r_b, self.tela, 410, 300)
                    self.escolhe(self.rect, self.r_c, self.tela, 30, 400)
                    self.escolhe(self.rect, self.r_d, self.tela, 410, 400)
                    if pg.MOUSEBUTTONDOWN == self.r1:
                        if self.r1 == self.correta:
                            self.pontos = int(self.pontos)
                            self.pontos += 100
                            self.pontos = str(self.pontos)
                            self.c+=1
                    elif pg.MOUSEBUTTONDOWN == self.r2:
                        if self.r2 == self.correta:
                            self.pontos = int(self.pontos)
                            self.pontos += 100
                            self.pontos = str(self.pontos)
                            self.c+=1
                    elif pg.MOUSEBUTTONDOWN == self.r3:
                        if self.r3 == self.correta:
                            self.pontos = int(self.pontos)
                            self.pontos += 100
                            self.pontos = str(self.pontos)
                            self.c+=1
                    elif pg.MOUSEBUTTONDOWN == self.r4:
                        if self.r4 == self.correta:
                            self.pontos = int(self.pontos)
                            self.pontos += 100
                            self.pontos = str(self.pontos)
                            self.c+=1


            # respostas
            self.perg1 = self.texto_resp.render(self.r1, 1, (self.cor_player))
            self.tela.blit(self.perg1, (50, 320))
            self.perg2 = self.texto_resp.render(self.r2, 1, (self.cor_player))
            self.tela.blit(self.perg2, (430, 320))
            self.perg3 = self.texto_resp.render(self.r3, 1, (self.cor_player))
            self.tela.blit(self.perg3, (50, 420))
            self.perg4 = self.texto_resp.render(self.r4, 1, (self.cor_player))
            self.tela.blit(self.perg4, (430, 420))

            # Mouse
            pg.draw.rect(self.tela, self.cor_player, self.rect)
            (self.rect.left, self.rect.top) = pg.mouse.get_pos()
            x, y = pg.mouse.get_pos()
            self.tela.blit(self.pointer, (x, y))
            pg.mouse.set_visible(False)

            pg.display.update()
        pg.quit()
