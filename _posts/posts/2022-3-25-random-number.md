## Generating a Random Selection

Hi all, 

This post is mainly to serve as a *very* light introduction to choosing a random number in python. Whenever there is money or something signifigant on the line for a random selection, it can also be usefull to have transparency so that people can feel confident in the result. Shown here is a way to generate just that, and right in web browser! This will allow people to reproduce a result and have confidence in the unbiased selection of a number :)

# Selecting a number from 1 to *n*

The only two things we have to define are"
 
 * The number **n** 
    * **Note**: Python is zero indexed. This means that that to pick a number from 1 to 5 (including both 1 and 5), we should choose *n* to be 5, but remember that python is really choosing from the list [0,1,2,3,4]. This means a result of 0 should be mapped to the first choice (i.e. 1) and a result of 4 mapped to 5.

 * A random seed. This helps make the results reproducible

We will use the [`choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html) function in numpy to make our selection. Click the link to read the function documentation. 

Therefore, using a random seed of 8739 (made up) and choosing from 20 participants, our code would be

```python
import numpy as np
rng    = np.random.default_rng(8739) # Define random number generator with seed
n      = 20 # Choose from list [0-19] (inclusive)
choice = rng.choice(n)
print('The number chosen is: '+ str(choice+1))  # I added 1 so that choice 1-20
```

Try copying this code into the below REPL! Remeber to hit **shift + enter** to evaluate code

<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="400px"
></iframe>

Adjust the number and seed for your particular needs!

