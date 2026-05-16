Now I have all the evidence I need. Let me synthesize the final review.

## Summary

This paper challenges the prevailing view that penultimate-layer (last-layer) representations are sufficient for OOD generalization. Using linear probes on frozen pretrained models (ResNets and ViTs), the authors show that intermediate-layer representations consistently outperform the penultimate layer in both few-shot and zero-shot OOD settings across 9 datasets covering subpopulation shifts, input perturbations, and style shifts. The gains are substantial in several cases — e.g., zero-shot CelebA worst-group accuracy jumps from 56.0% to 82.0% — and the paper provides a sensitivity analysis suggesting intermediate layers are less affected by distribution shifts. The paper is an empirical/analysis contribution, not a new-method paper.

## Strengths

1. **Large and consistent outperformance of intermediate layers in zero-shot OOD generalization (novel finding).** Section 4.3 shows that ILCs trained on ID data alone substantially outperform last-layer retraining on OOD data. On CelebA, the best ILC achieves 82.0% WGA vs. 56.0% for last-layer retraining (Figure 5). On CIFAR-10C, all models gain 2–5 percentage points (Figure 6). This is a genuinely new result — prior last-layer retraining methods (Kirichenko et al., Izmailov et al.) require OOD data.

2. **Comprehensive evaluation across diverse shift types and architectures.** The study covers subpopulation shifts (Waterbirds, CelebA, MultiCelebA), input perturbations (CIFAR-10/100-C), and style shifts (ImageNet variants), using both CNNs (ResNets) and transformers (ViTs). This breadth strengthens the generality of the central claim.

3. **Quantitative evidence supporting the proposed mechanism (reduced sensitivity to distribution shifts).** Section 5.2 introduces a sensitivity metric and shows that intermediate layers, especially for minority groups, have lower sensitivity scores than the penultimate layer (Figure 9). PCA projections (Figure 10) provide complementary qualitative evidence. While the metric has limitations (noted below), this analysis goes beyond a purely observational finding and offers a mechanistic hypothesis.

4. **Data efficiency advantage with few OOD samples.** Figure 4 shows that ILCs improve more over last-layer retraining precisely when OOD data is scarce (e.g., +27 p.p. on MultiCelebA at π ≤ 0.03). This is practically relevant — the setting where the method helps most is also the setting where alternatives struggle most.

## Weaknesses

### Fatal

None.

### Major

1. **Data-splitting ambiguity in the few-shot "information content" experiment (Section 4.2.1) undermines confidence in Figure 3.** The paper states: "the entire validation set, as defined in §4.1, is used for D_probe ~ P_OOD." But Section 3.2 specifies that layer selection is performed on D_valid. If D_valid is entirely consumed as D_probe, no separate validation set remains for selecting the best layer. The paper does not clarify what data was used for layer selection in this specific setting. If training accuracy on D_probe was used, the "best layer" comparison reflects training fit, not generalization. If a different mechanism was used (e.g., a subset of the test set), this needs to be explicitly stated. Given that Figures 3 and 4 are the primary exhibits for the few-shot claim, this must be resolved before the results can be fully trusted. The zero-shot results (Section 4.3) do not share this ambiguity since they use ID data for D_probe and OOD data for D_valid — but the few-shot results are still central to the paper's overall narrative.

### Minor

1. **"Best layer" vs. "last layer" comparison gives ILCs a free model-selection advantage.** The main results (Figures 3, 4, 5, 6) compare the *best among multiple intermediate layers* (selected via validation) against the *single* penultimate layer. This asymmetry inflates the apparent benefit of ILCs. The paper partially addresses this by showing layer-wise results in Figure 8, and selection via a held-out set is standard practice. Nevertheless, the headline numbers would benefit from a sanity check — e.g., showing the *average* intermediate layer performance or noting when the penultimate layer is actually the best. A brief caveat in the figure captions would improve transparency.

2. **Absence of error bars or variance estimates throughout.** For an empirical study drawing comparative conclusions from numerical differences (e.g., "+6.3 p.p. on CIFAR-10"), the reader has no way to assess whether these gaps are stable or within noise. This is especially relevant for the data-efficiency curves (Figure 4), where small-π regimes likely have high variance and the paper does not specify whether multiple random trials were run or how the fraction π was drawn. This is the paper's most notable lack of rigor.

3. **The sensitivity metric (sens_l) has a subtle structural confound.** The denominator dist_l(D_probe_g, D_probe_g) captures the intra-class spread at layer l, which varies with depth. If earlier layers have tighter intra-class clusters, the denominator shrinks, mechanically affecting the ratio. The paper's conclusions (intermediate layers have lower sensitivity) go in the *opposite* direction of what this confound would predict (tighter clusters → inflated sensitivity), so the qualitative finding is likely robust. But the metric conflates intrinsic representation structure with sensitivity to shift, making precise quantitative comparisons across layers unreliable. The qualitative PCA projections (Figure 10) provide helpful complementary evidence.

4. **Source of pretrained model weights not specified.** The paper states it uses "publicly available pre-trained model weights" but does not list exact identifiers (e.g., torchvision checkpoint names, timm model IDs). This is a reproducibility gap — the results cannot be exactly reproduced without knowing which specific weight files were used.

### Trivial

None beyond the above.

## Nice-to-Haves

- **Variance/confidence estimates** for the data-efficiency curves (Figure 4), ideally with multiple random subsamples.
- **A brief remark on computational cost** — training one linear probe per candidate layer is not prohibitive but is worth acknowledging for practitioners.
- **An "average intermediate layer" baseline** alongside the "best layer" in Figures 3–6 for transparency.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **The harsh critic's claim that the sensitivity metric "mechanically inflates" intermediate-layer scores** — removed because the actual data shows the *opposite* pattern (lower sensitivity at earlier layers), meaning the concern does not threaten the paper's conclusions. If the confound were operating, it would make the paper's reported differences *underestimates*, not overestimates.
- **The critic's suggestion that the paper should compare against random/average intermediate layers** — downgraded to Minor (it's already partially addressed by Figure 8). The "best layer" vs "last layer" comparison is standard practice when model selection uses a held-out validation set, which the paper does.
- **The critic's comment about "zero-shot setting not being comparable to prior methods"** — removed because the paper acknowledges this distinction (Section 4.3: "This scenario was not considered in previous last-layer retraining methods") and frames it as an extension, which is fair.
- **Strength Finder's generic phrasing about "important problem" and "timely question"** — these are not specific enough to retain as actionable strengths.

## Novel Insights

The reviews surface one insight not fully articulated in the paper itself: the data-splitting ambiguity and model-selection asymmetry, taken together, suggest that the few-shot results may be weaker than the headline numbers suggest — but the zero-shot results, which are the paper's most novel contribution, are not affected by either concern. This means the paper's strongest and cleanest evidence is in the zero-shot setting (Section 4.3), not the few-shot setting (Section 4.2), which is somewhat at odds with how the paper is framed (the abstract mentions both settings). The paper would be stronger if it explicitly acknowledged this asymmetry in evidentiary strength.

## Suggestions

1. **Clarify the data splits for Section 4.2.1** — state explicitly: (a) what data was used for training the probes, (b) what data was used for layer selection, and (c) whether the test set was ever used for model selection. If the protocol is clean, one paragraph can resolve the most serious concern.

2. **Add error bars** to the key quantitative claims, even if only from a small number of random trials. For an empirical study, the absence of variance estimates is the single most impactful improvement the authors could make.

3. **Add a brief caveat** to Figures 3–6 noting that "Best layer" is selected from multiple candidates via a held-out set, while "Last layer" is a single fixed baseline.

4. **Specify exact model weight sources** in the final version for reproducibility.

## Score and Decision

The paper makes a genuine and useful empirical contribution: it convincingly demonstrates that intermediate-layer representations can dramatically outperform penultimate-layer representations for OOD generalization, especially in the zero-shot setting. The zero-shot CelebA result (82.0% vs. 56.0%) is striking and not subject to the data-splitting ambiguity. The breadth of datasets and architectures is a strength. However, the data-splitting ambiguity in the few-shot experiments (Section 4.2.1) must be resolved, and the absence of error bars is a nontrivial gap in an otherwise well-designed empirical study. The core claims are likely correct, and the issues are addressable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>