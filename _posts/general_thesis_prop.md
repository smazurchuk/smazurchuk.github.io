# What is the goal??

An underlying assumption of todays langauge models is that word meanings can be represented as vectors. This is largely driven by the versatility of vectors to represent many abstract objects. Considering sets of objects and some rules for relating items in the sets is the basis of math. As such, it seems natural delve into all the machinery that has already been thought of.

Flipping the standard paradigm on its head, we might not concern ourselves with picking any particular representation of a word an only ask: "What are the rules governing the mapping between words". One sense of this question is asking what sorts of things can be done to a word while keeping in tact some essential meaning. For example, saying that I ordered a ____ at the restaurant somehwat constricts what word is allowed to go in the middle 

The first clear case of this are adjectives. There are manys

So, phrased in terms of abstract algebra there is a set of elements, here they are concepts, and we might suppose that there is a set of operations which map one element in the group into another.

$$ A = {a_1, a_2, a_3, ..., a_n} $$
$$ F{a_n} --> F{a_m} $$

Each element of the group might be able to be expressed as a vector in some space, which is was word2vec tries to determine, but there is also an analogous question about whethere we can determine the mappings without explicitly embedding the elements. Such a task is indeed daunting, but we might note a couple of hopefull features for such operators.
 
 1. Concepts are continous
 2. The manifolds are differentiable
 3. The group stucture can be determined from the commutative relatiohsips of the group generators
 
 The reason for considering this is ultimately, we are interested in finding the generators of the group. We might suspect that our brains have a natural disposition for learning groups 