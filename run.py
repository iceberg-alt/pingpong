from main import *

from items.place import *
from items.score import * 
from items.ball import *

score = Score(canvas, 'black')
paddle = Paddle(canvas, 'black')
ball = Ball(canvas, paddle, score, 'red')
while not ball.hit_bottom:
        if paddle.started == True:
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
time.sleep(1)

