## Summary

The paper addresses the trade-off between watermark strength and speculative sampling efficiency in LLMs. It introduces a continuous, KL-divergence-based measure of watermark strength (WS), proves this governs the p-value decay rate and sample complexity for detection (Theorem 3.1), and casts the trade-off as a Pareto optimization problem (Def. 3.2). The central contribution is Algorithm 1, which injects pseudorandomness into draft-token acceptance and is proved to simultaneously achieve maximum watermark strength and maximum speculative sampling efficiency (Theorem 4.1). Experiments validate maintained efficiency and improved detectability over prior methods.

---

## Strengths

- **Quantitative watermark strength definition with statistical grounding.** Def. 3.1 defines WS as the expected KL divergence E_ζ[D_KL(P_ζ ∥ P)], and Theorem 3.1 proves it governs the exponential decay rate of the p-value under the UMP likelihood ratio test, directly linking the measure to sample complexity. This is not a superficial reformulation — it provides a rigorous statistical foundation.

- **Maximal strength characterization.** Theorem 3.2 shows that WS ≤ Ent(P) with equality iff P_ζ is degenerate, and Theorem 3.3 confirms that Gumbel-max and SynthID (m→∞) both achieve this bound. This gives an actionable, closed-form target for optimization.

- **Pareto frontier derivation.** Lemma 3.1 shows that speculative sampling is the optimal kernel for any fixed (Q_ζ, P_ζ), cleanly decoupling the optimization over kernels from the optimization over decoders. The explicit convex formulation in Eq. (10) for linearly watermarked classes makes the trade-off curve concretely computable.

- **Provably optimal Algorithm 1.** Theorem 4.1 proves three properties simultaneously: (a) unbiasedness, (b) maximum SSE = 1 − TV(Q, P), and (c) maximum WS = Ent(P). This directly overturns the binary impossibility of Hu & Huang (2024) under the new quantitative measure and is a non-trivial result with clearly stated premises.

- **Empirical validation on two model families.** Figure 2 shows AATPS of Algorithm 1 matches standard speculative sampling (left panel), and TPR@FPR=1% improves materially over prior-based methods for both Gumbel-max (middle) and SynthID (right), with results on both Llama and Gemma pairs.

- **Practical detection design.** Section 4.2 gives concrete, implementable detectors (Ars-τ and Bayes-MLP) that leverage ζ^R to select the correct test statistic rather than probabilistically averaging, directly addressing the signal dilution problem in prior methods.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Trade-off curves illustrated on a single simulated (Q, P) pair.** Figure 1 and the supporting claim that "Google's class achieves higher watermark strength than Hu's at matched sampling efficiency, yet neither reaches the theoretical optimum" are derived from one simulated pair (details in Appendix C.1). Since the whole comparative point of Figure 1 (right panel) is to guide practical method selection, it is not evident whether the rank ordering of Hu's vs. Google's classes is robust across different model pairs or whether it depends on properties of the chosen simulation. The paper does validate Algorithm 1 on real model pairs in Section 5, but the trade-off curve comparisons themselves remain restricted to the single simulated scenario.

- **Conservative temperature choices with unclear generalization.** Section 5 explicitly states temperatures of 0.5 (Gumbel-max) and 0.7 (SynthID) are chosen "to make results more pronounced." Typical production LLM settings use temperatures closer to 1.0. Lower temperatures make distributions more peaked, increasing acceptance rates and amplifying the information content of ζ^R. Whether the detection improvement holds at temperature 1.0 — the realistic deployment scenario — is not addressed, leaving a gap between the stated practical motivation and the experimental evidence.

### Trivial
- The paper does not report how TPR degrades as the calibration set size for τ in Ars-τ decreases from the 1,000-sample setting used in experiments. This is a minor missing detail for practitioners, though unlikely to change the paper's conclusions.

---

## Nice-to-Haves

- **Vary (Q, P) pairs for Figure 1.** Adding trade-off curves computed from two or three representative pairs drawn from the Llama and Gemma settings (the same distributions used in Section 5) would directly test whether the comparative ranking of Hu's vs. Google's classes is robust. The mathematical machinery is already in place.

- **Temperature sensitivity plot.** A single figure showing TPR@FPR=1% vs. temperature (e.g., 0.5, 0.7, 1.0) for one watermark/model pair would significantly strengthen the claim of practical applicability without broadening the paper's scope.

- **Calibration set sensitivity for Ars-τ.** A brief ablation showing how TPR degrades as the validation set size decreases from 1,000 would be informative for practitioners who cannot easily generate large volumes of watermarked text.

- **Brief argument for tree-based extension.** The conclusion identifies tree-based speculative sampling (Miao et al., 2024; Cai et al., 2024) as future work. Even a brief paragraph arguing why the pseudorandom acceptance principle extends naturally to tree structures would add practical weight, given that tree-based methods are now widely used.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Connect WS maximization to detection efficiency analytically."** The paper explicitly addresses this in Remark 3.1 ("watermark strength is conceptually different from detection efficiency") and Sections 4.1–4.2, which explain both the theoretical maximum WS result and the practical detection improvement mechanism via ζ^R. The critic acknowledges "this is not a fatal weakness." The request for a formal log-likelihood ratio result quantifying the exact mutual information contribution of ζ^R is beyond the paper's stated scope and would constitute a separate theoretical contribution. Downgraded to Nice-to-Have.

- **Harsh critic: "The calibration of τ introduces a non-trivial data dependency."** The 1,000-sample calibration set is disclosed in Section 5. Criticizing the data dependency without showing it degrades performance is speculative. Retained only as a Trivial note.

- **Harsh critic: "Missing proofs" / "appendix deferred."** The Reproducibility Statement explicitly says "full proofs are provided in Appendix B and D." The parser strips appendix sections. Removed per hard rule.

- **Generic strength: "paper addresses an important problem."** Removed as non-specific. The substantive strengths retained above provide the concrete grounding.

---

## Novel Insights

The most genuinely novel insight is the observation that pseudorandomizing the acceptance decision — rather than the sampling decision — is the missing ingredient that reconciles maximum watermark strength with maximum speculative sampling efficiency. Prior work treated the acceptance coin as a source of irreducible randomness that weakens watermarking; this paper shows that replacing it with a pseudorandom variable converts the entire generation pipeline into a deterministic function of ζ, enabling the token to carry its maximum possible watermark signal (Ent(P)) while leaving the marginal acceptance probability unchanged. This coupling principle — that determinism in the generation mechanism is equivalent to maximum mutual information between token and pseudorandomness — is a clean and non-obvious structural insight that could inform future watermarking scheme design beyond the speculative sampling context.

---

## Suggestions

1. Report at least one trade-off curve computed from a real Llama or Gemma pair (not only a simulated distribution) to make the comparative claims in Figure 1 more robust.
2. Add a temperature sweep experiment (T = 0.5, 0.7, 1.0) for one model pair to address the practical deployment concern explicitly.
3. Add a one-paragraph discussion of how the pseudorandom acceptance principle would extend to tree-based speculative decoding in the conclusion or an appendix section.

---

## Evaluation on Core Axes

- **Originality:** High. The core idea — making the acceptance variable pseudorandom — is simple to state but its consequences (Theorem 4.1's triple guarantee) are non-trivial and not apparent from prior work.
- **Importance:** High. Watermarking and efficient inference are both practical priorities; a principled resolution of their trade-off has direct deployment relevance.
- **Claims well supported:** Mostly. The theoretical claims (Theorems 3.1–3.3, 4.1) are stated with clear assumptions and proofs provided. The empirical claims are supported for two model pairs. The main gap is the single-simulated-pair trade-off curves and the conservative temperature choices.
- **Soundness of experiments:** Good. Two model pairs, two datasets, clear baselines, confidence intervals reported.
- **Clarity of writing:** High. The problem setup, theoretical framework, algorithm, and experiments are logically organized and clearly connected.
- **Value to research community:** High. Directly resolves an open question (Hu & Huang, 2024 impossibility), provides a reusable framework, and delivers a practical algorithm with code.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>