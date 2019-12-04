---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: post
title: SOE Data to MNI Space
date: 2019-11-07
permalink: /posts/afni_reproc
---
The SOE data was processed with the intent of doing RSA analysis where the scans were aligned to anatomical space. However, I thought it might be a fun project to look at the functional connectivity of the patients that are already processed. The first step to accomplish this is re-processing the SOE data into MNI space for group analysis!

# AFNI Notes
Shana Terai wrote some scripts for processing the SOE data. These are very well documented, and well written. They should be looked at prior to this script, as these are based off of her scripts. I've written this largely for my own documentation.

# Re-Processing
Since the patients have already been processed once through Shana's scripts, I can re-process her files with an updated script.

Need to re-run the proc_py files and have alignment into MNI space. Shana's help function is great, and patients need to be queued one at a time. Once in the RCC, jobs should be run with the command
```
queue.SOE.ap.sp [ -s SUBJECT# ] [ -d SESSION# ] [ -r SEMAP#]
```
Note that the -d and -r options should be left blank so that all scans are reprocessed. This command then submits the proper jobs using the `SOE.ap.bySE` script which does all the real work. This script can be edited for the SOE data to MNI space by editing the `afni_proc.py` script call. 
Here is the updated call.

```
afni_proc.py -subj_id SOE_${subj}_${sesh}_SEmap${SEn}                   \
        -dsets $dsets                                                   \
        -copy_anat SOE_${subj}_T1w_acpc_dc_restore_brain_1mm+orig       \
        -blip_forward_dset SOE${subj}_SEmap${SEn}_AP.nii.gz             \
        -blip_reverse_dset SOE${subj}_SEmap${SEn}_PA.nii.gz             \
        -blocks despike tshift align tlrc volreg  mask scale                 \
        -volreg_align_e2a                                               \
        -tlrc_base MNI152_T1_2009c+tlrc                                 \
        -tlrc_NL_warp                                                   \
        -volreg_tlrc_warp                                               \
        -anat_has_skull no                                              \
        -align_opts_aea -giant_move                                     \
        -align_epi_strip_method 3dSkullStrip
```
The only change I made was adding the three tlrc commands which were taken from the AFNI proc_py documentation. The only other editing that I made to Shana's script was chanigng the output_dir variable to a directory under my username.

The next steps are to re-process the patients and use nilearn for some ICA!


## Notes
* Shana has the check for SE maps after the job is submitted, which works, but could be in the main script (the queue script)

* I dont think the original proc_py used the `combine` option which should optimally combined the steps
  
* Not sure why 'giant_move' was used instead of some other option

* Not sure what the '-F' option is in the torque script
  

