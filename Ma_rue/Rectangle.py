# Dépendances
from Ma_rue import rue, affiche 
from ipycanvas import Canvas
# Définitions

# Fonction rectangle()
def rectangle(x,y,w,h,c):
    rue.fill_style = c 
    rue.fill_rect(x-(w/2), y-h, w, h)
    rue.stroke_style = "black"
    rue.stroke_rect(x-(w/2), y-h, w, h)

# Tests
if __name__ == '__main__' :
    affiche(rue)
    rectangle(0, 50,200,100,'YellowGreen')
    rectangle(800, 450,200,100,'plum')
    rectangle(400, 250,200,100,'SkyBlue')
    rectangle(400, 250,100,50,'salmon')
    