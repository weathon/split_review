Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes DVCL (Distance-aware Voxel-wise Contrastive Learning) for semi-supervised multi-organ segmentation. The key insight is that existing complementary-label VCL methods can disrupt semantic relationships among unreliable voxels (close voxels get pushed apart, distant ones pulled together). DVCL instead identifies "neighbors" and "outsiders" in feature space and uses a contrastive loss that pulls neighbors together while pushing outsiders apart, preserving these relationships. A secondary contribution is an entropy-based selection module (ESM) that adaptively separates reliable/unreliable pseudo-labels and reweights the CPS loss. Experiments on FLARE 2022, AMOS, MMWHS, and BTCV show consistent SOTA improvements (e.g., +2.02% mean Dice on FLARE 2022 with 10% labels over the second-best method).

## Strengths

1. **Well-motivated problem identification.** The paper clearly demonstrates (Figure 1(b)) a genuine limitation of complementary-label VCL: pushing unreliable voxels away from complementary prototypes can break semantic relationships that are useful for segmentation. This conceptual contribution challenges the rationale of prior work (U²PL, BaCon, CCL).

2. **Consistent SOTA results across four datasets and two label ratios.** The gains are substantial and reproducible: +2.02% mean Dice on FLARE 2022, +5.28% on AMOS, +2.01% on MMWHS, and +2.53% on BTCV over the second-best method. The Dice curves (Figure 4) show that DVCL learns effective features for challenging organs (right adrenal gland, pancreas) thousands of iterations earlier than competitors, which is practically meaningful.

3. **Ablation isolates the DVCL contribution.** Table 2 confirms that DVCL alone adds +2.1% mean Dice over the baseline, and the full method (+EBL) adds +3.06%. This cleanly separates the effect of the relationship-preserving contrastive mechanism from the entropy-based reweighting.

4. **Thorough comparison against related nearest-neighbor VCL methods.** Table 4 compares DVCL with NNCLR-like alternatives and shows DVCL outperforms them, validating the specific design (neighbors + outsiders with set-level contrastive learning).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contribution is well-motivated, coherently designed, and empirically validated across multiple datasets.

### Minor

1. **No empirical verification that neighborhoods are actually preserved.** The central claim of DVCL is that it "maintains useful semantic relationships among unreliable voxels" (neighbors remain neighbors, outsiders remain outsiders). Yet the paper provides no quantitative measurement of this. How many neighbor pairs remain K-NN after training? Does this correlate with the Dice improvement? Without such verification, the mechanism is a plausible-but-unconfirmed explanation for the empirical gains. The authors should measure neighborhood preservation over the course of training (e.g., fraction of neighbor pairs that remain nearest neighbors, or precision/recall of the K-NN graph against ground-truth class boundaries on a held-out set).

2. **Key hyperparameters lack ablation or justification.** Three hyperparameters are set without sensitivity analysis: (a) the entropy threshold factor α = 0.5 in τ_e = e_at + α·e_st, (b) the DVCL loss weight β = 0.3, and (c) the denominator log₂ C in the weight function W_max·exp(-e/log₂ C). While Table 3 ablated K and K', these other choices could affect results. An ablation sweep over a plausible range for α and β would improve confidence in the method's robustness.

3. **No analysis of computational overhead.** K-NN search over unreliable voxels per mini-batch could be expensive, especially for large 3D volumes. A comparison of training time per iteration against competing methods (e.g., U²PL, BaCon) would help readers assess the practicality of DVCL.

4. **No discussion of when DVCL might not help.** The method is applied throughout training, but at very early epochs (when most voxels are unreliable and features are random) or very late epochs (when few unreliable voxels remain), DVCL could be unnecessary or harmful. A stage-wise analysis or an ablation that applies DVCL only during certain training intervals would clarify its utility.

### Trivial
None that survive filtering — the observed formatting issues are parser artifacts, not author errors.

## Nice-to-Haves
- An ablation of α (threshold factor) and β (loss weight) over a plausible range to demonstrate robustness.
- A runtime comparison (training time per iteration) against U²PL or BaCon to assess the practical cost of K-NN search.
- A measurement of neighbor-set overlap between consecutive training epochs to show neighbor assignments stabilize over time.

## Removed Points
The following criticisms from the harsh review were removed as they reflect misunderstandings or parser artifacts:

1. **"Incoherent derivation of DVCL loss and internal inconsistency"** — The harsh critic claims the derivation in Eqs. 14–17 is "garbled or fallacious" and that there is an "internal inconsistency" between neighbor selection (feature space) and loss application (prediction space). *Reason for removal:* (a) The equations are garbled in the parsed text due to parser limitations, not author errors. The original PDF submission has properly typeset equations. (b) The claimed "inconsistency" misreads the paper. The paper's logic is explicit (line 145): "features that are close or distant in the feature space should yield consistent or inconsistent predictions." Neighbors are defined by feature cosine similarity, and the loss enforces that these neighbors have similar **predictions** (p_m^T p_n high). This is a coherent and standard design — the feature space defines the relationship, and the prediction space is the optimization target. There is no mismatch.

2. **"Circularity in neighbor selection and risk of confirmation bias"** — The harsh critic argues that early-stage unreliable features cause noisy K-NN graphs that DVCL might "lock in" as confirmation bias. *Reason for removal:* This concern applies equally to virtually all SSL methods that use pseudo-labels or self-training (including the baselines the paper compares against). The paper's entropy-based selection already focuses on "unreliable" voxels (where the model is uncertain), which is a reasonable mitigation. The critic provides no evidence that DVCL's neighbor-based approach is more susceptible to this than alternative methods. The suggestion to measure neighborhood quality is valid (kept as Minor weakness #1), but the framing as a "circularity" issue is overstated.

3. **"ESM is very similar to U²PL with marginal novelty"** — *Reason for removal:* The paper explicitly cites Wang et al. (2022c) for entropy-based selection (line 65). The claimed novelty is the O(1) vs O(log N) complexity improvement and the exponential weighting scheme, which are modest but not incorrect. The harsh critic's framing as a weakness is a matter of opinion on novelty rather than a verifiable error. The paper's main claimed novelty is DVCL, not ESM.

4. **"Self-supervised learning related work is disconnected"** — *Reason for removal:* The related work on NNCLR connects to the use of nearest-neighbor queues in DVCL (line 157: "Following Dwibedi et al., we use queues as candidate sets"). It is not disconnected.

5. **"DVCL can be applied to other tasks — no evidence"** — *Reason for removal:* This is a forward-looking statement in the conclusion (line 245), not a core claim requiring validation in this paper.

6. **"No discussion of when unreliable voxels are very large/small"** — Kept as Minor weakness #4 (analysis of failure cases or regimes), but the critic's framing as a "missing part" was excessive for what is a suggestion for future work.

7. **"Tables not visible"** — *Reason for removal:* The tables are present as embedded images in the parsed text; the numerical results are described in the text (lines 208–213, 232–238). This is a parser limitation.

## Novel Insights

The most interesting observation bridging the reviews is that the paper identifies a genuinely non-obvious failure mode of complementary-label VCL — that pushing unreliable voxels away from prototype of a "least likely" class can distort relationships that were actually correct. This is a more subtle problem than the standard "confirmation bias" concern in SSL, and the proposed solution (preserve feature-space neighborhoods via a set-level contrastive loss) is a natural fit. The strong and consistent empirical gains across four anatomically diverse datasets suggest the mechanism is capturing something real.

## Suggestions

1. **Measure neighborhood preservation directly.** Track the fraction of K-NN pairs that remain K-NN after applying DVCL over training, compared to a baseline using complementary labels. This would directly confirm the mechanism.
2. **Add ablation sweeps for α (entropy threshold factor) and β (DVCL loss weight).** Even a 3-point sweep (e.g., α ∈ {0.3, 0.5, 0.7}, β ∈ {0.1, 0.3, 0.5}) would significantly strengthen the claim of robustness.
3. **Include a runtime comparison.** Report training time per iteration for DVCL vs. U²PL and BaCon to help readers assess the practical cost of K-NN search on unreliable voxels.

## Score and Decision

This is a solid empirical paper with a well-motivated idea, clean ablations, and strong results across four datasets. The core contribution (DVCL) is coherent: the design uses feature-space neighborhoods to define relationships and prediction-space agreement as the optimization target. The weaknesses are addressable (missing hyperparameter ablations, no direct measurement of the claimed mechanism). None are fatal or threaten the paper's central claims.

**Originality**: 7/10 — The problem identification (complementary labels disrupt relationships) is genuinely insightful. The loss formulation builds on existing techniques (InfoNCE, NNCLR) but applies them in a novel setting (unreliable voxel relationships in MoS).

**Importance**: 8/10 — Multi-organ segmentation is clinically important, and semi-supervised methods that better use unreliable pseudo-labels are practically valuable.

**Claims support**: 7/10 — Empirical support is strong, but the central mechanistic claim (neighborhood preservation) lacks direct verification.

**Soundness**: 7/10 — Experiments are thorough (4 datasets, 2 label ratios, 3 runs with SD). Minor gaps in hyperparameter analysis and mechanism verification.

**Clarity**: 8/10 — Well-structured, clear motivation. Equations are complex but the intuition is clearly conveyed.

**Value**: 8/10 — The DVCL idea could generalize to other segmentation tasks with unreliable labels.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>