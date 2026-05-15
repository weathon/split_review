Now I have verified the paper content against all reviewer claims. Let me construct the final review.

## Summary

This paper introduces Influencer Backdoor Attack (IBA), a segmentation-specific backdoor attack where a trigger placed on *non-victim* pixels indirectly forces misclassification of all victim pixels. Two enhancement techniques are proposed: Nearest-Neighbor Injection (NNI), which places the trigger adjacent to the victim object, and Pixel Random Labeling (PRL), which randomly reassigns some non-victim pixel labels during poisoning to encourage the model to rely on broader context. Experiments on PSPNet, DeepLabV3, and SegFormer across Cityscapes and PASCAL VOC show that both techniques outperform a random-trigger-placement baseline, with PRL maintaining high ASR even when the trigger is far from the victim — the attack success rate holds above 90% at trigger-victim distances of 120–150 pixels.

## Strengths

- **Novel attack paradigm for segmentation (trigger on non-victim pixels, indirect influence).** The paper clearly distinguishes IBA from prior segmentation backdoor attacks: OFBA (Mao et al.) places the trigger on the victim class itself, while IBA allows trigger placement on any non-victim object. This is a practically relevant scenario — e.g., a roadside sticker affecting car segmentation — that prior work does not address. (Sec. 1, Sec. 2)

- **PRL maintains high ASR across all trigger-victim distances, validated by a controlled distance experiment.** Table 1 shows PRL achieving 90.75–96.32% ASR at distances up to 120–150 pixels with 5–15% poisoning, while the baseline IBA drops to 54–73% and NNI drops even lower at far distances. This directly supports the paper's core claim about enabling effective attacks under arbitrary trigger placement. (Table 1 / exp:dis)

- **Real-world physical attack demonstration.** The authors printed the trigger on a large sheet (840mm²) and tested it in outdoor scenes with 265 frames, achieving 60–64% ASR across baseline, NNI, and PRL. While limited in reported detail, the existence of a real-world experiment is a step beyond purely digital evaluation. (Sec. 5.4)

- **Systematic ablation study validating PRL label-choice design.** Figure 3 compares four label-replacement strategies (null, single class, all dataset classes, same-image classes) and shows that only the proposed same-image design provides continuous ASR improvement without degrading benign accuracy. This ablation is well-designed and informative. (Sec. 5.2)

- **Standard deviations reported for distance experiments, and experiments span multiple models and datasets.** Results are reported on three architectures (PSPNet, DeepLabV3, SegFormer) and two datasets, improving reliability. (Sec. 4, Sec. 5)

## Weaknesses

### Fatal
None.

### Major

- **PRL's claimed mechanism ("forces global context learning") is asserted without direct evidence.** The paper repeatedly states that PRL makes the model "learn the image's global information" or "aggregate better context," but the only supporting evidence is the distance experiment (Table 1), which is consistent with this explanation but does not prove it. The ablation study (Fig. 3) rules out alternative label choices but does not isolate "global context learning" from other possible effects (e.g., PRL acting as a regularizer that prevents overfitting to the trigger location, or creating a stronger gradient signal). Without receptive-field analysis, feature-attribution maps, or a targeted control experiment, this mechanistic claim remains speculation. This weakens the paper's central technical narrative for PRL. (Sec. 3.2, Sec. 5.2)

- **Real-world experiment lacks sufficient detail and shows a large ASR gap from digital results.** The real-world experiment is described in a single paragraph (Sec. 5.4): 265 frames, trigger size 840mm², "various outdoor settings." No information is given about camera parameters, lighting conditions, trigger placement variance across frames, number of unique scenes, or per-image ASR distribution. The ASR drops from >95% (digital) to ~60% (physical), and the paper does not analyze why or discuss whether this level is practically concerning. The reference to an appendix (\ref{app:realworldexp}) that was stripped from the PDF suggests additional details existed, but the main text alone is insufficient to evaluate the experiment's rigor. (Sec. 5.4)

### Minor

- **No experimental comparison against prior segmentation-specific backdoor attacks.** The paper cites two prior segmentation attacks (Li et al. 2021; Mao et al. 2023) in Related Work and argues they use fundamentally different trigger paradigms. However, the paper simultaneously claims that backdoor attacks on segmentation have been "largely overlooked" and presents IBA/NNI/PRL as improvements. Some quantitative comparison — even if focused on the different trigger-placement constraints — would help the reader calibrate the contribution relative to existing work. The current evaluation only compares against a self-defined random-trigger baseline. (Sec. 2)

- **Defense evaluation is limited to two simple defenses, but the claims are appropriately scoped.** The paper tests only fine-tuning (1–10% clean data) and channel pruning, explicitly acknowledging that exhaustive adaptation is out of scope. The claims are limited to outperforming the baseline under these specific defenses. This is acceptable for a single paper, but the resistance to stronger defenses (Neural Cleanse, STRIP, spectral signatures) remains unknown, and the title "robustness" is somewhat generous given the limited defensive arsenal tested. (Sec. 5.2, Table 5)

- **NNI's distance bounds (L, U) are set empirically without sensitivity analysis.** The upper bound U is set to 30 (VOC) / 60 (Cityscapes) with L=0, but no analysis explores how the choice of bounds affects attack success. The algorithm (Alg. 1) also constrains the trigger to a single class region, but this constraint's effect is not ablated. (Sec. 3.1)

### Trivial
None.

## Nice-to-Haves

- **Comparison to prior segmentation backdoor attacks (Li et al., OFBA).** Though the attack paradigms differ, benchmarking ASR, benign accuracy degradation, and stealthiness under comparable poisoning budgets would strengthen the positioning of IBA.
- **Mechanism analysis for PRL using Grad-CAM, receptive-field statistics, or targeted controls** that isolate "global context aggregation" from alternative explanations (e.g., label noise regularization effects).
- **Real-world experiment with controlled variables** — number of scenes, per-image ASR distribution, lighting conditions, camera-to-trigger distances — to make the physical-world claim reproducible.
- **NNI distance-bound sensitivity analysis** to show how L and U affect the attack.

## Removed Points

These points were flagged by reviewers but removed for the reasons indicated:

- **"Backdoor attacks on segmentation 'largely overlooked' contradicts Related Work which cites two prior segmentation attacks."** — REMOVED. "Largely overlooked" does not mean "never studied." Hundreds of classification backdoor papers exist vs. two segmentation-specific works, so the claim is accurate. No contradiction.
- **"NNI is trivial and lacks novelty."** — REMOVED. The paper explicitly describes NNI as "simple, yet effective." Simplicity is not a flaw; the method is clearly described and includes non-trivial algorithmic choices (distance bounds, eligibility computation). The paper's novelty primarily rests on the IBA formulation and PRL, not on NNI being complex.
- **"Defense evaluation is insufficient to claim robustness."** — WEAKENED to minor. The paper explicitly states "exhaustive adaptation... is out of the scope of our work" and limits its claims to outperforming the baseline under the tested defenses. This is appropriate scoping.
- **"Missing stronger non-adaptive baseline (fixed trigger position, trigger on victim pixels)."** — WEAKENED to nice-to-have. The random-trigger baseline is standard for the IBA setting; additional baselines would strengthen but are not required.

## Novel Insights

The most interesting finding from the review process is the asymmetric behavior of NNI vs. PRL under defense and distance conditions. NNI is more robust to fine-tuning (55% ASR after 10% clean data vs. 29% for PRL) but collapses at far trigger-victim distances (45% at 120–150px vs. 90% for PRL). This suggests a fundamental trade-off: NNI creates a strong, spatially local trigger association that is hard to unlearn but only works nearby, while PRL creates a more distributed association that covers long distances but is more easily forgotten during fine-tuning. The paper mentions this briefly in the combination analysis but does not explore the underlying reasons. This trade-off could inform future work on segmentation backdoor attacks that balance robustness and distance-invariance.

## Suggestions

1. **Provide direct evidence for the PRL mechanism** — e.g., compare receptive-field statistics or Grad-CAM attribution between models trained with and without PRL, or include a control experiment where random label noise (without the "same-image" constraint) is applied to rule out regularization effects.
2. **Expand the real-world experiment section** with clear per-image ASR distributions, descriptions of scene diversity, lighting conditions, and camera parameters. Even without the appendix, a properly self-contained description is needed.
3. **Add a brief quantitative comparison to OFBA (Mao et al.)** under a setting where the trigger is on the victim class (their setting) vs. on non-victim pixels (IBA setting), to demonstrate the different use cases concretely. This would help contextualize the contribution without requiring a full re-implementation.
4. **Ablate the distance bounds (L, U) in NNI** to show the sensitivity of ASR to these hyperparameters.

## Score and Decision

**Originality:** Medium-High. The IBA formulation (indirect influence via non-victim triggers) is novel for segmentation backdoor attacks. PRL is a creative technique. NNI is simple but effective.

**Importance of research question:** High. Backdoor attacks on segmentation are practically important (autonomous driving, surveillance) and understudied compared to classification.

**Claims well-supported:** Partially. The ASR and distance results are well-supported. The PRL mechanism claim is not directly supported. The real-world claim needs more evidence.

**Soundness of experiments:** Generally sound within stated scope. Distance experiment is well-designed. Ablation studies are informative. Missing comparison to prior attacks is the main gap.

**Clarity of writing:** Good. The paper is well-organized and the contributions are clearly stated.

**Value to research community:** Moderate. Opens a new attack vector (non-victim trigger on segmentation). The PRL technique could inspire further work on context-aware backdoor attacks.

The paper makes a solid contribution to an underexplored area. The weaknesses — unvalidated mechanism claim, thin real-world evidence, missing comparison to prior attacks — are real but do not invalidate the core findings. The distance experiment alone convincingly demonstrates PRL's effectiveness. The paper should be accepted with a recommendation to strengthen the mechanism analysis and real-world reporting.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>