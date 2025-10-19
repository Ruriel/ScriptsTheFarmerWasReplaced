posicao_robo = 0,0
def resetar_posicao():
	global posicao_robo	
	clear()
	posicao_robo = 0,0

def mova_para_ponto(x=0, y=0):
	global posicao_robo
	x0, y0 = posicao_robo
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

