## Summary

This paper proposes TTPI (Generalized Policy Iteration using Tensor Train), an Approximate Dynamic Programming (ADP) algorithm for hybrid control problems with mixed discrete-continuous action spaces. It uses Tensor Train (TT) decomposition via TT-Cross to approximate state-value and advantage functions, and TTGO for policy retrieval over hybrid action spaces. The method assumes access to system dynamics and is evaluated on two benchmark tasks and a real-world planar pushing experiment.

## Strengths

- **Addresses a genuine gap in ADP for hybrid action spaces.** The paper correctly identifies that policy retrieval over hybrid (mixed discrete-continuous) actions is a bottleneck in ADP. Combining TT-Cross for function approximation with TTGO for optimization over hybrid spaces is a technically well-motivated approach.

- **Real-world robotic demonstration.** The planar pushing experiment (Section 3.2) involving contact-mode switching on a physical robot shows the method can solve a genuinely challenging control problem, going beyond pure simulation.

- **Candid limitations section.** Section 4 honestly discusses when the method would break down (high-rank value functions, very high-dimensional state spaces, reliance on parallelized simulators) without over-promising. This transparency is commendable.

- **Computational complexity is properly characterized.** The paper gives concrete complexity expressions: \(O(n d r^2)\) for TT-Cross evaluation and \(O(N m d r^2_{\max})\) for policy retrieval (lines 102, 153), and explicitly notes the quadratic dependence on TT rank (line 155).

## Weaknesses

### Fatal
None.

### Major

- **The "superiority" claim rests on an asymmetric comparison.** TTPI has direct access to the system dynamics \(f\) and reward function \(r\) (it is a model-based ADP method), yet the only baselines are model-free Deep RL methods (HyAR, HPPO, PDQN) that must discover dynamics from interaction. The paper acknowledges this asymmetry (lines 192–193: *"TTPI assumes access to the system dynamics and the reward function, whereas Deep RL techniques, in theory, are agnostic to the system model and implicitly address a more challenging problem than TTPI"*) but still claims **"superiority over previous baselines"** (abstract, conclusion). This conflates the advantage of having the model with the advantage of the specific TT-based function approximation. The framing substantially overstates the evidence for the algorithmic contribution. To isolate the benefit of TTGO/TTPI, the paper should compare against other model-based methods—in particular, the prior TT-based ADP work it cites (Gorodetsky et al., 2015; Boyko et al., 2021) that used Newton-type optimization.

- **No experimental comparison against prior TT-based ADP methods.** The paper's claimed novelty is TTGO-based policy retrieval for hybrid actions over prior TT-ADP work that used Newton-type optimization (lines 231–232). Without comparing TTPI against these prior TT-ADP baselines (or at least ablating TTGO vs. Newton optimization on the same TT-represented value functions), it is impossible to assess whether TTGO provides any benefit. The contribution is not experimentally isolated.

- **Real robot experiment lacks any baseline or quantitative context.** The planar pushing experiment reports a "100% success rate" (line 208) with no comparison against any alternative method—not even a hand-tuned baseline, and not even runtime numbers against the cited methods (MIP, hybrid DDP) that the paper claims struggled with this task. The number of trials, the tolerance for success, and the exact nature of disturbances are not reported, making the result an existence proof rather than a comparative evaluation.

### Minor

- **No ablation studies of key algorithmic parameters.** The paper fixes the discretization at 100 points per variable, \(r_{\max}=100\), and accuracy \(\epsilon=10^{-3}\) (Section 3) without any sensitivity analysis. How performance and computation scale with these choices—especially when TT rank grows—is not characterized, even though the limitations section (line 218) acknowledges this as a failure mode.

- **Baseline methods are not described.** The configuration, hyperparameters, and training budget used for HyAR, HPPO, and PDQN are not reported. Without this, the comparison cannot be reproduced or assessed for fairness.

- **Unusual metric choice without justification.** For the HM task, the metric \(\mu\) is defined as the *square* of the ratio between trajectory length and shortest-path length (line 204). Squaring this ratio is non-standard and could inflate differences between policies; its rationale is not discussed.

### Trivial
None.

## Nice-to-Haves

- An ablation replacing TTGO with Newton-type optimization (from prior TT-ADP work) on the same TT value functions would directly isolate the advantage of TTGO for hybrid actions.
- Comparison against model-based alternatives (e.g., iLQR, DDP, or prior TT-ADP) would strengthen the evaluation.
- Reporting confidence intervals or variance across runs for the numerical results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Quantitative results are absent"** — The table exists as an image in the original PDF; only the caption survived parsing. The numerical data is present in the original submission. → Removed (parser artifact).
- **"TTGO improvements in appendix are missing"** — Appendix Section A was stripped by the parser, as happens for all papers. → Removed (parser artifact).
- **"Algorithm 2 is presented as an image"** — The pseudocode is embedded as an image; this is a formatting choice typical of PDF papers. → Removed (formatting artifact).
- **"Stochastic extension is speculative"** — Section 2.9 is explicitly framed as "how our approach *can be* extended" and acknowledges the difficulty of obtaining stochastic models. It is not presented as a core contribution. → Removed (not a genuine weakness of the claimed contributions).
- **"Computational cost analysis ignores rank dependence"** — The paper explicitly states the cost "grows quadratically with the rank" (line 155) and gives \(O(n d r^2)\) for TT-Cross (line 102). The critic's assertion is factually incorrect about what the paper says. → Removed (factually wrong).
- **"No discussion of policy evaluation termination criteria"** — Partially addressed in Section 2.8 (lines 151–156). The description is high-level but the paper is not silent on the matter. → Removed (overstated).

## Novel Insights

The core tension exposed by the reviews is between the paper's stated contribution (TT-based ADP for hybrid control via TTGO) and the experimental design (exclusively model-free baselines). The paper's technical approach is reasonable and the real-robot demonstration is valuable, but the evidence does not distinguish whether TTPI's performance comes from being model-based, from the specific TT representation, or from the TTGO policy retrieval. The most impactful revision would be to reframe the paper around a comparison with prior TT-ADP methods, isolating the contribution of TTGO for hybrid actions, rather than claiming superiority over model-free methods that solve a harder problem.

## Suggestions

1. Reframe the central claims from "superiority over baselines" to a more precise statement: TTPI achieves strong results on hybrid control benchmarks compared to model-free methods, noting that it has access to the dynamics. Better yet, add model-based baselines.
2. Add an ablation comparing TTGO against Newton-type optimization (as used in prior TT-ADP) on the same TT value functions to isolate the claimed advantage for hybrid actions.
3. Provide full numerical results from Table 1 (success rates, \(\mu\) values, training times) with standard deviations or intervals, and describe the baseline configurations used.
4. Include a simple baseline (e.g., uniform random policy, heuristic controller) on the real robot experiment to contextualize the 100% success rate, and report the number of trials.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>