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
 

