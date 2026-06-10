## Summary

This paper introduces Memory-Augmented Network (MAN), a supervised local learning framework that extends local learning beyond image classification to object detection and super-resolution. MAN consists of Simple Local Modules (SLM)—downsized copies of the backbone used as auxiliary networks—and a Feature Bank that stores task-specific key features (multi-scale FPN features for detection, initial image features for super-resolution) to address the "short-sightedness" of gradient-isolated local modules. Experiments are conducted on classification (CIFAR-10, STL-10, SVHN), object detection (VOC, COCO with RetinaNet and YOLO backbones), and super-resolution (DIV2K).

## Strengths

- **First strong demonstration that local learning can match end-to-end performance on object detection, with direct comparison against a prior local learning method.** On COCO with RetinaNet-R34, MAN achieves 28.9 mAP vs. BP's 28.7 mAP, while the only prior local learning baseline (DGL, enhanced with FPN structures to give it the best chance) achieves only 21.3 mAP (Table 3, lines 245–248). This 7.6-point gap is the paper's strongest evidence that the Feature Bank is solving a real limitation of prior local learning approaches.

- **Multiple configurations where MAN matches or exceeds end-to-end BP while saving GPU memory.** On VOC, RetinaNet-R50 MAN (56.5 mAP) exceeds BP (56.2 mAP) (Table 2). On COCO, RetinaNet-R101 MAN (31.9 mAP) exceeds BP (31.8 mAP) (Table 3). Memory savings reach 24.66% on YOLO-R34 (8.89 GB vs. 11.80 GB) and 28.77% on YOLO-R101 (Table 3). These are specific, quantified comparisons against the standard end-to-end baseline across multiple backbones and datasets.

- **Same architectural principle applied coherently across three different task types.** The SLM design (downsizing the backbone to create a task-aligned auxiliary network with n_{s,𝒜_i}=1 per stage) and the Feature Bank mechanism (storing task-specific key features) are applied to classification (fc features), detection (multi-scale FPN features), and super-resolution (initial image features) without per-task manual redesign of the auxiliary network (Sections 4.1–4.3).

- **Controlled comparison that isolates the Feature Bank as the cause of improvement.** The paper builds an FPN structure into DGL's auxiliary network via upsampling (Section 5.2, line 269) to give DGL the best possible chance at detection. Despite this enhancement, DGL's gap to BP is catastrophic (21.3 vs. 28.7 mAP), while MAN closes it to within 0.2 mAP. This controlled experiment strengthens the case that the Feature Bank, not merely better auxiliary network capacity, drives the improvement.

## Weaknesses

### Major

- **The super-resolution results contradict the paper's central "comparable to end-to-end" claim.** On DIV2K, MAN trails BP by 0.73 dB (×2), 1.71 dB (×3), and 1.21 dB (×4) in PSNR (Table SR, lines 304–311). In super-resolution, differences above ~0.3 dB are considered meaningful; the 1.71 dB gap at ×3 is large. The abstract claims MAN "achieves performance on par with end-to-end approaches," and the conclusion states "maintaining comparable performance to BP" — but these claims are misleading when applied to SR. Additionally, the SR backbone architecture is never specified, making it impossible to contextualize the gap. The paper acknowledges the gap in Section 5.3 but its textual framing throughout (abstract, introduction, conclusion) does not reflect this limitation.

- **The experiments provide essentially no training details, making the work structurally irreproducible.** The paper does not specify: which exact ResNet variant was used for classification (depth, number of parameters), number of training epochs, batch sizes, numerical values for learning rates (η_a and η_l are named in Eq. 1–2 but never given values), optimizer choice, weight decay, learning rate schedules, data augmentation, or number of independent runs. No standard deviations or confidence intervals are reported for any metric. Every numeric result in every table appears to come from a single run (lines 172–321, all tables). Without these details, readers cannot assess whether small differences (e.g., +0.05% on STL-10, +0.2 mAP on COCO) are meaningful or noise. This is not a trivial omission — it is a structural gap that prevents independent verification.

- **The core "first successful application of local learning beyond classification" claim is under-evidenced by the experimental design.** On VOC detection (Table 2), there are *no* local learning baselines at all — only BP. On super-resolution (Table SR), there are no local learning baselines — only BP. On COCO detection (Table 3), only one local learning baseline (DGL) is compared, and only on one backbone (RetinaNet-R34). To substantiate a claim of being the "first successful" extension, the paper should demonstrate that other local learning methods fail (or perform substantially worse) on these tasks. The DGL comparison on RetinaNet-R34/COCO provides one data point for this, but VOC and SR remain undefended. The paper even acknowledges that "because the traditional Local-learning method lacks the key information of the initial image, it leads to a catastrophic performance gap" for SR (Section 5.3, line 321) — but this is asserted, not demonstrated experimentally.

### Minor

- **The ablation study conflates SLM and Feature Bank, preventing isolation of their individual contributions.** The ablation (Table Ablation, lines 288–292) compares three configurations on RetinaNet-R34/COCO: (a) no Adapt, no Head; (b) Adapt yes, Head no; (c) Adapt yes, Head yes. The "Adapt" variable represents using both SLM *and* Feature Bank together. There is no configuration that separates SLM from Feature Bank (e.g., SLM alone without Feature Bank, or Feature Bank alone without SLM). Since SLM and Feature Bank are presented as the paper's two key innovations (Section 3.2), the ablation does not experimentally disentangle their respective contributions. The paper claims the Feature Bank "alleviates the myopic problem" but provides no experiment that measures the effect of the Feature Bank in isolation.

- **The method description is underspecified in several critical aspects.** (i) The Feature Bank selection procedure: Eq. 3 defines ℱ_bank as "an empirically derived index set of distinct feature maps" (line 112), but no procedure is given for deriving this index set. For classification, "fc features" is mentioned (line 104) but not operationalized. (ii) The mechanism for incorporating Feature Bank features into the auxiliary network is described only as "using them in local-modules just as they are used in the backbone network" (line 105) — this is too vague to implement. Are features concatenated, added, or used as attention? (iii) For detection, how a "local FPN" is constructed from the feature bank in a gradient-isolated local module is described narratively rather than algorithmically (Section 4.2). These gaps collectively mean the method cannot be faithfully re-implemented from the text alone.

### Trivial

- The "Inference Speed" column in Table 1 has no units or description, making the numbers uninterpretable (lines 178–188).
- Figure 3 (SR architecture) is referenced but the specific SR backbone model is never named in text or tables.
- Line 104 contains a typo: "lcoal-learning."

## Nice-to-Haves

- Adding at least one additional local learning baseline on VOC detection and any baseline on super-resolution would substantially strengthen the "first successful" claim. Even showing that a simple adaptation of DGL or AugLocal fails on these tasks (as asserted in Section 5.3) would turn a current weakness into evidence.
- An ablation that separates SLM from Feature Bank (e.g., MAN w/o Feature Bank, MAN w/o SLM, MAN with random features in bank) would directly validate the paper's central architectural thesis.
- Reporting results with standard deviations over 3+ seeds would help distinguish signal from noise in the small-difference comparisons.
- Adding a dedicated "Implementation Details" subsection with hyperparameters, architectures, and training procedures would address the reproducibility gap.

## Removed Points

- **Criticism that the paper "only compares DGL on one backbone**:" This is factually accurate but overstated in severity — the DGL comparison on RetinaNet-R34/COCO *is* the key controlled experiment, and the paper does compare against BP across many backbones. The limitation is noted in the main body under-evidenced claim above.
- **"Related Work reads as a list of references"**: Subjective opinion about presentation style, not a verifiable weakness.
- **"No standard deviations — every result is from a single run"**: Kept as part of the major weakness on missing training details above.
- **Strength Finder's generic framing about "important problem"**: The strengths kept above are all specific and evidence-backed; removed generic phrasings.

## Novel Insights

The harsh critic notes that MAN's detection results on COCO dramatically outperform DGL (28.9 vs. 21.3 mAP) despite giving DGL architectural enhancements, and the strength finder identifies that this controlled experiment is the paper's strongest evidence. Neither reviewer surfaces a novel insight beyond what the paper itself presents.

## Suggestions

1. **Reconcile the SR claims with the evidence.** Either add more SR baselines (including other local learning methods) to contextualize the gap, or temper the "comparable/on par" language throughout the paper to accurately reflect that detection results are comparable while SR shows a meaningful gap that merits further investigation.

2. **Add a complete "Implementation Details" section** covering: exact backbone architectures (ResNet depth per dataset, SR backbone identity), training hyperparameters (epochs, batch size, learning rate values, optimizer, schedule, weight decay), data augmentation pipeline, and number of runs / variance reporting.

3. **Redesign the ablation study** to separate SLM from Feature Bank: compare (a) baseline local learning (DGL or similar), (b) SLM only (no Feature Bank), (c) Feature Bank only (no SLM, using a fixed auxiliary network), (d) full MAN. This would directly validate which component drives the improvement.

4. **For VOC and SR**, add at least one local learning baseline. Even adapting DGL or AugLocal with minimal changes would demonstrate whether the "first successful" claim is warranted.

5. **Specify the feature incorporation mechanism precisely** — are Feature Bank features concatenated, added, gated, or used as attention in the auxiliary network's forward pass?

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>