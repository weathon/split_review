# Estimating Shape Distances on Neural Representations with Limited Samples

- Decision: Accept
- Scores: 6, 6, 1, 8

## Abstract
Measuring geometric similarity between high-dimensional network representations is a topic of longstanding interest to neuroscience and deep learning.
Although many methods have been proposed, only a few works have rigorously analyzed their statistical efficiency or quantified estimator uncertainty in data-limited regimes.
Here, we derive upper and lower bounds on the worst-case convergence of standard estimators of \textit{shape distance}---a measure of representational dissimilarity proposed by \citet{Williams2021_shape_metrics}.
These bounds reveal the challenging nature of the problem in high-dimensional feature spaces.
To overcome these challenges, we introduce a new method-of-moments estimator with a tunable bias-variance tradeoff.
We show that this estimator achieves substantially lower bias than standard estimators in simulation and on neural data, particularly in high-dimensional settings.
Thus, we lay the foundation for a rigorous statistical theory for high-dimensional shape analysis, and we contribute a new estimation method that is well-suited to practical scientific settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel estimator for distances between neural representations from both biological and artificial neural networks. The key technical contribution is a new moment based estimator of the nuclear norm of the cross covariance matrix which has significantly lower bias than the plug in estimator. The authors provide both theoretical and empirical analysis to illustrate the benefits of the proposed estimator.

### Strengths
1. The problem is clearly identified and analysed theoretically, and the estimator proposed to solve it is principled and technically sound. The theoretical analysis in Section 3 is fairly detailed and appears to be novel. It clearly explains the flaws in the plugin estimator and the subsequent derivation of the new estimator is also well grounded in theory.

2. Simulations and experiments match the intuition used to derive the estimator (Fig 2A) and clearly highlight the strengths of the estimator over the plug-in baseline.

### Weaknesses
1. The overall motivation of the problem is a bit weak. The experiments don't clearly illustrate the downstream benefits of this work. Further experiments showing tangible gains on at least one real world application would greatly strengthen the paper in my opinion.

2. The main technical weakness of the approach appears to be its effect on the variance. While deriving the estimator the authors seem to primarily focus on reducing the bias compared to the plug-in estimator and acknowledge at the end of Section 3.3 that the bias is being bounded at the expense of the variance. This is also seen in the experiments (Fig 2) where the proposed estimator appears to have a significantly higher variance than the moment estimator. This raises questions about the reliability of the estimator, specifically it is not clear if it can reduce the mean squared error for all distributions. This is further illustrated in Fig 4 where on real neural data it appears that other than the case where similarity is set to 0 (A) the plug-in estimator performs comparable to (C, D) or better than (B) the proposed estimator.

### Questions
1. In the last equation on page 5, why is $x \in [0,1]$?

2. In Section 4.2 it is acknowledged that the proposed estimator is highly variable in low SNR regimes and so neurons with the highest SNR are selected. Can you provide the relative proportion of such neurons in the presented scenario and also (if possible) comment on their prevalence in general? This is important because if the relative proportion is small then it means that the proposed estimator can only be applied in very few cases.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors study the estimators of the so-called "shape distance", more precisely Procrustes size-and-shape distance $\rho$, and Riemannian shape distance $\theta$., that are distances defined on data manifold. They measure the uncertainty (bias and variance) of the empirical estimates of these distances, relying on centration inequalities, and design a new estimator whose bias/variaqnce tradeoff can be controlled. Their theoretical results are illustrated on:
* a synthetic experiment
* measure of calcium in the neural activity of a mouse

### Strengths
### Clarity

The paper is well written, and the and theoretical results are explained in a way that make it accessible to a broad range of readers. The proof techniques are well explained. 

### Quality

Experiments are convincing and support

### Weaknesses
### Out of scope: no link with neural networks

This work has nothing to do with artificial neural networks. In the statement of the problem, the authors assume that thew observations are $X=h_i(Z)$ with $Z$ the input data  and $h_i$ the neural network. No hypothesis is made on $h_i$ nor $Z$. The whole paper could be rewritten with $X$ to get rid of the assumption that the measures are the outputs of a neural network. Even Theorem 2 mentions "neural" for no good reason: authors only meant to talk about the existence of some r.v $X$.  

The only experiment linked with neural network is in Sec 4.2, and the "neural data" is actually *calcium measurements* from mouse primary visual cortex, which are typical tabular data.  

Overall, a conference or journal focused on statistics seems to be a better match for the content of the article than ICLR.  

### Novelty

The novelty is poor: all the proofs are classical bias-variance decomposition and concentration inequalities. 

Moreover, there exists previous work on the topic that are not covered in the literature review:   
   
Kent, J.T. and Mardia, K.V., 1997. Consistency of Procrustes estimators. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 59(1), pp.281-290.
  
Goodall, C., 1991. Procrustes methods in the statistical analysis of shape. Journal of the Royal Statistical Society: Series B (Methodological), 53(2), pp.285-321.

### Questions
### Application to artificial neural networks

Which results your method yield in the latent space of an *artificial* neural network?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper theoretically quantifies the performance of some typical shape distances between neural representations and the dependence of the performance with respect to the number of samples. The authors find that typical methods have low variance but high variance, and instead propose a new method that enables a tunable bias-variance tradeoff.

### Strengths
- The paper contains significant insight into the performance of 'plug-in' estimators of shape distance between two neural representations and the performance dependence on the number of samples and the dimensionality of the ambient space.
- The paper identifies the key component behind the non-ideal performance of these estimators (the $||\Sigma_{ij}||_\ast$ term) and proposes a simple but intuitive and effective estimator to allow a tunable bias-variance tradeoff.
- There are adequate experiments on synthetic data to validate this new estimator.

### Weaknesses
 - The paper should contain some more intuition-building sentences so that the mathematical formulation is more easily digestible. However, the authors have done a really nice job of making the mathematical foundations and derivations themselves clear.
- One small experiment with VAEs (even if it is confined to the appendix) might be useful for quantifying the performance of stochastic networks.

### Questions
NA

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends some works from shape analysis into the space of neural networks. That is, how does one measure the distance between two NNs where a NN is represented as a mapping h:features ->R^N. The main idea is to think of this mapping into the space of point clouds and hence one can use a Kendall Shape space type distance. The key difference contribution I see is the fact the point clouds have some stochastic properties to them so the shape distance is measuring the distance between expectations. The authors spend a great deal with considering the bounds of these distances.

### Strengths
A key component of this paper is the bounds on the distances when using an estimator for the cross covariance estimator. The authors present Lemma 1, 2 and Theorem 1 to do this (and theorem 2). The authors explain this bound well as it makes sense that the higher the dimension, the more landmarks need to be observed. 

The authors show how under a variety of scenarios their estimator is performing. The variety is suitable.

### Weaknesses
When referencing the shape distances such as (2) and (3) the authors cite Williams 2021 but these are simply common shape distances which have been around for much longer. Unless this specific formulation is novel to Williams 2021 I don't see how it's different than just measuring the distance on a circle.

When considering the "failure modes of plug-in..." there is the missing component of mentioning scale. If h_i differ in scale their $\rho$ distance can be large but their $\theta$ distance can be very small as it rescales in the denominator.

Some of the figure axis are impossible to read.

### Questions
When setting up the background, the authors define $h_i:\mathcal{Z}\rightarrow \mathbb{R}^n$ as a function representing each neuron. I have no problem with this definition. My question is, why do the authors limit their writing to that of NNs while this is true for a much wider class of functions. I may have missed something in an assumption but it seems these functions can be quite generally considered.

For (5) isn't the last equation enough?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
