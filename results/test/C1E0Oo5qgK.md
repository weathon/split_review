Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper identifies a "model-fitting" problem in conditional diffusion sampling with guidance, where samples are argued to overfit to the guidance classifier's parameters rather than generalizing. The paper proposes **Compress Guidance (CompG)**, which reduces guidance computation by applying gradients at a subset of timesteps and reusing them at intermediate steps, with an early-heavy timestep distribution. Experiments across ADM, CADM, DiT, GLIDE, and Stable Diffusion show CompG reduces guidance steps by 5–10× and computation time by ~40% while often improving FID/sFID/Recall over vanilla guidance.

## Strengths

1. **CompG is a well-motivated, empirically effective method across diverse settings.** The method improves or matches FID while substantially reducing computation on ImageNet (ADM FID 11.65 vs 11.96 with 5× fewer guidance steps, CADM FID 1.82 vs 2.07 unguided), MSCOCO (GLIDE ZFID 33.12 vs 34.78, SD FID 14.04 vs 16.04), and across classifier guidance, classifier-free guidance, and text-to-image. This breadth makes the practical contribution credible and useful.

2. **The analysis of guidance properties (gradient balance, continuity, magnitude sufficiency) and the failure of naive alternatives (early stopping → forgetting, uniform skipping → non-convergence) is illuminating.** The paper does not just propose a method; it diagnoses why simpler baselines fail and designs CompG to address all three properties simultaneously. Table 4 directly shows CompG closes the on-sampling/off-sampling accuracy gap better than vanilla or ES.

3. **Systematic ablation of the $k$ parameter provides actionable guidance for practitioners.** Table 6 (Table 5 in paper) shows increasing $k$ (shifting guidance early) reduces guidance steps from 50 to 28 while maintaining or improving FID, demonstrating a clear quality-efficiency trade-off.

## Weaknesses

### Fatal
None.

### Major

1. **The central "model-fitting" claim is partially confounded by noise-awareness of the classifiers.** The paper defines model-fitting via the gap between on-sampling accuracy (90.8%) and off-sampling accuracy (62.5% for OADM-C, 34.2% for ResNet152). However, the paper states the on-sampling classifier is "noise-aware ADM classifier" (trained on noisy images at multiple timesteps), while the off-sampling OADM-C is described only as having "the same architecture and performance" — it is **not explicitly stated** whether it too was trained on noisy images. If the off-sampling classifier was trained only on clean images, then at early-to-mid timesteps where samples are noisy, the accuracy gap would partially reflect distribution shift rather than (just) overfitting to the guidance classifier's parameters. The ResNet152 figure is further contaminated by architecture differences and lack of noise-aware training. The visual evidence (Evidence 3, orange features for goldfish) and the loss convergence pattern are still meaningful independent pieces, but this weakens the paper's central diagnostic claim considerably. The method's practical value does not depend on this diagnosis, but the paper's framing does.

### Minor

1. **The theoretical derivation (Theorem 1) is not rigorous and adds little to the paper.** The theorem assumes $q(\mathbf{x}_0)$ is Gaussian (unrealistic for images) and assumes $\|\epsilon - \epsilon_\theta(\mathbf{x}_{t_1}, t_1)\| \approx \|\epsilon - \epsilon_\theta(\mathbf{x}_{t_2}, t_2)\| \approx \Delta$, which is questionable since noise prediction error depends on $t$. The proof also contains a likely typo (comparing the same quantity against itself). The method is validated empirically and does not rely on this theory; the derivations could be condensed to intuition without loss of rigor.

2. **The contribution of gradient reuse vs. early-heavy scheduling is not fully disentangled.** The paper compares CompG against ES (early stop, which fails) and UG (uniform skip, which fails), showing CompG works while both alternatives fail. However, there is no ablation where the *same* early-heavy schedule as CompG is used *without* gradient reuse at intermediate steps. Such an ablation would isolate whether gradient reuse itself adds value beyond simply choosing an early-heavy schedule. Given that the $k$ ablation (Table 6) shows most of the benefit comes from concentrating guidance early, this separation would strengthen the paper.

3. **Implementation details needed for reproducibility are incomplete.** The paper does not report guidance scale values ($s$ or $w$) used for each experiment. Since CompG accumulates gradients at compressed steps, the effective guidance magnitude differs from vanilla guidance, and it is unclear whether the scale was re-tuned or kept constant. No pseudocode or algorithm box is provided — the description via Equations 12–14 is ambiguous about the exact application of accumulated gradients.

4. **The "compact rate" concept is defined but not experimentally analyzed.** The paper defines compact rate as $T/|G|$ and notes that larger values save computation, but provides no experiment or analysis of the trade-off at different compact rates.

### Trivial

1. **Inconsistency between abstract and conclusion.** The abstract claims "reducing the required guidance timesteps by nearly 40%," but the conclusion states "reduce the number of guidance steps by at least five times" (80% reduction) with running time reduced by ~40%. The abstract appears to conflate timestep reduction with computation time reduction. The correct statement (running time ~40%, guidance steps 5×) is in the conclusion.

2. **Formatting error in Theorem 1 proof** where the inequality compares $||\Tilde{\xb}_0^{(t_1)} - \xb_0||$ against itself (line 87) instead of against $||\Tilde{\xb}_0^{(t_2)} - \xb_0||$. This is a typesetting issue but should be fixed.

## Nice-to-Haves

- An ablation comparing CompG against an early-heavy schedule *without* gradient reuse (i.e., simply skipping guidance on non-scheduled steps) would cleanly isolate the benefit of gradient reuse.
- Reporting guidance scale values used in each experiment and whether they were tuned separately for CompG vs. vanilla.
- Including a pseudocode block or algorithm description for CompG to clarify the gradient accumulation schedule.
- Explicitly stating whether the off-sampling OADM-C classifier was trained on noisy images (like the on-sampling classifier from ADM) or only on clean images, and if the accuracy gap persists after controlling for this.

## Removed Points

- **"Confidence intervals likely overlapping" (for ImageNet256x256 FID 11.96 vs 11.65):** Removed because the paper does not report confidence intervals, and this is speculation by the reviewer. The evidence across multiple settings, not a single comparison, supports the method.
- **"Appendix may provide details about off-sampling classifier training":** Removed per hard rules — appendix content is stripped by the parser and may exist in the original submission.
- **"The paper does not rely on these derivations for the proposed method" (as a criticism):** This is not a weakness — the paper is not claiming theoretical proof as a core contribution.
- **Strength 4 from Strength Finder ("provides theoretical grounding"):** Removed because it conflicts with the verified weakness that the theory is not rigorous. The "theoretical grounding" is not actually substantive.
- **Strength 1 from Strength Finder ("multiple independent evidence"):** Kept but tempered — the evidence is partially confounded but still contains meaningful independent pieces (visual examples, loss convergence patterns).

## Novel Insights

Beyond the paper's own contributions, the reviews collectively surface a useful meta-point: the paper's practical method (gradient reuse at a subset of steps with early-heavy scheduling) is well-validated empirically and genuinely useful, but the conceptual "model-fitting" frame it uses is overclaimed and somewhat orthogonal to the method's actual mechanics. The method may succeed simply because (a) guidance is most important early, (b) gradient magnitude changes slowly across consecutive timesteps, and (c) distribution of guidance over more steps via accumulation prevents forgetting. None of these require the model-fitting analogy to hold. Future work in this area could benefit from decoupling the diagnostic claim from the algorithmic contribution.

## Suggestions

1. **Reframe the paper's contribution around the practical method and the three identified properties** (gradient balance, continuity, magnitude sufficiency) rather than the model-fitting analogy. The model-fitting evidence is suggestive but not definitive; the paper is stronger positioned around the engineering insight that guidance gradients can be safely reused.

2. **Add the suggested ablation** (same early-heavy schedule as CompG, but without gradient reuse at intermediate steps — just run the diffusion model without guidance on skipped steps). This would directly demonstrate that gradient reuse, not just the schedule, is adding value.

3. **Report guidance scale values** used for each experiment and clarify whether the scale was re-tuned for CompG vs. vanilla guidance. Fix the abstract's "40% guidance timesteps" claim to match the conclusion.

4. **Explicitly clarify the off-sampling OADM-C training details** in the main paper. If it was trained on noisy images (same as the ADM classifier), state this explicitly. If not, acknowledge the distribution shift confound and reinterpret the accuracy gap accordingly.

## Score and Decision

**Overall assessment:** The paper proposes a practical, well-validated method for reducing guidance computation in diffusion models. CompG consistently reduces guidance steps by 5–10× and computation time by ~40% while maintaining or improving FID/Recall across classifier guidance, classifier-free guidance, and text-to-image — a genuine engineering contribution. The main weakness is overclaiming on the conceptual "model-fitting" diagnosis, for which the evidence is partially confounded. The theoretical derivation is weak but not central. These issues are addressable in revision by reframing the contribution and adding clarifying ablations. The practical value of the method justifies acceptance.

**Originality:** Good — the gradient reuse idea for guidance, combined with the early-heavy scheduling analysis, is novel.

**Importance:** High — reducing the computational cost of guidance is practically relevant as diffusion models are widely deployed.

**Claims support:** Weakened by the model-fitting confound, but the core method claims are well-supported.

**Soundness:** Good empirical methodology across multiple architectures and datasets. Missing some details (guidance scales, one ablation) but not fatally.

**Clarity:** Adequate but would benefit from pseudocode and sharper framing.

**Value:** Genuine practical utility for researchers and practitioners using guided diffusion.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>