## Summary

This paper addresses the tension between watermarking language model outputs and the efficiency of speculative sampling. The authors make three main contributions: (1) a quantitative measure of watermark strength (WS) defined as expected KL divergence between watermarked and original token distributions, which links to statistical detectability; (2) a formal characterization of the trade-off as a constrained Pareto optimization problem, with explicit trade-off curves for existing watermarking schemes (Gumbel-max, SynthID); and (3) a principled algorithm (Alg. 1) that replaces the random acceptance coin-flip in speculative sampling with a pseudorandom decision, ensuring maximal watermark strength while maintaining sampling efficiency. Theorem 4.1 proves that under the assumption of a degenerate decoder, the algorithm simultaneously achieves unbiasedness, maximum sampling efficiency (1−TV(Q,P)), and maximum watermark strength (Ent(P)). Experiments on Llama‑68M/7B and Gemma‑2B/7B show that the method preserves average accepted tokens per step (AATPS) relative to unwatermarked speculative sampling while improving true-positive rates at 1% FPR compared to prior detection strategies that lack access to the pseudorandom acceptance variable.

## Strengths

- **Quantitative watermark-strength measure (Def. 3.1).** The paper moves beyond the binary watermark-preserved/not-preserved definition in prior work (Hu & Huang 2024) by defining WS as expected KL divergence. Theorem 3.1 connects this measure to the p-value decay rate of the UMP test, establishing a direct link between WS and sample complexity. Theorem 3.2 proves WS is bounded by the entropy of the original distribution and maximized only by degenerate (deterministic) decoders. This is a substantive theoretical advance that enables continuous trade-off analysis.

- **Principled Pareto characterization (Definition 3.2, Figure 1).** The trade-off is formalized as a constrained optimization problem where sampling efficiency (expected acceptance rate) constrains achievable watermark strength. The formulation is plug-and-play: specifying the draft and target decoder families yields a concrete Pareto frontier. Figure 1 provides the first side-by-side visual comparison of the achievable strength–efficiency region for linearly interpolated classes, Hu's class, and Google's class, clearly showing that neither existing scheme reaches the theoretical optimum.

- **Pseudorandom acceptance mechanism (Algorithm 1, Theorem 4.1).** The core algorithmic idea—making the acceptance decision pseudorandom rather than truly random—is clean and well-motivated. Theorem 4.1 proves unbiasedness, maximum sampling efficiency, and maximum watermark strength under this scheme (assuming a degenerate decoder). This is the first construction that theoretically achieves both extremes simultaneously, directly addressing the impossibility result of Hu & Huang (2024).

- **Empirical verification of improved detectability at preserved efficiency (Figure 2).** The experiments confirm that AATPS remains statistically indistinguishable from standard (unwatermarked) speculative sampling across lookahead values K ∈ {2,3,4} for both Gumbel-max and SynthID watermarks. Meanwhile, the detection methods that leverage the pseudorandom acceptance variable ζ^R (Ars‑τ for Gumbel-max, Bayes‑MLP for SynthID) achieve substantially higher TPR at 1% FPR than the prior-based counterparts that do not use ζ^R. The evaluation covers two model pairs (Llama‑68M/7B, Gemma‑2B/7B), two datasets (EL15, C4), and reports both efficiency and quality (log-perplexity) metrics.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The empirical comparison is within-algorithm, not against a competing trade‑off scheme.** The detectability experiments compare Ars‑τ vs. Ars‑Prior and Bayes‑MLP vs. Bayes‑Prior—all applied to the output of Algorithm 1. The baselines (Ars‑Prior, Bayes‑Prior) represent the prior detection approach from Dathathri et al. (2024) that does not use the acceptance variable ζ^R, so the comparison cleanly isolates the benefit of ζ^R for detection. However, the paper does not benchmark against a method that explicitly sacrifices sampling efficiency to preserve watermark strength (e.g., the Pareto-frontier operating points from Section 3). While such a comparison is difficult because Hu & Huang (2024) proved an impossibility result rather than proposing a specific alternative algorithm, the paper's central claim of "improving the trade-off" would be strengthened by showing that at a matched efficiency level the proposed method achieves higher detectability than any scheme that does not use pseudorandom acceptance. The current experiments convincingly show that using ζ^R helps, but they do not quantify the gap relative to the best attainable trade‑off without the algorithmic change.

2. **Watermark strength is not empirically measured.** Definition 3.1 defines WS in terms of expected KL divergence, and Theorem 4.1(c) proves that Algorithm 1 achieves maximal WS. However, the experiments measure TPR at fixed FPR, not WS itself. The paper attributes improved detectability to the extra information from ζ^R, but does not verify empirically that the improvement stems from attaining maximal WS (rather than from better exploitation of ζ^R for detection). Computing or estimating the empirical KL divergence on generated sequences and plotting the operating points on the Pareto diagram of Figure 1 would bridge the gap between the theoretical guarantee and the experimental results.

3. **Theorem 4.1 assumes a degenerate decoder; experiments use non‑degenerate SynthID (m=30).** Theorem 4.1 builds on the assumption that the decoder achieves maximal watermark strength, which by Theorem 3.2 requires degeneracy (Ent(P_ζ)=0 a.s.). Gumbel‑max satisfies this, but SynthID does so only in the limit m→∞. The experiments use SynthID with m=30, which is not fully degenerate. The paper acknowledges this gap for the trade‑off curves in Section 3.2 ("when we set m=30…the watermark strength drops below that of Gumbel‑max"), but does not discuss its implications for the guarantees of Theorem 4.1. The fact that the algorithm still empirically improves detectability with non‑degenerate decoders is encouraging, but the paper would benefit from either extending the theory to non‑degenerate cases or explicitly discussing why the algorithm is still expected to work.

4. **Trade‑off curves in Figure 1 are derived under simplified parametric families.** The curves are obtained using linearly interpolated classes (Eq. 9) that mix the original distribution with a fully watermarked distribution. This is a legitimate simplification for illustration, but the language ("fully characterize the trade‑off," "explicit Pareto curves for two existing watermarking schemes") somewhat overstates what is derived. The paper notes that these are examples ("For illustration…"), but the gap between the simplified parametric families and the actual deployed watermarking algorithms should be more prominently acknowledged in the figure caption or associated discussion.

5. **Detection for Gumbel‑max uses a fixed threshold τ instead of the token‑dependent acceptance threshold.** Equation (11) selects between y^D and y^T using a fixed τ calibrated on a validation set, whereas the exact acceptance rule in Algorithm 1 is min{1, P_w/Q_w}, which is token‑dependent. The paper acknowledges that τ is a heuristic and calibrates it via grid search, but does not analyze how the gap between the heuristic and the oracle detector (visible in Figure 2) relates to the variability of the true acceptance threshold. A brief discussion of this gap would help readers understand the remaining headroom.

### Trivial

- The paper uses reduced temperatures (0.5 for Gumbel‑max, 0.7 for SynthID) to "make the results more pronounced." A brief comment on whether the findings hold at temperature 1.0 would strengthen the evaluation.
- The AATPS error bars in Figure 2 are very small; a note on the number of independent runs used to compute them would improve interpretability.
- The paper does not report the total variation distance TV(Q,P) or baseline acceptance rates for the model pairs used, which would help contextualize the AATPS numbers.

## Nice-to-Haves

- **Empirical WS measurement.** Computing or estimating the empirical KL divergence on generated sequences would directly connect the experimental results to the theoretical framework and strengthen the claim that the trade‑off is broken in practice.
- **Analysis of detection gap.** A brief analysis of why the proposed detectors (Ars‑τ, Bayes‑MLP) do not reach the Oracle bound would help clarify the remaining limitations and guide future work.
- **Extension to temperature 1.0.** A small experiment or discussion of how the trade‑off behaves at higher temperatures would broaden the applicability of the results.

## Removed Points

These points from the reviewers were evaluated against the paper and removed for the reasons indicated:

- **Residual sampler normalization (Critic point on Alg. 1, Line 12):** The notation `(P-Q)_+` as a distribution is the standard convention in the speculative sampling literature (Leviathan et al. 2023, Chen et al. 2023)—it refers to the normalized residual distribution. This is a nitpick about well-established notation, not an error.
- **Theorem 3.1 assumptions not justified:** The assumptions of bounded log-likelihood ratios and finite MGF in a neighborhood of zero are standard technical conditions in large‑deviation theory. Brief justification would be nice but is not required; the paper is not unusual in stating these without extensive defense.
- **Equation (10) derivation is compressed:** The derivation from Eq. (8) to Eq. (10) is standard for the linear families defined, and the compression is appropriate for a conference paper. The reasoning is clearly stated: combining Defs. 2.1 and 3.1 with the speculative sampling kernel and the identity Σ min(P,Q) = 1 − ½‖P−Q‖₁.
- **Missing repeated context masking details:** The paper provides a one-sentence explanation ("skips watermarking for repeated contexts") and cites three prior works. The appendix (stripped from the review copy) likely contains further detail. This is adequately referenced for a main-text description.
- **Comparison against Hu & Huang (2024) as a specific method:** Hu & Huang (2024) proved an impossibility theorem; they did not propose a deployable watermark + speculative sampling algorithm. The paper's baselines (Ars‑Prior, Bayes‑Prior) represent the closest prior detection approach (Dathathri et al. 2024). Requiring a comparison against a method that does not exist as a concrete algorithm is not reasonable.

## Novel Insights

The key insight not previously in the paper is that **the trade‑off between watermark strength and speculative sampling efficiency is not fundamentally about the distributions themselves, but about the source of randomness in the acceptance step**. By converting the acceptance coin‑flip from a source of true randomness into a pseudorandom function computed from a recoverable key, the entire generation pipeline becomes a deterministic function of pseudorandom variables. This converts the acceptance decision from information-theoretic noise into part of the signal available to a detector, making the tension between efficiency and detectability a design choice rather than a statistical necessity. The paper's theoretical framing—where WS is defined as expected KL divergence and maximized by degenerate distributions—reveals that the original "impossibility" result (Hu & Huang 2024) was an artifact of a binary definition of watermark strength that could not capture intermediate or alternative design dimensions.

## Suggestions

1. **Add an experiment measuring empirical WS.** Compute the average KL divergence D_KL(P_ζ ∥ P) on generated tokens for Algorithm 1 and for a baseline that does not use pseudorandom acceptance. Plot these points on the Pareto diagram of Figure 1 to directly visualize that the method operates near the theoretical optimum.
2. **Discuss the non‑degenerate case.** Either extend Theorem 4.1 to provide a lower bound on WS for non‑degenerate decoders, or add a paragraph explaining why the algorithm is still beneficial when the decoder is not fully degenerate (supported by the SynthID m=30 results).
3. **Clarify the baseline scope.** Explicitly state in the experimental section that Ars‑Prior and Bayes‑Prior represent the prior art from Dathathri et al. (2024) and that the comparison isolates the benefit of the pseudorandom acceptance variable, clarifying why no separate external algorithm baseline is included.
4. **Add a brief analysis of the τ heuristic gap.** Explain how the fixed threshold τ relates to the distribution of min{1, P_w/Q_w} and discuss under what conditions the gap to the Oracle detector could be closed.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>