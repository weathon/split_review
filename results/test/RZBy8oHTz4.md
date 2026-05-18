Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes adding an additive factor τ to the negative-pair term of spectral contrastive loss, which is equivalent to zero-mean regularization. The key insight is that this uniformly reduces all positive-pair edge weights, thereby altering the ratio between intra-class and inter-class connections and implicitly mitigating wrong connections. The paper provides theoretical analyses for unsupervised domain adaptation (showing the target error bound tightens by a factor of (1−τ)²), for supervised SpeCL (showing optimal representations mirror Neural Collapse), and for label noise (showing τ provably reduces the effective noise rate). Experiments across self-supervised, supervised, UDA, and noisy-label benchmarks show consistent but modest improvements.

## Strengths

1. **Simple yet principled modification with a unified interpretation**: Adding τ to the negative-pair term is conceptually minimal, and the paper convincingly shows it is equivalent to zero-mean regularization. The uniform-weight-reduction intuition (Figures 1–3) provides a clean, geometric explanation of why this helps across different settings (self-supervised, UDA, noisy labels). This conceptual unification is a genuine contribution.

2. **Closed-form optimal representations with Neural Collapse connection**: Theorem 3.3 derives the unique global minimizer of the supervised SpeCL loss, showing that class-mean features satisfy ĤᵀĤ = rI − τ𝟙𝟙ᵀ (when r ≤ d+1), which directly mirrors the Neural Collapse geometry. The paper correctly notes that τ = 1 recovers the standard Neural Collapse ETF solution. This bridges spectral contrastive learning and the Neural Collapse literature.

3. **Provable mitigation of label noise**: Proposition 3.5 gives a clean theoretical result: under symmetric label noise with rate ω, using τ ≥ rω makes the noisy-loss minimizer equivalent to the clean-loss minimizer with a reduced effective regularization (τ−rω)/(1−rω). This is an elegant and non-obvious result that directly explains the empirical gains.

4. **Consistent empirical validation across tasks**: Tables 1–3 show that τ > 0 consistently outperforms τ = 0 on self-supervised linear probing, supervised classification, UDA across four digit datasets, and noisy-label benchmarks (e.g., +5.97% on CIFAR-10 at 80% noise). The gains are modest but systematic, and largest in high-noise scenarios where the theory predicts the most benefit.

## Weaknesses

### Fatal
None.

### Major

1. **The eigenvalue scaling behind Proposition 3.2 is presented without justification in the main text.** The paper's central theoretical result for UDA is that zero-mean regularization tightens the target error bound by (1−τ)². Theorem 3.1 expresses the bound in terms of λ̃₁(τ), λ̃_d(τ), λ̃_{d+1}(τ). Proposition 3.2 then states that under a stated condition on τ, the bound becomes O(((1−τ)²(λ̃₁(0))²)/(η⁴(λ̃_d(0)−λ̃_{d+1}(0))²·n))·poly(r,p). The paper provides no reasoning — not even a sketch — for why λ̃₁(τ) = (1−τ)λ̃₁(0) or why the spectral gap λ̃_d(τ)−λ̃_{d+1}(τ) = λ̃_d(0)−λ̃_{d+1}(0). Since Ã = E[A] − (τ|E|/N²)𝟙𝟙ᵀ is a rank-1 perturbation, the eigenvalue shift is plausible, but the mapping to the clean (1−τ) factor requires connecting λ̃₁(0) to |E|/N in a specific way. Without any derivation or even a sentence explaining the reasoning, the main theoretical claim for UDA is essentially an opaque assertion. The appendix may contain the full derivation, but the main text must give enough of a sketch for a reviewer to assess plausibility. (This does not invalidate the result, but it does mean the paper's strongest theoretical claim cannot be evaluated from the main text alone.)

2. **UDA experiments are limited to digit datasets.** The experiments use SVHN, MNIST, USPS, and MNIST-M — all digit recognition datasets with relatively simple visual structure and small domain shifts. Claims about domain adaptation benefits would be substantially strengthened by evaluation on more challenging benchmarks (e.g., Office-Home, VisDA-2017) where wrong connections in the positive-pair graph are more consequential. Without this, it is unclear whether the theoretical benefits translate to realistic UDA settings.

### Minor

1. **The supervised loss formulation includes same-class pairs in the negative term without empirical validation of the design choice.** The paper explicitly notes (line 149) that it retains c = k in ℒ_{neg} and provides two reasons: alignment with the self-supervised form, and prevention of the loss from diverging. These are reasonable justifications, and Theorem 3.3 shows the global minimizer resolves the tension. However, no ablation study compares this formulation against the more common design (excluding positive pairs from negatives). Such an experiment would clarify whether the proposed formulation is *necessary* for good performance or merely sufficient, and would help assess whether the practical utility is robust to this design choice.

2. **No systematic sensitivity analysis for τ.** The experiments test a few discrete values of τ (sometimes just τ = 0 vs. τ = 1). A plot of performance versus a sweep of τ values — especially for the noisy-label setting where the theory predicts a threshold effect at τ ≥ rω — would help identify the optimal range and robustness of the method.

3. **No empirical analysis of representation geometry.** The paper proves that optimal representations satisfy ĤᵀĤ = rI − τ𝟙𝟙ᵀ (Theorem 3.3), which predicts specific angular relationships between class means. Reporting empirical measures of within-class collapse, between-class angular separation, or Neural Collapse metrics would directly corroborate the theoretical predictions and strengthen the paper.

### Trivial

- The conclusion states that zero-mean regularization "makes representations of negative pairs opposite" (line 209), while the introduction describes it as "relaxing the orthogonality" (line 14). These are not contradictory (relaxing orthogonality toward negative dot products is the mechanism; the effect is making representations more opposite), but the stronger phrasing in the conclusion could mislead readers into thinking τ forces strict anti-alignment.

## Nice-to-Haves

- **Asymmetric or real-world label noise experiments.** Theorem 3.4 covers general noise, but Proposition 3.5 and the experiments are restricted to symmetric noise. Evaluating on benchmarks like CIFAR-10N or CIFAR-100N with asymmetric/real-world noise would demonstrate that the mitigation effect holds beyond the simplest noise model.
- **More challenging UDA benchmarks** (as noted in Major weakness 2 above).
- **Sensitivity analysis of τ** (as noted in Minor weakness 2 above).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Missing dedicated related work section"** — The reviewer notes that related work is scattered through the introduction and remarks. The parser strips supplementary sections; a dedicated related work section may exist in the original submission. Moreover, the introduction already provides adequate context for the paper's positioning. **Reason for removal**: the parser may have stripped the related work section; this is a formatting artifact, not an author error.

2. **"Notation overloaded"** — The reviewer mentions notation is "sometimes overloaded but generally clear." This is too vague and minor to constitute a meaningful weakness. **Reason for removal**: generic observation without a concrete problem.

## Novel Insights

The reviewers surface a genuine tension at the heart of the paper: the main UDA theoretical result (Proposition 3.2) is presented as a clean multiplicative factor (1−τ)², but the eigenvalue perturbation argument connecting Ã = E[A] − (τ|E|/N²)𝟙𝟙ᵀ to this clean factor is not sketched in the main text. Since the paper's UDA story hinges on this result, this is where a rebuttal must focus. Conversely, the Neural Collapse result (Theorem 3.3) and the label-noise mitigation result (Proposition 3.5) are presented with sufficient clarity to be evaluated on their own terms. The paper's strongest claim (UDA) is its least transparent one.

## Suggestions

1. In the main text (Section 3.2), add a short paragraph or footnote showing the key eigenvalue perturbation step: that Ã = E[A] − (τ|E|/N²)𝟙𝟙ᵀ is a rank-one subtraction, that the eigenvectors of E[A] (under the SBM) are preserved, and that under the stated condition on τ, the first eigenvalue scales as (1−τ)λ̃₁(0) while the spectral gap for d vs. d+1 is unchanged. Even 3–4 lines of reasoning would make Proposition 3.2 evaluable from the main text.

2. Add an ablation comparing the proposed supervised loss (with c = k in ℒ_{neg}) against a variant that excludes positive pairs from the negative term. This would either confirm the design choice is necessary or reveal that the simpler variant works equally well.

3. Add a sensitivity plot of performance vs. τ for at least one task (e.g., CIFAR-10 with 80% label noise) to show the optimal range and the threshold predicted by Proposition 3.5.

## Score and Decision

The paper presents a conceptually clean modification to spectral contrastive learning with a unified theoretical framework and consistent empirical support. The main theoretical weakness — opaque presentation of the eigenvalue scaling in Proposition 3.2 — is a clarity issue rather than a substantive error, and the experimental scope is adequate but not extensive. The Neural Collapse connection and label-noise mitigation results are well-supported. With the presentation issues addressed, the paper's contributions are solid.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>