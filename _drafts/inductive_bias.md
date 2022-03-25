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

# Random Thought

Have you ever thought about how long you would have to simulate a box of water before it would start forming some complex interactions? I'm not sure how much it crosses your mind, but I often think that the best way to find out the necessary pre-requisites for life is simulation. 

# Where do concepts come from?

Suppose I had finished writing out the thoughts above. The ultimate thesis is that there has to be some objective function in order to define meaning. Meaning has to do with how some things effect some variable of interest. Although that definition might seem incredibly abstract, at the core of it, I think that we can agree that life must have some objective function. I hesitate to immediately phrase it in terms of one (i.e. maximize dopamine). That might be the immediate reason we make a particular decision, but that is surely an awful objective function. There has to be a system so that we don't overfit that particular objective (i.e. someone could gain a mutation that floods their brain with dopamine. This would be pretty useless and in principle, probably selected against). That leaves us with needing to abstract a level and think about what is selected for in life forms. I think that we have a general intuition about what this should be, but ideally, I'd love for it to fall out of first principles. That begs the question: what are the minimum set of principles?

## Determining the Principles

Critical to solving this problem is determining the right level of abstraction. This motivated that line above: should we simulate atoms and wait to see if life arises from this? Surely how patently absurd this is strikes you. For example, several people at MCW do molecular dynamic simulations and they simulate proteins for **nano-seconds**. Imagine simulating a large sea (such as in the beggining of earth). Now remember that single cells took at least a billion years to appear, and then, remember that it was only single cells for another billion years. This hopefully motivates that it is not the right level of abstraction. At the other level, simulating full agents already requires us to explicitly state the objective function and include assumtions (e.g. imagine agents playing some game. By fixing the rules, we've already introduced many assumptions and perhaps dictated the optimal behavior and probably won't gain too much insight into the natural formation of "conscious" agents.)

So, what are we to do? This is the point I was stuck at in my head the other day. I don't really have any easy answers on this one. My gut is to mix hebbian networks with some randomness and time evolution. The reasoning for this is that hebbian networks have a natural sense of energy and with each time step, minimize energy. This is nice and it is a general physical principal of the universe (or at least something analogous to it). Secondly, there is perhaps a way to just add noise to weights, and then what is needed is to determine the rule for selection. This is critical. Without it, I think we would just be simulating something akin to atoms in a box. It might take billions of years for anything to happen. This has to be accelerated with some assumptions. The question is which ones should be included. 

The natural one that comes to me is that if entropy is increased(?) then we have a decay value associated with how much randomness should be included with the updated weight. Perhaps we should immediatly simulate the target. Namely, we want a system that starts with high entropy, and we then find systems that minimize it. In the macro-scale, we might make the arguement that local decreases in entropy are always associated with global increases in entropy. But, that seems to miss the point. All the entropy in earth is minuscule compared to that of the sun. Perhaps there is an edge-effect, where places of very high entropy (the sun) and places of very low entropy (core of the earth) can have places of very high complexity form on the interface (just the surface of the earth). `