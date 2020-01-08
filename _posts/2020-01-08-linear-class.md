---
layout: post
title: Linear Regression and Linear Classification
date: 2020-01-08
---
This post is to detail the similarities between linear regression and linear classification techniques. First, we will consider some data for linear regression

Consider some data:

| X1                 | X2                | Category |
|--------------------|-------------------|----------|
| 0.11  | 0.96 | 1        |
| 0.2  | 0.57 |  1       |
| 3.29   | 4.22  | 2        |
| 5.02   | 6                 | 2        |
| 6.08   | 7.13  | 2        |
| 0.60  | 1.24  | 1        |
| 3.96  | 4.08  | 2        |
| 3.16  | 3.48  | 2        |
| -0.50 | 0.73 | 1        |
| 2.28 | 2.490  | 1        |
| 0.56  | 1.73  | 1        |
| 5.24  | 6                 | 2        |
| 1.50 | 2.900 | 1        |
| 3.68  | 3.79 | 2        |
| 0.86  | 1.48  | 1        |

![scatt]("../assets/scat1.svg")

Above, the regression can be thought of as finding some w's such that:
$$ X2 = w_1*X1 + w_0 $$
From here, one can a closed form solution of the form:
$$ w* = (X^TX)^{-1}X^Ty $$

In matlab, the above results can be found through:
```matlab
rz = rotz(-45); % Make rotation matrix
X = [10*rand(15,1),rand(15,1)]*rz(1:2,1:2); % Generate data
d = [X(:,1),ones(15,1)];
w = inv(d'*d)*d'*X(:,2);
hold on
scatter(X(:,1),X(:,2),[],c,'filled')
plot(X(:,1),w'*d')
hold off
```
![scattfit]("../assets/scat_wfit.svg")

## Classification
In order to change the above regression problem into a classification problem, we can simply use the columns X1 and X2 to regress out a third column (Category). After this, we can simply set a threshold (naivly, maybe 1.6) to classify! The code to do this in matlab is (note: I know the inline 'for' loop is terrible to read):

```matlab
g = [1,1,2,2,2,1,2,2,1,1,1,2,1,2,1];
d2 = [X, ones(15,1)];
w2 = inv(d2'*d2)*d2'*g';
g_hat = w2'*d2';
colors = zeros(15,3);
for i=1:15 if g_hat(i)<1.6 colors(i,:)=r; else colors(i,:)=b; end; end 
scatter(X(:,1),X(:,2),[],colors,'filled')
```
![scatt]("../assets/scat2.svg")

## Conclusion
In short, as you expect, for linearly seperable data, we can think of linear regression and linear classification as almost identical processes!

