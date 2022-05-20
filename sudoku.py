import pygame
from pygame.locals import *
import numpy

import random

count, mil = 0, 10

matrix = numpy.zeros((9,9))
matrix_posible = 	numpy.zeros((9,9), dtype="object")
matrix_posible_cs = numpy.zeros((9,9), dtype="object")

# def find_couples():
# 	global matrix_posible

# 	for x in range(9):
# 		for y in range(9):
# 			current_N 	= matrix_posible[x,y]

# 			if y != 8:
# 				side_u 		= matrix_posible[x,y+1]
# 				if current_N == side_u:

# 			if y != 0
# 				side_d, 	= matrix_posible[x,y-1]
# 			if x != 8:
# 				side_r, 	= matrix_posible[x+1,y]
# 			if x != 0
# 				side_l 		= matrix_posible[x-1,y]


# 				for axis in range(9):
# 					number_of_axis = int(matrix[x, axis])
# 					if number_of_axis == tring_N or number_of_axis-9 == tring_N:
# 						is_in_line = True
# 						break
# 				if not is_in_line:
# 					for axis in range(9):
# 						number_of_axis = int(matrix[axis, y])

def couples():
	for x in range(3):
		for y in range(3):
			every_in_cube = []
			every_in_cube_c = []
			repeated = []
			repeated_c = []
			index_l = 0
			for xc in range(3):
				for yc in range(3):
					x_matrix = x*3+ xc
					y_matrix = y*3+ yc
					this_block_N = matrix_posible[  x_matrix , y_matrix  ]

					if this_block_N != 0:
						if len(this_block_N) == 2:
							every_in_cube.append(this_block_N)
							every_in_cube_c.append([x_matrix, y_matrix])

			for z in every_in_cube:
				if every_in_cube.count(z) > 1:
					repeated.append(z)
					repeated_c.append(every_in_cube_c[index_l])
				index_l += 1

			if len(repeated) == 2:	#REMOVE IN BLOCK
				for xr in range(3):
					for yr in range(3):
						xr_matrix = x*3+ xr
						yr_matrix = y*3+ yr
						this_block_R = matrix_posible[  xr_matrix , yr_matrix  ]

						if this_block_R != 0 and this_block_R != repeated[0]:
							c_lis = repeated[0]
							for a in c_lis:
								try:
									this_block_R.remove(a)
								except:
									pass
							matrix_posible[  xr_matrix , yr_matrix  ] = this_block_R

			if len(repeated_c) >= 2:
				c_val = repeated[0]
				x1,y1, x2,y2 = repeated_c[0][0], repeated_c[0][1], repeated_c[1][0], repeated_c[1][1]
				hor,ver = False, False
				if x1 == x2+1 or x1 == x2-1:
					hor = True
				if y1 == y2+1 or y1 == y2-1:
					ver = True

				if hor or ver:
					if not (hor and ver):
						if hor:
							for t in range(9):
								c_po = matrix_posible[  t , y1  ]
								if c_po != 0 and c_po != c_val:
									for e in c_val:
										try:
											c_po.remove(e)
										except: pass
									matrix_posible[  t , y1  ] = c_po

						if ver:
							for t in range(9):
								c_po = matrix_posible[  x1 , t  ]
								if c_po != 0 and c_po != c_val:
									for e in c_val:
										try:
											c_po.remove(e)
										except: pass
									matrix_posible[  x1 , t  ] = c_po


	posibles_to_real()


def hor_ver():
	global matrix_posible, matrix


	for x in range(3):
		for y in range(3):
			ammount_each_n = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
			for xc in range(3):
				for yc in range(3):
					
					x_matrix, y_matrix = x*3+ xc, y*3+ yc
					this_block_N = matrix_posible[  x_matrix , y_matrix  ]

					if this_block_N != 0:
						for i in this_block_N:
							c_list = ammount_each_n[i-1]
							ammount_each_n[i-1] = [c_list[0]+1, x_matrix, y_matrix]

			numer_write = 0
			for i in ammount_each_n:
				numer_write+=1
				if i[0] == 1:
					matrix[i[1], i[2]] = numer_write+9
					matrix_posible[i[1], i[2]] = 0	

	posibles_to_real()					




def posibles_to_real():

	global matrix_posible, matrix

	for x in range(9):
		for y in range(9):
			current_posible = matrix_posible[x,y]

			if current_posible != 0:
				if len(current_posible) == 1:
					matrix[x,y] = current_posible[0]+9
					matrix_posible[x,y] = 0

	#hor_ver()


def solve(): #x_posibles, y_posibles, matrix, matrix_posible

	global matrix_posible, matrix, matrix_posible_cs

	c_block = [0,0]
	for x in range(9):
		for y in range(9):
			every_possible = []

			current_N = int(matrix[x,y])								#GET NUMBER

			if x == 0 or x == 1 or x == 2: c_block[0] = 1				#GET BLOCK
			if x == 3 or x == 4 or x == 5: c_block[0] = 2
			if x == 6 or x == 7 or x == 8: c_block[0] = 3
			if y == 0 or y == 1 or y == 2: c_block[1] = 1
			if y == 3 or y == 4 or y == 5: c_block[1] = 2
			if y == 6 or y == 7 or y == 8: c_block[1] = 3

			if current_N == 0:											#SI EL QUAD ESTÁ VACÍO
				for index in range(9):									#LOOP OF 9 for try evbery number
					tring_N = index+1
					is_in_block = False

					for xc in range(3):										#PROVE IF Number IS NOT IN CUBE
						for yc in range(3):

							x_matrix = ((c_block[0]-1)*3)+ xc
							y_matrix = ((c_block[1]-1)*3)+ yc

							this_block_N = int(matrix[  x_matrix , y_matrix  ])

							if this_block_N == tring_N or this_block_N-9 == tring_N: is_in_block = True


					if not is_in_block:
						is_in_line = False
						for axis in range(9):
							number_of_axis = int(matrix[x, axis])
							if number_of_axis == tring_N or number_of_axis-9 == tring_N:
								is_in_line = True
								break
						if not is_in_line:
							for axis in range(9):
								number_of_axis = int(matrix[axis, y])
								if number_of_axis == tring_N or number_of_axis-9 == tring_N:
									is_in_line = True
									break
						if not is_in_line:
							every_possible.append(tring_N)
							matrix_posible[x,y] = every_possible

	posibles_to_real()


def draw_tablero(screen, width, matrix, selected_quad, matrix_posible):

	stroke_color_line = 10, 10, 10
	stroke_color_fill = 250, 250, 250
	quad_size = (width-1)/9

	poly = [(0, width/3),(width,width/3-2)]; 		pygame.draw.polygon(screen, stroke_color_line, poly, 5)
	poly = [(0, width/3*2),(width,width/3*2-2)];	pygame.draw.polygon(screen, stroke_color_line, poly, 5)
	poly = [(width/3-2, 0),(width/3,width)];		pygame.draw.polygon(screen, stroke_color_line, poly, 5)
	poly = [(width/3*2-2, 0),(width/3*2,width)];	pygame.draw.polygon(screen, stroke_color_line, poly, 5)

	for x in range(9):
		for y in range(9):
			if int(selected_quad[0]) == int(x) and int(selected_quad[1]) == int(y):
				poly = [(x * quad_size,         (y+1) * quad_size),
	                    ((x+1) * quad_size,     (y+1) * quad_size),
	                    ((x+1) * quad_size,     (y) * quad_size),
	                    (x * quad_size,         (y) * quad_size)]
				pygame.draw.polygon(screen, stroke_color_fill, poly, 0)

			poly = [(x * quad_size,         (y+1) * quad_size),
                    ((x+1) * quad_size,     (y+1) * quad_size),
                    ((x+1) * quad_size,     (y) * quad_size),
                    (x * quad_size,         (y) * quad_size)]
			pygame.draw.polygon(screen, stroke_color_line, poly, 1)
			

			font_size = 30
			current_N = int(matrix[x,y])

			pygame.font.init()
			

			if current_N != 0:

				color_text = 	(1,1,1) 	if current_N <= 9 else (200,0,0)
				font_size = 	30 				if current_N <= 9 else 25
				current_N = 	current_N 		if current_N <= 9 else current_N-9

				font = pygame.font.SysFont('Arial', font_size)
				
				text = font.render(str(current_N), False, color_text)
				text_coor = text.get_rect(center=( int((x * quad_size)+(quad_size/2)), int((y * quad_size)+(quad_size/2))  ) )
				screen.blit(text, text_coor)
			else:
				current_P = matrix_posible[x,y]
				font_size = 	10
				if current_P != 0:
					current_P = str(current_P)
					font = pygame.font.SysFont('Arial', font_size)
					text = font.render(current_P, False, (50,50,50))
					text_coor = text.get_rect(center=( int((x * quad_size)+(quad_size/2)), int((y * quad_size)+(quad_size/2))  ) )
					screen.blit(text, text_coor)

	pygame.display.flip()






def findNextCellToFill(grid, i, j):
    for x in range(i,9):
            for y in range(j,9):
                    if grid[x][y] == 0:
                            return x,y
    # for x in range(0,9):
    #         for y in range(0,9):
    #                 if grid[x][y] == 0:
    #                         return x,y
    return -1,-1

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
            columnOk = all([e != grid[x][j] for x in range(9)])
            if columnOk:
                    # finding the top left x,y co-ordinates of the section containing the i,j cell
                    secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                    for x in range(secTopX, secTopX+3):
                            for y in range(secTopY, secTopY+3):
                                    if grid[x][y] == e:
                                            return False
                    return True
    return False

def solveSudoku(grid, screen, width, matrix, selected_quad, matrix_posible, i=0, j=0):
	global count, mil
	i,j = findNextCellToFill(grid, i, j)
	count += 1
	if count >= mil:
		mil += 10
		print(count)
		screen.fill((250, 250, 250))
		for x in range(9):	matrix[x,0] = grid[0][x]
		for x in range(9):	matrix[x,1] = grid[1][x]
		for x in range(9):	matrix[x,2] = grid[2][x]
		for x in range(9):	matrix[x,3] = grid[3][x]
		for x in range(9):	matrix[x,4] = grid[4][x]
		for x in range(9):	matrix[x,5] = grid[5][x]
		for x in range(9):	matrix[x,6] = grid[6][x]
		for x in range(9):	matrix[x,7] = grid[7][x]
		for x in range(9):	matrix[x,8] = grid[8][x]
		draw_tablero(screen, width, matrix, selected_quad, matrix_posible)
	if i == -1:
		return True
	for e in range(1,10):
		if isValid(grid,i,j,e):
			grid[i][j] = e
			if solveSudoku(grid, screen, width, matrix, selected_quad, matrix_posible, i, j):
				return True
			# Undo the current cell for backtracking
			grid[i][j] = 0
	return False


def main():

	global matrix_posible, matrix

	#PYGAME INIT
	pygame.init()
	height, width = 600, 600
	screen = pygame.display.set_mode((height, width))

	clock=pygame.time.Clock()

	bg = 250, 250, 250
	selected_quad = [-1,-1]

	arr = [
		[6,0,2	,0,9,0	,0,7,0],
		[0,0,0	,0,4,0	,9,0,5],
		[0,0,0	,0,0,7	,3,1,0],
		[4,3,0	,8,0,0	,5,0,0],
		[0,0,0	,0,0,0	,0,3,0],
		[0,0,9	,0,0,2	,0,0,0],
		[0,0,8	,5,0,9	,1,0,0],
		[0,0,0	,0,0,0	,2,0,0],
		[7,0,0	,0,0,6	,0,0,0]
	]

	for x in range(9):	matrix[x,0] = arr[0][x]
	for x in range(9):	matrix[x,1] = arr[1][x]
	for x in range(9):	matrix[x,2] = arr[2][x]
	for x in range(9):	matrix[x,3] = arr[3][x]
	for x in range(9):	matrix[x,4] = arr[4][x]
	for x in range(9):	matrix[x,5] = arr[5][x]
	for x in range(9):	matrix[x,6] = arr[6][x]
	for x in range(9):	matrix[x,7] = arr[7][x]
	for x in range(9):	matrix[x,8] = arr[8][x]

	# matrix[2,0] = 7
	# matrix[4,0] = 4
	# matrix[6,0] = 5

	# matrix[3,1] = 9
	# matrix[5,1] = 8

	# matrix[1,3] = 1
	# matrix[6,3] = 6

	# matrix[0,4] = 2
	# matrix[1,4] = 6
	# matrix[2,4] = 9
	# matrix[5,4] = 7
	# matrix[6,4] = 3

	# matrix[4,5] = 5
	# matrix[8,5] = 8

	# matrix[1,6] = 4
	# matrix[4,6] = 2
	# matrix[5,6] = 3
	# matrix[7,6] = 9

	# matrix[8,7] = 1

	# matrix[2,8] = 5
	# matrix[6,8] = 7
	# matrix[7,8] = 4
	# matrix[8,8] = 6


	x_posibles, y_posibles = 0, 0

	solve_b = False

	#CONTROLS INPUTS
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONUP:
				mouse_pos = pygame.mouse.get_pos()
				x,y = str(mouse_pos[0] / (width/9)), str(mouse_pos[1] / (width/9))
				x,y = x[0:1], y[0:1]
				selected_quad[0], selected_quad[1] = x,y

			if event.type == KEYDOWN:
				if event.key == pygame.K_w: key_W_pressed = True

			if event.type == KEYUP:
				if event.key == pygame.K_w: key_W_pressed = False

				current_N = int(matrix[int(selected_quad[0]),int(selected_quad[1])])

				if current_N > 9 or current_N == 0:
					if event.key == pygame.K_1:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 1+9
					if event.key == pygame.K_2:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 2+9
					if event.key == pygame.K_3:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 3+9
					if event.key == pygame.K_4:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 4+9
					if event.key == pygame.K_5:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 5+9
					if event.key == pygame.K_6:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 6+9
					if event.key == pygame.K_7:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 7+9
					if event.key == pygame.K_8:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 8+9
					if event.key == pygame.K_9:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 9+9
					if event.key == pygame.K_0:	matrix[int(selected_quad[0]),int(selected_quad[1])] = 0

				if event.key == pygame.K_p:	solve()	#solve_once = True; x_posibles, y_posibles = 0, 0

				if event.key == pygame.K_o:	posibles_to_real()

				if event.key == pygame.K_i:	couples()

				if event.key == pygame.K_l:	hor_ver()

				if event.key == pygame.K_t:	solve_b = not solve_b



		screen.fill(bg)
			
		draw_tablero(screen, width, matrix, selected_quad, matrix_posible)



		if solve_b:
			solve_b = False	

			solveSudoku(arr, screen, width, matrix, selected_quad, matrix_posible)

			print(arr)

			for x in range(9):	matrix[x,0] = arr[0][x]
			for x in range(9):	matrix[x,1] = arr[1][x]
			for x in range(9):	matrix[x,2] = arr[2][x]
			for x in range(9):	matrix[x,3] = arr[3][x]
			for x in range(9):	matrix[x,4] = arr[4][x]
			for x in range(9):	matrix[x,5] = arr[5][x]
			for x in range(9):	matrix[x,6] = arr[6][x]
			for x in range(9):	matrix[x,7] = arr[7][x]
			for x in range(9):	matrix[x,8] = arr[8][x]

			print("YA")
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# hor_ver()			

			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# solve()
			# couples()		



			
		pygame.display.flip()
		clock.tick(30)

if __name__ == "__main__":
	main()