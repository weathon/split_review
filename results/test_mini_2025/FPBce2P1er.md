Now I have enough information to synthesize the review. Let me write it.

## Summary

This paper presents a theory of compositional generalization in kernel models with compositionally structured representations. The core theoretical result (Theorem 4.2) proves that such models are restricted to "conjunction-wise additive" computations — summing values assigned to each component or conjunction seen during training. This fundamentally limits what compositional tasks kernel models can learn (e.g., preventing transitive equivalence but permitting context dependence). The paper further identifies two failure modes — memorization leak and shortcut bias — that arise from training data statistics even for tasks that are in principle learnable. Finally, it provides empirical evidence that deep networks (ConvNets, ResNets, ViTs) exhibit qualitatively similar behavior on corresponding image-based tasks.

## Strengths

1. **Theorem 4.2 (conjunction-wise additivity)** — This is the paper's central theoretical contribution: a precise, formal characterization showing that any kernel model with a compositionally structured representation is constrained to sum over conjunctions seen during training. This goes beyond prior analyses of specific tasks (Abbe et al., 2023; Lippel et al., 2024) and covers all tasks with discrete categorical components. The proof is cited to the appendix and the reasoning in the main text is clear.

2. **Proposition 5.1 (exact analytic formula for memorization leak)** — The paper derives a closed-form expression for the distortion factor *m* in symbolic addition tasks, showing it depends only on representational salience *S*(1;2) and training set size *p*. This provides a concrete, mechanistically grounded prediction that separates generalization behavior from surface-level task details like interpolation vs. extrapolation.

3. **Representational salience metric (Section 5.1, Figure 3)** — The paper introduces *S*(*k*;*C*), a compact metric that reduces the full kernel to *C*−1 interpretable parameters, and shows how depth and nonlinearity systematically change these saliences in random-weight networks. This is a practical tool for predicting whether a representation supports compositional generalization.

4. **Two identified failure modes (memorization leak and shortcut bias)** — The paper isolates and formally characterizes two distinct mechanisms that prevent compositional generalization even on tasks that are, in principle, solvable by kernel models. This provides a concrete explanation for the conflicting prior results on whether disentangled representations are sufficient for compositional generalization.

5. **Empirical validation across multiple deep architectures (Section 6, Figure 5)** — The paper tests ConvNets, ResNets, and ViTs on MNIST/CIFAR versions of symbolic addition and context dependence. The qualitative alignment (compressed predictions on symbolic addition, chance-level accuracy on CD-3) across diverse architectures supports the relevance of the theory beyond simple kernel models. The use of real image data rather than synthetic one-hot inputs strengthens the demonstration.

## Weaknesses

### Fatal
None.

### Major
None. The theory is sound, the claims are properly scoped, and limitations are acknowledged. The weaknesses below are substantive but do not undermine the paper's core contributions.

### Minor

1. **The empirical validation tests directional trends, not the exact quantitative predictions of the theory.** Proposition 5.1 gives an exact formula for the memorization leak slope *m* = *p*·*S*(1;2) / (1 + (*p*−2)*S*(1;2)). The deep network experiments test whether the slope *increases* with larger training sets and higher *S*(1;2) (via distance), which is the correct directional prediction. However, the paper never measures *S*(1;2) in the deep networks for the experimental conditions of Figures 5c–d and compares the actual slope values to the formula. For the kernel model experiments (Figure 4b), the formula is validated directly. For the deep networks, the evidence remains correlational. The paper acknowledges this limitation in the Discussion ("do not provide any quantitative bounds"), but the abstract's claim that the theory is "empirically validated" in deep networks, combined with the Section 6 framing ("our experiments confirmed this prediction"), somewhat overstates the strength of the confirmation. The qualitative trends are real and worth reporting, but the gap between the theory's precision and the empirical test creates an asymmetry in the paper's narrative.

2. **The ViT results for distance vs. slope are weak, and the *p*=4 exception is noted but not explained.** In Figure 5c, the effect of distance on slope is much subtler for ViTs than for ConvNets, raising the question of whether the mechanism driving ViT behavior on symbolic addition aligns with the kernel theory or involves other factors. Similarly, the paper reports that for *p*=4, the extrapolation slope is smaller than the interpolation slope, contradicting the theory's prediction and the pattern for other values of *p*. The paper flags these discrepancies honestly but does not investigate them. While no theory is expected to explain every observation, these exceptions are the very places where understanding the limits of the theory would be most informative.

3. **The connection between kernel theory and deep network behavior is phenomenological rather than mechanistic.** The theory is developed for kernel models with fixed, compositionally structured representations trained via norm-minimizing linear readout (ridge regression / gradient descent with MSE). The deep networks (trained with backpropagation and cross-entropy) learn their own internal representations and operate far from the kernel regime. The paper shows that similar *output patterns* emerge, but does not establish that the same *computation* (conjunction-wise additivity arising from the combination of compositional structure and norm-minimization) is responsible. The paper invokes evidence from Appendix D.3 that a conjunction-wise additive model is predictive of network responses, but this result is relegated to the appendix and not quantified in the main text. The Discussion honestly acknowledges these limitations, and for a theoretical paper this is not a fatal gap, but the framing throughout the paper — the abstract's "empirically validate," the Section 6 title "Our theory can describe the behavior of deep networks," and the language of "confirmed" — implies a stronger connection than the phenomenological evidence supports.

### Trivial
None.

## Nice-to-Haves

- **Test the exact quantitative formula of Proposition 5.1 in at least one architecture.** Measuring *S*(1;2) in the deep networks for the conditions of Figures 5c–d and comparing the empirical slope to *m* = *p*·*S*(1;2) / (1 + (*p*−2)*S*(1;2)) would strengthen the claim that the theory is capturing the right functional form, not just the right sign. Even an imperfect fit would be informative.
  
- **Analyze representational salience in deep networks for context dependence.** The paper attributes the failure on CD-3 to specific patterns of *S*(1;3), *S*(2;3), *S*(3;3) (Figure 4c). Measuring these saliences in the deep networks' penultimate layer would connect the explanation directly to the observed accuracy pattern in Figure 5e.

- **Report effect sizes or confidence intervals for slope differences** in Figures 5c–d, to help readers assess the practical significance of the trends.

## Removed Points

- **"The empirical validation does not establish that deep networks implement the same mechanism"** — Partially demoted. The paper does test whether a conjunction-wise additive model predicts network responses (Appendix D.3). What remains as Weakness #3 is the narrower claim that the main text does not quantify this fit and the overall framing overstates the mechanism-level connection.

- **"Theory scope is narrower than framing suggests"** — Removed. The paper explicitly defines its scope (Definition 3.1, Section 4.3 end, Section 7) and provides evidence for broader applicability in the appendix. The framing is appropriate for a theoretical paper that is transparent about its assumptions.

- **"Proposition 5.1 makes an exact quantitative prediction never tested"** — Incorporated into Weakness #1 but softened. The paper does test directional predictions correctly; the issue is the gap between the theory's precision and the empirical test, not a failure to test.

- **"Missing related works"** — Removed per policy (no external sources to confirm).

- **"Missing appendix content / proofs in appendix"** — Removed per policy (parser strips appendix).

- **"Should test for conjunction-wise additivity directly"** — Removed per policy. The paper states this is done in Appendix D.3 and the parser strips appendix content.

- **"Weaknesses from Strength Finder about generic strengths"** — The Strength Finder's strengths are all specific and grounded in the paper's content, so none were removed.

- **"Formatting/style nitpicks"** — Removed per policy.

## Novel Insights

The two reviewers converge on the same core assessment — a strong theoretical contribution with empirical validation that is suggestive but falls short of matching the theory's precision — but they frame it differently. The harsh critic construes this as a structural gap that requires scaling back claims or adding evidence; the strength finder accepts the qualitative validation as meaningful. The novel insight from the synthesis is that *the paper's most impressive empirical result is also its most underexploited*: Figure 5a shows that *S*(1;2) in a ConvNet intermediate layer varies systematically with digit distance, establishing that the deep network's *representational geometry*, not just its output, tracks the theory's key parameter. The paper uses this only to motivate the distance manipulation in Figures 5c–d; it does not close the loop by checking whether the *quantitative relationship* between *S*(1;2) and the memorization leak slope in the deep network matches Proposition 5.1. This single measurement — already collected — could convert a qualitative trend into a quantitative test without any new architecture or dataset.

## Suggestions

1. In the main text, quantify how well a conjunction-wise additive model fits the deep network responses (currently only in Appendix D.3). This is the single most direct test of whether the mechanism transfers.

2. For the deep network experiments on symbolic addition, measure *S*(1;2) in the penultimate layer and compare the empirical slopes to the formula from Proposition 5.1. Even if the fit is imperfect, reporting the comparison (e.g., as a parity plot or R² value) would strengthen the claim substantially.

3. For context dependence in deep networks, measure *S*(1;3), *S*(2;3), *S*(3;3) in the penultimate layer to check whether the failure on CD-3 correlates with the salience pattern predicted by the kernel theory (Figure 4c).

4. Tone down the "confirmed" and "validated" language in the abstract and Section 6 to match the qualitative nature of the evidence. Phrasing like "our theory captures qualitative trends in deep networks" is more precise.

## Score and Decision

**Round-1 bracket**: The paper sits between the weak anchors (< 3.5: "Brain-inspired Geometry Constrain" avg 3.0, "Weak Correlations" avg 2.33, "How Neural Networks With Derivative Labels Work" avg 3.0) and the strong anchors (> 7.5: "Generalization error of spectral algorithms" avg 8.0, "Exploring Loss Landscape" avg 8.0). The initial bracket is 4.0 – 7.5. The paper is clearly above papers scoring 3–4 and below the exceptional oral-level papers at 8+.

**Round-2 narrowing**: Inside the 4.0–7.5 bracket, the most relevant anchors are:
- "Towards a formal theory of compositionality" (avg 6.75): a compositionality theory paper that proposed a formal metric but had fundamental identifiability issues. The current paper has a cleaner theoretical contribution and broader empirical validation.
- "Provable Compositional Generalization for Object-Centric Learning" (avg 7.33, oral): tighter theory-to-experiment link but narrower scope (2-object synthetic images only). The current paper has weaker quantitative theory-to-experiment alignment but broader scope.
- "GeoCon" (avg 6.33, withdrawn): a method paper with neuroscience motivation that had incremental novelty concerns. The current paper has stronger theoretical novelty.
- "Spectral Truncation Kernels" (avg 5.25): a kernel methods theory paper that was partly rejected for unclear implications. The current paper has clearer practical relevance.

The paper at 6.5 is comparable to "Towards a formal theory" (6.75) in overall quality but for different reasons — stronger theoretical rigor but weaker empirical precision. It is clearly better than "GeoCon" (6.33) and "Spectral Truncation Kernels" (5.25), and worse than the oral-level "Provable Compositional Generalization" (7.33), where the empirical results directly and quantitatively support the theoretical claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>