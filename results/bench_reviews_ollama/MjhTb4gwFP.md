## Summary
PerLDiff is a diffusion-based street-view generator that injects perspective-projected 3D bounding-box and road-map masks as additive biases inside cross-attention (a PerL-CM module bolted onto Stable Diffusion). The paper reports large gains in perception-based controllability metrics (mAP/NDS, mIoU) on NuScenes and KITTI relative to BEVControl* and MagicDrive*, plus a data-augmentation experiment showing synthetic validation data nearly closes the gap to real validation data.

## Strengths
- The augmentation experiment (Table 3) is concrete and well-targeted: training on `train + Syn. val` reaches 31.66 mAP for BEVFormer vs. 32.20 with real `val` (a 0.54-pt gap), and a similar pattern holds for StreamPETR. This is the most credible evidence that the generated images carry information beyond the conditioning box itself.
- The ablation in Table 4 cleanly localizes the source of the headline gains: adding the box mask alone (row c) lifts mAP from 16.48 → 26.07. Whatever one thinks about the metric (see Major-1), the experiment is well-designed and transparent about where the improvement is coming from.
- The mechanism is mathematically simple and the paper states it plainly (Eq. 5): `softmax(λ·M + QKᵀ/√d)`, a binary in-box mask added as an attention logit bias. This makes the method easy to evaluate, reproduce, and integrate.
- Honest failure-mode disclosure: the front/rear yaw flip is acknowledged and traced to the orientation-agnostic 2D box mask (Section 5 / Fig. on limitations).

## Weaknesses

### Fatal
None.

### Major
- **The dominant gain is partially tautological by construction (Table 4 row c).** Injecting a binary in-box mask as an attention bias forces the generator to place content at the exact pixel footprint the downstream detector is asked to recover. Row (c) reaches mAP 26.07, within 1 point of the Oracle (27.06), *without* the road mask and with only marginally lower FID. The headline mAP/NDS gains in Tables 1–2 therefore measure "the generator paints inside the supplied box" as much as they measure generative fidelity. The paper never disentangles these — e.g., by ablating the box mask while keeping H_b cross-attention content, perturbing boxes at generation time, or measuring detector performance under shifted/rotated conditioning. The one counterweight metric (FID) is *worse* than BEVControl* (13.36 vs 13.05) and is dismissed with the qualitative claim that "prior constraints… may adversely affect the details in the background," which is asserted, not measured.
- **Baseline reproductions are materially weaker than the published numbers, and SOTA framing leans on the weakened reproductions.** Original MagicDrive reports mAP 12.30 / NDS 23.32 on BEVFusion; the paper's MagicDrive* gets 10.27 / 20.42 (Table 1). BEVControl is likewise re-run as BEVControl*. The paper does not explain why its re-implementations underperform the original publications, nor justify using them as the head-to-head reference. PerLDiff still beats the *original* MagicDrive (15.24 vs 12.30 mAP), so the SOTA claim is not entirely dependent on the weakened baselines, but the magnitude of BEVControl* comparisons (e.g., +8.62 mAP) is partly attributable to a degraded baseline.
- **No quantitative comparison against the closest geometric-prior baselines (BoxDiff, ZestGuide).** Section 2.3 motivates PerLDiff explicitly against these methods — arguing training-time priors are superior to inference-time attention manipulation — but no numerical comparison is reported. This is precisely the comparison that would substantiate contribution (ii).

### Minor
- **KITTI head-to-head is weakly framed.** BEVControl* gets 0.33 mAP (Easy) vs PerLDiff's 11.04, but the paper itself notes that KITTI has only 3,712 training images and no road map, conditions BEVControl was not designed for. The paper offers reasonable interpretation (sensitivity to depth/size), but the 30× gap is partly an artifact of running the baseline outside its intended setting. A within-method ablation on KITTI (with/without box mask) would be more probative than the side-by-side.
- **Limited ablation coverage.** Beyond mask presence and λ, the paper does not ablate: keeping the box mask but removing H_b cross-attention content (would directly test the tautology concern), the ConvNext map encoder choice, alternatives to Fourier encoding, or the gating mechanism. The first of these is the most consequential and would either strengthen or rebut Major-1.
- **Novelty relative to GLIGEN's gated attention and segmentation-conditioned attention biasing is asserted but not isolated.** The paper says PerL-CM uses gating "similar to GLIGEN" but does not delineate what is new beyond replacing GLIGEN's grounding tokens with a binary in-box logit bias.
- **The "predefined network architecture" critique of prior work (line 5) is never operationalized.** PerLDiff is itself a predefined architecture; the actual differentiator is the mask-as-bias, not architectural flexibility.

### Trivial
None retained.

## Nice-to-Haves
- Robustness study: perturb conditioning boxes (small shifts/rotations) at generation time and measure how perception metrics degrade — this would directly probe whether the model has learned object semantics vs. mask-filling.
- FID decomposed by foreground/background to test the paper's own explanation for its FID regression.
- A perceptual or VLM-based realism study, since the paper itself argues FID is the wrong metric.
- Failure cases beyond the orientation flip — e.g., implausible box placements.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *Harsh critic's "Section 4.2 sentence truncation"* — parser artifact (the text cuts at "As illustrated in Fig."), not an author error.
- *Harsh critic's note on FID dismissal being unprincipled* — Substantive part already retained in Major-1; the rest is a presentation nitpick.
- *Strength Finder #3 (attention-map visualization is direct evidence)* — Cross-attention map visualization showing sharper alignment is largely circular evidence given the mask is added directly to the attention logits; attention sharpening is by construction, not an independent confirmation.
- *Strength Finder claim that the method is "reproducible and transparent"* — Generic boilerplate; kept implicitly under the simple-mechanism strength but not as a standalone bullet.

## Novel Insights
The most useful synthesized observation is the box-mask tautology concern: because the additive mask uses the same projected 3D box geometry that the downstream detector is evaluated against, perception-based controllability metrics on synthetic data partially measure compliance with the conditioning, not generative quality. The ablation actually quantifies this — row (c) of Table 4 alone nearly hits Oracle — making the metric design (and the absence of perturbed-box or generative-quality counterweights) the central interpretive issue of the paper.

## Suggestions
- Add an ablation that keeps the binary box mask but removes the H_b cross-attention content (or vice versa), to disentangle "placement by mask" from "object generation."
- Re-run MagicDrive and BEVControl at the authors' published configurations/resolutions, or explicitly document why reproductions diverge; report both numbers side-by-side.
- Add a quantitative comparison against BoxDiff and ZestGuide on at least one of NuScenes or KITTI to back Section 2.3.
- Evaluate perception metrics under perturbed conditioning boxes (shift/rotate the box at generation time, evaluate detector on real boxes); this gives a controllability metric that is not aligned with the mask.
- Report FID decomposed into in-box and out-of-box regions to support the paper's own explanation of the FID regression.

---

**Axis-by-axis assessment.** *Originality:* moderate — a clean, well-executed combination of in-box attention biasing with the autonomous-driving controllable-generation setting, but the underlying mechanism (mask-as-logit-bias) is a known idea. *Importance:* the controllable-generation-for-perception problem is genuinely important. *Claim support:* uneven — the augmentation result is compelling, but the SOTA / controllability headline is undermined by the box-mask tautology and weakened baselines. *Soundness of experiments:* adequate breadth across detectors/datasets, but the missing ablations and the absence of geometric-prior baselines (BoxDiff/ZestGuide) leave the central methodological claim partially unsupported. *Clarity:* generally good; the method is explained with equations and figures. *Value to community:* real — the augmentation pipeline and the simple recipe are likely to be useful — but limited until the controllability evaluation is decoupled from the conditioning shortcut.

The paper has a real contribution (the augmentation result is strong, the recipe is simple and works), but the headline controllability claim is over-supported by a metric that partly bakes in the answer, and the closest methodological baselines are not compared.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>