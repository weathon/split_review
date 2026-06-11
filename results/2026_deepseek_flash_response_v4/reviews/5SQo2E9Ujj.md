## Summary

This paper proposes a conceptual reframing of curriculum learning in goal-conditioned RL (GCRL) as "selective data acquisition" — biasing the training distribution toward underachieved goals — rather than primarily an exploration heuristic. The authors train UVFAs on GridWorld data collected via greedy rollouts under PBRS shaping, comparing uniform vs. edge-biased goal sampling. They report modest improvements on edge goals (e.g., +0.034 in baseline, +0.083 in weighted variant) and a dose-response relationship where stronger distributional bias yields larger gains.

---

## Strengths

1. **Explicit verification of distributional shift (Section 3.1, Figure 2)** — The paper does not stop at success rates; it directly verifies that the curriculum shifts the training distribution toward harder goals, providing evidence for the claimed mechanism rather than relying solely on downstream performance.

2. **Dose-response relationship in the weighted curriculum (Section 3.2)** — The weighted curriculum amplifies the edge bias beyond the baseline and produces proportionally larger edge-goal gains ($\Delta_{\text{edge}} \approx +0.18$ vs. ~$+0.08$). This monotonic relationship strengthens the causal interpretation that gains are driven by selective data acquisition, not incidental features of the sampling heuristic.

3. **Clean experimental isolation** — All training parameters (architecture, optimizer, learning rate, batch size, epochs) are held constant across conditions; the only manipulated variable is the goal sampling distribution (Section 2.5).

---

## Weaknesses

### Major

1. **Experiments do not involve online RL, despite the GCRL framing.**  
   The data collection protocol (Section 2.5) rolls out 1000 episodes using *greedy action selection under PBRS shaping* — which, in a deterministic GridWorld with a potential based on Manhattan distance, produces essentially optimal trajectories from a near-oracle policy. The UVFA is then trained via supervised regression on this static dataset. There is no online RL loop: the agent never uses its learned value function to explore, never receives sparse rewards, and never generates new training data from its own behavior. The paper motivates its study with challenges such as "sparse rewards" and "exploration issues" (Section 1), yet the experimental design sidesteps both by using dense shaped rewards and optimal data collection. The claim that curricula should be understood as "not merely exploration heuristics" is hollow when the setup excludes exploration entirely. This is a structural disconnect between the paper's framing and its evidence.

2. **Paper claims curricula "reduce approximation error" but never measures it.**  
   The abstract states that curricula "reduce approximation error on a shared evaluation set," and the introduction repeats this claim. However, the Results section reports only success rates. No metric of function approximation quality — MSE between predicted and true values, prediction error, or any other direct measure — is presented. This is an evidential gap: the paper makes a quantitative claim about a specific variable and then does not measure it.

3. **Empirical results are too weak to support the conclusions drawn.**  
   The headline comparison (Section 3.1) shows edge-goal success improving from 0.183 (NoCurr) to 0.217 (Curr) — a 3.4 percentage point gain — with overlapping standard deviations ($\pm 0.131$ vs. $\pm 0.125$ across 3 seeds). The overall success rate is essentially unchanged (0.361 vs. 0.370). No statistical tests, confidence intervals, or effect sizes are reported. With 3 seeds and high variance, the observed differences are consistent with noise. The weighted curriculum comparison (Table 1) shows a larger edge improvement (0.060 → 0.143), but the NoCurr baseline in this condition (0.060 edge success) differs sharply from the baseline condition NoCurr (0.183), with no explanation for why the same "uniform" condition performs so differently across experiments.

### Minor

4. **GridWorld dimensions are unspecified (Section 2.1).**  
   The number of cells, grid dimensions, and start-state distribution are absent. This is a basic reproducibility gap, since "edge" vs. "interior" is defined relative to grid size.

5. **The "curriculum" is a fixed static sampling bias, not an adaptive or sequenced curriculum.**  
   As used in this paper, "curriculum" means a fixed reweighting of the goal distribution that does not change over training. This differs from most of the cited literature (Bengio et al., Florensa et al., Portelas et al.), where curricula adapt difficulty over time. The paper does not acknowledge this distinction clearly.

---

## Nice-to-Haves

- Running experiments with actual online GCRL (sparse rewards, exploration, policy improvement loop) to give the "data acquisition vs. exploration" distinction real stakes.
- Directly measuring approximation error (e.g., MSE of the learned value function against the true value) to substantiate the central claim.
- Statistical testing (confidence intervals, effect sizes) to determine whether the observed differences are meaningful.
- Specifying grid dimensions and start-state distribution for reproducibility.

---

## Removed Points

The following points from the Harsh Critic and Strength Finder were removed after cross-checking against the paper:

- *"The core conceptual contribution is nearly tautological"* — Removed as an overly subjective judgment that is not a specific, verifiable weakness. The paper provides empirical evidence, however modest, for its framing.
- *"No comparison to actual online RL training (DQN, PPO, etc.)"* — Removed because the paper explicitly acknowledges its limited scope (Section 4.1) and positions itself as a simple demonstration of a conceptual point. Requesting a full online RL comparison stretches beyond the stated scope.
- *"Missing related work"* — Removed per policy (cannot verify from paper alone).
- *Formatting, typos, and parser artifacts* — Removed per policy; these are parser issues, not author errors.
- *The paper "should not be accepted in its current form" / "experiments would need to be fundamentally reconfigured"* — This is a summary judgment, not a specific weakness. The specific weaknesses (no online RL, no approximation error measurement, weak results) are already captured above.
- *Strength about "clean experimental isolation"* — Retained as it is specific and justified. Other claimed strengths from the Strength Finder that were generic or unfounded (e.g., "this paper addressed an important problem") have been removed.

---

## Novel Insights

None beyond the paper's own contributions. The dose-response finding in the weighted curriculum is already presented by the paper itself.

---

## Suggestions

1. **Address the framing-experiment gap.** Either reconfigure the experiments to involve online GCRL with sparse rewards (where curricula can be meaningfully distinguished from exploration), or explicitly reframe the paper as a supervised learning study on how biased sampling affects learned value functions — removing the GCRL/exploration framing from the title and claims.
2. **Measure what you claim to measure.** If the paper asserts that curricula "reduce approximation error," report a direct measure of approximation error (e.g., MSE between predicted and true values on a held-out evaluation set).
3. **Increase statistical rigor.** Use more seeds (at least 10), report confidence intervals, and explain the discrepancy between the NoCurr baselines across the baseline and weighted experiments.
4. **Specify all environmental parameters** (grid size, start-state distribution) for reproducibility.

---

## Calibration Anchors

**Round 1 — Bracketing (low: <3.5, mid: 3.5–7.5, high: >7.5):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `lnB7rTsT9Y.md` | 3.40 | R1 | Similar concept (curriculum + value functions), poor presentation; our paper is clearer but has structural issues |
| `VCscggkg2t.md` | 3.00 | R1 | GCRL with GFlowNets, limited evaluation; our paper is better written |
| `llXCyLhOY4.md` | 3.00 | R1 | GCRL paper with poor writing; our paper is cleaner |
| `sXF5P4N7e8.md` | 3.00 | R1 | GCRL for grasping; different domain |
| `OZ3NXrF3gQ.md` | 2.50 | R1 | Reward-free RL; weaker than our paper |
| `hCfhfwSfCg.md` | 2.00 | R1 | LLM-guided exploration; weaker than our paper |
| `OjCWG58ZyY.md` | 5.50 | R1 | GCRL curriculum with stronger experiments; stronger than our paper |
| `qg5JENs0N4.md` | 5.50 | R1 | TD vs SL generalization; stronger theoretical contribution |
| `7b2itdrxMa.md` | 4.00 | R1/R2 | Curriculum learning + human study; broader contribution, somewhat stronger |
| `o2IEmeLL9r.md` | 7.33 | R1 | Pre-training goal-based models; substantially stronger |
| `V8Lj9eoGl8.md` | 5.25 | R1 | Proximal curriculum with theory + experiments; stronger |
| `f3QR9TEERH.md` | 5.25 | R1 | Safe curriculum for constrained RL; stronger |
| `9pW2J49flQ.md` | 8.00 | R1 | LTL instruction RL; much stronger paper |

**Round 2 — Narrowing (target range 2.0–5.0):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `E4Ero36Zr4.md` | 4.40 | R2 | Data-centric TSCL analysis with stronger theoretical framing; better than our paper |
| `xw4jtToUrf.md` | 4.20 | R2 | Online RL in world models; different domain, stronger execution |
| `BMWOw3xhUQ.md` | 3.75 | R2 | SL/TD bridging with theoretical issues; comparable quality |
| `BH8Nrt2dPf.md` | 4.25 | R2 | GCRL invariance to planning; stronger conceptual contribution |
| `Uxm7DxPwrZ.md` | 4.80 | R2 | Offline GCRL navigation; stronger empirical work |
| `1OGhJCGdcP.md` | 3.50 | R2 | GCHRL with subgoal representations; comparable quality |
| `VDkye4EKVe.md` | 3.00 | R2 | Minimal RL environments; weaker than our paper |
| `L143pPpIHv.md` | 3.00 | R2 | Curiosity paper; weaker |

**Round 1 bracket:** 3.0–5.0. **Round 2 narrowing:** The paper is notably weaker than the 4.0+ anchors (7b2itdrxMa, E4Ero36Zr4) but better than the 3.0 anchors (llXCyLhOY4, VDkye4EKVe). It is most comparable to lnB7rTsT9Y (3.40) and BMWOw3xhUQ (3.75). The structural issues (no online RL despite GCRL framing, unmeasured claims) prevent a higher score. **Final score: 3.5.**

---

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>