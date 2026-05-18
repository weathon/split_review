Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes a multi-task framework that jointly learns a DAG-constrained causal structure (via CausalGAE) and an outcome prediction head, sharing a latent representation between both tasks. The goal is to improve out-of-sample generalization for outcome prediction in medical settings. Experiments on synthetic data, three UCI classification datasets, and a survival analysis case study show competitive or superior performance relative to CASTLE and MLP baselines, along with better scalability.

## Strengths

- **Sound core idea with practical motivation.** The paper identifies a genuine limitation of CASTLE (scalability, treating the reconstructed target as the final output) and proposes a principled fix: a graph-autoencoder backbone that scales linearly with features, plus a separate supervised prediction head that leverages the shared representation. This is a natural and well-motivated extension of CausalGAE.

- **Clear scalability advantage.** Table 4 and Figure 1 show that the proposed architecture maintains stable test MSE (~0.31) across d=20 to d=500, while CASTLE's MSE degrades to 1.37 at d=500 and training time grows exponentially. This is a genuine engineering contribution that directly addresses a stated gap in the literature.

- **Competitive causal discovery as an auxiliary benefit.** Table 2 shows that adding the supervised head does not degrade causal graph recovery — SHD is comparable to CausalGAE (13 vs 12 in Case 1; 13 vs 14 in Case 2) and TPR improves (0.73 vs 0.70 in Case 1; 0.72 vs 0.65 in Case 2). This supports the claim that shared representations can benefit both tasks simultaneously.

- **Promising results on the hardest test scenarios.** On the Las Vegas multi-class classification task (Table 5, test AUC 0.73 vs 0.56 for the next best) and the temporal generalization survival scenario (Table 6, Scenario 2: test AUC 0.80 vs 0.63 for CASTLE, 0.53 for MLP), the proposed model shows substantial advantages over all baselines. These are the settings where generalization matters most.

## Weaknesses

### Fatal
None.

### Major

1. **Contradictory reporting of the loss-weight hyperparameter κ.** Section 5 (Experimental setup) states: *"The loss hyperparameter κ is set to 0."* In Equation 5, κ controls the trade-off between the DAG reconstruction loss and the supervised outcome prediction loss — κ=0 means the supervised term has zero weight, and the model reduces to CausalGAE. Yet Tables 1–6 report results from "our model" that are clearly distinct from and better than CausalGAE, and the ablation study (Table 3) treats "Our model" as different from "Causal structure learning only" (essentially CausalGAE). This is a direct internal contradiction. The most charitable reading is a writing error (κ was nonzero in actual experiments), but as published, a reader cannot determine how the model was actually trained. The authors must clarify the true κ settings used per experiment. If κ was indeed nonzero, the experimental setup statement is wrong and must be corrected. This issue alone prevents sound evaluation of the paper's empirical claims.

2. **Missing control ablation: the DAG constraint is not isolated from multi-task learning.** The ablation study (Table 3) compares the full model against "causal structure learning only" and "outcome prediction only," but neither of these ablations controls for the multi-task architecture itself. The critical missing baseline is: *the same architecture (shared encoder + two decoders) but without the DAG constraint* (i.e., unconstrained W, or no acyclicity penalty). Without this, one cannot determine whether observed improvements come from the DAG-constrained causal structure learning or from the more generic benefit of multi-task representation learning (reconstruction + prediction). Since the paper's framing emphasizes *causal* structure learning as the driver of generalization, this gap undermines the central interpretative claim.

3. **No error bars, confidence intervals, or repeated-run statistics for any experiment.** All reported numbers are point estimates (single-run means). Given the small-scale nature of several experiments (500 samples in survival analysis; synthetic data with 1000 samples), results may be sensitive to train/test splits and initialization. Without standard deviations or significance tests, the reader cannot assess whether observed improvements are reliable or within the noise range. This is especially consequential for (a) the survival analysis case study, (b) the ablation study in Table 3, and (c) the Las Vegas dataset where the improvement is large but the run-to-run variance is unknown.

### Minor

1. **Baseline comparisons are adequate for the paper's framing but narrow.** The primary comparison against CASTLE is appropriate and well-motivated. However, the paper would benefit from one additional baseline — a multi-task autoencoder (reconstruction + prediction, no DAG constraint) — which directly addresses the scope question raised in Major #2 above. The requests for IRM, domain-adversarial training, anchor regression, etc. are scope-creep for a method that is fundamentally about leveraging causal structure learning for prediction, not about invariant learning per se.

2. **Real-world classification results are mixed.** On Statlog Heart and Breast Cancer (binary, Table 5), all methods achieve AUC > 0.9 with negligible differences. The method's advantage is only clearly demonstrated on the Las Vegas multi-class task. While this is a valid positive result, the framing implies more consistent advantages than the evidence supports.

3. **Survival analysis case study lacks statistical and clinical rigor.** (a) The dataset has only 500 samples and no confidence intervals are reported. (b) The causal graphs in Figure 2 are presented as evidence of interpretability, but there is no ground truth, no stability assessment (e.g., bootstrap confidence for edges), and no expert validation of the claimed clinical relevance. (c) The observation that different edges appear in different scenarios could equally reflect overfitting to spurious correlations rather than adaptation to "evolving real world scenarios."

4. **Decoder architecture details are underspecified.** The paper states g1 and g2 are MLPs with shared weights across variables and g3 is a projection layer, but does not specify number of layers, hidden dimensions, or activation functions. While some parameters follow Ng et al. (2019), this should be stated explicitly for reproducibility.

5. **No discussion of limitations.** The paper promotes interpretability and generalization but never acknowledges that the method inherits the strong assumptions of CausalGAE (acyclicity, additive noise, no hidden confounders), which are questionable in medical data. A candid limitations paragraph would strengthen the paper.

### Trivial
- The paper contains a duplicated word ("like like" on line 101).
- The notation around X_{(d-1)} and Y in Section 4 is slightly ambiguous and could be cleaned up for clarity.

## Nice-to-Haves
- A sensitivity analysis of κ (how performance varies with different trade-off weights between reconstruction and prediction).
- Comparison against a simple survival model (e.g., Cox proportional hazards) to ground the clinical case study.
- Stability selection or bootstrap confidence intervals for the edges in Figure 2.

## Removed Points
- **"Equation 1 uses e^W but Equation 6 uses W⊙W"** — Removed as factually incorrect. The paper correctly uses W⊙W in both the NOTEARS-style constraint formulation (referenced in text) and Equation 6. The mention of e^M on line 45 is a notation definition.
- **"Missing related works"** — Removed per instructions (cannot verify existence of undiscovered related work).
- **"Weak baselines / missing domain-adversarial training, IRM, anchor regression, ICP"** — Moved to Removed Points. These are methods from a different family (invariant learning / distributional robustness), not causal-structure-based regularizers. Including them would expand the paper into a different scope. The core baseline CASTLE is defensible and directly comparable.
- **"Formatting/style nitpicks"** — Removed per instructions.
- **"Missing appendix/proofs"** — Removed per instructions (parser strips these; they exist in the original submission).

## Novel Insights
None beyond the paper's own contributions. The reviews surface a clear tension: the paper's technical contribution (shared representation for causal structure learning + outcome prediction) is well-motivated and the scalability results are convincing, but the experimental evaluation as presented has two structural gaps that prevent clean attribution of the reported gains to causal structure learning specifically. The κ=0 contradiction is the most pressing — once resolved, the missing DAG-constraint ablation (same architecture without acyclicity penalty) becomes the single most informative experiment the authors could add.

## Suggestions
1. **Clarify κ immediately.** Report the exact κ value(s) used for each experiment (synthetic, real classification, survival). If κ was tuned via cross-validation, say so and report the selected values.
2. **Add the missing DAG-constraint ablation.** Run the full architecture (shared encoder + reconstruction decoder + prediction decoder) with the same optimization but *without* the acyclicity penalty (set ρ=0 or remove the h(W)=0 constraint). If the resulting performance is similar to the full model, the paper's contribution is best framed as multi-task causal-representation learning; if it degrades, the DAG constraint's role is confirmed.
3. **Report mean and standard deviation over multiple seeds** (at least 5) for all key results, especially synthetic data (Tables 1–3), real classification (Table 5), and the survival case study (Table 6).
4. **Add a limitations paragraph** acknowledging the assumptions inherited from CausalGAE (acyclicity, additive noise, no hidden confounders) and discussing when the method might fail.

## Score and Decision

This paper proposes a reasonable and well-motivated extension of CausalGAE with a clear practical advantage (scalability) and promising initial results on temporal generalization. However, the internal contradiction regarding the κ hyperparameter is a barrier to evaluation, and the missing DAG-constraint ablation means the paper's central interpretive claim is not adequately supported. The lack of statistical confidence intervals further weakens the empirical case. These issues are addressable but require additional experiments and corrections that cannot be fully resolved in a rebuttal.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>