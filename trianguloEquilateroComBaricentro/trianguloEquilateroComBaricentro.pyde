def setup():
    size(400, 400)

def draw():
    background(255)
    lado = 100 
    altura = sqrt(3) * lado / 2 
    strokeWeight(3)

    x1 = width / 2
    y1 = height / 2 - altura / 2
    x2 = width / 2 - lado / 2
    y2 = height / 2 + altura / 2
    x3 = width / 2 + lado / 2
    y3 = height / 2 + altura / 2
    
    baricentroX = (x1+x2+x3) / 3
    baricentroY = (y1+y2+y3) / 3

    #triangle(x1, y1, x2, y2, x3, y3)
    stroke("#ff0000")
    line(x1, y1, x2, y2)
    
    stroke("#008000")
    line(x2, y2, x3, y3)
    
    stroke("#ffff00")
    line(x1, y1, x3, y3)
    
    #baricentro do triângulo
    stroke(1)
    circle(baricentroX, baricentroY, 2)
