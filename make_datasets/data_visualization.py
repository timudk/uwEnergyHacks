import numpy as np 
import matplotlib.pyplot as plt
import pickle

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

	temperatures = np.zeros((time_range, 5, 6))

	current_time = 0.0
	for i in range(time_range):
		current_time = 24*(i/time_range)
		for j in range(16): 
			avg = compute_average_in_office(current_time, data[j][0])

			num_x, num_y = compute_nx_ny(j)
			temperatures[i, num_x, num_y] = avg

	return temperatures
		
def compute_average_in_office(time, data):
	who_in_office = []

	for i in range(4):
		if time >= data[i][0] and data[i][1] >= time:
			who_in_office.append(i)

	n_people_in_office = len(who_in_office)
	if n_people_in_office == 0:
		return np.nan

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
	
	N_FRAMES_PER_MINUTE = 1

	temp = compute_24_hours_matrix(outside_temp, data, N_FRAMES_PER_MINUTE)

	for i in range(24):
		plt.imshow(temp[i], cmap=plt.cm.RdBu)
		plt.show()

if __name__ == '__main__':
	main()