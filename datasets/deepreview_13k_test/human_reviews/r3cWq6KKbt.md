# Global Well-posedness and Convergence Analysis of Score-based Generative Models via Sharp Lipschitz Estimates

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We establish global well-posedness and convergence of the score-based generative models (SGM) under minimal general assumptions of initial data for score estimation. \textit{For the smooth case}, we start from a Lipschitz bound of the score function with optimal time length. The optimality is validated by an example whose Lipschitz constant of scores is bounded at initial but blows up in finite time. This necessitates the separation of time scales in conventional bounds for non-log-concave distributions. In contrast, our follow up analysis only relies on a local Lipschitz condition and is valid globally in time. This leads to the convergence of numerical scheme without time separation.  \textit{For the non-smooth case,} we show that the optimal Lipschitz bound is $O(1/t)$ in the point-wise sense for distributions supported on a compact, smooth and low-dimensional manifold with boundary.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the mathematical framework behind score-based generative models (SGMs). The authors' primary focus is to establish conditions under which these models are well-posed and convergent.

Key points from the paper include:
1. **Well-Posedness of SGMs:** The authors prove that SGMs are well-posed under global conditions. They introduce Lipschitz estimates that maintain stability and prevent the “blow-up” of the score function, which has been an issue in practical applications where score gradients become unstable.
2. **Convergence and Sharp Lipschitz Bounds:** They provide a Lipschitz bound for the score function, addressing both smooth and non-smooth cases. This bound helps establish global convergence of the backward process (used in sample generation), even for non-log-concave distributions. For non-smooth data distributions, the bound asymptotically scales as $1/t$, ensuring convergence on low-dimensional manifolds with compact support.
3. **Theoretical Contributions:** The authors introduce rigorous estimates for the Hessian and gradient of the score function, reinforcing the stability and convergence properties. This allows the generative models to better approximate complex data distributions.

The paper concludes with insights into how these findings could guide model implementation, such as early stopping strategies and parameter adjustments, to ensure stable and efficient generation in real-world applications.

### Strengths
The major strengths of this paper are:
- Establishing crucial bounds on the Hessian of the score function, which significantly enhance existing bounds on the KL divergence from *Chen et al. (2023)*. These bounds are vital for assessing the fidelity of generated distributions.
- Carefully tracking the dependence on dimensionality throughout the analysis, a critical aspect for score-based generative models (SGMs) given their frequent application to high-dimensional data distributions.
- Characterizing the explosion of the score function as $t$ approaches $0$. Although this instability near zero has been commonly observed in practice, the authors quantify the explosion’s magnitude through PDE techniques, opening the door to improve model stability in high-dimensional generative tasks.
- Describing the case of compactly supported data distributions, shedding light on the theoretical limits of score-based generative models (SGMs). This perspective allows for a deeper understanding of how SGMs behave when data is restricted within a bounded region, which has practical relevance given that real-world data often exhibit such constraints.

### Weaknesses
Here are some weaknesses of the paper:
1. **Limited Comparison with Recent Literature:** The paper lacks sufficient engagement with recent literature on SGMs, particularly from a PDE perspective. A broader comparison with recent works is needed, especially regarding bounds on KL divergence, as several relevant contributions exist and should be cited.
2. **Redundancy in Subsection 2.2:** The computations in Subsection 2.2 are already present in the literature, as seen in *Conforti, Durmus, Gentiloni-Silveri (2023)*. While this content is valuable for readability, it might be better suited to an appendix section to streamline the main text.
3. **Unclear Novelty in Theorems 4.3 and 4.4:** The novelty of Theorems 4.3 and 4.4 is unclear in comparison to the results in *Chen et al. (2023)*. It would be beneficial to clarify how the bounds on the Hessians improve convergence rates relative to this paper, particularly in establishing any distinct contributions.
4. **Lack of Appendix Structure:** Adding a paragraph at the beginning of the appendix outlining its structure would improve navigation and clarity for readers.

Addressing these points would strengthen the paper, and I would consider raising the evaluation if these aspects are clarified and expanded.

### Questions
All the questions have been addressed in the *Weaknesses* section.

### Soundness
4

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
2

### Summary
Recent theoretical works on analyzing diffusion models require bounds on the Lipschitzness of the score function of the noised distribution at all time-steps. This work gives bounds on Lipschitzness under various conditions on the initial data distribution, and uses some of these bounds to instantiate prior guarantees for diffusion models.
- Theorems 3.1 and 3.4 show that if the initial data distribution is smooth, then the score of the noised distribution is Lipschitz up to some finite time T, and that this cannot be extended to all times
- Theorem 3.5 gives local Lipschitzness estimates of the score function under local assumptions
- Theorems 3.9/3.10 and Example 3.11 show that if the data distribution is supported on a manifold, then one gets Lipschitzness bounds of 1/t^2 at time t, and in fact almost everywhere one gets 1/t, and there is an example where the "almost everywhere" is necessary
- Theorem 4.3/4.4 instantiate diffusion model guarantees using Theorem 3.1 and Theorem 3.5 respectively

### Strengths
The paper addresses an interesting question of trying to substantiate the Lipschitzness assumptions on score functions. The result on manifolds showing that 1/t^2 can be almost-everywhere improved to 1/t seems qualitatively new and interesting, and the example showing that this is tight provides a fairly complete story.

### Weaknesses
The paper could be written better, as far as comparison to prior work, clarity about which of the results are most "important", readable theorem statements, and discussion about the assumptions.
- Theorem 3.1, 3.9, and 4.1 seem as though they may be fairly standard / similar to prior results, but there is very little discussion about what is new and what is included merely for completeness.
- Theorem 4.4 says "with same assumption as Corollary 3.6", which in turn says "under the same assumption as in Theorem 3.5". The stated assumption is uninterpretable: is it reasonable? I can't tell. 
- The invocation of Theorem 3.5 in the proof (line 1320) provides no explanation as to how the complicated bound in Theorem 3.5 becomes this simple bound.

The most interesting result would be if the 1/t^2 -> 1/t improvement could be used to instantiate a better bound for diffusion models. However it appears that this is not done. The rest of the results in Section 4 just have lots of assumptions (e.g. the bound on T in Theorem 4.3) so it's not clear how applicable they are.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the global well-posedness and convergence of score-based generative models (SGMs) by providing sharp Lipschitz estimates for the score function under both smooth and non-smooth initial conditions. By developing optimal point-wise gradient and Hessian estimates, the authors establish conditions under which the backward diffusion process is well-posed up to time zero, effectively covering cases where previous approaches failed due to exploding scores or separated time regimes.

### Strengths
The paper introduces new sharp Lipschitz bounds for the score function, which enable global well-posedness and convergence without requiring separated time scales. This is particularly valuable for SGMs where score explosion has previously posed challenges.

### Weaknesses
I did not identify any major weaknesses in this paper. I listed some typos below.

Typos: 
1. On the LHS of equation (3), I believe $p_t$ means $\partial_t p$. Using the notation $p_t$ will probably make the reader confused as $p_0$ denotes the initial data;
2. In line 108, it should be $Q_{t'}$ instead of $Q_t'$;
3. In line 127, the LHS should be $\hat{x}$ instead of $d\hat{x}$;
4. In line 218, it should be $\mathbb{R}^n$ instead of $\mathbb{R}^d$.

### Questions
1. It appears that the main assumption in this work is Assumption 2.3, which requires that the tail distribution is bounded by a Gaussian distribution. Could you provide some intuition behind this assumption? It seems potentially quite strong, as it may imply that the data is approximately Gaussian—perhaps even stronger than the strong dissipativity condition. Could you clarify why this is a reasonable assumption for real-world data distributions?

2. The statements in Section 3.3 appear somewhat inconsistent. In Theorem 3.9, it is assumed that the density is smoothly defined on $D_0$, which may be a low-dimensional manifold, while in the proof, the integral over $\mathbb{R}^n$ is equal to the integral over $D_0$. How is $d\pi_0(y)$ defined to ensure this equality holds? Is $p_0$ a density on $D_0$ or $\mathbb{R}^n$? I may have misunderstood, so please correct me if I'm mistaken.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper focuses on providing the Lipschitz estimates for the score-function in the score-based generative models. It also provides a sharp example showing that the loss of Lipschitz bound of the score function as time gets large even with nice initial data distribution.  As a by-product, well-posedness and convergence are obtained by following existing literature.

### Strengths
(1) Estimating the Lipschitz constant for the score-function using the idea of the PDE approach is novel and makes a nice contribution to the theory of score-based generative models.

(2) An example is provided to show the Lipschitz estimate is sharp in some sense.

### Weaknesses
(1) I think in the abstract, the paper overclaims that the results are obtained under minimal general assumptions of initial data because when you look at Theorem 3.1., Corollary 3.2. etc., some relatively strong assumptions are used.

(2) Well-posedness follows immediately from the estimate on the score function and Theorem 4.1. can be found in any textbook on stochastic calculus. Moreover, the convergence analysis follows immediately from existing literature (Chen et al. 2023). In that regard,
I think the main contributions of the paper are simply the Lipschitz estimates for the score function, and well-posedness and convergence analysis are not the main contributions of the paper.

### Questions
(1) In the last paragraph of page 1, well-poseness should be well-posedness.

(2) In the last paragraph of Section 1, Planc should be Planck.

(3) On page 3, "In the analysis, we assume an $\epsilon^{2}$ bounds for this estimation'' I think you may replace $\epsilon$ by $\epsilon_{0}$ because this is what you used in Assumption 2.1.

(4) It would be nice to add some discussions about Assumption 2.3., how it is related to the assumptions in the previous theoretical work on score-based generative models.

(5) In the statement of Corollary 3.2, $p_{0}\in C^{2}(\mathbb{R}^{d})$ but you also use $\sup_{x\in\mathbb{R}^{n}}D^{2}\log p_{0}(x)$. I think in your case $d=n$? Similar issue appears in the statement of Theorem 4.3. and Theorem 4.4., where you have used both $d$ and $n$.

(6) In Theorem 4.3., in the upper bound for $\mathrm{KL}(p_{0}\Vert\hat{q}_{T})$, the first term is $(M_{2}+d)e^{-T}$. Can you remind the readers what is $M_{2}$ here (or where it is defined)? Also, for $H_{T}$, does it have an explicit formula (depending on $L_{0},L_{1},T$) and if so you should mention it. Also, I think it will be nice to spell out the dependence on $T$ because your upper bound is written in a way with an emphasis on the dependence on $T$, and if $H_{T}$ is implicit in $T$ it will make your bound less
valuable.

(7) In order to have $\mathrm{KL}(p_{0}\Vert\hat{q}_{T})$ to be small in  the upper bound for $\mathrm{KL}(p_{0}\Vert\hat{q}_{T})$ in Theorem 4.3., it seems you have to choose $T$ to be large, but on the other hand $T<-\log(1-\frac{1}{L_{0}+1})$, which seems
problematic to me. 

(8) If my understanding is correct, the main contribution of the paper is the Lipschitz estimate on the score function, rather than the convergence analysis, which follows from Chen et al. (2023) etc. from the literature. In that spirit, does that mean your Lipschitz estimate on the score function can also be used to obtain convergence analysis for probability flow ODEs by leveraging existing works on the convergence analysis of the probability flow ODEs in the literature?

### Soundness
3

### Presentation
3

### Contribution
3
