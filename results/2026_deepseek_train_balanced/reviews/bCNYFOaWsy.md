Here is my final consolidated review.

---

## Summary

This paper studies class-imbalanced graph learning (CIGL) from a topological perspective. It formally defines two local topological phenomena — Ambivalent Message-Passing (AMP) and Distant Message-Passing (DMP) — proves theorems showing minority classes are inherently more susceptible to both, and proposes TBA (Topological Balanced Augmentation), a lightweight framework that creates virtual nodes and edges to mitigate AMP/DMP. The method is designed to be orthogonal to and combinable with existing class-rebalancing (CR) techniques. Empirical results on five benchmarks show TBA boosts existing CIGL baselines with negligible computational overhead.

## Strengths

- **Formal theoretical characterization of topology-induced bias.** The paper defines quantifiable AMP and DMP coefficients (Section 2, lines 130–135) and proves Theorem 1 (AMP bias grows polynomially with imbalance ratio ρ) and Theorem 2 (DMP bias grows exponentially with ρ). This formalizes, for the first time, how graph topology itself — not just class sizes — amplifies class-imbalance bias, going beyond prior work that treats topology as a separate issue (ReNode defines influence conflict only on labeled nodes via global PageRank).

- **Demonstrates complementarity with existing class-rebalancing methods.** The paper reports that TBA boosts the best CIGL baseline by 4.1/13.8/5.8 points in balanced accuracy on Cora/CiteSeer/PubMed (line 410) and is tested with six different CIGL techniques and three GNN backbones. Showing that a purely topological augmentation method delivers gains *on top of* reweighting/resampling provides stronger evidence of complementarity than merely matching baselines.

- **Extreme computational efficiency.** TBA introduces only 0.014–0.258% additional nodes and 0.527–3.715% additional edges, and runs in 4.50–31.91 ms per augmentation on a V100 GPU (Table tab:runtime, lines 460–468). This makes practical deployment in training loops feasible and distinguishes it from heavier augmentation strategies (e.g., GraphSMOTE's edge predictor).

- **Theoretical predictions confirmed on real data.** The paper validates on PubMed (Fig. 2, line 189) that minority classes empirically show higher AMP and DMP coefficients (α₁/α₂ = 1.357/0.179, δ₁/δ₂ = 0.040/0.004), confirming the theoretical results on real graphs rather than relying solely on synthetic SBM analysis.

- **Robustness under extreme imbalance.** The performance gain of TBA over Base rises from 8.2 to 18.5 when IR increases from 10 to 20 on Cora (line 424), showing the method's advantage grows rather than diminishes under more severe imbalance — the opposite pattern from standard reweighting/resampling approaches.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No ablation study isolating individual design choices.** The paper compares 0th-order vs 1st-order posterior estimation, but does not ablate the imbalance calibration term (Eq. 5), the quadratic program for γ_v (Eq. 8 vs. a simpler fixed threshold), or the virtual node design (vs. directly adding edges between high-risk and candidate nodes). Without ablations, it is unclear which component contributes most to the gains, and whether simpler alternatives would suffice.

- **No variance reporting for the main experimental results.** The paper only mentions "5 independent runs" for Figure 5 (line 429). The main results (described in lines 406–412 across 3 datasets × 3 backbones × 7 baselines × 3 metrics) report point improvements (e.g., "4.1/13.8/5.8") without standard deviations or confidence intervals. Given the stochasticity in TBA (edge sampling each iteration), readers cannot assess whether reported gains are statistically reliable. The missing tables (parser artifacts) may have contained this information, but the text itself does not reference it.

- **Self-training circularity from using model predictions to generate augmentation signals is not discussed.** TBA uses the model's own prediction uncertainty and predicted labels to identify high-risk nodes and create virtual connections (Algorithm 1, lines 352–364), then retrains the same model on the augmented graph. If the model systematically misclassifies certain minority nodes with high confidence (e.g., minority nodes embedded in majority-dominated neighborhoods), those nodes would have low uncertainty and never be augmented. This failure mode — confidently wrong predictions — is known for GNNs on graphs with strong homophily, but the paper does not analyze it or check how often high-risk nodes actually correspond to AMP/DMP-affected vs. simply ambiguous nodes. The empirical validation (Figures 3 and 4) is suggestive but shown only on PubMed without error bars.

- **Theoretical analysis under SBM assumptions not fully bridged to real graphs.** The theorems (Section 2) assume a stochastic block model with constant intra/inter-class edge probabilities and uniform random labeling. Real citation and co-authorship graphs have heterogeneous edge probabilities, power-law degree distributions, and non-uniform labeling (Planetoid splits). The paper partially mitigates this by empirically validating the theoretical predictions on real data (Fig. 2), but the gap between the theoretical setting and the empirical one could be more explicitly discussed.

### Trivial

- The paper does not discuss scenarios where TBA might underperform (e.g., highly heterophilic graphs, very low label rates, or settings where the classifier's predictions are too poor to provide useful posterior likelihoods). A brief limitations paragraph would strengthen the paper.

## Nice-to-Haves

- An ablation study isolating the calibration term, the quadratic program, and the virtual node design would help identify which design choices are essential.
- Reporting standard deviations for the main results tables would improve reproducibility confidence.
- An analysis of how the set of high-risk nodes evolves across training iterations would clarify whether the augmentation converges to a stable structure.

## Removed Points

These points from the inputs were removed for the following reasons:

- **"Without class rebalancing" framing criticism (harsh critic, Point 1):** The reviewer argues the framing is misleading because TBA "functionally rebalances" through topology. However, the paper is technically correct — TBA does not use reweighting or resampling, the standard definition of class rebalancing. The paper explicitly calls TBA "orthogonal to CR" and demonstrates it boosts CR methods. This is a semantic overreach, not a substantive weakness.

- **Missing tables (harsh critic, Section 4):** The main results tables are loaded via `\input{}` commands that the PDF parser did not process. This is a parser artifact of the review system, not an author error. The original submission includes these tables.

- **Section-by-section design nitpicks (calibration trade-off, 1st-order noise, biased prototypes, edge sampling stability):** These are speculative concerns about design choices that are clearly explained and justified in the paper. The paper explicitly discusses the calibration motivation (lines 235–244) and the choice of 1st vs higher-order estimation (lines 291–305). These do not constitute verified weaknesses.

- **Strength Finder's generic strengths** (e.g., "addressed an important problem"): Removed as generic and not grounded in specific evidence from the paper.

## Novel Insights

None beyond the paper's own contributions. The paper's key insight — that AMP and DMP can be quantified, proven to disproportionately affect minority classes, and mitigated via lightweight topological augmentation without class rebalancing — is clearly presented in the paper itself.

## Suggestions

1. Add an ablation study (even in supplementary material) to isolate the contributions of calibration, the quadratic program for γ_v, and the virtual node aggregation design.
2. Report standard deviations for the main results across multiple runs to establish statistical significance, especially given the stochastic edge sampling.
3. Discuss the self-training circularity and potential failure modes (confidently wrong minority predictions) as a limitation or analyze how often the risk estimation correctly identifies AMP/DMP-affected nodes vs. being misled.
4. Explicitly acknowledge the gap between SBM theoretical assumptions and real graph characteristics, and discuss how the empirical validation bridges it.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>