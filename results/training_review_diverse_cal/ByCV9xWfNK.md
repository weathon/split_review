Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces Intermediate Layer Classifiers (ILCs), a framework where linear probes are trained on intermediate-layer representations of frozen pretrained models, rather than the penultimate layer, for out-of-distribution (OOD) generalization. Across experiments on 9 datasets covering subpopulation shifts, input perturbations, and style shifts, the authors find that the best intermediate layer frequently outperforms the penultimate layer in both few-shot and zero-shot settings. A sensitivity analysis is offered as a mechanistic explanation.

## Strengths

- **Consistent advantage across diverse settings**: The paper demonstrates across 9 datasets, multiple architectures (ResNet, ViT), and three types of distribution shifts that intermediate-layer representations can substantially outperform penultimate-layer representations. Gains are often large — +16.8% (CMNIST, ResNet), +6.3% (CIFAR-10, ResNet), +26% WGA on CelebA — making this a robust empirical finding rather than an artifact of a single benchmark.

- **Per-layer results (Figure 8) provide clean, selection-free evidence**: Section 5.1 reports per-layer accuracies without the layer-selection confound. In the zero-shot setting (ID-trained probes), the pen-penultimate layer (layer 7) achieves 86.7% WGA vs. 79.4% for the penultimate layer on Waterbirds, and similar patterns hold across CelebA and MultiCelebA. This directly supports the claim that intermediate-layer representations themselves are more useful for OOD generalization, independent of the selection mechanism.

- **Sensitivity metric offers an interpretable explanation**: The paper introduces a tractable metric (Section 5.2) showing that intermediate layers exhibit lower representation drift between ID and OOD data compared to the penultimate layer, especially for minority groups. This provides a principled, testable hypothesis for why intermediate layers generalize better.

- **Zero-shot results are practically relevant**: Showing that ID-trained probes on intermediate layers can approach or exceed the performance of OOD-retrained last-layer probes (e.g., 87.1% vs. 79.4% on Waterbirds) broadens the practical applicability when target-domain data is unavailable.

## Weaknesses

### Major

- **Main "Best layer vs. Last layer" comparisons conflate layer quality with selection advantage.** In Figures 3–7, the ILC framework selects the best from multiple layer candidates using OOD validation data (Section 3.2, Layer Selection), while the last-layer baseline is a single probe on the penultimate layer with no equivalent selection mechanism. The reported gains therefore reflect a combination of (a) whether intermediate-layer features are genuinely better, and (b) the benefit of having a pool of candidates with a hold-out set to choose from. This is a real methodological confound. The per-layer results in Figure 8 partially address this (and are the cleanest evidence in the paper), but they are presented as secondary analysis rather than foregrounded. In the few-shot oracle setting (Figure 8), the gap between layer 7 and layer 8 on Waterbirds is only 0.1% (94.0% vs. 93.9%), which is much smaller than the gaps reported in the main few-shot figures — suggesting that the selection advantage accounts for a nontrivial portion of the gains claimed in Section 4.2.

- **No error bars, confidence intervals, or significance tests are reported anywhere in the paper.** Some gains are small (e.g., +1.1% for CMNIST with ViT, –0.2% for CIFAR-100C with ViT in Figure 3), and without any measure of variability it is impossible to assess whether these reflect genuine improvements or noise. The "best layer" is a maximum over multiple candidates, which is susceptible to optimism bias even with honest hold-out selection. This is the single most important missing element for trusting the quantitative claims.

### Minor

- **The "zero-shot" label, while carefully defined, risks misinterpretation.** The paper defines zero-shot as using ID data for probe training (Section 4.3) but still uses OOD validation data for layer selection (Section 3.1: "The validation is performed over OOD: D_valid ~ P_OOD"). This is transparently documented and follows standard practice (Gulrajani & Lopez-Paz, 2020), but readers may assume "zero-shot" means no OOD data is used at all. The practical relevance would be strengthened by an experiment without any OOD data for selection (e.g., a fixed heuristic like "always use layer L-2").

- **Sensitivity analysis is limited to subpopulation shifts.** The sensitivity metric (Section 5.2) is only computed for CelebA and MultiCelebA where group labels are available. The paper then uses this analysis to explain OOD improvements on other shift types (CIFAR-10C, ImageNet variants) without empirical verification. While the explanation is plausible, it would benefit from extending the analysis to corruption/style shifts (e.g., measuring representation drift via CKA between clean and corrupted images at each layer).

- **The claim that ILCs "provide a stronger baseline for zero-shot and few-shot learning" (Conclusion) slightly overstates the contribution.** ILCs are not a new learning algorithm but a framework for probing and selecting a layer. The value lies in the empirical findings, not the method itself. This is a framing issue, not a substantive flaw.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- An experiment that ablates the size of the OOD validation set used for layer selection, showing how many OOD samples are needed for reliable selection.
- A zero-shot variant with a fixed-layer heuristic (always use layer L-2) to quantify how much of the reported gain depends on OOD data for selection.
- Extending the sensitivity analysis to corruption shifts by measuring pairwise-distance drift between clean and corrupted ImageNet/CIFAR images at each layer.
- Reporting per-layer accuracies (as in Figure 8) more prominently alongside the Best-vs-Last comparisons.

## Removed Points

- **Criticism that the comparison is "fundamentally unfair" and that the "central claim cannot be disentangled":** Overstated. Figure 8 provides per-layer (selection-free) evidence in both few-shot and zero-shot settings, directly supporting the core claim. The selection confound is real but partial — the paper does contain cleaner evidence, just not as the main presentation. Moved here because the fatal framing is not justified.
- **Criticism about missing hyperparameters (learning rate, epochs, optimizer):** These details are standardly placed in the appendix, which is stripped by the parser. Not a valid criticism given the parsing pipeline.
- **Criticism about the sensitivity metric being "low because the layer is uninformative":** The paper's data contradicts this — the same intermediate layers showing low sensitivity also achieve high probe accuracy, so the metric is capturing robustness, not uninformative collapse. The combination of high accuracy + low sensitivity is precisely what makes the analysis meaningful.
- **"The paper does not discuss the effect of representation dimensionality on linear probing":** A valid point but minor. The paper is already broad (9 datasets, multiple architectures); adding a dimensionality analysis would be a nice-to-have, not a structural weakness.

## Novel Insights

Beyond the paper's own contributions, the most noteworthy observation emerging from the reviews is the asymmetry between the zero-shot and few-shot settings. The clean per-layer evidence (Figure 8, zero-shot panel) shows a large, selection-free gap (e.g., 7.3% on Waterbirds: layer 7 at 86.7% vs. layer 8 at 79.4%), while the clean few-shot oracle evidence shows a much smaller gap (0.1% on Waterbirds). This suggests the paper's strongest and most robust finding is in the zero-shot regime — where intermediate layers genuinely provide superior OOD features without any OOD training data — while the few-shot advantage may be substantially driven by the selection mechanism. This distinction is not clearly drawn in the paper itself.

## Suggestions

1. **Foreground Figure 8 (per-layer results) as the primary evidence** for the core claim, and reframe the "Best layer vs. Last layer" comparisons as method-vs-method rather than layer-vs-layer.
2. **Add error bars** to all main figures (e.g., standard deviations over multiple data splits or random seeds). This is essential for the smaller gains.
3. **Add a zero-shot experiment without OOD validation data** — e.g., always use layer L-2 or select based on an ID-only criterion — to clarify how much of the zero-shot gain depends on OOD samples for selection.
4. **Extend the sensitivity analysis** to corruption shifts by measuring representation drift (CKA or pairwise distance) between clean and corrupted versions of the same images.

## Score and Decision

The paper identifies an important and underappreciated phenomenon and provides substantial empirical evidence across many settings. The per-layer results (Figure 8) offer clean, selection-free support for the core claim, particularly in the zero-shot regime. However, the main presentation relies on confounded "Best vs. Last" comparisons that conflate layer quality with selection advantage, and the complete absence of error bars weakens confidence in the quantitative claims. These issues are addressable but limit the paper's current strength.

**Score:** 6.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>