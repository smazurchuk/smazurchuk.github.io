---
layout: post
title: The Somatopy of Language
date: 2020-01-14
---
I thought I might make a post of an idea that has been circulating in my head this past week.

# Background
Somatotopy is known to exist throughout many regions of the brain. From the visual cortex to the humunculus in the motor gyrus, it is a general theme that neurons close together in the cortex tend to represent similar things. For a more formal definition of somatopy, we can define it as:

> Somatotopy is the point-for-point correspondence of an area of the body to a specific point on the central nervous system [^1]

Practically speaking, this results in retinotopic, tonotopic, and sensory maps, shown below:

![](/assets/phase_gif.gif)
<p align="center"><em>Polar angle across the visual cortex </em></p>


Another well studied example is in the audutory cortex where there is tonotopy. The below gif shows a down-sweep of tones.

![](/assets/down_sweep.gif)

Both of these examples are taken from the website of [Marty Sereno](http://www.cogsci.ucsd.edu/~sereno/). A general question is: is there tonopy in the language system? If so, how might we go about exploring it?

## Language System
For a general idea of which parts of the brain are involved in word represention, we can look at computer-generated meta-analysis found at [NeuroSynth](https://neurosynth.org/analyses/terms/language/).

[![](/assets/lang_neurosynth.png)](https://neurosynth.org/analyses/terms/language/)

We can use this mask to select voxels of interest in MNI space. These b-values then make vectors for which we can look as the question:

> Are there any continous degrees of freedom exhibited by the system?

To do this in python, first, all the t-scores were converted into MNI space, and then the neurosynth mask was scaled and applied to the voxels.

```python
import os
import numpy as np
import subprocess as sp
import nibabel as nib

langMask = nib.load('language_association-test_z_FDR_0.01.nii.gz') #Neurosynth-Mask

volnames = list(set([k.rsplit('.',1)[0] for k in os.listdir('alignedData')]))
wordLabels = []; patLabel = []; wordVecs = []
for vol in volnames:
    g    = nib.load('alignedData/'+vol+'.HEAD')
    gg   = nib.brikhead.AFNIHeader(nib.brikhead.parse_AFNI_header('alignedData/'+vol+'.HEAD'))
    wordLabels.extend(gg.get_volume_labels()); patLabel.extend([vol.rsplit('.')[0]]*320)
    resamp_mask = nil.image.resample_to_img(langMask,g)
    wordVecs.append( g.get_fdata()[resamp_mask.dataobj >2,:].T ) #Threshold neurosynth mask at Z>2
allVecs = np.concatenate(wordVecs,axis=0)
```
The result of this is a 34,000 dimensional vector for **each word** in **each patient** which gives us a data matrix of **[7,000 by 34,000]**. This can then be analyzed using dimensionality reduction techniques such as PCA, tSNE, and Diffusion mapping. Unfortunately, after running these analysis, there was no 'naturual' ordering to the words, so for the moment, this is where my analysis ends. 

# References
[^1]: " Saladin, Kenneth (2012). Anatomy and Physiology. New York: McGraw Hill. pp. 541, 542.