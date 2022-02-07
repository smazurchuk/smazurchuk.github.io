# Background

A term that is gaining popularity in machine learning is *inductive bias*. This term has been around for a while, but for I haven't seen a succint/intuitive description of its importance. The following summarizes the key point as I understand it. The main punchline as I see it is:

> Inductive biases are the assumptions that are critical for how models **extrapolate** to new data. 

## Interpolation verses Extrapolation

To me, the critical jump that has to be made if we are to broach intelligence is not seeing how a machine/algorithm responds to new inputs that are from the same sample distribution as the input/output. Intelligence, however it is ultimately defined, has to be a measure of what models predict under new circumstances. 

## Prerequisits

This section just summarizes what a joint distribution is. It's a *very* cursory overview/refresher

We all (hopefully) have an intuitive sense of what a distribution is[^1]. It's a something that tells you the probabibility of a particular state for a system. A very simple system could be a sigle coin that can either be in either the HEADS or TAILS state with equal probability. This system has one degree of freedom and the corresponding distrubtion of the probability of different states is pretty boring. 

[simpleSystem]

Another system could be 3 fair coins. The state-space of this *system* is now three dimensional as there are three "random variables" we are measuring. The distribution that characterizes the probability of any particular state is called the **joint distribution**. If each coin is indepedent, then (**only then**) the joint distribution is the product of the marginal distributions. A marginal distribution is just the distribution of each individual coin. 

## Short Background

Any set of observations can be thought of as a joint distribution. For example, a common dataset in machine learning is a large collection of images. For simplicity, let's assume each picture is 100x100 pixels (so to a computer each picture is a list of 10,000 numbers). Supposing that we have a collection of 5,000 of such images we then have 5,000 observations of 10,000 dimensioal vectors. It is hopefully easy to see why pictures can be thought of as a joint distribution. We could think of each pixel value as being a random variable (here, it corresponds to a particular intensity value in a location of an image)! It is also hopefully clear that this joint distribution is (almost certainly) **NOT** the product of the marginal distributions. This is because only in the case of perfect noise would each pixel value be completely indepedent of every other pixel value in the image. At a minimum, for almost any image, one pixels value will likely correlate with nearby pixel values.

## Machine Learning

Why talk about joint distributions? Because learning can be thought of as modeling joint distributions. 


 For the intuitive case of physical sensors (i.e. cameras, microphones, force sensors) we can imagine that the state of a system at a given time is given by some list of numbers. 


each instant[^1] could there is some list of numbers that captures  could be collectivily thought of as capturing the major components of the information that comes into a brain. In the case of a biological system, we could think we can model  natural kindsTake for example two sensors that measure something out in the world. Below are twenty outputs from the two sensors.


me I think that the basis of it has become more clear to me, so I thought I might make a little description of it as I understand it.

For reference, there is this recent paper by Anirudh Goyal and Yoshua Bengio all about this topic.

[img here];

For me, there was insight when I realized that anytime we are fitting a model to data, there are *always* inductive biases. Where these biases come to bear are not so important when our model is explaining training and testing data that are coming from the same overall distribution. 

A recent push in machine learning has been to focus