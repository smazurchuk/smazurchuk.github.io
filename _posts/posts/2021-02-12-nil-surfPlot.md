---
layout: post
title: Cifti Surface Plots
date: 2021-02-12
author: Stephen
---

# Nilearn Surface Plot

The [NiLearn](https://nilearn.github.io/) library has some very nice plotting functions. One of my favorite features of the library is the ability to create stand-alone surface plots like the one below!

<iframe src="https://smazurchuk.github.io/assets/left_hem_SOE.html" title="Example Surface Plot" width="1000" height="600"></iframe>
<p align="center"><em> Example of surface plot </em></p>

While I often create *ad-hoc* surface plots, I thought I thought I might actually document the process both for my future reference, and to help others.

First, I'll go through the general case: suppose we have some cifti file on the standard hcp 32k mesh (like a `.dscalar.nii` file). It might be nice to create an interactive visualization of this file for a presentation/website. I'll outline the steps to doing this below, but first two quick notes:

1. To keep stand-alone files small and have the demo work on most machines, it's best to downsample the 64k cifti file to the 10k free-surfer mesh. This also saves bandwith and helps the visualization to load faster. 
   
2. The Nilearn surface plotting function is designed to deal with hemispheres separately.

## Converting to Gifti

The first step is to separate the input file into two hemispheres for separate processing. To do this we will use [`-cifti-separate`](https://www.humanconnectome.org/software/workbench-command/-cifti-separate). The command will look like:

```bash
wb_command -cifti-separate $inputF COLUMN \
-metric CORTEX_LEFT inputLeft.dscalar.nii \
-metric CORTEX_RIGHT inputRight.dscalar.nii
```

We are now ready to downsample! Fortunately there is a nice HCP document ([here](https://wiki.humanconnectome.org/download/attachments/63078513/Resampling-FreeSurfer-HCP.pdf)) that covers how to convert from a cifti file to a gifti file. I summarize the key part here. We can downsample using the following workbench command [`wb_command -metric-resample`](https://www.humanconnectome.org/software/workbench-command/-metric-resample). The documentation for this functions recommends using using the `ADAPT_BARY_AREA` option which will give us a command that looks like the following:

```bash
wb_command -metric-resample <metric-in> <current-sphere> <new-sphere> \
ADAP_BARY_AREA <metric-out> -area-metrics <current-area> <new-area>
```

This command will have to be run separately for the two hemispheres. If we assign the input file to the variable `$inputF` and the needed files for the left hemisphere are:

| Argument           | File                                                    | Description                                                                                  |
|--------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `<metric in>`      | `$inputF`                                               | Metric file to resample                                                                      |
| `<current-sphere>` | fs_LR-deformed_to-fsaverage.L.sphere.32k_fs_LR.surf.gii | A sphere surface with the mesh that the metric is currently on                               |
| `<new-sphere>`     | fsaverage5_std_sphere.L.10k_fsavg_L.surf.gii            | A sphere surface that is in register with `<current-sphere>` and has the desired output mesh |
| `<current-area>`   | fs_LR.L.midthickness_va_avg.32k_fs_LR.shape.gii         | A metric file with vertex areas for `<current-sphere>` mesh                                  |
| `<new-area>`       | fsaverage5.L.midthickness_va_avg.10k_fsavg_L.shape.gii  | A metric file with vertex areas for `<new-sphere>` mesh                                      |

The relevant files can be found in a zip file realeased by WashU ([here](http://brainvis.wustl.edu/workbench/standard_mesh_atlases.zip)) Assuming that all these files are placed in a directory called `refDir`, the final command looks like:

```bash
wb_command -metric-resample \
inputLeft.func.gii \
${refDir}/fs_LR-deformed_to-fsaverage.L.sphere.32k_fs_LR.surf.gii \
${refDir}/fsaverage5_std_sphere.L.10k_fsavg_L.surf.gii \
ADAP_BARY_AREA left.func.gii -area-metrics \
${refDir}/fs_LR.L.midthickness_va_avg.32k_fs_LR.shape.gii \
${refDir}/fsaverage5.L.midthickness_va_avg.10k_fsavg_L.shape.gii
```

## Creating Visualization

We are now in the fun part. One of the reasons for converting to the freesurfer5 10k mesh is because the Nilearn library has a buit-in helper function for retrieving the surface mesh and sulcal depth for this surface. The following python code can then be used to save a stand-alone view of a hemisphere!


```python
import numpy as np
import nilearn as nil
from nilearn import plotting

left  = nil.surface.load_surf_data('left.func.gii')
right = nil.surface.load_surf_data('right.func.gii')
bg = nil.datasets.fetch_surf_fsaverage5(mesh='fsaverage5')

img = plotting.view_surf(bg['pial_left'],left,bg_map=bg['sulc_left'])
img.save_as_html('leftHem.html')
```

Finally, the last step in this process we will clean up all the files generated in this process

```bash
rm inputLeft.dscalar.nii inputRight.dscalar.nii left.func.gii right.func.gii 
```

For convience, we can combine all of these steps into one single python script. This script will take in a `.dscalar.nii` file and output two html files in the directory where it was called. 

**I recommend reading the options**

The main one being choosing whether the input file is a mask or not

<script src="https://gist.github.com/smazurchuk/955daf0fd9d4943b03026831a402389a.js"></script>

If you have the RCC mounted, just use the following

```
echo "alias nilPlot='python /group/jbinder/work/smazurchuk/nil_surfPlot.py'" >> ~/.bashrc
```

## Notes:
* You cannot set alpha values on the surface plot. I tried many times.