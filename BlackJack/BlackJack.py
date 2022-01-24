# Author: Saurin Patel                                                                                                          #
# Program Name: BlackJack 2.0 (Graphical Version)                                                                               #
# Program Description: Graphical BlackJack that is fun to play and is as efficient as possible.                                 #
# Last Revision Date: 2020 - 1 - 6                                                                                              #
                                                                                                                                #
#------------------------------------------------ PRESET VARIABLES + DISPLAY ---------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
import pygame, copy, time, os, random, math, sys                                                                                #Imports all the necessary "functions" to preform game
sys.setrecursionlimit(10000000)                                                                                                 #Set the recursion limit really high so you can't crash the game as easily
pygame.init()                                                                                                                   #Initialize the whole game/Pygame
pygame.event.get()                                                                                                              #Initialize the part where events are collected(mouse position/clicked etc.)
pygame.mixer.init()                                                                                                             #Initialize the mixer for the music to play
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)                                                                            #Put the game screen at 0,0 on the screen. Taken from online
FPS = 100                                                                                                                       #Make the max FPS 100 for when it's called later
clock = pygame.time.Clock()                                                                                                     #Used to track time, which wasn't used, but was going to be added if the player took too long
DisplayWidth = 1600                                                                                                              #Sets the Display width of the game menu
DisplayHeight = 1200                                                                                                             #Sets the Display height of the game menu
GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                             #Creates the window for the game
pygame.display.set_caption('BlackJack')                                                                                         #Sets the caption of the window BlackJack, which can be read at the bottom
pygame.mixer.music.load('Music.mp3')                                                                                            #This is the song that is imported into the game
pygame.mixer.music.play(-1)                                                                                                     #This is the functions that plays the music (-1 means infinite loop)
                                                                                                                                #
#---------------------------------------------------- QUIT GAME FUNCTION -------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Quit():                                                                                                                     #Just defines the function "Quit"
  pygame.display.quit()                                                                                                         #Quits the Display of the game
  pygame.quit()                                                                                                                 #This quits all processing being done
  quit()                                                                                                                        #This quits the game, which actually waits for user input to finish quit function
                                                                                                                                #
#------------------------------------------------------ LIST OF COLORS ---------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
Red = [240,85,85]                                                                                                               #Color Red
Red2 = [220,60,60]                                                                                                              #Another variation of the color Red
Yellow = [255,215,84]                                                                                                           #Color Yellow
Yellow2 = [255,235,84]                                                                                                          #Another variation of the color Yellow
Purple = [222,213,214]                                                                                                          #Color Purple
Purple2 = [200,177,201]                                                                                                         #Another variation of the color Purple
Black = [64,64,65]                                                                                                              #Color Black
Gray = [123,120,120]                                                                                                            #Color Gray
LightGray = [172,167,167]                                                                                                       #Color LightGray
White = [255,255,255]                                                                                                           #Color White
                                                                                                                                #
#-------------------------------------------- DECK OF CARDS IMAGES + CARD VALUES -----------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
AceHearts = pygame.image.load('AceHearts.jpg')                                                                                  #Imports Card
AceDiamonds = pygame.image.load('AceDiamonds.jpg')                                                                              #Imports Card
AceSpades = pygame.image.load('AceSpades.jpg')                                                                                  #Imports Card
AceClubs = pygame.image.load('AceClubs.jpg')                                                                                    #Imports Card
TwoHearts = pygame.image.load('2Hearts.jpg')                                                                                    #Imports Card
TwoDiamonds = pygame.image.load('2Diamonds.jpg')                                                                                #Imports Card
TwoSpades = pygame.image.load('2Spades.jpg')                                                                                    #Imports Card
TwoClubs = pygame.image.load('2Clubs.jpg')                                                                                      #Imports Card
ThreeHearts = pygame.image.load('3Hearts.jpg')                                                                                  #Imports Card
ThreeDiamonds = pygame.image.load('3Diamonds.jpg')                                                                              #Imports Card
ThreeSpades = pygame.image.load('3Spades.jpg')                                                                                  #Imports Card
ThreeClubs = pygame.image.load('3Clubs.jpg')                                                                                    #Imports Card
FourHearts = pygame.image.load('4Hearts.jpg')                                                                                   #Imports Card
FourDiamonds = pygame.image.load('4Diamonds.jpg')                                                                               #Imports Card
FourSpades = pygame.image.load('4Spades.jpg')                                                                                   #Imports Card
FourClubs = pygame.image.load('4Clubs.jpg')                                                                                     #Imports Card
FiveHearts = pygame.image.load('5Hearts.jpg')                                                                                   #Imports Card
FiveDiamonds = pygame.image.load('5Diamonds.jpg')                                                                               #Imports Card
FiveSpades = pygame.image.load('5Spades.jpg')                                                                                   #Imports Card
FiveClubs = pygame.image.load('5Clubs.jpg')                                                                                     #Imports Card
SixHearts = pygame.image.load('6Hearts.jpg')                                                                                    #Imports Card
SixDiamonds = pygame.image.load('6Diamonds.jpg')                                                                                #Imports Card
SixSpades = pygame.image.load('6Spades.jpg')                                                                                    #Imports Card
SixClubs = pygame.image.load('6Clubs.jpg')                                                                                      #Imports Card
SevenHearts = pygame.image.load('7Hearts.jpg')                                                                                  #Imports Card
SevenDiamonds = pygame.image.load('7Diamonds.jpg')                                                                              #Imports Card
SevenSpades = pygame.image.load('7Spades.jpg')                                                                                  #Imports Card
SevenClubs = pygame.image.load('7Clubs.jpg')                                                                                    #Imports Card
EightHearts = pygame.image.load('8Hearts.jpg')                                                                                  #Imports Card
EightDiamonds = pygame.image.load('8Diamonds.jpg')                                                                              #Imports Card
EightSpades = pygame.image.load('8Spades.jpg')                                                                                  #Imports Card
EightClubs = pygame.image.load('8Clubs.jpg')                                                                                    #Imports Card
NineHearts = pygame.image.load('9Hearts.jpg')                                                                                   #Imports Card
NineDiamonds = pygame.image.load('9Diamonds.jpg')                                                                               #Imports Card
NineSpades = pygame.image.load('9Spades.jpg')                                                                                   #Imports Card
NineClubs = pygame.image.load('9Clubs.jpg')                                                                                     #Imports Card
TenHearts = pygame.image.load('10Hearts.jpg')                                                                                   #Imports Card
TenDiamonds = pygame.image.load('10Diamonds.jpg')                                                                               #Imports Card
TenSpades = pygame.image.load('10Spades.jpg')                                                                                   #Imports Card
TenClubs = pygame.image.load('10Clubs.jpg')                                                                                     #Imports Card
JackHearts = pygame.image.load('JackHearts.jpg')                                                                                #Imports Card
JackDiamonds = pygame.image.load('JackDiamonds.jpg')                                                                            #Imports Card
JackSpades = pygame.image.load('JackSpades.jpg')                                                                                #Imports Card
JackClubs = pygame.image.load('JackClubs.jpg')                                                                                  #Imports Card
QueenHearts = pygame.image.load('QueenHearts.jpg')                                                                              #Imports Card
QueenDiamonds = pygame.image.load('QueenDiamonds.jpg')                                                                          #Imports Card
QueenSpades = pygame.image.load('QueenSpades.jpg')                                                                              #Imports Card
QueenClubs = pygame.image.load('QueenClubs.jpg')                                                                                #Imports Card
KingHearts = pygame.image.load('KingHearts.jpg')                                                                                #Imports Card
KingDiamonds = pygame.image.load('KingDiamonds.jpg')                                                                            #Imports Card
KingSpades = pygame.image.load('KingSpades.jpg')                                                                                #Imports Card
KingClubs = pygame.image.load('KingClubs.jpg')                                                                                  #Imports Card
                                                                                                                                #
#------------------------------------------------- ASSIGNING CARD VALUES -------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
Deck = [[AceHearts, 11], [TwoHearts, 2],[ThreeHearts, 3],[FourHearts, 4],[FiveHearts, 5],[SixHearts, 6],                        #Assigns Card values
        [SevenHearts, 7],[EightHearts, 8],[NineHearts, 9],[TenHearts, 10],[JackHearts, 10],                                     #Assigns Card values
        [QueenHearts, 10],[KingHearts, 10],[AceSpades, 11],[TwoSpades, 2],[ThreeSpades, 3],                                     #Assigns Card values
        [FourSpades, 4],[FiveSpades, 5],[SixSpades, 6],[SevenSpades, 7],[EightSpades, 8],[NineSpades, 9],                       #Assigns Card values
        [TenSpades, 10],[JackSpades, 10],[QueenSpades, 10],[KingSpades, 10],[AceDiamonds, 11],                                  #Assigns Card values
        [TwoDiamonds, 2],[ThreeDiamonds, 3],[FourDiamonds, 4],[FiveDiamonds, 5],[SixDiamonds, 6],                               #Assigns Card values
        [SevenDiamonds, 7],[EightDiamonds, 8],[NineDiamonds, 9],[TenDiamonds, 10],[JackDiamonds, 10],                           #Assigns Card values
        [QueenDiamonds, 10],[KingDiamonds, 10],[AceClubs, 11],[TwoClubs, 2],[ThreeClubs, 3],                                    #Assigns Card values
        [FourClubs, 4],[FiveClubs, 5],[SixClubs, 6],[SevenClubs, 7],[EightClubs, 8],[NineClubs, 9],                             #Assigns Card values
        [TenClubs, 10],[JackClubs, 10],[QueenClubs, 10],[KingClubs, 10]]                                                        #Assigns Card values
                                                                                                                                #
#----------------------------------------------------- FONTS + ICONS -----------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
pygame.font.get_fonts()                                                                                                         #Gets all the fonts on the computer
Azonix10 = pygame.font.Font("Azonix.ttf", 10)                                                                                   #Sets the font varibale and the size for use later
Azonix20 = pygame.font.Font("Azonix.ttf", 20)                                                                                   #Sets the font varibale and the size for use later
Azonix25 = pygame.font.Font("Azonix.ttf", 25)                                                                                   #Sets the font varibale and the size for use later
Azonix30 = pygame.font.Font("Azonix.ttf", 30)                                                                                   #Sets the font varibale and the size for use later
Azonix40 = pygame.font.Font("Azonix.ttf", 40)                                                                                   #Sets the font varibale and the size for use later
Azonix50 = pygame.font.Font("Azonix.ttf", 50)                                                                                   #Sets the font varibale and the size for use later
Azonix60 = pygame.font.Font("Azonix.ttf", 60)                                                                                   #Sets the font varibale and the size for use later
Azonix70 = pygame.font.Font("Azonix.ttf", 70)                                                                                   #Sets the font varibale and the size for use later
Azonix80 = pygame.font.Font("Azonix.ttf", 80)                                                                                   #Sets the font varibale and the size for use later
Azonix90 = pygame.font.Font("Azonix.ttf", 90)                                                                                   #Sets the font varibale and the size for use later
Azonix100 = pygame.font.Font("Azonix.ttf", 100)                                                                                 #Sets the font varibale and the size for use later
Icon = pygame.image.load('BlackJack Icon.png')                                                                                  #Loads the image for the icon
pygame.display.set_icon(Icon)                                                                                                   #Displays the Icon beside the window name
                                                                                                                                #
#--------------------------------------------- REFRESH SCREEN AT 100 FPS MAX ---------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def RefreshScreen():                                                                                                            #Just defines the function "RefreshScreen"
  mouse = pygame.mouse.get_pos()                                                                                                #Gets the mouse position
  pygame.display.update()                                                                                                       #Updates the display
  pygame.display.flip()                                                                                                         #Flips the display (Which also updates it)
  clock.tick(FPS)                                                                                                               #Actually refreshed the screen at the desired FPS
                                                                                                                                #
#----------------------------------------------- DRAWING POLYGON FUNCTION ------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Polygon(GameScreen, Colour, Points):                                                                                        #Just defines the function "Polygon"
  pygame.draw.polygon(GameScreen, Colour, Points)                                                                               #Draws a shape with the given information from the Function
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def RoundButton(GameScreen, x1, y1, radius, height, width, OriginalColour, NewColour, Text, Textx, Texty, TextFont, OriginalTextColour, NewTextColour, Antialias, TrueFalse, Occurence): #Just defines the function "RoundButton"
  mouse = pygame.mouse.get_pos()                                                                                                #Gets the mouse position
  Clicked = pygame.mouse.get_pressed()                                                                                          #Gets the pressed or not of the mouse
  x = mouse[0]                                                                                                                  #x coordinate is the mouse[0] value
  y = mouse[1]                                                                                                                  #y coordinate is the mouse[1] value
  sqxOne = (x - x1)**2                                                                                                          #Calculation to determine if mouse is inside circle 1
  sqyOne = (y - y1)**2                                                                                                          #Calculation to determine if mouse is inside circle 1
  sqxTwo = (x - (x1 + width))**2                                                                                                #Calculation to determine if mouse is inside circle 2
  sqyTwo = (y - (y1 + height))**2                                                                                               #Calculation to determine if mouse is inside circle 2
  sqxThree = (x - (x1 + width))**2                                                                                              #Calculation to determine if mouse is inside circle 3
  sqyThree = (y - y1)**2                                                                                                        #Calculation to determine if mouse is inside circle 3
  sqxFour = (x - x1)**2                                                                                                         #Calculation to determine if mouse is inside circle 4
  sqyFour = (y - (y1 + height))**2                                                                                              #Calculation to determine if mouse is inside circle 4
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
  if x1 < mouse[0] < x1 + width and y1 < mouse[1] < y1 + height or x1 - radius < mouse[0] < x1 and y1 < mouse[1] < y1 + height or x1 < mouse[0] < x1 + width and y1 - radius < mouse[1] < y1 or x1 + width < mouse[0] < x1 + width + radius and y1 < mouse[1] < y1 + height or x1 < mouse[0] < x1 + width and y1 + height < mouse[1] < y1 + height + radius or math.sqrt(sqxOne + sqyOne) < radius or math.sqrt(sqxTwo + sqyTwo) < radius or math.sqrt(sqxThree + sqyThree) < radius or math.sqrt(sqxFour + sqyFour) < radius:
    pygame.draw.rect(GameScreen, NewColour, pygame.Rect((x1, y1), (width, height)))                                             #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, NewColour, pygame.Rect((x1 - radius, y1), (radius, height)))                                   #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, NewColour, pygame.Rect((x1, y1 - radius), (width, radius)))                                    #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, NewColour, pygame.Rect((x1 + width, y1), (radius, height)))                                    #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, NewColour, pygame.Rect((x1, y1 + height), (width, radius)))                                    #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, NewColour, (x1, y1), radius)                                                                 #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, NewColour, (x1 + width, y1 + height), radius)                                                #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, NewColour, (x1 + width, y1), radius)                                                         #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, NewColour, (x1, y1 + height), radius)                                                        #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    GameScreen.blit(TextFont.render(Text, Antialias, NewTextColour), [Textx, Texty])                                            #This renders the text information which is given in the second half of the function
    if TrueFalse == True:                                                                                                       #This is done to tell the code to do a function or not if the rectangle is pressed
      if Clicked[0] == 1 and Occurence != None:                                                                                 #This is done to tell the code to do a function or not if the rectangle is pressed
        time.sleep(0.25)                                                                                                              #sleep function to prevent fast computers from outputting so many cards.

        pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                    #This is done to tell the code to do a function or not if the rectangle is pressed
        Occurence()                                                                                                             #This is done to tell the code to do a function or not if the rectangle is pressed
    else:                                                                                                                       #Basic Else statement
      return None                                                                                                               #This is done to tell the code to do a function or not if the rectangle is pressed
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
  else:                                                                                                                         #Basic Else statement
    pygame.draw.rect(GameScreen, OriginalColour, pygame.Rect((x1, y1), (width, height)))                                        #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, OriginalColour, pygame.Rect((x1 - radius, y1), (radius, height)))                              #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, OriginalColour, pygame.Rect((x1, y1 - radius), (width, radius)))                               #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, OriginalColour, pygame.Rect((x1 + width, y1), (radius, height)))                               #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.rect(GameScreen, OriginalColour, pygame.Rect((x1, y1 + height), (width, radius)))                               #Draws a rectangle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, OriginalColour, (x1, y1), radius)                                                            #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, OriginalColour, (x1 + width, y1 + height), radius)                                           #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, OriginalColour, (x1 + width, y1), radius)                                                    #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    pygame.draw.circle(GameScreen, OriginalColour, (x1, y1 + height), radius)                                                   #Draws a circle with the given information from the function (Collectively makes a round rectangle)
    GameScreen.blit(TextFont.render(Text, Antialias, OriginalTextColour), [Textx, Texty])                                       #This renders the text information which is given in the second half of the function
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def DrawCard(x):                                                                                                                #Just defines the function "DrawCard"
  CardDrawn = random.choice(x)                                                                                                  #Randomly chooses a card from the x value which is usually the deck
  x.remove(CardDrawn)                                                                                                           #Removes that card from the deck/x list
  return CardDrawn                                                                                                              #returns the card that was drawn
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def CalculateScore(x):                                                                                                          #Just defines the function "CalculateScore"
  Total = 0                                                                                                                     #The start must be 0 to reset all calculations
  ListOfValues = []                                                                                                             #This list must also be empty to recalculate everything, rest of function will be in lamens terms
  for Value in x:                                                                                                               #For every value in x (deck):
    ListOfValues.append(Value[1])                                                                                               #Append value[1] (the integer) to the empty list that was created
  Total = sum(ListOfValues)                                                                                                     #Then find the sum of all the cards in the new list
  CheckForAce = True                                                                                                            #This is true so the next part of the function happens once
  while CheckForAce == True:                                                                                                    #While the checking for Ace is true
    if Total > 21 and 11 in ListOfValues:                                                                                       #If the hand total is above 21 and 11 is in the list
      ListOfValues.remove(11)                                                                                                   #Remove the 11 from the list
      ListOfValues.append(1)                                                                                                    #Add in a 1 to change the Ace value from 11 to 1
      Total = sum(ListOfValues)                                                                                                 #Recalculate the sum with the new Ace value
    else:                                                                                                                       #If the previous segment is false, then
      CheckForAce = False                                                                                                       #Check for Ace is false and the function ends
  return Total                                                                                                                  #Then return the final total
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def ShowPlayerCards(x):                                                                                                         #Just defines the function "ShowPlayerCards"
  CardX = 100                                                                                                                   #The first X coordinate of the card is 100
  for Value in x:                                                                                                               #For every card in x (the hand)
    GameScreen.blit(Value[0], (CardX, 175))                                                                                     #Blit the image (value[0]) of the card onto the screen at the x,y values
    CardX += 90                                                                                                                 #Card = Card + 90 so the next card can be printed to the right
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def ShowDealerCards(x):                                                                                                         #Just defines the function "ShowDealerCards"
  CardX = 100                                                                                                                   #The first X coordinate of the card is 100
  for Value in x:                                                                                                               #For every card in x (the hand)
    GameScreen.blit(Value[0], (CardX, 350))                                                                                     #Blit the image (value[0]) of the card onto the screen at the x,y values
    CardX += 90                                                                                                                 #Card = Card + 90 so the next card can be printed to the right
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Menu():                                                                                                                     #Just defines the function "Menu"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 85, 75, Azonix90, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 275, 250, 35, 0, 250, Black, Red, "START", 317.5, 235, Azonix40, White, Black, True, True, Game)    #Creates a Black Start button that changes colour when hovered and goes to the Game when clicked
    RoundButton(GameScreen, 225, 350, 35, 0, 350, Black, Red, "INSTRUCTIONS", 237.5, 335, Azonix40, White, Black, True, True, Instructions) #Creates a Black Instructions button that changes colour when hovered and goes to the Instructions menu when clicked
    RoundButton(GameScreen, 275, 450, 35, 0, 250, Black, Red, "QUIT", 337.5, 435, Azonix40, White, Black, True, True, Quit)     #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Instructions():                                                                                                             #Just defines the function "Instructions"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "INSTRUCTIONS", 110, 75, Azonix70, Purple2, Purple2, True, False, None) #Creates a white overlay with the title Instructions. If clicked nothing happens
    RoundButton(GameScreen, 275, 200, 25, 0, 250, Black, Red, "CARD VALUES", 275, 187.5, Azonix30, White, Black, True, True, CardValues) #Creates a Black Card Values button that changes colour when hovered and goes to the Card values page when clicked
    RoundButton(GameScreen, 260, 275, 25, 0, 275, Black, Red, "WIN CONDITIONS", 262.5, 262.5, Azonix30, White, Black, True, True, WinCondition) #Creates a Black Win conditions button that changes colour when hovered and goes to the Win condition page when clicked
    RoundButton(GameScreen, 232, 350, 25, 0, 325, Black, Red, "LOSE CONDITIONS", 242.5, 337.5, Azonix30, White, Black, True, True, LoseCondition) #Creates a Black Lose conditions button that changes colour when hovered and goes to the Lose condition page when clicked
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "GO BACK", 315, 412.5, Azonix30, White, Black, True, True, Menu)  #Creates a Black Go back button that changes colour when hovered and goes to the Menu when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def CardValues():                                                                                                               #Just defines the function "CardValues"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "CARD VALUES", 150, 75, Azonix60, Purple2, Purple2, True, False, None) #Creates a white overlay with the title Card Values. If clicked nothing happens
    RoundButton(GameScreen, 100, 200, 50, 125, 590, Black, Black, "CARD VALUES IN BLACKJACK:", 105, 175, Azonix30, Yellow, Yellow, True, False, None) #Creates a Black overlay and the subtitle for the Card Values
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "1) 2 THROUGH 10 COUNT AS FACE VALUE", 105, 220, Azonix25, White, White, True, False, None) #Rules for the card values in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "2) FACE CARDS (J, Q, K) COUNT AS 10", 100, 262.5, Azonix25, White, White, True, False, None) #Rules for the card values in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "3) ACE COUNTS AS 1 OR 11 BASED ON", 100, 305, Azonix25, White, White, True, False, None) #Rules for the card values in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "WHAT YOUR HAND VALUE IS", 105, 335, Azonix25, White, White, True, False, None) #Rules for the card values in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "GO BACK", 315, 412.5, Azonix30, White, Black, True, True, Instructions) #Creates a Black Go back button that changes colour when hovered and goes to the Menu when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def WinCondition():                                                                                                             #Just defines the function "WinCondition"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "WIN CONDITIONS", 125, 75, Azonix60, Purple2, Purple2, True, False, None) #Creates a white overlay with the title Win Conditions. If clicked nothing happens
    RoundButton(GameScreen, 100, 200, 50, 125, 590, Black, Black, "TO WIN IN BLACKJACK:", 105, 175, Azonix30, Yellow, Yellow, True, False, None) #Creates a Black overlay and the subtitle for the Win conditions
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "1) YOU DRAW A HAND VALUE THAT IS", 105, 220, Azonix25, White, White, True, False, None) #Rules for the basic win conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "HIGHER THAN THE DEALER'S", 105, 250, Azonix25, White, White, True, False, None) #Rules for the basic win conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "2) DEALER DRAWS A HAND VALUE", 100, 295, Azonix25, White, White, True, False, None) #Rules for the basic win conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "GREATER THAN 21", 105, 325, Azonix25, White, White, True, False, None)#Rules for the basic win conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "GO BACK", 315, 412.5, Azonix30, White, Black, True, True, Instructions) #Creates a Black Go back button that changes colour when hovered and goes to the Instructions when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the Screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def LoseCondition():                                                                                                            #Just defines the function "LoseCondition"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse postition
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "LOSE CONDITIONS", 95, 75, Azonix60, Purple2, Purple2, True, False, None) #Creates a white overlay with the title Lose Conditions. If clicked nothing happens
    RoundButton(GameScreen, 100, 200, 50, 125, 590, Black, Black, "TO LOSE IN BLACKJACK:", 105, 175, Azonix30, Yellow, Yellow, True, False, None) #Creates a Black overlay and the subtitle for the Lose conditions
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "1) YOUR HAND VALUE MUST EXCEED 21", 105, 220, Azonix25, White, White, True, False, None) #Rules for the basic Lose conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "2) THE DEALERS HAND HAS A GREATER", 100, 267.5, Azonix25, White, White, True, False, None) #Rules for the basic Lose conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "VALUE THAN YOURS AT THE END OF THE", 105, 300, Azonix25, White, White, True, False, None) #Rules for the basic Lose conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Black, Black, "ROUND", 105, 333.5, Azonix25, White, White, True, False, None)        #Rules for the basic Lose conditions in BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "GO BACK", 315, 412.5, Azonix30, White, Black, True, True, Instructions) #Creates a Black Go back button that changes colour when hovered and goes to the Instructions when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                #  
def Game():                                                                                                                     #Just defines the function "Game"
  global PlayingDeck                                                                                                            #creates a global variable for the actual game
  PlayingDeck = copy.copy(Deck)                                                                                                 #creates a global variable for the actual game
  global PlayersHand                                                                                                            #creates a global variable for the actual game
  PlayersHand = []                                                                                                              #creates a global variable for the actual game
  global PlayersScore                                                                                                           #creates a global variable for the actual game
  PlayersScore = 0                                                                                                              #creates a global variable for the actual game
  global DealersHand                                                                                                            #creates a global variable for the actual game
  DealersHand = []                                                                                                              #creates a global variable for the actual game
  global DealersScore                                                                                                           #creates a global variable for the actual game
  DealersScore = 0                                                                                                              #creates a global variable for the actual game
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  PlayersHand.append(DrawCard(PlayingDeck))                                                                                     #Draws a card from the deck and places it in the players hand
  PlayersHand.append(DrawCard(PlayingDeck))                                                                                     #Draws a card from the deck and places it in the players hand
  PlayersScore = CalculateScore(PlayersHand)                                                                                    #Calculates the score of the players hand
  DealersHand.append(DrawCard(PlayingDeck))                                                                                     #Draws one card for the dealer. The other card is hidden/not drawn yet.
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse positions
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                        #Blackens out the canvas to draw stuff onto
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(PlayersScore), 617.5, 225, Azonix30, Red, Yellow, True, False, None)#Draws the Players Score onto the screen
    RoundButton(GameScreen, 600, 310, 25, 0, 75, Yellow, Red, "HIT", 617.5, 300, Azonix25, Red, Yellow, True, True, Hit)        #Creates a Yellow Hit button that changes colour when hovered and does the Hit function when clicked
    RoundButton(GameScreen, 600, 375, 25, 0, 75, Yellow, Red, "STAND", 592.5, 365, Azonix25, Red, Yellow, True, True, Stand)    #Creates a Yellow Stand button that changes colour when hovered and does the Stand function when clicked
    ShowPlayerCards(PlayersHand)                                                                                                #Shows all the cards that have been drawn from the start of the function
    ShowDealerCards(DealersHand)                                                                                                #Shows all the dealers cards that have been drawn from the start of the function
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Lose():                                                                                                                     #Just defines the function "Lose"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  PlayersScore = CalculateScore(PlayersHand)                                                                                    #Calculates the score for the player
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                        #Blackens out the canvas to draw stuff onto
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, White, White, "YOU LOSE!", 210, 175, Azonix60, Purple2, Purple2, True, False, None)   #Prints the text You lose. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "YOUR HAND : " + str(CalculateScore(PlayersHand)), 265, 265, Azonix30, Red, Yellow, True, False, None) #Prints your hand value after being calculated
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "DEALER'S HAND : " + str(CalculateScore(DealersHand)), 225, 340, Azonix30, Red, Yellow, True, False, None) #Prints the dealers hand value after being calculated
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "PLAY AGAIN", 295, 412.5, Azonix30, White, Black, True, True, Game) #Creates a Black Play Again button that changes color when hovered and goes back to another round when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Win():                                                                                                                      #Just defines the function "Win"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  PlayersScore = CalculateScore(PlayersHand)                                                                                    #Calculates the score for the player
  DealersScore = CalculateScore(DealersHand)                                                                                    #Calculates the score for the dealer
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse positions
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                        #Blackens out the canvas to draw stuff onto
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, White, White, "YOU WIN!", 235, 175, Azonix60, Purple2, Purple2, True, False, None)    #Prints the text You Win. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "YOUR HAND : " + str(CalculateScore(PlayersHand)), 265, 265, Azonix30, Red, Yellow, True, False, None) #Prints your hand value after being calculated
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "DEALER'S HAND : " + str(CalculateScore(DealersHand)), 225, 340, Azonix30, Red, Yellow, True, False, None) #Prints the dealers hand value after being calculated
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "PLAY AGAIN", 295, 412.5, Azonix30, White, Black, True, True, Game) #Creates a Black Play Again button that changes color when hovered and goes back to another round when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the Screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Tie():                                                                                                                      #Just defines the function "Tie"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  PlayersScore = CalculateScore(PlayersHand)                                                                                    #Calculates the score for the player
  DealersScore = CalculateScore(DealersHand)                                                                                    #Calculates the score for the dealer
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                        #Blackens out the canvas to draw stuff onto
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, White, White, "IT WAS A TIE", 175, 175, Azonix60, Purple2, Purple2, True, False, None) #Prints the text for a tie. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "YOUR HAND : " + str(CalculateScore(PlayersHand)), 265, 265, Azonix30, Red, Yellow, True, False, None) #Prints your hand value after being calculated
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "DEALER'S HAND : " + str(CalculateScore(DealersHand)), 225, 340, Azonix30, Red, Yellow, True, False, None) #Prints the dealers hand value after being calculated
    RoundButton(GameScreen, 285, 425, 25, 0, 225, Black, Red, "PLAY AGAIN", 295, 412.5, Azonix30, White, Black, True, True, Game) #Creates a Black Play Again button that changes color when hovered and goes back to another round when clicked
    RoundButton(GameScreen, 310, 500, 25, 0, 175, Black, Red, "QUIT", 357.5, 487.5, Azonix30, White, Black, True, True, Quit)   #Creates a Black Quit button that changes colour when hovered and Quits the game when clicked
    RefreshScreen()                                                                                                             #Refreshes the screen
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Hit():                                                                                                                      #Just defines the function "Hit"
  time.sleep(0.25)                                                                                                              #sleep function to prevent fast computers from outputting so many cards.
  PlayersHand.append(DrawCard(PlayingDeck))                                                                                     #Draws another card from the deck and gives it to the player
  PlayersScore = CalculateScore(PlayersHand)                                                                                    #Calculates the new hand value of the player
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                        #Blackens out the canvas to draw stuff onto
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(CalculateScore(PlayersHand)), 617.5, 225, Azonix30, Red, Yellow, True, False, None) #Prints your hand value after being calculated
    RoundButton(GameScreen, 600, 310, 25, 0, 75, Yellow, Red, "HIT", 617.5, 300, Azonix25, Red, Yellow, True, True, Hit)        #Creates the Hit button for the user to click. If clicked the function repeats (if possible)
    RoundButton(GameScreen, 600, 375, 25, 0, 75, Yellow, Red, "STAND", 592.5, 365, Azonix25, Red, Yellow, True, True, Stand)    #Creates the Stand button for the user to click. If clicked the Stand functions runs
    ShowPlayerCards(PlayersHand)                                                                                                #Shows all of the cards that have been drawn
    ShowDealerCards(DealersHand)                                                                                                #Shows all of the dealers cards that have been drawn
    RefreshScreen()                                                                                                             #Refreshes the screen
    if PlayersScore > 21:                                                                                                       #If the player Busts
      time.sleep(3)                                                                                                             #Wait 3 seconds
      RefreshScreen()                                                                                                           #Refreshes the screen
      Lose()                                                                                                                    #Lose function runs
    if PlayersScore == 21:                                                                                                      #If the player hits BlackJack
      time.sleep(3)                                                                                                             #Wait 3 seconds
      RefreshScreen()                                                                                                           #Refreshes the Screen
      Stand()                                                                                                                   #Runs the Stand function
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
def Stand():                                                                                                                    #Just defines the function "Stand"
  GameScreen = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.NOFRAME)                                           #Recreates a new display as functions don't work as well with 1 screen
  PlayersScore = CalculateScore(PlayersHand)                                                                                    #Calculates the players hand value
  mouse = pygame.mouse.get_pos()                                                                                                #Gets the mouse position
  Clicked = pygame.mouse.get_pressed()                                                                                          #Gets the pressed or not of the mouse
  pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                          #Blackens out the canvas to draw stuff onto
  Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                           #Draws the polygon for aesthetic design
  Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                              #Draws another polygon for aesthetic design
  RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
  RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(CalculateScore(PlayersHand)), 617.5, 225, Azonix30, Red, Yellow, True, False, None)  #Prints your hand value after being calculated
  RoundButton(GameScreen, 600, 310, 25, 0, 75, Yellow, Yellow, "HIT", 617.5, 300, Azonix25, Red, Red, True, False, None)        #Creates the Hit button for the user to click. If clicked nothing happens
  RoundButton(GameScreen, 600, 375, 25, 0, 75, Yellow, Yellow, "STAND", 592.5, 365, Azonix25, Red, Red, True, False, None)      #Creates the Stand button for the user to click. If clicked nothing happens
  RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, "DEALERS TURN", 250, 400, Azonix30, Red, Yellow, True, False, None)       #Says that its the dealers turn
  ShowPlayerCards(PlayersHand)                                                                                                  #Shows all of the cards dealed to the user
  ShowDealerCards(DealersHand)                                                                                                  #Shows all of the cards dealed to the dealer
  RefreshScreen()                                                                                                               #Refreshes the screen
  time.sleep(2)                                                                                                                 #Waits 2 seconds
  DealersHand.append(DrawCard(PlayingDeck))                                                                                     #Appends another card to the dealers hand
  DealersScore = CalculateScore(DealersHand)                                                                                    #Recalculates the hand value for the dealer
  while True:                                                                                                                   #While the Code is running
    for event in pygame.event.get():                                                                                            #For any event in pygame get
      pass                                                                                                                      #Pass the whole thing (done to speed up processing)
    mouse = pygame.mouse.get_pos()                                                                                              #Gets the mouse position
    Clicked = pygame.mouse.get_pressed()                                                                                        #Gets the pressed or not of the mouse
    pygame.draw.rect(GameScreen, Black, pygame.Rect((0, 0), (800, 600)))                                                        #Blackens out the canvas to draw stuff onto
    Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                         #Draws the polygon for aesthetic design
    Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                            #Draws another polygon for aesthetic design
    RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(CalculateScore(PlayersHand)), 617.5, 225, Azonix30, Red, Yellow, True, False, None) #Prints your hand value after being calculated
    RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(CalculateScore(DealersHand)), 617.5, 425, Azonix30, Red, Yellow, True, False, None) #Prints the dealers hand value after being calculated
    RoundButton(GameScreen, 600, 310, 25, 0, 75, Yellow, Yellow, "HIT", 617.5, 300, Azonix25, Red, Red, True, False, None)      #Creates the Hit button for the user to click. If clicked nothing happens
    RoundButton(GameScreen, 600, 375, 25, 0, 75, Yellow, Yellow, "STAND", 592.5, 365, Azonix25, Red, Red, True, False, None)    #Creates the Stand button for the user to click. If clicked nothing happens
    ShowPlayerCards(PlayersHand)                                                                                                #Shows all of the cards dealed to the user
    ShowDealerCards(DealersHand)                                                                                                #Shows all of the cards dealed to the dealer
    DealersScore = CalculateScore(DealersHand)                                                                                  #Calculates the dealers score from new hand
    RefreshScreen()                                                                                                             #Refreshes the screen
    while DealersScore <= 17:                                                                                                   #While the dealers score is equal to or below 17
      time.sleep(2)                                                                                                             #Wait 2 seconds 
      DealersHand.append(DrawCard(PlayingDeck))                                                                                 #Draw another card from the deck
      DealersScore = CalculateScore(DealersHand)                                                                                #Calculates the new score of the hand
      Polygon(GameScreen, Red, [(800,400), (0,200), (0,600), (800, 600)])                                                       #Draws the polygon for aesthetic design
      Polygon(GameScreen, Black, [(800,400), (0,200), (0,0), (800,0)])                                                          #Draws another polygon for aesthetic design
      RoundButton(GameScreen, 70, 70, 35, 450, 650, White, White, "BLACKJACK", 120, 75, Azonix80, Purple2, Purple2, True, False, None) #Creates a white overlay with the title BlackJack. If clicked nothing happens
      RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(CalculateScore(PlayersHand)), 617.5, 225, Azonix30, Red, Yellow, True, False, None) #Prints your hand value after being calculated
      RoundButton(GameScreen, 0, 0, 0, 0, 0, Yellow, Red, str(CalculateScore(DealersHand)), 617.5, 425, Azonix30, Red, Yellow, True, False, None) #Prints the dealers hand value after being calculated
      RoundButton(GameScreen, 600, 310, 25, 0, 75, Yellow, Yellow, "HIT", 617.5, 300, Azonix25, Red, Red, True, False, None)    #Creates the Hit button for the user to click. If clicked nothing happens
      RoundButton(GameScreen, 600, 375, 25, 0, 75, Yellow, Yellow, "STAND", 592.5, 365, Azonix25, Red, Red, True, False, None)  #Creates the Stand button for the user to click. If clicked nothing happens
      ShowPlayerCards(PlayersHand)                                                                                              #Shows all of the card the player was dealt
      ShowDealerCards(DealersHand)                                                                                              #Shows all of the cards the dealer has been dealt
      RefreshScreen()                                                                                                           #Refreshes the screen
    DealersScore = CalculateScore(DealersHand)                                                                                  #Calculates the dealers score
    if DealersScore > 21:                                                                                                       #If the dealers score exceeds 21
      time.sleep(3)                                                                                                             #Wait 3 seconds
      RefreshScreen()                                                                                                           #Refreshes the screen
      Win()                                                                                                                     #Goes to win screen/function
    DealersScore = CalculateScore(DealersHand)                                                                                  #Calculates the dealers score
    if DealersScore == PlayersScore:                                                                                            #If the dealers score is the same as the players
      time.sleep(3)                                                                                                             #Wait 3 seconds
      RefreshScreen()                                                                                                           #Refreshes the screen
      Tie()                                                                                                                     #Goes to the tie screen/function
    DealersScore = CalculateScore(DealersHand)                                                                                  #Calculates the dealers score
    if DealersScore < PlayersScore:                                                                                             #If the dealers score is less than the players
      time.sleep(3)                                                                                                             #Wait 3 seconds
      RefreshScreen()                                                                                                           #Refreshes the screen
      Win()                                                                                                                     #Goes to win screen/function
    DealersScore = CalculateScore(DealersHand)                                                                                  #Calculates the dealers score
    if DealersScore > PlayersScore:                                                                                             #If dealers score exceeds the players score
      time.sleep(3)                                                                                                             #Wait 3 seconds
      RefreshScreen()                                                                                                           #Refreshes the screen
      Lose()                                                                                                                    #Goes to the lose screen/function
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
                                                                                                                                #
Menu()                                                                                                                          #Runs the Game from the Menu Page
                                                                                                                                #
#-------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------#
