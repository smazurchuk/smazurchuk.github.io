# On Concepts and Meaning

It's difficult to write out an ideas abstract concepts that many of us have our own intuitions and pre-conceptions on. Even more difficult still to try to call upon people's intuitions to motivate a formulaziation of something abstract. However, even given this difficulty, I thank you for your understanding and I hope forgiving reading of the text that follows

## Problem Statement

The general task I am attempting to undertake is to define more precisely (i.e. formally) what *semantic meaning* is. This undertaking of what is surely an absurd task is difficult to do without knowing a readers personal background. Perhaps you have thought extensivly about perception, phenomenology, and the representation of concepts in the brain, but perhaps you have not. Given the (potential) variety of readers, I will try to strike a middle ground of explaining some background, but ommitting the vast majority background/motivation due to the desire not get too bogged down before even starting. However, due to the abstractness of the problem and the large amount of jargon that has been developed over the past few thousand years (primarily by philosiphers), I will write periodically use some jargon in-case it is clarifying for some. 

## Problem Motivation

Unfortunettely, I will not give too strict a motivation for most of the points here, but hopefully, at least from the surface of it, they seem intuitvly correct. Firstly, what is a *concept*? How can we define what, for example, a "ball" is? In all honestly, I think it is great to pause here and actually try defining what a ball is. Hopefully after some thought, this task strikes you as very difficult to do; at least difficult to do in any formal way that doesn't resort to recursive definitations that leave some ill-defined base-case (e.g. balls are round) or an appeal to platonic ideals.

It might seem that since for all practical purposes, we normally can agree on what a ball is, it isn't too important to really work on this problem. However, I would argue that since it certainly appears that concepts are the building block of cognition, that actually getting a better understanding of what a concept is is critical for understanding how cognition is actually implemented in the physical hardware of the brain. As to why it is an interesting question to understand how the mind arises the physical substrate of neurons, I'd be deeply curious what sorts of questions your mind considers. 




## Re-enforcement Learning

It's my personall feeling that the field of RL learning will have the most insight to give in an attempt to formalize intuition. The basic formulation is of an agent (or neural network) interacting with an environment.

![RL_basis](/assets/RL_basis.svg)

In the case of a simple agent that is a feed-foward neural network, the network is approximating what is called a "q" function. To make these things concrete, we can look at a computer agent that is trained to play the atari game pong. We will use a simple convolutional network following the design of AlexNet

![Q_learning](/assets/q_learning.svg)

The actual game is slightle more complicated, but follows the same basis. It is called coin-runner
<center>
<video style="width: 80%;" controls muted="">
        <source src="/assets/coinrun.mp4" type="video/mp4">
        Your browser doesn't support videos
</video>
</center>
<p align="center"><em> Trained model playing CoinRun. Left: full resolution. Right: 64x64 RGB observations given to the model.</em></p>

![Network Design](/assets/networkDesign.svg)

Here, a given set of observations is mapped to an output space that can either be `Move Left` `Move Right` or `No Move`. Skipping the details of how such a model is trained, we can imagine that we update weights in the neural network until it plays the game quite well. That is excatly what was done in this paper!

[gameGif]()

Great! A natural question to ask next is has this network learned anything akin to *concepts*? 

## Can RL agents learn concepts?

The following distill publication addresses this question, in what is for my money, 

I **implore** you to play around with this interface below. It is taken from the distill publication (here) and for my money, is **the** critical window into what a concept is. What the interface is able to do is go into 

My feeling is that this interface (and their analysis) *emphatically* answers the question that something like semantic conepts are represented in the network. 

<iframe src="/assets/static_pages/understanding_rl/" title="RL Visualization" width="1000" height="1000" scrolling="no"></iframe>


### Understanding meaning Attribution

This is a superficial covering of the result 

### Defining a Concept

To understand the result of performing NMF on intermediate representations in a neural network we first have to give a bit of detail on NMF. For this section, I will think about NMF focusing on its similarities to PCA (I will later talk about differences)

First, NMF is being performed not on the activations of layer 2b, but on the *amount of reward assigned to each neuron in layer 2b for a given observation*.

To make the example concrete, we will take the trained network and a case of 5,000 random observations from across games. What the network ultimately does is assign an expected reward value to each observation. Since the network is purely feed-forward, we can assign this equivalent reward to each layer of the network. Using the method of integrated gradients, for each observation, we can assign some component of the expected reward to each neuron in layer 2b. We can concatenate this inta a matrix that is [5,000 , 780]. What PCA and NMF will do is decompose this matrix so that each particular observation is just the sum of some small number of states

$$ \text{Obs}_i = w_1 PC_1 + w_2 PC_2  \ \ ... $$

As I understand it, what is then visualized the contribution in the input space (i.e. some weight assigned to each input pixel) that quantifies how much that pixel is effecting the loading of the hidden state on the given principal component (or non-negative matrix factor).

If you follow that, brilliant!

> Given a system that maps $$ R^n $$  to $$R^m$$, concepts are the highly occupied regions in phase-space (i.e. attractor basins) and *meaning* arises from the degrees of freedom implicit in the systems dynamics

# Implications

## Concepts arise out of the reward function



## The "meaning" of a concept


The primary focus of the first part of this writing

How do we define what a concept are.