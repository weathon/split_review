- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes Feature-Level Instance Attribution (FLIA), a method that extends instance-level training data influence analysis (TDIA) by attributing influence to individual features (pixels, tokens) within a training sample. The approach perturbs a training sample along the sign of the gradient of its IL (TracIn) score, then uses a first-order Taylor expansion to decompose the resulting IL change into per-feature attributions. The paper validates the approach through three experiments: showing IL can be manipulated while preserving confidence, correlating IL changes with actual influence via unlearning, and using insertion/deletion analysis on the attribution maps.

## Strengths

1. **Novel problem formulation.** The paper correctly identifies a genuine gap in TDIA: existing methods can only tell *which* training samples matter, not *why* (which features drive their influence). This reframing of the problem is valuable and could stimulate follow-up work. The backdoor detection example (Figure 2) effectively motivates why feature-level TDIA is needed.

2. **Interesting method design.** Using small perturbations to training samples to probe the IL function, and then deriving feature attributions from the resulting changes via Taylor expansion (Equations 4–7), is a clever and technically sound idea. The derivation shows that the sum of feature attributions equals the total change in IL, which provides an internal consistency check.

3. **Empirical evidence that IL values are manipulable.** Table 1 convincingly shows that IL values can be substantially changed (e.g., >110× increase on CIFAR-100 with DenseNet-121) via perturbations smaller than one pixel value, while model confidence remains nearly unchanged. This is a necessary precondition for the method and is well-demonstrated.

4. **Unlearning-based validation of IL changes.** Experiment B (Table 2, Figures 3a–3d) provides evidence that changes in IL values are positively correlated with actual changes in training influence measured via unlearning (CDCI values > 0 across all settings). This supports the claim that manipulating IL has meaningful downstream effects.

## Weaknesses

### Fatal

None.

### Major

1. **No baseline comparisons.** The experiments include zero comparisons to any alternative attribution method. Simple baselines such as (a) the vanilla gradient of IL w.r.t. the input, (b) Integrated Gradients applied to IL, or (c) random attribution, would provide minimal sanity checks and are standard practice in the attribution literature. Without them, it is impossible to assess whether FLIA offers any advantage over straightforward alternatives. This is the most critical weakness: the INS/DEL values in Table 3 are uninterpretable without knowing what random or gradient-based ordering would yield.

2. **The evaluation does not directly validate that the feature-level attributions are correct.** Experiments A and B validate properties of the *instance-level* IL score (that it can be manipulated, and that changes correlate with influence). These are necessary preconditions for FLIA, but they do not test whether FLIA's *feature-level attributions* are accurate or meaningful. The only experiment that uses the attribution maps (Experiment C, INS/DEL) is also the least probative because:
   - The insertion/deletion uses the adversarial (perturbed) image as the replacement source — the same type of perturbation used to compute FLIA. This creates a self-referential evaluation: the test checks whether the adversarial image, when introduced according to FLIA's ranking, changes IL. Without a random ordering or gradient-based baseline, it is unclear whether FLIA's ranking is meaningful.
   - The target of INS/DEL is IL rather than model prediction. The paper's interpretation of INS/DEL values in terms of "core features occupying a smaller proportion during training" (line 185) is non-standard and unvalidated.

3. **Combined effect of the above.** The paper claims to provide "fine-grained TDIA" and "identify crucial feature locations in training data," but the evidence does not establish that the per-feature attributions are correct, reliable, or superior to alternatives. The main contribution — feature-level attribution — is asserted rather than demonstrated.

### Minor

1. **Overstated theoretical claim.** The paper states that "the above derivation process proves that any change in $x_{tr}$ leading to a change in the IL value will inevitably be captured by the FLIA algorithm" (line 118). However, the derivation (Equation 4) uses a first-order Taylor expansion that explicitly includes a higher-order term $\mathcal{O}$, which is then dropped in the final formula (Equation 6). The Taylor approximation is only exact for infinitesimal perturbations, but the method uses sign-based perturbations with a fixed step size (1/2550 per pixel, 10 steps). The claim of "inevitably captured" is too strong; the method is better characterized as a well-motivated heuristic backed by a first-order approximation. The paper should clearly state the approximation and qualify the claim.

2. **CDCI metric ambiguity.** The CDCI is defined as "the covariance … between the attack steps and the confidence difference" (line 158), but the reported values (e.g., 0.8566 in Table 2) and the interpretive threshold ("a value greater than 0.5 indicates a strong correlation") are characteristic of correlation coefficients, not raw covariances. Covariance has no fixed upper bound and its scale depends on the units of the variables. The paper does not provide an explicit formula for CDCI, making it difficult to precisely interpret or reproduce the results.

3. **Dataset count inconsistencies.** The paper states for CIFAR-10: "Randomly selected 100 images per class from the training set and 10 images per class from the test set, totaling 10,000 samples" (line 134). CIFAR-10 has 10 classes, giving 1,100 total — an order of magnitude off. Similar mismatches exist for CIFAR-100, GTSRB, and SVHN. This raises concerns about the reliability of the experimental pipeline.

4. **No error bars or variance reporting.** All results in Tables 1–3 are single numbers with no standard deviations, confidence intervals, or multiple-seed results. Given the random subsampling, this makes it impossible to assess the stability of the findings.

### Trivial

None.

## Nice-to-Haves

- The NLP example (Figure 6) is presented as a qualitative demonstration, but the paper does not specify which model architecture or IL variant was used for the NLP task. Adding this detail would improve reproducibility.
- The paper does not discuss computational cost or compare the overhead of FLIA's iterative perturbation to a single gradient computation. This would help readers assess practical utility.
- The INS/DEL evaluation could be strengthened by also measuring against model confidence or accuracy (the standard in the attribution literature) rather than IL alone.
- A synthetic experiment with ground-truth feature importance (e.g., linear model with known coefficients, or backdoor triggers at known locations) would provide a clean validation of the attributions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The method's relationship to existing gradient-based feature attribution is not discussed"**: The paper discusses feature attribution methods in Section 2.4 and notes that existing methods focus on model predictions for test samples, not training data influence. This is a domain-difference rationale, not an omission. The critic's framing assumes FLIA is "essentially an accumulated gradient" — this is an interpretation, not a missing citation topic.
- **"No code or reproducibility details beyond a footnote"**: The paper provides an anonymous code link. The hard rules forbid questioning the existence or availability of cited resources.
- **"The insertion/deletion evaluation would be more convincing if it used model confidence"**: This is a suggestion for improvement, not a weakness of the existing evaluation. Moved to Nice-to-Haves.
- **Strength Finder claim that the derivation is "rigorous" and proves "no higher-order terms are omitted"**: This is incorrect — the derivation starts with $\mathcal{O}$ (Equation 4) and drops it in the final sum (Equation 6). The paper's own claim is stronger than the derivation supports, but the strength finder's characterization is also wrong. Removed because it conflicts with a verified weakness.
- **Strength Finder claim about "completeness guarantee"**: Same issue as above. Not retained.
- **"The backdoor experiment could be extended to multiple trigger types"**: This is a scope-expansion suggestion. Not a weakness of the paper as submitted.

## Novel Insights

None beyond the paper's own contributions. The reviews do not reveal a perspective on the work that the authors themselves did not articulate.

## Suggestions

1. **Add baseline comparisons.** The single most impactful improvement would be to compare FLIA against (a) vanilla gradient of IL w.r.t. the input, (b) Integrated Gradients applied to IL (with a zero baseline), and (c) random feature ordering, using standard INS/DEL metrics on both IL and model prediction. This would immediately clarify whether FLIA adds value.

2. **Clarify the theoretical claim.** State explicitly that FLIA provides an *approximate* first-order decomposition, and justify why the sign-based perturbation with small step sizes makes higher-order terms negligible in practice.

3. **Fix the dataset count errors and provide error bars.** The inconsistencies in Section 4.1 need correction. Report means and standard deviations across at least 3 random seeds.

4. **Define the CDCI formula explicitly.** Provide a mathematical equation for CDCI and clarify whether it is a covariance or correlation.

5. **Add a synthetic ground-truth experiment.** Use a setting where the influential features are known a priori (e.g., a linear model with sparse coefficients, or backdoor triggers at known pixel locations) and measure whether FLIA recovers them better than baselines.
