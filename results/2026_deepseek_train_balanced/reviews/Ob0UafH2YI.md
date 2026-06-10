Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes two federated learning algorithms (FedDRO and DS-FedDRO) for non-convex compositional optimization with a distributed compositional function — a setting more general than prior work where the compositional function is local to each agent. The paper contributes a negative result (Theorem 4.1) proving that vanilla FedAvg fails for this problem class, and develops two algorithms with theoretical convergence guarantees: FedDRO (O(ε^{-3/2}) communication, requiring extra low-dimensional communication of y-embeddings) and DS-FedDRO (O(ε^{-1}) communication, using two-sided learning rates to avoid extra communication). Experiments on CIFAR-ST and Adult datasets demonstrate empirical performance, though with significant gaps relative to the theoretical claims.

## Strengths

- **First formal negative result establishing vanilla FedAvg's failure for federated CO (Theorem 4.1).** The paper constructs an explicit counterexample satisfying standard assumptions (3.2, 3.3, 3.4) where FedAvg does not converge for any fixed number of local updates I>1 and any step-size below a constant. This is a rigorous proof, not just a claim of difficulty.

- **Novel problem setting with distributed compositional functions that is strictly more general than prior work.** Remark 2.1 clearly distinguishes the paper's formulation (g = (1/K) Σ g_k(x) distributed across agents) from prior works (Huang et al., Gao et al.) where the compositional function is local to each agent. The paper correctly notes that data heterogeneity of the inner problem also affects convergence in this setting.

- **DS-FedDRO achieves O(ε⁻¹) communication complexity, matching the best-known rate for standard (non-compositional) FL (Corollary 5.3).** This is a significant theoretical advance: prior federated CO algorithms had worse communication complexity, and DS-FedDRO attains this without the extra per-iteration y-communication required by FedDRO.

- **Both algorithms achieve linear speedup with the number of clients (Corollaries 4.4 and 5.3), claimed as the first for federated CO.** Each client requires O(K⁻¹ε⁻²) samples.

- **Hybrid momentum-based estimator (Section 4.2, Equation 8) avoids accuracy-dependent large batch gradients** required by prior works (Haddadpour et al., Huang et al., Guo et al.), directly addressing challenge [C3].

- **Empirical validation on Adult dataset shows both algorithms outperform GCIVR** (Figure 3), the only prior distributed algorithm that handles compositional + non-compositional objectives.

## Weaknesses

### Major

- **DS-FedDRO's headline O(ε⁻¹) communication complexity depends on Assumption 5.1 (bounded heterogeneity of function values ‖g_k(x)−g(x)‖² ≤ Δ_g²), which is strong and may be violated in the paper's own motivating DRO applications.** For the KL-Divergence DRO example (Section 2.1), g(x) = (1/m) Σ exp(ℓ(x;ζ_i)/λ). With heterogeneous client data distributions — the defining feature of FL — the function values g_k(x) can differ by orders of magnitude. The paper acknowledges this is "strong" (line 264) and lists it as a drawback of DS-FedDRO (lines 284–285), but does not justify why it is reasonable for the DRO problems that motivate the work. This is a structural issue: the best theoretical result rests on an assumption that undercuts the paper's own motivation. The paper does not provide empirical evidence that DS-FedDRO works well even when Assumption 5.1 is violated.

- **Communication complexity — a central theoretical contribution — is never measured empirically.** The paper claims O(ε^{-3/2}) vs O(ε^{-1}) communication as a key advantage, yet the experiments contain no plots with communication rounds (or total bits transmitted) on the x-axis against accuracy or gradient norm on the y-axis. This is a fundamental disconnect: the paper's strongest selling point is left entirely unvalidated. Without this measurement, the claim that DS-FedDRO's better communication rate "matches the best-known communication complexity even for standard FL problems" (line 282) is purely theoretical.

### Minor

- **Experiments use only 8 clients with no variation in K.** Linear speedup with K is a central theoretical claim (Corollaries 4.4 and 5.3: each client requires O(K⁻¹ε⁻²) samples), but no experiments vary the number of clients (e.g., K ∈ {2, 4, 8, 16, 32}) to validate this. This limits the empirical support for a core theoretical prediction.

- **Results are reported only qualitatively, without numerical values or variance.** The discussion uses phrases like "superior training and comparable test accuracy" (line 303) with no numbers, and the paper notes "All results are averaged over 5 independent runs" (line 301) but shows no error bars, standard deviations, or significance tests. The figures are unrendered images in the extracted text, so the actual numerical content cannot be assessed.

- **The connection between theoretical local-update constraints and empirical choices is not discussed.** Theorem 4.3 requires I ≤ O(T^{1/4}/K^{3/4}) for FedDRO; Corollary 5.3 requires I = O(1/ε) for DS-FedDRO. The paper tests I values up to 60 (CIFAR) and 96 (Adult) but does not state whether these satisfy the theoretical constraints or discuss robustness when constraints are violated.

- **Figure reference mismatch.** The text references "Figure 1" for the CIFAR experiments (line 303), but the extracted figures are labeled Figure 2/3. This appears to be either a parser artifact or a figure numbering error.

### Trivial

- DS-FedDRO's server learning rates are fixed at 1.3 and 1.4 with no sensitivity analysis or explanation for these particular values (line 301). For a new algorithm with two-sided learning rates, some ablation or discussion of how these values were chosen would be helpful.

## Nice-to-Haves

- An experiment demonstrating the FedAvg failure (Theorem 4.1) on a simple synthetic problem would make the negative result tangible and strengthen the motivation.
- A comparison on CIFAR tasks against a distributed CO baseline (e.g., a simplified variant of the algorithms from Huang et al./Gao et al. adapted to the distributed compositional setting) would broaden the empirical support. The current comparison is only against centralized baselines on these tasks.

## Removed Points

*These points were flagged by reviewers but are removed or filtered per the filtering guidelines. Treat with caution; they do not reflect genuine weaknesses.*

1. **Claim that Theorem 4.1's narrative overclaims relative to the proof (existence result treated as categorical failure).** The paper proves "there exist functions... for which FedAvg does not converge" (Theorem 4.1) and concludes "vanilla FedAvg is not suitable for solving federated CO problems" (line 205). This is standard language in optimization theory — proving a counterexample establishes that an algorithm "fails" for the problem class. No overclaiming.
2. **Criticism that the FedAvg failure experiment is missing (Theorem 4.1 is an empirical claim needing validation).** Theorem 4.1 is a mathematical proof, not an empirical claim. It does not require experimental validation.
3. **Criticism that baselines on CIFAR tasks sidestep comparison with relevant prior works.** The paper is transparent about using centralized baselines on CIFAR (line 293: "we compare FedDRO and DS-FedDRO with popular centralized baselines"). The relevant distributed CO baseline (GCIVR) is compared on the Adult dataset. Theoretical comparison to other methods (Huang et al., Gao et al., Guo et al.) is provided in Table 1 for communication complexity — the claims about those methods are theoretical, not empirical.
4. **Complaints about unrendered images, formatting artifacts, and missing appendix content.** These are PDF parser issues, not author errors.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface genuinely novel insights. The cross-check between Assumption 5.1 and the DRO examples is a point worth the authors' attention but follows directly from the paper's own presentation.

## Suggestions

1. **Measure communication complexity empirically.** Add plots with communication rounds on the x-axis and test accuracy (or gradient norm) on the y-axis for FedDRO, DS-FedDRO, and GCIVR on at least one task. This would directly substantiate the paper's core theoretical claim.
2. **Validate Assumption 5.1 or relax it.** Either prove that Assumption 5.1 holds for the DRO examples under reasonable conditions (e.g., bounded losses, Lipschitzness), or provide empirical evidence that DS-FedDRO's advantage persists even when the assumption is violated.
3. **Vary the number of clients.** Test with K ∈ {2, 4, 8, 16} to provide at least suggestive evidence for the linear speedup claim.
4. **Report numerical results with variance.** Provide tables with accuracy means and standard deviations over the 5 runs, so that claims of "superior" performance can be assessed quantitatively.
5. **Discuss the relationship between theoretical local-update constraints and empirical choices.** State whether the tested I values satisfy the theoretical constraints (I ≤ O(T^{1/4}/K^{3/4}) for FedDRO) and comment on robustness.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>