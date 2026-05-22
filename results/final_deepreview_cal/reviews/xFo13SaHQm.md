Now I have enough calibration context. Let me synthesize the final review.

## Summary

This paper identifies and formalizes the "copy-paste artifact" in identity-consistent image generation—where models replicate reference faces rather than generating controllable variations—and addresses it through three contributions: (1) **MultiID-2M**, a large-scale paired dataset of ~500k group photos with multiple reference images per identity; (2) **MultiID-Bench**, a benchmark with a novel Copy-Paste (CP) metric that quantifies reference bias; and (3) **WithAnyone**, a diffusion-based method using GT-aligned ID loss and ID contrastive loss with extended negatives to reduce copy-paste while maintaining identity fidelity. Experiments across 12 baselines, qualitative comparisons, ablations, and a user study show WithAnyone breaks the trade-off between identity similarity and copy-paste artifacts.

## Strengths

- **Breaks the copy-paste vs. identity-fidelity trade-off**: Table 1 and Figure 5 show WithAnyone achieving Sim(GT)=0.460 (second only to InstantID at 0.464) while maintaining the lowest copy-paste score (0.144) among ID-specific methods, and is the only model off the regression curve that all other methods follow. This is a direct, quantifiable demonstration of the paper's central claim.

- **Novel Copy-Paste metric (ℳ_CP)**: Equation (2) formalizes reference bias as the relative angular distance of the generated embedding toward the reference versus ground truth, normalized by the reference–GT distance. This moves beyond the standard practice of reporting only Sim(Ref), which rewards copying, and provides a principled way to compare methods on the artifact the paper targets.

- **GT-aligned ID loss**: Section 5.1 and Figure 7 show that using ground-truth landmarks (rather than predicted landmarks from noisy generations) enables applying ID supervision across all noise levels with negligible overhead, providing more informative gradients at high noise. This is a clean engineering contribution with demonstrated impact.

- **Large-scale paired dataset with comprehensive benchmark**: MultiID-2M provides ~500k group photos with ~1M reference images across ~3k identities (avg. 400 per identity), filling a genuine resource gap. MultiID-Bench standardizes evaluation with 435 test cases, multiple metrics, and long-tail identity selection that avoids training-set leakage.

- **Thorough evaluation**: 12 baselines spanning general customization models (OmniGen, GPT-4o, FLUX.1 Kontext) and face-specific methods (PuLID, InstantID, UniPortrait) across single- and multi-person subsets, plus ablation studies and a user study with 10 participants ranking 230 groups on four criteria.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Controllability evaluated only on GT-matching prompts**: The benchmark uses prompts that exactly describe the ground-truth image (Section 4: "a prompt describing the GT"). While the CP metric and Sim(GT) do capture the model's ability to deviate from the reference toward the GT, a direct test of controllability would use prompts specifying deliberate variations from the reference (e.g., "smiling" when the reference is neutral) and measure whether the model complies while preserving identity. The qualitative examples in Figure 6 show this capability anecdotally, but it is not quantified. This gap between the paper's stated goal ("controllable generation") and the evaluation protocol weakens the narrative but does not invalidate the core contributions.

- **Internal trade-off in the ablation under-analyzed**: Table 3 shows that removing extended negatives (w/o Ext. Neg.) improves CP to 0.074 (versus 0.161 in the full setting) but drops Sim(GT) to 0.368 (versus 0.405). This indicates that the extended negatives are needed for identity fidelity but increase copy-paste artifacts. The paper's claim of "breaking the trade-off" refers to the *external* trade-off across methods, which is supported, but the *internal* behavior shows the trade-off is still present—the method simply chooses a more advantageous operating point. A brief discussion of this would improve clarity.

- **CP metric sensitivity to small reference–GT angles not analyzed**: The denominator of ℳ_CP uses max(θ_tr, ε). When the reference and GT images happen to be very similar (small θ_tr), small deviations in the generated embedding could be amplified. The paper does not analyze the distribution of θ_tr across benchmark cases or test the metric's robustness to this scenario. Since CP is a headline metric, this is a gap in technical rigor.

### Trivial
None.

## Nice-to-Haves

- A direct controllability experiment with out-of-distribution prompts (e.g., "now smiling," "looking left") would strengthen the claim of controllable generation.
- An analysis of ℳ_CP's correlation with θ_tr (scatter plot or correlation coefficient) would address the sensitivity concern.
- An ablation on the loss weight ratio λ_ID : λ_CL would show robustness of the hyperparameter choice.

## Removed Points

- *Criticism about the paper's "controllability" framing being misleading* — removed because the CP metric and Sim(GT) do quantify the model's ability to generate non-reference outputs, and the paper provides substantial qualitative evidence. The weakness is kept in a softened form above.
- *Request for detailed dataset statistics (images per identity, pose variation)* — removed because the paper states averaging 400 per identity and refers to Appendix C for further statistics. The appendix is stripped by the parser but exists in the original submission.
- *Criticism about missing correlation coefficient between CP and human rankings* — removed because the paper states "a moderate positive correlation" without claiming a specific number, which is acceptable for a user study summary.
- *Reproducibility concerns about undisclosed hyperparameters (λ_ID, λ_CL)* — the paper states both are set to 0.1 across all training phases, which is sufficient.
- *Generic strengths about "addressing an important problem" and "clear writing"* — removed as superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a direct controllability experiment: sample a subset of benchmark cases, construct prompts that explicitly differ from the GT image (e.g., "now smiling" when the GT shows a neutral expression), and report prompt-following accuracy alongside identity similarity.
2. Include a scatter plot of ℳ_CP vs. θ_tr for all benchmark cases to demonstrate that the metric is stable across the range of reference–GT distances.
3. Add one sentence in Section 6.3 discussing the internal trade-off observed in the ablation (w/o Ext. Neg. improves CP but hurts Sim), clarifying that the method's advantage is in choosing a better operating point on this trade-off curve.

---

## Calibration Report

**Round 1 bracket:** 6.5–7.5 (based on comparison to middle-band anchors at avg 4.40–6.67 and strong-band anchors at 7.33–8.00).

**Round 2 narrow:** Compared against InstantPortrait (6.67, similar dataset+method structure but less comprehensive evaluation and fewer baselines), UIFace (6.00, narrower scope and fewer contributions), MGFR (7.33, face restoration with dataset, but method novelty is weaker and evaluation less comprehensive).

**Final score rationale:** 7.0. The paper is clearly stronger than UIFace (6.00) and InstantPortrait (6.67) — it has more comprehensive contributions (dataset + benchmark + metric + method + 12-baseline evaluation + user study), identifies an genuinely underappreciated problem, and provides convincing evidence. It is comparable to MGFR (7.33) but falls slightly short of the strongest work in the space due to the controllability evaluation gap and the unanalyzed CP metric sensitivity. The weaknesses are real but minor and addressable; they do not threaten the paper's core claims.

**All anchors considered:**
- NWvsm2VxAM (3.00, Round 1, weak): Identity-consistent generation paper; less relevant and much weaker.
- 12iSWNLDzj (3.00, Round 1, weak): Adversarial face masks; not topically relevant.
- FsgGBhNIt4 (3.00, Round 1, weak): Unsupervised facial attributes; not relevant.
- KK29oh8jZs (3.00, Round 1, weak): OOD detection; not relevant.
- Bz9wjToCS (4.40, Round 1): Face de-identification; much weaker.
- riieAeQBJm (6.00, Round 1&2): Synthetic face recognition; narrower scope.
- daRu82GAoZ (5.00, Round 2): Origin identification; different task.
- ZkFMe3OPfw (6.67, Round 1-3): Portrait editing; similar structure but less evaluation breadth.
- EE2tIwKhSW (5.50, Round 2): MIA on diffusion models; not relevant.
- Qg0gtNkXIb (5.25, Round 2): Memorization benchmark; not relevant.
- UkLSvLqiO7 (5.50, Round 2): Diffusion reproducibility; not relevant.
- f8S3aLm0Vp (6.50, Round 2): Copyright detection; different task.
- m9RNBZewW2 (7.33, Round 2&3): Face restoration with dataset; comparable strength, slightly more novel method in the paper under review.
- uELjxVbrqG (7.00, Round 2): Face recognition constraint; different task.
- U3PBITXNG6 (7.50, Round 2): Inverse problem benchmark; very different domain.
- bnINPG5A32 (8.00, Round 1): Training-free personalization; stronger paper, different approach.
- vaEPihQsAA (7.60, Round 1): Talking body generation; different task.
- u1cQYxRI1H (10.00, Round 1): Illumination harmonization; much stronger paper, different domain.
- 6O3Q6AFUTu (8.00, Round 1): Image interpolation; different domain.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>