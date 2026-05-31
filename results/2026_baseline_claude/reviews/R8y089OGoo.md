## Summary
DIPOLE (Dichotomous diffusion Policy improvement) proposes a novel RL framework for training diffusion-based policies. The approach begins by identifying limitations of the standard KL-regularized optimal policy – specifically the exponential weighting that causes training instability and learning inefficiency. By replacing the reference policy with a sigmoid-weighted, "greedified" version, the authors show that the optimal policy can be decomposed into two dichotomous policies: π⁺ (focused on reward maximization, weighted by σ(βG)) and π⁻ (focused on reward minimization, weighted by 1 − σ(βG)). Both policies have bounded training losses, and sampling from the optimal policy reduces to a linear combination of their scores – structurally identical to classifier-free guidance (CFG). The method is evaluated on ExORL, OGBench (offline + offline-to-online), and a large 1B-parameter VLA for autonomous driving on NAVSIM.

---

## Strengths

- **Theoretically principled and elegant decomposition.** The derivation in Theorem 1 is mathematically correct and clean. The greedified KL objective (Eq. 5) yields an optimal policy that decomposes naturally into π⁺ and π⁻ with strictly bounded sigmoid weights, directly resolving the exponential-explosion issue in standard AWR-style weighted regression. The score-level combination in Eq. 10 is analytically exact, not an approximation.

- **Tight connection to classifier-free guidance.** The parallel between DIPOLE's sampling formula ε̃ = (1+ω)ε⁺ − ω ε⁻ and CFG is not superficial; it arises from first principles and gives practitioners an intuitive, well-understood knob (ω) to control greediness at inference time. This both validates the design and makes deployment simple.

- **Comprehensive and multi-scale evaluation.** The paper covers 39 tasks in offline RL (ExORL + OGBench), 4 tasks in offline-to-online RL, and a 1B-parameter VLA on NAVSIM. The NAVSIM result (PDMS 88.3 → 94.8 on navtest split, vs. 89.0 for DPPO) demonstrates that the method scales to large-scale real-world settings without instability. Reporting 8-seed averages throughout adds reliability.

- **Better data utilization than prior approaches.** By assigning high weight to high-return samples for π⁺ and high weight to low-return samples for π⁻, the method fully exploits both ends of the data spectrum. This directly addresses the "dominated by high-return samples" failure mode of exp-weighted regression and the "all samples positive weight" issue noted in existing literature.

- **Stronger than CFGRL with theoretical grounding.** CFGRL uses a hard indicator I[A ≥ 0] for positive samples and treats all data uniformly as negative, limiting greediness and lacking a derivation from an RL objective. DIPOLE replaces both with smooth, advantage-proportional weights and derives them from a proper greedified KL objective.

---

## Weaknesses

### Fatal
None.

### Major

1. **Fairness of the ExORL comparison.** The headline DIPOLE results in Table 1 include rejection sampling, while CFGRL and FQL do not use it. The ablation variant "DIPOLE w/o rs" reveals a substantially weaker picture against CFGRL: on Cheetah-run (194 vs. 216), Cheetah-run-backward (227 vs. 262), and Quadruped-run (560 vs. 571), CFGRL is competitive or better. Across all nine ExORL tasks, DIPOLE w/o rs is not clearly superior to CFGRL, yet DIPOLE (with rejection sampling) is presented as the primary result for that comparison. This conflates the contribution of the RL algorithm with inference-time search and weakens the headline claim.

2. **Notable performance gap on ExORL Jaco tasks.** Even the full DIPOLE (with rejection sampling) scores 117 and 110 on Jaco reach-top-right/left, versus IFQL's 193/181 and FQL's 224/222 — roughly half the performance. This is a substantial shortfall in an important manipulation domain and is not discussed or explained in the main text.

### Minor

1. **Double-model computational cost.** Training two diffusion models (ε⁺ and ε⁻) doubles parameter count and training compute for the standard RL settings. The paper justifies this for the VLA case via LoRA, but the cost in standard settings (ExORL, OGBench) is unaddressed.

2. **The greedified objective in Eq. 5 is not independently motivated.** The choice to regularize against μ·σ(βG)/Z is clearly designed to produce the desired decomposition, but no intuitive or principled reason is given for why this particular form of value-aware reference policy is preferred before revealing the elegant consequence. A brief forward-looking justification would strengthen the presentation.

3. **Offline-to-online competitiveness is mixed.** In cube-double, FQL achieves 40→92 vs. DIPOLE's 41→89; in scene, multiple methods reach 100. The advantage of DIPOLE in online fine-tuning is most pronounced in humanoidmaze-m; across the four tasks, the gap is meaningful but not uniformly large.

### Trivial
- The note "Due to space limit, more discussion on limitations and future direction can be found in Appendix F" follows conventional paper writing and is understandable.

---

## Nice-to-Haves

- An analysis of how sensitive performance is to β and ω across tasks, even a brief one in the main paper, would help readers apply the method.
- A wall-clock or FLOPs comparison between DIPOLE and single-model baselines (e.g., FQL, CFGRL) would quantify the cost of the two-model design.
- A clearer explanation of the Jaco task gap (or an experiment addressing it) would strengthen the completeness of the evaluation.

---

## Novel Insights

DIPOLE's core insight — that the exponentially-weighted optimal policy of KL-regularized RL can be *re-derived* by choosing a sigmoid-weighted value-aware reference, yielding a decomposition into two bounded, complementary weighted regressions whose score functions combine exactly like classifier-free guidance — is genuinely novel and valuable. Prior work using weighted regression (AWR, IQL variants, CFGRL) did not recognize this connection, and the resulting algorithm is both more principled and more stable than existing alternatives. The revelation that CFG is not merely an engineering trick but has a natural correspondence to an RL policy decomposition is likely to influence future work at the intersection of diffusion models and RL fine-tuning.

---

## Suggestions

- Report ExORL tables both with and without rejection sampling for all baselines (or at minimum, clearly delineate which methods use it), so the algorithmic contribution is directly isolated.
- Investigate and discuss the Jaco task underperformance: is it related to the dimensionality, sparse rewards, or the reference policy quality?
- Provide a paragraph (or table row) quantifying the training-time overhead of the two-model design vs. single-model baselines.
- Consider an experiment varying ω to show the inference-time controllability more concretely (e.g., a performance-vs-ω sweep), as this is one of the advertised advantages.

---

## Score and Decision

The paper makes a clean theoretical contribution, resolves a real practical problem in diffusion-policy RL training, and validates the approach convincingly at scale including on a 1B-parameter VLA. The ExORL fairness issue and Jaco gap are the most notable weaknesses, but neither invalidates the core claims — the OGBench results are comprehensive and not subject to the same caveat. Overall this is a strong submission that adds both theoretical clarity and practical value to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>