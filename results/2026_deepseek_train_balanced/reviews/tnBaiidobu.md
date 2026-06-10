## Summary

This paper tests whether CLIP's strong zero-shot performance on ImageNet-based OOD benchmarks is primarily caused by the presence of highly similar (even duplicate) images from its web-scale LAION training set. The authors formalize a "similarity gap" between training and test sets, prune LAION to match ImageNet's similarity gap to each OOD benchmark, then retrain CLIP from scratch and evaluate. The central finding—presented in Table 1 and the effective-robustness comparison (Section 7)—is that after removing only ~12.4M of ~201M samples to align similarity gaps, CLIP's accuracy on ImageNet-Sketch drops from 50.21% to 44.12%, far above the ~14% expected from an ImageNet-trained model at the same ID accuracy level. The paper concludes that high train-test similarity alone cannot explain CLIP's OOD generalization.

## Strengths

1. **Principled causal intervention via similarity-gap alignment (Sec. 3.4, Fig. 3).** The paper formalizes the similarity gap (Eq. 3–4) and uses it to surgically remove from LAION only those samples whose nearest-neighbor similarity to a test point exceeds any ImageNet sample's similarity. This creates a controlled counterfactual where LAION matches ImageNet's train–test similarity, enabling a clean causal test rather than a purely correlational analysis.

2. **Quantitative refutation using the effective-robustness baseline (Sec. 7).** After aligning similarity gaps on ImageNet-Sketch, the pruned model achieves 44.78% accuracy, while the effective-robustness line from Fang et al. (2022) predicts only ~14% at the same ImageNet-Val performance level—a 30+ percentage-point gap. This is the paper's strongest evidence and directly quantifies that similarity alone cannot explain CLIP's performance.

3. **Discovery of a 100M core set (Sec. 4.2).** By far-pruning LAION (removing samples *dissimilar* to six benchmarks simultaneously), the paper identifies a 100M subset on which CLIP matches or slightly exceeds its full-dataset performance. This provides convergent evidence: if high-similarity samples were the dominant factor, far-pruning should hurt performance rather than maintain it.

4. **Systematic ablation across three pruning strategies and multiple dataset sizes (Fig. 2, Sec. 4.2).** The comparison of near-pruning, far-pruning, and random-pruning at 50M, 100M, and 150M shows that near-pruning causes rapid degradation while far-pruning barely reduces accuracy, ruling out dataset-size confounds and validating similarity-based pruning as a meaningful intervention.

5. **Concrete duplicate-rate quantification (Sec. 4.3).** The paper reports that 3.1% of ImageNet-Sketch images have duplicates in LAION vs. only 0.04% in ImageNet, and 2.67% of ImageNet-V2 images are duplicated in ImageNet vs. 0.14% in LAION. These numbers ground the similarity-distribution differences in measurable overlap statistics.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claim is well-supported; the issues below are addressable limitations that do not undermine the central conclusion.

### Minor

1. **No variance estimates across the central experiments.** Every model in Table 1 is trained once. No standard deviations, confidence intervals, or alternative seeds are reported. CLIP training on hundreds of millions of images involves stochastic optimization with non-negligible noise; the "combined-pruned" model's 6-point drop on Sketch (50.21→44.12) and 5-point drop on ImageNet-R (72.9→67.88) are interpreted as "not significant," but without variance estimates it is impossible to gauge whether these magnitudes are stable or within training noise. This does not threaten the conclusion—the qualitative gap between 44.12% on Sketch and the ~14% effective-robustness baseline is large enough to survive generous variance—but it weakens the precision of the paper's quantitative claims about the *modest* size of the drop.

2. **Circularity of the similarity metric.** The perceptual similarity metric uses a LAION-trained ViT-B/16 embedding space—the same training distribution whose properties the paper interrogates. The concern is not philosophical only: if the embedding space already encodes invariance learned from LAION's diversity (e.g., mapping sketches close to natural images), it could understate how genuinely "similar" LAION images are to test samples. The paper acknowledges this (Discussion, "Similarity metric" paragraph) and references an ablation with alternative metrics in the appendix (App.~\ref{app:comparing_metrics}). However, the metric choice is structurally entangled with the central claim, and the ablation is deferred rather than presented as a main-table robustness check. The finding is unlikely to be overturned by a different metric (the qualitative pattern is too large), but the paper would be stronger with a primary result verified using at least one alternative embedding space (e.g., DINOv2, ImageNet-trained ResNet).

3. **The similarity-gap framework requires an engineered patch rather than holding naturally.** The formal method (Sec. 3.4) assumes D_S (ImageNet Train) is a subset of D_L (LAION) to guarantee $s_i(D_S) \leq s_i(D_L)$. The paper explicitly adds ImageNet images to LAION with the caption "a photo of a {class}" to satisfy this. This introduces a confound: (a) the added images have a different caption format than natural LAION captions, and (b) the pruned splits all contain these added ImageNet images, which could themselves contribute to retained performance. The paper reports an ablation without the ImageNet addition (referenced to Tab.~\ref{tab:app_main_exp_wo_imagenet} in the appendix), showing similar trends, which mitigates but does not fully eliminate the concern that the reasoning is less clean than the framing suggests.

4. **The core set's actual performance numbers are deferred to the appendix.** The paper identifies a 100M core set as a practical contribution (Sec. 4.2, line 137–139) but only reports that it "roughly matches" the baseline and "outperforms" a de-duplicated dataset of the same size—without giving actual numbers in the main text. Given that dataset curation is listed as a contribution, the main text should contain the concrete performance figures to substantiate this claim.

5. **Framing of the performance drop as "not significant" could be sharper.** The conclusion states that models "do not significantly lose performance" (line 360). The combined-pruned model drops from 50.21→44.12 on Sketch (12% absolute, 10.8% relative) and 72.9→67.88 on ImageNet-R (5% absolute, 4.8% relative). These absolute drops on a 100-point scale are non-trivial. The paper's actual argument does not depend on the drop being zero—it depends on performance remaining far above the effective-robustness baseline—so the framing could be more precise to avoid overstatement.

### Trivial
None.

## Nice-to-Haves

- Present the effective-robustness comparison as a full curve with the paper's models plotted as data points, rather than a single textual comparison.
- Run 2–3 seeds for at least the sketch-pruned condition to confirm the stability of the headline 44.78% result.
- Move one alternative similarity-metric ablation (e.g., DINOv2) from the appendix into the main text.
- Provide a clearer terminological separation between the "far-pruned" 100M coreset (based on six-test-set far-pruning) and the "combined-pruned" similarity-gap dataset (Table 1), which serve different purposes.

## Removed Points
Points removed per filtering discipline (listed for completeness, treat with caution):

- **Duplicate section content (lines 67–198 vs. 200–284):** Appears to be a PDF-extraction artifact; the original submission likely does not contain this duplication. Removed per formatting-artifact rule.
- **"Typo/spelling/formatting" critic notes:** No such specific criticisms were made; the critic's note about "the similarity hypothesis appearing twice" is addressed above.
- **Criticism that D_S subset assumption is not "structurally true":** The paper explicitly acknowledges the assumption, engineers a fix, and provides an ablation without it. The critic's concern is reasonable but the paper addresses it; remaining concern is captured in Weakness #3 above.
- **Generic speculation about confounders not grounded in paper content:** Removed per filtering rules.
- **Missing related work:** Not permitted to mention per instructions.

## Novel Insights

None beyond the paper's own contributions. The paper's framing—testing a causal hypothesis through similarity-gap alignment rather than correlation—is itself the methodological insight, and the reviews do not add analytical perspectives beyond what the paper already provides.

## Suggestions

1. Add 2–3 training seeds for the sketch-pruned and combined-pruned conditions reported in Table 1, and report the mean ± std across runs.
2. Move at least one alternative similarity-metric result (e.g., DINOv2, ImageNet-trained ResNet) into the main table for the sketch-pruned condition as a robustness check on the metric circularity concern.
3. Include the actual performance numbers for the 100M core set in the main text rather than deferring to the appendix.
4. Replace the phrase "do not significantly lose performance" with a more precise characterization (e.g., "performance drops by 10.8% relative on Sketch but remains far above the effective-robustness baseline").

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>