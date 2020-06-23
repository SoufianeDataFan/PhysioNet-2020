import os
from os import path
import shutil

####### All you need is to create parent directory and put run the .sh file inside it.
# Parent_dir/
# ├── data
# ├── physionet-challenge-2020-12-lead-ecg-public
# │   ├── Training_2
# │   ├── Training_PTB
# │   ├── Training_StPetersburg
# │   ├── Training_WFDB
# │   └── WFDB

src = '/path/to/parent/dir/' # Change your directory from here.
dst = os.path.join(src,'data')
data_files = ['Training_StPetersburg', 'Training_WFDB', 'Training_PTB', 'Training_2', 'WFDB']

# create file if it doesn't exist.
if not os.path.exists(dst):
    os.makedirs(dst)


# move file from a dir to another
def move_files(list_f):
#### warning: I advise against using shutil.move, because in the case of failed run, you risk
#### to lose your subjects files, and you'll have to repeat the download process from the start.
    for f in list_f:
        print(f)
        shutil.copy(f, dst)

# want to move only the subject files and not any other files in the dir
def lambda_file(x):
    if x.endswith(tuple(['.mat', 'hea'])) :
        return os.path.join(src_, x)


##### this is a parallelized for loop. It will run this code on all your CPUs
##### independently for faster run time.

for data_file in data_files:
    # go to one file
    src_ = os.path.join(src, data_file)
    # get list of subjects' files
    list_of_files= list(map(lambda_file, os.listdir(src)))
# start the parallel process
    from multiprocessing import Pool, cpu_count
    n = round(len(list_of_files)/cpu_count())+1
    files= [list_of_files[i:i + n] for i in range(0, len(list_of_files), n)]

    with Pool(processes=cpu_count()) as pool:
        print('processing ..')
        res1 = pool.map(move_files, files)

    pool.close() # shut down the pool
