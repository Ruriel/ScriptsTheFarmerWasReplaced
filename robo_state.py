posicao_robo = 0,0
def inicializar():
	global posicao_robo	
	clear()
	posicao_robo = 0,0

def move_wrapped(x,y):
	global posicao_robo
	x0, y0 = posicao_robo
	ws = get_world_size()
	hws = ws // 2
	dx = ((x - x0 + hws) % ws) - hws
	dy = ((y - y0 + hws) % ws) - hws
	for i in range(dx):
		move(East)
		print("Move East")
	for i in range(-dx):
		move(West)
		print("Move West")
	for i in range(dy):
		move(North)
		print("Move North")
	for i in range(-dy):
		move(South)
		print("Move South")
	
	posicao_robo = x, y

def mova_para_ponto(x=0, y=0):
	global posicao_robo
	x0, y0 = posicao_robo
	posicao_robo = x,y
	while x0 > x:
		move(West)
		x0 = x0 - 1
	while x0 < x:
		move(East)
		x0 = x0 + 1
	while y0 > y:
		move(South)
		y0 = y0 - 1
	while y0 < y:
		move(North)
		y0 = y0 + 1
	posicao_robo = x, y
