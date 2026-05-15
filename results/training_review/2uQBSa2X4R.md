Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper introduces Robust-Gymnasium, a unified modular benchmark for robust reinforcement learning built on top of Gymnasium and other existing environment suites. It formalizes a Disrupted-MDP framework that encompasses three types of disruptors (observation, action, environment) operating in four modes (random, adversarial, internal dynamic shift, external disturbance) at different frequencies, and provides over 60 task bases spanning control, robotics, safe RL, and multi-agent RL. The paper also presents initial benchmarking experiments across standard RL, robust RL, safe RL, and multi-agent RL algorithms, as well as a demonstration of LLM-based adversarial disturbances.

## Strengths

- **Unified Disrupted-MDP framework**: The paper formalizes a single MDP extension integrating observation, action, and environment disruptors into one modular framework (Section 2). While conceptually straightforward, this unification is a genuine contribution — prior robust RL benchmarks and algorithms typically address only one disruption type in isolation, and the formalism cleanly captures all major robustness concerns in the literature.

- **Broad task coverage and modular design**: The benchmark provides over 60 task bases from 11 environment sets (Box2D, MuJoCo, Robosuite, MetaWorld, Safety Gymnasium, MAMuJoCo, etc.), spanning control, robotics, safe RL, and multi-agent RL (Section 3.1). The modular construction process (select task base → choose disruptor type/mode/frequency) is practically useful and enables flexible evaluation scenarios that go beyond what existing tools like RRLS (environment-shift-focused) offer.

- **Non-trivial algorithm comparisons in specific settings**: The experiments do yield some non-obvious findings — e.g., RSC demonstrates greater robustness than ATLA and DBC on Robosuite external-semantic-disturbance tasks (Section 4.2, Figures 6c-d), and PCRPO outperforms CRPO in safe RL under action/cost disturbances, with the interesting observation that "PCRPO's performance under disturbance surpasses its performance without disturbance" (Section 4.3). These go beyond the trivial finding that noise hurts performance.

## Weaknesses

### Fatal

None.

### Major

1. **Experimental validation is far too narrow for a benchmark paper claiming "comprehensive evaluation."** The paper benchmarks algorithms on only ~6 environments (HalfCheetah, Ant, Hopper, Walker2d, DoorCausal, LiftCausal, MA-HalfCheetah) out of the claimed 60+ task bases. Standard RL baselines (PPO, SAC) are tested on exactly one environment (HalfCheetah). Robust RL algorithms are evaluated on disjoint task sets — OMPO on Ant/Hopper with internal shifts, RSC/ATLA/DBC on Robosuite with external disturbances — making cross-algorithm comparison impossible. Safe RL and multi-agent evaluations each use a single task. For a benchmark paper, the minimal requirement is demonstrating that the benchmark can reveal meaningful distinctions across diverse settings with statistical rigor; the current experiments fall short of this bar. This is the paper's most significant limitation.

2. **Lack of statistical rigor in all experiments.** The paper reports no seed information, no multiple-run variance, no error bars, and no confidence intervals for any experiment. The text only describes qualitative trends ("performance degrades quickly"). In RL, variance across seeds is known to be high (Henderson et al., 2018; Colas et al., 2018), and single-run evaluations without any statistical characterization are insufficient to support the paper's claims about algorithmic deficiencies.

### Minor

3. **LLM-based adversarial attack is under-specified and under-evaluated.** The paper does not identify which LLM model was used (GPT-4? GPT-3.5? LLaMA?), provides no prompt template or details about how the LLM was instructed to generate perturbations, and compares only against uniform noise (not against gradient-based or random-objective attack baselines). The experiment uses a single environment (Ant-v4) and a single algorithm (PPO). The claim that this "illustrates the potential of LLMs in robust RL research" (abstract) is overstated given these limitations.

4. **Claims in the abstract and introduction overstate the experimental contribution.** The abstract claims "uncovering significant deficiencies in each and offering new insights," but the experiments mostly confirm the well-known fact that adding noise degrades performance. While there are genuinely interesting specific findings (RSC robustness, PCRPO improvement under disturbance), calling the evaluation "comprehensive" and the findings "significant deficiencies" inflates what is actually demonstrated.

5. **No comparison or positioning against RRLS (Zouitine et al., 2024).** The paper mentions RRLS once in the introduction as "a recent one focused on robustness to environment shifts" but never directly compares the two benchmarks — e.g., what specific tasks, disruptor types, or evaluation capabilities does Robust-Gymnasium offer that RRLS does not? A comparison table would help substantiate the claimed advantages.

### Trivial

None.

## Nice-to-Haves

- Performance profiles sweeping over continuous disruption intensities (e.g., varying noise std from 0 to 0.5) would strengthen the demonstration of algorithmic degradation patterns.
- Example trajectory visualizations comparing robust vs. non-robust policies under specific disruptions would help illustrate why the benchmark matters.
- Experiments combining multiple disruptors (e.g., observation noise + environment shift) would showcase the modular combinability that the paper highlights as a feature.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The claim of 'over sixty diverse task environments' is counting combinatorial variations, not validated tasks"** — The paper explicitly states "over 60 task bases from eleven sets" (Section 3, line 61), referring to base environments (MuJoCo tasks, Robosuite tasks, MetaWorld tasks, etc.), not combinatorial variations. The critic misread this.

- **"No baseline showing performance under no disturbance for context"** (safe RL section) — The paper explicitly states "PCRPO's performance under disturbance surpasses its performance without disturbance" (Section 4.3), confirming a no-disturbance baseline exists.

- **"Straightforward wrapper design, not a conceptual advance"** — This is overly dismissive of what is a legitimate benchmark/systems contribution. Many high-impact benchmarks are wrapper-based; the value lies in the unified formalization, modular implementation, and comprehensive coverage. The claim is weakened as a judgment, not fact.

- **"The mathematical framing does not add theoretical insight"** — The Disrupted-MDP is a formalization for engineering purposes, not a theoretical contribution. Criticizing it for not adding "theoretical insight" is scope creep; the formalism is clear and serves its purpose.

- Several of the "Section-by-section notes" items (e.g., the claim about Section 2 lacking theoretical insight) are essentially the same point rephrased as a section note. These are consolidated into the weaknesses above.

## Novel Insights

The reviews surface a core tension: the paper's benchmark design is genuinely useful and fills a real gap (no existing benchmark unifies observation, action, and environment disruptions across standard RL, safe RL, and multi-agent RL in a modular way), but the experimental validation is too shallow for the paper to convincingly demonstrate the benchmark's value. Notably, the RSC vs. ATLA vs. DBC comparison on Robosuite tasks (Section 4.2) is the kind of meaningful algorithmic differentiation a robust RL benchmark should enable — but it's confined to two tasks with three algorithms, leaving the reader to wonder whether similar patterns hold more broadly. The LLM adversary experiment, while creative, is presented as a "featured" contribution but lacks the specification and baselines needed to be reproducible or properly assessed.

## Suggestions

1. **Expand experimental scope substantially** — at minimum, evaluate 2-3 algorithms across a representative sample of 3-5 environments from each of the major domains (control, robotics, safe RL, multi-agent RL), with standardized disruption configurations.

2. **Run all experiments with 5+ seeds and report mean ± std or interquartile ranges** — this is essential for any RL evaluation to be credible, especially for a benchmark intended for community adoption.

3. **Ensure robust RL algorithms are compared on shared tasks** — e.g., run OMPO, RSC, ATLA, and DBC on the same set of environments with the same disruption types so the benchmark can demonstrate which algorithms are more robust.

4. **Specify LLM details** — state which model was used, provide the prompt template, and compare against at least one additional attack baseline (e.g., gradient-based or random-objective attacks).

5. **Add a positioning table or section comparing Robust-Gymnasium to RRLS** along dimensions like disruption types covered, supported environment suites, safe/multi-agent support, and modularity features.

## Score and Decision

**Originality**: 6/10 — The Disrupted-MDP framework is a useful unification but not a deep conceptual breakthrough. The benchmark's breadth across domains is its main novelty.
**Importance of research question**: 8/10 — Standardized robust RL benchmarks are genuinely needed.
**Claims supported**: 4/10 — Claims of "comprehensive evaluation" and "significant deficiencies" are not well-supported by the experiments.
**Soundness of experiments**: 3/10 — Too narrow in scope, no statistical rigor, disjoint algorithm comparisons.
**Clarity of writing**: 7/10 — The framework and benchmark design are clearly explained.
**Value to community**: 7/10 — The benchmark itself would be useful if better validated; the current version has potential.

The benchmark design is a legitimate contribution that fills a gap, but the experimental validation is substantially insufficient for a benchmark paper. The paper would benefit from major revisions to expand and strengthen the experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>