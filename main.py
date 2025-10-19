import robo_state
import harvest_state
robo_state.resetar_posicao()
harvest_state.inicializar_tiles()

def plantar(sentido_inicial):
	lista_plantacao = [Entities.Carrot, Entities.Tree, Entities.Pumpkin, Entities.Carrot]
	sentido = sentido_inicial
	if sentido == True:
		for i in range(get_world_size()):
			if sentido == True:
				for j in range(get_world_size()):
					robo_state.mova_para_ponto(i,j)
					harvest_state.colher(i,j)
					quadrante = harvest_state.get_quadrant(i,j)
					entity = lista_plantacao[quadrante]
					harvest_state.plantar(i,j,entity)
				sentido = False
			else:
				for j in range(get_world_size()-1,-1,-1):
					robo_state.mova_para_ponto(i,j)
					harvest_state.colher(i,j)
					quadrante = harvest_state.get_quadrant(i,j)
					entity = lista_plantacao[quadrante]
					harvest_state.plantar(i,j,entity)
				sentido = True
	else:
		for i in range(get_world_size()-1,-1,-1):
			if sentido == False:
				for j in range(get_world_size()):
					robo_state.mova_para_ponto(i,j)
					harvest_state.colher(i,j)
					quadrante = harvest_state.get_quadrant(i,j)
					entity = lista_plantacao[quadrante]
					harvest_state.plantar(i,j,entity)
				sentido = True
			else:
				for j in range(get_world_size()-1,-1,-1):
					robo_state.mova_para_ponto(i,j)
					harvest_state.colher(i,j)
					quadrante = harvest_state.get_quadrant(i,j)
					entity = lista_plantacao[quadrante]
					harvest_state.plantar(i,j,entity)
				sentido = False
while(True):
	plantar(True)
	plantar(False)