# How useful are these papers?

I was recently looking to see if there was a general consensus about the network connectivty changes that occur in people who have temporal lobe epilepsy (TLE). For those not aquainted with the field, resting state functional connectivity (rsFC) is very popular in functional Magnetic Resonance Imaging (fMRI). One popular thought is that resting stat

In performing this literature review, I came across two papers that are remarkably similar[^1][^2]. Below are screenshots and some text.

**Paper 1**

<img src="/assets/functionalHomotopy.png" width="800">

> Methods: [...] were included to collect the fMRI data and perform the voxel-mirrored homotopic connectivity (VMHC) and FC analyses

* 36 TLE patients, 37 healthy controls (HC)

**Paper 2**
<img src="/assets/voxelMirroredHomotopy.png" width="800">
 
> Methods: [...] Then VHMC analyses of bilateral brain regions were conducted

* 58 TLE patients, 60 HCs

Quite remarkable! Both papers, published within a year of each other, set out to examine VMHC in different datasets. So that begs the natural question: did they have similar results?

# Results

The first paper found decreases in VMHC values in TLE patients in bilateral inferior temporal gyrus (ITG), and higher VMHC values in bilateral lingual gyrus. The authors also report a postive correlation between the VMHC value of bilateral ITG and the HAMA test (r = 0.376, p = 0.024)

<img src="/assets/paper1Figs.png" width="800">
<p align="center"><em> Relevant figures from paper 1 </em></p>

What about paper 2?

The second paper found decreased VMHC in bilateral middle temporal gyrus (MTG) and middle cingulum gyrus (MCG) with no regions exhibiting increased VMHC values

## Method differences between the papers

The first paper used Data Processing & Analysis for Brain Imaging (BPABI) software to do preprocessing and analysis. Covariates of age, sex, and education were removed and the resulting differences were FDR corrected.

The second paper used the [RSET toolkit](http://www.restfmri.net/forum/) to perform the analysis. Results were random field corrected. 

# Our own data

After seeing these two papers, I was very interested in trying this analysis on our own data. To do this with a toolbox, the natural choice is the REST toolbox which performs alignment and all processing. However, since we already have all the data in the proper space and projected to the surface, the alternative is simply to calculate 

[^1]: Shi, K. et al. Altered interhemispheric functional homotopy and connectivity in temporal lobe epilepsy based on fMRI and multivariate pattern analysis. Neuroradiology 63, 1873–1882 (2021).
  
[^2]: Wu, J. et al. The decreased connectivity in middle temporal gyrus can be used as a potential neuroimaging biomarker for left temporal lobe epilepsy. Frontiers Psychiatry 13, 972939 (2022).

