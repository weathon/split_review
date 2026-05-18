Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes ALBAR, an adversarial training framework that mitigates both background and foreground biases in video action recognition. The key idea is to construct a static clip (a single frame repeated) and apply an adversarial cross-entropy loss, an entropy maximization loss, and a gradient penalty loss — all using the same 3D encoder with no external attribute classifiers or separate critic models. The method achieves state-of-the-art contrasted accuracy (53.02%) on HMDB51 SCUBA/SCUFO, improving by over 12% over prior work. The paper also identifies and addresses a background leakage issue in the existing UCF101 bias protocol by replacing bounding boxes with SAMTrack segmentation masks.

## Strengths

- **Novel adversarial framework requiring no bias attribute labels or external critics.** Unlike prior debiasing methods that rely on separate attribute classifiers (Duan et al.), scene detectors, or pre-trained salience models (StillMix), ALBAR operates on a single 3D encoder with a self-contained static-clip adversarial objective. The paper clearly motivates this design in Section 1 and develops it across Sections 3.1–3.4. This architectural simplicity is a genuine departure from prior work.

- **New state-of-the-art on HMDB51 background/foreground bias benchmarks.** ALBAR achieves 53.02% contrasted accuracy, an absolute improvement of over 12% over the previous best (Table 1), and reaches 53.68% when combined with StillMix. These are large, unambiguous gains on a protocol that jointly measures both bias types. The result directly supports the paper's central claim.

- **Identification and remediation of background leakage in the UCF101 bias protocol.** The paper correctly identifies that bounding-box masks from THUMOS-14 leak background context into the SCUBA/SCUFO evaluation (Section 4.2, Figure 2), and proposes a fix using SAMTrack segmentation masks. This is a valuable methodological contribution to the community's evaluation infrastructure.

- **Informative ablation isolating each loss component.** Table 3 experimentally justifies the composite objective: adversarial loss alone causes label-flipping (row b), entropy maximization alone is weak (row c), gradient penalty alone has little effect (row d), but the combination yields strong gains (row h). This directly supports the design rationale in Section 3.

- **Analysis of static frame selection strategy.** Table 4 compares first/middle/last/random frame choices for constructing the static clip and finds that middle-frame selection works best, with a clear explanation (the middle frame is a hard negative because it depicts the action underway). This provides practical guidance for practitioners.

- **Demonstration of complementary benefits with existing augmentations.** ALBAR can be combined with StillMix to further improve results (Table 1), showing it is not competing with augmentation-based approaches but can be integrated into existing pipelines.

## Weaknesses

### Fatal
None.

### Major

- **The new UCF101 evaluation protocol relies on per-video manual inspection of segmentation masks, undermining reproducibility.** Section 4.2 states: "Each testing video is manually checked for accurate segmentation." This introduces an unscalable, uncalibrated step — no inter-annotator agreement, no objective quality criteria, and no automated verification pipeline are reported. As described, the protocol functions as a one-off private dataset rather than a usable benchmark for future work. The conceptual critique of the old bounding-box protocol is valid, but the proposed fix needs a reproducible release (masks + an automated/semi-automated quality-control script) to be a true contribution. This does not affect the validity of the HMDB51 results (the main contribution), but it weakens the UCF101-based claims and the broader methodological contribution of the benchmark fix.

### Minor

- **No variance estimates for the headline results.** The paper states "reporting the average Top-1 accuracy across 3 runs" (Section 4.4) but does not report standard deviations or per-run values for any of the main tables. While 3-run averaging is standard practice in this sub-area, a 12+ point gain over the best competitor demands variance estimates to confirm it is not driven by optimization noise. The absence of this information leaves room for doubt — especially because the paper does not specify whether hyperparameters were separately tuned per baseline method (they appear to use the same recipe for all, which could disadvantage methods requiring different schedules).

- **IID accuracy trade-off is reported but not discussed.** The paper includes IID accuracy in the tables alongside OOD scores, yet never comments on whether debiasing degrades in-distribution performance. From the text, the IID accuracy on HMDB51 appears to hold steady or improve slightly — which would be a noteworthy positive result (removing spurious features acting as a regularizer) — but the paper passes over this without analysis. A brief discussion (even one sentence) would strengthen the paper. This is a presentation gap rather than a scientific one.

- **Downstream task gains (Table 5) are modest and not statistically characterized.** The improvements on UCF_Crime anomaly detection and THUMOS14 action localization appear small. The paper reports single runs with fixed hyperparameters for the downstream methods. Given task stochasticity, the significance of these results is unclear. The authors should either report variance or explicitly characterize these as suggestive rather than conclusive.

### Trivial

- **Integrated gradients qualitative evidence (Figure 3) is acknowledged by the authors themselves as showing similar attribution maps between baseline and ALBAR.** The paper already observes this: "both the baseline and our method have similar attribution maps" (line 109). The interpretation that the baseline is still using foreground appearance cues despite similar gradients is plausible but post-hoc. This figure is illustrative, not evidential, and the paper's framing is appropriately cautious — no revision needed.

## Nice-to-Haves

- A diagnostic plot of gradient norm w.r.t. static input over training (with vs. without $\mathcal{L}_{gp}$) would strengthen the claim that the gradient penalty actually reduces sensitivity to static inputs.
- An explicit computational graph or pseudocode clarifying the gradient flow for the adversarial loss (negative cross-entropy sign convention) would aid reproducibility, though the current description ("negative cross-entropy loss" / "negative gradients") is sufficient for practitioners familiar with adversarial debiasing.
- An automated mask quality check (e.g., IoU threshold relative to the original bounding box) to replace or supplement the manual inspection step for the UCF101 protocol.

## Removed Points

These points are flagged to be removed — treat them with caution.

- *Criticism about Equations 1 and 2 missing from parsed text, and concern about whether the adversarial loss uses gradient reversal or negated cross-entropy.* The equations for the adversarial cross-entropy objectives appear in Sections 3.1 and 3.2, which were stripped by the parser (these sections exist in the original submission). The paper states "negative cross-entropy loss" and "adversarial loss through negative gradients" (lines 15, 134), which is a clear enough description of the sign convention. Removed as parser artifact.
- *Criticism that the WGAN-GP-style "1-centered interpolation" is missing from the gradient penalty formulation.* The paper's design is intentionally different: it directly minimizes the gradient norm w.r.t. the static clip, which is a valid regularizer. The WGAN-GP analogy is explicitly noted only as inspiration. This is a design choice, not a flaw.
- *Criticism that the qualitative evidence (Figure 3) is weak because the attribution maps look similar.* The paper itself acknowledges this observation and provides a plausible interpretation. Sentence-level pedantry that does not affect the contribution.

## Novel Insights

The adversarial approach proposed here — applying the adversarial loss, entropy maximization, and gradient penalty to static clips within a single 3D encoder — represents a cleaner formulation than prior two-classifier adversarial debiasing (Bahng et al., Bao et al.). The key insight from the ablation is that the adversarial loss alone engenders a "label-flipping" degenerate solution, and that entropy maximization (forcing uniform predictions on static inputs) together with gradient penalty (reducing sensitivity to static inputs) are both necessary to prevent that collapse. This three-part design rationale is the paper's most important conceptual contribution and could inform future debiasing methods beyond action recognition. The identification of how static frame *position* matters (middle frame > random > first/last) is also practically useful and non-obvious.

## Suggestions

1. **Add standard deviations to all main result tables** (Tables 1, 2, 3, 4, 5). Even if the field standard is 3-run averages without error bars, the size of the claimed improvement (12+ points) makes this essential.
2. **Release the corrected UCF101 segmentation masks** with an automated quality-control script (e.g., flagging masks that cover less than X% of the bounding box area), and evaluate whether automatic-only masks change the benchmark results.
3. **Add a brief discussion of the IID accuracy trade-off** — in particular, note whether ALBAR preserves or improves IID accuracy, and offer a hypothesis for why (e.g., spurious feature removal acting as a regularizer).
4. **Acknowledge the downstream task results as suggestive rather than conclusive** if per-run variance cannot be provided.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>