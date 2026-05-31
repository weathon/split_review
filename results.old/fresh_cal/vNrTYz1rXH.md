Now I have verified all claims systematically. Let me produce the final consolidated review.

---

## Summary

This paper introduces "dependence shift" — a novel type of distribution shift capturing variation in the correlation between sensitive attributes and class labels across domains — and proposes FDDG, a framework that trains a disentangled transformation model to map instances between domains, then generates synthetic domains with varied style and dependence patterns to learn a fairness-aware invariant classifier. The paper provides theoretical bounds connecting fairness across domains (Theorem 1) and a duality-gap guarantee (Theorem 2), and reports experiments against 17 baselines on 4 benchmarks.

## Strengths

- **Novel formalization of dependence shift.** Definition 2 (Sec. 2) formally defines dependence shift as variation in ρ(Y⁑, Z⁑) across domains. Prior fairness-aware DG work (Pham et al., 2023) addressed covariate shift but assumed constant fairness dependence. This extension to the shift taxonomy is genuine and well-motivated through the illustrative example in Figure 1 and the running example (Dog/Cat with Grass/Couch).

- **Coherent method design directly operationalizing both shift types.** The two-stage approach (train transformation model T on source domains → generate synthetic domains with randomly sampled sensitive factors **a**∼𝒩(0,Iₐ) and style factors **s**∼𝒩(0,Iₛ) → train invariant classifier via the empirical dual in Eq. 8) provides a concrete mechanism for handling both covariate and dependence shifts simultaneously. This is a principled departure from prior disentanglement-based DG methods (MBDG, DDG) that only randomize style.

- **Ablation analyses validate individual components.** Table 4 (though embedded as an image) tests three ablated variants: removing the sensitive factor from the encoder (w/o sf), skipping synthetic-domain augmentation (w/o T), and omitting the fairness constraint (w/o fc). The degradation observed from each variant supports the paper's claim that all three design choices — three-factor disentanglement, transformation-based augmentation, and fairness regularization — contribute.

- **Theoretical bounds provide formal grounding.** Theorem 1 bounds target-domain fairness in terms of source-domain fairness plus Jensen–Shannon divergence terms, showing that near-fair source classifiers remain near-fair in unseen domains provided distributional distances are controlled. Theorem 2 provides a data-dependent duality gap bound. While these bounds share limitations common to domain generalization theory (discussed below), they go beyond what prior fairness-aware DG methods offered.

## Weaknesses

### Fatal

None.

### Major

- **No measures of uncertainty in experimental results.** The paper reports point estimates without standard deviations, confidence intervals, or distribution statistics across runs. This is a significant omission for a domain generalization paper, where results across random seeds and domain splits are known to be noisy. The tables show "bold is the best; underline is the second best" but the text does not indicate whether results are averaged over multiple trials. Without variance information, the reported improvements (e.g., 8% DP on YFCC) cannot be assessed for statistical significance. Readers cannot tell whether these gains reflect a reliable advantage or an outlier from a single run.

- **Inconsistency between the formal fairness definition and the reported DP metric.** Definition 1 (lines 36–42) defines ρ(Ŷ, Z) = 0 as perfect fairness: "Strictly speaking, a classifier f is fair over subgroups if it satisfies ρ(Ŷ, Z) = 0." However, line 184 states: "A value of DP closer to 1 indicates fairness." The numerical DP values reported in the tables (ranging ~0.9–1.0 for all methods) cannot correspond to the raw ρ metric from Definition 1. The paper never explains what transformation is applied (e.g., 1 − |ρ|, or a normalized variant), leaving the quantitative DP claims uninterpretable in absolute terms. While relative comparisons between methods remain valid if the same transformation is applied uniformly, the reader cannot connect the reported numbers to the formal constraint the method is designed to satisfy.

### Minor

- **Theoretical bounds are of limited practical utility.** Theorem 1 bounds target-domain fairness using JS-divergences between target and source distributions — but the target distribution is unseen, so the bound cannot be computed or used to guide algorithm design. The duality gap bound (Theorem 2) depends on the approximation error ξ (the ∞-norm gap between f and its parameterized counterpart) and a VC-dimension term; no estimates or simplifications are provided. These limitations are standard for generalization bounds in domain generalization, but the paper's language framing them as "interpretable" (line 21) slightly overstates their practical reach.  
  *Counterpoint*: The paper is not alone in this — essentially all DG generalization bounds share this limitation. The contribution here is extending existing bounding techniques (Robey et al., 2021) to handle the fairness constraint, which is a valid theoretical contribution.

- **Strong assumptions about the transformation model and latent factorization are not stress-tested.** Assumptions 1 and 2 posit that a single transformation model T can map any instance from any source domain to any target domain, and that content and sensitive factors are completely invariant across domains. The paper acknowledges these follow prior work (Robey et al., 2021; Zhang et al., 2022) but does not discuss failure modes (e.g., content leakage, incomplete disentanglement) or test how performance degrades when assumptions are violated. The ablation study removes components but does not probe the boundaries of the assumptions.

- **Details of the FC baseline augmentation are not described.** The paper adds "FC" (fairness constraint) to DDG and MBDG (DDG-FC, MBDG-FC) but specifies neither how this constraint is imposed (e.g., penalty weight, Lagrangian formulation) nor how it was tuned. These are two baselines among 17, but they are the closest ablations for isolating the benefit of FDDG's synthetic-domain generation versus simpler fairness regularization.

### Trivial

- The paper defers "a detailed description of the experimental settings (including datasets, baselines, evaluation metrics, etc.)" (line 184) due to space limits. While this is acceptable, the main paper should either define the DP→1 transformation or commit to reporting the raw ρ throughout for self-containedness.

## Nice-to-Haves

- A controlled experiment isolating the effect of modeling dependence shift vs. covariate shift alone — e.g., comparing FDDG against a version that randomizes style but keeps sensitive factors fixed (rather than randomizing both), which would cleanly attribute the benefit to dependence-shift handling.
- A diagnostic experiment on a synthetic dataset with known ground-truth ρ(Y⁑, Z⁑) across domains, tracking how well the learned classifier's fairness tracks the worst-case bound from Theorem 1.
- Brief discussion of limitations: when might the T-model assumptions break, and how does the method degrade?

## Removed Points

These points were considered but removed with justification:

1. **AUC definition is "confusing" or "garbled"** — REMOVED. The paper's AUC definition on line 184 is a standard fairness-adapted AUC based on the Mann-Whitney U statistic (Calders et al., 2013; Zhao & Chen, 2019): perfect fairness corresponds to AUC=0.5, meaning prediction distributions are indistinguishable between sensitive groups. The paper cites the relevant references and the description is correct. The reviewer's confusion does not reflect a paper error.

2. **Baseline comparison is "not fairly staged"** — PARTIALLY REMOVED. The critic speculates that FC baselines use a "naive penalty term" while FDDG uses constrained optimization, but FDDG's empirical dual (Eq. 8) is itself a Lagrange multiplier approach structurally similar to penalty-based methods. Moreover, FDDG is compared against 17 baselines including dedicated fairness methods (EIIL, FarconVAE, FATDM) that do not suffer from this concern. The remaining kernel — that DDG-FC/MBDG-FC implementation details are underspecified — is kept under Minor weaknesses.

3. **Criticism about theoretical bounds being "more one of labeling than of novel machinery"** — REMOVED as it is an opinion about contribution size rather than a verifiable weakness. Extending existing bounding techniques to a novel problem setting with additional constraints is standard practice in theory papers.

4. **Claim that "the novelty here is adding dependence shift and the transformation model" is overclaimed** — REMOVED. The paper states "to our knowledge, we are the first" (line 25), which is appropriately hedged. The contribution statement accurately describes what is new.

## Novel Insights

The reviews do not surface a genuinely novel observation beyond the paper's own contributions. The dependence shift concept is the paper's central insight, and the reviews largely orbit it without adding new analytical perspective.

## Suggestions

1. **Clarify the DP metric.** In the main paper (not just an appendix), state explicitly: "We report DP as [1 − |ρ|] (or whatever the transformation is), where 1 indicates perfect demographic parity." This single line would resolve the central presentation issue.

2. **Add measures of uncertainty.** Report results averaged over ≥3 random seeds with standard deviations for all tables. If space is a concern, a compact format (e.g., "0.94±0.02") is standard.

3. **Provide a limitations paragraph.** One paragraph discussing when the strong assumptions (perfect T, complete factor invariance) might fail and how the method degrades would strengthen the paper's scientific rigor.

4. **Specify the FC baseline protocol.** A sentence in the experimental setup describing how the fairness constraint is added to DDG/MBDG baselines would improve reproducibility.

## Score and Decision

This paper makes a genuine contribution — the dependence shift formalization and the FDDG method are both novel and well-motivated. The method is principled, the theory provides grounding, the ablation studies validate the design, and the empirical scope (17 baselines, 4 datasets) is substantial. The weaknesses are real but not fatal: the DP metric inconsistency is a presentation issue that can be fixed with one clear sentence, the missing variance is a reporting gap that is standard to address in a camera-ready version, and the assumption/limitation discussion is a common space-constrained shortcoming. The core claims (dependence shift is a meaningful new problem dimension; FDDG's approach of generating synthetic domains with varied dependence patterns is effective) are supported by the evidence presented.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>