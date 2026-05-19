- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 1, 5
Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes Fixed Strength Optimization (FSO), a method that directly optimizes adversarial examples on the ε-sphere (fixed perturbation strength) rather than incrementally growing the perturbation via multi-step attacks. It also introduces the L₂₋∞ norm, a combined norm that constrains both L₂ and L∞ perturbation magnitudes. The paper claims FSO achieves 2–3× faster convergence and improved black-box transferability relative to multi-step PGD, and that the L₂₋∞ norm yields more imperceptible perturbations while maintaining transferability.

## Strengths

- **Empirically demonstrated faster convergence.** Section 5.2 and Figure 4 show that FSO converges to a plateau in ≤10 steps, while multi-step attacks (Figure 3) require >20 steps — a roughly 2–3× acceleration. This is a clean, verifiable result that holds regardless of other confounds.

- **Well-motivated problem framing.** The paper identifies a genuine limitation of multi-step attacks: perturbation strength grows slowly during iteration, and the same attack steps that increase strength may not optimize the perturbation direction well. Figure 1(a) empirically documents this, and the observation that transferability correlates with strength is correctly cited as motivation for fixed-strength optimization.

- **Novel combined norm with clear geometric interpretation.** The L₂₋∞ norm (Equation 3) is a principled interpolation between L₂ and L∞ constraints. The paper correctly identifies that L∞-FSO is impossible (zero tangential component) and provides a practical remedy. Figure 2(b) verifies that the proposed approximate projection converges to the target norm. The hyperparameter m smoothly interpolates between behavior dominated by L₂( m = √d ) and L∞ (m = 1).

- **Large-scale evaluation across multiple models.** Table 1 spans six source models and seven target models, demonstrating systematic coverage.

## Weaknesses

### Fatal
None.

### Major

- **Confounded primary comparison between FSO and multi-step PGD.** The paper's headline transferability comparison (Table 1) is performed after 30 iterations. The authors explicitly acknowledge (line 152) that multi-step PGD "after 30 steps, the attack strength is still smaller than the control value." This means the comparison is not FSO at strength ε vs. multi-step at strength ε; it is FSO at strength ε vs. multi-step at a lower strength. Since Section 5.1 independently shows that transferability depends on perturbation strength, the reported gains conflate two effects: reaching the target strength faster (a genuine benefit of FSO) and potentially better direction optimization. These cannot be disentangled from Table 1 alone. Furthermore, the leave-one-out validation picks the "best" perturbation from sets with different strength profiles (varying for multi-step, constant for FSO), adding another source of asymmetry.

- **Unsupported claim that FSO enhances other attack methods.** The paper states (line 167): "Other attack methods such as MI, VR, SGM, IR, and TI, can also be naturally incorporated in FSO. For these attack methods, we also observed significant enhancement of transferability by using FSO under the L₂₋∞ norm." No quantitative comparison is provided for any of these methods. Figure 4 shows FSO+SGM results but only with varying m, not compared against multi-step SGM. For MI, VR, IR, and TI, there is zero comparative data. Since the paper's title and introduction promise a general enhancement framework, this evidential gap is substantial.

### Minor

- **No quantitative imperceptibility metrics.** The paper claims the L₂₋∞ norm produces perturbations with "high imperceptibility" (abstract, line 27, conclusion) but supports this only with visual examples in Figure 5. No standard metric (SSIM, PSNR, LPIPS, or human evaluation) is reported. Since the paper's motivation for the L₂₋∞ norm is that it "achieves both advantages of L₂ norm and L∞ norm" — including imperceptibility — the lack of measurement on one side of this trade-off weakens the claim.

- **Unsubstantiated geometric intuition.** The paper states (line 63) that "the tangential component ... is usually small compared to the normal component" as a key motivation for why multi-step methods converge slowly. No empirical measurement of this angle is provided (e.g., average cosine similarity between gradient and normal vector over iterations). While the intuition is plausible, a central geometric claim should be supported with data.

- **Narrow baseline set.** The only multi-step attack compared quantitatively is PGD. The paper's own Figure 1(a) shows PGD has the weakest transferability among the four methods tested (PGD, SGM, VR, IR). Comparing FSO+PGD against multi-step SGM, VR, or IR would establish whether FSO improves upon already-strong baselines or merely raises a weak baseline. By only benchmarking against the weakest competitor, the paper's reported margins may overstate the practical benefit.

### Trivial

- **Step size hyperparameter not discussed.** The decaying step size αᵗ = α₀/t (line 73) is introduced without any discussion of how α₀ is chosen or whether results are sensitive to this choice.

- **No variance reporting.** The paper notes "three different random samplings" (line 150) but does not report standard deviations or confidence intervals for success rates, which is standard practice for transfer attack experiments where variance is known to be non-negligible.

## Nice-to-Haves

- A strength-controlled analysis: rescale multi-step perturbations to match FSO's strength (as in Section 5.1's diagnostic) and then compare transferability. This would separate the strength benefit from the direction-optimization benefit.
- An ablation comparing FSO vs. multi-step under the same L₂₋∞ norm (to isolate the benefit of fixed-strength optimization from the benefit of the new norm).
- Sensitivity analysis for α₀ and the projection repetition (single vs. double Proj).

## Removed Points

These points were flagged by reviewers but are removed from the main weakness list for the reasons indicated:

- *"Section 4: The convergence of the norm to ε is shown in Figure 2(b), but the impact of this inexactness on the optimization objective is not analyzed."* — The paper explicitly discusses this (line 96: "This realization is not the exact projection") and shows empirically that the norm converges quickly. The request for deeper theoretical analysis exceeds what is standard for an empirical paper; retaining as a minor weakness would over-amplify a reasonable scope choice.
- *"The paper does not discuss scenarios where FSO might underperform."* — This is a generic "add a limitations section" request. The paper's scope is presenting a method with empirical validation, and the absence of a limitations section does not constitute a specific flaw in the contribution.
- *"Pure formatting/style nitpicks"* and *"typos"* — Removed per hard rules; these are parser artifacts, not author errors.
- *"Reproducibility concerns about undisclosed hyperparameters"* — Removed per hard rules (trivial implementation details).

## Novel Insights

The synthesized reviews reveal a tension that the paper itself does not fully confront: FSO's primary benefit may be **convergence speed** (reaching the target strength in fewer steps) rather than **superior direction optimization** at the same strength. The paper acknowledges but does not resolve this. An interesting observation from Section 5.1 — that rescaling multi-step perturbations to a fixed strength yields non-monotonic transferability curves that peak where the perturbation was originally computed — suggests that direction quality depends on the path taken, not just the terminal point. This is a potentially deeper result than the paper exploits: it implies that even under fixed-strength optimization, different initialization strategies could lead to different-quality directions, which is worth further study.

## Suggestions

1. **Disentangle strength and direction in the main comparison.** Either (a) run multi-step PGD for enough iterations to reach the target ε (even if that requires many more than 30 steps), or (b) rescale multi-step perturbations to match FSO's strength and compare transferability at matched strength, extending the Section 5.1 analysis to the full model set. This directly addresses the core confound.
2. **Provide quantitative imperceptibility metrics** (SSIM, LPIPS, or at minimum average per-pixel perturbation statistics) for all methods compared in Table 1 to substantiate the claim about the L₂₋∞ norm's visual advantages.
3. **Add at least one additional attack method** (e.g., SGM or MI-FGSM) to the main comparison table, comparing FSO+method against multi-step method under both L₂ and L₂₋∞ norms, to support the generalizability claim.
