Now I have a thorough understanding of the paper, all reviewer claims, and the calibration landscape. Let me write the final consolidated review.

---

## Summary

PIRN proposes a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD). It introduces three novel components: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) for test-time prototype adaptation via GRU-gated updates, and Multimodal Normality Communication (MNC) for cross-modal normality exchange. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3, consistently outperforming baselines across 5/10/50-shot settings while being 4.35× faster and using 85% fewer FLOPs than the prior SOTA FIND.

## Strengths

1. **Consistent few-shot gains across multiple benchmarks** — Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.9 AUROC_I (5-shot), +3.7 (10-shot), and +2.4 (50-shot), and on Eyecandies by +3.6, +4.0, and +2.2 respectively. These gains are consistent across all three shot settings and two datasets, providing direct evidence that the method succeeds in data-scarce regimes.

2. **Component-wise ablation confirms all three innovations contribute** — Table 2 isolates BPA, APR, and MNC; removing each from the full model produces a measurable drop (e.g., removing APR drops AUROC_I from 0.922 to 0.883 at 10-shot), demonstrating that each module independently contributes to the reported gains.

3. **State-of-the-art accuracy at substantially lower cost** — Table 4 reports PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs. This contradicts the assumption that better few-shot AD must be more expensive.

4. **Design-space validation via systematic ablations** — Tables 5 and 6 ablate codebook size K and decoder depth L across multiple shots. The optimal K=10 and L=2 are consistent, and performance degrades symmetrically with too few or too many prototypes/layers (e.g., K=100 gives 0.901 vs. 0.963 AUROC_I at K=10), showing empirically grounded design choices rather than arbitrary ones.

5. **Interpretable evidence of discriminative prototype encoding** — Figure 4 visualizes token displacements in PCA space, showing anomalous tokens undergo larger shifts toward normal prototypes during reconstruction, with histograms confirming clear separation. This directly supports the claim that prototypes act as normality anchors.

## Weaknesses

### Fatal
None.

### Major

1. **Missing FIND baseline in the main few-shot comparison table** — FIND (Li et al., 2025) is cited as a "recent SOTA" and achieves 0.921 AUROC_I on 10-shot MVTec-3D-AD (Table 4), nearly matching PIRN's 0.922. Yet FIND is absent from the main few-shot table (Table 1), where it would serve as a crucial point of comparison. The paper's central claim of "consistently achieving superior performance compared to existing baselines" is weakened without this inclusion. The authors should either add FIND to Table 1 or explain why a direct comparison is not possible.

2. **No variance estimates for any few-shot results** — The paper reports all results without standard deviations or confidence intervals. In few-shot settings (5, 10, 50 samples), the specific samples chosen can substantially affect results. This is especially concerning given that pixel-level margins are very small (e.g., AUROC_P differences of +0.002 to +0.006 in most settings), making it impossible to assess statistical significance. The authors should report mean and std over at least 3 random seeds with different few-shot splits.

### Minor

3. **APR robustness assumption is theoretically motivated but empirically unvalidated** — The paper claims that anomalous patches "tend to be assigned more diffusely across prototypes... thereby contributing weakly to each prototype context" during APR's OT-based context extraction. This is a reasonable theoretical argument, but no experiment validates it. A synthetic test (e.g., inserting a known anomaly and measuring context vector deviation) would strengthen the paper. The APR ablation (Table 2) shows removal drops AUROC_I from 0.922 to 0.916, confirming APR's contribution is meaningful but modest, so this is not a fatal concern.

4. **Real-IAD D3 evaluation uses the full-shot setting and comparisons are not perfectly controlled** — The Real-IAD results (Table 8) are presented as supplementary evidence but compare PIRN (RGB+Surface Normals) against D³M (RGB+Pseudo-3D+3D), which uses a tri-modal representation. The paper acknowledges this asymmetry, but a cleaner comparison against methods using the same input modalities would strengthen this experiment. Presenting per-category cherry-picked comparisons (e.g., "fork_crimp_terminal 0.978 vs. 0.819") without systematic analysis also weakens the narrative.

### Trivial

None.

## Nice-to-Haves

- Include an ablation of APR's test-time adaptation to quantify the benefit of dynamic refinement across different shot settings (currently only shown for 10-shot).
- Clarify whether early stopping or a validation set is used during few-shot training; 60 epochs on 5–10 samples may lead to overfitting without monitoring.
- Provide an analysis of when APR's OT-based context extraction might fail (e.g., large contiguous anomalous regions, subtle but consistent global shifts).

## Removed Points

- **INP-Former baseline adaptation is unfair** (from Harsh Critic). REMOVED: The critic claims the adaptation "entirely discards INP-Former's core contribution: its test-time prototype extraction from the same image." This is factually incorrect. INP-Former's core mechanism is extracting intrinsic normal prototypes from a single test image. In the paper's two-stream adaptation, each stream independently performs exactly this operation on its respective modality (RGB or surface normals). This is the natural and faithful adaptation of a 2D method to multimodal input. Adding cross-modal fusion to INP-Former (as the critic suggests) would give it capabilities it was never designed for, creating an unfair advantage in the opposite direction. The adaptation is reasonable and the comparison is fair as-is.

- **Generic "evaluation lacks rigor" / "area-of-concern" sweeps** — the harsh critic's section-by-section notes contain several speculative concerns (e.g., "the table formatting is broken (OCR issues)") that are not substantive. Removed as noise.

- **Strength Finder's generic strengths** — the Strength Finder's summary paragraph duplicates points already covered in the specific strengths above. Removed to avoid redundancy.

- **Missing related works complaint** — removed per policy (I cannot verify whether works exist or not).

- **Complaints about appendix/table formatting** — removed as these are parser artifacts, not author errors.

## Novel Insights

The most interesting observation across the reviews is the tension between PIRN's two core design principles. BPA enforces a fixed, balanced prototype assignment that prevents codebook collapse during training, while APR actively adapts those same prototypes at test time. These two mechanisms pull in opposite directions (stabilizing vs. adapting the normality representation), yet the ablation shows both contribute positively. Understanding why this tension does not cause instability — and whether there is a principled trade-off between codebook compactness and adaptive coverage — would be a valuable line of inquiry beyond what the paper currently provides.

## Suggestions

1. **Add FIND to the main few-shot comparison table.** Since FIND achieves 0.921 AUROC_I on the same 10-shot setting (per Table 4), its inclusion in Table 1 is necessary to support the claim of consistent superiority. If FIND uses a different backbone or protocol, state this explicitly.

2. **Report error bars.** Run at least 3 random seeds with different few-shot training splits and report mean ± std for all metrics. This is essential for a paper whose margins are modest in several metrics.

3. **Validate APR's OT robustness empirically.** A simple experiment injecting synthetic anomalies into normal test samples and measuring context vector distortion would substantially strengthen the paper's claims about APR's robustness.

4. **On Real-IAD, report only the metrics relevant to the paper's scope or add a disclaimer** that this is a full-shot comparison with uneven modality usage. Avoid selective per-category cherry-picking without a systematic pattern analysis.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Weak anchors (<3.5): CLIP-LAD (3.00, reject), Generalized AD (2.50, reject) — far weaker than PIRN
- Middle anchors (3.5–7.5): Prototype-oriented Fast Refinement (5.50, reject), H-PAD (5.60, accept), One-for-All Few-Shot AD (6.40, accept), AnomalyCLIP (6.17, accept), PTAD (4.25, reject)
- Strong anchors (>7.5): Deep Orthogonal Hypersphere (8.00, accept) — clearly higher quality than PIRN

**Bracket:** 5.5–7.5

**Round 2 (Narrowing):**
- Prototype-oriented Fast Refinement (5.50, reject): Closest topical match. PIRN is substantially stronger — broader evaluation, clearer ablations, addresses multimodality, better efficiency analysis. Score should be above 5.5.
- One-for-All Few-Shot AD (6.40, accept): Comparable quality but with a different focus (multi-class single-modality vs. few-shot multimodality). PIRN matches it on evaluation breadth but falls short on error-bar reporting and baseline completeness. Score should be near 6.0–6.4.
- AnomalyCLIP (6.17, accept): Similar evaluation thoroughness. PIRN's weakness profile (missing FIND, no error bars) is roughly comparable to AnomalyCLIP's weaknesses (questionable DPAM motivation, missing related work).

**Final score:** 6.0. PIRN is clearly stronger than papers scoring in the 4–5.5 range and has genuine novelty and thoroughness. However, the missing FIND baseline in the main results table and the absence of variance estimates are meaningful evaluation gaps that prevent it from scoring at the 6.5+ level where papers typically have near-complete evaluation protocols.

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| CLIP-LAD | bESxQeXTlo | 3.00 | R1 | Much weaker — limited eval, unclear method |
| Generalized AD | MbtUctg3KW | 2.50 | R1 | Much weaker — different domain, limited |
| Fake News Detection | O0vy7hHqyU | 3.00 | R1 | Different topic, much weaker |
| PTAD | Vi6p2TeujL | 4.25 | R1 | Weaker — overcomplicated, unclear notations |
| Prototype-OT OOD | J2we1sVd9m | 4.60 | R1 | Weaker — OOD detection, narrower scope |
| Prototype-oriented Fast Refinement | gTsLBDMZrL | 5.50 | R1/R2 | Weaker — narrower eval, missing baselines |
| H-PAD | 8TBGdH3t6a | 5.60 | R1/R2 | Comparable quality but different domain (time series) |
| Optimal Multiple Transport | 3P87ptzvTm | 5.00 | R2 | Different topic, purely theoretical |
| Partial OT for OSSL | 3WB5hT27zf | 5.33 | R2 | Different topic, weaker |
| One-for-All Few-Shot AD | Zzs3JwknAY | 6.40 | R2 | Slightly stronger — cleaner evaluation, novel paradigm |
| MMAD | JDiER86r8v | 6.50 | R2 | Different topic (MLLM benchmark) |
| AnomalyCLIP | buC4E91xZE | 6.17 | R2 | Similar quality — comparable strengths/weaknesses |
| ThermalGaussian | ybFRoGxZjs | 6.60 | R2 | Different domain |
| Segment Any 3D Object | ENv1CeTwxc | 6.50 | R2 | Different task |
| Deep Orthogonal Hypersphere | cJs4oE4m9Q | 8.00 | R1 | Stronger — cleaner eval, theoretical grounding |
| Test-time Adaptation | TPZRq4FALB | 8.00 | R1 | Stronger — solid theoretical+empirical |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>