- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have sufficient information to produce the final consolidated review.

---

## Summary

This paper introduces I-PHYRE, a 2D block-elimination benchmark that requires agents to exhibit **interactive physical reasoning** — combining intuitive physics understanding, multi-step planning, and precisely-timed in-situ interventions. The benchmark comprises 40 games across four splits (basic, noisy, compositional, multi-ball) designed to test generalization. The paper evaluates three planning strategies (advance, on-the-fly, combined) using several RL algorithms and a human baseline (46 participants), finding a substantial gap between all tested learning agents and human performance.

---

## Strengths

1. **First benchmark to jointly require multi-step interventions AND precise action timing in physical reasoning.** Table 1 provides a systematic comparison against prior benchmarks (PHYRE, Virtual Tools, SMP, Block Towers, ComPhy), showing that I-PHYRE is the only intuitive-physics benchmark with ✓ for multi-step, action order, and action timing — all prior intuitive-physics benchmarks have ✗ for at least two of these dimensions.

2. **Carefully designed generalization splits that isolate specific reasoning challenges.** Section 3.1 defines each split's distinct purpose: the noisy split tests invariance to distractor blocks, the compositional split tests chaining of known concepts into longer sequences, and the multi-ball split tests coordination of multiple dynamic objects. This design goes beyond single-faceted generalization testing in existing benchmarks.

3. **Human baseline with a clear, reproducible protocol.** Section 4.1 reports results from 46 participants with 5 attempts per game and a 15-second time limit (Table 2: 92.39% success on Basic, 82.83% on Compositional and Multi-ball), alongside oracle scores, establishing interpretable upper bounds that many physical reasoning benchmarks lack.

4. **Three distinct planning strategies provide a structured analytical framework.** Section 3.2 formally defines planning-in-advance, planning-on-the-fly, and combined strategies; Sections 4.2.2 contrasts their training dynamics (Figure 4) and generalization behavior (Figure 2), showing that planning-in-advance converges more stably while on-the-fly strategies offer adaptability. This enables fine-grained diagnosis of agent limitations.

5. **Empirical results demonstrate a large and consistent performance gap between all tested RL agents and humans.** Figure 2 shows human rewards of ~800–900 across splits, while the best RL agents (PPO-C) achieve ~600 on Basic and drop sharply on compositional/multi-ball splits. The gap is analyzed in Section 5.1 with concrete hypotheses (physics modeling limitations, delayed feedback from multi-step interventions, sensitivity to precise timing).

---

## Weaknesses

### Fatal
None.

### Major

1. **No error bars, confidence intervals, or variance reporting on any experimental result.** All RL results (Figures 2 and 4) are presented without any indication of variability across random seeds or runs. Human results (Table 2) report only mean values with no standard deviation across participants. For a benchmark paper that aspires to serve as a standard evaluation tool, this is a significant methodological gap. Without variance estimates, readers cannot assess whether differences between agents (or between agents and humans) are reliable. *Evidence: Figure 2 shows bar charts with no error bars; Figure 4 shows single training curves; Table 2 reports only mean reward and success rate.* The paper contains no mention of multiple seeds, standard deviations, or statistical testing.

### Minor

2. **Oracle construction is insufficiently specified.** The oracle is described only as "scores achieved by the experimenters" (line 188), without stating how many experimenters, whether scores were verified to be optimal (e.g., by exhaustive search or dynamic programming), or whether unlimited attempts were allowed. This weakens the interpretability of the reported oracle rewards (all ~970) and the gap between humans and oracle.

3. **Per-split game counts are not reported in the main text.** The paper states "40 distinctive games" and "four splits" (lines 37, 123), but the number of games allocated to each split (basic, noisy, compositional, multi-ball) is not given. This information is likely in the supplementary material (referenced as \cref{sec:supp:games}), but its absence from the main text makes it harder to assess split balance, training set size, and evaluation reliability from the paper alone.

4. **No planning/search-based baseline for calibration.** The paper contrasts RL agents only with humans and a random agent. Adding a simple search-based baseline (e.g., beam search with the simulator as a forward model) would help separate the challenge of *learning* from the challenge of *planning* and calibrate the benchmark's intrinsic difficulty. This is noted as a gap in the Discussion (Section 5 lists no planning-based baselines).

### Trivial
None — the paper is reasonably well-written and the presentation issues are minimal.

---

## Nice-to-Haves

- A per-game breakdown of agent success rates (even a heatmap in the supplement) would clarify whether agents succeed on some games and fail completely on others, helping identify where the difficulty lies.
- A brief statement about the physics engine's determinism/stochasticity and whether its approximations could affect timing-critical solutions would be useful for reproducibility.
- Reporting standard deviation of human participants' scores across games would indicate whether some games are uniformly hard or show large individual variation.

---

## Removed Points

These points from the reviewers were assessed and removed with justification:

- **"Contradiction between 'interactivity' definition and 'planning in advance' strategy"** (Harsh Critic Critical Issue 4) — Removed because the paper explicitly acknowledges this. Line 157 calls planning-in-advance "a simplification" of the multi-step task, and line 250 notes it "limits real-time decision-making capabilities." The tension is acknowledged, so the criticism misreads the paper's own framing.
- **"Unfair comparison / baseline asymmetry"** — Not raised; included as a reminder that if such a claim had been made, asymmetry favoring baselines over the author's method would not be a valid weakness.
- **"Reproducibility concerns about hyperparameters"** — Removed per rule: trivial implementation details are not valid weaknesses for a benchmark paper.
- **Missing related-work citations** — Removed per rule: I cannot independently verify the existence of missing citations.
- **"Missing appendix / supplementary content"** — Removed per rule: the parser strips these sections; they exist in the original submission.
- **Formatting/style nitpicks** — Removed per rule.
- **Generic "noise split explanation is confusing"** — Removed. The paper's explanation (lines 46–47) is clear: the noisy block can be disregarded with accurate timing; suboptimal solutions occur when timing is imprecise, which is exactly the capability the split tests.
- **"Section 5 claims not backed by evidence"** — Weakened to minor. The three hypotheses in Section 5.1 (physics modeling, multi-step, timing) are plausible diagnostic claims supported by the observed performance gaps and standard RL limitations; they do not require separate experimental proof within the scope of this benchmark paper.

---

## Novel Insights

The reviews surface an interesting tension that the paper itself does not deeply explore: the "planning in advance" strategy (which pre-computes all actions from the initial static scene) achieves competitive performance on some splits despite explicitly *not* performing in-situ reasoning — the very capability the benchmark is designed to test. The paper notes this strategy converges "more swiftly, stably, and effectively" and acknowledges it "limits real-time decision-making capabilities," but does not analyze *which games or splits* admit advance planning and which genuinely require on-the-fly adaptation. A post-hoc analysis (e.g., per-game success rates for advance vs. on-the-fly planners) would clarify the benchmark's actual demand for interactivity and could reveal a spectrum from "solvable with static planning" to "requires real-time interaction." This is a useful direction for future work that the paper could have discussed.

---

## Suggestions

1. **Report error bars / confidence intervals on all results.** Add mean and standard deviation across at least 5 random seeds for each RL agent, and report standard deviation of human participant scores per split. This is the single most important improvement for establishing I-PHYRE as a credible benchmark.

2. **Specify the oracle construction.** Describe how many experimenters produced oracle scores, whether optimality was verified (e.g., by manual search over action sequences), and whether the oracle uses the same physics simulator.

3. **State per-split game counts in the main text.** This is a one-line addition that addresses a clear reader need.

4. **Add a simple planning-based baseline** (e.g., beam search or random shooting with the simulator) to calibrate the benchmark's difficulty independently of the learning challenges.

5. **Include a per-game breakdown** (even as a heatmap in the main paper) to show which games are particularly difficult and where agent failure concentrates.

---
