# Minixax Optimal Two-Stage Algorithm For Moment Estimation Under Covariate Shift

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Covariate shift occurs when the distribution of input features differs between the training and testing phases.  In covariate shift, estimating an unknown function's moment is a classical problem that remains under-explored, despite its common occurrence in real-world scenarios. In this paper, we investigate the minimax lower bound of the problem when the source and target distributions are known. To achieve the minimax optimal bound (up to a logarithmic factor), we propose a two-stage algorithm. Specifically, it first trains an optimal estimator for the function under the source distribution, and then uses a likelihood ratio reweighting procedure to calibrate the moment estimator. In practice, the source and target distributions are typically unknown, and estimating the likelihood ratio may be unstable. To solve this problem, we propose a truncated version of the estimator that ensures double robustness and provide the corresponding upper bound. Extensive numerical studies on synthetic examples confirm our theoretical findings and further illustrate the effectiveness of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of estimating moments of responses under covariate shifts. The authors propose a two-stage algorithm, using a doubly robust structure with weight truncation, that achieves a minimax estimation lower bound.

### Strengths
- The investigated problem of estimating moments under covariate shift appears fundamental, and the paper offers an approach that the authors show is minimax optimal, which seems a valuable contribution.

 - The technical results are presented and interpreted clearly.

### Weaknesses
 **Technical Contributions**: The novelty in attaining and proving the main theorems (Theorems 1 and 2), compared to the existing literature, is unclear. In particular, the proofs appear similar to those in Blanchet et al. (2024), with the main addition being separating and upper bounding the term $w(x)$. It is not clear how the specific structure of the covariate shift problem necessitates the particular proof techniques used, beyond the inclusion of the reweighting term. The authors should more clearly articulate the novel technical challenges that arise from the covariate shift setting and how their proofs specifically address these challenges, rather than simply adapting existing techniques. 

**Limitations of the minimax lower bound results**: If I understand correctly, the minimax lower bound result, as well as the proposed algorithm from the authors that achieve the lower bound, assumes the source and target distributions are known. However, a major difficulty of covariate shifts is to handle the unknown distributions. In this regard, the authors only show an upper rate bound and double robustness of their approach in the latter setting. So, I feel there's a gap between the claimed minimax optimality and the actual efficiency of the proposed approach, and this gap is not just the usual discrepancy between theoretical bounds and practical algorithms (as common in ML theoretical guarantees), but is about whether the claimed theory is conceptually trying to capture the fundamental difficulty of the estimation problem. The theoretical results seem to be more of a proof of concept under a strong assumption, rather than a practical solution for the general covariate shift problem.

The above are my main concerns. Additionally, the following suggestions might be useful:
- It would be helpful to provide more justification for the critical Assumption 1, for instance discussing specific estimators that meet the assumption (i.e., to make the paper more self-contained instead of just referring readers to previous papers).
- Section 4.3 deserves more discussions. For example, 
- It would be beneficial if the authors could draw parallels of their assumed condition on the probability concerning likelihood ratio with existing literature, possibly through examples demonstrating the probability of large shift regions and the functions $g(T)\leq T^{-\alpha}$ for classical parametric distribution classes.
- More guidance can be provided on choosing threshold $T$ in practice. For example, how much do we need to know about $\alpha$ to choose $T$ properly.
- More discussions can be provided on the implication of the power decay $\alpha$. In particular, when $\alpha = \infty$, does the convergence rate reduce to $\bar b r(n)$, matching the dependence on $n$ observed in Theorem 2?

Some typos:
- In the right-hand side of eq (4) in Assumption 1, the last “+” should be a subscript.

### Questions
1. Do we really need to do two-stage algorithm? For example, can $\hat f$ obtained from importance-weighted regression satisfy the upper bound? (perhaps truncating the weights in the regression?)
2. Assumption 1 requires $f$ to be sufficiently smooth. Can the upper bound still be matched if $f$ is less smooth?
3. There is not much discussion on the difference with recent minimax optimal results, e.g., [Ma et al. 2023], which also addresses estimation under nonparametric space. More detailed comparisons would help highlight the unique contributions of this work.

**Reply to authors' response:** I thank the authors for the clarifications and additional experiments. The explanation on the literature regarding known versus unknown distributions is helpful, and so is the additional experiment that shows the significance of two-stage over one-stage procedures. Regarding the relative novelty, my feeling is that using truncation on likelihood ratio to control bias-variance is, in some sense, obvious as an idea, but working it out rigorously and demonstrating its usage as the authors did requires a lot of careful work, which I appreciate. I raised my score in view of all these.

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
3

### Summary
This paper considers the problem of estimating the moment of an unknown function under covariate shift. Specifically, the paper aims to estimate the $q$-th moment of $f$ under target distribution $\mathbb{P}^*$ with p.d.f. $p^*(x)$, based on a random sample drawn from source distribution $\mathbb{P}^{\circ}$ with p.d.f. $p^{\circ}(x)$. Here, the unknown function $f$ is assumed to belong to the Sobolev space $\mathcal{W}^{s, p}(\Omega)$ with $\Omega \subset \mathbb{R}^d$, where $s$ indicates the degree of smoothness and $p$ specifies the integrability condition of these derivatives. The paper characterizes the impact of covariate shift on the minimax lower bound when $p^{\circ}$ and $p^*$ are known. It turns out that a constant $B \geq w(x)$, where $w(x):=\frac{p^*(x)}{p^{\circ}(x)}$, plays a central role in the established minimax lower bound. Then, the paper proposes a two-stage algorithm which attains the minimax lower bound up to a logarithmic factor for two cases: (i) $p^{\circ}$ and $p^*$ are known and (ii) $p^{\circ}$ and $p^*$ are unknown. For the latter case, the paper truncates an estimator of $w(x)$ to stablize the algorithm. The proposed method requires two models: one for estimating $f(x)$ and the other for estimating $w(x)$. The proposed estimator is doubly robust in that it will be consistent if at least one of the two estimators is consistent.

### Strengths
The paper is clearly laid out. Specifically, it provides the minimax lower bounds and develops an estimator that matches the lower bounds up to the log factor when both target and source distributions are known. Furthermore, a doubly robust estimator is developed when the distributions are unknown.

### Weaknesses
Although the paper considers an interesting problem in theme of an important topic, namely covariate shift, there are two major weaknesses. 

(1) The problem of estimating the $q$-th moment of an unknown function $f$ is not well motivated. On page 1, it is stated that "This is a common scenario in many fields, such as counterfactual inference in causal inference (Ding, 2024)." However, this is not informative enough; Ding (2024) is a textbook and there is no concrete example by simply citing the textbook. The paper fails to articulate why estimating higher-order moments, specifically, is crucial in these scenarios, beyond the general notion that they capture risk. For instance, in causal inference, while counterfactual means are often the focus, the relevance of higher-order moments like variance or skewness is not clearly established. The paper needs to provide specific examples where these higher-order moments are directly used for decision-making or inference, rather than just being a theoretical exercise.

(2) In addition, the current numerical example is very artificial and has nothing to do with real applications in causal inference or any other substantive field. The example uses a simple polynomial function and a toy distribution shift, which does not reflect the complexities of real-world data. This makes it difficult to assess the practical utility of the proposed method. The paper should demonstrate the method's performance on a more realistic dataset where the function $f$ is complex and the covariate shift is non-trivial.

### Questions
(1) There is a typo in the title: "Minixax" should be "Minimax".

(2) When the target distribution is unknown, it is assume that m (≫n) unlabeled samples from the target distribution. Is it necessary that m is much larger than n? This seems quite restrictive. Also, what condition is exactly needed between m and n? Is it enough to assume that $m/n \rightarrow \infty$?

### Soundness
3

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
The paper studies the problem of functional estimation, specifically, a moment of some function, with respect to the target distribution under covariate shift. The paper establishes minimax lower bound of this problem under RKHS assumption on the objective f, with additional constraints on source and target distribution. Furthermore, the paper proposes an estimator which attains this lower bound. The paper also introduces a practical version of the proposed estimator, and further establishes convergence rate.

### Strengths
The paper is beautifully written with a solid theoretical results. Starting from the optimality, it presents an idealized estimator which attains the optimality, and most importantly, it provides a practically usable estimator and establishes theoretical results for the stabilized estimator. The structure and presentation of the theoretical statements hits perfect balance between technical details and insights for readers to follow. The results are stated in a way how each step of the proposed estimator influences the final convergence rate, which really helps to gain insight on the proposed estimator.

### Weaknesses
No major weakness.

### Questions
On the decaying rate assumption on g(T) in theorem 3, it seems that this imposes further restrictions on the source/target distributions. In addition to the statements on the weight itself, is there any way to gain further insights on what type of source/target distributions pairs would satisfy this condition?

### Soundness
3

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
This paper proposes a moment estimation method under covariate shift.
More specifically, the authors consider the moment estimation problem with the Sobolev class for the labeling function and with a bounded likelihood ratio of the source and target covariate distribution.

Under this setup, the paper proves a minimax lower bound on the estimation error.

Then, the authors propose a method whose upper bound of the error meets the lower bound, but with the knowledge of the target covariate distribution and the likelihood ratio.
The proposed method combines any estimate of the labeling function and the estimate with truncated likelihood-ratio weighting to construct a doubly robust estimator (Eq. (3)).

Furthermore, the paper proposes an estimator that does not use the knowledge of the target covarite distribution or the likelihood ratio but estimate them using additional unlabeled data sampled from the target distribution. Under some tail probability condition on the likelihood ratio, this estimator has an upper bound slightly worse than the minimax lower bound.

Finally, the paper presents some simulation to see the impact of the degree of covariate shift and the smoothness of the labeling function.

### Strengths
- The paper is nicely written. The analyses in the appendix are quite involved, but I can see the authors' efforts to make them accessible.

- The paper studies an interesting and useful problem and theory.

- The proposed doubly robust estimator is interesting (although the core idea has been already wide used in the causal inference/econometrics literature).

### Weaknesses
 - In the minimax lower bound of Theorem 1, is the estimator $\hat{H}^q$ is not allowed to access any information about $p^*$ or $w$, unlike the proposed estimator does. This makes the comparison between the lower bound and the upper bound in Theorem 2 irrelevant.

  Indeed, the proof does not construct the two hypotheses in a way that the estimator needs to know about $p^*$ or $w$. For example, in the first part of the proof, it suffices to determine whether $p(y | x)$ is $g_0$ or $g_1$.

  I believe that in the formulation of $\mathcal{H}_n^{f,q}$, we can construct two hypothesis with a common $p(y | x)$ but different $p(x)$'s, to make any estimator unable to tell the difference.

- There is a strong assumption that there is no noise in the observations of the label: $y_i = f(x_i)$. This limits applications of the proposed method.

- The estimator in the case of an unknown likelihood ratio does not seem minimax-optimal because of the exponent $\frac{\alpha}{\alpha + 1}$ in Eq. (8).

- There is no experiment about the comparison between the proposed method and the Monte Carlo estimate using $\hat{f}^q(x_i')$ or $w(x_i) y_i^q$.

- Likewise, there is no experiment about the effect of the truncation.


### Questions
### Major concerns
- Is there anything I am missing in the first comment in Weaknesses (about the minimax lower bound)?

- Is there a practical application where there is no noise or uncertainty in the label?

- Does the truncation bring any benefits in theory?

- Do the authors have any result for the ablation study about the effect of truncation? That is, comparison between the proposed estimate and that without truncation.

- Any comparison between the proposed method and the Monte Carlo estimate only using $\mathbb{E}[\hat{f}^q(x_i')]$ or $\mathbb{E}[w(x_i) y_i^q]$?

### Minor issues
- Perhaps, the paper should mention that Ma et al. (2023) uses the truncation trick but in the case of unbounded likelihood ratios.

- Is the calculation of the KL divergence with the delta function mathematically sound? Because there is the logarithm function inside the integral. In particular, I could not figure out how to obtain the equality in line 718. Could the authors detail this calculation?

- What is $s$ in $f(x; s)$? Is it $k$?

- Is the $+$ at the end of Eq. (4) a typo?

- In line 644, maybe $K_0$ should be $K$ (otherwise, the support should be $[-1, 1]^d$).


---
**Edit:**
After the discussions with the authors, my concerns about the soundness has been addressed. I have adjusted my score from 5 to 6.
However, I still think the assumptions that there is no noise in $y_i$ and the density is known are strong, and the applications are very limited.

Moreover, the former assumption allows one to change the label from $y_i$ to $y_i^q$, to reduce the problem to the expectation of the mean under covariate shift. This type of problem has been already well studied in the treatment effect estimation literature, including the doubly robust estimators. The submitted paper might lack comparison with such work and discussions about its novelty.

### Soundness
2

### Presentation
3

### Contribution
2
