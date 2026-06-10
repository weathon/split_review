Here is the final consolidated review.

---

## Summary

This paper proposes a test-time refinement procedure that enforces explicit topological constraints—contact ratios and minimum distances—between parts of composite 3D objects represented as DeepSDF implicit functions. The core technical idea is a Monte Carlo approach that estimates constraint violations from uniformly sampled points, enabling differentiable losses that refine latent vectors toward constraint compliance. Experiments on heart (5-chamber) and spine (5-vertebra) reconstruction from nn-UNet segmentations are presented.

## Strengths

1. **Monte Carlo-based constraint estimation from implicit surfaces (Eq. 7, Sec. 3.2).** The paper derives a differentiable, sampling-based estimator of the contact ratio between two implicit surfaces. This is the key technical enabler—contact ratios involve global surface-area ratios that prior local-intersection-checking methods could not handle. The gradient flows through the loss to the latent vectors, enabling test-time refinement toward a target contact ratio.

2. **Demonstrated improvement on out-of-distribution data (Sec. 4, lines 199-200).** On OOD cardiac images, individual SDF fitting reduces Chamfer error "by a factor of more than 10" over nn-UNet alone but exhibits "severe topological errors." The proposed joint fitting with constraints further reduces Chamfer error and yields "only minimal topological mistakes." This is concrete evidence that the method delivers on its central claim in a practically relevant setting.

3. **Unified treatment of two distinct constraint types (Sec. 3).** Contact ratio (heart) and minimum distance (spine) constraints are handled through the same infrastructure of uniform sampling, topological point identification, and differentiable losses. The paper correctly notes these constraints pose different challenges that would require separate approaches in traditional frameworks.

4. **Explicit mesh-based baseline comparison (Sec. 4.1, lines 215-217).** The paper compares against a direct mesh-based refinement approach and shows it produces "rough surfaces" and higher reconstruction errors, providing evidence that the implicit approach is preferable to an obvious alternative.

## Weaknesses

### Fatal

None.

### Major

1. **Confounded evaluation: joint optimization vs. constraint enforcement (Sec. 4).** The main comparison is between (a) independent SDF fitting per part and (b) joint fitting WITH all constraint losses—two factors differ simultaneously. There is no control condition where SDFs are fitted jointly but WITHOUT any constraint losses. The ablation study (Tab. tab:ablation) removes individual loss components but does not include the condition where ALL constraint losses are removed while joint optimization is retained. Without this control, the reader cannot determine whether the reported topological improvements are driven by the constraint losses themselves or simply by the regularization effect of jointly optimizing latent vectors in a shared volume. This directly undermines the paper's central claim that the constraint enforcement mechanism is responsible for the improvement. This control experiment is straightforward to run and should be standard.

2. **Missing optimization details prevent reproducibility (Secs. 3.3, 3.4).** The λ hyperparameters in Eqs. (9) and (11) are described only as "controlling parameters" with no numerical values. No optimizer, learning rate, total iteration count, or convergence criterion is specified. The ε threshold for "contact distance" in Eq. (7) is also unspecified. Without these details, the method cannot be independently reproduced or applied by other researchers.

### Minor

1. **Tension between claimed a priori medical knowledge and data-derived constraint values (lines 22 vs. 192, 202).** The introduction (line 22) states that contact ratios and gaps are "known a priori from centuries of medical practice and do not need to be learned from data." However, for heart reconstruction, contact ratios are "pre-computed based on the training data" (line 192). For the spine, the enforced constraint is "1 pixel" (line 202), a dataset-resolution-specific value rather than an independently verified medical constant. The method itself does not depend on how the constraints are derived, but the framing over-promises relative to what is actually done.

2. **Small heart test sets without variance estimates (Sec. 4).** The heart evaluation uses 5 in-distribution and 10 out-of-distribution test images, with no standard deviations, confidence intervals, or per-instance results reported. With N=5, a single outlier can dominate aggregate metrics. The spine experiment (460 CTs, 46 test cases after the 10% split) is better-sized, partially mitigating the concern, but the heart evidence is quantitatively weak.

3. **Unfinished editorial artifacts (lines 26, 31, 33, 65, 70, 179, 199).** Multiple `\pf{}`, `\PF{}`, and `\hl{}` annotations remain in the text, including the author dialogue "@Pascal: When the data is not scarce, nn-Unet still works fine on training data and in-domain testing data." (line 33). While the technical content is unaffected, the submission is not in a publishable state.

### Trivial

None.

## Nice-to-Haves

- The claimed "30% computational overhead" (line 26, inside a `\pf{}` annotation) lacks context: 30% overhead relative to what? What is the total per-instance runtime in seconds/minutes?
- A systematic analysis of failure cases: line 200 mentions "instability when fitting SDFs on extremely noisy input shapes" without quantifying incidence or describing what the failures look like.

## Removed Points

The following points were removed or downgraded from the reviewer inputs with justification:

- **"Missing comparison to mesh-based constraint enforcement approaches"** (Harsh Critic): **Removed** — factually incorrect; the paper explicitly includes a mesh-based refinement baseline (lines 215-217) and shows it underperforms the proposed method.
- **"Self-Intersection Loss could be more carefully explained"** (Harsh Critic): **Removed** — an opinion about presentation quality, not a substantive weakness.
- **Severity of "small test sets" claim**: **Downgraded** from the reviewer's framing to Minor because the spine experiment is well-sized, and the heart results are supplemented with qualitative evidence.
- **Strength Finder generic strengths** (e.g., "addressing an important problem", "this paper targeted an interesting question"): **Removed** as superficial praise lacking specific evidence. Only concrete, evidence-backed strengths (Monte Carlo estimator, OOD improvement, unified framework, mesh baseline) are retained.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses sharpen existing observations but do not reveal unexpected connections.

## Suggestions

- Add the missing control experiment: joint SDF fitting with only L_data (no constraint losses) across all object parts. If this control already reduces topological errors compared to independent fitting, reframe the contribution around the joint optimization framework with constraint enforcement as an additional benefit. If it does not, the constraint losses are demonstrably responsible.
- Report all missing hyperparameter values (λs, optimizer, learning rate, total iterations, ε threshold).
- Add standard deviations or per-instance results to the heart evaluation (N=5 and N=10).
- Remove all editorial annotations (`\pf{}`, `\PF{}`, `\hl{}`, @Pascal commentary) before any resubmission.
- Either reframe constraints as data-derived statistics (with honest justification that they are stable across annotated instances) or cite independent medical sources for the specific numerical values used.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>