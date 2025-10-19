tileEntities = []
tileGrounds = []
tileWater = []
tileInfected = []
def inicializar_tiles():
	global tileEntities
	global tileGrounds
	global tileWater
	global tileInfected
	for i in range(get_world_size()):
		tileEntities.append([])
		tileGrounds.append([])
		tileWater.append([])
		tileInfected.append([])
		for j in range(get_world_size()):
			tileGrounds[i].append(Grounds.Grassland)
			tileEntities[i].append(Items.Hay)
			tileWater[i].append(get_water())
			tileInfected[i].append(False)
def get_quadrant(x, y):
	length_quadrant = (get_world_size())/2
	if x - length_quadrant < 0 and y - length_quadrant < 0:
		return 0
	if x - length_quadrant < 0 and y - length_quadrant >= 0:
		return 1
	if x - length_quadrant >= 0 and y - length_quadrant < 0:
		return 2
	return 3

def can_plant_tree(x,y):
	global tileEntities
	if	y+1 >= get_world_size():
		entityN = None
	else:
		entityN = tileEntities[x][y+1]

	if y-1 < 0:
		entityS = None
	else: 
		entityS = tileEntities[x][y-1]
		
	if x+1 >= get_world_size():
		entityL = None
	else:
		entityL = tileEntities[x+1][y]
		
	if x-1 < 0:
		entityO = None
	else:
		entityO = tileEntities[x-1][y]
	return entityN != Entities.Tree and entityS != Entities.Tree and entityL != Entities.Tree and entityO != Entities.Tree

def plantar(x,y, entity):
	global tileEntities
	global tileGrounds
	global tileWater
	global tileInfected
	entity_to_be_planted = entity
	if entity == Entities.Tree and not can_plant_tree(x,y):
		entity_to_be_planted = Entities.Bush
	if entity == Entities.Bush and can_plant_tree(x,y):
		entity_to_be_planted = Entities.Tree
	if entity_to_be_planted == Entities.Carrot or entity_to_be_planted == Entities.Pumpkin: 
		if tileGrounds[x][y] == Grounds.Grassland:
			till()
			tileGrounds[x][y] = Grounds.Soil
	if entity_to_be_planted == Entities.Grass or entity_to_be_planted == Entities.Bush or entity_to_be_planted == Entities.Tree:
		if tileGrounds[x][y] == Grounds.Soil:
			till()
			tileGrounds[x][y] = Grounds.Grassland
	plant(entity_to_be_planted)
	tileEntities[x][y] = entity_to_be_planted
	water = get_water()
	if water < 1 and entity_to_be_planted != Entities.Grass:
		use_item(Items.Water)
	if tileInfected[x][y] == True:
		use_item(Items.Weird_Substance)
		tileInfected[x][y] = False
	else:
		use_item(Items.Fertilizer)
		tileInfected[x][y] = True
	tileWater[x][y] = water
	esperar(2)
	#TODO Aguardar Abóbora crescer
	if tileEntities[x][y] == Entities.Pumpkin and not can_harvest():
		plant(Entities.Pumpkin)
	else:
		harvest()
		
def esperar(n):
	for i in range(n):
		can_harvest()	

def colher(x,y):
	if tileGrounds[x][y] == Grounds.Grassland and can_harvest():
		harvest()
	while can_harvest():
		harvest()