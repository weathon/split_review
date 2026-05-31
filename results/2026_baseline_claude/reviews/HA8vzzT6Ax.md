---

## Summary

The paper revisits the trade-off between watermark strength and speculative sampling efficiency in LLM inference. It introduces a quantitative, continuous measure of watermark strength as the expected KL divergence between the watermarked and original token distributions (equivalently, mutual information I(w; ζ)), shows it governs the p-value decay rate during detection, and fully characterizes the Pareto frontier between watermark strength and acceptance rate for linearly-interpolated watermark classes. Crucially, it proposes a mechanism—pseudorandom draft-token acceptance—that resolves the trade-off: by replacing the truly-random acceptance coin flip with a pseudorandom one, the algorithm simultaneously achieves maximal watermark strength (Theorem 4.1c) and maximal speculative sampling efficiency (Theorem 4.1b), while preserving unbiasedness.

---

## Strengths

- **Crisp resolution of a prior impossibility result.** Hu & Huang (2024) proved an impossibility that was framed as fundamental. This paper shows the impossibility artifact stems from a binary, all-or-nothing definition of watermark strength. The fix—pseudorandom acceptance—is elegant and backed by three simultaneous guarantees in Theorem 4.1 (unbiasedness, max efficiency, max watermark strength), providing a genuine advance over the prior state of knowledge.

- **Well-motivated quantitative measure with operational semantics.** Defining WS(P_ζ) = E_ζ[D_KL(P_ζ ‖ P)] = I(w; ζ) is a natural choice from information theory. Theorem 3.1 gives it a direct operational interpretation: it governs the exponential decay rate of p-values, so a higher WS directly translates to needing fewer tokens for detection. This closes the conceptual loop between the measure and its detection-theoretic consequences.

- **Explicit Pareto curve characterization.** The reformulation in Definition 3.2 and Eq. (8)–(10) casts the trade-off as a concrete constrained optimization problem. For linearly-interpolated decoder families, the problem simplifies to a convex program (when S_target is degenerate), yielding explicit Pareto curves. Comparing Gumbel-max, SynthID, "Hu's class," and "Google's class" on a single plot (Fig. 1) provides a useful and previously unavailable picture of the achievable region.

- **Theorem 3.2 and 3.3 are clean and important.** Showing that maximum WS = Ent(P) is attained if and only if P_ζ is degenerate, and that both Gumbel-max and SynthID (m → ∞) achieve this bound, directly connects the popular practical schemes to the theoretical maximum, justifying their use in Algorithm 1.

- **Empirical validation is well-structured.** Experiments on two model pairs (Llama and Gemma), two datasets (EL15 and C4), two watermarking schemes, and K ∈ {2, 3, 4} provide a reasonable picture. The AATPS results confirm efficiency is preserved, and the TPR@FPR=1% curves confirm detectability improves, with confidence intervals and a meaningful oracle baseline.

---

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical guarantee (max WS) and the practical gain (detectability) are decoupled.** Theorem 4.1(c) proves maximal *watermark strength* (WS = Ent(P)), but the paper's Remark 3.1 and Section 4.2 explicitly acknowledge that WS ≠ detection efficiency. The detection improvements via Ars-τ and Bayes-MLP are empirically demonstrated but not theoretically grounded. The gap between these methods and the oracle in Fig. 2 is real and not explained theoretically. A reader might reasonably ask: does maximal WS *guarantee* any improvement in practical detectability over the baseline, or is this purely empirical? The answer is yes—there is a gap—and its source is the mismatch between WS and the practical detector's sub-optimality, which deserves more careful treatment.

2. **The Pareto curve analysis is limited to linearly interpolated decoder families.** The closed-form result in Eq. (10) only applies when S_target is degenerate (allowing the entropy constraint to reduce to a scalar threshold), and the family Q_draft × Q_target is parameterized by (θ, γ) ∈ [0,1]². For non-degenerate S_target, the entropy constraint is not convex and no closed form is given. The practical significance of the "linear class" is not clearly motivated—it is introduced as a mathematical convenience for visualization rather than as a class that practitioners would choose.

3. **Experimental evaluation scope.** The draft-target pairs (Llama-68M/7B, Gemma-2B/7B) represent only moderate-size gaps. The efficiency and detectability improvements could behave differently with very small or very large draft-target KL divergences. The claim of general applicability would benefit from at least one evaluation where the draft model is notably weaker relative to the target.

### Minor

1. **Repeated context masking interaction with pseudorandom acceptance is not analyzed.** Algorithm 1 mentions repeated context masking to maintain unbiasedness, but Theorem 4.1 is stated for a single token step ("focus on a single intermediate step") and assumes independence of ζ^D, ζ^T, ζ^R. How repeated context masking affects the joint statistics across tokens—especially for the detection tests—is not formally addressed.

2. **Calibration of τ in Ars-τ requires a validation set.** The threshold τ is grid-searched on 1,000 held-out watermarked texts. Sensitivity to calibration set size and composition is not reported. In a deployment scenario, this is a non-trivial operational requirement.

3. **Comparison with other watermark-efficiency approaches** (e.g., token-level batching or training-based acceleration) is absent, making it difficult to situate the practical improvement in a broader efficiency landscape.

### Trivial

- Notational inconsistency: Theorem 4.1 uses P'_ζ in the setup but P^t_ζ in the conclusions.
- The footnote 3 dismisses bonus-step tokens as "negligible in practice" without quantifying the impact.

---

## Nice-to-Haves

- A theoretical lower bound on the practical detectability improvement (relative to baselines) that follows from maximal WS would significantly strengthen the contribution by closing the gap between theory and practice.
- Extension or at least a discussion of how pseudorandom acceptance could be combined with tree-based speculative decoding (Miao et al. 2024, Cai et al. 2024), since these are the dominant practical variants.
- An analysis of robustness to edit attacks (Sadasivan et al. 2023) for the new mechanism versus baselines.

---

## Novel Insights

The paper's deepest insight is that the "impossibility" of simultaneously achieving maximal watermark strength and sampling efficiency is an artifact of randomness in the acceptance decision, not a fundamental incompatibility. By identifying that maximal watermark strength requires the entire generation process to be a deterministic function of pseudorandom inputs (Theorem 3.2), and observing that standard speculative sampling injects independent Bernoulli randomness into the acceptance step that breaks this determinism, the fix becomes obvious: replace the Bernoulli coin with a pseudorandom one. The resulting algorithm does not modify the marginal acceptance probability at all (maintaining efficiency), yet fully restores the pseudorandom-determinism required for maximal watermark strength. This unification of speculative sampling and watermarking under the lens of pseudorandomness is genuinely novel and likely applicable beyond the specific schemes studied here.

---

## Suggestions

- Provide a theorem or proposition quantifying how much of the oracle detectability gap can be attributed to the imprecision in estimating the acceptance threshold (min{1, P_w/Q_w} in Ars-τ), so that the empirical gap has a rigorous explanation.
- Clarify whether the Pareto curve optimality (red star in Fig. 1) is truly achievable or only a theoretical upper bound, and if achievable, provide the corresponding algorithm.
- Explicitly state and prove whether Algorithm 1's unbiasedness holds under repeated context masking across multiple token positions (not just at a single step), to ensure Theorem 4.1 applies in the multi-token setting.
- Report detection results at FPR thresholds other than 1% (e.g., 5%, 0.1%) to demonstrate robustness of the improvement across the ROC curve.

---

## Score and Decision

The paper makes a clean and principled contribution: it introduces a well-motivated quantitative measure, proves it governs detection difficulty, resolves a prior impossibility result with an elegant algorithm, and validates the approach empirically. The theoretical results are sound and the writing is clear. The main limitation is the decoupling between the theoretical guarantee (maximal watermark strength) and the empirical payoff (detection improvement), which relies on heuristic detectors. The scope of the Pareto curve analysis is also somewhat narrow. Nonetheless, the contribution is solid and the core results are novel and useful.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>