# Dépendances
from Ma_rue import rue, affiche

# Définitions

# Fonction trait()
def trait(x1,y1,x2,y2):
    rue.begin_path()
    rue.move_to(x1, y1)
    rue.line_to(x2, y2)
    rue.close_path()
    rue.stroke()
    
    # Tests
if __name__ == '__main__' :
    affiche(rue)
    trait(50, 25, rue.width/2, rue.height/2)

    # Autres tests
    for x in range (int(rue.width/2), rue.width + 1, 20) :
        trait(x, 0, 3*rue.width/2 - x, rue.height)

