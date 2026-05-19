Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes using a virtual sound synthesizer with randomly perturbed parameters to generate positive pairs (called "audio doppelgängers") for contrastive representation learning — without any real audio during pretraining. A single hyperparameter δ controls pair hardness, and the method is lightweight (1-2 hours training, no data storage). Experiments across 8 downstream tasks show that models trained entirely on synthetic data outperform an equivalent ResNet18 trained on real VGGSound audio with standard augmentations, and beat temporal jitter in 6/8 tasks.

## Strengths

- **Novel and well-motivated approach to generating contrastive pairs.** Using the parameter space of a sound synthesizer to create positive pairs is a genuinely creative idea. The method is principled: the synthesizer parameters causally determine acoustic properties (pitch, timbre, envelope), and perturbing them produces variation that is qualitatively different from post-hoc signal augmentations. The paper correctly related this to vision work on procedural/fractal data generation (Baradad et al., Kataoka et al.).

- **δ provides simple, interpretable control over pair hardness.** The perturbation factor δ monotonically controls the cosine similarity of positive pairs (Fig. 3A) and their separation from negatives (Fig. 3B). This is cleaner than hand-designed augmentation schedules and the paper systematically evaluates δ across all 8 tasks (Fig. 5), finding δ=0.25 to be broadly optimal.

- **Synthetic data outperforms the real-data internal baseline.** The best synthetic model achieves 58.90% vs 48.85% on ESC-50, 66.71% vs 63.82% on UrbanSound8K, and beats VGGSound SSL on 7/8 tasks (Table 1). These results — all using the same ResNet18 architecture — demonstrate that purely synthetic pretraining can produce genuinely useful representations. The paper also shows that augmentations do not improve over δ alone (58.75 vs 58.90 on ESC-50), suggesting the perturbation subsumes hand-crafted augmentation.

- **Thorough distributional analysis.** The FAD analysis (Table 2), spectral feature comparisons (Fig. 4A), and causal uncertainty analysis (Fig. 4B) go beyond simple benchmark reporting to characterize *why* synthetic data might work. The mixture experiments (VGGSound-Mix) attempting to match synthetic spectral properties are a thoughtful diagnostic.

- **Practical advantages.** The method requires no data storage, trains in 1-2 hours (vs 6-8+ hours for real datasets with augmentations), and has a single hyperparameter. These are concrete operational benefits for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **The synthetic data has an uncontrolled diversity advantage over the real-data baseline, making the comparison less fair than claimed.** The synthetic model generates 100,000 *new* unique sounds each epoch — 20M unique source sounds over 200 epochs (Section 3.4). The real-data baseline uses a fixed set of 100,000 VGGSound source files, repeatedly sampled with random 1-second crops (Section 3.2). While crops differ across epochs, the synthetic model sees orders of magnitude more unique source material. This confound means the central claim ("competitive with real data") rests on a comparison where synthetic data benefits from vastly higher acoustic diversity. A controlled experiment (e.g., pre-generating a fixed synthetic dataset of the same size as the real set, or using the full VGGSound dataset) would be needed to determine whether the advantage comes from the causal perturbation mechanism or simply from more diverse training data. The paper does not address this in its limitations section.

- **The framing overstates results relative to existing SSL methods.** The abstract and introduction claim "strong performance" and "competitive with real data," but the best synthetic results are 20–40 points below existing SSL models on the same benchmarks (e.g., 58.90% on ESC-50 vs HEAR/ARCH SSL at 80.50% and MS-CLAP at 89.95%; 44.40% on NSynth Pitch vs 87.80%). The paper's internal comparison to a VGGSound ResNet18 SSL baseline is valid, but the broader language in the abstract and introduction suggests a level of competitiveness with the field that the numbers do not support. The paper should clearly scope its claim: synthetic data produces useful representations that beat a reasonable real-data SSL baseline of the same architecture, but is far from SOTA. The honest limitations section partially mitigates this, but the abstract and introduction still over-sell.

- **The "Best Synthetic" row in Table 1 aggregates across different δ values and synthesizers per task, not a single model.** The paper also reports *Voice* (δ=0.25) as a single strong model, so the aggregation is transparent, but the presentation inflates the apparent performance. For example, on NSynth Pitch, "Best Synthetic" is 44.40% while *Voice* (δ=0.25) achieves only 32.20% — the best comes from *Voice* (δ=0.25, Aug.) and *Voice* (δ unspecified for NSynth specifically). The paper should more prominently state which single model it recommends and report that model's full-row results.

### Minor

- **The FAD analysis produces an internal contradiction that the paper does not resolve.** On ESC-50, VGGSound has a much lower FAD (6.71) than *Voice* (17.39), yet the *Voice*-trained model outperforms the VGGSound-trained model (58.90 vs 48.85). If FAD measures distributional similarity relevant to task performance, this result is anomalous. The paper acknowledges FAD limitations (line 186) but does not explain why the metric fails in this specific case. This weakens the argument that synthetic data works because it better matches downstream distributions.

- **The "causal manipulation" framing is aspirational relative to the implemented method.** The introduction and related work emphasize intervening on the "data-generating process" and "causal mechanisms" (lines 19–21), but the actual perturbation is isotropic Gaussian noise applied uniformly to all 78 synthesizer parameters with no semantic structure. As the limitations section honestly acknowledges, this does not account for parameter correlations or semantics (e.g., octave relationships in pitch). The gap between the causal framing and the actual random perturbation should be narrowed in the introduction, or the method should be described as operating in "parameter space" rather than making a strong causal claim.

- **The paper does not specify which training checkpoint is used as the fixed feature extractor.** The evaluation uses linear probing on a fixed feature extractor (Section 3.5), but it is unclear whether the extractor comes from the last epoch, a moving average, or a checkpoint selected by validation performance. This affects reproducibility.

### Trivial

- **"First study ... of synthetic data methods for audio representation learning" should be qualified as "first study using randomly parameterized synthesis for general-purpose non-speech audio representation learning"** to avoid overclaiming given prior work on NSynth and speech synthesis for pretraining — though the paper's related work does make this distinction clear.

- **Table 1 caption lists tasks in abbreviated form without expanding them in the caption, requiring the reader to search the text for the full names.**

## Nice-to-Haves

- **Controlling for data diversity:** Running an experiment where a fixed synthetic dataset of 100k sounds is pre-generated and reused across 200 epochs (matching the real-data setup) would cleanly isolate whether the advantage is from the perturbation mechanism or from diversity alone. This is the single most informative additional experiment.
- **Hybrid training:** Fine-tuning synthetic-pretrained models on small amounts of real data would directly test the paper's stated goal of "reducing the data burden."
- **Analysis of training dynamics:** Do synthetic models converge faster or overfit differently? This would inform the "data burden" claim.

## Removed Points

- **"The real-data baseline is too weak because a supervised ResNet18 gets 87.45% on ESC-50."** Self-supervised learning (no label access) and supervised learning are fundamentally different regimes. Comparing SSL accuracy to supervised accuracy is not apples-to-apples and does not indicate the baseline is "weak."
- **"No analysis of training dynamics / No measurement beyond linear probing / No investigation of synthesizer parameter count vs diversity."** These are nice-to-have extensions, not weaknesses. The paper already provides a substantial experimental investigation.
- **Missing related works / reproducibility nitpicks about hyperparameters.** These either could not be verified or reflect standard community practice rather than omissions.
- **Criticisms about missing appendix content or missing proofs.** The parser strips appendices from all papers; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a key confound (data diversity mismatch) that the paper overlooks, but this is a methodological critique rather than a novel insight about the method itself.

## Suggestions

1. **Fix the diversity confound before claiming "competitive with real data."** Either (a) pre-generate a fixed synthetic dataset of 100k sounds and train for 200 epochs on it (matching the real-data setup), or (b) use the full VGGSound dataset (~160k files). If synthetic still wins, the claim becomes credible. If not, the paper becomes a transparent negative result about the importance of diversity — still valuable.
2. **Recalibrate the framing in the abstract and introduction.** Replace "strong performance" and "competitive with real data" with precise language: "outperforms an equivalent self-supervised model trained on a standard real dataset (VGGSound) using the same architecture, while using no real audio during pretraining." Acknowledge the gap to SOTA SSL methods explicitly and early.
3. **Report a single recommended model configuration** (e.g., *Voice*, δ=0.25) with its complete row of results rather than aggregating best-per-task. Move the aggregate to a supplementary table.
4. **Explain the ESC-50 FAD discrepancy** or remove the causal claim about FAD predicting task performance. Currently, the FAD analysis is used to argue that synthetic data better matches downstream distributions, but the ESC-50 result contradicts this.
5. **Tone down the "causal manipulation" language** in the introduction since the actual perturbation is isotropic random noise. Describe the method as operating in "parameter space" of a synthesizer, which is already sufficiently distinctive.
6. **Specify checkpoint selection** for the fixed feature extractor (last epoch? best validation? moving average?).

## Score and Decision

The paper introduces a genuinely novel approach — using synthesizer parameter perturbations for contrastive learning — with thorough experiments (8 tasks, 3 synthesizers, systematic δ analysis) and thoughtful distributional characterization. The core finding (synthetic-only pretraining produces useful representations) is real and interesting. However, the paper oversells its results (the comparison against real data is confounded by a diversity mismatch, and the absolute performance is far from SOTA despite claims of being "competitive"), and the framing creates expectations the evidence does not meet. These weaknesses are addressable but require non-trivial changes to the experimental design and a major reframing of the claims. In its current form, the paper's contribution is promising but not yet established convincingly.

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**