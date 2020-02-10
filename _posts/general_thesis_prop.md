# What is the goal??

Much of machine learning is focused on learning the embeddings of a particular word. However, we might be able to flip this question on its head and ask: "What are the legal operations we can do to a word". By this I mean, what are the things we can do to a word while keeping in tact some essential meaning. The first clear case of this are adjectives. There are manys

So, phrased in terms of abstract algebra there is a set of elements, here they are concepts, and we might suppose that there is a set of operations which map one element in the group into another.

$$ A = {a_1, a_2, a_3, ..., a_n} $$
$$ F{a_n} --> F{a_m} $$

Each element of the group might be able to be expressed as a vector in some space, which is was word2vec tries to determine, but there is also an analogous question about whethere we can determine the mappings without explicitly embedding the elements. Such a task is indeed daunting, but we might note a couple of hopefull features for such operators.
 
 1. Concepts are continous

 2. The manifolds are differentiable
 3. The group stucture can be determined from the commutative relatiohsips of the group generators
 