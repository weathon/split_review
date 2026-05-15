Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper challenges the widespread use of artificial memorization (noisy labels/inputs) as a proxy for studying memorization in deep learning. Using the Feldman & Zhang (2020) leave-one-out methodology across VGG, ResNet, and ViT families on CIFAR-10, CIFAR-100, and Tiny ImageNet, the authors measure *natural* memorization and find that (1) over-parameterization *reduces* memorization (contra the claim from artificial-memorization studies), (2) training iterations produce a non-monotonic effect (increase then decrease), and (3) the discovery of "transient memorization"—points memorized under some conditions but generalized under others. The paper also reports a very strong Pearson correlation (0.99) between memorization and the train-test gap, concluding that memorization is not necessary for generalization.

## Strengths

- **Systematic natural memorization measurements across architectures and datasets.** The paper applies the computationally intensive Feldman & Zhang leave-one-out approximation across VGG (4 sizes), ResNet (2 sizes), and ViT (2 sizes) on three datasets, providing one of the largest empirical maps of natural memorization trends. Tables 1–2 and Figure 1 document the core finding: within each family, increasing parameter count *decreases* memorialization (e.g., SmallVGG → VGG19, ResNet18 → ResNet50), directly challenging the artificial-memorization narrative.

- **Discovery of transient memorization.** The paper identifies and characterizes two forms of this phenomenon—model-wise (points memorized by SmallVGG but generalized by ResNet50) and temporal-wise (points memorized at Epoch 77 but generalized by Epoch 99). The quantitative analysis showing average memorization scores of 44.99% (model-wise) and 35.71% (temporal-wise) versus a dataset average of 11.17% is concrete evidence that these are mid-frequency sub-population points, not outliers. This is a genuinely novel observation.

- **Non-monotonic effect of training iterations on natural memorization.** Figure 2 documents a three-stage pattern (no memorization → increase to a peak → decrease) across LargeVGG and ViT models within standard 100-epoch training, demonstrating that memorization can *decline* with prolonged training—a finding that would be invisible under the artificial-memorization paradigm where models are overtrained for thousands of epochs.

- **Strong empirical correlation between memorization and train-test gap.** The reported Pearson correlation of 0.99 across the full model zoo on three datasets (Figure 3) is a striking relationship that deserves attention, regardless of how one interprets its causal direction.

## Weaknesses

### Fatal
None.

### Major

- **The claim that "memorization is not necessary for generalization" is not supported by the evidence presented.** The paper asserts this causal conclusion (Section 5, echoed in the abstract) based on (a) the 0.99 Pearson correlation between memorization count and train-test gap, and (b) the observation that some points transition from memorized to generalized (transient memorization). Both are correlational/observational: (a) a strong correlation does not establish that memorization is causally unnecessary—it could still be that for a fixed architecture, some points must be memorized to achieve peak accuracy; (b) transient memorization shows that *some* points can be unlearned, not that *all* memorized points can be, nor that memorization is globally unnecessary. The paper directly contradicts Feldman & Zhang's empirical findings that memorization of long-tail points is necessary for high test accuracy without providing the kind of causal intervention (e.g., influence-based reweighting, explicit regularization against memorization) that would settle this. This overclaim is the paper's most significant weakness because it reaches beyond what the evidence supports. The transient-memorization discovery and the measurement trends are valuable with or without this claim.

- **The "opposite effect" framing lacks a controlled, head-to-head comparison with artificial memorization under the same conditions.** The paper claims that over-parameterization and increased training time have the "opposite effect" on natural memorization compared to what artificial memorization studies found. However, the paper does not replicate any artificial memorization experiment on the same architectures, datasets, and evaluation metric. The artificial memorization literature (Krueger et al., Collins et al., Stephenson et al., Morcos et al.) defines memorization differently—typically as the ability to correctly classify a noisy label or noisy input after extended training—which measures *capacity to fit random patterns*, not the same quantity as the leave-one-out influence score. While the paper argues (Section 3.1 and Section 5) that both definitions are compatible ("artificial points have high scores as well"), this assertion is not empirically verified. Without a controlled comparison showing that the two measures diverge on the same models, the "opposite effect" framing is an apples-to-oranges comparison. The paper's within-family memorization trends (e.g., larger models memorize less) are a solid standalone contribution; the rhetorical framing around "reversing" artificial-memorization findings overreaches without the controlled experiment.

### Minor

- **The Pearson correlation of 0.99 is reported without any measure of uncertainty (confidence intervals, standard error, or a detailed breakdown per data point).** With roughly 7–8 model-architecture combinations per dataset (and only 3 for Tiny ImageNet), a correlation this extreme is fragile—a single outlier could drive it. The paper should report confidence intervals or at least show the individual data points transparently.

- **No sensitivity analysis for the 25% memorization-score threshold.** The paper adopts this threshold from Feldman & Zhang without testing whether the observed trends (decreasing memorization with over-parameterization, three-stage training dynamics) are robust to alternative thresholds (e.g., 10%, 50%, or treating memorization score as a continuous variable). This would strengthen confidence that the findings are not artifacts of a particular cutoff.

- **The transient memorization analysis is limited to two comparisons (SmallVGG vs. ResNet50; Epoch 77 vs. Epoch 99).** While these are reasonable starting points, the paper does not systematically characterize why certain points become transient or whether the phenomenon generalizes across more architecture pairs and epoch ranges. The connection to "small sub-populations" is supported by memorization-score averages but lacks finer-grained analysis (e.g., examining which classes or visual features these transient points share).

- **The cross-family comparison (VGG19 vs. ResNet18) in Section 4.4 conflates architectural improvements with parameter count.** While the paper's main over-parameterization claims use within-family comparisons where only parameter count varies, the discussion in Section 4.4 compares VGG19 (143.7M params) with ResNet18 (11.2M params) and attributes the difference to "architectural improvements." This is fine as a separate observation but could confuse readers about what the over-parameterization claim is based on.

### Trivial

- The comparison to epoch-wise double descent (Section 4.2) is speculative and adds little; the paper could simply state its observed three-stage pattern without invoking this connection.
- Figure captions lack sufficient detail to be interpretable without the main text.

## Nice-to-Haves

- A direct controlled experiment: train models on the same architectures with noisy labels/inputs, measure memorization using *both* the leave-one-out score and the standard artificial-memorization metric, and show that over-parameterization and training time affect the two measures differently. This would transform the "opposite effect" claim from a rhetorical comparison into a rigorous one.
- Sensitivity analysis showing that the main trends (over-parameterization reduces memorization; three-stage training dynamics) hold across multiple memorization-score thresholds.
- Examples of actual images from CIFAR-10 that exhibit transient memorization, to make the phenomenon concrete and reveal qualitative patterns.
- Causal evidence for the "memorization not necessary" claim, such as training models explicitly regularized to minimize the memorization score and checking whether test accuracy suffers.

## Removed Points

*"The paper does not cite specific studies that make these claims [about over-parameterization and training time increasing memorization]."* — **Factually incorrect.** The paper cites Krueger et al. 2017, Collins et al. 2018, Stephenson et al. 2021, and Morcos et al. 2018 in Section 1 as examples of artificial memorization studies, and the claims about their findings are standard in that literature. The paper could be more precise about which finding comes from which specific study, but the criticism as stated is inaccurate and is removed.

*"The paper does not reproduce those experiments."* — Already addressed as a major weakness (lack of controlled comparison), but the phrasing that the reader "cannot verify that the supposed findings are correctly characterized" overstates the issue. The cited studies are publicly available; readers can verify the claims. Moved to the major weakness above with appropriate nuance.

*"Section 4.1: The paper then compares across families (VGG19 vs. ResNet18) and attributes the difference to 'architectural improvements.' This conflates architecture changes with parameter count changes and muddles the over-parameterization claim."* — The paper's over-parameterization claim rests on within-family comparisons (SmallVGG→VGG19, ResNet18→ResNet50), not cross-family. The VGG19-vs-ResNet18 comparison in Section 4.4 is a separate discussion about architectural effects, clearly labeled as such. This criticism misattributes the paper's argument. Kept as a minor weakness about potential confusion but significantly softened.

*"Scatter plot for the correlation in Figure 3"* — The paper already has Figure 3, which (based on its caption) shows the relationship. The issue is not the absence of a plot but the absence of confidence intervals. Moved to the minor weakness about uncertainty.

## Novel Insights

The critical reviews, taken together, reveal that the paper's strongest empirical contribution—the systematic documentation of natural memorization trends across architectures, including the discovery of transient memorization—is somewhat obscured by its framing. The reviewers converge on the view that the transient-memorization phenomenon and the within-family measurements are novel and solid, while the interpretive claims ("opposite effects," "memorization not necessary") are where the paper overreaches. An interesting pattern across the reviews is that the claimed contradiction with Feldman & Zhang (2020) about the necessity of memorization for generalization may be less of a direct contradiction than the paper presents: Feldman & Zhang showed memorization is *necessary* under specific data-limit regimes (long-tail distributions with scarce sub-populations), whereas this paper operates in a different regime where model capacity is varied and can overcome those scarcities. The two findings may be compatible if memorization is necessary when model capacity is insufficient to learn rare features, but unnecessary when capacity is ample—which is exactly the "fallback mechanism" narrative the paper gestures toward but does not fully develop. This reconciliation point is worth exploring explicitly.

## Suggestions

1. **Temper the causal claim about memorization not being necessary for generalization.** Replace it with the more defensible statement that "memorization is not *inherently* necessary—larger models with better feature learning can reduce or eliminate memorization while improving test accuracy." Alternatively, present it as a hypothesis with the transient-memorization data as suggestive evidence, not a conclusion.

2. **Add confidence intervals or bootstrap estimates for the Pearson correlation of 0.99**, and show the scatter plot with axis labels so readers can assess the influence of individual data points. A correlation over ~8 data points needs uncertainty quantification.

3. **Run at least one sensitivity analysis on the 25% memorization-score threshold** (e.g., 10% and 50%) to confirm that the main trends (over-parameterization reduces memorization, three-stage training dynamics) are robust.

4. **Either add a controlled artificial-memorization experiment** (same architectures, datasets, with the leave-one-out metric applied to models trained on noisy labels/inputs) **or re-frame the paper** to focus on "characterizing natural memorization" rather than "showing artificial memorization findings are reversed." The empirical contributions stand on their own without the adversarial framing, and the latter framing would eliminate the weakest part of the paper.

5. **Expand the transient memorization analysis** to include more architecture pairs and provide visual examples of transient points, along with class-level analysis of which sub-populations are affected.

## Score and Decision

The paper makes genuine empirical contributions: the first large-scale measurement of natural memorization across architecture families, the discovery of transient memorization, and the documentation of non-monotonic training effects. These are valuable and nontrivial (requiring training 2,000 models per architecture). However, the paper's most prominent interpretive claims—specifically that memorization is "not necessary for generalization" and that artificial memorization findings are "reversed"—outrun the evidence. The former is a causal claim supported only by correlation; the latter lacks a controlled comparison. These overclaims substantially weaken the paper's persuasiveness and need to be addressed before the paper meets its own stated ambitions. The core empirical findings are solid and would make a meaningful contribution once framed more carefully.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>