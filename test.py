import math
world_size = 6
def get_quadrant(x, y):
	length_quadrant = (world_size)/2
	if x - length_quadrant < 0 and y - length_quadrant < 0:
		return 0
	if x - length_quadrant < 0 and y - length_quadrant >= 0:
		return 1
	if x - length_quadrant >= 0 and y - length_quadrant < 0:
		return 2
	return 3

print("Quadrante 0")
print(get_quadrant(0,0))
print(get_quadrant(0,1))
print(get_quadrant(0,2))
print(get_quadrant(1,0))
print(get_quadrant(1,1))
print(get_quadrant(1,2))
print(get_quadrant(2,0))
print(get_quadrant(2,1))
print(get_quadrant(2,2))
print('\n')
print("Quadrante 1")
print(get_quadrant(0,3))
print(get_quadrant(0,4))
print(get_quadrant(0,5))
print(get_quadrant(1,3))
print(get_quadrant(1,4))
print(get_quadrant(1,5))
print(get_quadrant(2,3))
print(get_quadrant(2,4))
print(get_quadrant(2,5))
print('\n')
print("Quadrante 2")
print(get_quadrant(3,0))
print(get_quadrant(3,1))
print(get_quadrant(3,2))
print(get_quadrant(4,0))
print(get_quadrant(4,1))
print(get_quadrant(4,2))
print(get_quadrant(5,0))
print(get_quadrant(5,1))
print(get_quadrant(5,2))
print('\n')
print("Quadrante 3")
print(get_quadrant(3,3))
print(get_quadrant(3,4))
print(get_quadrant(3,5))
print(get_quadrant(4,3))
print(get_quadrant(4,4))
print(get_quadrant(4,5))
print(get_quadrant(5,3))
print(get_quadrant(5,4))
print(get_quadrant(5,5))