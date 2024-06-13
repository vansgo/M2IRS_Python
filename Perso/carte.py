from folium import Map

# Creation d'une carte du monde interactive dans un fichier HTML
def init_carte():
    
    provider = 'https://tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token=3muP4SP1F7Ms6fBq4n8MvsdsZjTEZ7DkglSktjdW1Dx1epPacPF9i995MDfpOupb'
    attrib = '<a href="https://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    Carte = Map(location=[0,0], zoom_start=2, tiles = provider,attr=attrib)

    Carte.save("carte1.html")
   

def main():
    ...

    init_carte()

#Main guard
if __name__=="__main__":
    main()
