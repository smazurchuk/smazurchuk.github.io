# General Background. 

There is a popular paper in Nature Communications that came out in 2018 that I recently re-assessed. Part of this was driven by the fact that it 



# Info about the paper

The paper has a Relative Citation Ratio of 4.42 indicating that it's about 4 times as influential as the *average* paper published the same year in the same field. At present (9/1/22) The paper has about 130 citations.

# Basic layout of the paper

While this blog-post is intended for people who are familiar with the paper and general field of the neural fMRI decoding, I'll provide a quick superficial summary here. For the analysis here, we are only concerned with the first experiment in the paper. Of note, while I'm leveraging most the forthcoming criticisms at the first experiment in the paper, the other experiments are built off of and depend upon the first experiment, so they are in general more applicable. 

In the first experiment the goal is to generate a robust neural activation pattern for different concpepts in participants. These beta maps are then going to be used to train a decoder by way of a distributional representation (Glove in this case).

# Data Leakage

The first **major** problem with the paper is that, at least as I understand it, there is data leakage in the method. 

I wanted to analyse the data seeing as it has been used in several publications. 

To ensure reproducibility, I will outline each step. 

The data can be downloaded here: 

<https://osf.io/crwz7/>

From this link you can download and extract `Pereira_Materials.zip`. 

The actual MRI data can be downloaded from this link:

<https://evlab.mit.edu/sites/default/files/documents/index2.html>

Note that each participant should be downloaded seperatetly. 

There are two general ways to asses the data. First we will process the data as was done in the initial publication, except we will use RSA. 

# Load the target representations

```matlab
targets  = readtable('vectors_180concepts.GV42B300.txt','ReadVariableNames',false);
targets  = targets{:,:};  % Convert table to array
concepts = readtable('stimuli_180concepts.txt','ReadVariableNames',false);
concepts = concepts{:,:}; % Place variables in variable
```

The result of this are two variables. 

# Load the data for a participant

We will follow the documentation and show how the data is loaded for just a single participant. Since `P01` took part in all three experiments, we will load their data. Some details outlined here are different from that on the evlab website I think because the website might just not be updated. The three central files we will load are:

* `examples_180concepts_sentences.mat`
* `examples_180concepts_pictures.mat`
* `examples_180concepts_wordclouds.mat`
  
Within each of these files are the variables:

```pre
	  examples              180x201011
	  keyConcept            180x1
	  labelsConcept         180x1
	  labelsConcreteness    180x1
	  meta                  1x1
```

Following the methodology of the paper, we will select the top 5,000 most reponsive voxels using the function provided in the zip file. To get a *score* for each function, we will use the following call signature:

```matlab
pictures = load('../../examples_180concepts_pictures.mat');
[scores] = trainVoxelwiseTargetPredictionModels(pictures.examples,targets,'lambda',1,'meta',pictures.meta);
```

Since the targets have 300 dimensions, the shape of the scores are `[300x201011]`. Following the paper, we take the maximum across the columns, and then take the top 5,000 voxels

```matlab
perf     = max(scores,[],1);
[~, topInds] = maxk(perf, 5000)
```

