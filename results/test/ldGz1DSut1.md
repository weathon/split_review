## Summary

This paper presents the first systematic empirical study of whether deep image watermarking methods can coexist in the same image. Through experiments across 8 open-source methods and all 64 ordered pairs, the authors demonstrate that contrary to intuition, different watermarks can coexist with only modest degradation in accuracy, robustness, and image quality. They further show that coexistence enables watermark ensembling as a post-training tool to increase capacity or adjust trade-offs without retraining. The paper is well-motivated by real use cases (super watermarking for decoder selection and multi-actor provenance chains) and is honest about the limitations of the approach.

## Strengths

- **First systematic study of deep image watermark coexistence.** The paper explicitly claims this novelty (Abstract, Sec. 1) and backs it with comprehensive empirical evidence across 8 methods in Table 1. Many pairs retain high accuracy for both watermarks (e.g., DwtDct followed by DwtDctSvd yields 1.00 for both), directly contradicting the expectation that the second watermark would overwrite the first.

- **Coexistence persists even after controlling for image quality degradation.** Figure 3 shows that when watermark strength is clipped to match the average quality of the base methods, many pairs still retain non-zero accuracy for both watermarks (highlighted cases with accuracy ≥25%). This shows coexistence is not merely an artifact of quality reduction.

- **Practical use-case motivation with concrete scenarios.** Section 3 defines two real-world applications (super watermarking and multi-actor provenance chains), framing the problem as practically necessary rather than purely academic.

- **Honest assessment of boundaries.** Section 4 explicitly acknowledges that ensembling is not always beneficial — Figure 8 shows TrustMark Q with ECC alone dominates all ensembles of RivaGAN and TrustMark Q. The paper also discusses limitations including PSNR as an imperfect quality metric, computational cost, and the domain restriction to images.

## Weaknesses

### Fatal
None.

### Major

- **Ensembling experiments lack comparison against single-method baselines at equivalent capacity.** The paper presents, e.g., an ensemble of SSL (100 bits) and TrustMark B (100 bits) as achieving 200-bit capacity, but never tests whether simply configuring SSL — which the paper itself notes "allows selecting... message length at inference time" (Sec. 2) — at 200 bits directly would achieve comparable or better accuracy, robustness, and quality. Since the ensembling experiments are presented as contribution (iii), this missing baseline makes it unclear whether ensembling genuinely adds value beyond existing flexibility in the base methods. The paper already includes comparisons against single-method+ECC baselines (Fig. 8), showing the authors are aware of this class of comparison, which makes the omission more conspicuous. This does **not** undermine the paper's core coexistence finding (contributions i and ii), but it weakens the ensembling claims in contribution iii.

### Minor

- **No confidence intervals or variance estimates.** All results (Table 1, Figures 2–6) are reported as point estimates over 1020 images without error bars, standard deviations, or confidence intervals. Many observations hinge on small differences (e.g., whether accuracy drops by 2% or 5%), and without variance information the reader cannot assess whether these differences are meaningful or due to sampling noise. This is a standard expectation for empirical studies that the paper should address.

- **TrustMark Q capacity is not stated explicitly.** The paper uses TrustMark B (implied 100 bits from context at line 102) and TrustMark Q but never states the message length for TrustMark Q. This information is needed to interpret the capacity-related results in Figures 6 and 8.

### Trivial

- **Robustness definition in the main text is brief.** The paper defines robustness conceptually (line 39: "the fraction of secrets we can decode correctly when certain transformations or edits have been added") and references App. D for the specific augmentations. While this is sufficient to interpret the main results, a short sentence naming the specific augmentations (e.g., crop, resize, JPEG compression) in the main text would improve readability without forcing readers to the appendix.

## Nice-to-Haves

- A comparison of the ensembled 200-bit system against a single SSL model configured for 200 bits (with appropriate quality/strength matching) would substantially strengthen the ensembling claims.
- Reporting variance (e.g., bootstrapped confidence intervals) for key quantitative results would make the comparisons more trustworthy.
- Including a small experiment showing whether SSL at higher capacities (150, 200 bits) maintains reasonable accuracy would directly address the most salient concern about the ensembling experiments.

## Removed Points

- **"TrustMark may also support variable capacity, so the same critique applies"** — The paper does not claim TrustMark supports variable capacity; this is speculation by the reviewer. Removed as speculative and factually ungrounded.
- **"Robustness evaluation is underspecified to the point of being impossible to evaluate"** — The paper does define robustness (line 39) and specifies the source of augmentations. The level of detail is adequate for an empirical study that defers implementation specifics to an appendix that exists in the original submission. Downgraded from the critic's implied severity to Trivial.

## Novel Insights

The finding that watermarks from different methods encode information in quasi-orthogonal subspaces (without explicit coordination) is the paper's most interesting contribution, and it raises a genuinely non-trivial question for the community: why does this happen, and can we design watermarking methods to either maximize or minimize this behavior? The paper's channel-coding analogy (FDMA without a coordinating authority) is a helpful mental model, though the paper correctly notes it cannot be directly applied to non-linear deep methods.

## Suggestions

1. Add an experiment comparing the ensemble of SSL (100 bits) + TrustMark B (100 bits) against SSL configured for 200 bits directly, matching for quality (PSNR) as closely as possible. If SSL at 200 bits performs worse, that strengthens the ensembling case; if it performs similarly or better, the ensembling claims should be tempered accordingly.
2. Add bootstrapped confidence intervals (e.g., 95% CI) to the key quantitative results, especially Table 1 and Figures 5–6.
3. Explicitly state the capacity (in bits) of TrustMark Q in the main text.
4. Add a one-sentence summary of the specific robustness augmentations (crop, resize, JPEG, etc.) to Section 2 for readability.

## Score and Decision

**Originality:** 7/10 — The coexistence finding is novel and runs counter to reasonable expectations. Ensembling as an application is a natural extension but not deeply surprising once coexistence is established.

**Importance:** 8/10 — Addresses a genuine practical need as multi-actor watermarking becomes more common. The findings have implications for standards like C2PA.

**Claims support:** 6/10 — The coexistence claims (i, ii) are well-supported. The ensembling claims (iii) are partially supported but lack a critical baseline comparison.

**Soundness:** 7/10 — Experimental design is reasonable and comprehensive. The main weakness is the missing single-method baseline and lack of variance reporting.

**Clarity:** 8/10 — Well-written, clearly structured, honest about limitations.

**Value to community:** 8/10 — Opens a new dimension in watermarking research and provides a solid empirical foundation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>