- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 8, 3
Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

GTMGC proposes a Graph Transformer that predicts molecular 3D ground-state conformations directly from 2D graphs in an end-to-end manner. The key technical novelty is the Molecule Structural Residual Self-Attention (MSRSA) mechanism, which incorporates the adjacency matrix and a row-subtracted distance matrix as learned residual bias terms on the standard self-attention scores, preserving global attention while encoding local and spatial structure. The model uses MoleBERT tokenization for chemically meaningful atom representations and a two-stage encoder–decoder architecture where the encoder produces a rough conformation whose distance matrix is fed into the decoder for refinement. Experiments on Molecule3D and QM9 report 18–29% improvements over previous methods across distance-based and alignment-based metrics.

---

## Strengths

1. **Novel MSRSA mechanism that preserves global attention while incorporating molecular structure.** Unlike prior work that uses the adjacency matrix as a hard mask (Dwivedi & Bresson, 2020), MSRSA (Section 3.2, Eq. 8–11) incorporates adjacency and distance information as element-wise residual biases on the full self-attention scores. The ablation study (Table 3) shows stepwise C-RMSD improvements of 2.37%, 1.21%, and 3.37% as each bias component is added, with decreasing standard deviation — concrete evidence that each term contributes.

2. **Strong empirical results with large relative improvements.** On Molecule3D, GTMGC reports 18–29% improvements over the previous best method across D-MAE, D-RMSE, and C-RMSD on the random split, and 20–23% on the scaffold split (Table 1). Results on QM9 also show superior performance, demonstrating cross-dataset generalization.

3. **Thoroughly executed ablation studies with uncertainty quantification.** Tables 2 and 3 report means and standard deviations over three runs, systematically isolating the contributions of input format, adjacency bias, and distance bias. The decreasing standard deviation as components are added supports the claim that MSRSA stabilizes training.

4. **Robust generalization to unseen molecular scaffolds.** On the scaffold split (Table 1b) — a harder distribution-shift setting — GTMGC's validation and test metrics remain close, while the previous best method (DeeperGCN-DAGNN) shows a significant performance drop from the random split, suggesting GTMGC avoids overfitting to training scaffolds.

5. **Attention visualization reveals interpretable multi-head behavior.** Figure 4 shows that different heads learn distinct attention patterns — e.g., some heads attend globally, while others exhibit distance-decaying spatial attention — providing qualitative evidence that MSRSA captures chemically meaningful structural information.

---

## Weaknesses

### Fatal

None.

### Major

1. **Main results (Table 1) lack uncertainty estimates, weakening the central SOTA claim.** The paper explicitly reports means and standard deviations over three runs for ablation studies (Section 4.4) but provides only point estimates for the main comparison table. Given that this table is the primary evidence for the claimed state-of-the-art performance, the absence of any measure of variability makes it impossible to assess whether the reported improvements (18–29%) are statistically significant or could arise from a favorable single seed. *Why it matters: the paper's core contribution rests on this table, and the evidence is incomplete without error bars.*

2. **The previous best method (DeeperGCN-DAGNN) was not re-implemented under the same experimental conditions.** The paper states: "Except for the results obtained from the original benchmark paper (Xu et al., 2021d) for DeeperGCN-DAGNN, all other findings presented in this study are derived from our experiments" (Section 4.3). This introduces uncontrolled confounds — different train/validation splits, data preprocessing, hyperparameters, and seeds — that could systematically inflate the apparent improvement. The authors *did* re-implement GINE, GATv2, and GPS, so adding one more model is not prohibitive. *Why it matters: the evidence for outperforming the previous SOTA is not demonstrated under fair, apples-to-apples conditions.*

### Minor

1. **Limited analysis of decoder sensitivity to the bootstrapped distance estimate D_cache.** The paper acknowledges that the row-subtracted distance matrix used by the decoder is "not sufficiently precise as it is derived from preliminary rough estimates" (Section 4.4) and notes that using the true distance matrix yields superior results. However, there is no analysis of how the final prediction degrades as a function of the encoder's initial estimate quality. Understanding this sensitivity would strengthen confidence in the iterative design.

2. **Baseline implementation details are absent from the main text.** The paper reports results for GINE, GATv2, and GPS but provides no details in the main text about how these models were configured (number of layers, hidden dimension, training hyperparameters, whether the same splits were used). While these details may be present in the appendix (which is not available to this review), the main text should at minimum reference where they can be found.

3. **No discussion of absolute error magnitude in chemical context.** The reported C-RMSD values (~0.35 Å) represent sub-ångström errors. The paper does not discuss whether a 0.05 Å improvement on a 0.4 Å baseline is chemically meaningful — e.g., how these errors compare to DFT accuracy or thermal motion — which would help readers gauge practical impact.

### Trivial

None.

---

## Nice-to-Haves

- **Contextualize the absolute error values.** A brief comparison of the achieved C-RMSD (~0.35 Å) to typical DFT uncertainties or thermal vibrations at room temperature would help readers assess real-world significance.
- **Analyze decoder sensitivity to D_cache quality.** A correlation plot between encoder prediction error and final error, or a perturbation experiment on D_cache, would strengthen the iterative refinement argument.

---

## Removed Points

The following points from the input reviews were identified as not belonging in the main weaknesses list and are recorded here for transparency:

- **Notation nitpick about 𝔼_n for the all-ones matrix (Harsh Critic, Eq. 9–11 comment):** The paper uses 𝔼_n to denote the all-ones matrix in Eq. 11; this is a standard convention (the identity of the matrix is clear from context and the surrounding text explains it as "an unobscured mask"). This is a trivial notation preference, not a substantive weakness.
- **Claim that MSRSA is not a "strong conceptual contribution" (Harsh Critic):** This is a subjective judgment rather than a verifiable weakness. The paper provides empirical evidence (Table 3) for why the D_row-sub formulation works, which is an acceptable level of justification for a design choice.
- **RDKit comparison framed as a "sanity check" (Harsh Critic):** The paper lists RDKit (DG, ETKDG) among several baselines and does not overstate the comparison; it is standard and informative to include widely-used classical methods for context.
- **Question about potential inconsistency in Eqs. 9–11 (Harsh Critic):** The reviewer ultimately concludes the derivation is consistent. There is no factual error to flag.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the strengths (MSRSA mechanism, thorough ablation, strong relative improvements) and the weaknesses (missing error bars on main results, unreproduced previous SOTA baseline). No genuinely novel observation emerged from synthesizing the reviews that the paper itself does not articulate.

---

## Suggestions

1. **Run the main experiments (Table 1) with at least 3 random seeds and report means ± standard deviations for all metrics.** This is the single highest-leverage change and directly addresses the most serious weakness.
2. **Re-implement DeeperGCN-DAGNN under the same experimental pipeline** (same splits, preprocessing, seeds) as the other baselines. If computational resources are constrained, at minimum demonstrate that the validation metric from the re-implemented model matches the published value.
3. **Add a brief sensitivity analysis** showing how the final C-RMSD varies with the quality of the encoder's initial D_cache estimate (e.g., by injecting controlled noise into D_cache or stratifying results by encoder error).
4. **Include a sentence contextualizing the absolute error magnitude** (e.g., "A C-RMSD of ~0.35 Å compares to typical DFT errors of X Å" or "this level of accuracy is sufficient for downstream tasks such as Y").
5. **Ensure baseline configuration details** (architecture sizes, optimizer, learning rate, epochs) are clearly stated either in the main text or explicitly referenced to an appendix section.

---
