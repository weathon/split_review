# Long-time asymptotics of noisy SVGD outside the population limit

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Stein Variational Gradient Descent (SVGD) is a widely used sampling algorithm that has been successfully applied in several areas of Machine Learning. SVGD operates by iteratively moving a set of $n$ interacting particles (which represent the samples) to approximate the target distribution. Despite recent studies on the complexity of SVGD and its variants, their long-time asymptotic behavior (i.e., after numerous iterations $k$) is still not understood in the finite number of particles regime. We study the long-time asymptotic behavior of a noisy variant of SVGD. First, we establish that the limit set of noisy SVGD for large $k$ is well-defined. We then characterize this limit set, showing that it approaches the target distribution as $n$ increases. In particular, noisy SVGD provably avoids the variance collapse observed for SVGD. Our approach involves demonstrating that the trajectories of noisy SVGD closely resemble those described by a McKean-Vlasov process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies the convergence of a noisy version of SVGD.
The noisy version of SVGD in this paper is defined as a mixture of SVGD and Langevin dynamics.
Specifically, a small Langevin dynamics update is added to each SVGD update.
The authors prove the convergence of this noisy SVGD.
In particular, they demonstrate that the empirical distribution of the particles converges to the target distribution in probability, under the condition that the number of iterations goes to infinity, followed by the number of particles going to infinity.
Empirical evaluations demonstrate that the noisy SVGD avoids variance collapse, unlike vanilla SVGD.

### Strengths
The theoretical understanding of SVGD has been lacking over the years.
In particular, most existing convergence analyses are based on population limits.
Instead, this paper attempts to study the asymptotic convergence behavior of finite particles, specifically by letting the number of iterations go to infinity and then letting the number of particles go to infinity.
A step in this direction helps deepen the understanding of SVGD.

### Weaknesses
1. The main weakness is that the noisy version of SVGD deviates a lot from the SVGD used in practice. The addition of Langevin dynamics, even with a small coefficient, fundamentally alters the optimization landscape. This makes it unclear how much the convergence analysis of this noisy version actually informs our understanding of vanilla SVGD. The practical implications are limited, as practitioners would likely not use this specific noisy variant.

2. The coefficient of the Langevin dynamics controls how similar the noisy SVGD is to vanilla SVGD and Langevin dynamics. Large coefficients effectively reduce the algorithm to Langevin dynamics, while small coefficients might only provide marginal benefits over vanilla SVGD. The paper does not provide a clear guideline on how to choose this coefficient, nor does it explore the trade-offs between the two extremes. It remains unclear if there is a moderate coefficient that provides a significant advantage over both vanilla SVGD and Langevin dynamics, and if so, how to find it.

### Questions
1. Is it possible to prove noisy SVGD with other types of noise?
What would be the technical challenges there?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper shows that noisy SVGD can properly sample a target distribution.

### Strengths
The paper shows that noisy SVGD can properly sample a target distribution.

### Weaknesses
The results are not all that surprising, and I'm surprised earlier papers haven't proved this before. The background section may not have been thorough enough. The lack of surprising results stems from the fact that adding noise to an optimization procedure is a common technique to avoid local minima, and it is not clear why this particular approach should be theoretically challenging. The paper does not sufficiently discuss the existing literature on noisy gradient descent methods, which could have provided a better context for the novelty of the results. The background section should have discussed the challenges of analyzing particle methods with noise, and how this work addresses those challenges.

### Questions
Why didn't earlier papers prove such results before?

If indeed the results are novel, what's the main barrier for theoretical analysis that was overcome?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the long-time behavior of noisy SVGD, by first taking the limit to infinity in the number of steps, and then taking the limit to infinity in the number of particles. Noisy SVGD is a variant of the SVGD algorithm where a Langevin update is added to the SVGD update. Using propagation of chaos arguments, the authors are able to show that the distributional limit set of NSVGD at a finite number of particles $n$ converges in probability to the target distribution $\pi(x) \propto \exp(-F(x))$ as $n$ goes to infinity. Since the limit in which the number of particles goes to infinity first and the number of steps goes second can be understood by the arguments from previous works, that implies that the order of the limits can be exchanged.

Experimentally, the authors show that for two different kernels, different number of particles, and increasing dimension $d$, the dimension-averaged marginal variance is much lower than it should for SVGD, while NSVGD performs correctly.

### Strengths
- The paper resolves a well-known issue of SVGD (variance collapse) by coming up with a modification that provably and empirically does not show variance collapse. The results of the paper are solid both in theory and practice.
- The theory of the paper relies heavily on results on McKean-Vlasov equations, which are not part of the standard toolkit for machine learning researchers. This paper can serve as a guide to finite-particle convergence results for other particle algorithms.

### Weaknesses
 - The paper would be really complete if the authors gave some guidance on how to appropriately set the Langevin regularization parameter, at least in the settings that they have studied. That would be useful for practitioners looking to replace SVGD or the Langevin algorithm by NSVGD.

 - Figure 1 is illustrative of the fact that NSVGD does not suffer from variance collapse, while regular SVGD does. In that sense, it is a correct validation of the theory presented in the paper. However, it would also be interesting to compare empirically NSVGD to Langevin dynamics. That is, is the SVGD term in NSVGD actually useful, or is the reason for the success of NSVGD simply the Langevin term? Should practitioners use NSVGD or just Langevin? In my view, resolving this issue is critical for NSVGD to be considered a useful algorithm.

 - While introducing the Langevin terms is useful to fix variance collapse, do the authors know if NSVGD is uniformly better than SVGD? For example, oftentimes SDEs may require a larger number of steps than ODEs to obtain numerical errors below a certain threshold. Can the authors comment on that?

 - Typos: In line 246, SGVD -> NSVGD. In line 517, usefull -> useful.

### Questions
- Figure 1 is illustrative of the fact that NSVGD does not suffer from variance collapse, while regular SVGD does. In that sense, it is a correct validation of the theory presented in the paper. However, it would also be interesting to compare empirically NSVGD to Langevin dynamics. That is, is the SVGD term in NSVGD actually useful, or is the reason for the success of NSVGD simply the Langevin term? Should practitioners use NSVGD or just Langevin? In my view, resolving this issue is critical for NSVGD to be considered a useful algorithm. I’ll be happy to raise my score if this is addressed.
- While introducing the Langevin terms is useful to fix variance collapse, do the authors know if NSVGD is uniformly better than SVGD? For example, oftentimes SDEs may require a larger number of steps than ODEs to obtain numerical errors below a certain threshold. Can the authors comment on that?
- Typos: In line 246, SGVD -> NSVGD. In line 517, usefull -> useful.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper poses a question on Stein variational gradient descent:
>What does SVGD converge to (i.e., as k → ∞) in the finite particles regime (i.e., when n < ∞ is
fixed)?

The paper then introduces a noisy version of SVGD (NSVGD), where each particle simultaneously undergoes Langevin regularization with regularization strength $\lambda \geq 0$.  In the case of $\lambda =0$, this recovers SVGD

The paper then proves convergence of the NSVGD under a vanishing stepsize setup ($\sum \gamma_k = \infty$ and $\gamma_k \downarrow 0$).  Under sufficient regularity on the kernel K (Assumption 3), this holds for the averaged iterate (Theorem 3), and under an additional log-soblev inequality assumption on the target measure $\pi$, this holds for the final iterate.

The paper is principally concerned with proof, and an overview of the proof is given in Section 5 of the main-text.  This builds on existing work around McKean-Vlasov SDEs and optimal transport theory.

Finally, in Section 6, the article provides numerical simulations illustrating that NSVGD avoids 'particle collapse', where the particles in SVGD can 'freeze' in high-dimensions.  This is measured by computing the average variance of the coordinates sampled from a high-dimensional distribution.  When dimension $d$ is large with respect to the number of particles,  (indeed from figures, this would appear to be in a proportionate $d \propto n$ regime), a non-degenerate gap appears between this variance and the ground truth, whereas numerical simulations suggest that for NSVGD this does not occur.

### Strengths
The paper's primary contributions are its main Theorems 2,3.  These are very clearly presented with a good level of mathematical detail.

The paper introduces an algorithm, with improved convergence characteristics with respect to SVGD.  It appears to be a natural extension of SVGD, with essentially identical complexity to SVGD and improved characteristics.

### Weaknesses
There are a few overall weaknesses.

1) The paper poses a question on SVGD, but then in fact does not answer this question (What does SVGD, $\lambda= 0$, converge to?), nor does the bulk of the paper seem particularly interested in answering it.  On the contrary, it would seem that SVGD has some obvious (empirically demonstrated) problems with convergence (especially the variance collapse), and you have found a better algorithm.  I think this is mostly a weakness of presentation, and it could be resolved by describing better what will appear in the paper (i.e. mostly not posing this question in italics).  Or alternatively, it should be addressed, somehow?

2) The variance collapse effect in Section 6 leaves open a deeper theoretical evaluation of SVGD, in particular proving a theorem which demonstrates this variance collapse effect for SVGD.  Furthermore, it is not clear if either the NSVGD theory proven would be enough to demonstrate this non-collapse (though in the Gaussian kernel case perhaps it is close?)

3) Since this is a new algorithm, it would be nice to see another panel of performance evaluations, comparing NSVGD to SVGD and Langevin sampling for a standard class of metrics, to get some sense to what extent there is a tradeoff in using something like NSVGD.  For example, to the extent that lambda > 0 acts like a regularizer, one may expect that too much regularization causes performance losses (on the other hand, given that it comes with the Langevin generator, perhaps this never occurs?)

### Questions
Questions related to the weaknesses:

Addressing Weakness 2:  Do the theorems allow any uniformity in the dimension d of the underlying problem, say in the case of a log-sobolev constants? 

Addressing Weakness 3:  Can you provide further experiments, evaluating performance of NSVGD vs SVGD and Langevin sampling?  Is there any setup, in particular where lambda=0 is favorable?

Other questions:
1) On l72 you say:  
> Indeed, SVGD does not converge to the target distribution when $n<\infty$. This is because the iterates of SVGD are discrete measures with a finite support of $n$ points, whereas the target $\pi$ has a continuous density with respect to the Lebesgue measure. 

But the _law_ of those $n$ points may very well have a density, and moreover the law of a randomly selected point could be close to $\pi$.  Why is the discreteness of this measure a problem? (You also mention this on l84). Furthermore, even if this were a problem, shouldn't one just change the metric?  
2)  On l.358:
>Moreover, in the population limit where $n$ is large, any of the continuous-time particles coincides, in law, with the solution to a McKean-Vlasov equation, as defined below. This phenomenon is known as the propagation of chaos. We refer to Chaintron \& Diez (2022) for a detailed exposition.

Why should _all_ particles need converge, instead of the evolution of a _tagged_ particle converges? (For example the right-most particle in a 1-dimensional setup need not converge)

3) l.386.  There is some double limit notation not properly introduced.

4) l.517.  ``usefull''

### Soundness
2

### Presentation
3

### Contribution
2
