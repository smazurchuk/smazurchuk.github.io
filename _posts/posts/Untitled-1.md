# I Would like to create a script which processes the fMRI data from start to finish. I think
shana's script is very readable, so I will start from that point and then move forward

The central job is to feed the right arguements into the deconvolve line of afni.

The main inputs are the:
* the censor regressor
* target word regressor
* other words regressor
* word_length regressor
* 6 responses?
* motion demean
* motion derivative

## Creating Proper AFNI Files
3Ddeconvolve will take in files and generate a regression matrix. These are CSV files for each run

```python
import pandas as pd 
def build_large_file(subj):
    def last_7chars(x): 
        return(x[-7:])
            
    all_file_sorted = sorted(glob.glob(os.path.join(output_dir,subj,'*')), key = last_7chars)
    table = pd.read_csv(all_file_sorted[0], index_col = 'Word')
    table['stim_onset_time'] = table['stim_onset_time'] - table['scannerWait.rt'][0]
    table['trial_end_time'] = table['trial_end_time'] - table['scannerWait.rt'][0]
    final_table = (table[1:].drop(columns = ['scannerWait.keys','scannerWait.rt'])).dropna(axis = 1, how = 'all')
```

