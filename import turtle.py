#Importando uma biblioteca
import turtle
import time
import random

# Jogo simples: SnakeByte usando turtle (Python 3)
# Para jogar: instale Python 3 (turtle já vem com a maioria das distribuições)

WIDTH, HEIGHT = 600, 600
DELAY = 0.1  # menor = mais rápido
MOVE_STEP = 20

# Setup da tela
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("SnakeByte")
screen.bgcolor("pink")
screen.tracer(0)

# Cabeça da cobra
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida
food = turtle.Turtle()
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0, 100)

segments = []
score = 0

# Texto do placar
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("purple")
pen.goto(0, HEIGHT//2 - 40)
pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

def update_score():
    pen.clear()
    pen.goto(0, HEIGHT//2 - 40)
    pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Movimentos
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x, y = head.position()
    if head.direction == "up":
        head.sety(y + MOVE_STEP)
    if head.direction == "baixo":
        head.sety(y - MOVE_STEP)
    if head.direction == "esquerda":
        head.setx(x - MOVE_STEP)
    if head.direction == "direita":
        head.setx(x + MOVE_STEP)

# Controles
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Função para reiniciar o jogo
def reset_game():
    global segments, score, DELAY
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)
    segments = []
    score = 0
    DELAY = 0.1
    update_score()

# Loop principal
try:
    while True:
        screen.update()

        # Verifica colisão com a borda
        x, y = head.position()
        if x > WIDTH/2 - MOVE_STEP or x < -WIDTH/2 + MOVE_STEP or y > HEIGHT/2 - MOVE_STEP or y < -HEIGHT/2 + MOVE_STEP:
            reset_game()

        # Verificando colisão com a comida
        if head.distance(food) < 20:
            # comida se move para lugar aleatório
            fx = random.randint(-WIDTH//2 + 20, WIDTH//2 - 20)
            fy = random.randint(-HEIGHT//2 + 20, HEIGHT//2 - 20)
            # Alinhando à grade
            fx = (fx // MOVE_STEP) * MOVE_STEP
            fy = (fy // MOVE_STEP) * MOVE_STEP
            food.goto(fx, fy)

            # Adicionando segmento
            new_seg = turtle.Turtle()
            new_seg.shape("square")
            new_seg.color("green")
            new_seg.penup()
            segments.append(new_seg)

            score += 10
            if DELAY > 0.03:
                DELAY -= 0.005
            update_score()

        # Movimentação do corpo da cobra (da ponta para a cabeça)
        for index in range(len(segments)-1, 0, -1):
            x_prev = segments[index-1].xcor()
            y_prev = segments[index-1].ycor()
            segments[index].goto(x_prev, y_prev)
        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Verificação da colisão com o próprio corpo
        for seg in segments:
            if seg.distance(head) < 10:
                reset_game()
                break

        time.sleep(DELAY)
except turtle.Terminator:
    pass