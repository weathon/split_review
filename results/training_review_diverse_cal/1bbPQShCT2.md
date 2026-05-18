Now I have all the information I need to synthesize the final review. Let me carefully construct it.

---

## Summary

This paper introduces I-PHYRE, a benchmark for interactive physical reasoning that requires agents to (1) reason intuitively about physics, (2) plan multiple sequential interventions, and (3) execute actions with precise timing — a combination missing from prior benchmarks like PHYRE (single-step) and SMP (computational, not intuitive). The benchmark comprises 40 games across four splits (basic, noisy, compositional, multi-ball) targeting different generalization abilities. The paper evaluates several RL and supervised agents with three planning strategies (in-advance, on-the-fly, combined) and provides human baselines from 46 participants. The results show a substantial gap between current learning algorithms and human performance.

## Strengths

- **First benchmark combining intuitive physics, multi-step planning, and in-situ timing.** Table 1 systematically contrasts I-PHYRE with prior work, showing that only I-PHYRE jointly requires intuitive mechanism, rich dynamics, multi-step planning, action order, and action timing. This fills a clear gap: PHYRE allows only single-step interactions, and SMP (Toussaint et al., 2018) uses computational rather than intuitive reasoning and lacks rich dynamics.

- **Deliberate split design targeting specific generalization abilities.** The four splits (basic, noisy, compositional, multi-ball) are designed to isolate distinct capabilities: resilience to distractors, composition of known routines, and simultaneous handling of multiple dynamic objects (Section 3.1, Figure 1). This enables targeted diagnosis of agent weaknesses beyond aggregate performance.

- **Controlled human baseline with a reasonable participant pool.** The paper recruits 46 participants with standardized instructions, a 15-second time limit per attempt, and up to 5 attempts per game (Section 4.1). The resulting data (humans achieving 83–92% success across splits, oracle near 100%) establishes that the games are solvable and provides a meaningful reference point.

- **Concrete analysis of why current RL agents fail.** Section 5.1 identifies three specific obstacles: lack of explicit physics understanding in model-free agents, difficulty with delayed rewards in multi-step settings, and sensitivity to precise action timing (where no-ops dominate on-the-fly policies). This analysis grounds future work in tangible challenges rather than generic speculation.

## Weaknesses

### Fatal
None.

### Major

1. **Unequal evaluation protocols confound the human–agent comparison.** Humans receive five attempts per game (line 183), while RL agents are evaluated zero-shot with a single rollout (Section 4.2). Because humans can learn from failure within each game instance, the observed "gap" conflates interactive physical reasoning ability with trial-and-error within the episode. The gap is large (humans ~90% success vs. best RL ~40%), so the asymmetry is unlikely to fully explain it, but the headline claim about "notable gap" would be substantially strengthened by equitable protocols (e.g., best-of-5 for agents, or single-attempt for humans).

2. **Missing forward-model/search baseline.** No non-learning planner that exploits the simulator as a perfect forward model is included (e.g., BFS or simple search over action sequences). Such baselines are standard in physics benchmarks (e.g., PHYRE) and would bound the problem, isolating whether poor RL performance stems from learning inefficiencies vs. the benchmark's intrinsic planning/timing demands. Model-based RL agents (deferred to supplement) do not fill this gap because they learn an imperfect model.

3. **Lack of statistical rigor in RL experiments.** The paper presents results (Figure 2, Figure 3) without any indication of variance, number of runs, or statistical significance. RL algorithms are notoriously sensitive to random seeds and hyperparameters. The paper makes comparative claims such as "DDPG-I struggle to outperform even random agents" and "agents using planning in advance converge more swiftly" without error bars or multiple seeds. This undermines the reliability of all quantitative conclusions in Section 4.2.

### Minor

4. **Oracle defined by experimenter performance, not provably optimal.** The "oracle" scores (Table 2) are "scores achieved by the experimenters" (line 188), not theoretical maxima derived from the reward function. The claimed upper bounds (968–976) may not be tight, making it unclear how close humans or agents are to true optimality.

5. **Implementation details of planning strategies are too sparse to reproduce.** For example, how the "planning in advance" agent handles a variable number of blocks is unclear (fixed-length action sequence? predicting indefinite length?). The description "action space aligning with the timings at which blocks are eliminated" (line 157) is ambiguous when the number of blocks varies across games.

6. **Novelty distinction from SMP is fragile.** Table 1 marks SMP as having multi-step, action order, and action timing — the three features considered most central to interactivity — and distinguishes I-PHYRE only on "mechanism" (intuition vs. computation) and "rich dynamics." Since "intuitive vs. computational" is as much a property of the agent as of the benchmark, the paper should argue more carefully why I-PHYRE's combination is substantively novel beyond what SMP already covers.

7. **Split design characterization is limited in the main text.** The paper describes splits conceptually (Section 3.1) but provides no quantitative characterization (e.g., minimal number of steps, timing tolerance, distribution of physical concepts per split). While details may exist in the supplement, the main text gives the reader insufficient information to assess whether the splits actually isolate the claimed abilities.

### Trivial
None.

## Nice-to-Haves

- A release statement with URL, license, and usage instructions would make the benchmark immediately usable by the community.
- Per-game performance breakdown would help diagnose specific failure modes for agents vs. humans.
- Hyperparameter tables and training details for all RL agents would aid reproducibility.
- Ablation of reward components (time penalty weight, block-removal penalty) would clarify behavioral sensitivity.

## Removed Points

- **"No URL, license, or usage instructions"** (from Harsh Critic's Missing Parts): Removed per Hard Rule that criticisms about release status/availability of cited entities should be removed. However, since the benchmark is the paper's own contribution (not a cited entity), this is not strictly covered by the rule — moved to Nice-to-Haves instead.
- **"The supplement is not visible in this review"** language: Removed per Hard Rule about missing appendix/parser artifacts.
- **"LLM experiments mentioned speculatively in limitations"**: The paper explicitly states these are "preliminary studies" deferred to the supplement (line 296). This is appropriate framing for a benchmark paper whose scope is not LLM evaluation. Moved to Nice-to-Haves.
- **Weakness about "generic reproducibility" (full training logs, complete hyperparameter tables)**: These are large artifacts impractical to include in a conference submission. The paper already references a supplement for training details.
- **Strength claiming generic importance of the problem**: The Strength Finder's framing of "addressed an important problem" is too generic — the strength is better captured by the specific comparison in Table 1 and the concrete gap in existing benchmarks.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a key tension that the authors do not fully grapple with: the benchmark's timing demands inherently favor methods that reason quickly (intuitive physics), but existing RL agents are evaluated on their ability to *learn* this timing through reward feedback. This creates a mismatch between what the benchmark measures (the capability to produce timed sequences of actions) and what it claims to measure (interactive physical *reasoning*). To truly isolate reasoning, a planner with a perfect forward model is needed — without it, the "gap" between humans and agents conflates at least three distinct challenges: exploration, credit assignment over long horizons, and the actual physical reasoning required. Future work should design ablation experiments that tease these apart.

## Suggestions

1. **Equalize the human and agent evaluations.** Run all agents with best-of-5 rollouts per game (matching the human protocol) and report whether the gap narrows. Alternatively, restrict humans to a single attempt. Both approaches would make the headline comparison interpretable.
2. **Add a forward-model baseline.** Implement a simple tree search or BFS planner that uses the physics simulator as a perfect forward model. This would bound the problem and clarify whether the benchmark's difficulty is primarily in learning or in planning.
3. **Run all RL experiments with at least 5 random seeds and report means ± std.** This is a minimal requirement for making quantitative comparative claims in a benchmark paper.
4. **Provide quantitative characterization of each split.** Show per-split statistics: average minimum steps to solution, timing tolerance (frames of error acceptable), types of physical concepts involved. This would help the community understand what each split truly tests.
5. **Strengthen the novelty argument relative to SMP.** Acknowledge that SMP shares multi-step, action order, and timing features, but emphasize that I-PHYRE requires *intuitive* (fast, approximate) reasoning due to tight timing constraints and enriches dynamics (falling, rotation, collision, friction, pendulum, elastic motion) in ways that SMP does not.

## Score and Decision

**Originality**: High — the benchmark fills a genuine gap in interactive physical reasoning evaluation.  
**Importance of research question**: High — interactive physical reasoning is a fundamental capability for embodied agents.  
**Claims well supported**: Low — the central human–agent comparison is confounded by unequal protocols, and agent comparisons lack statistical rigor.  
**Soundness of experiments**: Medium — the human study is well-designed, but the RL experiments have significant methodological gaps.  
**Clarity of writing**: Medium — generally clear but sparse on implementation details.  
**Value to the research community**: Medium-High — the benchmark itself is valuable, but the evaluation needs strengthening to make the paper's claims credible.

Overall, the paper presents a genuinely novel and well-motivated benchmark that addresses a clear gap in existing physical reasoning evaluations. The core idea is valuable. However, the experimental validation has three major issues (unequal human/agent protocols, missing forward-model baseline, lack of statistical rigor) that directly affect whether the central claims about the human–agent gap can be accepted. These are fixable but require substantial reanalysis. In its current form, the paper's evaluation is not sufficiently rigorous to support its main conclusions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>