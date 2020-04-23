---
title: Noise Ceiling
layout: slides
date: 2020-04-21
theme: simple
---
<div markdown="0">

## Noise in fMRI

**Note**: To advance through these slides, use the **spacebar** 

Also, you press control and click you can zoom-in <!-- .element: class="fragment" data-fragment-index="1" -->


--

## Great!
Using the space helps to keep the slide's in order, as opposed to just using the arrow keys

---

## Plan
One question that I'm interested in is:

<q>How much variance is shared across subjects when being scanned?

I'm interested in finding the "*noise ceiling*" of our data. To begin, I'll consider a pure noise case

---

## Outline
1. Generate random vectors
2. Calculate noise bounds on vectors which are just derived from a normal distribution

---

Noise Ceiling

The approach I am going to take is explained here:
* http://www.fmri4newbies.com/tutorial-7

The general points are as follows:
* The upper noise ceiling is usually calculated by correlating each participants RSM to the average RSM of **all** participants 
    * No model can exceed this upper bound as it represents the best possible model 
* The lower noise ceilling expresses how similar data is across participants. It is calculated by correlating one RSM to the average of all **other** participants 
    * If this is low, then there is little systemic variance across participants 
    * If a model outperforms the lower noise ceiling, it indicates that on average, each participants RSM is more similar to the model than the average of all other participants!

---

## Random Vecotors

![3 series](/assets/3_rand_series.svg) <!-- .element: class="fragment" data-fragment-index="1" -->

The Corresponding correlation values for this plot are:

|        | Green | Blue  | Orange |
|--------|-------|-------|--------|
| Green  |       | -.754 | -.335  |
| Blue   |       |       | .282   |
| Orange |       |       |        | 


<!-- .element: class="fragment" data-fragment-index="2" -->

---

## hello



## Generalization

This is meant to create some artificial data to see how well we estimate the noise ceilings. I'm also trying out a new presentation style.




## The General Approach
Let us assume we have **n** time series, and we want to know how ThI wanted to put in some fragments, so here is a list:
1. item 1 <!-- .element: class="fragment" data-fragment-index="1" -->
2. item 2 <!-- .element: class="fragment" data-fragment-index="2" --> 

---

## Slide three
This is a code block
```python
import numpy as np
np.load('file.npz')
```

---

<!-- .slide: data-background="#9e8c16" -->
## Different Color


</div> 