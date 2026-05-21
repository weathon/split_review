Now let me write the comprehensive review.

## Summary

PIRN proposes a prototype-driven reconstruction framework for **few-shot multimodal anomaly detection** (RGB + surface normals). It introduces three core innovations: (1) **Balanced Prototype Assignment (BPA)** using optimal transport to prevent codebook collapse; (2) **Adaptive Prototype Refinement (APR)** via GRU-based gated updates to expand prototype coverage to unseen normal variations at inference time; and (3) **Multimodal Normality Communication (MNC)** that exchanges prototype-level normal knowledge across modalities through graph alignment and cross-attention. Experiments on MVTec-3D-AD, Eyecandies, and Real-IAD D³ show consistent improvements over prior methods across 5-shot, 10-shot, 50-shot, and full-shot settings.

## Strengths

1. **Consistent and substantial few-shot gains across three benchmarks.** Table 1 shows PIRN outperforms the strongest prior method (INP-Former) on MVTec-3D-AD by +3.9 (5-shot), +3.7 (10-shot), and +2.4 (50-shot) AUROC_I. On Eyecandies, gains are +3.6, +4.0, and +2.2 respectively. Gains hold across all three metrics (AUROC_I, AUROC_P, AUPRO) and both datasets, supporting the core claim.

2. **Balanced optimal transport demonstrably prevents codebook collapse.** The t-SNE visualization in Figure 1 compares softmax assignment (collapsed prototypes) against BPA (uniform prototype distribution). This visual evidence is corroborated by the ablation removing BPA, which drops AUROC_I from 0.922 to 0.828 (10-shot), the largest single-component drop.

3. **Cross-modal communication provides measurable benefit, especially in low-data regimes.** Table 3 shows RGB+SN outperforms either modality alone, with the largest relative gain in the 5-shot setting (0.900 vs. 0.854 for SN-only, +4.6 points). This directly validates the MNC design motivation.

4. **Computational efficiency with no accuracy sacrifice.** Table 4 shows PIRN achieves the best AUROC_I (0.922) while requiring only 103.36G FLOPs and 17.49ms latency — 85% fewer FLOPs and 4.35× faster than FIND (728.46G, 76.09ms). This practical advantage is meaningful for deployment.

5. **Systematic analysis of design choices.** Ablations on prototype count K (Table 5), decoder depth L (Table 6), and APR aggregation methods (Table 7) show clear trends and non-monotonic behavior (e.g., too many prototypes weaken the information bottleneck), supporting the authors' design rationale.

6. **Strong localization on Real-IAD D³ with fewer modalities.** In Table 8, PIRN achieves the best average AUROC_P (0.961) using only RGB and surface normals, outperforming D³M (0.937 AUROC_P) which uses three input modalities.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled backbone for most baselines.** The paper adapts INP-Former to use the same frozen DINOv2 ViT-B/14 encoder as PIRN, but does not specify or control the feature backbones for M3DM, CFM, 3D-ADNAS, BTF, or AST. DINOv2 features are known to be exceptionally strong for anomaly detection, so the reported gains may partially reflect the backbone quality rather than the proposed modules alone. This does **not** invalidate the paper's contribution (the ablation still shows that removing each component degrades performance on the same backbone, and INP-Former uses the same backbone), but it weakens the fairness of direct comparison and makes it difficult to quantify how much of the margin over M3DM/CFM/3D-ADNAS is due to the method vs. the encoder. The paper should at minimum disclose the backbone used for each baseline and acknowledge this as a limitation.

### Minor

1. **Ablation table (Table 2) has suspicious values.** The 4th row reports AUROC_I = 0.967, which exceeds the full model's 0.922 in the same setting. This is inconsistent with the stated claim that removing any component degrades performance. It could be a different evaluation setting or a labeling/formatting error. The authors should clarify or correct this entry.

2. **No statistical significance for few-shot results.** Few-shot experiments involve random selection of training samples; performance can vary noticeably across draws. The paper reports only single-run numbers without standard deviations. Given some margins are modest (e.g., +2.4 AUROC_I in 50-shot on MVTec), reporting mean and std over multiple random trials would substantially strengthen confidence.

3. **No limitations or failure case discussion.** The paper does not discuss when or why PIRN might fail — e.g., sensitivity to surface normal estimation quality, dependence on prototype count tuning per dataset, or scenarios where APR might adapt to anomalous patterns (large uniform defects matching a prototype cluster). Including a brief limitations paragraph would strengthen the paper.

4. **Optimal transport implementation details omitted.** The Sinkhorn algorithm's entropy regularization coefficient and number of iterations are not specified. Given the central role of OT in both BPA and APR, these details are necessary for reproducibility.

### Trivial

1. Table header says "BFA" instead of "BPA" (Table 2). Minor typo.
2. Table 2 has identical checkmarks (✓ ✓ ✓) across all rows, making it impossible to determine row semantics from the table alone. (Likely a PDF parsing artifact; the surrounding text compensates but the table should render correctly.)

## Nice-to-Haves

- An analysis comparing PIRN's decoder with a simpler reconstruction head (e.g., linear projection) using the same DINOv2 backbone would help isolate the contribution of the prototype mechanism from the backbone.
- A comparison of baselines re-implemented with the same frozen DINOv2 encoder (at least for a subset of methods) would address the backbone fairness concern most directly.
- Reporting few-shot results with standard deviations over 3–5 random training splits.

## Removed Points

- **"Ablation table is effectively uninterpretable"** (harsh critic, critical issue #2): The table's identical checkmarks are a PDF extraction artifact. The surrounding text clearly explains each row's semantics and the ablation logic. The *numerical* inconsistency (0.967) is kept as a Minor weakness; the formatting complaint itself is not.
- **"Missing appendix content / missing proofs"**: Removed per instructions — parser strips these from all papers.
- **"Unfair comparison with methods using different modality sets on Real-IAD"** (harsh critic, section notes): PIRN is explicitly compared against D³M which uses three modalities, and the paper acknowledges this difference. This discussion is fair and not a weakness.
- **"Computational efficiency comparison is selective"** (harsh critic): Table 4 compares against the most relevant reconstruction-based methods (M3DM, CFM, FIND). This is a reasonable selection, not a selective omission.
- **"Pure formatting nitpicks"** about table headers, garbled symbols, etc.: These are parser artifacts.
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem"): Removed because they lack specific, concrete content tied to the paper's evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disclose and ideally control baselines' backbones.** At minimum, state the backbone architecture used for each baseline in Table 1. Strongest action: re-run M3DM and CFM with the same frozen DINOv2 encoder features as input, or run a "PIRN decoder replaced by a simple predictor" baseline to isolate the prototype contribution from the backbone.
2. **Fix or explain the 0.967 value in Table 2.** If this corresponds to a different setting (e.g., all-shot instead of 10-shot), clearly label it.
3. **Add standard deviations** over multiple random training splits for few-shot experiments.
4. **Add a brief limitations paragraph** discussing failure cases and sensitivity to hyperparameters (prototype count K, surface normal quality).
5. **Specify Sinkhorn parameters** (entropy regularization, iterations) in the implementation details.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- **Weak anchors** (score < 3.5): Topological Alignment (2.50), FewGAD (3.00), GAUSS-Fusion (3.00). These papers have fatal flaws (confounded comparisons, unsupported central claims, weak evidence). PIRN is clearly stronger — its core claims are supported by controlled ablations and consistent results across three benchmarks.
- **Middle anchors** (3.5–7.5): UIP-AD (4.00, Withdrawn), DCR²-AD (5.00, Reject), TokenCLIP (5.50, Reject), FoundAD (6.00, Accept Poster). UIP-AD (similar topic — prototype-based multimodal AD) was rejected for missing ablations and missing INP-Former comparison. PIRN addresses both, giving it an edge. DCR²-AD was rejected for limited novelty; PIRN has stronger methodological novelty. TokenCLIP was rejected partly for missing visualizations and unclear OT implementation; PIRN provides qualitative analysis and clearer OT motivation. FoundAD was accepted for its clean evaluation and strong results despite simplicity.
- **Strong anchors** (score > 7.5): Depth Anything 3 (7.00, Oral), YoNoSplat (6.50, Poster). These are top-tier papers with extensive evaluation and no major methodology concerns. PIRN is clearly below this tier.

**Initial bracket**: 4.0 – 6.5

**Round 2 — Narrowing within bracket:**
I pulled anchors in the (4.5–6.5) and (6–8) ranges. The most relevant comparisons:
- **UIP-AD (4.00)**: Very similar topic. PIRN is stronger — it has proper ablations, compares to INP-Former, has cleaner presentation, and provides more thorough evaluation. But UIP-AD was withdrawn/rejected.
- **FoundAD (6.00, Poster)**: Few-shot AD with foundation encoders. FoundAD has cleaner baseline comparisons (controlled backbone experiments) but less methodological novelty. PIRN has more methodological depth and broader evaluation (3 datasets vs 2) but weaker baseline controls. Roughly comparable, with PIRN slightly behind due to the backbone fairness concern.
- **TokenCLIP (5.50, Reject)**: Uses OT for AD like PIRN. TokenCLIP's weaknesses include missing localization visualizations, hyperparameter sensitivity concerns. PIRN provides these. However, TokenCLIP was rejected; PIRN is stronger.

**Final score**: 5.5. The paper has genuine methodological contributions and strong empirical support across three benchmarks. However, the uncontrolled backbones for most baselines and the suspicious 0.967 value in the ablation table prevent it from being a clear accept. The weaknesses are fixable in revision, and the core methodology is sound.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>