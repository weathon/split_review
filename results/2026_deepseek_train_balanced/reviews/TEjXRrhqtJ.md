Below is my final consolidated review.

---

## Summary

The paper proposes TIEM, a perturbation-based video explanation method with a dual-perturbation architecture: first compute frame-level Time Importance Scores (TIS) via temporal window masking, then use the TIS to constrain per-frame spatial extremal perturbation masks. This design explicitly separates temporal from spatial importance estimation to address "temporal concentration" and "temporal spillover" — failure modes identified in prior blending-based approaches like STEP.

## Strengths

1. **Novel dual-perturbation design.** TIEM's separation of temporal importance estimation (TIS via multi-window temporal perturbation) from spatial mask generation (TIS-aware extremal perturbation) is a genuine architectural departure from STEP and EP-3D. The TIS calculation with total-variation-based window filtering (Eq. 2–4) adaptively selects relevant temporal scales, which is non-obvious and not present in prior perturbation-based video methods.

2. **Strong white-box validation.** The synthetic regressor experiment (Section 4.1, Table 2, Fig. 5) is clean: ground truth is known, the gentle/dynamic contrast is informative, and TIEM achieves ~100% pointing game accuracy on the dynamic regressor versus STEP's ~65% and EP-3D's ~91%. The visualizations (Fig. 5) confirm that TIEM eliminates both temporal concentration and spillover in this controlled setting.

3. **Clear problematization of specific failure modes.** Temporal concentration and temporal spillover are crisply defined, visually demonstrated (Fig. 2), and tracked through both experiments. This makes the paper's contribution directly testable.

4. **Honest limitations discussion.** Section 4.3 acknowledges concrete shortcomings (TIS averaging may overestimate insignificant frames in long windows; spatial discontinuity across frames), which strengthens credibility.

## Weaknesses

### Fatal
None.

### Major

1. **Black-box evaluation rests on only two videos (n=2).** The quantitative real-world evidence (Table 3) reports temporal pointing game scores for exactly two customized videos from UCF101-24 (front crawl, breaststroke). The reported standard deviations reflect multiple runs on these same two videos, not variation across a diverse video sample. With n=2, there is no basis for generalizing to the claimed breadth ("real-world applications where an action is presented ephemerally"). The paper does not sample across action classes, temporal dynamics, or difficulty levels. The central claim about real-world effectiveness is substantially undersupported by the evidence presented.

2. **Temporal pointing game measures alignment with human-labeled "signature frames," not model faithfulness.** The metric (Eq. 8) computes the fraction of unmasked pixels in manually designated signature frames — frames the *authors* believe contain distinctive movements. This evaluates agreement with human intuition about temporal salience, not whether the explanation identifies what the *model* actually uses for its prediction. The paper is transparent about the metric's design (Section 4.2: "since the ground truth of the visual explanation in real-world videos is unclear"), but the broader claim that TIEM "outperforms the existing methods in terms of interpreting the black-box model" conflates human-interpretable temporal focus with model-grounded explanation faithfulness. A faithfulness metric adapted for video (e.g., temporal deletion/insertion: progressively remove top-TIS frames and measure prediction drop) would directly address this gap.

3. **No ablation analysis.** The paper attributes TIEM's improvement to the dual-perturbation architecture but provides no ablation isolating each component. Critical comparisons are missing: TIEM without TIS (uniform budget allocation), TIEM without TV-based window filtering (using all window sizes), or TIEM without the per-frame area constraint. The white-box setting is ideal for such ablations, and their absence means the source of improvement is asserted rather than demonstrated.

### Minor

1. **Hyperparameter values and sensitivity are undisclosed.** The method has at least three hyperparameters (α in Eq. 3 for window filtering, λ in Eq. 7 for regularization, and the area constraint a). Only a (set to 10%) is mentioned in experiments. No sensitivity analysis for α or λ is provided, making it unclear how brittle the method is to these choices.

2. **No runtime or complexity comparison.** TIEM requires forward passes for all windows of all valid sizes (potentially O(T²) in the worst case). The computational cost is not reported or compared against baselines, which limits assessment of practical deployability.

3. **The claim "outperforms the state-of-the-art video interpretation method" (introduction) is overbroad relative to the experiments.** The experiments compare against only two perturbation-based baselines (EP-3D and STEP). While the paper scopes to "model-agnostic perturbation-based methods" in the experimental section, the introduction's unqualified SOTA claim creates a mismatch. Adding a simple per-frame adaptation of an image XAI method (e.g., Grad-CAM aggregated per frame) would help establish whether the complex dual-perturbation machinery is justified relative to simpler alternatives.

### Trivial

1. Equation 1 uses p^{w,t'} on both sides of the definition, creating a self-referential notation. The intended algorithm (compute raw drops, then normalize) is clear, but the notation is sloppy.

## Nice-to-Haves

- Extending the black-box evaluation to a broader, representative sample of videos (≥20 videos) from UCF101-24 with diverse temporal dynamics.
- Adding video-adapted faithfulness metrics (deletion/insertion curves) to complement the temporal pointing game.
- Hyperparameter sensitivity analysis for α and λ.

## Removed Points

These points were flagged by the reviewers but are removed or downgraded from the main review with justification:

- **Critic's claim that the method has a "circularity" rendering the spatial phase meaningless:** The sequential dependency (TIS → spatial budget) is by design and acknowledged in Section 4.3. The white-box validation shows the approach works when TIS estimation is correct. This is an inherent property of the approach, not an undetected flaw — it is correctly scoped as a limitation the authors already identify. Demoted to Minor framing above.
- **Critic's demand to compare against gradient-based video XAI methods (Saliency Tube, cEB-R, SWAG-V, etc.):** These are in a different family (gradient-based, model-specific) from TIEM (perturbation-based, model-agnostic). The paper's comparison against EP-3D and STEP is appropriate for its stated scope. The suggestion of per-frame image XAI baselines is retained as Minor weakness 3.
- **Critic's assertion that the paper frames STEP's limitations as universal to all blending-based approaches:** The paper reasonably discusses the blending-based approach used by STEP within scope. This is a valid characterization, not a weakness.
- **Strength Finder's "dramatic and statistically robust gains on real-world video":** "Statistically robust" implies generality that the n=2 evaluation does not support. Removed as overclaimed.
- Various formatting/style nitpicks and missing-appendix complaints: removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Broaden the black-box evaluation substantially.** Run on a representative sample (≥20 videos) from UCF101-24 spanning different action types (short-duration events, continuous actions, fast/slow motions). Report distributional results (mean and variance across videos, not just across runs on the same two videos).

2. **Replace or supplement the temporal pointing game with a faithfulness metric.** Adapt deletion/insertion (Petsiuk et al., 2018) to video: progressively remove or preserve the top-TIS frames (or top-ranked spatial regions within frames) and measure how the model's prediction changes. This directly tests whether the explanation captures model-important content.

3. **Add ablations in the white-box setting.** Compare TIEM against variants with: (a) uniform TIS (all frames equal), (b) no TV-based window filtering (all window sizes used), and (c) global rather than per-frame area constraint. This would isolate the contribution of each component.

4. **Report hyperparameter values (α, λ) and include a brief sensitivity analysis** for at least one of them, showing how the temporal pointing game score varies with the hyperparameter choice.

5. **Add a simple per-frame baseline** such as Grad-CAM applied independently to each frame and then aggregated, to test whether the complexity of dual perturbation is justified relative to straightforward alternatives.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>