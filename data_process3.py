import csv

data_name = 'birrt'
# open CSV file
csvFile = open('./data/' + str(data_name) + '.csv', "r")
reader = csv.reader(csvFile)
result = []
data = []

# process CSV file
for index, item in enumerate(reader):
	result.append(item)
csvFile.close()

print(len(result))

for i in range(0, len(result)):
	if i != 0:
		if "c_max" in result[i]:
			data.append(result[i-1])
		elif i == len(result)-1:
			data.append(result[i])

# save CSV file, and "newline" can delete the free space between two lines.
csvFile1 = open('./data/final_data/' + str(data_name) + '_final.csv', "w", newline='')
writer = csv.writer(csvFile1)
for i in range(0, len(data)):

	writer.writerow(data[i]) 	# save row by row

csvFile1.close()

# the following three lines of code can be used to drop duplicate line.

# frame = pd.read_csv('./data/data_50/' + str(data_name) + str(i) + '.csv', engine='python')
# data = frame.drop_duplicates(subset=['c_max'], keep='first', inplace=False)
# data.to_csv('./data/data_50/' + str(data_name) + str(i) + '.csv', encoding='utf8')