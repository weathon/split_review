## Summary

The paper introduces **Generative Trajectory Policies (GTP)**, a new policy paradigm for offline reinforcement learning. The authors first propose a unified ODE framework that subsumes diffusion models, flow matching, consistency models, and consistency trajectory models (CTMs) as special cases via a shared solution map Φ(x_t, t, s). Building on this, GTP learns the full ODE solution map as a policy, with two key practical adaptations: (1) a closed-form score approximation that replaces costly ODE integration during training, and (2) an advantage-weighted generative objective derived from KL-regularized policy optimization. Empirically, GTP achieves strong results on D4RL benchmarks, including a perfect score on antmaze-umaze and a 80.6 average on AntMaze that surpasses prior generative policy baselines.

---

## Strengths

- **Principled unification.** The ODE framework of Section 3 cleanly shows that diffusion models, flow matching, CMs, CTMs, shortcut models, and mean flows all instantiate the same flow map Φ(x_t, t, s) via two complementary objectives (Instantaneous Flow Loss and Trajectory Consistency Loss). This is a genuine conceptual clarification that motivates GTP's design.

- **Theorem 1 is practically useful.** The bound |L_prac − L_ideal| = O(h^p) formally justifies using the closed-form surrogate f̃(x_t, t) = (x_t − x)/t in place of a self-referential ODE solver during training. This prevents the bootstrapping error cycle that destabilizes standard CTM-style training and is validated empirically (Table 3, score 99.7 vs 112.2).

- **Strong BC expressiveness on AntMaze.** In the pure BC setting (Table 1), GTP-BC averages 66.3 on AntMaze versus C-BC's 44.1—a +22 point gain with no RL signal. This cleanly isolates the policy architecture's representational capacity and is a convincing demonstration.

- **Competitive offline RL results.** Table 2 shows GTP achieves 89.0 on Gym and 80.6 on AntMaze, outperforming strong baselines (QGPO: 78.3; D-QL: 69.6 on AntMaze). Perfect scores on antmaze-umaze are particularly notable.

- **Advantage-weighted objective is theoretically grounded.** Theorem 2 derives the advantage weighting from KL-regularized policy optimization, and the ablation (Table 3) confirms that the naive alternative (linear Q-term) diverges except for a single brittle coefficient, whereas GTP's weighting is stable.

---

## Weaknesses

### Fatal
None.

### Major

1. **GTP is essentially CTM adapted for offline RL, with incremental novelty.** Section 3.4 explicitly states that CTMs "correspond exactly" to both core components of the unified framework (the instantaneous flow loss and the trajectory consistency loss). The distinguishing contribution of GTP over CTM-in-RL is (a) replacing the ODE solver with the closed-form surrogate from offline data, and (b) adding advantage weighting. Both are reasonable, but the paper's framing of a "new and more general policy paradigm" overstates the architectural novelty. The actual paper contribution is a well-motivated offline RL adaptation of CTMs.

2. **Advantage-weighted generative training (Theorem 2) is a restatement of known results.** The result π*(a|s) ∝ π_BC(a|s) exp(ηA(s,a)) is standard in offline RL (AWR, AWAC, IQL, DPPO). Presenting it as a theorem deriving the "theoretically correct" objective for GTP is accurate, but it is not a contribution novel to this paper—applying known advantage weighting to a new policy class is engineering, not a new theorem.

3. **Ablation study covers only one task.** Table 3 is restricted to `hopper-medium-expert-v2`. This is a relatively easy, well-studied task. It is unclear whether the ablation conclusions (score approximation is important, variational guidance is stable) hold on harder tasks like antmaze-large or antmaze-medium-diverse. Multi-task ablations are needed to establish the general claim.

4. **Missing baselines for AntMaze and selective comparisons.** BDM and C-AC have missing entries on antmaze-md, antmaze-lp, and antmaze-ld in Table 2. The GTP average of 80.6 is computed over all 6 tasks, while BDM and C-AC averages cannot be computed. This makes the "GTP is best on AntMaze" claim unverifiable against these baselines. Additionally, on individual tasks, GTP does not lead: CQL beats GTP on antmaze-ud (84.0 vs 81.9), QGPO beats GTP on antmaze-lp (66.6 vs 53.5), and IDQL-A beats GTP on antmaze-mp (84.2 vs 83.3).

### Minor

1. **Training time not compared to baselines.** Table 3 compares GTP (4.26h) against its own ablation variants but never against D-QL, QGPO, or C-AC. The claim that GTP resolves the "efficiency" side of the expressiveness–efficiency trade-off is partially unsupported—it is faster than its own naive counterpart but its absolute training time of ~4 hours is not contextualized.

2. **Theorem 1's assumption "solver states admit bounded second moments independent of h"** is stated without verification. In the offline RL setting where the data distribution can be highly non-Gaussian, it would be valuable to at least discuss whether this condition is practically satisfied.

3. **Score approximation is a one-step Euler step in disguise.** The claim that x_u = x + u·z is a "closed-form surrogate" is true, but it is also exactly what one gets from a single Euler step on the flow-matching vector field evaluated at x. The presentation in Remark 1 would benefit from making this connection explicit, as it would clarify why the approximation works well.

### Trivial

- The paper uses "score" for the Inst Map, acknowledging in Footnote 1 that this is a slight abuse. This is fine but may cause minor confusion.

---

## Nice-to-Haves

- Ablations on at least 3–4 tasks across both Gym and AntMaze to validate claims about training stability and score approximation.
- A training-time comparison table that includes D-QL, QGPO, and C-AC to properly characterize the efficiency claim.
- A more precise statement of what distinguishes GTP from "CTM applied to offline RL" to help readers assess the contribution's scope.

---

## Novel Insights

The most genuinely novel contribution is the insight that, in offline RL, the bootstrapping instability of CTM-style trajectory training can be avoided entirely by anchoring intermediate trajectory points directly to the offline dataset via the linear interpolation x_u = x + u·z. This observation—that the offline data itself serves as a free and stable supervision source, avoiding the need for any ODE integration—enables learning a full flow map more reliably than the CTM approach while being computationally cheaper. The O(h^p) bound in Theorem 1 provides the theoretical glue. The unified ODE framing also provides a cleaner conceptual vocabulary for the field, even if the underlying ideas were partially anticipated by CTMs.

---

## Suggestions

- Expand the ablation to cover at least antmaze-medium-play and antmaze-large-play to test whether score approximation and variational guidance remain critical in harder, sparser-reward settings.
- Report wall-clock training time for all baselines in a single table, including D-QL, QGPO, and C-AC, to properly evaluate the efficiency claim.
- Clarify the architectural distinction between GTP and CTM (Kim et al., 2024) in a dedicated paragraph, specifying exactly what is new vs. what is inherited.
- Consider single-step inference performance (K=1) to fully characterize the expressiveness–efficiency curve, as this would most directly demonstrate that GTP avoids the consistency model degradation.

---

## Score and Decision

GTP is a well-executed paper that addresses a real problem in offline RL. The unified ODE perspective is clean and useful, the score approximation is a practical contribution with formal justification, and the empirical results—particularly the large BC gains on AntMaze—are convincing. The main limitation is that the core architecture (CTM-style trajectory learning) is not new, and several "state-of-the-art" claims are only true in an aggregate sense while individual task comparisons reveal competitive or weaker performance against specific baselines. The ablation coverage is narrow. These concerns push the paper to the borderline acceptance range.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>