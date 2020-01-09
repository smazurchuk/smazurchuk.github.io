---
layout: post
title: Linear Regression and Linear Classification
date: 2020-01-08
---
This post is to detail the similarities between linear regression and linear classification techniques. First, we will consider some data for linear regression which falls into two categories.

Consider some data:

| X1 | X2 | Category |
|----|---|---------|
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

![scattfit](/assets/scat1.svg)

To copy these variables, paste the following lines into matlab
```matlab
X = [0.110705312404362,0.962036338238243;0.195536168994095,0.567433726105442;3.29080172573339,4.21580925766402;5.02219607197230,5.99689256969713;6.07542982055026,7.13347594983259;0.599994589792336,1.23715662880782;3.96292001423081,4.08146134381088;3.15718188586238,3.48100422049278;-0.561666701284046,0.729987382373674;2.27606954894299,2.49156460997681;0.562861314317448,1.73074288392112;5.23577426251946,5.99710543566519;1.49624905326917,2.90499627947359;3.68201519547809,3.79257208848654;0.858292592800166,1.48433420568446];
r = [0.6350 0.0780 0.1840]; b=[0 0.4470 0.7410]; c = [b; b; r; r; r; b; r; r; b; b; b; r; b; r; b];
```

Above, the regression can be thought of as finding some w's such that:

$$ X2 = w_1*X1 + w_0 $$

From here, one can use a closed form solution which follows:

$$ w^* = (X^TX)^{-1}X^Ty $$

In matlab, this equation can be implemented as follows:

```matlab
d = [X(:,1),ones(15,1)];  % add a ones column for offset
w = inv(d'*d)*d'*X(:,2);
hold on
scatter(X(:,1),X(:,2),[],c,'filled')
plot(X(:,1),w'*d')
hold off
```
![scattfit](/assets/scat_wfit.svg)

## Classification
In order to change the above regression problem into a classification problem, we can simply use the columns X1 and X2 to regress out a third column (Category). After this, we can simply set a threshold (naivly, maybe 1.6) to classify!
We might also want to look at the decision boundary, and this can be done by using the solved weights. The code to do this in matlab is:

```matlab
g = [1,1,2,2,2,1,2,2,1,1,1,2,1,2,1];
d2 = [X, ones(15,1)];
w2 = inv(d2'*d2)*d2'*g';
g_hat = w2'*d2';
colors = zeros(15,3);
for i=1:15 
    if g_hat(i)<1.6 
        colors(i,:)=b; 
    else
        colors(i,:)=r;
    end 
end 
hold on
scatter(X(:,1),X(:,2),[],colors,'filled')
fimplicit(@(x,y) w2(1)*x + w2(2)*y +w2(3)-1.6)
hold off
```
![scatt](/assets/scat2.svg)

## Conclusion
In short, as you expect, for linearly seperable data, we can model linear regression and linear classification as similar processes

