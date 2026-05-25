Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me compose the consolidated review.

## Summary

The paper proposes **ScaPre**, a closed-form framework for large-scale concept unlearning in text-to-image diffusion models. It introduces a conflict-aware stable design (spectral trace regularizer + Bures-distance geometry alignment) to stabilize multi-concept optimization, and an Informax Decoupler that uses mutual information to selectively weight parameter updates toward target concepts. The method is evaluated on object, style, and explicit content benchmarks, showing strong unlearning performance at scale (up to 50 concepts) compared to existing closed-form and training-based methods.

## Strengths

- **Demonstrated scalability without generative collapse.** The paper provides clear evidence that ScaPre can unlearn up to 50 diverse concepts while maintaining generative quality, whereas prior closed-form methods (UCE, RECE) suffer catastrophic quality degradation at this scale (Table 3: CLIPcoco ~29% vs ~21%, FID ~14 vs >49). Figure 4 further shows ScaPre maintaining stable UQ as the number of concepts grows, while baselines deteriorate.

- **Principled conflict-resolution design.** The spectral trace regularizer (Eq. 3–4) explicitly penalizes directions of high conflict via second-order statistics of concept embeddings, and the smooth gating on SVD singular values (the **R** matrix construction) provides a theoretically-motivated mechanism to suppress inter-concept interference. This goes beyond the standard Frobenius regularization used in prior closed-form work (UCE, RECE).

- **Strong evidence for precision on confusable concepts.** The ImageNet-Confuse5 benchmark (Table 4) is a well-designed test of fine-grained disentanglement: ScaPre achieves Overall Acc of 84.3% versus the best baseline (SP at 50.3%), demonstrating that the Informax Decoupler combined with the stable design genuinely helps confine unlearning to target concepts while preserving visually similar non-targets.

- **Validated generalization to artistic styles.** The style unlearning results (Table 2, 50 artists) show ScaPre achieves the best CLIPπ (3.44), confirming that the scalability and precision advantages extend beyond object categories.

## Weaknesses

### Fatal
None.

### Major

- **Internal contradiction in the efficiency claim.** The paper states in both the introduction bullet points and Section 5.5 that ScaPre "completes the unlearning of 50 concepts in only **120 seconds**" (2 minutes). However, Figure 3's own data table lists ScaPre's execution time as **~1.5 hours** (~5400 seconds), a 45× discrepancy. The same figure's caption claims ScaPre is "the most efficient method in both metrics," yet UCE (listed at ~0.5 hours) has strictly lower execution time. This is not a minor formatting issue — it is a factual inconsistency between a headline claim and the paper's own reported data. The reliability of all reported numbers is called into question until this is resolved. The authors must clarify what "120 seconds" refers to (e.g., only the closed-form solve vs. the full pipeline including forward passes) and reconcile the figure data with the text.

### Minor

- **Unclear/incorrect notation in the Informax Decoupler definition.** Section 4.2 defines the activation as `a_i(s) = W_{i,s}`, where `W_{i,s}` is described as "the activation of channel i on input feature s." As written, `W_{i,s}` is a static weight matrix element, not an input-dependent quantity, making the MI computation between this static value and the label conceptually incoherent. The intended meaning (likely the output of channel i for input feature s, e.g., the i-th element of W·x_s) is clear from context, but the notation needs correction for reproducibility.

- **No error bars or multiple-run statistics.** None of the main tables report standard deviations, confidence intervals, or results over multiple seeds. Given that unlearning metrics can be sensitive to randomness in generation and evaluation, the reported point estimates alone do not demonstrate that the observed improvements are systematic. Adding error bars (at least for key results like Tables 1, 3, and 4) would significantly strengthen the empirical claims.

- **The "×5 more concepts" claim lacks a precise threshold.** The abstract and introduction state ScaPre can "forget up to ×5 more concepts than the best baseline within the limits of acceptable generative quality," but "acceptable generative quality" is not formally defined. The claim is qualitatively plausible from Figure 4, but the paper should either define the threshold or soften the claim.

- **UQ metric is relative to the method set.** The unified metric UQ is defined using the mean and standard deviation of accuracy and CLIP score across the compared methods. This makes UQ a set-dependent measure — it could change if methods are added or removed. While still informative for the current comparison, this limitation should be explicitly noted.

- **Geometry alignment refinement deferred to appendix.** The proximal refinement (Bures geodesic + Procrustes) is a core algorithmic step, but its derivation is relegated entirely to Appendix B.2 (not available in the main text). While the two-step conceptual description is clear enough to understand the approach, the main paper would benefit from at least the final closed-form solution or update equation.

### Trivial

None.

## Nice-to-Haves

- An ablation study in the main text isolating the contribution of each component (spectral trace regularizer, geometry alignment, Informax Decoupler) on a key benchmark like ImageNet-Confuse5 would strengthen the attribution of improvements. (Currently, ablations are deferred to Appendix C.5–C.7.)
- A discussion of how the method's computational complexity scales with the number of concepts m (beyond the 50-concept demonstration) would help readers assess practical limits.
- Clarify whether "training-free" is the best descriptor, given that the method requires forward passes to compute S, R, and MI. "Gradient-free" or "closed-form" may be more precise.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unfair comparison on precise unlearning benchmark"** (Harsh Critic Point 5): The paper explicitly states all baselines are run using their official open-source implementations (Section 5.1). This is standard practice. The speculation that baselines might be suboptimally configured on this new benchmark is not supported by any evidence in the review and would apply equally to any paper introducing a new benchmark. **REMOVED** (speculative, not grounded in paper content).

- **"Incomplete specification of the geometry alignment refinement"** (partially): The main text provides a clear two-step conceptual description (Bures geodesic interpolation + orthogonal Procrustes). Deferring detailed derivations to an appendix is standard practice in ML papers. The harsh critic's framing of this as a critical issue is overstated; it is at most a minor presentation concern. **DEMOTED** to Minor above.

- **"Overall Acc metric conflates generation quality with precision"**: The metric's formulation (harmonic mean of (100−Unlearn) and Preserve) is clearly specified in Section 5.3. While preserve accuracy can be affected by generation quality, this is a known aspect of the evaluation, not a hidden flaw. ScaPre's advantage is large enough to be meaningful even under alternative interpretations. **REMOVED** (criticism does not identify a real flaw in the metric given the context).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the efficiency contradiction immediately.** This is the single most important fix. Either correct the text (if ~1.5 hours is the accurate time) or correct Figure 3 (if 120 seconds is accurate). If the two numbers refer to different stages of the pipeline, clarify this explicitly. The figure caption claiming ScaPre is "the most efficient method in both metrics" should also be reconciled with the data (UCE shows lower execution time).

2. **Fix the Informax Decoupler notation.** Replace the ambiguous `a_i(s) = W_{i,s}` with a proper input-dependent expression, e.g., `a_i(s) = (W·x_s)_i` or `a_i(s) = w_i^T x_s`, where x_s is the input feature vector at position s.

3. **Add error bars** to at least the key tables (Tables 1, 3, 4) by reporting results over 3 random seeds.

4. **Define the "acceptable generative quality" threshold** used for the ×5 claim, or soften the claim to a qualitative statement supported by Figure 4.

5. **Include a main-text ablation study** showing the contribution of each component on a single benchmark (e.g., ImageNet-Confuse5 or Imagenette).

## Score and Decision

The paper tackles an important and timely problem — large-scale concept unlearning — with a well-motivated, principled approach. The core empirical results (especially on ImageNet-Confuse5 and the 50-concept benchmarks) are strong and demonstrate genuine advances in both scalability and precision. However, the paper is significantly undermined by an internal contradiction between the text (120 seconds) and Figure 3 (~1.5 hours) regarding the efficiency claim — one of the paper's headline contributions. This inconsistency reduces confidence in the reported numbers and must be resolved. The remaining issues (notation clarity, statistical rigor) are addressable. The underlying technical contribution is solid, and the paper would be suitable for acceptance contingent on a satisfactory resolution of the efficiency discrepancy.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>