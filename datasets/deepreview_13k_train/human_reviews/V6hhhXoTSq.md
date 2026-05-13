# A Likelihood Based Approach to Distribution Regression Using Conditional Deep Generative Models

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
In this work, we explore the theoretical properties of conditional deep generative models under the statistical framework of distribution regression where the response variable lies in a high-dimensional ambient space but concentrates around a potentially lower-dimensional manifold. More specifically, we study the large-sample properties of a likelihood-based approach for estimating these models. Our results lead to the convergence rate of a sieve maximum likelihood estimator (MLE) for estimating the conditional distribution (and its devolved counterpart) of the response given predictors in the Hellinger (Wasserstein) metric. %Particularly, 
Our rates depend solely on the intrinsic dimension and smoothness of the true conditional distribution. These findings provide an explanation of why conditional deep generative models can circumvent the curse of dimensionality from the perspective of statistical foundations and demonstrate that they can learn a broader class of nearly singular conditional distributions. Our analysis also emphasizes the importance of introducing a small noise perturbation to the data when they are supported sufficiently close to a manifold. Finally, in our numerical studies, we demonstrate the effective implementation of the proposed approach using both synthetic and real-world datasets, which also provide complementary validation to our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
A statistical analysis of conditional deep generative models using a likelihood approach (specifically a sieve MLE) is proposed and analyzed. A convergence rate for the estimator is established using neural network approximation theory for the (conditional) generator. Numerical examples are provided showing the efficacy of the method.

### Strengths
1. Very well written paper
2. Method is clearly explained and proof are followable

### Weaknesses
1. The method seems to be extending the techniques of previous work and filling in some details with approximation.
2. Question on the applicability to multiple chart manifolds.
3. Numerical examples are very simple.

### Questions
1. In regards to the discussion in 2.4.3 and Appendix C with the multiple manifold case: If a partition of unity is used to define local transport maps, we require that the local distributions on each chart need to have density lower bounded. However, a partition of unity will have its weights vanish to 0 on the boundary, so the induced local distribution would have density that vanishes to 0 on the boundary. How can you apply optimal transport regularity theory in that case, when your target has density that is not lower bounded?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies using neural network generative models for distribution regression. Statistical rates are established, and a significant effort is devoted to resolving the curse of dimensionality issue. Numerical results are provided to support the theory.

### Strengths
The theoretical results appear to be correct and sound. Moreover, there are detailed analyses for different setups and matching lower bound.

There are numerical results to support the performance of neural network generative models for distribution regression.

### Weaknesses
The paper is not very easy to follow in places, mostly due to the technical presentations and pure statistical discussions. I would suggest authors to prepare a preliminary section before mixing background introduction with main results in current Section 2.

It is relatively difficult for me to judge the technical novelty of the paper. On the one hand, the distribution regression problem and low-dimensional generative neural networks seem to pose technical difficulties. On the other hand, the results as well as most of the assumptions are replication of many existing works, such as Schmidt-Hieber, 2020 and Tang and Yang, 2023.

Practical impact of this work may be limited, due to many technical assumptions.

Numerical results loosely connect to the theoretical results.

The paper is not prepared in the standard ICLR style --- the left and right margins are altered significantly. Under the standard style template, this submission will go beyond the page limit.

### Questions
Do numerical results support the rates proved in theory? Maybe we can take logarithm on the sample size and inspect the slope of the error.

Assumption 3 excludes interior points. Does this assumption hold (approximately) in practical applications?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors describe a method for estimating high dimensional conditional distributions that concentrate around a manifold. Such distributions appear in common settings such as conditional generative modeling. The authors consider the convergence of an estimator that improves based on the number of data points to the true distribution in the Hellinger distance sense. The authors then consider applying this estimator to some synthetic and real datasets to understand its empirical performance. The analysis considers two types of neural networks: a sparse neural network and fully connected one that parameterize the push forward of the latent variable to the conditional outcome. The analysis is heavily dependent on empirical process theory to establish different properties of the architectures.

### Strengths
The proposed analysis is helpful in understanding why generative models work as they do. Additionally the proposed error analysis is useful for anticipating the number of data points needed to achieve a specific targeted error with respect to the Wasserstein or Hellinger distances. 

The empirical results support the main claims of the work to some extent.

### Weaknesses
Some of the theoretical results seem hard to verify in practice. It would be interesting for some contrived examples if the authors can show the convergence of the distances as a function of the number of points. Specifically, while the authors provide asymptotic rates, it is unclear how these rates manifest in practical scenarios with finite datasets. The lack of concrete examples demonstrating the convergence behavior makes it difficult to assess the practical relevance of the theoretical findings. Furthermore, the theorems contain some constants that do not have a clear way of being estimated making some of the errors hard to use in practice. These constants, which depend on various model parameters and domain characteristics, are crucial for quantifying the error bounds. The absence of a clear methodology for estimating or approximating these constants limits the applicability of the theoretical results in real-world settings. It is unclear how sensitive the error bounds are to perturbations of these constants and how these constants scale with the dimensionality of the problem. Note that the paper does not appear to be in the right ICLR format since the margins are considerably smaller.

### Questions
How easy are some of the conditions to verify for the convergence theorems to hold?

How do you interpret the constants in the various theoretical statements? For example, some are dependent on the domain or other parameters, in what sense do they grow for perturbations of their dependencies? Can these be estimated in practice?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims at providing statistical bounds for conditional generative models under various smoothness assumptions. The overall goal is to model conditional distributions $Y|X$ via conditional generative models, i.e., $y = G(x)_{*}P_Z$ of some latent distribution $P_Z$. First empirical convergence rates of so-called sieve MLE estimators are provided (Theorem 1), showing that as paired data tends to infinity the approximation of the measure tends to zero in probability.  Then also the Wasserstein distance between the pushforward distribution of the MLE estimate and the true generated distribution can be controlled via a pertubation strategy that depends on the data dimension and smoothness. Then with some ansatz function class spaces for the true generating process, a convergence theorem for sieve MLE with generating functions in some sparse NN class is presented. 

Finally, the sieve MLE is validated on some toy examples which is learned via a VAE and on the MNIST dataset.

### Strengths
The paper tackles a very interesting topic. There has not been much theory of conditional generative models, in particular not on their statistical rates with respect to the true smoothness and intrinsic dimension. 

Theorem 1 presents a very nice approach on how to tackle these problems, which allows for splitting these problems up into the covering number and the accuracy of the approximation. This gives a nice guideline: Pick a function class that has a good covering scaling and good approximation capabilities. In particular the noise injection strategy seems very neat in corollary 2, if the data distribution is close to a singular one. Generally, the writing and the maths is very rigoruous, with clearly defined objects up to a few exceptions (see weaknesses). It is also nice that the qualitiative behaviour of the theorems is verified in understandable toy examples.

### Weaknesses
First, let me say, that I come from a background in conditional generative models, not so much in statistical theory. Therefore I had difficulties following some claims in the paper. 

1) First, when I think of where conditional generative models are actually used, I am confused about the whole modelling assumption in section 2.1. Usually the latent space Z should take care of the uncertainty in Y, so that T(x,Z) models this perfectly. of course for trained models there will still be a mismatch, but treating this as an independent Gaussian seems very unrealistic. Can you elaborate this assumption maybe taking the example of inverse problems?

Can you maybe find for lets say a normalizing flow always a similar regular normalizing flow with a small gaussian noise added to it such that it becomes the "real" generative model? This would increase my confidence in this assumption.

2) It would be good to have a running example, something super simple like taking the pushforward of a Gaussian under a linear operator (with non trivial rank) to explain the rates and corollaries. 

3) I am worried about the scaling in corollary 1 for the $\sigma^{*}$, basically this means that if the noise level tends to zero, that the approximation accuracy has to increase by a lot. This might be due to the choice of the Hellinger distance. Why not try to control the Wasserstein distance in equation 7 in the first space? Since $W_1(p, p \star \mathcal{N}(0,\sigma))$ are close for small $\sigma$ this might alleviate this problem.

4) I feel like section 2.4 is not rigorous in the sense that it is very unclear if the article looks at joint measures of $(X,Y)$ or conditional measures $Y|X=x$. Looking at the proofs I think it holds for the condiitonals and arbitrary $X=x$? ´

5) For the experiments part, it would be very enlightening to consider manifolds with a known dimension (and maybe make them conditional) to validate how the intrinsic dimension comes into play [1]. Further, for the MNIST example, one does not need to take the MNIST dataset as the ground truth, but rather one can take a pretrained generator as the ground truth and then validate how smoothness and approximation error impact the Wasserstein/FID/... between the pretrained generator and a learned model. This would be much more in spirit with validating the bounds, since the point of this paper is not to come up with a practical algorithm I presume. 

6) Can the in probability bounds be strengethened to expectation bounds over x between the conditional measures under stronger assumptions, see also [4].Conditional Wasserstein Distances with Applications in Bayesian OT Flow Matching

7) Also, one algorithm where the composition approach might come into play is flow matching/diffusion with odes [2]. Here, if one takes a simple Euler scheme to sample one indeed has such a simple compositional structure. I would find it very interesting to briefly state the relation to those, as they are bit more SOTA and practical interest than VAEs at the moment. 

8) Can you make a practical example where the smoothness disparity is obvious?

9) This paper is missing some citations on generative models and manifolds [1,3], and the relation between conditional measures and joint measures [4] and also in what sense conditional generative models optimize the MLE estimator (somewhat clear for NFs and VAEs, less clear for diffusion/...). Here I am thinking along the lines of [5]

### Questions
see the weaknesses, they are a bit intertwined.

POST REBUTTAL: Concerns have been mostly addressed. raising score from 6 to 8.

### Soundness
3

### Presentation
2

### Contribution
3
