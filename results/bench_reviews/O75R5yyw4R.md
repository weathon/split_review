## Summary

This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses reward-guided noising–denoising transitions within a Multiple-Try Metropolis (MTM) framework to iteratively refine intermediate states during the denoising trajectory. The method is evaluated across three discrete diffusion backbones (MDLM, LLaDA-8B, MaskGIT) on diverse language and image reward tasks, consistently outperforming prior baselines (FK, SVDD, SoP, BoN) under equal compute budgets.

## Strengths

- **Novel and well-motivated algorithmic contribution.** The use of a noising–denoising kernel as the MTM proposal within discrete diffusion sampling is a genuinely new idea. Designing the transition as forward-noising then backward-denoising to enable exploration while preserving the MTM framework's detailed-balance structure is creative and practically motivated (Section 3.1, Eq. 2).

- **Strong, broad empirical results.** IterRef consistently outperforms strong baselines (FK, SVDD, SoP, BoN) across three model backbones (MDLM, LLaDA-8B, MaskGIT) and five reward types (Toxicity, CoLA, Sentiment, Perplexity, CLIPScore). On MDLM with Toxicity reward, IterRef reaches at 4T NFEs what FK needs 32T NFEs to achieve — roughly an 8× speedup in scaling (Section 4.2, Figure 2a). Gains are most pronounced at low compute budgets, an important practical regime.

- **Persuasive ablation on iteration vs. particles.** Table 3 (and Figure 4) cleanly demonstrates that increasing refinement iterations _k_ consistently yields larger gains than increasing parallel candidates _N_ (e.g., on LLaDA-8B, k=8/N=4 achieves Toxicity 54.0 and CoLA 85.3 vs. k=1/N=32 at 3.3 and 8.7). This validates the core "iterative refinement" philosophy and distinguishes the method from simple particle-broadening approaches.

- **Valuable insight into discrete diffusion dynamics.** The effective-timestep analysis (Section 4.4, Table 2) reveals that IterRef is far more effective at later denoising stages (e.g., 0.1T yields 37.6% Toxicity gain vs. 7.0% at 0.9T), which is the opposite pattern from continuous diffusion. This provides actionable guidance for where to concentrate compute.

- **Practical cost-management strategies.** The use of the effective timestep set _U_, the balancing function choice (λ=1) that eliminates backward auxiliary proposals, and pool reuse are well-motivated optimizations (Section 3.3) that make the method computationally viable.

## Weaknesses

### Fatal
None.

### Major
- **Gap between convergence claim and algorithm scope.** Proposition 1 proves convergence to the optimal intermediate distribution _p*(xt)_ under stated assumptions. However, the abstract and introduction (lines 14–15, 52, 105–106) describe this as "convergence to the target/reward-aligned distribution" without qualification — which in the paper's own problem setup (line 189) is _p*(x0)_. The algorithm follows MTM refinement with an unguided denoising step _xt−1 ∼ pθ(·|xt)_ (Algorithm 2, line 10), which is not the optimal transition kernel (Eq. 1). The paper does not establish that composing MTM-converged intermediate distributions with standard denoising yields _p*(x0)_, nor does it discuss this gap. This is not fatal — the empirical results are strong and Proposition 1 itself is correctly scoped — but the paper should explicitly acknowledge the gap between the local (per-timestep) convergence guarantee and the global (final-sample) objective.

### Minor
- **The reversible-kernel assumption is an approximation, not an identity.** The symmetry of λ (Appendix D.4) and consequently the simplified acceptance ratio (Eq. 3) rely on the assumption that _q_ and _pθ_ form a reversible Markov kernel (Proposition 1). In practice, _pθ_ is a learned approximation to the time-reversal of _q_, so detailed balance holds only approximately. The paper is transparent about making this assumption, and it is a standard kind of idealization in diffusion theory. Still, the practical impact of the approximation error on the MTM chain's stationary distribution warrants brief discussion.

- **NFE metric conflates model scales.** The paper's own complexity analysis (Section 3.3, lines 444–448) acknowledges that aggregating large diffusion-model calls and small reward-model calls into a single NFE is problematic — the paper itself recommends reporting them separately. The main experiments nonetheless use combined NFE. This is mitigated by the wall-clock analysis in Appendix C.4, which shows that IterRef's practical runtime is competitive at higher budgets, though slower at low budgets on LLaDA-8B.

### Trivial
- The characterization of prior methods in the abstract ("assume the current state is already aligned with the reward distribution") is slightly imprecise. Methods like SVDD and FK use importance sampling/resampling to approximate the optimal intermediate distribution — they do not literally "assume" alignment, though they are single-pass rather than iterative.

## Nice-to-Haves
- A control experiment replacing the unguided denoising step after MTM refinement with a guided transition (e.g., importance sampling as in SVDD) would help quantify how much the unguided step limits alignment to _p*(x0)_.
- A formal discussion or bound on the error propagation from the unguided denoising step to the final distribution.
- Sensitivity analysis of the acceptance ratio to errors in the approximate intermediate reward _r(xt)_.

## Removed Points
These points were flagged by the reviewers but are not substantiated or are parser artifacts. Treat them with caution.

- **"The derivation rests on an unverified and likely incorrect assumption" (harsh critic).** The paper explicitly states the reversibility assumption in Proposition 1. It is a standard and reasonable idealization for well-trained diffusion models. This is an acknowledged assumption, not a hidden error. Kept as a minor weakness about approximation rather than incorrectness.

- **"Missing experiments: evaluation of how closely the final distribution matches p*(x0)" (harsh critic).** The paper includes diversity metrics (Appendix C.1, Table 6) showing IterRef maintains or improves diversity, and a human evaluation (Appendix C.1, Table 5) confirming benefit to human preference. A formal KL divergence to p*(x0) would be ideal but is computationally infeasible for these model scales and is not standard in this literature. Moved to Nice-to-Haves.

- **"The method proposed does not sample from p*(x0)" (harsh critic).** This is true of essentially all practical reward-guidance methods for diffusion — no existing baseline (FK, SVDD, SMC) provably samples from p*(x0) either at finite particle counts. The harsh critic's framing of this as a fatal structural error is disproportionate. Proposition 1 correctly scopes the guarantee to p*(xt), and the overall algorithm inherits the same asymptotic limitations as all particle-based methods. Kept as a major weakness about claim precision, not a fatal error.

- **"Comparisons that isolate the effect of the denoising step" and "Integrate MTM into a proper particle-based framework" (harsh critic).** These are reasonable suggestions for future work but demand the paper address problems outside its stated scope. The paper's core contribution is the MTM refinement of intermediate states; hybridizing with SMC is explicitly mentioned as possible (lines 381–383). Moved to Nice-to-Haves.

- **"Overclaim the convergence" (harsh critic).** Partially valid — the abstract/intro language could be more precise. Kept as a major weakness about precision, but the harsh critic's claim that this invalidates the entire theoretical backbone is an overstatement. Proposition 1 is correctly scoped and technically valid.

- **"Formal analysis of the bias introduced by the base denoising step" (harsh critic).** This is a useful theoretical extension but not required to validate the paper's core empirical claims. Moved to Nice-to-Haves.

- **"Sensitivity to the reward model's quality" (harsh critic).** A reasonable ablation to suggest but not a weakness of the current contribution. The intermediate reward approximation is standard practice in this literature (used by SVDD, FK, etc.).

- **Strength Finder claim about "principled convergence guarantee."** The guarantee is correctly scoped to p*(xt) at the intermediate level and stated with assumptions. This is a genuine theoretical contribution, but the strength finder's framing glosses over the gap to p*(x0). Retained as a strength with appropriate qualification.

## Novel Insights
The effective-timestep analysis (Section 4.4) provides a genuinely novel observation about discrete diffusion dynamics: refinement is most effective at late denoising stages, which is the opposite of continuous diffusion where early steps dominate content. This finding, combined with the _k_ vs. _N_ ablation showing iteration trumps breadth, suggests that discrete diffusion sampling is more amenable to in-place correction than continuous diffusion, likely because the discrete state space creates "lock-in" effects where early token decisions cannot be easily overridden by later steps.

## Suggestions
- Revise the abstract and introduction to be precise: the convergence guarantee applies to the intermediate distribution p*(xt) at each refined timestep, not to the final sample distribution p*(x0). Use language like "convergence to the reward-aligned intermediate distribution" or "converges to the optimal distribution at each refined timestep."
- Add a brief discussion (one paragraph) in Section 3 or the limitations section about the gap between per-timestep MTM convergence and the overall denoising trajectory, acknowledging that the unguided denoising step may introduce bias relative to the optimal transition.
- In the NFE reporting for future work, consider showing generative-model calls and reward-model calls as separate axes as the paper itself recommends, or at minimum note this limitation more prominently in the main text.

## Score and Decision

**Originality:** High. The combination of MTM with a noising–denoising proposal kernel for discrete diffusion refinement is novel and well-motivated. The effective-timestep analysis also yields original insights.

**Importance:** The problem of test-time scaling for discrete diffusion is timely and important as these models gain traction. The method addresses a genuine gap.

**Claims supported:** Strongly supported by experiments. The theoretical claim about convergence to p*(x0) is slightly overbroad but Proposition 1 itself is correctly scoped and valid.

**Soundness:** Generally sound. The reversible-kernel assumption is idealizing but standard. Experiments are thorough.

**Clarity:** Good overall. The abstract could be more precise about the scope of the convergence claim.

**Value to community:** High. The method is practical, effective, and the insights about discrete diffusion dynamics are useful beyond this specific method.

### Anchor comparison:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/7wbrFQvfdH.md` (SMC for discrete diffusion) | 6.00 | Comparable: both have novel methodology + strong experiments. IterRef has broader model coverage and a clean ablation story, but the SMC paper's theory-to-practice gap is smaller. |
| `/home/wg25r/review_agent/human_reviews_2026/DBlMothexq.md` (MH discrete diffusion) | 3.50 | IterRef is substantially stronger: cleaner theory, broader experiments, proper baselines, better ablations. |
| `/home/wg25r/review_agent/human_reviews_2026/N1RYhOg6ib.md` (Discrete guidance matching) | 4.50 | IterRef is stronger empirically and has a cleaner algorithmic contribution, though both have theoretical approximations. |
| `/home/wg25r/review_agent/human_reviews_2026/QqgGE3mvrF.md` (Langevin refinement) | 2.50 | IterRef is far stronger in every dimension: experiments, baselines, theoretical grounding, scope. |
| `/home/wg25r/review_agent/human_reviews_2026/wbNXoqcaSi.md` (Inference-time scaling for flow matching) | 3.50 | IterRef has much stronger empirical validation and a more principled algorithmic framework. |
| `/home/wg25r/review_agent/human_reviews_2026/l01eG3Qikl.md` (DriftLite) | 6.00 | Both are strong inference-time scaling methods. DriftLite has stronger theory, IterRef has broader empirical coverage. Comparable. |

IterRef sits comfortably at the 6.0 level — comparable to the accepted SMC discrete-diffusion paper (7wbrFQvfdH) and DriftLite (l01eG3Qikl), with strong empirical results that outweigh the minor theoretical imprecision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>