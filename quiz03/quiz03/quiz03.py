from bangtal import *

scene1 = Scene("Room 1", "Images/배경-1.png")
scene1.setLight(0.3)
scene2 = Scene("Room 2", "Images/배경-2.png")

door1 = Object("Images/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True
door1.tried = False

key = Object("Images/열쇠.png")
key.locate(scene1, 250, 250)
key.haveNow = False

doorWithKey = Object("Images/문-왼쪽-닫힘.png")
doorWithKey.locate(scene1, 250, 290)
doorWithKey.show()
doorWithKey.tried = False

exitSign = Object("Images/exit.png")
exitSign.setScale(0.7)
exitSign.locate(scene2, 660, 500)
exitSign.show()

door2 = Object("Images/문-오른쪽-열림.png")
door2.locate(scene2, 800, 290)
door2.show()


def door1_onMouseAction(x, y, action):
    if door1.closed and key.inHand() is True:
        scene1.setLight(1)
        door1.setImage("Images/문-오른쪽-열림.png")
        showMessage("I opened the door with the key! Let's enter the open door!")
        door1.closed = False
    elif door1.closed is True:
        showMessage("The door is locked tightly. I think I need a key. Let's find the key elsewhere.")
        door1.tried = True
    else:
        scene2.enter()
        showMessage("I find the exit! Let's escape through the open door!")


def doorWithKey_onMouseAction(x, y, action):
    if doorWithKey.tried is True:
        pass
    elif door1.closed is True and key.haveNow is False and door1.tried is True:
        key.show()
        scene1.setLight(0.7)
        doorWithKey.setImage("Images/문-왼쪽-열림.png")
        showMessage("The door opened, and the key fell through the door gap."
                    " It seems that I can open the right door with the key!")
        doorWithKey.tried = True
    else:
        showMessage("The door is locked tightly and nothing happened.")


def door2_onMouseAction(x, y, action):
    endGame()


def key_onMouseAction(x, y, action):
    key.pick()
    showMessage("I finally get the key! Let's open the right door!")


door1.onMouseAction = door1_onMouseAction
doorWithKey.onMouseAction = doorWithKey_onMouseAction
key.onMouseAction = key_onMouseAction
door2.onMouseAction = door2_onMouseAction

startGame(scene1)
