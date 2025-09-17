import libraries
import pygame
from pygame import mixer

#initialize library
pygame.init()

#Set Screen
size = (730, 500)
screen = pygame.display.set_mode(size)

#Note images
downNote = pygame.image.load('downNote.png')
upNote = pygame.image.load('upNote.png')
downSharp = pygame.image.load('downSharp.png')
upSharp = pygame.image.load('upSharp.png')
lowC = pygame.image.load('lowC.png')
lowCSharp = pygame.image.load('lowC#.png')
highA = pygame.image.load('highA.png')
highASharp = pygame.image.load('highA#.png')
highB = pygame.image.load('highB.png')
highC = pygame.image.load('highC.png')
rest = pygame.image.load('Rest.png')
C4 = pygame.image.load('CF.png')
F4 = pygame.image.load('CF.png')
C5 = pygame.image.load('CF.png')
F5 = pygame.image.load('CF.png')
D4 = pygame.image.load('DG.png')
G4 = pygame.image.load('DG.png')
D5 = pygame.image.load('DG.png')
G5 = pygame.image.load('DG.png')
A4 = pygame.image.load('A.png')
A5 = pygame.image.load('A.png')
E4 = pygame.image.load('EB.png')
B4 = pygame.image.load('B.png')
E5 = pygame.image.load('EB.png')
B5 = pygame.image.load('B.png')
CS4 = pygame.image.load('Black.png')
DS4 = pygame.image.load('Black.png')
FS4 = pygame.image.load('Black.png')
GS4 = pygame.image.load('Black.png')
AS4 = pygame.image.load('Black.png')
CS5 = pygame.image.load('Black.png')
DS5 = pygame.image.load('Black.png')
FS5 = pygame.image.load('Black.png')
GS5 = pygame.image.load('Black.png')
AS5 = pygame.image.load('Black.png') 
C6 = pygame.image.load('C6.png')

#Note Audio
RestSound = mixer.Sound('Rest.mp3')
C4Sound = mixer.Sound("C4.mp3")
CS4Sound = mixer.Sound("C#4.mp3")
D4Sound = mixer.Sound("D4.mp3")
DS4Sound = mixer.Sound("D#4.mp3")
E4Sound = mixer.Sound("E4.mp3")
F4Sound = mixer.Sound("F4.mp3")
FS4Sound = mixer.Sound("F#4.mp3")
G4Sound = mixer.Sound("G4.mp3")
GS4Sound = mixer.Sound("G#4.mp3")
A4Sound = mixer.Sound("A4.mp3")
AS4Sound = mixer.Sound("A#4.mp3")
B4Sound = mixer.Sound("B4.mp3")
C5Sound = mixer.Sound("C5.mp3")
CS5Sound = mixer.Sound("C#5.mp3")
D5Sound = mixer.Sound("D5.mp3")
DS5Sound = mixer.Sound("D#5.mp3")
E5Sound = mixer.Sound("E5.mp3")
F5Sound = mixer.Sound("F5.mp3")
FS5Sound = mixer.Sound("F#5.mp3")
G5Sound = mixer.Sound("G5.mp3")
GS5Sound = mixer.Sound("G#5.mp3")
A5Sound = mixer.Sound("A5.mp3")
AS5Sound = mixer.Sound("A#5.mp3")
B5Sound = mixer.Sound("B5.mp3")
C6Sound = mixer.Sound("C6.mp3")

#key names, positions, and arrangements
keys = [C4,CS4,D4,DS4,E4,F4,FS4,G4,GS4,A4,AS4,B4,C5,CS5,D5,DS5,E5,F5,FS5,G5,GS5,A5,AS5,B5,C6]
xkeys = [0,30,50,86,100,150,180,200,236,250,292,300,350,380,400,436,450,500,530,550,586,600,642,650,700]

workspace = []
nextNoteX = [80]
nextNoteY = []
noteImg = []

tempo = 60

#Plays recording
def audioRun():
    speed = int(1000 / (tempo / 60))
    for note in workspace:
        for event in pygame.event.get():
            cx,cy = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(cx > 75 and cx < 105  and cy > 365 and cy < 390):
                    return
                
        if pygame.mixer.get_busy() == False:
            if note == "Rest":
                RestSound.play()
                pygame.mixer.Sound.fadeout(RestSound,speed)
            if note == "C4note":
                C4Sound.play()
                pygame.mixer.Sound.fadeout(C4Sound,speed)
            if note == "CS4note":
                CS4Sound.play()
                pygame.mixer.Sound.fadeout(CS4Sound,speed)
            if note == "D4note":
                D4Sound.play()
                pygame.mixer.Sound.fadeout(D4Sound,speed)
            if note == "DS4note":
                DS4Sound.play()
                pygame.mixer.Sound.fadeout(DS4Sound,speed)
            if note == "E4note":
                E4Sound.play()
                pygame.mixer.Sound.fadeout(E4Sound,speed)
            if note == "F4note":
                F4Sound.play()
                pygame.mixer.Sound.fadeout(F4Sound,speed)
            if note == "FS4note":
                FS4Sound.play()
                pygame.mixer.Sound.fadeout(FS4Sound,speed)
            if note == "G4note":
                G4Sound.play()
                pygame.mixer.Sound.fadeout(G4Sound,speed)
            if note == "GS4note":
                GS4Sound.play()
                pygame.mixer.Sound.fadeout(GS4Sound,speed)
            if note == "A4note":
                A4Sound.play()
                pygame.mixer.Sound.fadeout(A4Sound,speed)
            if note == "AS4note":
                AS4Sound.play()
                pygame.mixer.Sound.fadeout(AS4Sound,speed)
            if note == "B4note":
                B4Sound.play()
                pygame.mixer.Sound.fadeout(B4Sound,speed)
            if note == "C5note":
                C5Sound.play()
                pygame.mixer.Sound.fadeout(C5Sound,speed)
            if note == "CS5note":
                CS5Sound.play()
                pygame.mixer.Sound.fadeout(CS5Sound,speed)
            if note == "D5note":
                D5Sound.play()
                pygame.mixer.Sound.fadeout(D5Sound,speed)
            if note == "DS5note":
                DS5Sound.play()
                pygame.mixer.Sound.fadeout(DS5Sound,speed)
            if note == "E5note":
                E5Sound.play()
                pygame.mixer.Sound.fadeout(E5Sound,speed)
            if note == "F5note":
                F5Sound.play()
                pygame.mixer.Sound.fadeout(F5Sound,speed)
            if note == "FS5note":
                FS5Sound.play()
                pygame.mixer.Sound.fadeout(FS5Sound,speed)
            if note == "G5note":
                G5Sound.play()
                pygame.mixer.Sound.fadeout(G5Sound,speed)
            if note == "GS5note":
                GS5Sound.play()
                pygame.mixer.Sound.fadeout(GS5Sound,speed)
            if note == "A5note":
                A5Sound.play()
                pygame.mixer.Sound.fadeout(A5Sound,speed)
            if note == "AS5note":
                AS5Sound.play()
                pygame.mixer.Sound.fadeout(AS5Sound,speed)
            if note == "B5note":
                B5Sound.play()
                pygame.mixer.Sound.fadeout(B5Sound,speed)
            if note == "C6note":
                C6Sound.play()
                pygame.mixer.Sound.fadeout(C6Sound,speed)

            while pygame.mixer.get_busy():
                    pass

#Clears workspace
def clear():
    global wipe
    workspace.clear()
    nextNoteY.clear()
    noteImg.clear()
    wipe = True
    pygame.time.delay(100)
    wipe = False

#Images of Keys
def keyboard():
    for i in range(25):
        screen.blit(keys[i],(xkeys[i],400))

#Displays notes on workspace
font = pygame.font.SysFont('arial',18,bold = True)
wipe = False
def display():
    tempoString = str(tempo)
    screen.blit(font.render(tempoString + " BPM",True,(0,0,0)),(90,54))
    for i in range(len(workspace)):
        if wipe:
            return
        if i < 24:
                screen.blit(noteImg[i],(nextNoteX[i],nextNoteY[i]))
        elif i < 48:
                screen.blit(noteImg[i],(nextNoteX[i] - 576,nextNoteY[i] + 82))
        else:
                screen.blit(noteImg[i],(nextNoteX[i] - 1152,nextNoteY[i] + 163))

#Adds/removes notes on workspace
def compose(key):
    global tempo
    if key == pygame.K_UP:
        tempo += 4
        print(tempo)
    if key == pygame.K_DOWN:
        tempo -= 4
    if key == pygame.K_BACKSPACE:
            if len(workspace) > 0:
                del workspace[-1]
                del nextNoteX[-1]
                del nextNoteY[-1]
                del noteImg[-1]
    if len(workspace) < 72:
        if key == pygame.K_SPACE:
            if len(workspace) > 0:
                workspace.append('Rest')
                nextNoteY.append(100)
                noteImg.append(rest)    
        if key == pygame.K_z:
            workspace.append('C4note')
            nextNoteY.append(119)
            noteImg.append(lowC)
        if key == pygame.K_s:
            workspace.append('CS4note')
            nextNoteY.append(119)
            noteImg.append(lowCSharp)
        if key == pygame.K_x:
            workspace.append('D4note')
            nextNoteY.append(115)
            noteImg.append(upNote)
        if key == pygame.K_d:
            workspace.append('DS4note')
            nextNoteY.append(115)
            noteImg.append(upSharp)
        if key == pygame.K_c:
            workspace.append('E4note')
            nextNoteY.append(110)
            noteImg.append(upNote)
        if key == pygame.K_q:
            workspace.append('F4note')
            nextNoteY.append(106)
            noteImg.append(upNote)
        if key == pygame.K_2:
            workspace.append('FS4note')
            nextNoteY.append(106)
            noteImg.append(upSharp)
        if key == pygame.K_w:
            workspace.append('G4note')
            nextNoteY.append(101)
            noteImg.append(upNote)
        if key == pygame.K_3:
            workspace.append('GS4note')
            nextNoteY.append(101)
            noteImg.append(upSharp)
        if key == pygame.K_e:
            workspace.append('A4note')
            nextNoteY.append(97)
            noteImg.append(upNote)
        if key == pygame.K_4:
            workspace.append('AS4note')
            nextNoteY.append(97)
            noteImg.append(upSharp)
        if key == pygame.K_r:
            workspace.append('B4note')
            nextNoteY.append(93)
            noteImg.append(upNote)
        if key == pygame.K_b:
            workspace.append('C5note')
            nextNoteY.append(109)
            noteImg.append(downNote)
        if key == pygame.K_h:
            workspace.append('CS5note')
            nextNoteY.append(104)
            noteImg.append(downSharp)
        if key == pygame.K_n:
            workspace.append('D5note')
            nextNoteY.append(105)
            noteImg.append(downNote)
        if key == pygame.K_j:
            workspace.append('DS5note')
            nextNoteY.append(100)
            noteImg.append(downSharp)
        if key == pygame.K_m:
            workspace.append('E5note')
            nextNoteY.append(101)
            noteImg.append(downNote)
        if key == pygame.K_y:
            workspace.append('F5note')
            nextNoteY.append(97)
            noteImg.append(downNote)
        if key == pygame.K_7:
            workspace.append('FS5note')
            nextNoteY.append(92)
            noteImg.append(downSharp)
        if key == pygame.K_u:
            workspace.append('G5note')
            nextNoteY.append(93)
            noteImg.append(downNote)
        if key == pygame.K_8:
            workspace.append('GS5note')
            nextNoteY.append(88)
            noteImg.append(downSharp)
        if key == pygame.K_i:
            workspace.append('A5note')
            nextNoteY.append(89)
            noteImg.append(highA)
        if key == pygame.K_9:
            workspace.append('AS5note')
            nextNoteY.append(84)
            noteImg.append(highASharp)
        if key == pygame.K_o:
            workspace.append('B5note')
            nextNoteY.append(85)
            noteImg.append(highB)
        if key == pygame.K_p:
            workspace.append('C6note')
            nextNoteY.append(81)
            noteImg.append(highC)
        nextNoteX.append(nextNoteX[-1] + 24)
    
#Plays Audio
def downCommands(key):
    if key == pygame.K_z:
        C4Sound.play()
        xkeys[0]-=1000
    if key == pygame.K_s:
        CS4Sound.play()
        xkeys[1]-=1000
    if key == pygame.K_x:
        D4Sound.play()
        xkeys[2]-=1000
    if key == pygame.K_d:
        DS4Sound.play()
        xkeys[3]-=1000
    if key == pygame.K_c:
        E4Sound.play()
        xkeys[4]-=1000
    if key == pygame.K_q:
        F4Sound.play()
        xkeys[5]-=1000
    if key == pygame.K_2:
        FS4Sound.play()
        xkeys[6]-=1000
    if key == pygame.K_w:
        G4Sound.play()
        xkeys[7]-=1000
    if key == pygame.K_3:
        GS4Sound.play()
        xkeys[8]-=1000
    if key == pygame.K_e:
        A4Sound.play()
        xkeys[9]-=1000
    if key == pygame.K_4:
        AS4Sound.play()
        xkeys[10]-=1000
    if key == pygame.K_r:
        B4Sound.play()
        xkeys[11]-=1000
    if key == pygame.K_b:
        C5Sound.play()
        xkeys[12]-=1000
    if key == pygame.K_h:
        CS5Sound.play()
        xkeys[13]-=1000
    if key == pygame.K_n:
        D5Sound.play()
        xkeys[14]-=1000
    if key == pygame.K_j:
        DS5Sound.play()
        xkeys[15]-=1000
    if key == pygame.K_m:
        E5Sound.play()
        xkeys[16]-=1000
    if key == pygame.K_y:
        F5Sound.play()
        xkeys[17]-=1000
    if key == pygame.K_7:
        FS5Sound.play()
        xkeys[18]-=1000
    if key == pygame.K_u:
        G5Sound.play()
        xkeys[19]-=1000
    if key == pygame.K_8:
        GS5Sound.play()
        xkeys[20]-=1000
    if key == pygame.K_i:
        A5Sound.play()
        xkeys[21]-=1000
    if key == pygame.K_9:
        AS5Sound.play()
        xkeys[22]-=1000
    if key == pygame.K_o:
        B5Sound.play()
        xkeys[23]-=1000
    if key == pygame.K_p:
        C6Sound.play()
        xkeys[24]-=1000

#Stops audio when key is lifted
def upCommands(key):
    if key == pygame.K_z:
        pygame.mixer.Sound.fadeout(C4Sound,300)
        xkeys[0]+=1000
    if key == pygame.K_s:
        pygame.mixer.Sound.fadeout(CS4Sound,300)
        xkeys[1]+=1000
    if key == pygame.K_x:
        pygame.mixer.Sound.fadeout(D4Sound,300)
        xkeys[2]+=1000
    if key == pygame.K_d:
        pygame.mixer.Sound.fadeout(DS4Sound,300)
        xkeys[3]+=1000
    if key == pygame.K_c:
        pygame.mixer.Sound.fadeout(E4Sound,300)
        xkeys[4]+=1000
    if key == pygame.K_q:
        pygame.mixer.Sound.fadeout(F4Sound,300)
        xkeys[5]+=1000
    if key == pygame.K_2:
        pygame.mixer.Sound.fadeout(FS4Sound,300)
        xkeys[6]+=1000
    if key == pygame.K_w:
        pygame.mixer.Sound.fadeout(G4Sound,300)
        xkeys[7]+=1000
    if key == pygame.K_3:
        pygame.mixer.Sound.fadeout(GS4Sound,300)
        xkeys[8]+=1000
    if key == pygame.K_e:
        pygame.mixer.Sound.fadeout(A4Sound,300)
        xkeys[9]+=1000
    if key == pygame.K_4:
        pygame.mixer.Sound.fadeout(AS4Sound,300)
        xkeys[10]+=1000
    if key == pygame.K_r:
        pygame.mixer.Sound.fadeout(B4Sound,300)
        xkeys[11]+=1000
    if key == pygame.K_b:
        pygame.mixer.Sound.fadeout(C5Sound,300)
        xkeys[12]+=1000
    if key == pygame.K_h:
        pygame.mixer.Sound.fadeout(CS5Sound,300)
        xkeys[13]+=1000
    if key == pygame.K_n:
        pygame.mixer.Sound.fadeout(D5Sound,300)
        xkeys[14]+=1000
    if key == pygame.K_j:
        pygame.mixer.Sound.fadeout(DS5Sound,300)
        xkeys[15]+=1000
    if key == pygame.K_m:
        pygame.mixer.Sound.fadeout(E5Sound,300)
        xkeys[16]+=1000
    if key == pygame.K_y:
        pygame.mixer.Sound.fadeout(F5Sound,300)
        xkeys[17]+=1000
    if key == pygame.K_7:
        pygame.mixer.Sound.fadeout(FS5Sound,300)
        xkeys[18]+=1000
    if key == pygame.K_u:
        pygame.mixer.Sound.fadeout(G5Sound,300)
        xkeys[19]+=1000
    if key == pygame.K_8:
        pygame.mixer.Sound.fadeout(GS5Sound,300)
        xkeys[20]+=1000
    if key == pygame.K_i:
        pygame.mixer.Sound.fadeout(A5Sound,300)
        xkeys[21]+=1000
    if key == pygame.K_9:
        pygame.mixer.Sound.fadeout(AS5Sound,300)
        xkeys[22]+=1000
    if key == pygame.K_o:
        pygame.mixer.Sound.fadeout(B5Sound,300)
        xkeys[23]+=1000
    if key == pygame.K_p:
        pygame.mixer.Sound.fadeout(C5Sound,300)
        xkeys[24]+=1000
