import pygame as pg
import chesspieces as cp
import time
board=cp.makeBoard();
print(board);
pg.init()
pg.display.set_caption("ChessProject1")
WIDTH=1000
HEIGHT=900
screen = pg.display.set_mode([WIDTH,HEIGHT])
font = pg.font.Font('freesansbold.ttf',50)
timer = pg.time.Clock()
fps = 60
#0- white no select, 1- white with select, 2 black no select, 3 black with select
turn_selection=0
run=True
valid_moves = []
def drawboard(pg, screen):
    for row in range(8):
        for column in range(8):
            color = 'light gray' if (row + column) % 2 == 0 else 'dark gray'
            pg.draw.rect(screen, color, [column * 100, row * 100, 100, 100])
    pg.draw.rect(screen, 'gray',[0,800,1000,100])
    pg.draw.rect(screen, 'gold',[0,800,1000,100],5)
    pg.draw.rect(screen, 'gold',[800,0,200,1000],5)
    status_text=['White select','White move','Black move','Black move']
    screen.blit(font.render(status_text[turn_selection],True,'black'),(20,820))
def loadimage(t):
    # Fix the path string and use double backslashes or a raw string
    image_path = r"C:\Users\Lenovo\Desktop\project1\chesscode\image\\" + t.name + ".png"
    a = pg.image.load(image_path)
    
    if t.name == "Wpawn" or t.name == "Bpawn":
        a = pg.transform.scale(a, (65, 65))
        screen.blit(a, ( (8-t.location[1] ) * 100 + 30,(8-t.location[0] ) * 100 + 22))
    else:
        a = pg.transform.scale(a, (80, 80))
        screen.blit(a, ((8-t.location[1] ) * 100 + 10,(8-t.location[0] ) * 100 + 10))
def load_chess():
    for chess in board:
        loadimage(chess)
valid_moves=[]
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    drawboard(pg,screen)
    load_chess()
    a=0
    for p in board:
        if(p.name=="WKing" or p.name=="BKing"):
            a=1
    if a==0:
        break
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if turn_selection==0:
        board=cp.makeMoveW(board)
        screen.fill('dark gray')
        drawboard(pg,screen)
        load_chess()
        time.sleep(0.5)
        turn_selection=2
        continue 
    pg.display.flip()
    if turn_selection==2:
        board=cp.makeMove(board)
        screen.fill('dark gray')
        drawboard(pg,screen)
        load_chess()
        turn_selection=0
        continue 
pg.quit()