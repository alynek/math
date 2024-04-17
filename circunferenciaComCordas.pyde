def setup():
   size(600, 600)
   
def draw():
    background(255)
    
    #linha
    coordenadaDoX = 300
    #coluna
    coordenadaDoY = 300
    raio = 50
    comprimento = 200
    strokeWeight(2)
    stroke(1)
    circle(coordenadaDoX, coordenadaDoY, comprimento)
    print(coordenadaDoX)
    
    #corda verde
    strokeWeight(3)
    stroke("#0afb3a")
    line(coordenadaDoX, coordenadaDoY - 2* raio, coordenadaDoX, coordenadaDoY + 2*raio)
    
    #corda vermelha
    strokeWeight(3)
    stroke(255, 0, 42)
    line(coordenadaDoX - 2*raio,coordenadaDoY, coordenadaDoX, coordenadaDoY - 2*raio)
    
    #corda amarela
    strokeWeight(3)
    stroke(255, 255,42)
    line(coordenadaDoX - 2*raio, coordenadaDoY, coordenadaDoX + 2*raio, coordenadaDoY)
    
