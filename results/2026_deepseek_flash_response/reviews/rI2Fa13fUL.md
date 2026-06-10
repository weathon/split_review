## Summary

This paper introduces Generative Trajectory Policies (GTPs), a policy class for offline RL that learns the entire solution map of a continuous-time generative ODE. The paper presents a unified ODE framework connecting diffusion models, consistency models, consistency trajectory models, shortcut models, and mean flows as special cases of learning a flow map $\Phi(x_t, t, s)$. To make this paradigm practical, the authors propose two adaptations: (1) a closed-form score approximation $\tilde{f}(x_t, t) = (x_t - x)/t$ with an $O(h^p)$ error bound (Theorem 1) that replaces costly ODE solvers with direct perturbation, and (2) an advantage-weighted objective derived from KL-regularized optimization (Theorem 2). Empirical results on D4RL benchmarks show GTP achieves strong average scores, particularly on AntMaze (80.6 average, beating prior generative methods), with a perfect 100.0 on antmaze-umaze.

## Strengths

- **Unified ODE framework (Section 3).** The paper provides a clean parameterization (Eq. 3–4) and two complementary loss functions (Eq. 5–6) from which Consistency Models, CTMs, Shortcut Models, and Mean Flows emerge as special cases. Section 3.4 explicitly maps each prior model to components of this framework. This is a genuinely useful conceptual organization that helps clarify the design space for generative policies in RL.

- **Score approximation with theoretical and empirical support.** Theorem 1 provides a concrete $O(h^p)$ error bound for replacing the true score with the closed-form surrogate, and the ablation (Table 3) confirms this is not just theoretical: removing the approximation drops the score from 112.2 to 99.7 while increasing training time by 23%.

- **Striking AntMaze BC results.** In the pure-BC setting (Table 1), GTP-BC achieves an AntMaze average of 66.3 vs. the next-best generative baseline C-BC at 44.1 — a 50% improvement. The gaps on the hardest tasks are dramatic (antmaze-md: 85.0 vs. 31.6; antmaze-ld: 40.8 vs. 12.8). This is the single strongest piece of evidence that learning the full trajectory map provides a meaningful advantage.

- **Clean ablation study (Table 3).** The ablation directly isolates the contribution of each proposed technique: score approximation (112.2 vs. 99.7 without it) and advantage weighting (stable across seeds while the linear Q-term baseline diverges for typical hyperparameters). This is higher-quality evidence than many papers in this area provide.

- **Stable advantage-weighted objective.** The derivation from KL-regularized optimization (Theorem 2) is principled, and the practical implementation (Eq. 14 with normalized, truncated weights) is shown to be substantially more stable than the common linear Q-term alternative, which diverges for most settings.

## Weaknesses

### Major

- **Factually inaccurate claim about "several perfect scores" in the abstract and introduction.** The abstract states that GTP "achiev[es] perfect scores on several notoriously hard AntMaze tasks," and the introduction repeats this. However, of the six AntMaze tasks reported in Table 2, only **one** — antmaze-umaze (100.0) — is a perfect score. The remaining five range from 53.5 to 94.2, with three below 85. The word "several" is objectively incorrect for a single perfect score. This is not a matter of interpretation or scope; it is a factual mismatch between the paper's headline claims and its own reported data. At a top venue, such inaccuracy in the abstract is a significant concern, as it means a reader relying on the abstract forms a fundamentally inflated impression of the results. This must be corrected.

### Minor

- **"State-of-the-art" claim overstates mixed individual-task performance.** The paper claims GTP "sets a new state-of-the-art for generative policies" and "significantly outperforms prior generative policies." GTP does achieve the highest *average* scores (Gym: 89.0, AntMaze: 80.6), but per-task comparisons are mixed: C-AC beats GTP by 15 points on halfcheetah-medium (69.1 vs. 53.9) and 8 points on halfcheetah-medium-replay (58.7 vs. 50.8); QGPO beats GTP on antmaze-large-play (66.6 vs. 53.5). The claim that GTP "significantly outperforms" prior methods is not supported uniformly across tasks. Characterizing the results as *competitive with strong average performance, with particular strengths on AntMaze* would be more accurate.

- **No inference speed measurements despite the paper's central motivation.** The paper is explicitly motivated by resolving the "expressiveness vs. efficiency" trade-off. Yet no wall-clock inference time is reported anywhere. GTP uses 5 sampling steps (same as diffusion baselines), while consistency baselines use 2 steps. Without timing data, the efficiency claim is unsubstantiated. Only training time is reported (Table 3), which speaks to a different concern. Given that this is a core part of the paper's narrative, the omission is notable.

- **Theorem 2 is a well-known result presented without proper attribution.** The optimal solution to KL-regularized policy optimization ($\pi^*(a|s) \propto \pi_{\text{BC}}(a|s) \exp(\eta A(s,a))$) is a standard result established by prior work (e.g., Peng et al., 2019; Nair et al., 2020; Wang et al., 2023). Presenting this as a new theorem without explicitly noting it is a restatement of an existing result is misleading. The paper should cite prior work and describe it as "following prior work, we adopt..." rather than formalizing it as a new theorem.

### Trivial

None.

## Nice-to-Haves

- Report wall-clock inference time per batch for GTP vs. D-QL (5 steps) and C-AC (2 steps) to substantiate the efficiency claim that is central to the paper's motivation.
- Consider adding statistical significance testing (e.g., confidence intervals or paired comparisons) for the key benchmark results, especially where standard deviations overlap.
- Perform a sensitivity analysis of the temperature parameter $\eta$ and the truncation/normalization choices in Eq. (14) to understand how robust the advantage weighting scheme is.

## Removed Points

Points from the inputs that were filtered out per instructions:

- *"Unified framework is primarily a synthesis, not a novel theoretical contribution"* — Removed. The paper presents its unified perspective as a synthesis that reveals connections between existing methods, which is a legitimate contribution. The novel contributions are the RL-specific adaptations (score approximation + advantage weighting). A synthesis that clarifies a design space is standard practice in ML venues and does not need to be defended as a fundamentally new theory.

- *"Table 1 mixes BC and value-based methods"* — Removed. Including methods that leverage additional information (TD3+BC, DT) makes the comparison *harder* for GTP-BC. That GTP-BC outperforms them despite using only BC training strengthens, not weakens, the claim about GTP's expressiveness.

- *"Theorem 1's analysis is decoupled from the actual algorithm"* — Removed. Theorem 1 establishes that the surrogate $\tilde{f}$ is a good approximation of $f^*$ in the solver setting. The practical benefit (bypassing the solver) follows from the specific form of that surrogate, which admits an analytic ODE solution. The connection is sufficiently clear: Theorem 1 provides the justification, Remark 1 notes the computational consequence. This is a theoretical framing choice, not a decoupling.

- *"Missing baselines on AntMaze"* — Removed. The paper cannot control which baselines report results on which tasks. Missing entries are marked with "-".

- Formatting/style nitpicks and speculative reproducibility concerns removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations identify framing issues that are real but orthogonal to the paper's core technical contribution — the method itself is sound and the empirical results are meaningful.

## Suggestions

1. **Correct the abstract and introduction.** Replace "several" with "a" or "the" when referring to perfect AntMaze scores. A perfect 100.0 on antmaze-umaze is genuinely noteworthy and does not need inflation. The AntMaze average of 80.6 (best among generative methods) is a strong result on its own.

2. **Qualify the SOTA claim.** Explicitly note that GTP achieves the highest average scores but individual-task performance varies, with particular strengths on AntMaze and hopper tasks. This would make the contribution clearer and more credible.

3. **Add inference time measurements.** Report wall-clock inference time for GTP and baselines. This directly supports the expressiveness-efficiency narrative that motivates the paper.

4. **Attribute Theorem 2 properly.** Add a citation to prior work establishing the advantage-weighted objective result, and reframe it as "following prior work" rather than presenting it as a new theorem.

5. **Add visual analysis of AntMaze trajectories.** The AntMaze BC results (66.3 vs. 44.1) are the paper's most striking finding. A visualization of learned trajectories comparing GTP-BC vs. C-BC on AntMaze would deepen understanding of *why* learning the full trajectory map helps on long-horizon, sparse-reward tasks.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Consistency Models for RL (v8jdwkUNXb.md) | 5.0 (accept) | R1 | GTP has more technical novelty and stronger AntMaze results → GTP is clearly stronger |
| Diffusion Actor-Critic/DAC (ldVkAO09Km.md) | 6.5 (accept) | R1/R2 | DAC has cleaner theory and more consistent individual-task results → GTP is somewhat weaker |
| RTDiff (0FK6tzqV76.md) | 5.75 (accept) | R2 | GTP has more technical depth (unified framework, theory, ablation) → GTP is slightly stronger |
| LDCQ (tGQirjzddO.md) | 6.33 (accept) | R2 | Both have similar strengths (novel technique, strong AntMaze) and weaknesses (stretched claims) → GTP is comparable |
| CDE (4WM0OogPTx.md) | 6.75 (accept) | R2 | CDE has a cleaner theoretical contribution and stronger results across tasks → GTP is weaker |
| ATraDiff (Ng7OYC3PT8.md) | 4.6 (reject) | R1/R2 | Different setting (online RL), but GTP is clearly stronger |
| DyDiff (ayUh0A6LIJ.md) | 5.25 (reject) | R2 | GTP has stronger theory and results → GTP is stronger |
| CL-DiffPhyCon (PiHGrTTnvb.md) | 7.0 (accept) | R1 | Different domain (physics control) — not directly comparable |
| Value function diffusion (TeeyHEi25C.md) | 6.25 (reject) | R2 | Different framing, comparable quality of contributions |

**Round 1 bracket:** The paper sits between 5.0 and 6.5 — clearly stronger than the Consistency Models paper (5.0) but somewhat weaker than DAC (6.5).

**Round 2 narrowing:** The paper is comparable to LDCQ (6.33) and somewhat stronger than RTDiff (5.75). The main drag on the score is the factual overclaiming in the abstract and the missing inference speed measurements, which are tangible flaws at a top venue. The technical contribution (unified framework + score approximation + advantage weighting + clean ablation) is solid.

**Final score: 6.0.** This reflects a paper with genuine technical contributions and strong empirical results on key tasks, held back by overclaiming that should be corrected before publication.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>