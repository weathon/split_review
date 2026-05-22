Now I have a thorough calibration picture. Let me synthesize the final review.

Round 1 bracket (from three-band search): DIPOLE is clearly above the 3.0–3.67 papers (BDQL, Offline MARL) and below the 8.0 papers on unrelated topics. It sits somewhere in the 6.0–7.5 band, competing with SRPO (6.25), DAC (6.5), EFM (6.25), and DyDiff (5.25).

Round 2 narrowing: Comparing directly against DAC (6.5), SRPO (6.25), EFM (6.25), and LDCQ (6.33), DIPOLE has a cleaner theoretical contribution (dichotomous decomposition is more elegant than DAC's formulation, and avoids the Q-ensemble confound), much broader evaluation (39 tasks + real-world driving vs D4RL-only for most), and demonstrates scalability to a 1B-parameter model. The writing is also clearer than any of these anchors. DIPOLE is stronger than all of them, placing it above the 6.25–6.5 cluster. The missing exp-weighted baseline and the navtest framing concern prevent it from reaching the 8.0 tier.

Final score: 7.0.

---

## Summary

This paper proposes DIPOLE, a reinforcement learning method for fine-tuning diffusion/flow-matching policies. The key idea is a "greedified KL-regularized" objective whose optimal solution decomposes into a pair of dichotomous policies — one for reward maximization and one for minimization — each trained with stable sigmoid-weighted regression losses. During inference, the score functions of these policies are linearly combined via a greediness parameter ω, yielding action generation analogous to classifier-free guidance. Experiments span offline RL (ExORL, OGBench, 39 tasks), offline-to-online RL, and a large-scale autonomous driving benchmark (NAVSIM) using a 1B-parameter vision-language-action model.

## Strengths

- **Clean, theoretically grounded dichotomous policy decomposition.** The derivation from the greedified KL-regularized objective (Eq. 5) through Theorem 1 to the dichotomous policies (Eq. 8) is elegant and mathematically sound. The sigmoid weighting bounds weights in [0,1], directly addressing the instability of exponential-weighted regression without requiring ad-hoc clipping or small temperatures. To the best of this reviewer's knowledge, this decomposition is novel.

- **Principled connection to classifier-free guidance.** The inference-time linear score combination (Eq. 10) is structurally identical to CFG, providing an interpretable control mechanism via ω. This connection is explicitly explained (Section 3.2) and distinguishes DIPOLE from heuristic CFG-based methods like CFGRL, which lack theoretical backing.

- **Comprehensive evaluation across diverse settings.** DIPOLE is evaluated on 39 RL tasks across ExORL and OGBench (Tables 1–2), offline-to-online fine-tuning (Table 3), and a 1B-parameter autonomous driving model on NAVSIM (Table 4). Results are consistently strong: DIPOLE achieves best or near-best aggregate scores on most domains, and the DIPOLE w/o rs variant (no rejection sampling) already outperforms CFGRL on ExORL, demonstrating the core algorithm's effectiveness independent of inference-time tricks.

- **Scalability demonstrated on a real-world system.** Applying DIPOLE to a 1B-parameter VLA model for autonomous driving and showing meaningful closed-loop improvement (1.4 PDMS gain on navtrain, 88.3→89.7) is a significant strength. This validates that the method scales beyond standard RL benchmarks to practically relevant, large-scale problems.

## Weaknesses

### Major

- **No direct comparison against the exponential-weighted regression baseline that the paper criticizes.** The paper motivates DIPOLE by articulating three specific failures of the exp-weighted regression objective (Eq. 4): optimality-stability tradeoff, inefficient learning, and dependence on reference policy quality. Yet no experiment compares DIPOLE against a version of DIPOLE that simply uses the exp-weighted diffusion loss (with and without clipping, with tuned β). This is the most natural ablation for the paper's core claim — that the dichotomous decomposition fixes problems inherent to exp-weighted regression. Without it, the reader cannot empirically separate the benefit of the decomposition from other design choices. The existing baselines (IQL, FQL, CFGRL) are not designed to test this specific point. Adding this comparison would directly either prove or bound the claimed contribution.

### Minor

- **Navtest result is transparently reported but non-standard.** The paper reports both "navtrain" (official training split) and "navtest" (test split used for training) variants. The navtest variant shows a 6.5 PDMS gain (88.3→94.8) while navtrain shows 1.4 (88.3→89.7). The paper does explain the navtest variant as a case study for human-takeover scenarios, and both numbers are clearly labeled in Table 4. However, presenting both results side-by-side without a clear designation that the navtest variant is a non-standard evaluation risks the 6.5 gain being interpreted as the headline result. The navtrain result (a modest but positive 1.4-point gain) is the valid closed-loop benchmark result. The presentation would be improved by clearly relegating the navtest variant to a separate case-study section and centering the navtrain result as the primary evidence.

- **No hyperparameter sensitivity study for the greediness factor ω.** Since ω is the primary interface for "controllable greediness" (Section 3.2, Eq. 10), a user needs to know how performance varies with ω. The paper shows a conceptual illustration (Figure 1) but no quantitative results. Standard deviations across several ω values on one or two tasks would significantly strengthen the practical utility of the method. (The paper references Appendix D.4 for ablation studies, which was stripped during PDF extraction; if this analysis exists there, it should be moved to the main text.)

- **No training stability analysis (curves, loss histograms, weight distributions).** The paper claims DIPOLE addresses the instability of exp-weighted regression but never directly shows evidence of this — e.g., training curves comparing DIPOLE to an exponential-weighted variant, or histograms of the sigmoid vs exponential weights during training. This is a direct evidence gap for a central claim.

### Trivial

- **Minor notation issue:** The paper uses ω and w interchangeably at one point (Eq. 10 uses w while the text and earlier equations use ω).

## Nice-to-Haves

- A study of sensitivity to the reference policy μ quality and update frequency in the offline-to-online setting would be informative.
- The computational cost of training two diffusion models is not discussed; while LoRA modules are used for the VLA model, the RL benchmark experiments train two full models per task. A brief note on training time and memory footprint relative to single-model baselines would help practitioners assess the tradeoff.

## Removed Points

Points from the harsh critic that are removed or significantly demoted after verification:

- *"Rejection sampling confounds the RL contribution"* — Demoted from Major to removed as a standalone point. The paper already provides DIPOLE w/o rs (no rejection sampling) which outperforms CFGRL on ExORL, and the comparison against IFQL/FQL (which use rejection sampling) puts DIPOLE at a disadvantage, making the results more conservative, not less. The critic's request to re-run all baselines without rejection sampling would require re-implementing other authors' methods, which is beyond reasonable expectations.

- *"The sigmoid function applied to advantages can be negative"* — Removed. The math is correct: sigmoid of a negative advantage is < 0.5, and (1 - σ) > 0.5, so the negative policy correctly assigns higher weight to negative-advantage actions. The paper could discuss this more explicitly but it is not an error or omission.

- *"No discussion of computational cost (two models)"* — Demoted to Nice-to-Have. Training two diffusion models per task is a cost, but (a) the paper uses LoRA for the large VLA model, mitigating this for the real-world application, and (b) many RL algorithms already train multiple networks (actor, critic × 2 in TD3/SAC). A brief note would improve the paper but is not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the exp-weighted regression ablation.** Train DIPOLE with Eq. (4) loss (with tuned β and optional clipping) on 2–3 ExORL or OGBench tasks and report training stability (loss curves, weight distributions) alongside final performance. This single experiment would either prove the core claim about the dichotomous decomposition's advantage, or bound the paper's contribution if performance is similar.

2. **Restructure the NAVSIM presentation.** Move the navtest result to an appendix or clearly labeled case-study subsection. Use the navtrain result (1.4 PDMS gain) as the primary closed-loop evaluation result in the main text.

3. **Add a quantitative ω sensitivity plot** for at least one representative task (e.g., walker-stand or humanoidmaze-medium), showing mean return with standard deviation for ω ∈ {0.25, 0.5, 1.0, 2.0, 4.0}.

4. **Provide training curves** comparing loss magnitude and variance between DIPOLE and a standard exp-weighted regression loss on a single task to visually confirm the stability advantage claimed in Sections 1 and 3.1.

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| mc97L2QVIa (Offline MARL) | 3.00 | 1 | Much weaker; limited evaluation and less clear contribution |
| cXxfVkRCHJ (O2O CFDG) | 3.00 | 1 | Much weaker; narrower scope and less principled |
| k1qVBh5fnb (Latent Diffusion Planning) | 3.40 | 1 | Much weaker; imitation-only setting |
| gEdg9JvO8X (BDQL) | 3.67 | 1 | Weaker; limited gains, narrower evaluation |
| ayUh0A6LIJ (DyDiff) | 5.25 | 1 | Weaker; high variance, marginal improvements |
| TeeyHEi25C (Value function diffusion) | 6.25 | 1, 2 | Weaker; weaker baselines, less clear contribution, no real-world scale |
| xCRr9DrolJ (SRPO) | 6.25 | 1, 2 | Weaker; D4RL-only evaluation, some clarity issues |
| HA0oLUvuGI (EFM) | 6.25 | 2 | Weaker; weighted regression novelty is limited, reviewers noted overclaiming |
| NRYgUzSPZz (Discrete diffusion reasoning) | 6.25 | 2 | Comparable score tier but different topic (discrete reasoning vs RL) |
| ldVkAO09Km (DAC) | 6.50 | 2 | Weaker; Q-ensemble confound, narrower evaluation, less clean theory |
| tGQirjzddO (Latent diffusion reasoning) | 6.33 | 2 | Weaker; D4RL-only, missing important baselines |

**Round-1 bracket:** [6.0, 7.5]  
**Round-2 narrowing:** Comparing against the 6.25–6.50 cluster (SRPO, DAC, EFM, LDCQ), DIPOLE has a cleaner theoretical contribution, broader evaluation (39 tasks + real-world driving vs D4RL-only), clearer writing, and demonstrates scalability to 1B-parameter models. The weaknesses (missing exp-weighted baseline, navtest framing) prevent it from reaching the 8.0 tier. The paper is stronger than all round-2 anchors.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>