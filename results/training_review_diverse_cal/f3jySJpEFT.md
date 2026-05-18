Here is the final consolidated review.

---

## Summary

This paper studies the sparse linear contextual bandit problem and proves that the compatibility condition on the *optimal arm's* expected Gram matrix (Assumption 3), combined with the margin condition, is sufficient to achieve poly-logarithmic regret. The authors propose FS-WLasso, a forced-sampling-then-Lasso algorithm, and develop a novel induction-based proof technique to analyze it. They demonstrate that their assumption is strictly weaker than the sets of conditions (anti-concentration, relaxed symmetry & balanced covariance) used in prior Lasso-bandit work achieving similar guarantees, and provide empirical validation on challenging synthetic settings.

## Strengths

1. **Strictly weaker assumption for poly-log regret**: The paper proves that the compatibility condition *only on the optimal arm* (Assumption 3.3) suffices for poly-logarithmic regret, whereas all prior Lasso bandit work with a single parameter setting required additional diversity conditions. This is well-supported by Figure 1 (implication diagram), Table 1 (assumption comparison), and the discussion in Section 2.3 demonstrating that existing conditions imply Assumption 3.3 but the converse does not hold. The fixed-suboptimal-arms counterexample (Experiment 2) provides concrete evidence of practical settings where prior assumptions fail but the proposed condition still holds.

2. **Novel induction-based proof technique**: Section 4.3 introduces a mathematical induction argument that captures the cyclic structure between optimal arm selection and low estimation error — when the estimator is accurate, the optimal arm is chosen frequently, which in turn keeps the estimator accurate. This addresses a genuine technical challenge (dependent data from greedy selections), and the paper clearly identifies and discusses the three main difficulties (initialization, propagation, failure probability accumulation). This technique could be of independent interest beyond this work.

3. **Competitive regret bounds with improvements over prior work**: Theorem 1 achieves \(\mathcal{O}(\text{poly}\log dT)\) regret. In the \(\alpha > 1\) margin case, the bound sharpens the dependence on \(\phi_*\) and \(s_0\) compared to Li et al. 2021 (from \(s_0^2/(\Delta_*\phi_*^4)\) to \(s_0^{1+1/\alpha}/(\Delta_*\phi_*^{2+2/\alpha})\)), and avoids the \(K^4\) factor present in Chakraborty et al. 2023. The paper also shows that forced sampling can be dropped entirely under stronger assumptions (Theorem 2), which is a clean sanity check.

4. **Clear assumption landscape mapping**: Table 1 and Figure 1 systematically compare all distributional assumptions used in the sparse linear bandit literature under the single parameter setting, clarifying which assumptions imply which. This is itself a useful reference contribution.

5. **Empirical validation under challenging settings**: Experiment 2 (Figure 2b) tests the algorithm when suboptimal arms have fixed contexts — a scenario where anti-concentration fails — and the algorithm still outperforms existing methods, confirming practical robustness beyond the theoretical assumptions.

## Weaknesses

### Fatal
None.

### Major

1. **Induction argument's central mechanism is not fully transparent from the main text.** The paper's core theoretical claim — that the compatibility condition on the *expected* Gram matrix of the optimal arm is sufficient for poly-log regret — hinges on an induction that propagates a "good event" forward in time. The induction must bridge from the *expected* compatibility of one specific arm (the optimal arm) to the *empirical* compatibility of a Gram matrix built from a mix of forced-sampling data (uniform over all arms) and greedily selected data, which can include suboptimal arms. Section 4.3 identifies the three difficulties and sketches their resolution at a conceptual level, but the technical machinery that actually executes this bridge (e.g., how the weighted loss function and forced-sampling stage jointly guarantee that the empirical Gram matrix of the *weighted* problem satisfies a sufficient condition for Lasso convergence) is deferred to the appendix. The main text's sketch alone is not detailed enough for a reader to verify the chain of reasoning end-to-end. While this is standard for a conference theory paper, the central reliance on this argument makes it a nontrivial transparency gap.

### Minor

1. **Interpretability of the proposed assumption.** Assumption 3 involves the expected Gram matrix of the *optimal arm*, i.e., \(\Sigma^* = \mathbb{E}[x_{t,a_t^*} x_{t,a_t^*}^\top]\), where \(a_t^* = \arg\max_k x_{t,k}^\top \beta^*\) is defined through the unknown parameter \(\beta^*\). This makes the assumption less transparent than conditions on the average-arm Gram matrix (e.g., \(\frac{1}{K}\mathbb{E}[\sum_k x_{t,k}x_{t,k}^\top]\)), which is a property of the marginal per-arm distributions. A practitioner considering whether to apply the algorithm would need to reason about whether the *optimal arm's* Gram matrix — which depends on the joint distribution of contexts and the unknown \(\beta^*\) — is well-conditioned. The paper would benefit from a brief discussion of why this condition is still natural (e.g., it follows from the margin condition plus mild regularity), rather than leaving the reader to infer this from the implication diagram alone.

2. **Informal theorem statements leave key constants underspecified.** Theorem 1 defines \(\tau\) as "a constant that depends on \(x_{\max}, s_0, \phi_*, \sigma, \alpha, \Delta_*, \log d, \log \delta\)" without giving its explicit form, yet \(\tau\) appears in the expressions for \(M_0\) (via \(\log\log\tau\)) and the weight \(w = \sqrt{\tau/M_0}\). Similarly, the regret bounds involve implicit constants in the \(\mathcal{O}(\cdot)\) notation whose dependence on problem-specific quantities is not fully expanded. The paper acknowledges these are informal statements and defers formal versions to the appendix, but for a theorem statement to be self-contained at the reader's level, the essential functional form of \(\tau\) should be specified.

### Trivial
None.

## Nice-to-Haves

- **Ablation on the exploration length \(M_0\).** The paper mentions that \(M_0\) is tuned as a hyperparameter and is not sensitive to its choice, but only shows one setting in the experiments. A brief ablation study varying \(M_0\) over a range would strengthen the practical guidance, especially since the theoretical expression for \(M_0\) depends on unknown quantities.
- **A concrete worked example showing Assumption 3 does not imply prior conditions.** The fixed-suboptimal-arms counterexample is described in Experiment 2 and Figure 1, but a short formal statement or even a paragraph explicitly demonstrating why this example satisfies Assumption 3 while violating anti-concentration/relaxed-symmetry would sharpen the paper's main selling point.
- **A more self-contained proof sketch (2–3 paragraphs)** explaining (a) how the weighted loss function's Gram matrix relates to the optimal arm's Gram matrix, (b) how the induction's "good event" is formally defined in terms of estimation error bounds and optimal-arm selection counts, and (c) how the failure probabilities are controlled to union-bound over the horizon.

## Removed Points

- **"The proof is deferred to the appendix, so the gap remains" framing of Critical Issue 1** — removed per the rule that parser-stripped appendix content should not be treated as absent. The substantive concern about induction transparency is kept and reframed above under Major weaknesses.
- **"The algorithm is essentially a forced-sampling-plus-Lasso scheme, incremental"** — this is a generic observation about the algorithm class, not a verifiable weakness. The paper's novelty lies in the analysis under weaker conditions, which is a legitimate contribution for a theory paper.
- **"Double probability phrase in Theorem 2"** — removed per the rule that formatting/grammar issues (including repeated phrases) are parser artifacts or minor author errors that carry no weight in evaluation.
- **"The constant regret for \(\alpha > 1\) needs more intuition"** — the paper already discusses this in Section 4.2 (lines 356–360), comparing with Papini et al. 2021. The concern is already addressed.
- **"Missing practical guidance for \(M_0\)" as a weakness** — downgraded to Nice-to-Haves since the paper provides a reasonable response (Remark after Theorem 1: \(M_0\) is tuned as a whole hyperparameter and the algorithm is not sensitive to its choice).
- **Strength Finder's generic strengths** — none were generic; all five strengths had specific citations to figures, sections, or tables in the paper. All retained.

## Novel Insights

The reviewer's framing of the central technical challenge — bridging expected compatibility of one arm to empirical compatibility of a dependent-data Gram matrix — highlights an aspect that the paper's own sketch mentions but does not fully elaborate. The induction argument's interest value lies precisely in this gap: prior work relied on diversity conditions that automatically ensure *every* arm's selections yield well-conditioned Gram matrices, bypassing the dependence issue. This paper's forced-sampling trick plus induction is a specific technical solution to a well-defined difficulty; readers may find it instructive to compare this approach with alternative strategies (e.g., UCB-style optimism or Thompson sampling with sparsity-inducing priors) that also grapple with dependence in high-dimensional bandits but do so through confidence-set construction rather than explicit forced exploration. The relationship between the induction technique here and the "epoch-based" analyses in the explore-then-commit literature (e.g., ESTC) is also worth noting but not explored in the paper.

## Suggestions

1. In the final version, add a 2–3 paragraph self-contained sketch of the induction argument in Section 4.3 that explicitly states the "good event" conditions (estimation error bound + optimal-arm selection count) and explains how the compatibility condition on \(\Sigma^*\) implies that when optimal-arm selections dominate the data, Lasso estimation error contracts.
2. Add a brief discussion (1 paragraph) in Section 2.3 explaining why the compatibility condition on the optimal arm is natural: e.g., it is implied by the margin condition plus a mild regularity condition on the distribution of the optimal arm's features.
3. In the formal theorem statement (appendix or main text), provide an explicit expression for \(\tau\) or at least clarify that it is the solution to a well-defined equation given in the proof.
4. Include a small experiment varying \(M_0\) (e.g., sweep over \(M_0 \in \{1, 50, 100, 200, 500\}\)) to support the claim of insensitivity.

---

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>