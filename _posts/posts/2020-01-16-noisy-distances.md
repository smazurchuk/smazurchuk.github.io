---
layout: post
title: Distance Metrics and Noise
date: 2020-01-16
---
Representational Similarity Analysis (RSA) is a widely used data analysis method used in fMRI. It is a form of Multi-Voxel Pattern Analysis (MVPA). In essence, it utilizes dissimilarity matrices to whether two datasets are expressing the same underlying information. Critical to this method is the underlying choice of distance metrics.

There are many ways to calculate 'Distances' between two vectors. Some of the most familiar are euclidean, correlation, and others. In Kriegesckorte's original paper, he reccomends using the Mahalanobis distance. 

## Distance Metrics

Starting broadly, in mathematics a *metric* is a function that defines a distance (~mapping to the reals) between each pair of elements of a set which meets 4 conditions. The details of this are outside the scope of this post, but it is worth pointing out that the metrics of most common study are of a bilinear form and are called [*Metric Tensors*](https://en.wikipedia.org/wiki/Metric_tensor). This means that the metric follows a general form of:

$$ B(\bf{v},\bf{w}) = x^{T}Ay $$

# Cross-Validated Mahalanobis
The central idea that underlies cross-validated mahalanobis is that you have **2 estimates** of the difference between the vectors. I wrote a matlab script to calculate the cross-validated mahalanobis distance between points in the presence of noise.

```matlab
X = 5*rand(100,20);      % Generate 100, 20 dimensional points (true signal)
s1 = X+randn(100,20);    % Add normally distributed noise to signal
s2 = X+randn(100,20);    % Add normally distributed noise to signal

s1 = s1*(cov(s1)^(-1/2)); % Normalize signal by covariance matrix
s2 = s2*(cov(s2)^(-1/2)); % Normalize signal by covariance matrix

for j=1:100
    for k=1:100
        d(j,k) = (s1(j,:)-s1(k,:))*(s2(j,:)-s2(k,:))'; % Calculate pairwise distance matrix
    end
end

estimated_distance = d(tril(ones(size(d)) == 1, -1));  % Get just the lower triangular part
true_distance      = pdist(X, 'mahalanobis');
```


## Examples

Here, I used Matlab to get a better feel for how these metrics respond to noise. The first major point is that **most** distance metrics **overestimate** distances in the presence of noise. An exception to this rule is the cross-validated Mahalanobis distance.

[ ![](/assets/est_dist_w_noise.svg)](/assets/est_dist_w_noise.svg)
<p align="center"><em> We can see that euclidean distance OVER estimates with noise, but other distance metrics are less sensitive to noise </em></p>

While there is a clear difference between some of the distance metrics, we might wonder if this makes a difference? To do this, we can perform a mantel test on dissimilarity matrices produced from pure signal, and in the presence of noise.

[ ![](/assets/mantel_with_noise.svg) ](/assets/mantel_with_noise.svg)
<p align="center"><em> Mantel test in the presence of noise. It is important to note that there are TWICE as many measurements that go into the cross-validated distance metrics as compared to the other distances </em></p>

We can see noise seperates out the metrics. We see that the euclidean distance over-estimates distances in the presence of noise, it strongly outperforms pearson correlation. Standardized euclidean happens to give identical results as cosine for our particular toy data. We also see that for our purposes, general mahalanobis performs the same as euclidean or cosine.

A matlab script which will generate these two figures can be found here:

[Distance Analysis](https://github.com/smazurchuk/smazurchuk.github.io/blob/master/assets/dist_analysis.m)

