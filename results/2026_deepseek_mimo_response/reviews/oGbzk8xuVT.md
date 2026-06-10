## Summary
BuilderBench introduces a hardware-accelerated (MuJoCo + JAX) block-building environment and a curated suite of 42 target structures for evaluating agents that learn through open-ended exploration. The benchmark features a self-supervised multi-task protocol (agents explore without supervision, then generalize to unseen tasks) and a supervised single-task protocol, with baselines from six RL algorithms and two LLMs.

## Strengths
- **Thoughtfully curated task suite with distinct reasoning requirements**: The five case-study tasks (T-Block, Four Cube Packing, Hexagonal Portal, Leaning Tower, Maximum Overhang) each demand qualitatively different abilities—geometric rotation, spatial packing, scaffolding with emergent simultaneous-grasp skills, counterweight reasoning, and mathematical optimization (Section 5.1, Figures 2–5). This avoids the common benchmark pitfall where many tasks test the same underlying skill.
- **Hardware-accelerated simulator with concrete speed claims**: MuJoCo + JAX backend claiming 10–100× faster training than CPU-based benchmarks (Section 1), with PPO on a stacking task completing in ~30 minutes on a single GPU. This is a genuine practical advantage for academic research.
- **Clean self-supervised protocol decoupling exploration from generalization**: Agents receive no task specification during training and must generalize to unseen target structures at test time (Section 6, Figure 1). This directly tests transferable-prior acquisition through exploration—something most RL benchmarks do not evaluate.
- **Honest benchmarking demonstrating significant headroom**: All tested algorithms largely fail beyond 1–2 cube tasks, and LLMs fail on all five case-study tasks (Figures 6–8). The benchmark is clearly unsaturated, leaving room for future research.
- **Full open-source release with practical tooling**: Single-file implementations of six algorithms, interactive scripts, fully open-source simulator and task suite (Section 9).

## Weaknesses

### Fatal
None

### Major
- **Over half the task suite (≈25 of 42 tasks) has no benchmarking results.** Self-supervised evaluation covers 12 tasks (Figure 6: 2 one-cube + 5 two-cube + 5 three-cube), supervised covers 17 (Figure 7: adds 5 four-cube), LLM evaluation covers 5 case-study tasks. With some overlap, roughly 25 of 42 tasks have no results. For a benchmark paper, the task suite is a core contribution, and presenting a curated suite without characterizing most tasks leaves readers unable to assess whether the suite is well-designed or covers genuinely distinct skills. A taxonomy table (number of cubes, required skills, difficulty tier, solution horizon) would substantially strengthen the paper.

- **The LLM evaluation (Section 7.1) draws an unsupported conclusion.** The paper tests ChatGPT-5 and Gemini 2.5 Pro by asking for open-loop text plans for building block structures, then concludes "solving our tasks requires non-obvious steps of reasoning that are beyond what current models can achieve through scaling alone" (line 219). LLMs are not designed for closed-loop physical manipulation planning, and their failure says little about what scaling could achieve (e.g., vision-language-action models trained on interaction data are a very different thing). The paper does qualify this ("not meant to be an extensive evaluation"), but the conclusion still overclaims. This should be reframed as motivation for embodied interaction rather than evidence about LLM limitations.

- **Self-supervised results provide limited diagnostic signal.** All tested algorithms essentially fail on 3-cube tasks; only MEGA shows partial progress on 2-cube tasks (Figure 6). While demonstrating task difficulty is valuable, a benchmark needs to distinguish better from worse approaches across a gradient. When every algorithm hits near-zero, the benchmark cannot differentiate approaches. The supervised protocol (Figure 7) partially addresses this but shifts the benchmark toward standard goal-conditioned RL, narrowing its niche.

### Minor
- **Missing error bars / variance reporting.** The paper states results are "reported across three seeds" (line 207) but no variance measures appear in the described figures. For a benchmark others will use for comparison, reporting confidence intervals or standard deviations is important for assessing reliability.

- **Aggregated results hide per-task signal.** Results are grouped by cube count rather than shown per-task. Even when algorithms fail on average, per-task partial progress could reveal which reasoning skills are more accessible and provide diagnostic value.

- **Reward function details deferred entirely to appendix.** The paper mentions dense vs. sparse and permutation-variant vs. invariant rewards (Section 6) but provides no specifics in the main text. Reward design affects whether algorithm comparisons are fair, and a brief inline description of the default dense reward would help readers.

### Trivial
None

## Nice-to-Haves
- Analyze how agents fail in the self-supervised protocol (do they discover reusable sub-skills like stacking or grasping?). Skill emergence analysis would make results more compelling even at current performance levels.
- Provide a concrete pathway from supervised success to self-supervised success, since the supervised protocol is positioned as a "training wheels" stepping stone.
- More detailed comparison to Kinetix (2D procedural rigid-body tasks) would strengthen positioning.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Reward function details concern (appendix was stripped by parser; cannot verify if details are present in the original submission's appendix).
- Missing appendix content concerns (task list in Appendix E, speed comparisons in Appendix B, prompts in Appendix D—all referenced but stripped by parser).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add a taxonomy table of all 42 tasks with required skills, number of cubes, estimated difficulty, and solution horizon.
- Reframe the LLM evaluation as motivation for embodied interaction, removing the claim about LLM limitations through scaling.
- Include error bars in all figures and per-task breakdowns of results.
- Add a brief inline description of the default dense reward function.

## Calibration Report

**Round 1 bracket:** 4.0–7.0

**Round 2 narrowed:** 5.5–6.5

**All retrieved anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Watchmaker Functions (RrIjnSMhMZ) | 2.50 | 1 | Weaker — theoretical/speculative open-ended learning paper, rejected |
| Non-Parameterized Randomization (fvTaoyH96Z) | 2.33 | 1 | Weaker — narrow generalization technique, rejected |
| Training Video-Prompt RL (5f0n5yi8qK) | 3.40 | 1 | Weaker — rejected Minecraft RL paper with fundamental issues |
| MuJoCo Manipulus (b9Ne5lHJ8Y) | 3.40 | 1 | Weaker — rejected benchmark felt like engineering project, limited novelty and utility |
| MCU Generalist Agents (IWC6zUEVcL) | 4.00 | 1 | Weaker — rejected generalist agent benchmark with code/writing/overclaim issues |
| Training Reachable Tasks (X6W5eqhzDx) | 4.67 | 2 | Weaker — narrower contribution on exploration for generalization |
| ManiBox (VEdeDd13gx) | 5.25 | 2 | Comparable but slightly weaker — narrower manipulation generalization paper |
| VTDexManip (jf7C7EGw21) | 5.50 | 2 | Comparable — vision-tactile manipulation benchmark, less conceptual novelty |
| MORL Generalization (tuEP424UQ5) | 5.75 | 1 | Comparable — accepted benchmark paper with formalization, similar evaluation thinness |
| ManiSkill-HAB (6bKEWevgSd) | 5.75 | 2 | Comparable — GPU-accelerated manipulation benchmark, less diverse task design |
| AgentQuest (fp6t3F669F) | 6.25 | 2 | Similar quality — benchmark for LLM/VLM agents on long-horizon tasks |
| Robust Gymnasium (2uQBSa2X4R) | 6.50 | 2 | Similar — broader but less focused benchmark; BuilderBench has cleaner design |
| OGBench (M992mjgKzI) | 7.00 | 1 | Stronger — more complete evaluation with better diagnostic signal across 85 datasets |
| D3IL (6pPYRXKPpw) | 7.33 | 2 | Stronger — stronger evaluation and clearer methodology |
| GenSim (OI3RoHoWAN) | 8.00 | 1 | Stronger — novel LLM-based task generation with strong sim+real results |
| Thin-Shell (KsUh8MMFKQ) | 8.00 | 1 | Stronger — different scope, stronger contribution |
| Geometry-aware RL (7BLXhmWvwF) | 8.00 | 1 | Stronger — different scope, stronger methodology |
| PhysBench (Q6a9W6kzv5) | 8.00 | 1 | Stronger — VLM physical understanding, different scope |

**Positioning:** BuilderBench is clearly stronger than rejected benchmark papers (MCU at 4.0, Manipulus at 3.4) and comparable to accepted mid-range benchmark papers (MORL 5.75, ManiSkill-HAB 5.75, AgentQuest 6.25, Robust Gymnasium 6.50). It falls short of OGBench (7.00), which achieves more complete evaluation with better diagnostic signal. The paper's infrastructure contributions (fast simulator, curated task suite, open-source release) are genuine, but the evaluation gaps (incomplete task coverage, thin self-supervised results, overclaimed LLM section) prevent it from scoring higher. The score of 6.0 reflects a solid benchmark contribution that would benefit from more thorough evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>