---
layout: post
title: Linear Dimensionality Reduction
date: 2020-03-28
---

While there are many high-level descriptions of both Principle Component Analysis (PCA) and Independent Component Analysis (ICA), I thought I might write about a few key differences to solidify my own understanding. Both PCA and ICA are used as general dimensionality reduction techniques. However, the two methods operate under different assumptions and should not be confused with each other.

# Common to Both
What all decompositions seek to preserve is some distance between all pairs of points. Strictly speaking, this means that for the Euclidean metric, only rotations, flips, and translations are allowed (think all matrices with determinant=+-1). However, if we want to reduce the dimensionality of data, we necessarily need to discard some information. Most often, this corresponds to **a linear projection into a subspace**. Exactly how to determine which information should be "thrown away" depends on how we construct our projection matrix. This brings us to the two most common techniques 

## PCA 
Most are familiar with PCA. Given some data that is multi-dimensional, the goal is to reduce the dimensionality of the data while still explaining as much of the **variance** as possible. In some sense, PCA can be thought of as fitting ellipses to data.
Crucial to how PCA explains variance, one can visualize it as finding lines in a high dimensional space in which the data appear very spread out. This approach makes the most intuitive sense when one considers the underling variables of interest as *uncorrelated gaussian random variables*. This brings us to our first point:

PCA performs source separation *if* the underlying variables are gaussian

# Point 1:
If a signal is assumed to be a linear combination of **independent** gaussian sources along with gaussian noise, then PCA and ICA optimize the same objective function. This should make sense from what we have just described

# Corollary
1. The sum of two gaussian random variables is also gaussian!

This is important for understanding as it makes clear why PCA amounts to rotation of coordinates. In particular, PCA generates a subspace with orthogonal basis vectors which explain a maximal amount of variance.

Assume **X** and **Y** are normally distributed variables

$$ X \sim N(\mu_X,\sigma_X^2) $$

$$ Y \sim N(\mu_Y,\sigma_Y^2) $$

$$ Z = X+Y $$

then:

$$ Z \sim N(\mu_X+\mu_Y, \sigma_X^2+\sigma_Y^2) $$

This particular formula requires that the undying variables are uncorrelated, and independent, however these conditions can be relaxed and there is still a similar result.

# Why PCA works
PCA as matrix diagonalization. We know that matrices can be thought of as collections of vectors, and a vector can be thought of as a random variable. So to have two variables be uncorrelated means they have no covariance. But what is covariance? It is a dot product! That illustrates why it is always possible to generate a rotation which uncorrelates the variables!!

Say we have *N* dimensions in our data (often # columns). Taking each column as a vector with *u* observations (# rows), we know that N independent vectors will at most spread an N dimensional space (even if there u >> N observations).

We can take each column as a basis for this space, however, there is no reason to think the columns will be orthogonal. However, for any space, we can generate and orthonormal set of basis for the space! One way of doing this which is taught in many intro linear algebra courses is the gram-schmitt method.

# Gram Schmitt
Write about the method here

# More General
This orthognalization is normally done implicitly through SVD decomposition which generates unscaled principal components corresponding to the "left" eigen-vectors

## ICA
Now that we have good hold on PCA, we talk about ICA. First, and perhaps most importantly,**Correlation is linear**! Variables can be completely dependent (as in example 2), but uncorrelated! To summarize the discussion above, given two random variables, there is always a distance preserving transformation which uncorrelates the variables. **Note**, this is often called a *whitening* operation to make variables less co-linear. This is not the case for a different objective called Mutual Information (MI). For a more detailed discussion about what MI is, see my other post on the topic [Mutual Information](https://smazurchuk.github.io/2020/02/20/pmi.html)! Avoiding the details of how ICA is implemented, on a high level, a user *apriori* selects a target dimensionality, and a transfrom matrix is then created (often iteravly) which projects the original data onto a basis where the marginal distributions are as independent as possible (minimize MI of the target basis).

We can get a feel for what this means by making some examples. 

# Example 1: Independent Gaussian Processes
Let's generate two independent gaussian variables:

```python
import numpy as np
A = .8*np.random.randn(1000);
B = 3*np.random.randn(1000);
```

We can verify that these distributions are both uncorrelated and independent

```python
from sklearn import feature_selection as fs
m = fs.mutual_info_regression(np.c_[A,B],B)
m = m/max(m); r = np.corrcoef(A,B)
```
This gives the result of **m=.00045** and **r=.01**. Now, We can correlate these signals by simply rotating the axis which generates a dependence. First, we will create a rotation matrix of 45 degrees, and apply this to our data. Here, a 2x2 matrix is multiplied (using `@`) by our row matrix

```python
import seaborn as sns
r = np.array([[np.cos(45), np.sin(45)],[-np.sin(45), np.cos(45)]]) @ np.c_[A,B].T
sns.jointplot('A','B',data=pd.DataFrame({'A':r[0,:],'B':r[1,:]}))
```
![plt](/assets/rot_joint_plt.svg)

We again calculate our correlation coefficient along with the mutual information!

```python
from sklearn import feature_selection as fs
m = fs.mutual_info_regression(r.T,r[1,:].T)
m = m/max(m); r = np.corrcoef(A,B)
```
This gives us the result of **m=.11** and **r=.84**! Our intuition should be confirmed! For a more general case, we could consider the overall dependence of these metrics on angle of rotation.

# Example 2: Sensitivity to Rotation
The following code will generate a plot of our metrics based on angle of rotation.

```python
A = .8*np.random.randn(1000); B = 3*np.random.randn(1000);
theta=np.linspace(0,np.pi,100);
vals = np.zeros((100,2))
for num in range(len(theta)):
    r = np.array([[np.cos(theta[num]), np.sin(theta[num])],[-np.sin(theta[num]), np.cos(theta[num])]]) @ np.c_[A,B].T
    vals[num,0]=np.corrcoef(r[0,:],r[1,:])[0,1]
    m = fs.mutual_info_regression(r.T,r[1,:].T)
    vals[num,1]=(m/max(m))[0]
plt.plot(theta*180/3.14,vals); plt.grid(True)
```
![plt](/assets/MI_vs_Corr_rotation.svg)

As you might expect, correlations have a natural depedence on basis you choose to represent your data in! However, M.I. is a much more invariant measure to the particular choice of basis.

# Example 3: Dependent Uniform Processes
There are other sorts of distributions we can look at for comparing our two metrics. A common example used to demonstrate the difference between correlation and dependence is a modified uniform distribution. We can create two completely dependent variables from a uniform distribution using the `abs()` function
```python
X = np.random.uniform(-1,1,500);
Y = np.zeros(len(X)); Y[X<0]=-X[X<0]; Y[X>0]=X[X>0];
sns.jointplot('X','Y',data=pd.DataFrame({'X':X,'Y':Y}),xlim=[-1,1])
```
![plt](/assets/uniform_depedent.svg)

For this plot, the M.I is 1, but the correlation is **.02**! Clearly, we see how limited the information correlation gives us is.

# Example 4: Spirals!!
A fun example of data which from afar looks gaussian but up close isn’t are spirals! To get a general equation for a spiral, we can convert from polar coordinates. A line in polar coordinates:

$$ r(\theta) = \theta $$

![plt](/assets/pol_line.svg)

We can then convert this to parametric coordinates and scale the axes seperatly

$$ x = .2*t*Cos(t) $$

$$ y = .1*t*Sin(t) $$

This now looks like an ellipsoid spiral. We can rotate any parametric equation by an angle $$\theta$$ using the following equations:

$$ u = x Cos(\theta) - y Sin(\theta) $$

$$ v = x Sin(\theta) + y Cos(\theta) $$

Applying this transformation we get the following plot

![plt](/assets/rot_pol_line.svg)

We can create these data points in python and look at the marginal distributions
```python
theta=3.14/4
t = np.arange(0,40,.2); 
x = .2*t*np.cos(t)
y = .1*t*np.sin(t)
u = x*np.cos(theta)-y*np.sin(theta);
v = x*np.sin(theta)+y*np.cos(theta);
sns.jointplot(u,v)
```
![plt](/assets/spiral_marge.svg)

Again, we find that the correlation is **.576** but the M.I is **.02**. This tells us that mutual information has **missed** the depedence. However, in the above discussion, we have glossed over a free parameter of the M.I. function in python: the number of nearest neighbors to consider. We can see the best that our function performs by iterating over all values for nearest neighbors.

```python
m=[]; ind=[];
for i in range(1,80):
    ind.append(i)
    tmp1 = fs.mutual_info_regression(u.reshape(-1,1),v,n_neighbors=i)
    tmp2 = fs.mutual_info_regression(v.reshape(-1,1),v,n_neighbors=i)
    m.append(tmp1/tmp2)
plt.scatter(ind,m)
```
![plt](/assets/mut_info_nn.svg)

We see that there appears to be an upper limit. Another consideration are different symmetric shapes. If we change the parametric parameter to `t=np.arrage(0,400,5)` we get the below shape:

![plt](/assets/spiral_marge_2.svg)

![plt](/assets/mut_info_nn2.svg)

This shows us the difficulty in finding the proper number of nearest neighbors: For the first case, more neighbors was better. For the second case, it turned out 2 neighbors was optimal!

## Closing Thoughts
In the above discussion, we looked at some of the underlying differences between PCA and ICA with a focus on what mutual information looks like for some specific pairs of random variables. Like most things in research, I think the results emphasize how important it is to be familiar with your data to know what marginal distributions look like, and how that impacts the results of different dimensionality reduction techniques. 

