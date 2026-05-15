Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

Here is my analysis of each major criticism against the actual paper content:

**Critical Issue 1 verification**: The paper explicitly acknowledges in Section 4.3: "First, the models are not directly comparable" and "Second, in this work we do not focus on tuning the performance." The asymmetry (simpler MLP decoder vs. autoregressive/top-k decoders) favors the baselines, not OCEBO. Per the rules: remove criticisms about unfair comparison when asymmetry favors baselines. However, the critic's point about not being able to attribute numbers to bootstrapping alone is partially valid — but the paper is transparent about this and its claim is "comparable" (not "superior"). I'll significantly weaken this.

**Critical Issue 2 verification**: The paper uses only two dataset sizes (COCO ~118k, COCO+ ~241k). This is indeed minimal evidence for a "scalability" claim. Valid concern but not fatal.

**Critical Issue 3 verification**: The value of k in k-NN patch filtering is never specified in the paper. Confirmed by grep. This is a concrete reproducibility gap. ✓

**Critical Issue 4 verification**: The paper cites Didolkar et al. (2024) for the plateau claim and doesn't run this experiment itself. This is scope creep — a paper need not re-validate every cited claim. Moving to nice-to-have.

Now producing the final review.

---

## Summary

OCEBO proposes a self-distillation framework for training object-centric models from scratch on real-world data via EMA target encoder updates and cross-view patch filtering. The key idea is to inject object-centric inductive biases into the target encoder itself, removing the upper bound imposed by frozen non-object-centric encoders. When pretrained on ~241k COCO images, OCEBO achieves unsupervised object discovery performance comparable to models relying on encoders pretrained on 142M images.

## Strengths

- **First demonstration of object-centric pretraining from scratch on real-world data without slot collapse.** Prior work required frozen pretrained encoders (DINO/DINOv2) to avoid collapse; OCEBO achieves this with random initialization on COCO (118k–241k images). Table 1 and Figure 2 provide clear evidence: without the proposed patch filtering, collapse occurs immediately (d = −0.48), while the full method maintains d > 0.4.

- **Cross-view patch filtering mechanism that enables stable bootstrapping from a randomly initialized target encoder.** The mutual nearest-neighbor condition provides a self-supervised proxy for feature quality, starting from ~10% supervised patches and rising to ~70% by epoch 200 (Figure 2). Ablation in Table 1(a) shows omitting this filter causes immediate collapse.

- **Convincing ablation evidence that both key components are necessary.** Table 1 systematically ablates: (a) removing patch filtering → collapse (d = −0.48); (b) removing the object-centric loss (λ_oc = 0) → collapse; and (c) showing mask sharpening further improves mBO. These ablations demonstrate the method is not trivial.

- **Comprehensive zero-shot evaluation across diverse datasets.** OCEBO is evaluated on MOVi-C, MOVi-E, Pascal VOC, and EntitySeg using both FG-ARI and mBO, comparing against multiple state-of-the-art methods (Table 2). The zero-shot protocol (training on COCO, testing on held-out datasets) is a principled evaluation choice.

- **Quantitative measure of slot collapse (d).** The paper introduces a simple, interpretable metric to diagnose slot collapse based on cross-view patch similarity, which is used consistently throughout the analysis.

## Weaknesses

### Fatal
None.

### Major

- **The hyperparameter k in cross-view patch filtering is never reported.** Section 3.3 defines the filtering condition using "k nearest neighbors," but the paper nowhere specifies the value of k used in experiments (nor whether it was tuned). This is a concrete reproducibility gap — the filtering mechanism cannot be re-implemented without this value. (The same is true for the distance metric used to determine nearest neighbors — cosine vs. L2 vs. other.)

### Minor

- **Scalability evidence is limited to two dataset sizes.** The "scalability" claim rests on comparing COCO (~118k) to COCO+ (~241k). While the results show consistent FG-ARI improvement, the trend is suggestive rather than definitive. The mBO decrease on MOVi-E (30.6 → 29.6) is acknowledged but hand-waved. Two data points do not establish a scaling trend. This weakens the paper's contrast with the "plateau at 16k" claim from prior work.

- **The global loss L_global is not ablated.** The training objective is L = λ_oc L_oc + λ_global L_global with λ_oc = λ_global = 1, but the paper never evaluates setting λ_global = 0. This leaves the contribution of the global loss to the method's success empirically uncharacterized.

- **The "optional" mask sharpening stage creates ambiguity about the core method.** Section 3.4 describes the sharpening stage as optional, yet it is used in all final results (300 epochs self-distillation + 100 epochs sharpening). The paper would benefit from clearer framing: is OCEBO the two-stage process, or just the self-distillation phase? And the sharpening stage reverts to a frozen-target L2 reconstruction loss — the very paradigm OCEBO is designed to replace (albeit with a bootstrapped target encoder). The contribution of the bootstrapping phase vs. the sharpening stage is not isolated.

- **The PCA visualizations (Figure 3) compare OCEBO (ViT-S/16) against DINOv2 (ViT-B/14).** The architectural difference (small vs. base ViT) introduces a confound: the better instance separation could partly be due to OCEBO's smaller feature space or different training data rather than bootstrapped object-centric inductive biases.

### Trivial
- The paper does not discuss scenarios where the cross-view patch filtering assumption might fail (aggressive cropping, uniform regions, heavy blur), though the dynamic mask percentage (Figure 2) partially addresses this by naturally filtering uninformative patches.

## Nice-to-Haves
- A controlled comparison holding the decoder architecture fixed (e.g., OCEBO's bootstrapped target vs. a frozen DINOv2 target, both with the same MLP decoder) would more cleanly isolate the benefit of bootstrapping.
- An ablation of λ_global to characterize its contribution.
- Reporting variance (error bars / seeds) for the main results would strengthen reliability claims.
- Training on a larger object-centric dataset (e.g., SA-1B filtered for multi-object scenes) would better demonstrate scalability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critical Issue 1** (decoder architecture confound makes central claim unsupported): The paper explicitly acknowledges the models are not directly comparable (Section 4.3: "First, the models are not directly comparable... we do not focus on tuning the performance"). Moreover, the decoder asymmetry (OCEBO uses a simple MLP decoder; baselines use stronger autoregressive/top-k decoders) **favors the baselines**, making OCEBO's "comparable performance" despite this disadvantage a stronger, not weaker, result. Per the rules, criticisms about unfair comparison when asymmetry favors the baseline are removed.

- **Critical Issue 4** (evaluation misalignment — paper should run its own frozen-target plateau experiment): The paper cites Didolkar et al. (2024) for this claim. Asking the paper to revalidate every cited result is scope creep; the motivation is well-supported by prior work.

- **Section 3.1 concern about invaug implementation**: The paper references Wen et al. (2022) for details. This is standard practice for citing prior work.

- **Claim that d (slot collapse measure) is never reported in Table 1**: The Table 1 caption explicitly states "We report the quantitative measure of slot collapse d described in Section 4.2." The table (rendered as an image) likely contains these values. The reviewer appears to have missed them.

- **Demand for 4+ dataset sizes with confidence intervals**: This asks for a methodology rigor (multi-point scaling curves with CIs) that is not standard practice in this field's empirical papers. The paper's two-point comparison is limited but not invalid.

## Novel Insights

None beyond the paper's own contributions. The key insight — that EMA updating the target encoder with object-centric inductive biases avoids the collapse observed in prior bootstrapping attempts, and that a mutual nearest-neighbor patch filter enables starting from random initialization — is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. **Report the value of k** used in cross-view patch filtering (and the distance metric) to resolve the reproducibility gap. This is the single most impactful fix.
2. **Frame the two-stage process more clearly** — specify what "OCEBO" refers to (self-distillation only, or self-distillation + sharpening), and ideally provide an ablation comparing both stages individually against the combined method.
3. **Add at least one more dataset size** (e.g., a 50k subset of COCO) to strengthen the scalability evidence.
4. **Ablate λ_global** to clarify whether the global loss is necessary or primarily ornamental.

## Score and Decision

The paper presents a novel and well-motivated framework for training object-centric models from scratch on real-world data — a first in the field. The core ideas (EMA target encoder bootstrapping, cross-view patch filtering) are clean, the ablations convincingly show both components are necessary, and the zero-shot evaluation protocol is principled. The main weaknesses are the unreported value of k (a concrete reproducibility gap) and thin scalability evidence, neither of which invalidates the core contribution. The paper is a solid empirical contribution that opens a new direction for object-centric pretraining.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>