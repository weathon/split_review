Now I have a comprehensive understanding. Let me write the final review.

The key technical point the harsh critic raises is that CPM's fixed-point equation (Eq. 8) is mathematically equivalent to the EM convergence condition. This is correct — at convergence, the EM algorithm satisfies exactly the same system of equations. The CPM solves it via BFGS minimization of a least-squares objective, while EM uses iterative fixed-point updates. Both converge to the same solution when they converge.

The paper's main framing — that CPM is a "novel" matching framework on Y that is conceptually distinct from both matching on X and matching on Ŷ — is misleading because:
1. CPM and EM share the same fixed-point condition (the paper does not discuss this)
2. CPM matches on estimated $\hat{p}(y|x)$, not on the true $Y$

However, this does not mean CPM has no contribution. The least-squares optimization formulation is genuinely different from EM in how it is solved, and the computational efficiency advantage over feature-matching methods is real.

The core claim that CPM "avoids introducing an additional prediction error" compared to matching on Ŷ is partially valid — CPM uses the full softmax $\hat{p}(y|x)$ rather than hard predictions, which is indeed richer information than the confusion matrix used by BBSL/RLLS. But it still relies on estimated $\hat{p}(y|x)$, not the true label Y, so the framing overstates the advantage.

For experimental advantages: since CPM and EM with calibrated networks share the same fixed-point, the performance differences must be due to optimization behavior (BFGS vs EM iterations). The paper doesn't analyze this.</think>Now I have a thorough understanding of the paper and the key issues. Let me write the final review.

## Summary

The paper proposes a class probability matching (CPM) framework for label shift adaptation, reformulating the problem as matching probability distributions on the label variable Y rather than on the feature variable X or the hard prediction Ŷ. Within this framework, the authors develop the CPMCN algorithm, which estimates the class probability ratio via a least-squares objective (Eq. 11) optimized by BFGS, using calibrated neural networks. The paper provides theoretical guarantees including an identifiability result (Theorem 5.3), estimation error bound (Theorem 5.4), and generalization bound (Theorem 5.5), and demonstrates empirically that CPMCN outperforms existing matching-based and EM-based methods.

## Strengths

- **Clean reformulation with computational advantages over feature-matching**: The CPM framework derives from a principled algebraic manipulation (Eqs. 6–8), showing that the class probability ratio can be recovered by matching K one-dimensional distributions over Y instead of a d-dimensional distribution over X, reducing per-iteration complexity from O(n_p³) to O(n_qK²). Theoretical guarantee is provided by Theorem 3.1, which proves equivalence with feature probability matching. This is a genuine computational advantage for the regime where feature-matching methods like KMM are used.

- **Generalization bound rationalizes use of calibrated networks**: The estimation error bound in Theorem 5.4 decomposes into a bias term (approximation error of the calibrated network) and variance terms. The subsequent discussion in Section 5 connects calibration's role to reducing the bias term, providing a principled explanation for why calibration helps rather than treating it as an engineering trick. The calibration ablation in Figure 3 empirically validates this.

- **Empirical effectiveness**: Table 1 shows CPMCN achieving the best MSE and ACC values across multiple Dirichlet shift parameters on CIFAR100, and Figure 4 confirms its computational efficiency compared to feature-matching methods.

## Weaknesses

### Fatal
None.

### Major

- **CPM shares the same fixed-point condition as EM, which the paper does not acknowledge**: The CPM fixed-point equation (Eq. 8), $p(y) = \mathbb{E}_{x \sim q}\left[\frac{p(y|x)}{\sum_k w_k p(k|x)}\right]$, is mathematically identical to the EM convergence condition from Saerens et al. (2002) and Alexandari et al. (2020). At convergence, the EM iteration $w_y^{(t+1)} \propto \frac{1}{n_q}\sum_i \frac{w_y^{(t)} \hat{p}(y|x_i)}{\sum_k w_k^{(t)} \hat{p}(k|x_i)}$ satisfies exactly the same system of equations. CPM minimizes a least-squares objective (Eq. 11) while EM maximizes likelihood, but both share the same set of population solutions. The paper frames CPM as a "novel matching framework" that is conceptually distinct from both feature-matching on X and prediction-matching on Ŷ, but omits any discussion of this equivalence with EM. This matters because the claimed experimental improvements over EM (Table 1) must then stem from optimization behavior differences (BFGS vs. EM iterations), not from a fundamentally different approach. The paper should explicitly acknowledge this relationship and analyze when/why BFGS offers advantages.

- **Overclaimed distinction from prediction-matching methods (BBSL, RLLS)**: The paper claims CPM "directly matches the probabilities of the label variable Y" (Abstract) and "avoids introducing an additional prediction error in contrast to matching methods predicting Ŷ" (Introduction, line 16). In practice, CPMCN uses estimated $\hat{p}(y|x)$ from a calibrated network (Eq. 10), not the true label Y. This is qualitatively similar to how BBSL and RLLS use the confusion matrix (which is itself a summary of $\hat{p}(\hat{y}|y)$). The accurate distinction is that CPM uses richer sufficient statistics — the full soft predictions $\hat{p}(y|x)$ rather than hard predictions or confusion matrices — not "matching on Y vs. Ŷ." The theoretical analysis honestly captures this through the approximation error term in Theorem 5.4, but the narrative overstates the conceptual distinction.

### Minor

- **Experimental advantage over EM is unexplained**: Given that CPM and EM share the same fixed point, the performance gaps in Table 1 (e.g., ACC 47.47 vs. 43.89 on CIFAR100 α=0.1) require explanation. Without comparing convergence trajectories or analyzing the optimization landscape differences between BFGS and EM iterations, it is unclear whether the improvements reflect genuine algorithmic advantages or implementation details. This is addressable in a rebuttal, but the absence of any analysis weakens the experimental claims.

- **Bound does not depend on shift severity**: The generalization bound in Theorem 5.4 does not depend on the shift magnitude $w^*$ or the condition number of the label shift, which limits its informativeness — in practice, estimation difficulty clearly scales with shift severity. This is a minor issue since even bounds that depend only on sample sizes and approximation error still have value.

- **Calibration benefit claim relies on empirical rather than theoretical evidence**: The argument that BCTS "significantly reduces" the bias term $\inf_{f \in \mathcal{F}} \mathcal{R}_p(f) - \mathcal{R}_p^*$ (Section 5, "Reduction of the Bias Error") is supported only by citing Alexandari et al. (2020), which is an empirical finding, not a theorem. The claim is plausible and empirically validated (Figure 3), but formally stating it as proven theoretical benefit overstates what the theory delivers.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing soft predictions (full $\hat{p}(y|x)$) vs. hard predictions (confusion matrix) within the CPM framework would substantiate the claim that using richer sufficient statistics is the key advantage over BBSL/RLLS.
- A direct convergence comparison between BFGS and EM iterations (convergence trajectory, sensitivity to initialization) would clarify the source of CPMCN's empirical advantage over EM.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that CPM "solves the same system of equations as EM, undermining novelty claims"**: While the fixed-point equivalence is real and important (kept as a major weakness above), the conclusion that novelty is completely undermined is too strong. The least-squares formulation with BFGS optimization is a genuinely different algorithmic approach, and the computational advantage over feature-matching methods is real. The issue is the *framing*, not the absence of any contribution.

- **Harsh critic's claim that KMM comparison is a "straw man"**: The paper compares against the full suite of methods (matching on X, matching on Ŷ, and EM). Including KMM is appropriate for completeness; it is not a straw man just because it is slow. The paper correctly notes it runs >10,000 seconds without producing results and focuses its main comparisons on other methods.

- **Harsh critic's concern about normalization constraint in BFGS**: The paper clearly states post-hoc normalization: "we take the normalized weight $\hat{w}_k / (\sum_{y \in [K]} \hat{w}_y \hat{p}(y))$ as the final estimation" (after Eq. 11). This is standard practice and not underspecified.

- **Strength finder's claim about convergence validation (Figure 1)**: This is a weak strength — a properly formulated optimization problem converging to near-zero loss is expected, not a notable finding.

- **Strength finder's generic claims about "superior empirical performance"**: The performance differences need the caveat that they may stem from optimization differences rather than a fundamentally different method.

## Novel Insights

The most significant insight emerging from the reviews is that the CPM framework occupies an interesting middle ground between feature-matching and prediction-matching methods that is not acknowledged in the paper: the CPM fixed-point equation is mathematically equivalent to the EM convergence condition, placing CPM not as a new category of "matching on Y" but as a reformulation of EM as a least-squares optimization problem solved by BFGS. This reframing has genuine value — it can offer different convergence properties and connects label shift estimation to optimization in a way that EM's iterative approach does not — but the paper would be stronger if it acknowledged this connection and investigated the specific conditions under which BFGS optimization provides practical advantages over EM iterations.

## Suggestions

- Explicitly acknowledge the equivalence between CPM's fixed-point condition and EM convergence, and reframe the contribution as a least-squares optimization formulation with potential practical advantages (e.g., faster/better convergence in severe shift regimes), rather than claiming a conceptually new matching framework.
- Replace the "matching on Y vs. Ŷ" framing with the more accurate distinction: using full soft predictions $\hat{p}(y|x)$ vs. hard predictions/confusion matrices, which is both honest and still a meaningful contribution.
- Add an ablation or convergence analysis comparing BFGS and EM iterations to explain the empirical performance gap.

## Score and Decision

The paper makes a real but incremental contribution: reformulating the label shift estimation problem as a least-squares optimization solved by BFGS, which empirically outperforms EM in some settings. The computational advantage over feature-matching methods is genuine. However, the core novelty claim is overstated — CPM shares the same fixed-point as EM, and the "matching on Y" framing is misleading since CPMCN uses estimated $\hat{p}(y|x)$. The theoretical results are valid but largely restate identifiability already implied by Theorem 3.1, and the bounds don't capture shift severity. The paper is publishable but should be more honest about its relationship to EM and more precise about what distinguishes it from prediction-matching methods.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>