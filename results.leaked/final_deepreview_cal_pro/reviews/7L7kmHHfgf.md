Now I have thorough calibration. Let me synthesize the final consolidated review.

---

## Summary

PIRN introduces a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD). It uses balanced optimal transport (BPA) to prevent codebook collapse, adaptive prototype refinement (APR) to handle unseen normal variations at test time, and a cross-modal normality communication module (MNC) to exchange high-level normal cues between RGB and surface-normal modalities. Evaluated on MVTec 3D-AD, Eyecandies, and Real-IAD D3, PIRN achieves strong performance, especially in few-shot settings (5-, 10-, 50-shot), with substantial margins over existing baselines.

## Strengths

- **Novel, well-motivated architecture for few-shot MAD.** The three core components (BPA, APR, MNC) each address a distinct, clearly articulated failure mode of prior work: codebook collapse in prototype learning, train-test distribution mismatch, and missing cross-modal collaboration. The balanced optimal transport formulation for prototype assignment is a principled way to ensure uniform prototype utilization, as visually confirmed by the t-SNE comparison in Figure 1 (Right).

- **Strong empirical results with large margins.** On MVTec 3D-AD, PIRN improves image-level AUROC over the strongest baseline by +3.9 (5-shot), +3.7 (10-shot), and +2.4 (50-shot). On Eyecandies, gains are +3.6, +4.0, and +2.2 respectively (Table 1). These consistent, substantial margins across shot settings and benchmarks provide convincing evidence of effectiveness under data scarcity.

- **Computationally efficient despite sophistication.** PIRN requires 103.36G FLOPs and 17.49ms latency — 85% fewer FLOPs and 4.35× faster than the recent SOTA FIND (Table 4) — while achieving the best AUROC_I. This is a practical advantage for deployment.

- **Interpretable prototype-based anomaly cues.** The displacement visualization (Figure 4) shows that anomalous patch tokens undergo significantly larger shifts toward normal prototypes during reconstruction, providing an interpretable link between the reconstruction mechanism and anomaly detection.

- **Sound design-space exploration.** Ablations on codebook size (Table 5) and decoder depth (Table 6) confirm that a compact codebook (K=10) and shallow decoder (L=2) are optimal for few-shot settings, offering practical guidance beyond the paper's own method.

## Weaknesses

### Fatal

None.

### Major

- **FIND omitted from the main comparison table despite being the most directly comparable baseline.** FIND (Li et al., 2025) is a recent reconstruction-based MAD method that uses the same surface-normal input representation as PIRN and is cited in the paper. It appears only in the computational efficiency table (Table 4, showing AUROC_I 0.921 vs. PIRN's 0.922) but is absent from the main results table (Table 1) across all shot settings and metrics. Since FIND shares the same input preprocessing pipeline, its inclusion would provide the most direct test of PIRN's architectural advantages. The paper offers no justification for this exclusion. This is a significant evaluation completeness gap.

- **Ablation table (Table 2) is unreadable as presented, making component contributions unverifiable.** All five rows show identical checkmarks for all three modules but different AUROC values, and one intermediate row (0.967 AUROC_I) appears to exceed the full model (0.922). While this may be partly a parser artifact, the paper's text description cannot be independently verified against the table, and the anomalous 0.967 value is not explained. This undermines the claim that "removing each component from the full model results in a consistent performance drop."

### Minor

- **No variance estimates in few-shot experiments.** All few-shot results (Table 1) are reported as single numbers. Random selection of the small training sets can cause substantial run-to-run variation, and without standard deviations or confidence intervals, the reliability of the reported gains cannot be fully assessed. This is a common limitation in the field but still weakens the evidence for the central few-shot superiority claim.

- **The training loss is described only by reference** ("a soft mining loss (Luo et al., 2025)") without specifying the exact function. Since this is the central training signal, a short definition in the main text would aid both understanding and reproducibility.

- **The AUROC₇ metric in Figure 1 (Left) is not defined.** The curve compares PIRN with baselines across a continuous range of training fractions, but the metric "AUROC₇" is never explained, and the experimental protocol for varying the fraction is not described, making the headline claim of "superior accuracy using less than 1% of the training data" harder to evaluate.

- **No analysis of prototype purity under APR.** The paper argues that anomalous patches are assigned diffusely and therefore do not contaminate prototypes during test-time refinement, but offers no direct evidence — e.g., tracking prototype drift on anomalous vs. normal samples, or ablating the GRU gate. Without this, the safety of the APR mechanism is assumed rather than demonstrated.

### Trivial

- Notation inconsistency: "AUROC_J" in Table 8 (Real-IAD) vs. "AUROC_I" elsewhere for image-level AUROC.
- Hardware and measurement conditions for the latency comparison (Table 4) are not reported.

## Nice-to-Haves

- Including FIND in all performance tables across all shot settings would complete the comparison with the closest contemporary method.
- Repeating few-shot evaluation with multiple random seeds (e.g., 5) and reporting mean ± std would strengthen confidence in the gains.
- An analysis of prototype drift under APR (normal vs. anomalous inputs) would directly support the claim that APR expands normality coverage without absorbing anomalies.
- Extending the Real-IAD D3 evaluation to the few-shot setting would better align that experiment with the paper's central motivation.
- Reporting the Sinkhorn entropy regularization strength and its sensitivity would aid reproducibility.
- Clarifying what 3D representation each baseline uses (point clouds, depth, or surface normals) and confirming parity or discussing potential effects would preempt modality-mismatch concerns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Input modality mismatch (structural).** The harsh critic claimed that PIRN uses surface-normal maps while baselines M3DM, CFM, 3D-ADNAS were designed for raw point clouds or depth maps, making comparisons "uninterpretable." This is speculative — the paper does not state what representations the baselines use, and surface-normal maps are a standard, derived representation from the same underlying point cloud data. The paper follows FIND's procedure to generate them. Without evidence that the baselines used fundamentally different data, this is not a verifiable flaw.

- **MNC contribution "at most ≈ 0.006" being marginal.** The harsh critic derived this number from a corrupted Table 2. While the exact contribution cannot be verified, the modality availability study (Table 3) shows that combining RGB and surface normals yields meaningful improvements over single-modality setups (e.g., 0.922 vs. 0.879 at 10-shot), and this gain is enabled by MNC's cross-modal communication. The specific numeric claim about MNC's isolated contribution is unreliable given the table corruption.

- **Strength Finder claim that "Without MNC, the full model's AUROC_I drops to 0.828."** This conflates removing ALL modules (the baseline) with removing only MNC. The actual contribution of MNC is smaller than this framing suggests. Removed to avoid overstating the MNC ablation story.

- **The paper's Figure 1 Left description mentions "AUROC₇" which the harsh critic flagged as undefined.** While this is a valid minor concern (retained above), the harsh critic framed it as undermining the "headline claim" — this is an overstatement given that the main results in Table 1 are clearly defined.

- **The Strength Finder's generic strength claims about "addressing an important problem" and "targeting an interesting question."** These are superficial and lack concrete grounding. Removed.

## Novel Insights

The paper's use of balanced optimal transport for both prototype assignment (BPA) and prototype refinement (APR) in a unified framework is a genuinely novel combination. The insight that the same OT machinery can simultaneously (a) prevent codebook collapse through uniform marginal constraints and (b) provide anomaly-robust context aggregation for test-time adaptation (since anomalous patches get diffuse OT assignments) is elegant and well-motivated. The two-stage cross-modal communication design — prototype-level alignment via graph attention followed by prototype-guided cross-attention for token-level injection — is also a thoughtful architectural contribution that avoids the brittleness of dense patch-to-patch alignment in low-data regimes.

## Suggestions

- Define the training loss explicitly in the main text rather than only by reference.
- Define "AUROC₇" and describe the protocol for Figure 1 Left.
- Address the anomalous 0.967 value in Table 2 — either it's a legitimate finding that BPA+APR can outperform the full model in some settings (which should be discussed), or it's a corrupted entry that needs correction.
- Add FIND to Table 1 across all shot settings and metrics where FIND results are available.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison to PIRN |
|---|---|---|---|
| gTsLBDMZrL | 5.50 | R1 | PIRN is stronger: more comprehensive benchmarks, clearer methodology |
| b7ROBvgNkE | 6.25 | R2 | PIRN is stronger: cleaner methodology, larger empirical gains |
| Zzs3JwknAY | 6.40 | R1/R2 | PIRN is slightly stronger: multimodal is harder, larger margins |
| lNZJyEDxy4 | 6.67 | R2 | Comparable: both have novel architectures and strong results across benchmarks |
| 7VkHffT5X2 | 6.75 | R2 | Comparable: PIRN has efficiency advantage but AnoLLM has novelty of LLM application |
| lR3rk7ysXz | 7.00 | R2 | PIRN is weaker: lR3rk7ysXz has theoretical derivations, more evaluation breadth |
| cJs4oE4m9Q | 8.00 | R1 | PIRN is much weaker: lacks theory, has evaluation gaps |

**Round 1 bracket:** 5.5 – 8.0. **Round 2 narrowed:** PIRN sits between 6.25 and 7.00, closest to lNZJyEDxy4 (6.67). PIRN has the stronger contribution of tackling the harder multimodal few-shot problem with large margins, but its evaluation completeness (FIND omission, corrupted Table 2, no variance estimates) pulls it below the 7.0 tier. **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>