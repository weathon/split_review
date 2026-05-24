Now I have a thorough understanding of the paper and can verify each claim. Let me compose the final consolidated review.

## Summary

This paper proposes an unsupervised OOD detection method that computes a k-NN density estimate on the intermediate embeddings of a neural network trained with label smoothing, then aggregates these estimates across layers to produce an OOD score. The paper provides finite-sample theoretical guarantees for using k-NN radius for OOD detection, a result (Proposition 1) providing intuition for why the Label Smoothed Embedding Hypothesis improves the method, and experimental results on several image datasets showing competitive performance.

## Strengths

1. **Clear, well-motivated method with practical advantages.** The paper identifies a genuine limitation of softmax-based OOD detection (inability to distinguish epistemic from distributional uncertainty) and proposes a simple alternative: use k-NN density on intermediate embeddings with label smoothing. The method is unsupervised, requires no OOD validation set, and has no tunable hyperparameters that depend on OOD data — all significant practical advantages over methods like ODIN or POEM.

2. **Provides new finite-sample guarantees for k-NN in the OOD detection context.** Theorem 1 and Corollary 1 (Section 3.1) give high-probability bounds on recall and precision that hold uniformly over the input space. While the techniques build on prior work (Dasgupta & Kpotufe 2014), deriving guarantees specifically for OOD detection (identifying points with f(x)=0, bounding false positives by density) is a new application of these tools. The paper transparently acknowledges the relationship to prior work (Section 5, lines 210).

3. **Theory and empirical evidence that label smoothing improves k-NN OOD scores.** Proposition 1 formalizes how a contraction mapping (consistent with the Label Smoothed Embedding Hypothesis) increases the ratio of k-NN distances between OOD and ID points. Figure 1 provides visual evidence of this contraction effect, and Table 1 confirms that k-NN(0.1) nearly always outperforms k-NN(0) across a range of dataset pairings, directly supporting the claim.

4. **Competitive experimental results including against an advantaged baseline.** Table 1 shows the proposed method (k-NN(0.1)) achieves the highest ROC-AUC on the most dataset pairings, outperforming Control, Robust k-NN, SVM, Isolation Forest, and POEM — the latter despite POEM having access to an external outlier pool that the paper honestly describes as an "unfair advantage" (Section 4.2, line 170).

5. **Thorough ablation studies providing practical guidance.** Section 4.4 systematically examines the impact of k, label smoothing amount α, and choice of intermediate layer. The results support clear defaults (k=1, α=0.1) and show the penultimate layer is often a good choice, which is useful for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between theoretical conditions and practical usage.** The theory (Theorem 1, Corollary 1, Theorem 2) requires k ≥ 2^8·log(2/δ)^2·d·log n. For d=256 (DNN hidden layer dimension) and n=50,000, this lower bound is on the order of several thousand neighbors, yet the method uses k=1 by default (Section 4.1, line 151) and the ablation in Figure 2 shows k=1 performs best. This is a genuine gap: the theoretical regime (large k growing with n) does not match the operational regime (k=1). The paper does not discuss this discrepancy or explain why the theory might still be informative when its core condition is violated.

2. **Theoretical results do not directly cover the actual algorithm.** The theory (Theorems 1-2) is stated for the raw k-NN radius r_k(x) under a direct threshold on that radius in the original feature space. The proposed method uses a normalized, layer-aggregated statistic T̂(x) = (1/M) Σ_i r_k(g_i(x); g_i(X_in)) / Q̂(X_in, g_i) (Section 2, Eq. 67). The normalization Q̂ changes the scale per layer, and the aggregation mixes layers. The paper provides no argument — formal or informal — that the guarantees for raw r_k carry over to the normalized, multi-layer statistic. The theory therefore does not logically support the algorithm as evaluated. This is not fatal because the theory still provides general motivation for using k-NN radius as a density proxy, but the paper should either adjust the method to match the theory or extend the analysis.

### Minor

3. **Absence of several standard OOD detection baselines.** The evaluation omits ODIN (Liang et al., 2017), Mahalanobis distance (Lee et al., 2018), and Energy-based detection (Liu et al., 2020) — widely-used benchmarks in the OOD literature. The paper's claim that the method is "competitive across a variety of datasets" (Table 1 caption) would be significantly strengthened by including these standard baselines. DeConf (which builds on ODIN) is included but performs unexpectedly poorly, making the omission of the original methods more conspicuous.

4. **Ambiguity about which model's embeddings are used for SVM and Isolation Forest baselines.** The paper says these baselines "leverage the same intermediate layer representations as our method" (line 186), suggesting they use embeddings from the label-smoothed model (α=0.1). If so, the comparison isolates the density estimator and is fair. However, Table 1 shows k-NN(0) and k-NN(0.1) as separate rows, while SVM and IF are listed without an α parameter, making it unclear whether they use the α=0 or α=0.1 model's embeddings. This should be explicitly stated.

5. **Proposition 1 is a heuristic illustration, not a rigorous justification for actual label smoothing.** The mapping φ in Proposition 1 is a *postulated* contraction transformation, not derived from actual label-smoothing training dynamics. The paper is transparent about this (line 120: "we provide some theoretical intuition") and does not overclaim, but the proposition does not constitute a theoretical guarantee that label smoothing *in practice* improves OOD detection.

6. **Unexpectedly poor DeConf performance without verification.** The paper reports that DeConf "routinely did worse than the simple control" (line 186) and that tuning its perturbation hyperparameter never helped (line 164). While the paper is transparent about this, when a baseline performs far below published expectations, verification against the authors' released code would strengthen confidence that the implementation is correct.

### Trivial
None.

## Nice-to-Haves

- **Report per-entry standard errors** in Table 1 rather than just aggregate statistics (mean/median/max). The max standard error of 0.0727 is meaningful for bolded entries near the decision boundary.
- **Include a version of k-NN without label smoothing on the same embeddings** used by SVM/IF to isolate the effect of the density estimator from the effect of label smoothing.
- **Discuss the computational cost** of storing all training embeddings and performing nearest-neighbor lookups at test time. The paper mentions "10k CPU hours" but does not address scaling to larger datasets or inference cost.

## Removed Points

These points were flagged for removal due to the filtering guidelines; treat them with caution.

- **"The DeConf result is inconsistent with published performance"** — The critic asserts this without evidence. The paper transparently reports its finding and acknowledges surprise. Without access to the authors' implementation, this is speculation, not a verifiable weakness.
- **"Missing related works"** — Removed per instructions (cannot independently verify external sources).
- **"Reproducibility: list exact layer indices"** — The paper specifies that it aggregates over "3 layers for the DNN and 4 dense layers for LeNet5, including the logits." For a 3-layer DNN (256-256-logits), this is unambiguous. For LeNet5, the description is sufficient for a systems paper and the critic's concern is a minor specification detail inflated to a weakness.
- **"Reproducibility: Q estimation for test queries"** — The paper clearly describes leave-one-out estimation on the training set for Q̂. For test queries, the full training set is used (since the test query is not in the training set). This is standard and adequately described.
- **"Figure 1 caption references panels not described"** — The caption describes the figure's content adequately. This is a parsing/style nitpick.
- **"Assumption 1 is strong, not discussed for learned embeddings"** — This is a generic concern about any theory paper that uses smoothness assumptions; the paper is following the standard practice in k-NN density estimation theory.
- **Strength Finder strength about "ranking preservation result"** — Merged into strength 1 as it is part of the same theoretical contribution.
- **Generic Strength Finder claims about "important problem"** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The two most interesting points emerging from the reviews are: (1) the tension between the theory (which requires large k) and the empirical finding (k=1 works best), which suggests the theoretical analysis may not capture the right mechanism, and (2) the fact that the paper's primary contribution may be more empirical than theoretical — demonstrating that simple k-NN density on label-smoothed embeddings is a strong OOD detector — but the paper tries to frame it primarily through a theoretical lens. A future version that acknowledged this tension and focused on the empirical findings while modestly positioning the theory as motivation would be stronger.

## Suggestions

1. **Address the theory-practice gap explicitly.** Either adjust the method to use raw k-NN radius (without cross-layer normalization) and apply the theoretical threshold, or adapt the theoretical analysis to cover the normalized, aggregated statistic. At minimum, discuss why the theory's requirements (large k) differ from practice (k=1) and what this means for interpreting the theoretical results.

2. **Clarify which model produces the embeddings for SVM and Isolation Forest.** Add a sentence explicitly stating whether these baselines use the base model (α=0) or the label-smoothed model (α=0.1), and consider adding a comparison of all embedding-based methods on both models' representations.

3. **Add standard OOD baselines** (ODIN, Mahalanobis, Energy-based detection) to the experimental comparison to better position the method against the broader literature.

4. **Verify the DeConf implementation** against the authors' released code, or note the discrepancy more cautiously. If the implementation is correct, report this as an interesting finding about the sensitivity of DeConf to architectural choices.

5. **Report per-entry standard errors** in Table 1 to allow readers to assess variance for individual dataset pairings, especially near decision boundaries.

## Score and Decision

**Overall assessment:** The paper proposes a sensible, well-motivated method with competitive empirical results and provides theoretical context for why k-NN density works for OOD detection. However, the theoretical framing has a significant disconnect from the actual algorithm (normalized, aggregated statistic vs. raw k-NN radius with a specific threshold), and the theoretical conditions (large k) are incompatible with the practical regime (k=1) that works best empirically. Additionally, the evaluation would be substantially stronger with standard baselines (ODIN, Mahalanobis, Energy) and a clearer statement of which model's embeddings are used for embedding-based baselines. The paper's core empirical finding — that k-NN density on label-smoothed embeddings is a practical and competitive OOD detector — is interesting and potentially valuable, but the presentation overstates the theoretical contribution relative to its actual scope. A major revision is needed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>