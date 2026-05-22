**Bracket (Round 1):** 5.5–7.0. The paper is clearly above low-quality benchmarks (~3.0) but not at the level of massive-scale, multi-domain benchmarks like RoboCasa365 (7.0) or the top method papers (7.5+).

**Narrowing (Round 2):** Compared to MIKASA (6.5, Accepted Poster) — similar structure as an RL benchmark with careful task design and honest evaluation — BuilderBench has more conceptually novel and diverse tasks (reasoning about physics, geometry, counterweights vs. pick-place memory), but its self-supervised evaluation covers only 12/42 tasks (the simplest ones). This is comparable to MIKASA's limitations (criticized as incremental over ManiSkill3). BuilderBench is slightly more novel in task design but slightly less complete in evaluation. ULEE (6.0, Accepted Poster) is a method paper, not directly comparable. Newt/MMBench (6.0, Accepted Poster) had novelty concerns. BuilderBench sits between these anchors.

---

## Summary

BuilderBench is a block-building benchmark designed to probe open-ended exploration and generalization in RL agents. It provides a fast MuJoCo/JAX simulator, 42 carefully curated tasks requiring diverse reasoning skills (physics, geometry, planning, motor control), and reference implementations of six algorithms. Experiments show that current unsupervised RL methods succeed only on the simplest tasks (1–2 cubes) and fail on 3+ cube tasks, honestly documenting headroom rather than overselling the benchmark as solved.

---

## Strengths

- **Hardware-accelerated, fast simulator with low barrier to entry.** The MuJoCo/JAX simulator is claimed to be 10–100× faster than CPU-based benchmarks like Crafter or Minecraft. Training PPO to stack two blocks takes ~30 minutes on a single GPU (Section 1, Appendix B). This speed advantage is a genuine practical contribution that makes the benchmark accessible.

- **Thoughtfully curated task suite with genuinely diverse reasoning demands.** The five-task case study (Section 5.1) concretely demonstrates that distinct tasks require qualitatively different strategies: rotating a base cube for stability (T-block), solving a packing problem with geometric reasoning (Four Cube Packing), building temporary scaffolds (Hexagonal Portal), using counterweights (Leaning Tower), and solving the maximum-overhang problem. This is more than a procedural generation of variants — each task targets a different reasoning ability.

- **Honest and informative baseline results.** The paper reports that SFL and MEGA succeed on 1-cube tasks, partially on 2-cube tasks, and fail on 3-cube tasks in the self-supervised protocol (Figure 6), and that even supervised PPO struggles on 3–4 cube tasks (Figure 7). Rather than overselling, the paper uses these results to establish headroom. The LLM evaluation (Figure 8) reinforces that language-only reasoning is insufficient.

- **Comprehensive open-source release.** The paper provides single-file implementations of six algorithms, the full task suite, and the simulator. The "training wheels" (single-task supervised) protocol allows researchers to incrementally build up to the harder unsupervised setting.

---

## Weaknesses

### Major

- **Self-supervised evaluation covers only 12 of 42 tasks (1–3 cubes), leaving the hardest tasks untested in the open-ended setting.** The most interesting tasks — hexagonal portal (8+ cubes), leaning tower (7+2 cubes), maximum overhang (5 cubes) — are tested only under the single-task supervised protocol, which sidesteps generalization entirely. The paper's central claim about evaluating "open-ended exploration and generalization on diverse, complex tasks" is not demonstrated by the experimental results for precisely those tasks that make the suite distinctive. The benchmark's value will depend on whether the community can scale methods to these harder tasks; this is an honest limitation but a real one.

- **Training protocol ambiguity for the multi-task self-supervised evaluation.** The paper states, "All algorithms are trained in environments with one, two and three cubes and the learned policies are tested on the respective tasks" (Section 7). It is unclear whether this means three separate training runs (one per cube count) or a single run with variable cube counts. If per-cube-count training is used, the benchmark does not evaluate the agent's ability to generalize across cube counts — a critical component of open-ended skill acquisition. The state representation dimension (ℝ^{11+13n}) depends on n, suggesting separate runs may be necessary, but this is not explicitly discussed.

### Minor

- **No quantitative difficulty decomposition for the 42 tasks.** The paper relies on qualitative descriptions and empirical results to convey difficulty. Providing per-task metrics (e.g., minimal solution length, reward sparsity, random-policy baseline performance) would help researchers select tasks and calibrate progress. Currently, tasks are only characterized by cube count.

- **LLM evaluation is suggestive but limited.** The evaluation uses open-loop language plans on 5 tasks (Section 7.1). While the negative result is informative, the paper itself notes this "is not meant to be an extensive evaluation." A closed-loop setting (LLM proposes actions, simulator checks feasibility) would be stronger. The current result is expected and does not add much beyond the RL experiments.

- **"Unknown solution" tasks are mentioned but never identified.** The design philosophy (Section 5.2) states that some tasks have solutions unknown even to the authors. This is intriguing but the paper does not specify which tasks these are, making it impossible for future researchers to target them.

### Trivial

- Figure 6 and 7 captions refer to "cube-1 (2 tasks)" but the number of tasks per condition could be more clearly explained.
- The speed comparison to Crafter/Minecraft/NetHack (10–100×) is deferred to Appendix B without a summary of the measured results in the main text.

---

## Nice-to-Haves

- A small-scale experiment showing that the self-supervised protocol can yield generalization to an unseen task with a different number of cubes (e.g., train on 1-cube, test on a 2-cube task) would strengthen the generalization claim.
- An analysis of *why* PPO fails on 3-cube tasks (e.g., state-space size, reward sparsity, horizon length) would help the community understand what algorithmic innovations are needed.
- Identifying and highlighting at least one "unknown solution" task as a concrete open problem.

---

## Removed Points

- **Critic: "No formal/analytic support for the claim that tasks require 'embodied reasoning'."** The paper provides extensive qualitative evidence (5-task case study, Section 5.1) showing non-trivial physical strategies. The claim is supported at the level expected for a benchmark paper and does not require formal decomposition. Not a valid weakness.
- **Critic: "The paper claims tasks require 'embodied reasoning' but doesn't show they can't be solved by simpler non-exploratory methods."** The paper shows that even supervised PPO struggles on 3+ cube tasks (Figure 7). This is evidence that simple methods fail. Moved as the paper already addresses this.
- **Critic: "The analysis of why tasks are difficult is largely informal."** See weakness #3 — this is included as a Minor weakness (no quantitative difficulty decomposition). The "informal" framing is too harsh for what is actually a missing feature.
- **Strength Finder: "Comprehensive open-source reference implementations" and "Open-source and fully reproducible"** — These are merged into a single strength in the final review. The Strength Finder's "Principled evaluation of open-ended generalization" and "LLM evaluation" are folded into existing strengths/weaknesses.
- **Strength Finder: "LLM evaluation demonstrates the benchmark's non-linguistic reasoning demand"** — This is included in the evaluation results honestly. Not a separate strength as the evaluation is limited (see weaknesses).

---

## Novel Insights

None beyond the paper's own contributions. The key observation — that block-building, a surprisingly simple setup, can generate tasks requiring diverse physical, geometric, and planning skills that current RL methods and LLMs cannot solve — is the paper's own claim, not a novel synthesis from the reviews.

---

## Suggestions

1. Clarify the training protocol: specify whether the multi-task self-supervised evaluation uses separate training runs per cube count or a single run, and discuss whether the environment supports variable cube counts during training.
2. Add quantitative difficulty metrics for each of the 42 tasks (e.g., minimal solution length, success rate of a random policy, reward sparsity).
3. Identify the "unknown solution" tasks explicitly to create concrete open challenges for the community.
4. Include a proof-of-concept generalization experiment across cube counts, even if small-scale.

---

## Score and Decision

**Anchors consulted (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| MIKASA (9cLPurIZMj) | 6.50 | 1,2 | Similar benchmark contribution; BuilderBench has more novel tasks but less complete evaluation |
| Newt/MMBench (MPabX9LEds) | 6.00 | 1,2 | Benchmark+method paper; BuilderBench stronger as pure benchmark |
| ULEE (UmxTIxHWkl) | 6.00 | 1,2 | Method paper on exploration; different contribution type |
| RoboCasa365 (tQJYKwc3n4) | 7.00 | 2 | Larger scale but similar contribution type; BuilderBench's tasks more diverse per-cube |
| Unifying URL (nNmd4pPSck) | 4.40 | 1 | Theoretical paper, rejected; BuilderBench stronger empirically |
| Explore-Go (KpltrPQ12x) | 4.00 | 1 | Method paper, rejected; BuilderBench stronger contribution |
| Task Tokens (6T3wJQhvc3) | 7.00 | 2 | Method paper, higher score; different contribution type |
| Theory of Space (8iPwqr6Adk) | 6.00 | 2 | Exploration benchmark, accepted; comparable quality |

**Round 1 bracket:** 5.5–7.0  
**Round 2 narrowing:** Compared to MIKASA (6.5), BuilderBench has more novel task design but the evaluation gap (only 12/42 tasks tested in the open-ended protocol) is a real limitation. The paper is cleaner and more honest than the rejected anchors (4.0–4.4) but not as comprehensive as RoboCasa365 (7.0). The score is positioned between MIKASA (6.5) and the lower anchors (6.0), slightly above the midpoint because the task curation is genuinely creative and the simulator speed is a practical advantage.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>