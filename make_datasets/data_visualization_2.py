import numpy as np 
import matplotlib.pyplot as plt
import pickle
import math
import matplotlib.animation as animation

def compute_nx_ny(k):
	n_x = k%4
	n_y = int((k-n_x)/4)

	return n_x, n_y

def read_outside_temp(filename):
	outside_temp = np.loadtxt(filename)

	return outside_temp

def read_data(filename):
	with open(filename, 'rb') as f:
		return pickle.load(f)

def compute_24_hours_matrix(outside_temp, data, frames_per_min):
	time_range = 24*frames_per_min

	temperatures = np.ones((time_range, 5, 6))

	current_time = 0.0
	for i in range(time_range):
		current_time = 24*(i/time_range)
		temperatures[i].fill(outside_temp[math.floor(current_time)])
		
		for x in range (4):
			wanted_avg = 0
			for y in range(4):
				print((x*4)+y, " ")
				if np.isnan(compute_average_in_office(current_time, data[(x*4)+y][0])):
					wanted_avg = 17 + wanted_avg
				else:
					wanted_avg = compute_average_in_office(current_time, data[(x*4)+y][0]) + wanted_avg
				
			for y in range(4):
				if i==0:
					temperatures[i, x+1, y+1] = wanted_avg/4
				else:
					temperatures[i, x+1, y+1] = (wanted_avg/4 + temperatures[i-1, x+1, y+1])/2
					print(temperatures[i, x+1, y+1])

	return temperatures
		
def compute_average_in_office(time, data):
	who_in_office = []

	for i in range(4):
		if time >= data[i][0] and data[i][1] >= time:
			who_in_office.append(i)

	n_people_in_office = len(who_in_office)
	if n_people_in_office == 0:
		return 20

	sum_temp = 0.0
	for j in who_in_office:
		sum_temp += get_temp(time, data[j][2])

	return sum_temp/n_people_in_office

def get_temp(time, data):
	temp = data[0][0]
	for i in range(10):
		if time > data[i][1]:
			temp = data[i][0]
	return temp


def main():
	outside_temp = read_outside_temp('day_toronto')
	data = read_data('section_data')
	print(len(data))
	N_FRAMES_PER_MINUTE = 12

	temp = compute_24_hours_matrix(outside_temp, data, N_FRAMES_PER_MINUTE)

	for i in range(24*N_FRAMES_PER_MINUTE):
		fig = plt.figure()
		plt.imshow(temp[i], cmap=plt.cm.RdBu_r, interpolation='nearest')
		plt.plot([0.5, 0.5], [0.5, 4.5], 'k')
		plt.plot([4.5, 4.5], [0.5, 4.5], 'k')
		for j in range(5):
			plt.plot([0.5, 4.5], [j+0.5, j+0.5], 'k')

		plt.axis('off')
		plt.colorbar()
		plt.clim(0.0, 28.0)
		# ims.append([im])
		# plt.show()
		if(i > 99):
			plt.savefig('picfolder1/00' + str(i) + '.jpeg')
		elif(i>9):
			plt.savefig('picfolder1/000' + str(i) + '.jpeg')
		else:
			plt.savefig('picfolder1/0000' + str(i) + '.jpeg')



if __name__ == '__main__':
	main()