Here is the final consolidated review.

---

## Summary

This paper revisits Neighbourhood Components Analysis (NCA), a classical differentiable nearest-neighbor method from 2004, and progressively upgrades it with modern deep learning components (SGD, deep architectures, PLR encoding, stochastic neighborhood sampling, soft-NN inference) to produce MODERNNCA. Evaluated on 300 tabular datasets against 20 methods, MODERNNCA performs on par with CatBoost and outperforms existing deep tabular models (including TabR) while offering competitive training efficiency. The paper's "Occam's-razor" framing — starting from a classical method and adding modern components — yields a clean ablation narrative.

## Strengths

1. **Large-scale, rigorous evaluation**: 300 datasets (120 classification, 180 regression), 20 comparison methods, 15 random seeds per dataset, hyperparameter tuning via Optuna (100 trials), and statistical testing (Win/Tie/Lose with t-tests at 95% confidence, Wilcoxon-Holm critical difference diagrams). This exceeds the typical evaluation scale in deep tabular papers.

2. **Systematic, component-wise ablation**: Table 2 traces performance through five incremental variants (NCAv0→NCAv1→...→NCAv4=L-NCA), with each variant isolating a single change (higher-dimension projection, SGD, log loss, soft-NN prediction). Each modification contributes positively, validating the incremental design methodology.

3. **Stochastic Neighborhood Sampling (SNS) that improves both efficiency and generalization**: SNS (Section 4.2) randomly samples a subset of the training set as neighbor candidates per mini-batch. Figure 3 shows using only 30–50% of the training set yields *better* average rank than using the full set, introducing beneficial stochasticity that acts as regularization — a genuine methodological insight, not just an engineering trick.

4. **Clear success against deep tabular competitors**: MODERNNCA outperforms TabR on 126/300 datasets (ties 102, loses 72) with a simpler architecture and lower training time. This is a practically meaningful result that validates the paper's main thesis.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Inference cost is completely unexamined.** The paper states that inference uses the full training set as the neighbor pool (Section 4.2: "During inference, however, the model resumes the searches for neighbors using the entire training set D"). This means per-query cost scales linearly with dataset size in both time (pairwise distance computation) and memory (storing all training instances). The paper reports training efficiency (Figure 1) but provides no analysis of inference time, memory scaling, or regimes where the method is practical for large datasets. The paper criticizes TabR for "high computational cost" (Related Work) but does not apply equivalent scrutiny to its own inference procedure — TabR at least limits neighbors to K via retrieval. This is a notable omission that should be addressed for a method being proposed as a practical deep tabular baseline.

2. **Ablation studies are conducted on a tiny benchmark (45 datasets), not the full 300.** The paper acknowledges this and cites Ye et al. (2024a) that ranks on this benchmark correlate with the full benchmark, but the evidence for this correlation is not demonstrated within the paper itself. Replicating the main ablation findings (especially the NCAv0→NCAv4 progression) on a larger subset would strengthen confidence.

3. **The distance function change (squared Euclidean → Euclidean) is not systematically isolated.** The transition from NCAv4 to full MODERNNCA involves simultaneously changing architecture, SNS, PLR encoding, and distance function. An ablation isolating the distance function's contribution would be valuable for understanding which design choices drive the gains.

4. **No uncertainty measures reported for average ranks or Win/Tie/Lose counts.** Given that 15 seeds per dataset are used, the paper could report standard deviations or confidence intervals around the average ranks to indicate stability.

### Trivial
- Section 6.1 uses the phrasing "replace the default L-BFGS optimizer used in scikit-learn with SGD" after stating NCAv0 is a PyTorch reimplementation. The paper should clarify what optimizer NCAv0/NCAv1 use (presumably PyTorch's L-BFGS) to avoid ambiguity about whether the framework or the optimizer is changing at NCAv2.

## Nice-to-Haves
- An analysis of where MODERNNCA wins vs. loses against CatBoost — are there identifiable dataset characteristics (size, number of features, proportion of categorical features) that predict outcomes?
- Ablating the SNS sampling ratio's effect while controlling for the effective number of gradient steps, to test whether the regularization story is correct or whether different batch statistics drive the effect.
- Reporting inference time as a function of dataset size to inform practitioners of practical deployment regimes.

## Removed Points
*These points were considered but removed per filtering rules. They are listed only for completeness.*

- **SGD vs L-BFGS confounded by framework change**: REMOVED — the critic argued the ablation compares scikit-learn against PyTorch, but the paper explicitly states NCAv0 is a "re-implementation of the original NCA using PyTorch" (line 182). The framework is already fixed before the optimizer comparison. NCAv0→NCAv1→NCAv2 all operate within PyTorch. The critic misread the ablation design. (Retained only as a Trivial clarity point about optimizer specification.)
- **CatBoost framing as selectively optimistic**: REMOVED — the paper reports 114 wins, 69 ties against CatBoost and uses "on par," which is accurate for a 114-117-69 split (a dead heat). The abstract does not claim to outperform CatBoost; it says "on par." The criticism does not identify a factual error.
- **Generic concerns about evaluation rigor, missing analyses, or speculative confounds**: REMOVED — not concretely anchored to specific paper content or reflect reviewer knowledge gaps.
- **Related works comments**: REMOVED — per hard rules, missing related works cannot be assessed without external sources.
- **Reproducibility nitpicks**: REMOVED — code is provided, method is straightforward.

## Novel Insights
Beyond the paper's own contributions, the most salient cross-review observation is the tension between the paper's clean training-time efficiency story and the complete absence of inference-cost characterization. MODERNNCA uses the full training set at inference time — a design choice that makes it a transparent nearest-neighbor method but one whose practical deployment envelope is unstated. The paper's otherwise strong empirical evaluation would be substantially strengthened by characterizing where it is and is not practical to deploy, akin to how TabR's limitations with neighbor retrieval are discussed in the literature. This is not a fatal flaw, but it is a notable blind spot in an otherwise thorough paper.

## Suggestions
1. Add an inference-cost analysis: report per-query latency as a function of training set size on datasets of varying N, and discuss practical regimes where MODERNNCA is or is not suitable.
2. Clarify the optimizer used in NCAv0/NCAv1 (state explicitly that NCAv0 uses L-BFGS in PyTorch).
3. Replicate the main ablation findings (NCAv0→NCAv4 progression) on a larger subset of the 300 datasets, or provide stronger evidence of rank correlation with the tiny benchmark.
4. Add an ablation isolating the Euclidean vs. squared Euclidean distance change.
5. Report standard deviations or confidence intervals around the average performance ranks across seeds.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>