Now let me run the calibration search to bracket the score.Round 1 bracket: **5.0 to 6.5**. Now let me narrow within that range.Let me read two of the closest anchors in full.Now I have sufficient information to write the final review. Let me synthesize everything.

---

## Summary

CLIP-Map proposes a two-stage mapping-retraining pipeline for CLIP compression. Instead of pruning (selecting a subset of parameters), it uses learnable Kronecker-factored matrices (F_in, F_out) to linearly map original weights into a smaller architecture, producing a better initialization before knowledge distillation retraining. The central technical contribution is **Diagonal Inheritance Initialization**, which initializes the Kronecker factors as near-identity matrices to prevent distribution shift during early optimization. Results demonstrate clear advantages over TinyCLIP at extreme compression ratios (1% and 10%) with fewer total training epochs.

---

## Strengths

1. **Clear improvement at extreme compression ratios (Table 1, verified):** At 1% compression, CLIP-Map_base achieves MSCOCO TR@1 of 15.8 vs progressive TinyCLIP's 12.5 (3×25ep), using 25 total epochs vs 75. At 10%, TR@1 is 38.4 vs 36.2 (2×25ep progressive). These are unambiguous gains over both single-stage and multi-stage TinyCLIP, achieved more efficiently.

2. **Diagonal Inheritance Initialization is load-bearing and decisively validated (Table 5):** Random, Kaiming, and Xavier initializations yield near-zero IN-1K accuracy (0.1%, 4.4%, 4.9%), while Diagonal Init achieves 28.9%. The mathematical justification (Eqs. 5–8) demonstrates that Kronecker factors initialized independently produce multiplicative variance (Var(R) = σ_A² · σ_B²), causing instability. The diagonal approach approximates R_width ≈ I, directly addressing this problem. This is the most portable technical insight in the paper.

3. **Sample efficiency demonstrated (Table 3):** CLIP-Map_base achieves 63.7% zero-shot IN-val with 0.30B seen samples, vs TinyCLIP's 63.5% requiring 0.75B—a 2.5× reduction. CLIP-Map_small achieves 42.7% with 0.45B vs TinyCLIP's 41.1% at 0.75B.

4. **Kronecker factorization reduces mapping parameter overhead (Section 3.2.2):** Reduces mapping complexity from O(D₁²D₂²) to O(D₁D₂), making the approach practical for large CLIP encoders.

---

## Weaknesses

### Fatal
None.

### Major

- **Catastrophic and unexplained task failures at 50% compression (Table 2, lines for ViT-39M):** At the "base" scale (50% compression), CLIP-Map collapses on several benchmarks: STL10 **13.0 vs TinyCLIP's 93.2**, VOC2007 **22.2 vs 76.0**, Oxford Pets **48.5 vs 80.8**. STL10 at 13.0% is barely above random chance for a 10-class benchmark. This occurs while the same model achieves 97.3% on ImageNet-1K and competitive retrieval in Table 1 (55.1 vs 54.9 MSCOCO TR@1). This severe and inconsistent failure pattern is entirely unacknowledged in the paper. Section 4.2 states "competitive performance at the base scale, achieving results comparable to the baseline," which is contradicted by these results. Whether the failure stems from depth compression, a pathological feature subspace interaction, or the width mapping at this compression ratio is unknown—but the silence on it is a meaningful gap that misleads readers about the method's reliability.

- **Baseline comparison is too narrow to support the central claim:** The claim that "mapping-based compression beats select-based compression" rests entirely on TinyCLIP as the single matched-condition baseline. Other methods (MoPE-CLIP, CLIP-KD, UPoP) appear in Table 3 under different parameter budgets or training data, preventing direct comparison. This weakens the paper's generalization claim.

### Minor

- **"Fewer training epochs" efficiency claim is overstated for the 50% setting:** At 1% and 10% compression, TinyCLIP uses progressive compression (3×25ep and 2×25ep), so CLIP-Map's 25 total epochs is genuinely more efficient. However, at 50% compression, TinyCLIP uses a single 25-epoch run—the same total budget as CLIP-Map (5 mapping + 20 retraining). The paper presents "fewer epochs" as a general advantage without this caveat.

- **Non-monotone Table 4 behavior unexplained:** At 1 mapping epoch, IN-1K accuracy (39.6%) drops below the manual-drop baseline (41.1%) while MSCOCO TR@1 (35.7) already exceeds it (33.8). This divergence between metrics during early mapping optimization is interesting but unexplored.

### Trivial
None verified.

---

## Nice-to-Haves

- An ablation comparing diagonal initialization at 0 mapping epochs (pure weight inheritance, no optimization) vs. the full mapping-optimization pipeline would clarify whether the gain comes from the initialization alone or from the learned compression mapping. This single experiment would greatly sharpen the mechanistic argument.
- A qualitative analysis of which feature subspaces or depth-compression patterns are responsible for the STL10/VOC2007/Oxford Pets failures at 50% compression would both explain the anomaly and potentially point toward a fix.
- Discussion of L_depth initialization (Eq. 2) in the main body, given the detailed treatment of F_in/F_out initialization in Section 3.2.3.

---

## Removed Points

*These points are flagged as removed; treat with caution.*

- **"Full-Mapping naming is misleading"** (Harsh Critic): Removed. Section 3.2.2 clearly defines Full-Mapping as meaning all parameters are transformed (vs. hybrid inherit/map schemes), and Eqs. 3–4 make the Kronecker structure explicit. Readers engaging with the math will not confuse "full" with "full-rank."

- **"Information preservation narrative is asserted not demonstrated"** (Harsh Critic): Removed as a standalone weakness. The core claim—better initialization leads to better final model—is empirically supported by Table 4. The non-monotone ablation behavior is retained as a Minor weakness.

- **"The appendix may contain L_depth initialization detail"** (Harsh Critic assertion): Section 3.2.3 states "The initialization strategy for F_in and F_out across different components is illustrated in detail in A.3"—the appendix exists and discusses initialization. L_depth's absence from the main text is a minor point, not a major gap.

- **Generic strength: "This paper addressed an important problem"** (Strength Finder): Removed as insufficiently specific.

---

## Novel Insights

The Diagonal Inheritance Initialization exposes a non-obvious failure mode in applying Kronecker factorization to compression: while zero-mean initializations are generally safe for standard linear layers, they are pathological for Kronecker-factored mappings because variance scales multiplicatively (σ_A² · σ_B²) rather than additively, causing the composed transformation to be either near-zero or explosive depending on the initialization scale. The diagonal fix—initializing each factor as a (truncated) identity matrix—ensures the composition approximates identity at initialization and sidesteps this problem entirely. This insight generalizes beyond CLIP compression to any setting where two independently parameterized matrices form a Kronecker product used as a weight transformation.

---

## Suggestions

1. **Address the Table 2 failures directly in the main body.** Analyze whether the STL10/VOC2007/Oxford Pets failures at 50% compression are attributable to depth compression, specific width-mapping behavior, or something else. A targeted ablation (depth-only compression vs. width-only at 50%) could isolate the source.

2. **Revise the "competitive at base scale" claim** to reflect the actual mixed picture: strong on retrieval and ImageNet, but with specific zero-shot classification failures that merit attention.

3. **Add one contemporaneous matched-conditions comparison** (e.g., UPoP or MoPE-CLIP at 10% compression with matched YFCC15M data) to substantiate the claim that mapping-based compression outperforms select-based compression beyond TinyCLIP.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `XCugWIuHR8.md` | 3.0 | R1-weak | CLIP compression via convex optimization, rejected; clearly weaker execution and narrower scope than CLIP-Map |
| `FwkYeLovHk.md` | 3.33 | R1-weak | CLIP weak-to-strong generalization, rejected; different problem |
| `I5S1a1NKxo.md` | 5.0 | R1-mid | Data-scarce VLM distillation, rejected; narrower contribution, less validated |
| `LC6ZtQV6u2.md` | 6.5 | R1-mid | Compressing vision foundation models (Proteus), accepted; clean results across 15 benchmarks, broader evaluation, no analogous failures |
| `2y8XnaIiB8.md` | 5.5 | R1-mid | VL dataset distillation; different problem |
| `5Ca9sSzuDp.md` | 8.0 | R1-strong | CLIP interpretation paper; clearly stronger contribution |
| `VFhJtV29jZ.md` | 4.75 | R2 | SlimLLaVA pruning, rejected; comparable scope, weaker ablations |
| `iIT02bAKzv.md` | 5.5 | R2 | ECoFLaP layer-wise VLM pruning, accepted; comparable technical depth, but CLIP-Map has stronger initialization insight and clearer ablation |
| `1xG3MN1RRW.md` | 5.2 | R2 | SparseVLM token sparsification, rejected; training-free, narrower claim |
| `6VhDQP7WGX.md` | 5.8 | R2 | VLM inference optimization; different problem |
| `QDkPAV9Fa5.md` | 5.75 | R2 | Transformer KD optimization; different problem |

**Round 1 bracket: 5.0–6.5**

**Round 2 narrowing:** The most directly comparable anchors are `iIT02bAKzv` (5.5, Accept) and `LC6ZtQV6u2` (6.5, Accept). CLIP-Map has stronger and more clearly motivated novelty than ECoFLaP (whose contribution is a "straightforward combination of existing techniques"), which argues for ≥5.5. However, CLIP-Map is weaker than Proteus/LC6ZtQV6u2: Proteus delivers clean results across 15 benchmarks with no analogous failure modes, while CLIP-Map has unexplained near-random performance on STL10 (13.0 vs 93.2) and VOC2007 (22.2 vs 76.0) at the most practical compression level, plus overclaimed conclusions about "competitive base-scale performance." The contribution at 1%/10% compression is genuine, but the 50% failures and narrow baseline infrastructure keep this paper below the 6.5 anchor.

**Final score: 5.0** — The paper's genuine contributions (Diagonal Init, extreme-compression results) are offset by the major unexplained failures at 50% compression and the overclaimed "competitive at base scale" conclusion. This places it below the ECoFLaP anchor (5.5, accepted with reservations) and well below the Proteus anchor (6.5).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>