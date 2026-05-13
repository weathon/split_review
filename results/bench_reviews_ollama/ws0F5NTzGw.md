Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

AdapTable proposes a model-agnostic test-time adaptation framework for tabular data that combines (1) a shift-aware uncertainty calibrator using GNNs over column-level shift trends to produce per-sample temperatures for recalibration, and (2) a label distribution handler that estimates and adjusts for target label distribution shifts. The method requires no updates to the target model's parameters, making it applicable to both deep learning models and GBDTs. Evaluations across six natural-shift datasets, six corruption types, and multiple architectures demonstrate consistent improvements over existing TTA baselines.

## Strengths

- **Well-motivated problem with diagnostic analysis**: The paper convincingly demonstrates why existing TTA methods fail on tabular data — deep tabular models violate the cluster assumption (Figure 1) and label distribution shifts are a primary degradation factor (Section 2.2, Figure 2). This analysis directly motivates the two-component design.
- **Model-agnostic applicability**: Unlike gradient-based TTA methods (TENT, EATA, SAR), AdapTable adjusts only output predictions, enabling application to CatBoost and other GBDTs (Table 1 shows consistent CatBoost gains), which is a practical advantage for real-world tabular deployments.
- **Broad empirical evaluation**: Experiments span 6 natural-shift datasets, 6 corruption types, 4 deep architectures plus CatBoost, and robustness tests under severe class imbalance and temporal correlation (Tables 1–3, Figures 3–5), providing substantial breadth of evidence.
- **Demonstrated label distribution estimation accuracy**: Figure 5 shows low JS divergence between estimated and true label distributions across online batches, confirming the handler works as intended.
- **Computational efficiency**: AdapTable processes HELOC in ~1.54 seconds total and shows favorable efficiency-efficacy trade-off with low hyperparameter sensitivity (Figure 7).

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation isolating the two-stage calibration (Eq. 8 vs. GNN output)**: The GNN calibrator produces continuous per-sample temperatures T_i, but the second stage (Eq. 8) overrides these with a coarse trinary value Ț_i ∈ {T, 1/T, 1} based on quantile thresholds. Without an ablation testing (a) GNN first-stage only, (b) second-stage heuristic only, and (c) full pipeline, it is impossible to determine whether the GNN or the trinary heuristic drives performance. The existing ablation (Table 2) compares only with Platt scaling and isotonic regression — external methods, not internal component isolation. This gap is critical because the two-stage design creates a tension: if the trinary override dominates, the GNN's claimed "shift-aware" contribution may be secondary, undermining the narrative that the GNN is a core innovation.

- **Missing standard label-shift correction baselines**: The paper compares against vision-based TTA methods (TENT, EATA, SAR, etc.) that are poorly suited to tabular data, setting a low bar. However, simpler model-agnostic label-shift correction methods such as BBSE or confusion-matrix-based approaches are natural baselines that share AdapTable's model-agnostic property and directly address label distribution shifts. Their absence leaves open the question of whether AdapTable's more complex pipeline outperforms straightforward label-shift correction alternatives.

- **Calibrator training procedure absent from main text**: The shift-aware uncertainty calibrator g_φ has learnable parameters, but its training procedure (what data it is trained on, when, and how) is deferred to the appendix (Section "adaptable_detail"). Since g_φ is a core method component, this omission makes the main text's method description incomplete. Clarifying whether g_φ is trained on source data (which would make it source-dependent and relevant to the privacy framing) or through some other mechanism is essential for properly interpreting the "no parameter updates" and "model-agnostic" claims. The claim on line 23 that "AdapTable requires no parameter updates" appears to refer to the target model f_θ, not g_φ — but this distinction needs explicit clarification in the main text.

### Minor

- **Inconsistent reported improvement figures**: The abstract (line 8) and introduction (line 25) claim "up to 16% improvement on the HELOC dataset," while Section 4.2 (line 194) states "dramatic performance improvements of up to 26% on the HELOC dataset." These are presented as comparable claims about the same dataset. The discrepancy likely reflects different metrics (F1 vs. bAcc) or different experimental conditions, but this is not explicitly stated, undermining the reliability of the headline results.

- **Unexplained asymmetry between debiased and online estimators**: The debiased estimator p_t^de (Eq. after line 133) uses the original uncalibrated predictions p_t(y|x), while the online estimator p_t^oe (line 135) uses the adjusted predictions p̄_t(y|x). This asymmetry is not discussed or justified. Using calibrated predictions in one but not the other seems inconsistent with the paper's stated goal of using calibration to improve label distribution estimation.

- **No convergence analysis for the online estimator's feedback loop**: Equation 10 (line 135) updates p_t^oe using p̄_t, which depends on p_t, which depends on p_t^oe. While this dependency is sequential across batches (not simultaneous), it creates a potential positive feedback loop: if p_t^oe drifts from the true distribution, the adjusted predictions will reinforce that error. The EMA smoothing factor α provides damping, but the paper provides no analysis of conditions under which convergence is guaranteed or when the estimator becomes unstable. Given that the label distribution handler is the paper's primary contribution, even a brief empirical sensitivity study would strengthen confidence.

- **No batch size sensitivity analysis**: All experiments use a fixed batch size of 64, but the method relies on batch-level statistics (shift trends, quantile computation, label distribution estimation). Performance under smaller batch sizes (relevant for real deployment) is unknown.

- **Fully-connected graph adjacency**: The GNN operates on an all-ones adjacency matrix (line 92), making it effectively a permutation-equivariant set network. The choice of GNN over simpler set-aggregation mechanisms (e.g., attention pooling) is not motivated by comparison.

### Trivial

- The temperature formula T = 1.5 · max_j p_s(y)_j / min_j p_s(y)_j uses an apparently arbitrary 1.5 multiplier with no justification.

## Nice-to-Haves

- Ablation testing the GNN first stage alone vs. the trinary second stage alone vs. the full pipeline
- Comparison with simple label-shift correction methods (BBSE, EM-based approaches)
- Batch size sensitivity experiments (1, 8, 16, 32)
- Clarification and resolution of the 16% vs. 26% improvement figures
- Brief convergence or stability analysis for the online estimator under extreme label shifts

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper's claim of 'revealing' label distribution shifts is overstated since TableShift already identified this"** (Harsh Critic, Section-by-Section): The paper appropriately cites TableShift and positions itself as building on that finding, not claiming sole discovery. This is a framing disagreement, not a weakness.

- **"The shift trend computation requires source data means, compromising the privacy-sensitive motivation"** (implied by Harsh Critic): The shift trend (Eq. 1) uses source column means, which are aggregate statistics, not raw data. This is standard practice in TTA and does not meaningfully compromise privacy. Moreover, TTA methods conventionally require some source statistics (e.g., batch norm statistics).

- **"t-SNE visualizations can create misleading cluster impressions"** (Harsh Critic, Section 2.1): While true in general, the paper uses t-SNE to show a clear qualitative contrast between image and tabular embeddings, which is a reasonable use of the tool. This is not a substantive weakness.

- **"Theorem 1 has undefined terms BSE and Δ_CE"** (Harsh Critic, Section 3.5): These terms are defined in line 155 of the paper (BSE reflects model performance on source, Δ_CE measures feature generalization). The detailed definitions are in the appendix (stripped by parser), not absent. The theorem's definitions are conceptually present in the main text.

- **Strength removed: "Theoretical error bound justifies the label distribution handler"** (Strength Finder): Overstated. Theorem 1 provides a generic bound motivating label-shift correction in general, not AdapTable's specific design choices (GNN architecture, trinary calibration, averaging scheme). Conflating the two inflates the paper's theoretical contribution.

- Strength removed: "Identifies concrete reasons why existing TTA methods fail" inflated to suggest novel discovery. The paper's contribution is more accurately described as building on TableShift's findings and adding the cluster-assumption analysis, not as revealing the label distribution shift problem for the first time.

## Novel Insights

The paper reveals an interesting tension within its own design: the sophisticated GNN-based shift-aware calibrator has its continuous output effectively discretized by a hard trinary rule, raising the possibility that the method's practical gains may stem more from the heuristic second-stage engineering than from the principled shift-awareness mechanism. This tension — between elegant learned representations and coarse post-hoc engineering — mirrors a broader pattern in TTA research, where batch-level statistics and heuristics often compete with learned adaptation modules. Resolving which component matters more would strengthen not just this paper but inform future TTA design choices.

## Suggestions

- **Crucial**: Add an ablation experiment that isolates the two calibration stages: test the GNN's continuous T_i without the trinary override, test the trinary scheme with a fixed (non-GNN) uncertainty measure, and test the full pipeline. This single experiment would resolve the most significant ambiguity about where the performance gains originate.
- Add comparison with at least one simple label-shift correction baseline (e.g., BBSE or EM-based correction from Lipton et al. 2018).
- Reconcile and clarify the "up to 16%" vs. "up to 26%" figures — specify which metric and which experimental condition each number corresponds to.
- Add a few sentences to the main text clarifying that "no parameter updates" refers to the target model f_θ, and briefly describe when/how g_φ is trained.

## Evaluation

**Originality**: The problem setting (TTA for tabular data) is novel, but the method combines several components that individually are not new (temperature scaling, label shift correction, GNNs). The specific combination is new, though the two-stage calibration design raises questions about whether the learned GNN or the heuristic second stage matters more.

**Importance**: TTA for tabular data is a genuinely important and underexplored area with real practical implications. The paper addresses a gap that existing methods fail to handle.

**Claim support**: The empirical results are strong and broad, but the claim that the shift-aware GNN calibrator is a key contributor is not well-supported by ablations. The theoretical contribution is minor (extending a prior theorem to non-uniform source distributions).

**Soundness of experiments**: Evaluation covers diverse settings, but missing critical ablations and standard label-shift baselines weaken the experimental argument.

**Clarity**: The writing is generally clear but has notable gaps (calibrator training deferred to appendix, inconsistent improvement figures, unexplained design asymmetries).

**Value to community**: High — the paper opens a new research direction and provides practical tools for tabular TTA. Even with its limitations, the contribution of demonstrating the viability of label-distribution-aware TTA for tabular data is valuable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>