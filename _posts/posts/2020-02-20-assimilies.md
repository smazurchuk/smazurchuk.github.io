---
layout: post
title: Word Meanings Through Analogies
date: 2020-02-20
---
When I first learned about the ability of distributionally derived word representations to complete analogies I was very surprised. I thought, "surely we are on the cusp of deeply understanding language". I think that sometimes we get so used to common knowledge that it looses some of its wonder. Why should distributional models perform well at analogies? Shouldn't analogies be a generally difficult task which require deep understanding? Surely completing analogies requires at least as much semantic information (if not more) as assigning pronouns to their proper referent?

Of course, the field of linguistics has recognized the somewhat counter intuitive result that in-fact the reverse is true. It is surprisingly hard to assign roles to pronouns, but word-ratings have been shown to be capable of completing analogies since the 1970's! (source)

## Winograd Schemas

The [Winograd Schema Challenge](https://en.wikipedia.org/wiki/Winograd_Schema_Challenge) (WSC) is a test of machine intelligence that was proposed by Hector Levesque (UoT). Roughly, it is a pair of sentences which contain two noun phrases and an ambiguous pronoun which refers to different noun-phrases in the sentences. The prototypical example is given below:

> The city councilmen refused the demonstrators a permit because they feared violence.
 
In asking who *they* refers to, it seems a rather simplistic task to assign it to *the committee*. However, by just changing the last words, we can change the role asignment

> The city councilmen refused the demonstrators a permit because they advocated violence.

This demonstrates that what might seem a simple task which can simply be answered through syntactic regularities of language, actually requires understanding the semantics of the sentence.

## Motivation

So, why did I reference analogies and Winograd schemas? Well, it is motivated by the success of word rating models at solving analogies. My hunch is that 

## Looking for Analogies
Following this line of thought, I considered whether we could derive word meanings through the use of assimilies in literature. For example, the sentence

> He was fast like a cheetah
 
Tells us a prototypical feature of cheetahs; namely, that they are fast! In general, I considered whether looking for phrases such as "like a" followed by a noun to be able to give insight to the prototypical features we have for different objects. To this end, I searched 16,000 free eBooks for "like a"

```python
string = "like a"
sentences = os.popen('grep -r -i -w -h "'+ string + '"').read().splitlines()
```
 
This command found 490,000 examples. So, just randomly clicking through them, what are the examples?

> Make me a offer, Mister Beeler. I’d like a offer if you’d care to make one

Not quite what I had hoped. The first example uses the work in a literal sense!

> and Jean Claude would retreat like a disparaged puppy

A puppy retreating? I think puppies are cute and innocent, hardly disparaging or retreating

> spires that reached to the heaven like a cathedral of praise, bringing symmetry to its background

Cathedrals, reaching. Okay, maybe, but still, pretty hard.

> tool that the creature Fur-nose carried, like a rock used for opening nuts

 One thing that seems to be a trend is that it is not always clear what adjective is referencing the noun following "like a". If we are to have any hope, we will require a syntatic depedency parser.

> Together they watched Paul flitting ahead like a human dragonfly

Here, what the noun should be is not very clear! We clearly know that it should be *dragonfly*, but that is because we recognize *human* as an adjective and not noun.

With everything above given, I picked some of the more random examples. There are many examples for which the assimily was clear. For fun, some are included here:

>  The apartment was furnished, but it didn't look like a home

This tells that "look" is strongly associated with home! This is great!

> We continued going until we arrived at an open place like a plateau with many chambers

# "As a"

For the other kind of simily, we find a similar number of raw occurences of "as a". In looking at the examples, some are:

> “I’m not sure,” she said. “I usually read them as a set, not as individual"

Here we have a tricky assignment. Are sets (a rather abstract concept) usually visual (as would be indicated by *read*)?

> Tenderness in a man is not viewed as a manly thing

Oooo, here he have a negation. Another tricky case I had not considered! Not to mention, how should "thing" be handled?

> “You served as a vassal of the Queen in my childhood,” Headred said

Here I have included a positive example. Vassals serve!

> and blow up a transformer without so much as a scratch?” Dodger asked 

How would we handle common phrases such as "without so much ...". A tricky problem indeed. On top of the examples given above, one final tantelizing example was:

> as ever-present as a heartbeat

I think that this does tell us something deep about how we represent the concept "heartbeat". But how is it captured?



There is an interesting idea that we might learn about abstract concepts through the use of metaphors. Metaphores allow us to extend our embdied knowledge in useful ways. Maybe we can come up with a Reg-Ex expression to search for metaphores. This is i