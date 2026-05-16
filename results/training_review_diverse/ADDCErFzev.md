Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper uses controlled variation of dropout probability (p=0 to 0.9) in AlexNet to operationalize a sparse-to-distributed coding continuum, and asks where the human visual system falls along this continuum. The authors report three convergent findings: (1) lesion robustness peaks at p=0.7 (non-monotonically), (2) representational similarity with human OTC (7T fMRI, NSD) also peaks at p=0.7, and (3) the eigenspectrum decay rate (α) of the p=0.7 model closely matches that of human OTC (~1.13). The central claim is that this reveals an optimal balance between efficiency (high-dimensional/sparse) and robustness (low-dimensional/distributed) in biological and artificial vision.

## Strengths

- **Systematic dimensionality control via dropout.** The paper convincingly shows that varying dropout proportion p produces monotonic changes in the eigenspectrum decay rate α of fc6 activations (Figure 1D, Section 2.1). This provides a clean, controlled empirical framework to manipulate representational dimensionality while holding other architectural factors constant.

- **Non-monotonic lesion robustness with a genuine sweet spot.** Lesioning experiments reveal that robustness to unit removal increases with dropout up to p=0.7 and then declines, with p=0.8 and p=0.9 models performing worse under severe lesions (Figure 2C–D, Section 2.3). This non-monotonicity is the paper's most interesting finding — it rules out a trivial "more dropout = more robustness" story and suggests genuine structural differences between models.

- **Convergent evidence across three independent measurements.** The fact that the same dropout level (p=0.7) emerges as optimal across lesion robustness, brain alignment (classical RSA), and spectral decay matching is a genuinely novel cross-level finding. The convergence of behavioral (lesion), representational (RSA), and spectral analyses on the same model is compelling and unlikely to be coincidental.

- **Extension to human high-level visual cortex.** While prior work (Stringer et al., 2019) was limited to mouse V1, this paper studies human OTC — a higher-order visual region — and uses high-resolution 7T fMRI data from the Natural Scenes Dataset.

## Weaknesses

### Fatal
None.

### Major

1. **The RSA brain alignment result lacks inferential statistics.** Figure 3C reports model–brain correlations across 8 subjects, and the paper claims the p=0.7 model shows "the highest degree of alignment." However, no statistical tests are provided (e.g., paired t-tests, confidence intervals, or Bayesian comparisons between dropout conditions). With only 8 subjects, the differences between p=0.7 and adjacent levels (p=0.6, p=0.8) could be driven by noise. This is the paper's central empirical finding, and the lack of uncertainty quantification is a significant gap that weakens the strength of the claim.

2. **The "optimal balance" narrative is overclaimed relative to the evidence.** The paper frames a trade-off between efficient high-dimensional (sparse) codes and robust low-dimensional (distributed) codes, then claims the p=0.7 model represents an "optimal balance" point. However, the p=0.7 model is the most low-dimensional (steepest spectral decay) among the models, placing it firmly on the distributed/robust side of the continuum. The paper does not measure "efficiency" independently — it is equated with dimensionality. The data are equally consistent with the brain simply favoring low-dimensional, robust codes. The non-monotonic lesioning result does show a sweet spot within the distributed regime, which is interesting, but the framing of a *balance between efficiency and robustness* goes beyond what the measurements support. The language in the title, abstract, and conclusion should be scaled back to match the evidence.

### Minor

1. **The lesioning evaluation is partially circular with respect to the training intervention.** Models are trained with dropout and then tested for robustness by applying the identical operation (randomly setting units to zero) at inference. Models trained with dropout are specifically adapted to that exact perturbation. The paper acknowledges this (Section 2.3: "Note that dropout regularization occurs during training but not during inference. In this analysis, we are effectively applying dropout during inference time") but does not address it as a limitation. **However**, the finding is not fully explained by circularity: if training on dropout directly caused inference-time robustness in a simple way, p=0.9 would be most robust, yet robustness declines after p=0.7. This non-monotonicity shows the result is not merely a self-fulfilling prophecy. Still, testing at least one alternative perturbation (e.g., additive Gaussian noise, weight scaling) would substantially strengthen the claim of general robustness.

2. **The spectral decay comparison between model and brain uses incompatible estimation procedures.** Model eigenspectra are computed from noiseless activations using standard PCA (Section 2.1), while brain eigenspectra are estimated using the GSN denoising method (Section 2.5.1), which explicitly subtracts noise covariance. The two estimates are on different footings. The GSN method is described as "to be fully described and validated in a forthcoming manuscript" (line 138) — no validation against alternative approaches (e.g., cvPCA from Stringer et al.) is provided here. Additionally, the model has 4,096 units while OTC has ~34k voxels; fitting power laws over the first 250 components in both cases is sensitive to truncation choice. The match in α could be coincidental.

3. **Dropout manipulation conflates multiple effects.** Varying p changes not just dimensionality but also feature norms, effective learning rate, training stochasticity, and potentially feature diversity. The paper attributes downstream effects to the dimensionality continuum, but no ablation isolates dimensionality from these confounds. The authors acknowledge this in the Limitations section ("it is possible that the percentage of dropout may reflect a pressure to be more-or-less distributed... Alternative regularization techniques such as L1 and L2 penalties could also be explored"), but the paper's central narrative relies on a cleaner mapping than the experiment delivers.

4. **Single architecture and limited layer analysis.** Only AlexNet (2012 architecture) is tested, with dropout applied to fc6/fc7. The main analyses focus on fc6; results for other layers (fc7, convolutional layers) are deferred to supplementary material. Testing at least one additional architecture would show the findings are not a quirk of AlexNet's fully connected layers.

5. **No variance estimates for model eigenspectra.** Models were trained with a single random seed each, so there is no distribution of α values from the model side to compare against the human distribution (mean α=1.13, sd=0.05 across 8 subjects). Multiple training seeds would enable proper statistical comparison.

### Trivial

None.

## Nice-to-Haves

- Testing alternative regularization methods (L1, L2 weight decay, input noise) to disentangle effects specific to dropout from more general regularization phenomena.
- Adding a second perturbation type to the lesioning analysis (e.g., additive Gaussian noise, targeted unit removal based on importance) to test whether the robustness advantage generalizes beyond the training intervention.
- Comparing GSN estimates to cvPCA (Stringer et al., 2019) on the same data as a validation check.
- Including results for additional model architectures (e.g., ResNet, ViT) and additional layers (conv5, fc7) in the main text.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about truncated sentence referencing an appendix ("A.2)").** Per hard rules: the parser strips appendix content from all papers; this exists in the original submission and is not a paper error.
- **Complaint that fc7 lesioning results are only in supplementary.** Per hard rules about appendix references.
- **Claim that the paper "does not engage with the fact that Stringer et al. used cvPCA while here GSN is used."** The paper explicitly compares GSN to cvPCA conceptually (Section 2.5.1). The valid residual concern is about *empirical validation*, not lack of engagement — moved to Minor #2.
- **Criticism about the weighted least squares (w_i = 1/i) departing from Stringer et al. without justification.** The paper provides a clear rationale for this weighting ("to emphasize the importance of the leading principal components"). This is a defensible methodological choice, not a flaw.
- **Criticism about the representational trajectory analysis being purely descriptive.** While this analysis is indeed descriptive, it is presented as supporting visualization (Section 2.2.1), not as a core claim. The space it occupies is reasonable for a results section.

## Novel Insights

The most interesting insight emerging from this review is that the non-monotonic lesion robustness pattern (optimal at p=0.7, declining at p=0.8–0.9) is actually the paper's strongest result because it *cannot* be explained by the simple circularity concern. If the lesioning result were merely "training matches test," one would expect monotonic improvement with higher dropout. The fact that robustness declines after p=0.7 suggests that extreme dropout degrades representation quality in a way that even training-adapted representations cannot compensate for — this is a genuine finding about the limits of distributed coding. The convergence of this sweet spot with brain alignment and spectral matching is striking, but the paper would benefit from explicitly framing the non-monotonic lesion result as the independent discovery and the brain results as convergent validation, rather than treating all three as equal legs of the "optimal balance" claim.

## Suggestions

1. **Add inferential statistics to the RSA analysis.** Report paired t-tests (or Bayesian alternatives) comparing the p=0.7 condition to each other dropout level across the 8 subjects, with multiple comparison correction. Show individual subject trajectories with error bars.
2. **Reframe the central claim.** Replace "optimal balance between efficiency and robustness" with more measured language: e.g., "a sweet spot in the distributed coding regime that aligns with human visual cortex." The data show convergence around p=0.7, not a measured trade-off between independently quantified efficiency and robustness.
3. **Add at least one alternative perturbation to the lesioning analysis.** Even a simple additive Gaussian noise experiment would substantially increase confidence that the robustness finding is general.
4. **Report model variability.** If computational budget allows, train 3–5 seeds per dropout level to provide error bars on model eigenspectra α values. This would enable proper statistical comparison with the human α distribution.
5. **Validate GSN or compare to cvPCA** on the brain data to ground the spectral comparison more firmly.

## Score and Decision

**Originality:** 7/10 — The controlled dropout manipulation as a tool to study the coding continuum is clever, though the underlying question is well-established.

**Quality of evidence:** 5/10 — The convergent findings are compelling but the key RSA result lacks statistical support, and the lesioning analysis has a circularity concern.

**Claims supported by evidence:** 5/10 — The "optimal balance" framing overreaches; the evidence better supports a more modest claim about a distributed-coding sweet spot.

**Clarity:** 7/10 — Well-written and clearly structured.

**Value to community:** 7/10 — The approach of using controlled regularization as an empirical lever is a valuable methodology, and the convergent findings will stimulate further work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>