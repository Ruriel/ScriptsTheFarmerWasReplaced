import robo_state
import harvest_state
import wood_harvester
robo_state.inicializar()
tiles = [(0,0), (0,1)]
wood_harvester.inicializar_tiles(tiles)
while(True):
	plantar(True)
	plantar(False)