# On Statistical Rates of Conditional Diffusion Transformer: Approximation and Estimation

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
We investigate the approximation and estimation rates of conditional diffusion transformers (DiTs) with classifier-free guidance.
We present a comprehensive analysis for ``in-context'' conditional DiTs under four common data assumptions.
We show that both conditional DiTs and their latent variants lead to the minimax optimality of unconditional DiTs under identified settings.
Specifically, we discretize the input domains into infinitesimal grids and then perform a term-by-term Taylor expansion on the conditional diffusion score function under Hölder smooth data assumption.
This enables fine-grained use of transformers' universal approximation through a more detailed piecewise constant approximation, and hence obtains tighter bounds.
Additionally, we extend our analysis to the latent setting under the  linear latent subspace assumption.
We not only show that latent conditional DiTs achieve lower bounds than conditional DiTs both in approximation and estimation, but also show the minimax optimality of latent unconditional DiTs.
Our findings establish statistical limits for conditional and unconditional DiTs, and offer
practical guidance toward developing more efficient and accurate DiT models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the statistical rates of approximation and estimation for conditional diffusion transformers (DiTs) with classifier-free guidance. It provides a comprehensive analysis under four common data assumptions, showing that both conditional and latent variants of DiTs can achieve minimax optimality. It uses a modified universal approximation of the single-layer self-attention transformer model to circumvent the need for dense layers, which results in tighter error bounds for both score and distribution estimation.

### Strengths
The paper is original in its theoretical approach to studying conditional diffusion transformers, offering new insights into their performance and limitations. The quality of the theoretical analysis is high, with clear outlines and complete proofs. The clear and thorough exploration of statistical limits and estimation procedures is a key strength.

### Weaknesses
1. Some results seem to suffer from the curse of dimensionality, which seems not a practical bound.
2. There is an absence of empirical results to complement the theoretical analyses.
3. More practical implications of the assumptions could be added.

### Questions
**1.** On the top of page 3, should the denominator of $\nu_3$ be $d_0+d_y$ instead of $d_x + d_y$?

**2.** The bound in Theorem 3.1, the first bound of Theorem 4.1, and the first bound of Theorem 4.2 seem to depend exponentially on $d_x$ or $d_0$, which seems to suffer from CoD. Is the bound tight here?

**3.** Is there any practical example that matches the assumption 3.2? If so, I’d suggest adding a brief paragraph to discuss this.

**4.** In the first bound of Theorem 3.3 and Theorem 3.4, the bound seems to be decaying in a rate of $exp(-d_x)$, is this a typo?

**5.** The second bound of Theorem 3.3 seems to be not sensitive to $d_y$. The second bound of Theorem 3.4 depends on $d_x$ and $d_y$ only through $d_x+d_y$, and is not sensitive to it. Similarly, the second bound of Theorem 4.2 only depends on $d_0$ and $d_y$ only through $d_0+d_y$. Is there any intuition behind this? 

**6.** There aren't any empirical results in the current version. I’d suggest adding a few practical examples to illustrate the validation of the bounds.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies the statistical understanding of the conditional diffusion transformers (DiTs) with classifier-free guidance. The authors focus on understanding the approximation and estimation rates of these models under various data conditions, particularly in "in-context" settings. They show that both conditional DiTs and their latent variants can achieve minimax optimality, similar to unconditional DiTs, in certain scenarios. The analysis is based on discretizing input domains into small grids and applying Taylor expansions to the conditional diffusion score function, assuming data follows Hölder smoothness. This approach allows for a more refined piecewise approximation, leveraging transformers' universal approximation capacity. The study also extends to latent conditional DiTs, showing that these models offer better approximation and estimation bounds than standard conditional DiTs, especially under linear latent subspace assumptions.

### Strengths
- The paper provides a detailed theoretical framework for analyzing the approximation and estimation rates of conditional diffusion transformers (DiTs) under various data assumptions.
- The work integrates classifier-free guidance into the analysis of conditional DiTs.
-  The paper provides rigorous results on score approximation and distribution estimation, including sample complexity bounds for score estimation which lead to minimax optimal estimation results.
- The work integrates classifier-free guidance into the analysis of conditional DiTs.
- Beyond theoretical contributions, the findings offer practical guidance for configuring transformer-based diffusion models to achieve optimal performance.

### Weaknesses
A general weakness of this paper is its reliance on a lengthy and detailed appendix, which is not mandatory for reviewers to read. While the results are strong and represent a valuable contribution to the field, the extensive appendix makes it challenging to validate the findings within a limited review timeframe.

- The analysis relies significantly on Hölder smoothness assumptions, which may not apply to all types of data. This limitation restricts the generalizability of the theoretical results to datasets that satisfy these specific conditions. Additionally, the assumption of isotropic smoothness across input variables does not always hold, particularly in cases where the condition is discrete or irregular.

- The study does not address the high-dimensional structural dependence of the data. It is overly restrictive to assume that the ambient dimensions of practical data distributions are small and that the rates of dependence relative to the ambient dimension are sufficiently slow.

- The paper lacks empirical validation that connects the theoretical rates and dimensionality to practical datasets. For instance, it would be beneficial to clarify what smoothness refers to in the context of the given dataset. Furthermore, it is unclear how one might establish practical relevance for the proposed rates and validate them empirically.

### Questions
In addition to the weaknesses outlined, please consider the following:

- Can the work be extended to a manifold setup where the rates depend on the intrinsic dimension of the data, similar to the approach taken by Oko et al. (2023)?

- Regarding the assumptions made, if one has a function with significantly less restrictive conditions than those presented in this study, what advantage does using a transformer provide over traditional statistical methods for achieving a minimax rate? This question is particularly relevant from a theoretical perspective, which is the primary focus of this paper.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provide a theoretical analysis for statistical rates of conditional diffusion transformer, mainly focusing on the score approximation, score estimation and distribution estimation.

### Strengths
1. This paper is well-written, which provides detailed theoretical analysis and clear explanations. Additionally, the main theorems are presented concisely and effectively, and the discussions in remarks are particularly helpful for interpreting the results.
2. Comparing with the previous work ([1]), the theoretical analysis alleviates the double exponential factor and achieves minimax optimal statistical rates for DiTs under Hölder smoothness data assumption.

[1]. Hu J Y C, Wu W, Li Z, et al. On statistical rates and provably efficient criteria of latent diffusion transformers (dits)[J]. arXiv preprint arXiv:2407.01079, 2024.

### Weaknesses
1. As a follow-up work of [1], maybe the contribution mainly focuses on polishing and extending the previous results, which may lead to a lack of novelty. Could you provide some new insight points about it?

2. With the good rates theoretically,  could this work provide some implementations in practice?

### Questions
See weakness.

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
3

### Summary
This paper mathematically investigates the approximation and estimation properties of conditional diffusion Transformers (DiTs) with classifier-free guidance. Theoretical connections between conditional DiTs and their unconditional latent variants are established for data distributions with certain smoothness.

### Strengths
1. This paper seems mathematically sound. 
2. The settings studied in this work are abundant and quite complex. 
3. The roadmaps of proofs are clear.

### Weaknesses
1. The derived approximation and estimation bounds appear to scale poorly in certain asymptotic regimes. Specifically, in high-dimensional settings or with long input sequences, several issues emerge:

   - For score approximation (Table 1), the upper bound becomes infinitely large as $\sigma_t^2$ approaches 0 when $t$ approaches 0. Additionally, the upper bound approaches $O(1)$ as $\epsilon^{1/d}$ approaches 1 when $d$ approaches infinity, which is vacuous in high-dimensional scenarios. The multiplicative term $(\log N)^{d_x}$ in Theorem 3.1 leads to an exponentially large upper bound with high-dimensional inputs. Furthermore, the parameter bounds of Transformers become exponentially large for long input sequences, as indicated by $\||W_{\{Q,K\}}\||=O(N^{L/d})$ in Theorem 3.1.

   - For score estimation, the upper bound in Theorem 3.3 derived from Assumption 3.1 exhibits a $(\log n)^{-dL}$ term, which decreases exponentially fast with increasing data dimension or sequence length, raising concerns about its reasonableness. Under Assumption 3.2, the sample complexity estimate becomes vacuous for long input sequences due to the power of $1/n$ being approximately $\Omega(1/L)$.

   - Similar issues regarding the upper bounds are present in Theorem 3.4 for distribution estimation, mirroring the concerns raised for score estimation.

2. The practical implications of the theoretical bounds are unclear without empirical validation. It is uncertain whether these theoretical constructions can be realized through concrete training dynamics. Numerical simulations are needed to verify the dependence of the derived upper bounds on various factors.

3. There is a lack of explicit characterization of the model capacity dependence in the provided estimates. The error terms do not clearly relate to the parameters $h$, $s$, and $r$.

4. Minor issues:

   - The notation $s$ is used for both head size and Hölder smoothness, leading to potential ambiguity.

   - In the caption of Table 1, "length" should be "lengths" in the phrase "... where $L$, $\tilde{L}$ are sequence length of transformer inputs".

### Questions
1. For the score approximation: 
- $\sigma_t^2 \to 0$ when $t \to 0$, leading to infinitely large upper bounds (Table 1).
- $\epsilon^{1/d} \to 1$ when $d \to \infty$, leading to $O(1)$ upper bounds (Table 1) that are vacuous in high-dimensional settings. 
- The upper bound is *exponentially* large given high-dimensional inputs, due to the multiplicative term $(\log N)^{d_x}$ (Theorem 3.1). 
- The parameter bounds of Transformers are also *exponentially* large given long input sequences (with fixed dimensions), since $\||W_{\{Q,K\}}\||=O(N^{L/d})$ (Theorem 3.1). 

2. For the score estimation: 
- In Theorem 3.3, why does the upper bound deriving from Assumption 3.1 (weaker) have a much better dependence of $\log n$ ($(\log n)^{-dL}$ v.s. $(\log n)^{\Omega(1)}$) over the upper bound deriving from Assumption 3.2 (stronger)? Also, the former error term $(\log n)^{-dL}$ decreases exponentially fast as the data dimension or sequence length increases, which seems unreasonable. 
- In Theorem 3.3, for the upper bound deriving from Assumption 3.2, $\nu_3=O(L/d)$, which gives $N=n^{\Omega(d/L)}$, $t_0 \sim O(n^{-d/L})$ and $\log (1/t_0) = \Omega(d/L\cdot\log n)$. This term can be merged into the subsequent polynomial dependences in data dimensions and sequence lengths (i.e. $d^{14}L^4$), and hence introduces no singularity. However, the power of $1/n$ is approximately $1/(\nu_3\cdot d)=\Omega(1/L)$, leading to the vacuous sample complexity estimate given long input sequences. 

3. For the distribution estimation: 
- In Theorem 3.4, there are the same issues raised in the second point of the score estimation, since the upper bounds in Theorem 3.4 and Theorem 3.3 are in similar forms. 

4. It seems that there is no characterization of the model capacity dependence. That is, all the provided estimates do not contain (at least, explicitly) error terms related to $h, s, r$. 

5. Minor issues:
- The notation $s$ denotes both the head size and Hölder smoothness (Definition 3.1). 
- In the caption of Table 1, "... where $L$, $\tilde{L}$ are sequence length of transformer inputs", length ->lengths.

### Soundness
3

### Presentation
2

### Contribution
2
