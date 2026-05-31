Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes Stochastic Gradient Discrete Langevin Dynamics (SGDLD), extending stochastic-gradient-based MCMC to discrete spaces. It introduces two techniques: a **caching scheme** that reuses mini-batch estimates when the chain stays in the same state (effectively growing the effective batch size without extra computation), and a **Polyak-style step size** that normalizes simulation time by the state-dependent jump rate to control variance. Empirical results span synthetic validation (Gaussian Bernoulli), Bayesian logistic regression, stochastic facility location, approximate computing, and prompt tuning.

---

## Strengths

- **Caching scheme for bias reduction (well-supported).** The paper identifies that naive stochastic gradient in discrete spaces is biased because expectation does not commute with the locally balanced weight function (Equation 11, lines 115–119). The caching technique (Equation 12) accumulates mini-batch estimates across non-jump steps. Figure 2 provides direct empirical evidence: SGDLD's total variation decreases as step size shrinks, while the no-cache variant (SGDLD-noC) plateaus or worsens. This is a clean, practical idea.

- **Polyak step size for variance control (well-supported).** Figure 1 shows that jump rates across mini-batches can differ by ~30 orders of magnitude. The Polyak normalization (Equation 14) adapts the simulation time per state. Figure 3 shows SGDLD mixes faster and has lower estimation error than SGDLD-noP, confirming the adaptive step size stabilizes the process.

- **Sample efficiency in expensive black-box settings.** In the approximate computing problem (Section 6.4, Table 2), SGDLD matches or beats state-of-the-art learning-based methods (CON, AFF) while requiring only 10k evaluations of the objective, compared to >100 million evaluations for training data collection by the baselines (lines 322–323). This is a compelling practical advantage.

- **Versatility across diverse discrete problems.** SGDLD is demonstrated on three real applications — stochastic integer programming (Table 1), black-box optimization (Table 2), and prompt tuning (Table 3) — with consistent gains over ablated variants and several strong baselines (Gurobi, SLS, CR).

---

## Weaknesses

### Fatal
None.

### Major

- **Proposition 4.1 is stated without proof.** The central theoretical claim — asymptotic unbiasedness of the cached estimator as ε → 0 — is asserted in a single sentence (line 183) with no proof or even a proof sketch provided anywhere in the paper. The paper does not contain the word "proof" or "appendix," so this is not a case of a stripped appendix. For a paper whose core contribution is a new stochastic MCMC algorithm, an unsubstantiated theoretical guarantee is a significant gap. The conditions under which the claim holds (bounded likelihood ratio, interaction with cache-emptying upon jumps, effect of the nonlinear weight function g on plug-in estimation) are not discussed.

    *Verification:* The paper states Proposition 4.1 on line 183 and says "With some mild assumptions" (line 181) but offers no proof. No reference to a proof location is given.

- **Computational and memory costs of caching and Polyak step size are not analyzed.** Algorithm 1 (line 2) requires computing ψ(z, ξ) for *every neighbor* z ∈ N(x_t) at each step. For Bayesian variable selection with d=1000, this means computing ψ for 1000 neighbors per step; for prompt tuning with a vocabulary of ~50k tokens, the cost scales accordingly. The paper claims "negligible computational overhead" (line 14) without any complexity analysis (time per step, memory per cache entry, cache size in practice). Similarly, the exact Z(x) in the Polyak step (Equation 14) requires summing over all neighbors; the paper mentions a gradient approximation following Grathwohl et al. (2021) but does not define it, analyze its bias or cost, or explain why it is appropriate. Without this analysis, claims of practicality are incomplete.

    *Verification:* Algorithm 1 line 2 requires ψ for all z ∈ N(x_t). No complexity analysis or memory usage is reported. The gradient approximation for Z(x) is mentioned only in passing (line 206).

- **Prompt tuning experimental comparison is too narrow.** The only existing method compared is the continuous relaxation (CR) method from Wen et al. (2023). Well-known discrete prompt tuning methods such as AutoPrompt, PEZ, and TEMPERA are not included. While the paper shows SGDLD outperforms CR and its own no-cache ablation, a single non-ablation baseline does not convincingly establish effectiveness in this application area.

    *Verification:* Section 6.5, lines 344: "We compare SGDLD with the continuous relaxation (CR) method in Wen et al. (2023) and SGDLD-noC." Only these two comparators.

### Minor

- **Cost calibration in Bayesian logistic regression lacks transparency.** The paper calibrates 320 stochastic updates = 2 DLMC updates (line 275) but does not report the dataset size M or mini-batch size B. The reader cannot verify whether the 320:2 ratio is a fair reflection of relative cost. Moreover, SGDLD's caching and neighbor-sum steps make each stochastic step *more* expensive than a naive mini-batch step, a gap the calibration does not account for.

    *Verification:* Line 275 states the calibration ratio. No M or B values are given in the paper.

- **SGDLD-noP failure mode is not explained.** The paper omits SGDLD-noP from facility location, approximate computing, and prompt tuning because "it can not generate reasonable solutions" (line 230). No explanation is given for what "not reasonable" means — divergence, constant output, numerical overflow? This is important for understanding the role of the Polyak step size.

    *Verification:* Lines 230–231: "We omitted the results for SGDLD-noP in three applications as it can not generate reasonable solutions."

- **Polyak schedule parameters (h_t, h*) are not specified.** The paper defines a schedule and threshold but does not report how these were chosen or what values were used in any experiment.

    *Verification:* Lines 208–209 mention the schedule and threshold h* but give no concrete values.

- **Neighborhood definition for prompt tuning is not specified.** The paper never defines what constitutes a neighbor in the prompt space (token replacement? swap? insertion?). This is required for reproducibility.

    *Verification:* Section 6.5 does not define the neighborhood structure for text prompts.

### Trivial
None.

---

## Nice-to-Haves

- A more detailed analysis of the gradient approximation for Z(x) (bias, cost, impact on stationary distribution) would strengthen the paper, though the empirical evidence suggests the approximation is acceptable in practice.
- Confidence intervals or standard errors for the Bayesian logistic regression results (Figure 3) would improve reproducibility assessment.

---

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- *"The bounded likelihood ratio assumption is violated in the paper's own experiments."* — This is speculative. The paper does not provide enough detail to verify or refute this claim. Without concrete evidence from the paper, it is not a valid criticism.
- *"Gaussian Bernoulli experiment is too small (d=4)."* — The purpose of this experiment is correctness validation, not scalability demonstration. The criticism is generic and does not harm the paper's core claims.
- *"Missing comparison to pseudo-marginal MCMC."* — The paper states "We conducted extra experiments to show the fast mixing of SGDLD and demonstrate its advantage compared to more baselines, such as pseudo marginal MCMC" (line 279), with a stripped footnote marker. Per the rules, stripped appendix/footnote content is not a valid weakness.
- *"Overclaiming 'first practical method'."* — The paper positions itself against Zhang et al. (2022) and explains why their assumption (unbiased estimator of the rate matrix) is generally unrealistic. The claim is defensible given this positioning.
- *"The remark about Hamiltonian Monte Carlo is cryptic and unsupported."* — This is a footnote (indicated by ".1.") that was stripped by the parser.
- *"Missing variance/confidence intervals for main results."* — Tables 1 and 3 report standard deviations, and Figure 2 reports mean and standard deviation. This criticism is not universally applicable.
- *"Naive stochastic gradient analysis only uses one task/seed in Figure 1."* — The paper shows this for one illustrative task; the magnitude issue it demonstrates is mathematically derived, not purely empirical.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Provide a proof (or at minimum a proof sketch) for Proposition 4.1** in the main paper or a clearly referenced appendix. Discuss the conditions under which the bounded-ratio assumption holds and how cache-emptying upon jumps affects the guarantee.

2. **Analyze the computational and memory complexity** of the algorithm: per-step time as O(|N(x)| · B) for caching and O(|N(x)|) for the Polyak sum (or its approximation). Report neighborhood sizes, cache sizes, and wall-clock times for each experiment.

3. **Add at least one additional discrete prompt tuning baseline** (e.g., AutoPrompt or PEZ) to strengthen the prompt tuning evaluation.

4. **Report dataset size M and batch size B** for the Bayesian logistic regression experiment so the 320:2 cost calibration can be verified.

5. **Document the failure mode of SGDLD-noP** and report its numerical results even if poor, with an explanation.

6. **Specify the Polyak schedule parameters** (h_t and h*) used in each experiment.

7. **Define the neighborhood structure** for the prompt tuning application.

---

## Score and Decision

The paper proposes a genuinely clever idea — caching stochastic gradient estimates in discrete Langevin dynamics — and demonstrates empirical promise across diverse tasks, with particularly strong results in facility location and approximate computing. However, the central theoretical claim (Proposition 4.1) is stated without proof, the computational costs of the key components are unanalyzed despite nontrivial overhead, and the prompt tuning evaluation relies on a single non-ablation baseline. These gaps prevent the paper from fully establishing its contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>