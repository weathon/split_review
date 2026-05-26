Now I have a comprehensive comparison set. Let me write the final review.

## Summary

This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transition kernels to iteratively refine intermediate states toward a reward-aligned distribution. The authors design a specific balancing function that yields uniform proposal weights and a simple acceptance probability β = min(1, exp((r(x′)−r(x))/α)), making the refinement computationally efficient. Experiments across two language diffusion backbones (MDLM, LLaDA-8B) and one image backbone (MaskGIT) with four reward functions show that IterRef consistently outperforms existing guidance methods (FK, SVDD, SoP, BoN), with substantial gains at low compute budgets.

## Strengths

1. **Well-motivated algorithmic design with clean instantiation.** The use of Multiple-Try Metropolis with a noising-denoising kernel is a principled adaptation of the predictor-corrector paradigm to discrete state spaces. The specific choice of balancing function (Eq. 2) yields a remarkably simple acceptance rule that depends only on the reward difference, avoiding expensive importance-weight computations. This is a non-trivial and elegant theoretical contribution.

2. **Theoretical grounding for the refinement loop.** Proposition 1 shows that the MTM kernel satisfies detailed balance at a fixed timestep and converges asymptotically to the optimal reward-aligned distribution p*(x_t). While the guarantee is per-timestep, it provides formal justification that prior heuristic methods lack.

3. **Iteration outperforms parallel particles.** Table 3 and Figure 4 provide clean empirical evidence that, under fixed total compute, increasing refinement iterations k yields larger gains than increasing the number of proposals N. This finding directly supports the core thesis that iterative refinement, not just parallel search, drives the method's effectiveness. Notably, this analysis is internal to IterRef and not subject to the NFE conflation concern.

4. **Cross-modality validation.** The method is evaluated on two language diffusion models (MDLM, LLaDA-8B) and one image diffusion model (MaskGIT), with consistent improvements. The MaskGIT CLIPScore results (Table 1) show meaningful gains (e.g., 35.8 vs. 34.8 at NFE=16) that are robust across the cost budget.

5. **Practical insights about discrete diffusion dynamics.** The effective timestep analysis (Table 2) reveals that later denoising stages (0.1T) are more influential for reward alignment in discrete diffusion, contrasting with continuous diffusion where early steps dominate. This is a useful finding for the community.

## Weaknesses

### Major

1. **Headline quantitative claims are built on a conflated compute metric the paper itself acknowledges as problematic.** The paper measures computational cost using NFEs that treat generative model calls and reward model calls as equivalent. The paper explicitly states this "may obscure meaningful differences" and that "it is preferable to report generative-model calls and reward-model calls separately" (Section 3.3). Yet the main results (Figure 2), the "8× faster" claim (Section 4.2, Figure 1b), and the "2× improvement" statement (Section 1) are all presented using this conflated metric. Because IterRef's acceptance mechanism samples proposals uniformly (avoiding reward evaluation for proposal selection) while baselines like FK evaluate the reward on every particle, the NFE comparison may systematically favor IterRef by allowing it more generative passes within the same declared budget. The paper promises a wall-clock time analysis in Appendix C.4, but this is insufficient to rescue the main text's narrative when the central quantitative evidence is presented in a potentially misleading form. The authors should either (a) report generative-model calls and reward-model calls separately for all figures, or (b) demonstrate that the wall-clock results replicate the same trends in the main paper.

### Minor

2. **Transition kernel hyperparameter s is underspecified.** The kernel K(x_t, x′_t) = Σ q(x_s|x_t)p_θ(x′_t|x_s) requires choosing s (a noisier timestep) that controls perturbation strength and computational cost per proposal. The paper never specifies how s is chosen, scheduled, or annealed across timesteps. This detail is essential for reproducibility, since s directly determines the exploration range and the generative cost (s−t steps per proposal).

3. **Effective timestep set U for the main results (Figure 2) is not disclosed.** Section 4.4 shows that performance varies significantly with the choice of U (e.g., 0.1T vs. evenly spaced vs. other configurations). The paper does not state which timesteps were selected for the primary comparisons in Figure 2, making it impossible to rule out that U was tuned per task to favor IterRef while baselines used a default schedule.

4. **Proposition 1's scope is limited to a single fixed timestep.** The convergence guarantee covers the MTM refinement loop at a given t, not the full sequential denoising trajectory. The paper does not analyze whether steering x_t toward p*(x_t) at one step harms the validity of subsequent denoising steps, since p_θ(x_{t-1}|x_t) was trained on the original data manifold. While this does not invalidate the theoretical contribution, the paper's framing (e.g., "converges to the target distribution") should be more precise about what is and is not proven.

5. **The CoLA/LLaDA failure case is acknowledged but not explored.** The paper notes that BoN outperforms IterRef on CoLA with LLaDA-8B, attributing this to LLaDA already generating well-formed text. This is a plausible explanation but is presented without supporting evidence (e.g., distributional analysis or ablation). It limits the claimed generality of the method, and the paper does not discuss what properties of a task/backbone predict when IterRef will be beneficial vs. neutral or harmful.

### Trivial

6. The paper states "3 seed, 15 controllable prompts" in the language setup (Section 4.1), which appears to be a typo (likely "3 seeds").

## Nice-to-Haves

- A pure-search ablation (generate N random proposals, pick the best, no acceptance step) would isolate the value of the Metropolis rejection mechanism from the noising-denoising kernel.
- Analysis of whether modifying x_t affects the manifold assumptions of p_θ(x_{t-1}|x_t), with synthetic or diagnostic experiments for distribution shift.
- Reporting both generative-model calls and reward-model calls separately for all main experiments would directly address the NFE concern.

## Removed Points

The following points from the harsh critic were removed per the filtering rules:

1. **"The paper cannot be accepted in its current form" / "invalidates the experimental evidence as presented"** — This overstates the severity. The paper acknowledges the NFE issue and provides wall-clock analysis in the appendix (which was stripped from this review process). The criticism assumes the worst-case interpretation without verifying the appendix's contents.

2. **"The paper implicitly assumes this distribution shift is always beneficial"** — The paper does not claim the refinement is universally beneficial; it reports one case (CoLA/LLaDA) where it is less effective than BoN. The critic's characterization is not supported by the paper's text.

3. **Missing related works** — Removed per instruction: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."

4. **Formatting/style nitpicks** — Removed per instruction.

5. **Reproducibility nitpicks about undisclosed hyperparameters beyond s and U** — Removed as trivial or addressed in the paper (e.g., α is mentioned as a hyperparameter, N and k are swept).

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective that the paper's own analysis does not already capture.

## Suggestions

1. **Disentangle the compute metric in all main figures.** Present the results of Figure 2 with separate x-axes for generative-model calls and total wall-clock time (or provide both NFE and a secondary metric). Without this, readers cannot assess whether IterRef's advantage is algorithmic or an artifact of the accounting.

2. **Specify s and U explicitly.** Provide the choice of s (or its schedule) and the exact effective timestep set U used for the main results. Even a brief sentence in the experimental setup would resolve the reproducibility gap.

3. **Add an ablation isolating the rejection mechanism.** Compare IterRef against a version that generates N proposals and selects the one with highest reward without the Metropolis acceptance step. This would directly measure the value of the rejection mechanism vs. the noising-denoising kernel alone.

4. **Clarify the scope of Proposition 1** in the main text (e.g., "converges to p*(x_t) at a single timestep t, conditioned on the backward kernel being well-specified") to avoid overclaiming.

## Score and Decision

**Calibration Anchors (all rounds)**

| Anchor | Score | Round/Query | Comparison |
|--------|-------|-------------|-----------|
| W4djmqKZC6 (Pixel-Aware DDPM) | 3.00 | R1-topic-low | Rejected; much weaker technical contribution than IterRef |
| QKqWnNkwPL (Self-distillation DDPM) | 3.00 | R1-topic-low | Rejected; limited scope vs. IterRef |
| RFJGFrMvYj (TCIG) | 1.50 | R1-topic-low | Rejected; very weak paper, not comparable |
| Ombm8S40zN (DDPP Steering MDDM) | 6.25 | R1-topic-mid | Accepted; more comprehensive framework (training-based), stronger eval rigor, IterRef is weaker |
| 4hFT4rfG40 (Plug-and-Play Masked) | 3.75 | R1-topic-mid | Rejected; limited experiments, no baselines. IterRef is stronger |
| 2fgzf8u5fP (SVDD Derivative-Free) | 3.80 | R1-topic-mid | Rejected; unfair baseline comparison (alpha issue). IterRef has similar but better-addressed fairness concern |
| peNgxpbdxB (Scalable Discrete Samplers) | 6.00 | R1-topic-mid | Accepted; stronger theory, narrower scope. IterRef comparable in quality |
| MJNywBdSDy (Think While You Generate) | 5.75 | R2-mid | Accepted; similar discrete diffusion contribution with missing details. IterRef slightly weaker on evaluation |
| D7PQ54l5Q1 (DPMC MCMC + diffusion) | 4.75 | R1-weakness | Rejected; limited novelty, computational concerns. IterRef has stronger novelty |
| Hpu3KIX8Am (Dreamguider) | 4.00 | R2-mid | Rejected; limited novelty. IterRef is more novel |
| pzpWBbnwiJ (Universal Guidance) | 5.25 | R2-mid | Accepted; similar evaluation gaps. IterRef has stronger novelty but similar eval concerns |
| hnrB5YHoYu (Fairness T2I) | 4.33 | R3-mid | Accepted; different domain, weaker comparison |

**Round-1 bracket:** [3.5, 6.0]. The low-band anchors (score ~3.0) were rejected for weak technical contribution or insufficient validation — IterRef does not share those failures. The mid-band anchors (3.5–6.25) include both accepts and rejects; IterRef's closest topical neighbor (DDPP, 6.25) was accepted with stronger training-based eval, while SVDD (3.80) was rejected for unfair comparison (similar in kind to IterRef's NFE issue). 

**What the low-band anchors failed at:** Weak technical novelty and insufficient validation. IterRef does not share those failures — its MTM formulation is novel and the experimental breadth is adequate.

**Round-2 narrowing:** Within [4.0, 5.5]. Comparing to "Think While You Generate" (5.75, accepted) and "Universal Guidance" (5.25, accepted), IterRef has comparable contribution strength but a more conspicuous evaluation concern. Compared to SVDD (3.80, rejected), IterRef handles its comparison-fairness issue better (acknowledgment + appendix analysis). This places IterRef in the borderline range around 5.0.

**Final score: 5.0.** The paper presents a genuinely novel and well-motivated algorithm (MTM for discrete diffusion refinement) with broad experimental validation. However, the headline quantitative claims rest on a conflated compute metric that the paper itself flags as problematic, and two key hyperparameters (s and U) are underspecified. These issues are addressable but prevent a stronger score in the current version. The paper sits at the boundary; the authors should be given the opportunity to resolve the NFE concern and clarify the missing specifications.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>