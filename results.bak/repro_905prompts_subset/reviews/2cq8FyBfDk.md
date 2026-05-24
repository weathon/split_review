Now let me write the consolidated review.

## Summary

ProteinVista introduces a full-atom 3D CNN for proteins, pretrained via contrastive alignment to ESM-2 embeddings on ~500K AlphaFold2 structures. The model voxelizes heavy atoms into a 5-channel density grid and processes them with a compact 123M-parameter 3D CNN. On three protein–ligand binding benchmarks (transporter-substrate classification, enzyme-substrate classification, and IC50 regression), ProteinVista matches or exceeds ESM-2 (650M parameters) while requiring 5× fewer parameters, ~20× faster inference, and 500× less pretraining data. An ensemble combining ProteinVista and ESM-2 outperforms either alone, and the optimized pipeline surpasses dedicated SOTA models (SPOT, ProSmith-ESP) on substrate prediction.

## Strengths

- **First large-scale, full-atom 3D CNN for proteins with pretraining on 500K structures.** While voxelized 3D CNNs for proteins existed pre-2020 (DeepSite, EnzyNet, 3DCNN_MQA), none were pretrained on hundreds of thousands of structures or combined with modern contrastive objectives. ProteinVista demonstrates that this earlier architectural paradigm can be made tractable and competitive with today's dominant PLM-based approaches. This is a genuine novelty that opens a complementary direction in protein representation learning.

- **Clear compute- and data-efficiency advantage.** ProteinVista (123M params, 20s per 1K proteins on an A100) substantially outperforms ESM-2_650M (650M params, 426s per 1K proteins) in runtime despite similar FLOPs, and was pretrained on 0.5M structures vs. ESM-2's 250M sequences. These efficiency claims are well-supported by the compute comparison (Section 4.3, Figure 3).

- **Demonstrated complementarity with sequence models.** Averaging ProteinVista and ESM-2 predictions yields statistically significant improvements on both substrate classification tasks (McNemar's test p < 10⁻¹³ for TSP, p < 10⁻¹⁷ for ESP). The stratification analysis (Figure 2a–c) further clarifies *when* structural information helps: high sequence identity, high structural similarity, and high AF2 confidence. This goes beyond a simple "better vs. worse" comparison and provides actionable guidance.

- **Substantial outperformance on IC50 regression.** ProteinVista alone achieves R² 0.69 vs. ESM-2_650M's 0.61 on BindingDB, with p < 10⁻³⁰⁴ (Wilcoxon). This task requires fine geometric resolution (binding affinity), and the gap is large enough to make a strong case for the value of explicit atom-level geometry.

- **Comprehensive ablation studies.** Figure 2e quantifies the contribution of multi-view inference (−6.4% R² for single view), contrastive pretraining (+1.0% over Rosetta regression), voxel resolution (−1.1% at 1.5Å), and augmentation strategy, giving a clear picture of which design choices matter.

## Weaknesses

### Major

- **Central comparison uses an identical simple pipeline that may systematically disadvantage the baseline.** Sections 3.1–3.2 compare ProteinVista and ESM-2 using fixed MolFormer embeddings and an identical two-layer head, which the paper acknowledges "likely underestimates for all models the peak accuracy achievable with a fully optimized pipeline" (Section 3.1). However, the paper does not verify whether the relative ordering holds when each model is paired with a pipeline suited to its strengths. ESM-2 may benefit from attention pooling over residues, fine-tuning the ligand encoder, or learned layer weighting — optimizations that could close or reverse the gap. The only optimized pipeline (Section 3.3) fuses *both* models, so it does not isolate ProteinVista's standalone advantage. Without a direct ProteinVista_OP vs. ESM-2_OP comparison, the paper's central claim that "ProteinVista outperforms sequence transformers" is not as well-supported as it could be. This is the most significant weakness.

- **The SOTA comparison (Table 1) uses an ensemble of ProteinVista + ESM-2, not ProteinVista alone.** Table 1 reports ESM-ProteinVista_OP surpassing SPOT and ProSmith-ESP, but this is an ensemble that includes ESM-2. The abstract claims "ProteinVista outperforms sequence transformers" (about standalone PV vs. ESM-2), and the SOTA claim is about the ensemble. These are different claims, but the paper's structure — placing them in adjacent sections and the same table — risks conflating them. The paper would benefit from a direct comparison of ProteinVista_OP (without ESM-2) against these SOTA methods.

- **IC50 regression uses raw IC50 values without specifying log-transformation.** The paper reports IC50 (not pIC50 = −log₁₀ IC50) and does not state whether values were log-transformed. The MSE values (0.86 for ESM-2, 0.67 for ProteinVista) are consistent with raw, not log-transformed, IC50 values. If raw IC50 is used, the metric is scale-dependent and dominated by outliers. This is a standard methodological detail that must be clarified for the results to be properly interpreted.

### Minor

- **The abstract's "outperforms" claim is slightly too strong for the enzyme-substrate task.** On ESP (Table 1), ProteinVista's accuracy (91.8%) is marginally below ESM-2_650M (91.9%), and ROC-AUC (0.951) is below ESM-2_650M (0.955). The paper's own language in the Discussion ("outperforms or matches") is more accurate. The title's formulation ("Outperforms Sequence Transformers in Protein-Ligand Prediction") is defensible as a generalization across three tasks, but a more precise qualifier would improve scholarly integrity.

- **Missing hyperparameter details.** The paper states that hyperparameters were obtained by searching for the optimal learning rate (Section 3.1) but does not report the found values, batch size, optimizer choice, or number of epochs for pretraining. While code release mitigates this, the review process evaluates the paper as submitted.

- **Compute comparison omits voxelization preprocessing time.** Section 4.3 reports ProteinVista's runtime at 20s per 1K proteins (forward pass only) but does not include the time required to voxelize each protein at 1.0Å resolution over up to 160³ grids. This preprocessing cost should be accounted for in a fair runtime comparison.

- **No confidence intervals on main results.** Tables 1 and 2 report point estimates without error bars or standard deviations across multiple runs. This is common in the field but limits assessment of result stability, especially for metrics like MCC where small differences (e.g., 0.78 vs. 0.79 on ESP) are hard to interpret without variance.

### Trivial

- Figure 2e reports ablation changes as relative R² changes, but the exact baseline R² value (0.69) could be stated more prominently in the figure itself rather than only in the caption text.
- The paper uses "ProteinVista_OP" interchangeably with "ESM-ProteinVista_OP" in places (Section 3.3, line 454–455), which could confuse readers about whether the standalone or ensemble model is being discussed.

## Nice-to-Haves

- Compare ProteinVista_OP (standalone, without ESM-2) against SPOT, ProSmith-ESP, and Fusion_ESP to directly test whether the structural encoder alone surpasses these task-specific architectures.
- Ablate pretraining data scale (e.g., 50K, 100K, 250K, 500K structures) to substantiate the data efficiency claim more thoroughly.
- Finer pLDDT binning in Figure 2c (e.g., separate bins for 0–50, 50–80, 80–90, 90–100) would clarify where the method degrades on low-confidence structures.
- Include a quantification of rotation invariance by reporting embedding or prediction variance across randomly rotated copies of the same proteins.

## Removed Points

These points from the reviewers were checked against the paper and removed for the following reasons:

- *"Rotation invariance scheme requires test-time averaging / single-view ablation loses 6.4% — methodological gap"* — The paper is fully transparent about this; the 5-view averaging is part of the method, not a flaw. The ablation explicitly measures this cost and it is correctly framed as a requirement, not a bug.
- *"The claim that GNNs 'omit atom-level details and therefore struggle' is asserted without quantitative support"* — This claim is supported by citation to the ESM-GearNet study (Zhang et al., 2023b) which showed most graph encodings only slightly outperformed or underperformed the sequence-only baseline.
- *"The GO result contradicts the outperformance claim"* — The abstract only claims outperformance on "three benchmarks" (the three binding tasks), not the GO task. The GO task is correctly presented as a negative control where PV is expected to underperform.
- *"ProteinVista is not purely structure-based because it aligns to ESM-2"* — This is correctly described in the paper as a design choice; the model takes voxelized structure as input and the contrastive objective is a pretraining loss, not an input modality.
- *"Missing related works"* — Cannot verify and should not be fabricated.
- *"Missing appendix / missing proofs"* — Parser artifact; appendices exist in original submission.
- *"Reproducibility: unspecified training details / hyperparameters"* — Partially valid (merged into Minor), but the code release commitment addresses the core concern; only specific missing values (learning rate, batch size) are noted.
- *"Overfitting potential: 123M parameters on 500K structures"* — Speculative; no evidence of overfitting is shown (no training curves needed, but absence is not evidence of a problem).
- *"Not accounting for batch size / GPU memory constraints"* — Speculative; adaptive boxing is described and addresses the concern.

## Novel Insights

The most interesting finding not fully explored by the paper itself is the **task-dependent complementarity profile** between atom-level structure and sequence models. On IC50 regression, the ensemble (ESM-ProteinVista) actually *underperforms* ProteinVista alone (R² 0.68 vs. 0.69), while on classification tasks the ensemble is beneficial. This creates a clear picture: when fine geometric detail is paramount (binding affinity), the structure encoder dominates and sequence information adds noise; when broader functional classification is needed, the two modalities complement each other. This "phase transition" between structure-dominant and sequence-complementary regimes as a function of task granularity is a useful design principle for practitioners. It also suggests that the community's current reflex of always ensembling structure and sequence models may be suboptimal — the optimal strategy depends on the resolution required by the task.

## Suggestions

1. **Add a head-to-head comparison under model-specific optimized pipelines.** For ESM-2, try fine-tuning the ligand encoder or using attention pooling over residues; for ProteinVista, apply the same OP enhancements. If ProteinVista still wins, the central claim is much stronger.
2. **Evaluate ProteinVista_OP (without ESM-2) directly against SPOT, ProSmith-ESP, and Fusion_ESP.** This separates the effect of the optimized pipeline from the effect of the ensemble.
3. **Clarify the IC50 data preprocessing** — specify whether pIC50 (−log₁₀ IC50) was used. If raw IC50 was used, report results after log-transformation.
4. **Report hyperparameters** (learning rate, batch size, optimizer, epochs) for both pretraining and fine-tuning, and include confidence intervals or standard deviations over multiple runs.
5. **Temper the abstract/title claims** to "outperforms or matches" or "outperforms sequence transformers on multiple structure-dependent tasks," acknowledging that on the enzyme-substrate task the models are competitive.

---

## Calibration Report

**Round 1 (Bracketing):** Searched for reviews of 3D CNN / protein structure papers in three bands:
- **Weak** (score < 3.5): e.g., rEQ8OiBxbZ (3.0), jqx5XI4Yr3 (3.4) — papers with fundamental flaws or very preliminary results.
- **Middle** (3.5–7.5): e.g., BEH4mGo7zP (5.75, Accept), umUIYdLtvh (5.50, Reject), iBAWiEjogY (3.67, Reject), OzUNDnpQyd (7.00, Accept).
- **Strong** (>7.5): e.g., 0ctvBgKFgc (8.0), kJFIH23hXb (8.0) — top-tier generative modeling papers with strong theoretical contributions.

**Bracket:** ProteinVista sits clearly above the weak band (3–3.5) and below the strong band (7.5+). Within the middle band, it is substantially stronger than ProteiNexus (3.67, which had data leakage issues). It is comparable to or slightly stronger than BEH4mGo7zP (5.75, accepted, marginal improvements) and AXbN2qMNiW (5.67, accepted, had data leakage concerns). It is roughly on par with EquiPocket (5.50, rejected mainly on novelty) but has a stronger novelty claim. **Initial bracket: 5.0–6.5.**

**Round 2 (Narrowing):** Searched within (5.0, 6.0) and (5.5, 7.0):
- sTYuRVrdK3 (6.25, Accept) — ProteinWorkshop benchmark suite; rigorous evaluation framework.
- 4S2L519nIX (6.50, Accept) — all-atom GNN pretraining; solid study but some novelty questions.
- ARQIJXFcTH (6.75, Accept) — AtomSurf; strong empirical results on Atom3D.
- QKywN4BbqA (5.25, Reject) — E³former; novelty concerns.
- 9AtlhmFVDi (5.50, Reject) — transformers learning Euclidean distance; weaker empirical support.

**Final Calibration:** ProteinVista is stronger than EquiPocket (5.50) because its novelty is clearer, and it is comparable to the accepted 5.67–5.75 papers. However, the verified weaknesses (pipeline fairness, SOTA conflation, missing IC50 details) prevent it from reaching the 6.0+ level of papers like ProteinWorkshop (6.25) or AtomSurf (6.75), which had more rigorous evaluation protocols. The paper's contribution is real and the strengths are substantive, but the claim-evidence gap in the central comparison is a meaningful weakness.

**Score: 5.5**

**Anchors consulted (all rounds):**
- rEQ8OiBxbZ (3.00) — much weaker; had fatal methodology issues.
- jqx5XI4Yr3 (3.40) — much weaker; ProteinAdapter.
- m9zWBn1Y2j (3.00) — much weaker; ligand conformation generation.
- iBAWiEjogY (3.67) — weaker; ProteiNexus had data leakage issues.
- BEH4mGo7zP (5.75) — comparable; marginal improvements but broader benchmark evaluation. ProteinVista has stronger novelty.
- umUIYdLtvh (5.50) — comparable; EquiPocket had similar score but was rejected on novelty grounds.
- AXbN2qMNiW (5.67) — comparable; BindNet had data leakage concerns. ProteinVista is cleaner in this regard.
- sTYuRVrdK3 (6.25) — stronger; ProteinWorkshop is a rigorous benchmark paper.
- ARQIJXFcTH (6.75) — stronger; AtomSurf has more rigorous Atom3D evaluation.
- 4S2L519nIX (6.50) — stronger; more comprehensive scaling analysis.
- QKywN4BbqA (5.25) — slightly weaker; novelty concerns.
- 9AtlhmFVDi (5.50) — comparable; but weaker empirical support.
- OzUNDnpQyd (7.00) — stronger; theoretical + empirical contribution.
- 0ctvBgKFgc (8.00) — much stronger; top-tier protein generation.
- kJFIH23hXb (8.00) — much stronger; top-tier protein generation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>