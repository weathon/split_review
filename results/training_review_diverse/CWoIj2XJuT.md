Now I have all the information needed to produce the consolidated review.

## Summary

This paper extends Diffusion Schrödinger Bridges (DSB) to the *unbalanced* setting where the total mass of the distribution changes over time (via killing/birth), by deriving time-reversal formulas for diffusions with killing and birth terms. The authors propose two algorithms — UDSB-TD (theoretically grounded but unstable in high dimensions) and UDSB-F (a more practical heuristic variant) — and evaluate them on synthetic dynamics and a 50-dimensional single-cell drug-response dataset.

## Strengths

- **Novel time-reversal formulas for diffusions with killing and birth** (Propositions 1–2 and surrounding text): The paper derives that time-reversing a killing diffusion yields a birth diffusion and vice versa, with explicit expressions relating killing/birth rates to score terms and mass ratios. This is a clean theoretical extension of classical DSB time-reversal (Anderson/Haussmann) to the cemetery-state formulation and is the foundation for any unbalanced dynamic SB solver.

- **Principled extension of IPF to the unbalanced setting via the one-point compactification** (Section 4, Proposition 3): The paper builds on Chen et al. (2022) to show that the unbalanced SB solution and its IPF iterates can be characterized by two systems of forward/backward Kolmogorov equations on $\hat{\mathbb{R}}^d$, and makes the duality structure explicit. This provides a rigorous basis for algorithmic development.

- **Two algorithmic schemes with honest discussion of trade-offs**: UDSB-TD (temporal-difference loss to estimate log-potentials) is theoretically grounded but acknowledged to be unstable; UDSB-F replaces the problematic log-potential estimation with a direct loss on the killing-rate ratio, sacrificing theoretical guarantees for practical stability. The paper explicitly states "we do not prove the theoretical validity of this new procedure" (line 607) and "minimizing this loss does not ensure that $g_{\zeta,t}$ is the optimal update" (line 622) — this intellectual honesty is a strength.

- **Shadow trajectory sampling** (Section 4, end): A practical scheme for sampling backward birth processes by reusing forward trajectories and Bernoulli acceptance, making the computationally challenging birth-process sampling tractable without integrating over the full state space.

## Weaknesses

### Major

- **The main experimental algorithm (UDSB-F) is a heuristic, and its only validation against the theoretically grounded UDSB-TD is deferred to the appendix.** The paper acknowledges this limitation honestly, but the practical consequence is that all main-text experiments — synthetic and cellular — rest on an algorithm whose approximation quality is unverified in the main manuscript. While the appendix exists in the original submission, the central empirical claim should be supported by at least one in-text comparison showing UDSB-F tracks UDSB-TD (e.g., on the 2D synthetic task where UDSB-TD is tractable).

- **Synthetic experiments are purely qualitative.** The paper shows that balanced SB fails and UDSB succeeds on the toy task, but reports zero quantitative metrics (no Wasserstein distance between true and predicted live trajectories, no error in terminal mass, no comparison of killing/birth rates to ground truth). The claim that the method "recovers the true evolution law" (Fig. 2 caption) is supported only by visual inspection. Quantitative metrics would significantly strengthen this evidence.

- **Cellular results show modest improvement without statistical rigor.** In Table 1, the MMD improvement over baseline is 1.86e-2 → 1.75e-2 (~6%), and the entropic Wasserstein distance improves 6.23 → 6.11 (~2%). Standard deviations overlap between conditions, and no hypothesis tests, confidence intervals, or effect sizes are reported. With only 10 runs, the significance of the claimed improvement is unclear. The ablation ("Ours, no deaths/births") performs identically to baseline, which is internally consistent but also means the entire improvement comes from a small margin.

- **Missing comparison to relevant unbalanced baselines.** The only baseline is the balanced DSB of Chen et al. (2021). The paper does not compare to static unbalanced OT methods (e.g., unbalanced Sinkhorn; Chizat et al. 2018) or the "reweighted" SB approach of Chen et al. (2022) (which the paper distinguishes but does not benchmark against). Such comparisons would help isolate whether the improvement comes from dynamic modeling, the unbalanced formulation, or both.

### Minor

- **The choice of death/birth priors in the synthetic experiments is not discussed.** The gray rectangles are hand-drawn by the user. Is this intended as known prior knowledge (e.g., a biologist's knowledge of toxic regions), or should these be learned? The paper does not address how such priors are set in practice.

- **The step-size $\gamma$ in shadow trajectory sampling is mentioned but its practical choice is not discussed.** Since the Lie-Trotter-Kato splitting requires "small-enough step-sizes" for correctness (Section 4), a practical guideline or default value should be provided.

- **No computational complexity analysis or wall-time comparison.** The paper is silent on how UDSB-F scales with dimension, number of IPF iterations, or number of particles — relevant for reproducibility and practical adoption.

- **The theoretical presentation in the main text is sketchy.** Propositions are labeled "informal" and assumptions are summarized as "mild assumptions" without specification. While full rigor is deferred to the appendix (which is standard and fine), the main text would benefit from stating even one or two key conditions (e.g., smoothness of $b,k$, integrability of $p_t$).

### Trivial

- None that survive filtering.

## Nice-to-Haves

- A comparison to the "reweighted" SB formulation from Chen et al. (2022) would help contextualize what the additional complexity of UDSB buys over existing approaches.
- A brief discussion of how users would specify death/birth priors in a real application (e.g., biological priors on known drug toxicity regions) would strengthen the practical narrative.
- Reporting the Wasserstein-2 distance between true and predicted live trajectories in the synthetic experiment would turn qualitative visual evidence into quantitative support.

## Removed Points

- **Criticism that UDSB-F validation is "relegated to the appendix" (Severity: Structural/Fatal):** The paper *explicitly* says empirical validation comparing UDSB-F to UDSB-TD is in the appendix. The parser strips the appendix from all submissions. In the original, this comparison exists. The core concern (heuristic unvalidated in main text) is kept as a Major weakness, but the "structural" severity is unwarranted given the appendix's existence and the paper's honest acknowledgment of limitations.

- **"The relationship to partial OT is mentioned but not pursued":** Scope-creep demand for expanding the paper beyond its stated focus. Removed.

- **"Step-size $\gamma$ not discussed" treated as a major flaw:** Downgraded to Minor — it is a practical implementation detail, not a structural issue.

- **Claim that the intermediate-mass test in synthetic experiments is "unclear":** The paper clearly states it is testing whether the method can match different amounts of mass loss—a straightforward sanity check on the method's interpolation behavior. The critic's confusion is not a paper error.

- **"The paper does not explain how the generator is derived from the SDE with killing":** The paper references the Feynman-Kac approach in the appendix, which is standard practice. Removed as an appendix-deferral nitpick.

- **Strength Finder's claim of "Thorough synthetic validation":** Downgraded from "thorough" — the synthetic experiments are entirely qualitative, which is a weakness, not a strength at the claimed level.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent picture: the theoretical framework (time-reversal formulas + unbalanced IPF) is a genuine advance, but the experimental validation is too weak relative to the claims made, and the reliance on an unvalidated heuristic algorithm for all main results is a significant concern.

## Suggestions

1. **Add one quantitative experiment in the main text** comparing UDSB-F to UDSB-TD on the 2D synthetic task, showing the two algorithms yield indistinguishable trajectories and killing/birth rates. This would validate the heuristic where theory cannot.
2. **Report quantitative metrics for the synthetic experiments**: Wasserstein-2 distance between true and learned live trajectories, and error in terminal mass. Even one number per scenario would substantially strengthen the evidence.
3. **Add statistical significance testing** (e.g., paired bootstrap or permutation test) for the cellular MMD/W_ε improvements, or acknowledge that the difference is within noise. If the sample size is limited, increase runs or use a more sensitive metric.
4. **Explicitly state key theoretical assumptions** in one sentence each for Propositions 1 and 2 (e.g., smoothness of $b,k$, existence of densities, integrability of $p_t$) rather than only "mild assumptions."
5. **Discuss the choice of death/birth priors** — are they user-specified or learned? If user-specified, provide practical guidance.

## Score and Decision

**Originality (7/10):** The time-reversal formulas for killing/birth processes are genuinely novel and nontrivial. The extension of DSB to unbalanced marginals has been called for in the literature. However, the heuristic UDSB-F is a practical adaptation of standard ideas rather than a radical departure.

**Importance (8/10):** Unbalanced SB is relevant for biology (cell death/proliferation), epidemiology, and any domain with population changes. The problem is well-motivated and timely.

**Claims well-supported (4/10):** The theoretical claims are sound but presented informally. The central experimental claims are weakly supported — qualitative synthetic results, modest improvement on cellular data without statistical significance, and reliance on a heuristic algorithm whose validation is appendix-only.

**Soundness (6/10):** The theory (time-reversal formulas, IPF derivation) appears correct under standard assumptions. The experiments are reasonably designed but lack statistical rigor and quantitative depth.

**Clarity (7/10):** Well-motivated, clearly written, with good notation. The honest discussion of limitations is a strength.

**Value to community (7/10):** The framework opens up a clear research direction for unbalanced dynamic SB. The algorithms, while heuristic, provide a practical starting point.

The paper presents a genuinely novel theoretical extension of DSB to unbalanced marginals. The time-reversal formulas and the IPF derivation are solid contributions. However, the experimental validation is the weakest aspect: the main algorithm (UDSB-F) is a heuristic and its only theoretical validation is appendix-only; the synthetic results are purely qualitative; and the cellular results show a modest improvement without statistical significance. The paper would be accepted in a venue where theoretical novelty is the primary criterion, but in a top-tier venue demanding strong empirical support, the evidence falls short. 

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>