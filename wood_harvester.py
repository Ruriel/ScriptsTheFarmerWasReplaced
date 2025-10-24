tiles = []
tiles_entity = []
tiles_ground = []
tiles_water = []
tiles_infected = []
tiles_course = []
def inicializar_tiles(points: list):
    global tiles
    global tiles_entity
    global tiles_ground
    global tiles_water
    global tiles_infected

    for i in len(list):
        tiles.append(points[i])
        tiles_course(points[i])
        tiles_entity.append(Entities.Grass)
        tiles_ground.append(Grounds.Grassland)
        tiles_water.append(0)
        tiles_infected.append(False)

def get_tile_index(x,y):
    global tiles
    index = -1
    for i in len(tiles):
        point = tiles[i]
        if point[0] == x and point[1] == y:
            index = i
    return index

def get_entity(x,y):
    index = get_tile_index(x,y)
    return get_entity(index)

def get_entity(i):
    global tiles_entity
    if i < 0 or i > len(tiles_entity):
        return None
    return tiles_entity[i]

def _can_plant_tree(index):
    global tiles
    if index < 0:
        return False
    point = tiles[index]
    point_x = point[0]
    point_y = point[1]
    entity_n = get_entity(point_x, point_y + 1)
    entity_s = get_entity(point_x, point_y - 1)
    entity_l = get_entity(point_x + 1, point_y)
    entity_o = get_entity(point_x - 1, point_y)
    return entity_n != Entities.Tree and \
           entity_s != Entities.Tree and \
           entity_l != Entities.Tree and \
           entity_o != Entities.Tree

def _can_plant_tree(x,y):
    global tiles
    index = get_tile_index(x,y)
    return _can_plant_tree(index)

def _is_grassland(index):
    global tiles_ground
    tile_ground = tiles_ground[index]
    return tile_ground == Grounds.Grassland

def _fertilize(index):
    global tiles_infected
    if tiles_infected[index] == True:
        use_item(Items.Weird_Substance)
        tiles_infected[index] = False
    else:
        use_item(Items.Fertilizer)
        tiles_infected[index] = True

def set_course(points_course):
    global tiles_course
    if points_course == None:
        tiles_course = tiles.copy()
        return
    tiles_course = []
    for i in len(points_course):
        point = points_course[i]
        x = point[0]
        y = point[1]
        index = get_tile_index(x,y)
        if index > 0:
            tiles_course.append(point)
    if len(tiles_course) == 0:
        tiles_course = tiles.copy

def plant_tree(x,y):
    global tiles_entity
    global tiles_ground
    global tiles_water
    global tiles_infected
    index = get_tile_index(x,y)
    if index < 0:
        return False
    if not _is_grassland(index):
        till()
        tiles_ground = Grounds.Grassland
    while get_water() < 0.5:
        use_item(Items.Water)
    tiles_water = get_water()
    if _can_plant_tree(index):
        entity = Entities.Tree
        if tiles_infected[index] == False:
            use_item(Items.Fertilizer)
            tiles_infected[index] == True
    else:
        entity = Entities.Bush
    plant(entity)
    tiles_entity[index] = entity
    
 