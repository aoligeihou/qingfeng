def on_countdown_end():
    game.over(True, effects.confetti)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    game.over(False, effects.melt)
    music.zapped.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

scene.set_background_color(7)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . b 5 5 b . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
            . . b d 5 5 b 1 f f 5 4 4 c . . 
            b b d b 5 5 5 d f b 4 4 4 4 b . 
            b d d c d 5 5 b 5 4 4 4 4 4 4 b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
毒药 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 1 4 1 . . . . . . . 
            . . . . . . 1 7 1 . . . . . . . 
            . . . . . . 1 7 1 . . . . . . . 
            . . . . . . 1 7 1 . . . . . . . 
            . . . . . . 1 7 1 . . . . . . . 
            . . . 1 1 1 1 7 1 1 1 1 . . . . 
            . . . 1 7 7 7 7 7 7 7 1 . . . . 
            . . . 1 7 7 7 7 7 7 7 1 . . . . 
            . . . 1 7 7 7 7 7 7 7 1 . . . . 
            . . . 1 1 1 1 1 1 1 1 1 . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
controller.move_sprite(mySprite)
info.start_countdown(60)
mySprite.set_position(25, 11)
scene.camera_follow_sprite(mySprite)
毒药.follow(mySprite, 80)
mySprite.set_velocity(100, 100)