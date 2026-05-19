- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8
Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me produce the final consolidated review.

## Summary

This paper introduces the Influencer Backdoor Attack (IBA) for semantic segmentation, where a trigger placed on non-victim pixels causes misclassification of a victim class (e.g., cars misclassified as road). Two variants are proposed: Nearest-Neighbor Injection (NNI), which places the trigger near victim pixels, and Pixel Random Labeling (PRL), which relabels random non-victim pixels with other classes from the same image during training to encourage broader contextual learning. Experiments on PSPNet, DeepLabV3, and SegFormer across PASCAL VOC and Cityscapes show that both techniques improve attack success rate over a randomly-placed trigger baseline, with PRL being particularly robust to large trigger-victim distances.

## Strengths

1. **Novel and well-motivated problem formulation.** Section 3.1 formally defines IBA with the key constraint that the trigger must be placed on non-victim pixels and cannot occupy a fixed location. This differs meaningfully from prior segmentation backdoor attacks (Li et al. 2021 uses a static black line at the top of images; Mao et al. 2023 places the trigger on the victim class itself). The formulation is motivated by realistic real-world constraints where trigger-victim distance is uncontrollable.

2. **PRL enables high attack success even with large trigger-victim separation.** Table 1 shows PRL achieves 94.31% ASR when the trigger is 120–150 pixels away from victim pixels at 15% poisoning rate, while baseline IBA drops to 73.54% and NNI drops to 72.13% under the same condition. This is the paper's strongest empirical result and directly supports its core claim.

3. **Low poisoning rates achieve high attack success.** Figure 2 shows PRL reaches approximately 95% ASR with only ~5% poisoning on VOC and ~7% on Cityscapes, compared to 10–20% for baseline IBA. This demonstrates practical stealthiness.

4. **Systematic ablation of PRL design choices.** Figure 3/4 compares four label-replacement strategies (null, fixed class, all dataset classes, classes in same image). The proposed strategy (classes in the same image) is the only one that continuously improves ASR without degrading benign accuracy up to 75,000 relabeled pixels — providing concrete evidence for the design choice.

5. **Evaluation across multiple architectures and datasets.** Experiments use three segmentation models (PSPNet, DeepLabV3, SegFormer) and two datasets (VOC, Cityscapes), demonstrating that IBA and its variants generalize beyond a single model-domain combination.

## Weaknesses

### Fatal
None.

### Major

1. **PRL mechanism is asserted without diagnostic evidence.** The paper claims PRL works by "forcing the model to learn the image's global information" and "enhancing context aggregation ability" (Section 4.2, lines 109–113). This explanation is presented as the *reason* PRL improves ASR, but no evidence — attention analysis, gradient attribution, or diagnostic experiments (e.g., testing on cropped images to measure context dependence) — is provided to link PRL to increased context use. Alternative explanations are equally consistent with the data: PRL injects label noise that could (a) increase effective poisoning rate by reducing model confidence in non-victim classes, (b) create a shortcut where the trigger becomes the most reliable predictor for victim pixels, or (c) degrade local pattern resolution so the model falls back on coarse contextual cues. The ablation in Figure 3/4 tests *which* label choice works but does not probe *why* it works. The claimed mechanism is plausible, but without diagnostic experiments the conclusion is incompletely supported.

2. **No experimental comparison to prior segmentation backdoor attacks.** The related work (Section 2, line 52) cites Li et al. (2021) and Mao et al. (2023) as prior segmentation backdoor attacks and describes differences in their threat models and trigger designs. Yet no experiments compare IBA against either method, even partially. Without any empirical comparison, the reader cannot assess whether IBA offers a genuine advantage over adapted versions of these prior methods, or whether the proposed techniques (NNI, PRL) provide benefits beyond what simple adaptations of existing attacks would yield. This limits the paper's ability to substantiate its claim of novelty or superiority.

### Minor

1. **Standard deviations missing from main results table.** Table 1 (distance-controlled experiment) reports standard deviations from 3 runs, but Table 2 (main comparison across poisoning rates, Cityscapes deep_cs_baseline) reports only point estimates. Given that backdoor attacks are stochastic (poisoned sample selection, trigger positioning, training), the absence of variance information makes it impossible to assess whether reported improvements (e.g., PRL 66.89 vs NNI 54.89 at 1% poisoning) are statistically significant or could arise from a single lucky run.

2. **Distance bound parameters not explained.** The upper bound U is set to 30 for VOC and 60 for Cityscapes (line 139), and the lower bound L is 0 for both. The paper does not explain how these values were chosen or whether NNI's performance is sensitive to this hyperparameter. This matters because NNI's effectiveness depends critically on how close the trigger can be placed to victim pixels.

3. **Real-world experiment values not contextualized.** The real-world experiment (Section 6.3, line 216) reports baseline IBA ASR of 60.23%, but the poisoning rate used for the model is not stated in the main text. The real-world PRL ASR (64.29%) is only ~4 points above baseline, in contrast to controlled experiments where PRL substantially outperforms baseline (e.g., 66.89 vs 27.65 at 1% poisoning in Table 1). These differences are not discussed. (Note: the paper references the appendix for additional details, so this is a presentation gap, not an absent experiment.)

### Trivial

- The abstract's claim that segmentation backdoors have been "largely overlooked" sits somewhat uneasily with the two prior segmentation backdoor works cited in the related work. The paper does distinguish its threat model (trigger on non-victim pixels, random position) from these works, and the claim is defensible, but a qualifying phrase would be more precise.

## Nice-to-Haves

- **Diagnostic experiment for PRL mechanism.** Adding a controlled experiment — e.g., comparing attention maps or measuring sensitivity to pixels at varying distances under PRL vs. baseline — would turn the plausible story into supported evidence.
- **Comparison to an adapted classification backdoor baseline** (e.g., a simple BadNets-style patch with relabeling adapted to segmentation) would further anchor the results.
- **Discussion of why NNI is more robust to fine-tuning/pruning defenses** than PRL (Table 3). The paper notes NNI's superior robustness but does not speculate on why, which is a missed opportunity given the interesting asymmetry.
- **Additional trigger designs.** The paper acknowledges trigger design is orthogonal (line 16), but a more natural trigger (e.g., a logo or texture) would strengthen the real-world threat claim.

## Removed Points

- **Point about real-world experiment being "severely underspecified"** — The paper references "\ref{app:realworldexp}" for detailed specifications of the real-world experiment (presumably including poisoning rate, trigger distance distribution, etc.). Per the review guidelines, criticisms about missing appendix content are removed since the appendix was stripped by the PDF parser. A weakened version noting the ASR inconsistency between real-world and controlled experiments is retained as a Minor weakness.
- **Point about trigger size being "not negligible"** — The paper correctly defines the trigger as small relative to the image (0.57% of pixels). This is a presentation nitpick.
- **Point about "unfair comparison" framing** — The reviewer's complaint about comparing only to a random-trigger baseline is weakened because comparing to a simpler/weaker version of the proposed method is a valid starting point. The lack of comparison to *prior* segmentation backdoor attacks is retained as a Major weakness (different issue).
- **Point about defense analysis being shallow** — The paper explicitly scopes out exhaustive defense adaptation ("Exhaustive adaptation of current defense approaches is out of the scope of our work," line 265). Criticizing the paper for not doing more than it scoped is scope creep.
- **Point about trigger stealthiness (Hello Kitty being conspicuous)** — The paper acknowledges trigger design is orthogonal to the method (line 16). This is a design choice, not a flaw.
- **Generic strengths from Strength Finder that are superficial** (e.g., "addressed an important problem") — These are removed. The concrete strengths (numbered 1–5 above) are retained.
- **Speculative claims about PRL mechanism alternatives** (e.g., "increases effective poisoning rate," "creates a shortcut") — The existence of plausible alternatives is kept as a reason the claimed mechanism is unsubstantiated, but the specific speculative alternatives are not listed as weaknesses themselves; the weakness is the *absence of evidence* for the claimed mechanism.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface observations that meaningfully reframe or extend the paper's own findings beyond identifying where the evidence is and is not sufficient.

## Suggestions

1. Add a diagnostic experiment for the PRL mechanism: compare feature attribution or attention maps between models trained with and without PRL. For example, measure whether PRL-trained models show broader spatial attention or stronger sensitivity to distant pixels. Alternatively, test on images where local evidence contradicts global cues and measure whether PRL-trained models rely more on the global signal.
2. Include an experimental comparison against an adapted version of at least one prior segmentation backdoor attack (e.g., Li et al.'s fixed-position trigger or Mao et al.'s OFBA) on the same datasets. Even a partial comparison would contextualize the contribution.
3. Report standard deviations for all main results tables (at minimum, for Table 2) to match the reporting standard established by Table 1.
4. Clarify the poisoning rate used in the real-world experiment in the main text and discuss why the real-world ASR values (particularly the narrower gap between baseline and PRL) differ from the controlled digital setting.
