import numpy as np 
import pickle

def generate_custom_temp_per_person(n_people, mean_temp, std_temp, section=0):
	custom_temp_cont = np.random.normal(mean_temp, std_temp, n_people)
	for i in range(n_people):
		custom_temp_cont[i] = round(custom_temp_cont[i]*2)/2

	return custom_temp_cont

def generate_checkin_and_checkout(n_people, n_days, mean_checkin, std_checkin, mean_checkout, std_checkout, section=0):
	checks = np.zeros((n_days, n_people, 2))

	for i in range(n_days):
		checkins_day_i = np.random.normal(mean_checkin, std_checkin, n_people)
		checkouts_day_i = np.random.normal(mean_checkout, std_checkout, n_people)

		for j in range(n_people):
			checks[i, j, 0] = checkins_day_i[j]
			checks[i, j, 1] = checkouts_day_i[j]

	return checks

def generate_ups_and_downs_per_section(checks, custom_temps):
	N_UPS_AND_DOWNS = 10

	adcanved_checks = []
	for i in range(checks.shape[0]):

		person_list = []
		for j in range(checks.shape[1]):
			ups_and_downs = np.random.randint(2, size=N_UPS_AND_DOWNS) #0 is down, 1 is up
			start_time = checks[i, j, 0]
			end_time = checks[i, j, 1]
			time_for_ups_and_downs = np.random.uniform(start_time, end_time, size=N_UPS_AND_DOWNS)
			time_for_ups_and_downs = sorted(time_for_ups_and_downs)

			ups_and_downs_list = []

			ups_and_downs_list.append((custom_temps[j] ,start_time))

			current_tmp = custom_temps[j]
			for k in range(N_UPS_AND_DOWNS):
				if(ups_and_downs[k]) == 0:
					current_tmp -= 0.5
				elif(ups_and_downs[k]) == 1:
					current_tmp += 0.5

				ups_and_downs_list.append((current_tmp, time_for_ups_and_downs[k]))

			ups_and_downs_list.append((np.nan, end_time))

			person_list.append((start_time, end_time, ups_and_downs_list))

		adcanved_checks.append(person_list)

	return adcanved_checks
	
def main():

	data_per_section = []
	for i in range(16):
		a = generate_checkin_and_checkout(4, 1, 8, 0.1, 17, 0.5)
		b = generate_custom_temp_per_person(4, 20, 1)
		c = generate_ups_and_downs_per_section(a, b)
		data_per_section.append(c)

	with open('section_data', 'wb') as f:
		pickle.dump(data_per_section, f, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
	main()




