Now I have all the calibration data I need. Let me write the final consolidated review.

## Round 1 Bracket

Based on Round 1, the paper clearly sits above the 2–4.5 range (strong/weak rejects) and above the 4.75–5.75 range (borderline/weak accept) — it is more novel, better evaluated, and better written than those papers. Papers in the 6.0–7.5 band (e.g., Proto Successor Measure at 6.75, Bridging State and History at 6.75) provide the closest match.

## Round 2 Narrowing

Round 2 compared against π2vec (5.25), Distributional Analogue to SR (5.75), and Reasoning with Latent Diffusion (6.33). TD-JEPA is clearly stronger than π2vec (more ambitious problem, deeper theory, broader evaluation) and Distributional Analogue (more practical, more thorough). It is comparable to or slightly stronger than Reasoning with Latent Diffusion (6.33), which was accepted with scores 6, 8, 5.

---

## Summary

TD-JEPA introduces a temporal-difference latent-predictive loss that enables learning representations predictive of long-term dynamics across multiple policies from offline, reward-free data. The method trains explicit state and task encoders, a policy-conditioned multi-step predictor, and parameterized policies — all in latent space — enabling zero-shot optimization of any reward function at test time. The paper provides novel theoretical analysis connecting the latent-predictive loss to successor measure approximation via gradient matching, and empirically evaluates across 13 datasets, 65 tasks, and two observation modalities.

## Strengths

1. **TD-based off-policy latent prediction (Eq. 7, 9) is a genuine algorithmic innovation.** Prior latent-predictive methods were limited to one-step prediction, single-task, or on-policy data. The paper explicitly identifies that the MC-JEPA loss "cannot be estimated on off-policy data" (line 88) and derives a TD variant that "only requires sampling one-step transitions and actions from the given policies" (lines 90–92). This is a concrete, well-motivated contribution that directly enables the paper's main claim.

2. **Gradient matching theorems (Th. 1, 3) formally connect latent-predictive losses to successor measure approximation.** The paper proves that gradients of the MC-JEPA and TD-JEPA losses match those of explicit successor measure approximation losses. As noted, this result generalizes and implies prior guarantees (Tang et al., 2023; Voelcker et al., 2024; Khetarpal et al., 2025; Lawson et al., 2025), providing a rigorous foundation for why the learned predictor can be used for zero-shot policy evaluation and optimization.

3. **Strong empirical results on pixel-based zero-shot RL** — the setting the paper correctly identifies as "the most challenging setting for unsupervised RL so far" (line 36). On DMC_RGB, TD-JEPA achieves 628.8 ± 5.5, substantially outperforming all seven baselines (next best: BYOL-γ* at 582.4 ± 9.8). The probability-of-improvement analysis (Fig. 2) confirms TD-JEPA is consistently among the top algorithms across diverse domains.

4. **Non-collapse guarantee (Theorem 2) for the more complex TD latent-prediction setting.** This result is non-trivial because TD latent-prediction is "doubly latent-predictive" — the target involves a bootstrapped version of the predictor itself (line 159) — making it strictly harder than the one-step case studied in prior work.

5. **Asymmetric state/task encoder design with empirical justification.** The distinction between φ (state) and ψ (task) encoders is well-motivated (lines 94–96) and empirically validated: Fig. 3 (right) shows the asymmetric variant improves performance more often than not relative to the shared-encoder alternative.

## Weaknesses

### Major

1. **Theory-operates under strong assumptions that are materially violated in practice.** Theorems 1–3 rely on orthonormal representations (A1), uniform state distribution (A2), and symmetric transition kernels P^{π_z} (A3). The symmetric-kernel assumption is the most consequential — it requires that for every policy, the probability of transitioning from s to s' equals that of transitioning from s' to s, which is rarely satisfied in real MDPs. While the paper mentions that "these assumptions can be relaxed" (line 157, citing App. C), the practical algorithm uses nonlinear function approximation, target networks, EMA updates, and orthonormality regularization — components that fall entirely outside the theoretical framework. The connection between the idealized linear analysis and the practical algorithm's behavior is largely asserted rather than demonstrated.

2. **The empirical advantage over BYOL-γ* — the closest competitor — is narrower in some settings than the headline suggests.** On OGBench_RGB, BYOL-γ* (41.58) numerically edges out TD-JEPA (41.34). On DMC (proprioception), the advantage is modest (661.2 vs 645.4). Since BYOL-γ* is an on-policy MC method that was retrofitted for zero-shot RL (as the paper acknowledges in lines 196–197: "the version we evaluate is a novel instantiation in a successor-feature framework"), the fact that it competes so closely despite being repurposed raises the question of whether the core advantage is TD-JEPA's specific TD formulation or simply that any latent-predictive representation works well for pixels. The paper's own Fig. 3 (left) partially addresses this by showing TD-JEPA outperforming BYOL and BYOL-γ on aggregate, but the pattern is not consistent across all settings.

### Minor

3. **The "off-policy" advantage is asserted but not directly demonstrated via a controlled ablation.** The claim that the TD formulation enables learning from offline, off-policy data (a key differentiator from "one-step" and "on-policy" methods) is central to the paper. However, there is no direct TD-vs-MC ablation holding other factors constant. The comparison against BYOL and BYOL-γ* in Fig. 3 (left) is confounded by multiple differences: behavior-policy vs policy-conditional, one-step vs multi-step, not just the TD vs MC distinction. A cleaner ablation (e.g., TD-JEPA trained via the MC loss using a learned dynamics model) would substantially strengthen the paper's core causal claim.

4. **The fine-tuning experiment (Fig. 4) selects tasks via cherry-picking.** The paper reports results for "the task in which the gap between online and zero-shot algorithms is largest" (line 289). This selects the most favorable task per domain rather than reporting average performance across tasks, making it difficult to assess whether the observed sample-efficiency gains are general or specific to particular tasks.

5. **Several failure cases are not discussed.** On antmaze-me (RGB), TD-JEPA scores 0.20 ± 0.20 (essentially zero) while BYOL-γ* gets 3.20 and FB gets 1.80. On cube-single (proprioception), TD-JEPA scores 34.2 vs HILP at 74.2. A brief discussion of when TD-JEPA struggles would improve the paper's honesty and practical utility.

6. **Theorem 2's non-collapse guarantee** relies on a continuous-time relaxation where optimal predictors are recomputed at each step before updating representations — this does not directly apply to the practical setting where encoders and predictors are learned jointly at the same rate. The result is a useful theoretical existence proof but provides limited guidance for practice.

### Trivial

None.

## Nice-to-Haves

- A direct TD-vs-MC ablation (e.g., comparing TD-JEPA trained via the TD loss vs the MC loss where on-policy samples are obtained via a learned dynamics model or importance sampling) would directly isolate the benefit of the TD formulation.
- Analysis of representation specialization (e.g., CKA similarity or mutual information between φ(s) and ψ(s)) would substantiate the claim that separate encoders capture different information.
- Reporting fine-tuning results averaged across all tasks (rather than the "largest gap" task) would provide a more faithful evaluation.

## Removed Points

- **BC regularization criticism** — The paper states this is "detailed in App. E.6" (line 249). Since the appendix was stripped by the parser, this is not a valid criticism of the submitted manuscript.
- **BYOL-γ* MC estimation methodology question** — The paper explicitly notes BYOL-γ* is "a novel instantiation in a successor-feature framework" (line 196) with implementation details in App. E (stripped by parser). The question of how it was adapted for offline data is valid but the paper does reference the appendix for these details.
- **Generic "evaluation lacks rigor" / "baselines may be unfair" framing** — These were removed as they lacked concrete anchors in the paper.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that TD-JEPA's contribution is better characterized as "TD-based latent-prediction enables practical off-policy multi-task representation learning" rather than "TD-based latent-prediction is demonstrably superior to MC-based latent-prediction." The theory provides a clean connection to successor measures, but under assumptions that bracket the hardest aspects of the practical setting. The empirical evaluation convincingly shows TD-JEPA is competitive or better across diverse settings, particularly on pixels, but does not include the controlled ablation that would isolate whether the TD formulation or the policy-conditioned multi-step prediction is the primary driver. This suggests the paper's contribution is strongest as a complete system demonstration (algorithm + theory + evaluation) rather than as a focused empirical test of a specific hypothesis about TD vs MC latent prediction. The asymmetric encoder design is a subtle but potentially impactful contribution that deserves more analysis than it receives.

## Suggestions

- Add a controlled TD-vs-MC ablation (Section 3) to directly isolate the benefit of the TD formulation, even if it requires a learned dynamics model for MC rollouts.
- Replace or supplement the "largest gap" fine-tuning results (Fig. 4) with averages across all tasks per domain.
- Add a brief discussion of failure cases (antmaze-me RGB, cube-single proprioception) to improve the paper's balance.
- Clarify in the main text that BYOL-γ* was adapted as an on-policy method to the offline setting, and discuss any methodological implications for the comparison.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Reward as Observation | .../473sH8qki8.md | 2.00 | R1 | Much weaker — poor evaluation, limited scope |
| Projected Subnetworks | .../WM5G2NWSYC.md | 2.00 | R1 | Much weaker — different problem, limited experiments |
| Non-Parameterized Randomization | .../fvTaoyH96Z.md | 2.33 | R1 | Much weaker — theoretical but limited evaluation |
| Latent Trajectory | .../ve5Omkxc13.md | 3.50 | R1 | Weaker — incremental contribution, limited experiments |
| Temporal-Difference VCL | .../0wQCSXJbwt.md | 4.25 | R1 | Weaker — narrower scope, less thorough |
| π2vec | .../o5Bqa4o5Mi.md | 5.25 | R2 | Weaker — policy evaluation only, less comprehensive |
| Distributional Analogue to SR | .../OMwD6pGYB4.md | 5.75 | R2 | Slightly weaker — good theory but limited evaluation |
| Conservative World Models | .../X5qi6fnnw7.md | 4.75 | R1 | Weaker — incremental contribution (CQL→FB) |
| Proto Successor Measure | .../s9SVlWOcLt.md | 6.75 | R1 | Comparable — stronger theory but much weaker experiments |
| Bridging State and History | .../ms0VgzSGF2.md | 6.75 | R1 | Comparable — theory paper with mixed reviews |
| Reasoning with Latent Diffusion | .../tGQirjzddO.md | 6.33 | R2 | Comparable — similar novelty and evaluation depth |
| Episodic Novelty Through TD | .../I7DeajDEx7.md | 6.75 | R1 | Comparable — different problem, similar quality |
| Generalized TD Learning | .../dxI1HLatWw.md | 6.25 | R1 | Weaker — TD for supervised learning, tangential |

**Round 1 bracket:** 5.5–7.0 (between the strong anchors in the 5–6 range and the 6.75–8 range).

**Round 2 narrowing:** Compared against π2vec (5.25), Distributional Analogue to SR (5.75), and Reasoning with Latent Diffusion (6.33). TD-JEPA is clearly stronger than the first two (more ambitious, more comprehensive) and comparable to the third (similar novelty, similar evaluation thoroughness). Given the hint about potential under-estimation of high-quality papers (>5), and comparing to the 6.33–6.75 anchors, the paper sits at the upper end of this range. The weaknesses (strong theory assumptions, narrow empirical win profile, missing ablation) prevent it from reaching the 7.5+ tier but are bounded and not paper-sinking.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>