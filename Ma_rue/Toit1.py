# Dépendances
from Ma_rue import rue, affiche 

# Définitions

# Fonction toit1()
def toit1(x, niveau):
    '''
    Dessine un triangle plein de couleur noir de 40 pixels de haut
    et avec une base de 160 pixels 
    Paramètres :
        x : abcisse du centre du toit
        niveau : numero du niveau (0 pour les rdc, ...)
    '''
    y = rue.height - 160 * 60
     # ordonnée de la base du toit
    
    ctx.beginPath();
ctx.moveTo(x,-80);
ctx.lineTo(x, 40);
ctx.lineTo(250, 140);
ctx.closePath();
ctx.stroke();

# Tests
affiche(rue)
toit1(rue.width/2, 0)

# Autres tests
for i in range(5) :
    for j in range(1, 6) :
        toit1(0 + 200 * i, j)