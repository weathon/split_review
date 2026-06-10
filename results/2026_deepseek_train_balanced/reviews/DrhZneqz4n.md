Now let me produce the final review.

## Summary
This paper proposes SinMDM, a diffusion model that learns from a single motion sequence of arbitrary skeletal topology and generates diverse, variable-length motions. The core architectural contribution is a shallow UNet with QnA (learned-query local attention) instead of global attention, designed to narrow the receptive field and prevent the overfitting that plagues standard architectures trained on a single example. The method is demonstrated on motion composition, harmonization/style transfer, long-motion generation, and crowd animation — all at inference time without retraining.

## Strengths
- **Architecturally grounded solution to the single-instance overfitting problem**: The paper identifies that standard UNets and transformers overfit on single motion sequences due to their large receptive fields, and proposes a concrete remedy — a shallow UNet with local QnA attention (Sec. 4). The ablation study (Sec. 6.4) systematically validates this design by varying receptive field width, attention type (QnA vs. vanilla vs. none), and backbone (UNet vs. transformer), showing that only the narrow-receptive-field QnA-based UNet achieves good scores across fidelity, inter-diversity, and intra-diversity simultaneously.

- **Inference-time multi-application framework without per-application retraining**: Motion composition (in-betweening, expansion, trajectory/joints control), harmonization/style transfer, long-motion generation, and crowd animation are all performed at inference time (Sec. 5), in contrast to Ganimator which requires specialized training per application. The unification of these tasks under a single mask-and-denoise mechanism is a clear advantage over prior work.

- **Quantitative outperformance over the sole prior single-motion work (Ganimator)**: On the Mixamo benchmark, the paper reports that SinMDM outperforms Ganimator on all metrics except one (lines 446–448). On the Gangnam-style sequence selected by Ganimator's own authors, SinMDM leads on two of three metrics (lines 454–456). A user study (lines 467–470) shows user preference. These claims are backed by reported comparisons.

- **Evaluation on diverse-topology skeletons**: The paper evaluates on Mixamo's 70 characters with unique bone lengths and topologies, as well as animals and imaginary creatures (abstract, lines 68–69), directly addressing the motivation that motion data for non-human skeletons is barely existent.

- **Extended evaluation methodology**: The paper identifies that Ganimator's metrics lack inter-diversity and intra-diversity measures (lines 420–421) and adds these missing dimensions — a genuine methodological improvement for single-motion evaluation.

## Weaknesses

### Fatal
None.

### Major
- **The Harmonic Mean metric's normalization procedure undermines the quantitative claims**: The Harmonic Mean (lines 406–412) normalizes each metric by the 90th percentile of the *computed scores*, meaning the normalization denominator changes depending on which methods are in the comparison set. This makes the composite metric non-comparable across experiments and potentially inflates results depending on set composition. Critically, the paper explicitly allows negative normalized values in the harmonic mean ("Note that a negative value is therefore valid," line 406) — the harmonic mean of a set containing negatives is mathematically problematic and can produce uninterpretable or undefined aggregates. Since the paper uses the Harmonic Mean to argue that SinMDM exhibits a "notable advantage" (line 448), this is a significant evidential concern that requires resolution (justify the metric formally, report raw scores alongside it, or use a more principled aggregation method).

- **The "MDM trained on crops" baseline in the user study is undefined**: Line 468 states that the user study compares SinMDM against "MDM trained on crops" but never explains what "crops" means, how crop sizes were chosen, how MDM (a large-dataset transformer model) was adapted for single-motion learning, or how training was configured. Without this information, the reader cannot assess whether this baseline is a reasonable competitor or an artificially weak one. Since the user study results are presented as evidence of quality ("significantly preferred by the users," line 470), this is a clear evidential gap.

### Minor
- **The quantitative comparison rests on a single meaningful baseline**: On the Mixamo benchmark, SinMDM is compared only against Ganimator (the sole existing single-motion work, which the paper acknowledges). On the HumanML3D benchmark, the only results presented are internal ablations of SinMDM variants — no external comparison at all. The paper explains that Mixamo uses Ganimator's own metrics while HumanML3D uses deep-feature metrics (lines 394–398), which is a reasonable rationale, but the absence of any external comparison on the more modern benchmark weakens the overall case. An explicit statement of whether Ganimator can be evaluated on HumanML3D metrics would strengthen the evaluation.

- **The receptive field size is never reported in concrete terms (e.g., number of frames)**: The paper's central architectural claim is that a narrow receptive field is critical for single-motion learning (Sec. 4), and the ablation (lines 493–495) compares "narrow" vs. "wide" by varying UNet depth. However, the actual receptive field size in frames is never reported for any configuration. Without quantification, the reader cannot assess what "narrow" concretely means or whether the fidelity-diversity trade-off is cleanly parametric.

- **The style transfer claim is overstated**: The paper presents style transfer as "a non-trivial task" (line 91) but implements it as a special case of harmonization where the entire motion is replaced with a reference and low-pass filtered (lines 340–341). This is closer to motion smoothing with content injection than to style transfer as conventionally understood in the literature (where content and style representations are separated and recombined). The paper would benefit from tempering this claim or providing evidence that the result genuinely transfers stylistic motion properties.

- **The user study lacks statistical rigor**: The paper states that SinMDM is "significantly preferred by the users" (line 470) but reports no statistical significance test, p-values, confidence intervals, or inter-rater agreement measures. With 10 users × 8 motions, the sample is modest, and no effect size or significance analysis is provided.

### Trivial
None.

## Nice-to-Haves
- Report the receptive field size (in frames) for each architecture variant and perform a parametric sweep over receptive field widths.
- Report raw metric scores alongside the Harmonic Mean so readers can assess trade-offs without relying on the composite.
- Provide a clearer explanation of the "MDM trained on crops" baseline or replace it.
- Provide statistical significance measures for the user study.

## Removed Points
These points were flagged in reviewer inputs but removed after verification:

1. "No systematic runtime/memory comparison" — the paper explicitly defines time-space efficiency metrics (lines 429–431: parameters, iterations, time per iteration, total running time) and reports them in the Mixamo comparison table. The critic overlooked this.
2. "QnA attention insufficiently explained" — the paper describes QnA's mechanism clearly (lines 244–247: learned queries shared by all windows, shift-invariant local attention) and cites the original paper.
3. "Missing related work discussion" — per rules, this cannot be assessed without external knowledge.
4. "Limitation about retraining for new skeletons unaddressed" — the paper acknowledges "limited ability to synthesize out-of-distribution" (line 525), which covers this.
5. "Hyperparameters not reported" — per rules, undisclosed hyperparameters are a reproducibility nitpick to be removed.
6. "Ganimator not compared on HumanML3D without justification" — the paper does provide a rationale (lines 394–398: different metrics for different benchmarks).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Replace or substantially justify the Harmonic Mean normalization: use a fixed, principled reference value and do not allow negative values in the harmonic mean. Report raw scores alongside any composite.
2. Explicitly define the "MDM trained on crops" baseline: specify crop sizes, training procedure, and any modifications made to adapt MDM for single-motion learning.
3. Attempt to evaluate Ganimator on the HumanML3D benchmark's deep-feature metrics, or clearly state why this is infeasible.
4. Report the receptive field size in frames for each ablated configuration to substantiate the central architectural claim.
5. Provide statistical significance tests for the user study.

## Score and Decision

The paper's core idea — controlling receptive field width for single-instance learning — is well-motivated, and the architecture-level ablation convincingly shows the design's internal validity. However, the evaluation has genuine gaps that affect the headline claims. The Harmonic Mean metric's normalization procedure is mathematically concerning and directly impacts the paper's claim of a "notable advantage." The user study relies on an undefined baseline. These issues are addressable but weaken the evidence as it stands. At a top conference, the contribution is promising but not yet sufficiently supported.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>