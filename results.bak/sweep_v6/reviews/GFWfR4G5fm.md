Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper identifies three fundamental limitations of static pre-training in Supervised Causal Learning (SCL)—fragility under distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap—and proposes Test-Time Training for SCL (TTT-SCL) as a remedy. The core idea is to dynamically generate a training set aligned to each test instance using an Alignment of Distribution (AD) metric with sparsity constraints. The instantiation, TACTIC, performs stochastic graph refinement guided by the AD+sparsity score, generates training data from the discovered graphs, and trains an SCL model on this data to predict the test graph. Experiments on synthetic, pseudo-real, and real-world datasets (Sachs, SynTReN) show TACTIC substantially outperforming existing SCL and traditional methods, notably on Sachs (78.9 AUROC vs. AVICI's 62.3).

## Strengths

- **Rigorous empirical diagnosis of static SCL limitations.** Section 3.2 provides clear quantitative evidence for all three claimed issues (Figure 2, Table 1), including the finding that SCL models fail on compositional generalization even when trained on all individual components—going beyond prior work that attributed drops only to unseen components.

- **Principled alignment metric with proven necessity.** The AD metric (Eq. 3) combined with sparsity (Eq. 4) is ablated cleanly in Table 3: removing the sparsity term consistently degrades performance across all settings (e.g., Sachs drops from 78.9 to 63.5 AUROC), validating that both components are required.

- **Demonstrated two-stage improvement over score-based search.** Table 4 traces performance from seed graph → highest-scoring graph in TACTIC's search → final SCL output. The consistent gain after the supervised learning phase (e.g., Sachs: 66.6 → 78.9) directly supports the claim that TACTIC's pipeline offers added value beyond classical score-based search, and shows the learning phase matters even when the search alone gives only modest improvement.

- **State-of-the-art results on real and pseudo-real data.** In Table 2, TACTIC (Notears) achieves 78.9 AUROC on Sachs and 80.1 on Syntren, outperforming all baselines including the strongest SCL baseline AVICI (62.3 and 65.4). This provides direct evidence that the test-time alignment approach transfers to realistic, non-synthetic domains.

- **Consistent superiority across multiple evaluation metrics and additional benchmarks.** The paper reports that conclusions hold for AUROC, AUPRC, F1, and ACC (Appendix D), and extends to four additional bnlearn benchmarks (Appendix G), showing robustness beyond a single metric or dataset.

## Weaknesses

### Fatal
None.

### Major

- **Unspecified SCL training procedure.** The paper states that TACTIC "trains a specialized SCL model" on the generated training set of K=200 instances (Section 4.2) and "We mainly use the AVICI as the model backbone" (Section 3.1). It never clarifies whether (i) the model is trained from random initialization, (ii) the pre-trained AVICI checkpoint is fine-tuned, or (iii) a different initialization strategy is used. This is a critical methodological detail: training a deep transformer from scratch on only 200 instances (each a full dataset matrix) is a very different regime from fine-tuning a pre-trained model. The paper's central experimental results cannot be properly interpreted or replicated without this specification. This is the single most important weakness and must be resolved (if it is fine-tuning, comparison to other fine-tuning baselines would also be needed).

- **No standard deviations reported for real and pseudo-real datasets.** In Table 2, results for Sachs and Syntren are reported as single numbers without standard deviations (unlike the synthetic benchmarks). This makes it impossible to assess statistical significance on the datasets where TACTIC's improvements are most striking. Since the method involves stochastic graph refinement and SCL training from generated data, variance estimates are essential for evaluating the reliability of the reported gains.

### Minor

- **Unspecified regression method for the AD score.** The AD metric (Eq. 3) requires fitting conditional distributions \(f_i^k\) from the test data, described as "regress mechanisms via SIM." The specific regression/density estimation method is not stated, and while the paper notes "many ways to implement AD as discussed in Appendix A" (which is stripped), the main text should at least specify whether this is linear regression, a neural network, a Gaussian process, or some other method. This affects reproducibility, though the regression is internal to the method (not a separate evaluation choice), so it does not give an uncontrolled advantage over baselines.

- **Strong claims about "fundamental limitations" are somewhat overblown.** The three issues identified (distribution shift, compositional failure, synthetic-to-real gap) are well-known failure modes of deep learning under domain shift. The paper's experiments confirm expected behaviors rather than reveal surprising new phenomena. The contribution is in the solution (TTT-SCL), not the diagnosis, and the paper would benefit from toning down the novelty claims about the problem characterization.

### Trivial

- The AD metric (likelihood-based scoring) is closely related to standard penalized likelihood scores in causal discovery (BIC, MDL). Explicitly acknowledging this connection would help readers situate the contribution.

- Table 4 reports AUROC without confidence intervals; unclear whether the improvement from highest-score graph to final SCL output is statistically significant for individual datasets.

## Nice-to-Haves

- Include the highest-scoring graph from the search as an explicit baseline in Table 2 (alongside the existing Table 4 analysis) for immediate visual comparison.
- Report computational cost (training time per test dataset) to establish practical feasibility.
- Discuss the transductive nature of the approach—training data is selected based on test data—and its potential for overfitting.
- Compare against a variant that uses the same score-based search but outputs the highest-scoring graph directly (skipping the SCL model), as a direct isolation of the learning stage benefit. (Partially addressed by Table 4, but a dedicated comparison would strengthen the claim.)

## Removed Points

- **"Missing control for highest-scoring graph"** — Removed because the paper already provides this analysis in Table 4 with explicit stagewise comparison. The critic's claim that the conclusion "is not properly tested" is factually incorrect; Table 4 directly compares seed → highest-score graph → final SCL output and demonstrates that the learning phase adds value even when the search alone gives modest gains (e.g., Linear_U: highest-score graph 80.1 is below seed 82.0, yet final SCL output reaches 86.3).
- **"Ambiguity invalidates core experimental claim"** — The core criticism about missing training details is retained (as Major), but the framing that this "invalidates" the paper's entire contribution is removed as excessive. The missing detail is serious but addressable and does not make the results uninterpretable.
- **Strength Finder's generic/superficial strengths** — None of the Strength Finder's claimed strengths were generic or superficial; all were concrete and evidence-based. All kept.

## Novel Insights

Beyond the paper's own contributions, one observation emerges from cross-referencing the reviews and the paper: the stagewise analysis (Table 4) reveals that on Linear_U, the highest-scoring graph from the AD+sparsity search (80.1 AUROC) is actually *worse* than the NOTEARS seed graph (82.0 AUROC), yet the final SCL model trained on the search-discovered graphs dramatically improves to 86.3. This suggests the SCL model is not simply distilling the search results but is learning something genuinely different—perhaps because the AD+sparsity score function is a proxy for graph quality (it measures distributional alignment), and the graphs that score well under this proxy may differ systematically from graphs that score well under AUROC. The SCL model may be learning to extract structure from the data that the score function alone cannot capture. This interesting asymmetry between the optimization target (AD+sparsity) and the evaluation metric (AUROC) is worth deeper investigation.

## Suggestions

1. **Clarify the SCL training initialization.** Specify whether the SCL model is trained from random initialization, fine-tuned from the pre-trained AVICI checkpoint, or uses some other initialization. If fine-tuning is used, add comparisons to other fine-tuning baselines (e.g., directly fine-tuning AVICI on test data via a self-supervised loss). This is the single most important issue to resolve.

2. **Report variance estimates for all datasets**, especially Sachs and Syntren where only single runs are reported. Multiple random seeds for the TACTIC pipeline (graph search + SCL training) would provide needed reliability information.

3. **Specify the regression method** used to fit \(f_i^k\) in the AD computation, or at least state what family of regressors is used (e.g., "linear regression" or "neural network with X layers").

4. **Add the highest-scoring graph from the search to Table 2** as an additional row, so readers can directly compare the search-only baseline against all other methods in the main comparison table.

## Score and Decision

**Calibration Anchors:**

| Path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/split_review/.../ZXs3pkmrRG.md` (TT TTL + causal discovery) | 5.50 | Similar topic (TTT + causal discovery). Our paper has a more novel framework (AD metric, sparsity) and stronger empirical validation on real data, especially Sachs. |
| `/home/wg25r/split_review/.../lQYi2zeDyh.md` (Demystifying amortized CD) | 5.00 | Our paper contributes both diagnosis AND solution, while this one only analyzes limitations. Our empirical scope is broader. |
| `/home/wg25r/split_review/.../wmV4cIbgl6.md` (CausalRivers benchmark) | 7.33 | Substantially different contribution type (benchmark kit vs. method). The empirical scale of CausalRivers is larger, but our paper has more algorithmic novelty. |
| `/home/wg25r/split_review/.../xByvdb3DCm.md` (Selection + Intervention) | 8.00 | Strong theoretical contribution with provably sound algorithm. Our paper lacks comparable theoretical depth. |
| `/home/wg25r/split_review/.../ToveGL9vRN.md` (Faithfulness Fails) | 5.50 | Analysis paper with limited novelty. Our paper has a concrete working method with empirical gains. |
| `/home/wg25r/split_review/.../JzFLBOFMZ2.md` (LLM-supervised CSL) | 3.20 | Much weaker presentation and theoretical issues. Our paper is clearly superior in rigor and clarity. |

The paper makes a genuine contribution—the TTT-SCL framework is novel, the AD metric is well-motivated, and the empirical results on real-world data are compelling. However, the missing detail about the SCL training procedure is a non-trivial gap that prevents full evaluation of the experimental claims, and the lack of variance estimates on the most important datasets weakens the empirical conclusions. The paper sits significantly above the rejected 3–5 range but does not match the theoretical depth or completeness of top-tier accepted papers. Relative to the anchors, this paper is above "Demystifying amortized CD" (5.00) and "Faithfulness Fails" (5.50), comparable to "TICL" (5.50), and below "CausalRivers" (7.33).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>