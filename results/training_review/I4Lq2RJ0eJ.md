Here is my consolidated meta-review.

---

## Summary

This paper identifies that existing unlearnable examples (UEs) — designed primarily for single-task classification — fail to prevent learning in multi-task scenarios, motivating a re-evaluation of what constitutes "true unlearnability." The authors propose Sharpness-Aware Learnability (SAL), a per-layer metric based on loss landscape flatness, and Unlearnable Distance (UD), which compares the proportion of "learnable" parameters (those with high SAL) between clean and poisoned models. They benchmark seven UE methods across three datasets, three defenses, and five architectures, offering UD as a more intrinsic alternative to test-accuracy-based evaluation.

## Strengths

- **Novel problem framing and timely observation**: The paper is the first to systematically evaluate whether existing UEs remain effective under multi-task training. The finding that EM, OPS, and AR perturbations fail to degrade performance on Taskonomy tasks (segmentation, depth estimation) is a genuine empirical discovery that exposes an important gap in the UE literature, which has overwhelmingly focused on single-task classification. This observation alone motivates a useful research direction.

- **Loss-landscape-based explanation and new metric (SAL)**: Shifting evaluation from post-hoc test accuracy to training-phase parameter behavior is a principled and underexplored direction. The intuition linking loss landscape flatness to unlearnability — that UEs cause parameters to reside in flat regions where gradient updates produce minimal loss reduction — is conceptually appealing. The SAL metric operationalizes this intuition, and the paper demonstrates that SAL distinguishes true UEs (EM, OPS, AR: low SAL) from adversarial attacks (TAP: high SAL), which standard test accuracy cannot do.

- **Comprehensive UD benchmark across methods, datasets, defenses, and architectures**: Tables 1–3 provide the first comparative resource evaluating UEs via a beyond-accuracy lens. Testing across CIFAR-10/100, ImageNet-100, three defenses, and five architectures (including ViT) yields practically informative results — e.g., that ViT exhibits higher UD than CNNs, suggesting that stronger models are harder to render unlearnable. The finding that JPEG compression increases UD most effectively is directly actionable.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative validation that UD correlates with actual task performance.** The paper repeatedly claims that UD is "consistent with test accuracy" (Sec. 3.3, Sec. 5.1) but never reports the test accuracy of the same models side-by-side with their UD values. A reader examining Table 1 cannot determine whether the method with the lowest UD (e.g., EM at 0.139 on CIFAR-10) actually produced the worst model accuracy, or how much information UD adds beyond the existing test-accuracy gap. Without a direct correlation analysis (e.g., Spearman rank correlation between UD and test accuracy across methods), the central claim that UD is a "more intrinsic tool" for evaluating UEs remains unvalidated. The defense experiments (Table 2) suffer the same gap: UD changes are reported, but the corresponding clean-data accuracy after defense is not shown, so the reader cannot assess whether increased UD actually corresponds to recovered model performance.

2. **Multi-task failure claim rests on a single narrow experiment.** The paper asserts that "existing UEs fail in multi-task model training" (Fig. 1) based on evaluating only 3–4 UE methods (EM, OPS, AR) on a single multi-task dataset (Taskonomy tiny split) with a single backbone (ResNet). No random noise baseline is shown, despite the caption claiming UEs perform "even close to random noise." No statistical significance is reported, and the y-axis metric names/units appear absent from the figure. While the paper does not overclaim this as exhaustive, the evidence is too thin to support the broad implication that "existing UEs are not truly unlearnable." A stronger claim would require testing UE methods specifically adapted for multi-task objectives and comparing against a random perturbation baseline.

### Minor

1. **Ambiguous link between per-layer SAL and per-parameter classification.** Definition 1 defines SAL as a scalar computed over an entire layer's parameters (θ_l), yet UD (Definition 3) and its constituent λ(·) are described as counting "learnable parameters" (plural). The paper never explicitly states whether a layer is classified as a whole (all its parameters counted as learnable if SAL_layer > β) or whether SAL is computed per-parameter. The pipeline is reconstructible (compute SAL per layer → β from K-Means on per-layer SAL values → classify layers → sum parameters in learnable layers), but the text uses language suggesting parameter-level granularity while the definitions operate at the layer level. This imprecision makes the metric harder to reproduce. The provided code release partially mitigates this, but the paper itself should clarify.

2. **SAL hyperparameters are unvalidated.** The inner maximization used to compute SAL uses the ℓ₂ norm with ε=0.05 and only 10 optimization steps. No ablation shows how UD changes with ε, step count, or norm choice. Without this, it is unclear whether UD is robust or an artifact of these specific settings.

3. **K-Means threshold (β) may be unstable.** The learnable threshold uses K-Means with k=2 on SAL values across all layers and epochs, without any mention of multiple restarts, initialization strategy, or stability checks. K-Means on high-variance SAL distributions could produce different thresholds across runs, affecting UD values.

4. **Toy-model experiments are suggestive but not probative.** The loss landscape analysis in Sec. 3.1 uses a 120-parameter linear classifier. The paper acknowledges this limitation but then concludes that "only a few key parameters … undergo normal learning" in DNNs broadly. This speculation is reasonable but unsupported — no analysis on an actual deep network (e.g., via per-layer SAL tracking from Sec. 3.3) is connected back to verify the toy-model conclusions.

5. **Incomplete benchmark entries.** Table 1 marks several entries as "pending (p)." While the authors note experiments are ongoing, the benchmark as presented is incomplete, which weakens the comprehensiveness claimed as a contribution.

### Trivial

- No y-axis labels are visible in Figure 1's description, making the quantitative comparison uninterpretable at a glance.
- Algorithm 1's notation (lines 3, 11) writes θ(t+1) ← θ(t) without showing the gradient update, which is fine as pseudocode but could confuse readers unfamiliar with the convention.

## Nice-to-Haves

- For the multi-task experiment, include a random-perturbation baseline (uniform noise at the same ℓ∞ budget) to calibrate what "close to random noise" means.
- Validate UD against simpler baselines (e.g., linear separability score from Yu et al. 2022, or test-accuracy gap directly) to demonstrate that UD provides information not already available from cheaper metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SAL definition ambiguity undermines the entire UD metric and makes it ill-posed"** — The paper's pipeline (per-layer SAL → threshold on layers → count parameters in learnable layers) is logically well-defined even if the presentation could be clearer. The reviewer's characterization of the metric as "ill-posed" and "cannot be interpreted" is an overstatement. Moved to Minor (#1 above).
- **"TAP inclusion without clear disclaimer undermines the analysis"** — The paper explicitly states multiple times that TAP is an adversarial example, not a true UE (lines 82, 98, 129, 133, 236, 242). This criticism is factually incorrect.
- **"Algorithm 1 notation is incomplete"** — The pseudocode uses standard conventions; the training update is implicit. This is a nitpick.
- **"Cosine similarity plots not explained clearly"** — The paper provides explanation (lines 106–109, Fig. 5 caption). The explanation is present even if not exhaustive.
- **"UD 1.639 for TAP on ViT conflates adversarial examples with UEs"** — The paper explicitly discusses this as an expected difference (line 248).

## Novel Insights

The reviewers collectively surface a substantive tension: the paper makes a strong case that existing UEs fail in multi-task settings and proposes an elegant loss-landscape-based metric, but the empirical validation of UD as a *replacement* for task-specific evaluation is missing a critical link — direct correlation with task performance. This gap is not fatal (the paper's contribution is metric proposal, not metric certification), but it means the paper is best read as a proof-of-concept for a new evaluation paradigm rather than as a fully validated tool. The most interesting observation to emerge across reviews is that UD reveals TAP (adversarial examples) as categorically different from true UEs — something test accuracy alone cannot distinguish — and that ViT's higher UD suggests model capacity is a confound in evaluating unlearnability that the community has not previously considered.

## Suggestions

1. Add a direct quantitative comparison: for every entry in Tables 1–3, report the test accuracy (or task metric) alongside UD, and compute a rank correlation (Spearman) to ground the claimed "consistency."
2. Clarify the SAL-to-parameter-count pipeline in Definition 2/3: state explicitly whether classification is per-layer or per-parameter, and provide the exact formula for λ(·).
3. Add an ablation of SAL's inner-maximization hyperparameters (ε, step count, norm) on a subset of Table 1 to demonstrate robustness.
4. Add a random-noise baseline to Figure 1 and label axes with both metric name and unit to make the results interpretable.
5. Run the multi-task experiment with at least one additional backbone (e.g., ViT) and one additional multi-task dataset to broaden the evidence base.

## Score and Decision

The paper tackles a genuine and timely problem, proposes a conceptually interesting metric (SAL/UD), and provides a useful comparative benchmark. However, the core contribution — UD as a reliable evaluation tool — is under-validated: the paper does not quantitatively demonstrate that UD correlates with task accuracy, which is the most direct way to argue for its utility. Additionally, the headline multi-task failure observation rests on limited experimental support. These weaknesses are addressable but present in the current submission. The paper makes a meaningful contribution to the conversation around UE evaluation, and the core ideas have merit.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>