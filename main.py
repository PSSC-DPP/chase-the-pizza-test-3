def on_overlap(sprite, otherSprite):
    ranColorNum: number = randint(0, 10)
    info.set_font_color(ranColorNum)
    info.change_score_by(1)
    Pizza.setPosition(randint(10, 150), randint(10, 110))
    info.start_countdown(2)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap)
Pizza: Sprite = None
scene.set_background_color(13)
mySprite = sprites.create(img("""
    c 7 7 7 7 7 7 7 7 7 7 7 7 7 7 c
    7 8 8 7 7 7 7 7 7 7 7 7 7 8 8 7
    7 7 7 8 8 8 7 7 7 7 8 8 8 7 7 7
    7 7 1 1 1 7 7 7 7 7 7 1 1 1 7 7
    7 7 1 f 1 7 7 7 7 7 7 1 f 1 7 7
    7 7 1 1 1 7 7 7 7 7 7 1 1 1 7 7
    7 7 7 7 7 7 7 7 b 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 2 2 2 2 2 2 2 7 7 7 7
    7 7 7 7 7 2 a d a d a 2 7 7 7 7
    7 c 7 7 7 2 d a a a d 2 7 7 c 7
    7 c 7 7 7 2 a a f a a 2 7 7 c 7
    7 c 7 7 7 2 d a a a d 2 7 7 c 7
    7 c 7 7 7 2 a d a d a 2 7 7 c 7
    7 c 7 7 7 2 2 2 2 2 2 2 7 7 c 7
    7 c 7 7 7 7 7 7 7 7 7 7 7 7 c 7
"""), SpriteKind.player)
mySprite.setPosition(73, 54)
controller.move_sprite(mySprite)
Pizza = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . d d d . . . . . . .
    . . . . . d d 5 d d d . . . . .
    . . . . d d 2 2 7 2 5 d . . . .
    . . . . d 2 7 2 2 2 d . . . . .
    . . . . . d 2 2 7 2 d . . . . .
    . . . . . d 2 5 2 d . . . . . .
    . . . . . . d 2 2 d . . . . . .
    . . . . . . . d d . . . . . . .
    . . . . . . . . d . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), SpriteKind.food)
# Named function
def add(x: number, y: number):
    return x + y
sum2 = add(1, 2)