Now I have enough data for calibration. Let me finalize the review.

**Calibration Anchor Summary:**

| Anchor | Score | Round | Comparison to PIRN |
|--------|-------|-------|-------------------|
| CLIP-LAD (bESxQeXTlo) | 3.0 | R1 | Weaker: training-free, limited novelty |
| Meta-Tasks (ZxsKRuP0o8) | 2.5 | R1 | Weaker: generic few-shot, incremental |
| Generalized AD (MbtUctg3KW) | 2.5 | R1 | Weaker: generic AD approach |
| Prototypical evolution (ZaudLwn0Hm) | 2.5 | R1 | Weaker: generic prototype method |
| PO3AD (Slr3KojVRO) | 4.5 | R1 | Weaker: 3D AD but no multimodal, only 2 datasets |
| Noise IGB-AD (09TI1yUo9K) | 4.5 | R1 | Weaker: 3D AD, limited evaluation |
| Prototype Refinement (gTsLBDMZrL) | 5.5 | R1 | Similar topic, weaker: 2D only, less comprehensive evaluation, no multimodal |
| H-PAD (8TBGdH3t6a) | 5.6 | R2 | Different domain (time series), weaker contribution |
| SeaS (VzZTHukfCB) | 5.67 | R2 | Different contribution (generation), inconsistent scores |
| AnomalyCLIP (buC4E91xZE) | 6.17 | R2 | Different paradigm (zero-shot), less comparable |
| CATCH (m08aK3xxdJ) | 6.25 | R3 | Different domain (time series) |
| One-for-All (Zzs3JwknAY) | 6.4 | R2 | Similar domain, weaker ablations, clarity issues |
| MMAD (JDiER86r8v) | 6.5 | R2 | Benchmark paper, different contribution type |
| Scale-Aware (HNOo4UNPBF) | 6.5 | R3 | AD method with incremental novelty, limited domain — PIRN is clearly stronger |
| GOLD (y5einmJ0Yx) | 7.5 | R3 | Graph OOD, different problem but strong contribution |
| Deep Orthogonal Hypersphere (cJs4oE4m9Q) | 8.0 | R1 | Strong AD paper with theoretical proofs — PIRN lacks theory but has stronger engineering |
| FITS (bWcnvZ3qMb) | 8.0 | R3 | Time series, extreme efficiency — different domain |

**Round 1 bracket:** 5.5–8.0 (PIRN is clearly above the 5.5 prototype refinement anchor and below the 8.0 theory-heavy AD papers)

**Round 2 narrowing:** 6.5–7.5 (PIRN is clearly above Scale-Aware at 6.5 with its incremental novelty, and below GOLD at 7.5 which has a more unique contribution)

**Final calibration:** PIRN is closest to the 7.0 mark — it is a strong, well-structured engineering contribution with principled components, comprehensive evaluation, and a genuine efficiency advantage. Its weaknesses (excluded FIND from main table, no variance, untested APR robustness) are real but addressable. It's above the 6.5 anchors (which had more significant issues like incremental novelty or clarity problems) but below 7.5+ anchors (which had more unique contributions or theoretical depth).

## Summary
PIRN proposes a prototype-based framework for few-shot multimodal anomaly detection (RGB + surface normals) with three key components: Balanced Prototype Assignment (BPA) via optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) using GRU updates at inference, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange via GAT and cross-attention. Experiments on MVTec 3D-AD, Eyecandies, and Real-IAD D3 demonstrate improvements over existing baselines in few-shot settings, with an 85% reduction in FLOPs compared to FIND (the acknowledged SOTA).

## Strengths
- **Significant computational efficiency advantage over comparable methods.** Table 4 shows PIRN achieves 0.922 AUROC_I at only 103.36G FLOPs and 17.49ms latency, which is 85% fewer FLOPs and 4.35× faster than FIND (728.46G, 76.09ms) while achieving comparable accuracy. This is a practically important contribution for industrial deployment.
- **Principled BPA formulation with empirical validation.** The balanced OT formulation (Eq. 1) enforces equal-mass constraints (a = 1_N, b = N/K · 1_K), preventing codebook collapse. Table 2 shows BPA provides the largest single-component gain (0.828 → 0.883 AUROC_I), and Figure 1 Right provides t-SNE visualization confirming more uniform prototype distribution compared to softmax assignment.
- **Comprehensive and well-designed ablation study.** Tables 2, 3, 5, 6, and 7 provide ablations on individual component contributions, modality availability, codebook size K, decoder depth L, and token aggregation method — each showing clean, interpretable trends that support the design choices.
- **Multimodal gain is most pronounced in few-shot settings.** Table 3 shows RGB+SN over RGB-only yields +10.6 AUROC_I at 5-shot (0.794 → 0.900) but only +8.9 at all-shot (0.874 → 0.963), directly supporting the claim that prototype-level cross-modal exchange is especially valuable when per-modality representations are underrepresented.
- **Strong Real-IAD D3 results with fewer modalities.** Table 8 shows PIRN achieves the best AUROC_P (0.961) in 13/20 categories and competitive AUROC_J (0.873) using only two modalities, while D³M (AUROC_J 0.890) uses three. This demonstrates generalization to real-world industrial scenarios with complex geometries.

## Weaknesses

### Fatal
None

### Major
- **FIND (acknowledged SOTA) excluded from main comparison table.** Table 4 reveals FIND achieves 0.921 AUROC_I on 10-shot MVTec-3D-AD — virtually identical to PIRN's 0.922 — yet FIND is absent from Table 1 (the main results table) across all four shot settings and both datasets. The paper labels FIND as "SOTA" in Table 4 (line 236). Excluding the strongest known baseline from the primary comparison while claiming "consistently superior performance" (line 194) overstates the accuracy contribution. Including FIND in Table 1 would show PIRN's accuracy margin is negligible — the real contribution is efficiency. The paper should include FIND in all main tables or honestly reframe the contribution.

- **No variance or statistical significance reporting for few-shot results.** In few-shot settings, which K samples are selected can substantially affect results. The paper reports only single-point metrics without standard deviations, confidence intervals, or multiple-run statistics. A 3–4 point AUROC_I improvement (the margin claimed over INP-Former) could fall within the noise range of few-shot sampling variability. Without this information, the community cannot assess whether the improvements are robust. This is the single most important missing piece for a paper whose central claim is few-shot superiority.

- **APR's robustness to anomalous inputs at test time is asserted but not validated.** The paper claims APR is robust because (a) OT-based context extraction assigns anomalous patches diffusely across prototypes (line 106-107) and (b) GRU gating restricts anomalous context. However, the GRU was only trained on normal data and has no learned mechanism for rejecting anomalous contexts. The OT argument is plausible but untested: no experiment varying anomaly severity or measuring prototype drift is provided. Table 7 compares aggregation methods but only evaluates on normal data, not under varying anomalous conditions.

### Minor
- **Training loss definition is ambiguous.** The paper states "we train PIRN end-to-end using an intra-modal feature reconstruction loss, e.g., a soft mining loss (Luo et al., 2025). In practice, we minimize the cosine distance" (line 144). It is unclear whether the soft mining loss IS the cosine distance or something additional. The exact training objective should be stated as a displayed equation.

- **Sinkhorn regularization parameter ε and KNN neighbor count unspecified.** The paper mentions using the Sinkhorn algorithm "with entropic regularization" (line 94) but never states the ε value. Section 3.4 describes connecting prototypes to "nearest neighbors" via KNN without specifying the neighbor count. Both directly affect reproducibility and the method's behavior.

### Trivial
None

## Nice-to-Haves
- A per-category breakdown for MVTec 3D-AD and Eyecandies (currently in appendix) would help readers understand which anomaly types benefit most from multimodal communication.
- An APR sensitivity analysis: e.g., varying the fraction of anomalous patches in synthetic corruption experiments to measure prototype drift.
- Discussion of APR's computational cost at inference (extra OT computation per test image) separately from overall FLOPs.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Concern about the "purification" step intuition (z'_n = z_n · σ(z^{bpa}_n)): the paper explains this is channel-wise gating using intra-modal reconstruction to suppress anomalous details. This is a design choice, not a flaw, and the paper does provide the intuition (line 118-119).
- Parser-garbled Table 2: the checkmarks appear identical due to parsing, but the paper's text (line 274) clearly explains which components each row includes. This is not a paper problem.

## Novel Insights
The key novel observation is that PIRN's primary contribution may be the efficiency-accuracy trade-off rather than pure accuracy superiority. FIND matches PIRN's accuracy (0.921 vs 0.922 AUROC_I) but at 7× the computational cost. If the authors honestly reframed the contribution around "matching SOTA accuracy with dramatically fewer FLOPs while enabling effective multimodal communication," this would be a cleaner and more defensible claim than "consistently superior performance."

## Suggestions
- Include FIND in Table 1 across all shot settings and datasets. If PIRN matches FIND's accuracy, reframe the contribution honestly around the efficiency-accuracy trade-off.
- Report mean ± std over 5+ runs with different few-shot sample selections. This is essential for the community to trust the reported improvements.
- Add an APR ablation that directly tests sensitivity to anomalous inputs (e.g., synthetic corruption experiments measuring prototype drift, or plots of APR-updated vs. original prototypes for normal vs. anomalous test images).
- State the full training loss as a displayed equation rather than deferring to a citation.
- Specify all hyperparameters: Sinkhorn ε, KNN neighbor count, number of GAT heads.

## Reporting

**All retrieved anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| bESxQeXTlo | 3.0 | R1 | Weaker: training-free few-shot LAD, limited novelty |
| MbtUctg3KW | 2.5 | R1 | Weaker: general AD robustness, incremental |
| ZxsKRuP0o8 | 2.5 | R1 | Weaker: generic few-shot classification |
| ZaudLwn0Hm | 2.5 | R1 | Weaker: generic prototype method for VLMs |
| Slr3KojVRO | 4.5 | R1 | Weaker: 3D point cloud AD, no multimodal |
| 09TI1yUo9K | 4.5 | R1 | Weaker: 3D AD with noise injection, limited |
| gTsLBDMZrL | 5.5 | R1 | Similar topic (OT + prototype refinement for few-shot AD), but 2D-only, less comprehensive |
| 8TBGdH3t6a | 5.6 | R2 | Different domain (time series), weaker |
| VzZTHukfCB | 5.67 | R2 | Different contribution (anomaly generation), inconsistent reviewer scores |
| buC4E91xZE | 6.17 | R2 | Different paradigm (zero-shot AD with CLIP) |
| m08aK3xxdJ | 6.25 | R3 | Different domain (time series AD) |
| Zzs3JwknAY | 6.4 | R2 | Similar domain (few-shot AD), weaker ablations and clarity |
| JDiER86r8v | 6.5 | R2 | Benchmark paper, different contribution type |
| HNOo4UNPBF | 6.5 | R3 | AD with incremental novelty, limited domain — PIRN is clearly stronger |
| eWocmTQn7H | 6.5 | R3 | Different domain (time series diffusion) |
| y5einmJ0Yx | 7.5 | R3 | Graph OOD detection, different problem with unique contribution |
| cJs4oE4m9Q | 8.0 | R1 | Strong AD paper with theoretical propositions — PIRN lacks theory |
| bWcnvZ3qMb | 8.0 | R3 | Time series, extreme efficiency with theory — different domain |
| k38Th3x4d9 | 8.0 | R3 | Time series causal discovery — very different |

**Round 1 bracket:** 5.5–8.0
**Round 2 narrowed bracket:** 6.5–7.5
**Final score justification:** PIRN sits at 7.0. It is clearly stronger than the 6.5 anchors (Scale-Aware with incremental novelty, One-for-All with clarity/ablation issues) due to its principled OT formulation, comprehensive evaluation across 3 benchmarks, multimodal design, and major efficiency advantage. It falls below 7.5 anchors (GOLD with its unique adversarial OOD synthesis contribution) primarily because of the excluded FIND comparison and missing variance reporting, which undermine confidence in the central accuracy claims. The engineering is clean, the ablations are thorough, and the method is well-motivated — this is a solid accept with room to improve the empirical presentation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>