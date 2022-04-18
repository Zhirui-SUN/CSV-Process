import numpy as np
import mne
import codecs
f = codecs.open('participants.txt', mode='r', encoding='utf-8')  # open txt file, read with‘utf-8’
line = f.readline()   # read file by line
list1 = []
while line:
    a = line.split()    # split data
    b = a[1:2]   # pick data we want
    list1.append(b)  # append to the list
    line = f.readline()
f.close()

for i in range(111):
    age = list1[i+1][0]
    if i < 9:
        name_input = 'data_edf/sub0'+str(i+1)+'.edf'
        name_output = 'data_csv/sub_0'+str(i+1)+'_'+str(age)+'.csv'
    else:
        name_input = 'data_edf/sub' + str(i+1) + '.edf'
        name_output = 'data_csv/sub_' + str(i+1) + '_'+str(age) + '.csv'

    print(name_output)
    # print(age)
    edf = mne.io.read_raw_edf(name_input)
    header = ','.join(edf.ch_names)
    np.savetxt(name_output, edf.get_data().T, delimiter=',', header=header)




