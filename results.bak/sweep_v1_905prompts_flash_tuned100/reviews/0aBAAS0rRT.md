Now I have thoroughly verified all claims against the paper. Let me write the final consolidated review.

## Summary

This paper proposes SigMap, a wireless localization foundation model with two claimed innovations: (1) a cycle-adaptive masking strategy for self-supervised pre-training of channel representations, designed to prevent shortcut learning from periodic CSI patterns, and (2) a geographic prompt tuning mechanism that encodes 3D building maps via a GNN to produce lightweight soft prompts for parameter-efficient fine-tuning. The method is evaluated on simulated (DeepMIMO O1) and semi-realistic (WAIR-D) datasets, showing consistent improvements over baselines including LWLM, SWiT, CNN, and OMP.

## Strengths

- **Consistent SOTA across multiple settings**: SIGMAP with map outperforms all baselines in single-BS (MAE 1.564 m vs. LWLM's 2.382 m) and multi-BS (MAE 0.673 m vs. LWLM's 0.828 m) localization. The gains hold across both MAE and CDF@1m metrics, and the multi-BS results (84.5% CDF@1m) represent a substantively meaningful improvement for practical localization use.

- **Map-quality ablation cleanly isolates the contribution of 3D geometry**: Table 4's controlled comparison (3D mesh → 2D bird's-eye → no-map) shows that the 2D variant (MAE 1.692 m) retains most of the benefit over no-map (MAE 2.275 m), while the 3D mesh adds further value (MAE 1.564 m). This provides clear evidence that the geographic prompts encode useful topological priors.

- **Impressive parameter efficiency**: Table 5 documents that only 0.085M parameters (0.7% of total) are trained during fine-tuning, with total fine-tuning time of 30 minutes and inference at 0.83 ms/sample. This is practically meaningful for deployment.

- **Cross-scenario generalization**: Results on DeepMIMO O2 (MAE 1.026 m) and WAIR-D with 100 real OpenStreetMap city layouts (MAE 1.880 m) show that the approach transfers to unseen environments. The WAIR-D evaluation, in particular, goes beyond single-scenario testing common in this field.

## Weaknesses

### Major

**1. The "NLoS-aware attention mechanism" — claimed as the key advantage — is never specified in the methodology.**

Equation (11) in §4.2 introduces:
$$\alpha_i = \frac{\exp(\phi(\mathbf{o}_s^{(i)} \cdot \mathbf{W}_{\text{NLoS}}))}{\sum_j \exp(\phi(\mathbf{o}_s^{(j)} \cdot \mathbf{W}_{\text{NLoS}}))}$$

with the statement that "the key advantage stems from our NLoS-aware attention mechanism." However, the variables $\phi$, $\mathbf{o}_s$, and $\mathbf{W}_{\text{NLoS}}$ are never defined anywhere in the paper. This mechanism does not appear in the methodology sections (§3.1–§3.5), in any architectural diagram, or in the task-specific adaptation section (§3.5). It is not the same as the multi-BS attention fusion (Eq. 9), which has a different functional form ($\mathbf{v}^T \tanh(\mathbf{W}_{\text{att}} \mathbf{t}_{\text{cls}}^{(t)})$). Since this mechanism is described as "key" to the reported results but is never properly specified, the reader cannot determine what system is actually being evaluated. A central component of the method is unaccounted for.

**2. The abstract and contributions overclaim "zero-shot generalization" when the experimental setup is explicitly few-shot.**

The abstract states "strong zero-shot generalization in unseen environments" and §1.2 claims "demonstrates strong zero-shot generalization." However, §4.5 explicitly describes "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)" and calls it a "few-shot learning setup." Using ~100 labeled samples per target scenario with task-head fine-tuning is a few-shot or minimal-fine-tuning protocol, not zero-shot. This is a clear discrepancy between what the paper advertises and what it actually evaluates.

### Minor

**3. Headline comparison numbers conflate map-modality benefit with method benefit.**

The paper's headline results (e.g., "34.4% improvement over LWLM") compare SIGMAP with map against baselines that do not have access to map input. The fairer comparison — SIGMAP without map vs. LWLM — shows much smaller margins (~4.5% in single-BS MAE: 2.275 vs. 2.382; ~4.7% in multi-BS MAE: 0.789 vs. 0.828). The paper does transparently include the w/o map variant in the tables, so the data is not hidden. However, the narrative framing inflates the claimed improvement, and the statistical significance of the ~5% margins (without confidence intervals or error bars in the tables) is unclear.

**4. Cycle-adaptive masking evidence is mixed and incomplete.**

Table 3 shows adaptive masking improves MAE (0.673 m vs. 0.753 m for strip-only) and CDF@1m (84.5% vs. 75.3%), but the RMSE is worse than strip-only masking (1.099 m vs. 0.972 m). This inconsistency is not discussed or explained. Additionally, only multi-BS results are reported; no single-BS ablation for masking strategies is provided, making it unclear whether the benefit generalizes. The claim that adaptive masking prevents "shortcut learning" is plausible but not supported by any feature visualization or reconstruction quality analysis.

### Trivial

**5. Figure reference error in §4.4**: The text states "Two-dimensional and three-dimensional map ablations are illustrated side-by-side in Figure 1" — but Figure 1 depicts wireless propagation paths, not ablation results. This appears to be a wrong figure cross-reference.

**6. Delaunay triangulation in 3D is ambiguous**: The paper constructs edges over a node set in $\mathbb{R}^3$ using Delaunay triangulation but does not clarify whether this is a 3D Delaunay tetrahedralization or a projection-based 2D Delaunay on the 3D coordinates. The distinction matters because 3D Delaunay behaves very differently with points on planar surfaces (building facades).

## Nice-to-Haves

- Report confidence intervals or per-run variance for the main tables, since the ~5% w/o-map margins over LWLM may overlap with run-to-run variation.
- Add single-BS ablation for masking strategies to show the generality of the cycle-adaptive claim.
- Provide a concrete algorithm for computing $d_{\text{final}}$ and $j_0$ from cross-correlation, and show example mask patterns on real CSI data rather than schematic stripes.
- Compare against a map-augmented baseline (e.g., a simple method that feeds map features alongside CSI to a standard architecture) to isolate the benefit of the specific prompt mechanism from merely having map information.

## Removed Points

These points are flagged to be removed, treat them with caution:
- "The paper does not cite any prior SSL methods that failed because of periodic shortcuts" — The paper identifies a research gap conceptually; it need not cite specific failures.
- "Figure 3 is not representative of actual CSI data" — The figure is labeled as an illustration/schematic; this is a presentational choice, not an error.
- "Speculation about street-level photography in future work is unwarranted" — Discussing future directions is standard and appropriate.
- "Future work section mentions directions not connected to current contribution" — Future work by definition extends beyond the current scope.
- "Backbone size / pre-training dataset details missing from main text" — These details are in the appendix (stripped by the parser), not absent from the submission.
- "Missing related works" — I cannot verify this without external sources.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the NLoS-aware attention mechanism (Eq. 11) fully in §3.5**, including definitions of all variables ($\phi$, $\mathbf{o}_s$, $\mathbf{W}_{\text{NLoS}}$), its architectural placement, and whether it is part of the backbone, the task head, or a separate module. Show an ablation isolating its contribution.
2. **Correct the "zero-shot" language.** Replace "zero-shot" with "few-shot" or "minimal-fine-tuning" throughout the abstract and contributions (§1.2). If zero-shot results exist without any fine-tuning, report them separately.
3. **Restructure the main comparison** to clearly separate: (a) CSI-only comparison (SigMap w/o map vs. baselines) to demonstrate the SSL pretraining advantage, and (b) map-augmented comparison to demonstrate the map benefit. The headline should reflect the method's own contribution, not the combined method+modality effect.
4. **Provide an algorithm or pseudocode** for computing $d_{\text{final}}$ from cross-correlation and show qualitative examples of the adaptive mask on real CSI amplitudes.

## Score and Decision

**Calibration anchors:**
- *Round 1 (bracketing)*:
  - Low band (<3.5): 7zJDTnogdG (3.33, ECG foundation model), XhdckVyXKg (3.00, wearable sensing), ntSP0bzr8Y (3.00, power systems) — rejected papers with fundamental methodological issues; SigMap is clearly stronger.
  - Mid band (3.5–7.5): 9TClCDZXeh (7.00, Wi-GATr wireless simulation), 29JDZxRgPZ (6.00, EM-GANSim), aefNwingnS (4.40, channel-invariant SSL), 54jmXCHrTY (5.75, SSL theory).
  - High band (>7.5): 7gUrYE50Rb (8.00, EQA-MX), NN6QHwgRrQ (8.00, MAP alignment) — different domains, less relevant.
- *Round 2 (narrowing, bracket 4.5–6.5)*:
  - 7KDuQPrAF3 (6.25, foundation model for error correction codes) — accepted but with limitations (short codes only); SigMap has more complete evaluation but also more structural gaps. SigMap is somewhat weaker.
  - Bmzv2Gch9v (6.75, SmartPretrain for motion prediction) — accepted with clear methodology and thorough evaluation; SigMap has gaps in method specification. SigMap is clearly weaker.
  - 29JDZxRgPZ (6.00, EM-GANSim) — rejected despite decent scores due to methodological concerns; comparable in quality to SigMap.
  - 7ipjMIHVJt (5.25, DASFormer) — rejected, self-supervised pretraining for signal data; comparable quality.
- *Round 1 bracket*: 4.0–6.0. *Final score after narrowing*: **5.0**.

The paper presents two interesting ideas (cycle-adaptive masking, geographic prompt tuning) and consistently strong empirical results. However, the evaluation is undermined by two verifiable structural issues: (1) the "NLoS-aware attention mechanism" attributed as "the key advantage" (§4.2, Eq. 11) is completely unspecified — the variables $\phi$, $\mathbf{o}_s$, $\mathbf{W}_{\text{NLoS}}$ are never defined and the mechanism does not appear in the methodology; (2) the abstract and contributions claim "zero-shot generalization" while the experiments (§4.5) explicitly use a few-shot protocol with ~100 labeled samples. These issues, combined with the inflated headline comparison margins and the mixed evidence for the masking contribution, prevent acceptance in the current form. The paper would benefit from substantial restructuring — specifying the missing mechanism, correcting the generalization claim, and reframing the comparisons to isolate the method's own contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>