# Generalization of noisy SGD under isoperimetry

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
We study the generalization of iterative noisy gradient schemes on smooth non-convex losses. Formally, we establish time-independent information theoretic generalization bounds for Stochastic Gradient Langevin Dynamics (SGLD) that do not diverge as the iteration count increases. Our bounds are obtained through a stability argument: we analyze the distance between SGLD iterates on two datasets sampled from the same distribution. Our result only requires an isoperimetric inequality to hold, which is merely a restriction on the tails of the loss. We thus relax the assumptions of prior work to establish that the iterates stay within a bounded KL divergence from each other. Under an additional dissipativity assumption, we show that the stronger Renyi divergence also stays bounded by establishing a uniform log-Sobolev constant of the iterates. Without dissipativity, we side step the need for local log-Sobolev inequalities and instead exploit the regularizing properties of Gaussian convolution. These techniques allow us to show that strong convexity is not necessary for finite stability bounds and thus for finite generalization and differential privacy bounds.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the stability of SGLD, which implies generalization and differential privacy guarantees of SGLD. Instead of assuming strong convexity of the loss function, the authors demonstrate that stability results still hold under the dissipativity assumption. Technically, their result is established via verify the uniform LSI of SGLD outputs. Beyond the dissipativity assumption, they also establish a stability result via utilizing the regularizing properties of Gaussian convolution.

### Strengths
1. Clear statement of setup and theoretical results.

2. Detailed proof with several illustrations of proof steps via pictures.

3. Previous results are clearly mentioned with detailed references.

4. The results in this paper extend previous findings under convexity to weaker conditions, which is an important improvement.

### Weaknesses
The writing in some parts is confusing, making it difficult to clearly understand the contribution in Section 6:

1. In line 199, the authors state, "we assume in the following that the Gibbs distribution with density proportional to exp(-Fn) satisfies the LS," but in Assumption 19, the authors seem to state this LSI assumption again. Is there any difference? It is unclear why the LSI assumption is restated, and whether this is a different LSI than the one mentioned earlier. The relationship between the LSI assumption and the dissipativity assumption should be clarified, as it's not immediately obvious why the analysis would need two separate assumptions.

2. In Section 6.1, the authors seem to claim two important preliminary results in Lemma 16 and 17 but don't explain how they affect establishing the main result. The role of these lemmas in the overall proof strategy is not clearly articulated. Specifically, it's unclear how the smoothing property of Gaussian convolution, as suggested by Lemma 17, is used to bridge the gap between the per-iterate analysis and the target measure LSI. The connection to the main result is missing, making it difficult to assess the importance of these lemmas.

3. It seems that the results in Section 6 are established without verifying the uniform LSI. If so,I am wondering if the analysis template in Section 4 is only applied in Section 5 and whether it should be merged with Section 5. Moreover what is the main proof framework for establishing results in Section 6? It's unclear if the analysis in Section 6 follows the same template as Section 5, and if not, what the alternative proof strategy is. The lack of clarity on the proof framework makes it hard to understand the technical contribution of Section 6. Specifically, it is not clear how the results are obtained without a uniform LSI, and what replaces this assumption in the analysis.


Other minor writing problems

1. In line 90, should it be "the bound does not decay to zero"?

2. In lines 439, 452, 874, "given in Theorem 12."

3. In line 504, "given in equation 8 and equation 9."

### Questions
My main questions are about Section 6, as stated in the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores KL and Rényi divergence stability of Stochastic Gradient Langevin Dynamics (SGLD) algorithm. The main characteristic of the presented stability bounds is that they do not become vacuous with the number of iteration of SGLD, which is achieved by assuming log-Sobolev type isoperimetric inequality being satisfied, either throughout the stochastic process, or just by the steady-state Gibbs distribution that SGLD asymptotically approximates. Such isoperimetric properties have also been recently shown to provide rapid convergence in informational divergence as well as convergent DP properties. In a similar vein, the paper derives non-asymptotic and convergent generalization bounds for SGLD as well as bounds on Rényi DP under isoperimetric assumptions. Moreover, the paper shows that the isoperimetric assumption is satisfied under settings considerably milder than strongly-convex losses, such as under dissipative and smooth losses.

### Strengths
- The paper is well-written and explains its ideas in a well-paced manner, introducing a bit of background, assumptions, and supporting theorems at convenient locations for the reader to follow.
- The paper presents an example where non-convex loss can provide generalization guarantees that are non-vacuous in number of iterations.
- The paper simplifies the expansive-contractive decomposition of SGLD steps used in related works for bounding information divergence.

### Weaknesses
Non-analytical issues:

- There is no comparison of the presented bounds with existing results in literature. The generalization bounds presented should be compared to both information-theoretic and non-information theoretic bounds under similar sets of assumptions. Specifically, the paper should discuss how its results compare to existing bounds for noisy iterative algorithms, highlighting the trade-offs between different approaches. The current discussion focuses on the number of iterations, but a more comprehensive comparison is needed.

- Contrasting with lower bounds on stability is needed to assess gaps in the tightness of the analysis presented. If such an analysis proves difficult, a well-designed experimental evaluation to compare the generalization bounds with the actual generalization behaviour under the stated assumptions should have been included. The paper should provide some empirical evidence to support the theoretical claims, especially given the difficulty in obtaining analytical lower bounds. This could involve testing the bounds on synthetic or real-world datasets.

Technical comments:

- Firstly, information-theoretic generalization bounds inspired by Xu and Raginsky seem to have an O(1/sqrt(n)) dependence on the dataset size, even in cases where other generalization approaches give a better O(1/n) bounds [1]. Since the bounds presented in this paper show dependence in the dataset size n only through Lemma 2 (by Xu and Raginsky), I believe the paper's generalization guarantees might have suboptimal dependence on n under the assumptions made. The paper should acknowledge that the dependence on dataset size might be suboptimal and discuss the limitations of the current analysis in achieving the faster O(1/n) rate.

- Lemma 3 for conversion of Rényi DP to $(\epsilon, \delta)$-DP isn't the best known bound. [Theorem 21, 2] gives a strict improvement which is the best known conversion in my knowledge. Using the best known conversion is important for obtaining tighter privacy guarantees.

- While Theorem 7 neatly presents the change in Rényi divergence under LSI after a single SGLD step, I believe this inequality might be loose, specially in the dependence on the order $q$ of Rényi divergence. That's because the paper slightly modifies the expansion-contraction template used in other prior works for simplicity. In [3] the expansion-contraction step seems to occur simultaneously, which yield a PDE that is better able to quantify the change in Rényi divergence when integrated over a single step. The paper should explore if the simplification introduces a significant loss in the tightness of the bound, especially with respect to the order of the Rényi divergence.

- In Section 5.1, the constant of LSI under convexity is dimension independent. But on relaxing strong convexity to dissipativity, the LSI constant has an exponential dependence O(e^d) on the dimension size. The paper further claims in line 418 that this dependence on dimension can't be improved without additional assumptions. To me, this seems like a major hurdle that greatly limits the applicability of the generalization bounds presented (both Corollary 14.1 and 15.1) as plugging in the $C_{LSI}$ constant of Theorem 12 gives an $KL(X_t\Vert X'_t) = O(e^d)$ dependence on dimension $d$. The paper should acknowledge this limitation and discuss the practical implications of the exponential dependence on dimension. This dependence could make the bounds vacuous in high-dimensional settings.


Crafting examples of loss functions satisfying the assumptions made and computing a lower bound on how the KL or Rényi divergence changes with iterations seems doable.

### Questions
I'm not sure if I understood the results in Section 6, which seems to be adopting an entirely different style of analysis as compared to section 5, which helps in lifting the LSI assumption on the entire sequence of intermediate distributions to LSI on the Gibbs distribution corresponding to the loss function. It would help if this approach is explained more thoroughly to see the idea in there a bit more clearly.

I'm open to increasing my score, especially if Section 6 has some good ideas that I might have missed.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies generalization of stochastic gradient Langevin dynamics (SGLD) via information theoretic bound. The author(s) obtained Renyi stability by assuming the iterates verify the log-Sobolev inequality (LSI). The author(s) further showed that the LSI indeed is satisfied under some dissipativity condition. Further results are obtained when dissipativity is not available, in which case KL stability can still be achieved. The bounds are uniform-in-time which are strong. A by-product is that the paper shows that under dissipativity, all the iterates verify a uniform LSI, which was previously shown only in the strongly-convex setting, that resolves an open question in the literature.

### Strengths
(1) The paper is well written, and it is a very solid theoretical paper. 

(2) The bounds are uniform-in-time, obtained under Renyi divergence under dissipativity condition and KL stability without dissipativity.

(3) A key ingredient in the proof is to show that under dissipativity, all the iterates verify a uniform LSI, which was previously shown only in the strongly-convex setting. This by-product resolves an open question in the literature.

### Weaknesses
 (1) Assumption 15 seems to be a really strong assumption. It would be nice if the author(s) can comment on whether this assumption is needed because of the proof technique or it might be unavoidable. Specifically, the assumption requires a bound on the sensitivity of the loss function with respect to the iterates, which may not hold for all loss functions, especially in non-convex settings where the gradients can be highly variable. It would be beneficial to discuss the implications of this assumption in more detail, perhaps with examples of loss functions where it might fail.

(2) As the author(s) mentioned in the conclusion section, the dimension dependence is strong. But since the author(s) are working with non-convex setting, this is understandable.

(3) Assumption 14, as stated, is unclear. It appears to be a pseudo-Lipschitz condition, but the absence of a term involving the difference between $z$ and $z'$ on the right-hand side makes it difficult to interpret. A pseudo-Lipschitz condition typically bounds the difference of a function at two points by a constant times the distance between those points. The current formulation seems to be missing this crucial element, raising concerns about its validity and applicability.

### Questions
(1) In the second paragraph under contributions, "all the iterates of verify a uniform log-Sobolev inequality''. Should it be "all the iterates verify a uniform log-Sobolev inequality''?

(2) In Lemma 2, is the constant $c$ the same one from Assumption 1? If so, you should mention in the statement of Lemma 2 that you are assuming Assumption 1. For a related question, for each lemma and theorem, it would be really nice if the author(s) can make it more transparent which assumptions are used, especially because the paper contains quite many theoretical results in different settings which require different assumptions.

(3) It would be nice if the author(s) can add some intuitive explanations about the half-step technique in the analysis. For example, when you split the Gaussian noise $N_{k+1}$ into $N_{k+1}^{(1)}$ and $N_{k+1}^{(2)}$, why the former becomes expansive, whereas the latter becomes contractive.

(4) Assumption 14 seems to be a bit strange. If it is pseudo-Lipschitz, shouldn't it be small
when $z$ and $z'$ are close to each other but I do not see $z$ and $z'$ appearing on the right hand side.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses stochastic optimization, where the goal is to minimize $F(x):=E_{Z\sim \nu}f(x;Z)$ for some underlying distribution $\nu$.
Let $D$ and $D'$ be two datasets, each consisting of $n$ i.i.d. samples from $\nu$. Running noisy stochastic gradient descent (SGD) on these two datasets yields sequences $\{X_k\}$ and $\{X_k'\}$ respectively. It is known that the generalization error scales with the KL divergence between the distributions of $X_k$ and $X_k'$ .

This paper provides a time-independent upper bound on the KL divergence, even as $k\to \infty$. The authors first show that when the log-Sobolev inequality (LSI) holds, an upper bound on the KL divergence can be derived. They further demonstrate that under appropriate conditions, such as dissipativity, the distribution satisfies the LSI, thus leading to the desired bound.

### Strengths
The problem studied is interesting and has practical relevance, with clear motivation provided.
The paper is well-structured, with different cases and scenarios analyzed in depth.
The results are extensively studied across various settings.

### Weaknesses
1. The main proofs rely heavily on existing work, like Theorems 6, 8, and 12.
2. Some assumptions require further discussion. For instance, Assumption 15 seems restrictive in unbounded domains like $R^d$.
3. In Theorem 12, the LSI constant scales exponentially with the dimension, which could be problematic for high-dimensional settings.



### Questions
1. Isoperimetric vs. Log-Sobolev Inequality:
The paper mentions the use of the isoperimetric inequality, but the arguments seem entirely based on the log-Sobolev inequality (LSI). In probability theory, the isoperimetric inequality is usually considered a separate concept. Could this be a typo or an imprecise reference?

2. What is \Tilde{X}_k' in Theorem 5? Is it a typo, and should it be S_k instead?

3. The $S_k$ is not carefully discussed. In SGLD, when drawing a batch of size $b$, could using a smaller batch size lead to a tighter bound on the KL divergence?

### Soundness
2

### Presentation
2

### Contribution
2
