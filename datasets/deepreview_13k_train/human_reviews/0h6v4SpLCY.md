# Universal generalization guarantees for Wasserstein distributionally robust models

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Distributionally robust optimization has emerged as an attractive way to train robust machine learning models, capturing data uncertainty and distribution shifts. Recent statistical analyses have proved that generalization guarantees of robust models based on the Wasserstein distance have generalization guarantees that do not suffer from the curse of dimensionality. However, these results are either approximate, obtained in specific cases, or based on assumptions difficult to verify in practice. In contrast, we establish exact generalization guarantees that cover a wide range of cases, with arbitrary transport costs and parametric loss functions, including deep learning objectives with nonsmooth activations. We complete our analysis with an excess bound on the robust objective and an extension to Wasserstein robust models with entropic regularizations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents novel bounds on for the DRO loss using the Wasserstein distance. In particular, they address the question of finding the minimal $\rho$ used by the empirical robust loss such that the loss is an upper bound for the actual population loss. The main challenge is to overcome the dependency on the distance between W(P_n, P) \sim n^{1/d}. While this problem has been studied in the literature, and dimension free bounds exist, this paper presents a proof requiring weaker assumptions.




---------- after the rebuttal ------------

I thank the authors for their response and increased the score accordingly.

### Strengths
The paper addresses an important problem is generalization bounds/theoretic ML. In particular:

- The paper is well written and the results are nicely presented. 
- The proof sketch in Section 4 is excellent. It is very easy to follow and often neglected in these types of papers
- The proof idea is smart, non-trivial and interesting.

### Weaknesses
Given that this is a more traditional field, I would expect a clearer comparison with the existing works. While the authors do a very good job in presenting the proof idea, it is not so clear how the proof fundamentally differs from existing works. Specifically, the paper would benefit from a more detailed explanation of how the assumptions and proof techniques differ from those in related works, such as Azizian et al. (2023a). It is not immediately obvious what specific limitations of existing proofs are overcome by the proposed approach. The current discussion lacks a concrete example of a distribution class that is covered by this paper but not by existing methods. Furthermore, the technical novelty of the proof needs to be highlighted more explicitly. It would be beneficial to provide a more detailed explanation of why the existing proof techniques cannot be directly applied under the assumptions of this paper, and what specific challenges are addressed by the proposed approach. The current presentation does not fully clarify the specific technical hurdles that are overcome by the new proof strategy. 

Isn't assumption 3.1 (1) always true satisfied by w<=1. Is it possible that this is a typo?

### Questions
I am happy to increase my score and support this paper with a high confidence if the authors can provide an extensive discussion during the rebuttal on the assumptions in Azizian et al. (2023a) . In particular, my two major questions are: can the authors be more precise in which cases their assumptions are weaker than the ones in  Azizian et al. (2023a). In particular, can you give an example for a class of distributions that are covered by this paper but not by  Azizian et al. (2023a)? Moreover, can the authors explain why the proof in  Azizian et al. (2023a) breaks for your assumptions and why it is not trivial to extend the proof?



Smaller question:
Isn't assumption 3.1 (1) always true satisfied by w<=1. Is it possible that this is a typo?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides exact generalization guarantees for Wasserstein Distributionally Robust Optimization (WDRO) for a wide variety of models with compactness and finite Dudley's entropy assumptions. The results apply to radius $\rho$ scaling as $O(1/\sqrt{n})$, which does not suffer from the curse of dimensionality. The results also cover the double regularization case.

### Strengths
- The generalization guarantees of this work do not rely on restrictive assumptions like smoothness compared to the previous work (Azizian et al. 2023a). 
- This paper is well-structured, and the theoretical results and proof sketches are clearly presented.

### Weaknesses
 - In Section 3.2, the authors discussed how their results on generalization guarantees apply to linear regression and logistic regression. However, more complicated models such as neural networks with ReLU or other smooth activation functions (e.g. GELU) are not discussed. 
- The theoretical results require a lower bound on $n$, while Theorem 3.4 of Azizian et al. (2023a) applies to all $n \ge 1$. The implications of this requirement should be discussed.

### Questions
- What are the practical implications of the generalization guarantees compared to Azizian et al. (2023a)? Can you provide some numerical results analogous to Appendix H of Azizian et al. (2023a)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The proposed paper provides lower bounds on the robust empirical risk under unorthodox but interesting scaling limits on the radius of the Wasserstein ball around the empirical risk.  The paper uses some cool techniques which are not often seen in machine learning.  

The paper is relatively clearly written.  However, I think there are a few little things here and there which are either difficult to justify (in the current form) or perhaps not well-defined (see below). Also, the introduction is excessively general while the setting rapidly collapses to a much more specific setting shortly after.

### Strengths
The paper is well written, interesting, and theoretical and provides very nice lower bounds on the robust empirical risk.  The results are nice, and so is the use of set-valued analysis to derive them.  Several relevant examples are considered, making a large portion of how these results can be used nearly transparent.

### Weaknesses
Nevertheless,  I think some of the assumptions are a bit opaque (see below), and I'm not certain some quantities are well-defined.

*Minor*
- Citing Cuturi and Perée's book is odd when mentioning the Wasserstein distance.  Perhaps the original source or a book on optimal transport such as Villani's book, would be more natural, IMO.

- The definition of Wasserstein distance circa (1) is incorrect, $\Xi$ must be Polish, and  c *must* be a power $p\in [1,\infty)$ of a *metric* topologizing $\Xi$; what you write is just some transport problem.  Eg if c is not symmetric, then $W_c$ is not a metric in general, or if $c(x,y)=0$ for all $x,y$ then $W_c$ cannot separate points.

- Perhaps "suitable" distributions is more appropriate before (1), since the distance explodes if these have no finite moment. 

- Line 65: bad grammar: "it does not introduce approximate term" also imprecise.

- Line 66: Is Wainright's book and Boucheron the best reference?  Perhaps older papers, e.g. on VC dimension, Bartlett's old papers on Rademacher complexity, or old papers on chaining are more natural references?

- Line 69: "This theoretical feature is specific to WDRO and highlights its potential to give more resilient models." This can be **much** less hand-wavy.  Please explain more precisely/mathematically.

- Line 149: In a metric space $(x,..)$ not "In (X,..) a metric space".

- Assumption 1 vs. Line 145: You say that $\Xi$ is just a measurable space, then later you say its a compact metric space.  Why no   be forthright and say its a metric space on line 145.  Similarly, why is $\mathcal{F}$ an arbitrary family of functions, then straightaway after is actually a compact set of continuous functions.

- Line 176: Why jointly Lipschitz?  If $\Theta$ is compact, then since you already assumed $\Xi$ is compact, then it is enough for $\Theta\times\Xi\ni (\theta,\xi)\mapsto f(\theta,\xi)\in \mathbb{R}$ to be continuous; to deduce the compactness of $\{f(\theta,\cdot):\,\theta \in \Theta\}$ by the currying Lemma.  

- Line 176: Not sure why you say "if $\Xi$ is compact, since this was assumed a few lines earlier on the same page.

- Maybe more natural examples come from Arzela-Ascoli...

- Should the definition of the Dudley entropy integral really be in a footnote, while more basic ideas are in the main text.

- Line 221: The words "the metric" are missing.

- Line 223: There are many more references of the use of this type of metric, especially in exponential convergence rate results for Markov chains (wrt $W_1$ over countable metric spaces with this distance).

- Line 245: "sample randomness" (I know what you mean...but the word independent is misleading as this 

- Assumption 1: Why call (2) jointly continuous, it is just standard continuity (actually inform continuity by compactness).

### Questions
- Why not submit to JMLR?  The paper is very rigorous and rather long and technical for an ML conference?  You also examine the problem in good detail.

- Could you provide a simple example in Theorem 3.2, where the optimal coupling is known under (say) Gaussianity assumptions?

- I'm a bit confused.  What does $\operatorname{argmax}_{\Xi}\,f$ mean in (5) a sup norm or something?  

- Why is $\min\{ c(\xi,\zeta): ... \}$ measurable?  In particular, (independent of the meaning of the argmax, above question), why is there a measurable selection $\xi\mapsto \zeta$?  Without this, its not clear that $\rho_{\operatorname{crit}}$ is well defined.  I'm guessing this is Berge's theorem (which is in Aliprantis & Border) somehow, but please spell it out for us :)

- Each result assumes that the (difficult to interpret) $\rho_{\operatorname{crit}}$ is "large enough".  Can you please provide a general set of conditions ensuring that $\rho_{\operatorname{crit}}$ can be bounded away from $0$. 

- Is it fair to compare, verbally, our results to those of Fournier et al. (and similar bounds, say, found in [1])?  Since you are considering a small ball around the empirical measure while their results guarantee a minimal radius such that the empirical measure contains the true measure whp.   Furthermore, those rates are only tight (afaik) when the measure is very spread out; more precisely, it is Alhors $d$-regular, see e.g. [3] for a nice clean proof.  

- In theorem 3.2, why is $\pi^{P,Q}\ll \pi_0$?  To be this isn't directly evident... I.e.\ why is the RHS not trivially $-\infty$ in general?



[1] Graf, Siegfried, and Harald Luschgy. Foundations of quantization for probability distributions. Springer Science & Business Media, 2000.
[2] Otto, Felix, and Cédric Villani. "Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality." Journal of Functional Analysis 173.2 (2000): 361-400.
[3] Kloeckner, Benoit. "Approximation by finitely supported measures." ESAIM: Control, Optimisation and Calculus of Variations 18.2 (2012): 343-359.

### Soundness
3

### Presentation
4

### Contribution
3
