Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes DPPN, a two-stage defense against embedding inversion attacks that (1) detects "privacy neurons" (embedding dimensions correlated with a target sensitive token) via differentiable neuron mask learning with hard concrete distributions and L0 regularization, and (2) perturbs only those neurons with a directional neuron-suppressing noise. The core idea — selective, targeted perturbation rather than uniform noise across all dimensions — is well-motivated by the insight that only a subset of embedding dimensions carry sensitive information.

## Strengths

- **Novel differentiable neuron mask learning framework for privacy neuron detection.** The paper operationalizes the concept of "privacy neurons" by learning a binary mask via HardConcrete distributions (Eqs. 3–5), enabling gradient-based optimization to identify which embedding dimensions carry sensitive token information. This is a concrete technical advance over uniform noise injection approaches.

- **Quantitative evidence of superior privacy-utility tradeoff.** Table 1 shows DPPN at ε=2 on STS12 reduces Leakage from 60% (unprotected) to 13%, while baselines (LapMech, PurMech) only reach 22%, with downstream performance improved by 14–40% relative to baselines. This directly supports the claim that selective perturbation yields better tradeoffs.

- **Black-box detection approximates white-box performance.** Section 5.1 (Figures 4 and 5) demonstrates DPPN's black-box method achieves only 3–6% absolute difference in Leakage and less than 5% relative difference in downstream metrics compared to a white-box oracle (DPPN-Oracle), with 32–51% neuron overlap. This provides evidence the method does not require knowledge of the attack model.

- **Consistent robustness across multiple attack models and embedding models.** Table 3 shows DPPN reduces leakage by 88% (Vec2text) and 51% (GEIA) at ε=1, outperforming baselines across all attacks. Table 5 extends this to GTR-base, Sentence-T5, and SBERT, showing consistent superiority.

- **Effectiveness on real-world sensitive datasets.** Table 4 shows DPPN lowers MIMIC-III sex leakage from 88% to 17%, while baselines only reach 43%. Similar improvements hold for disease names and PII categories.

## Weaknesses

### Fatal
None.

### Major
- **Handling of multiple sensitive tokens simultaneously is unspecified.** The paper defines the defender's goal as protecting a set of sensitive tokens T (Section 2.2) and reports results on datasets with multiple PII categories (e.g., MIMIC-III with sex, diseases, symptoms). However, the methodology only describes learning a separate mask per token t. How multiple masks are combined for a single embedding containing multiple sensitive tokens is not described. The qualitative analysis (Figure 6) mentions using the "union of the top-5 neuron indices" for related words, but this is stated in passing for visualization only, not presented as the general defense mechanism. Without specifying this, it is unclear whether the reported real-world results (Tables 4, 6) are achievable in multi-token scenarios as described.

### Minor
- **Eq. 4 uses a non-standard loss formulation whose gradient behavior is suboptimal for negative examples.** The loss for negative examples is -(1 - log P) = log P - 1. While the optimization *direction* is correct (pushing P → 0), the gradient magnitude is (1-P) — small when the prediction is wrong (P near 1) and large when correct (P near 0), which is the opposite of the standard binary cross-entropy gradient (p). This is not a fatal error (the method still converges) but it is unusual, the paper provides no justification for it, and it may slow or destabilize training. Clarification or correction to standard BCE is needed.

- **Noise comparison is partially confounded by the one-sided perturbation.** The paper scales ε by √(k/d) for DPPN, which correctly equalizes total variance for *symmetric* Laplace noise. However, DPPN's actual perturbation uses one-sided noise (|ν_i|, an exponential distribution), which has half the variance of the symmetric Laplace used by baselines. This gives DPPN a structural advantage in total noise power (~2× less total variance), making it hard to fully attribute the privacy-utility improvement to the selectivity/directionality of perturbation vs. lower total noise. A controlled comparison matching the *actual* (one-sided) noise variance across methods would strengthen the evidence.

- **White-box oracle (DPPN-Oracle) may not be a proper ground truth for optimal privacy neurons.** The white-box method uses FGSM on the *attack model's* loss to identify influential neurons. As the paper notes, this gives 32–51% overlap with DPPN's black-box neurons, suggesting the two criteria differ. The paper should discuss whether the attack model's loss gradient is the correct ground truth for the *defender's* ideal privacy neuron set, or whether there is a more principled definition of "privacy neuron."

- **"5-78%" leakage reduction range is reported without specifying which settings produce the extremes.** This makes it hard to assess the robustness and consistency of the claimed improvement across the full experimental space.

- **Definition of Leakage for sentence-level attacks (Vec2text, GEIA) could be more precise.** The paper defines Leakage as "the attack model's accuracy in predicting sensitive tokens," but for sentence-level reconstruction, it is not specified how the presence of a sensitive token is detected from reconstructed text (e.g., substring match, exact match, probability threshold).

- **The qualitative analysis (Figure 6) relies on visual inspection.** The claim that "semantically similar words share similar privacy neurons" would be strengthened by a quantitative overlap measure (e.g., average Jaccard similarity within vs. across semantic groups). The case study (Table 6) uses only two examples; representativeness is unclear.

- **Hyperparameters ξ, γ for the HardConcrete distribution are not specified.** The paper states these are "constants" but does not give their values or initialization ranges for the learnable temperature β_i.

### Trivial
None.

## Nice-to-Haves
- Evaluation against adaptive attackers who know DPPN is being used and attempt to circumvent it (e.g., by training on perturbed embeddings).
- Discussion of the computational cost of mask learning, which requires one model per sensitive token.
- A properly controlled experiment matching the *actual noise power* (expected L2 norm of the one-sided perturbation) across all methods at multiple levels, to isolate the benefit of targeted perturbation from lower total noise.

## Removed Points

- **Eq. 4 is "incorrectly specified" and "fatal"** — REMOVED (factually wrong: the reviewer analyzed (1 − log P) in isolation, ignoring the outer negative sign that makes the optimization direction correct. The formulation is non-standard but not invalid. The actual issue is suboptimal gradient magnitude, noted above as minor.)
- **Noise scaling "factually incorrect" and "fatal"** — REMOVED (the reviewer assumed ε is the Laplace scale parameter; the paper uses Lap(0, 1/ε) making 1/ε the scale. The scaling √(k/d)*ε correctly equalizes variance for symmetric Laplace. The genuine secondary issue of one-sided noise variance mismatch is addressed as minor above.)
- **Missing Vec2text training hyperparameters** — REMOVED (trivial implementation detail not expected in a main paper).
- **Only 2 of 6 datasets shown in Table 1** — REMOVED (standard for space-constrained papers; the other 4 are mentioned).
- **Sensitivity measure Δ_i uses max** — REMOVED (this is a preliminary analysis; using max is a standard approach for sensitivity analysis and is not central to the method).
- **Lack of theoretical analysis for perturbation function** — REMOVED (the paper is empirical; theoretical analysis is not required).
- **MLC robustness alternative explanation** — REMOVED (speculative; both explanations are plausible and the paper's interpretation is reasonable).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the multi-token handling mechanism.** The simplest approach (union of top-k neurons across all target tokens) should be stated explicitly; more sophisticated approaches (weighted combining) could be discussed. This is the most impactful improvement.
2. **Fix or justify the unusual loss formulation in Eq. 4.** Either replace it with standard binary cross-entropy (which would have the correct gradient behavior) or explain why the current formulation is preferred.
3. **Add a controlled experiment matching one-sided noise power.** Run DPPN and baselines at multiple levels where the total *expected L2 norm* (or total variance) of the *actual applied noise* is matched, not just the symmetric Laplace noise.
4. **Report the specific settings for the "5-78%" leakage reduction range** so readers can assess consistency.
5. **Add quantitative overlap metrics for the qualitative analysis** (Figure 6) and increase the case study sample size.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Accept</decision>