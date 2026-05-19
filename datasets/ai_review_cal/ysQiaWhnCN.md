- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have a thorough understanding of the paper and both reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces Autoverse, a domain-specific language for 2D grid-based games whose rewrite rules are implemented as convolutions, enabling GPU-parallelized simulation via JAX. The paper also proposes a warm-starting pipeline for open-ended reinforcement learning: evolve environments via tree search → collect playtraces → imitate via behavior cloning → fine-tune with PPO while adaptively evolving new environments. The submitted paper only evaluates the behavior cloning component; the RL stage of the claimed pipeline is described but not executed, and the abstract's assertion that the approach "improves the performance and generality of resultant player agents" is entirely unsupported. The Autoverse DSL design is a genuine technical contribution, but the experimental scope falls far short of what the paper advertises.

## Strengths

1. **Convolutional rewrite-rule formalization enables GPU-batched simulation of diverse game mechanics.** Section 2.1 formalizes environment dynamics as a series of convolutions and transposed convolutions (Eq. 1–3), allowing forward simulation to run in parallel on the GPU. This is a clean, principled extension of PuzzleScript-like rewrite rules into a differentiable, hardware-accelerated setting, and is the paper's strongest technical contribution.

2. **Evolutionary algorithm co-evolves rules, rewards, and initial layouts.** Section 2.2 describes a μ+λ evolution strategy that mutates input/output patterns of rewrite rules, associated reward values, and the initial map layout simultaneously, using search-depth as a fitness signal. This goes well beyond layout-only PCG and is a well-motivated approach for generating diverse environment dynamics.

3. **Empirical evidence that rule-set visibility aids imitation learning.** Tables 1 and 2 (described in text) show that agents observing the environment's rule set outperform agents with zero-padded rule slots, and that larger observations improve BC performance. This supports the claim that evolved environments have sufficiently distinct mechanics that a rule-agnostic policy cannot generalize.

## Weaknesses

### Fatal

1. **The paper's central claim is entirely unsupported by experiments.** The abstract asserts that the full warm-starting pipeline (imitate search → RL + adaptive environment evolution) yields improved performance and generality, and the title and introduction frame this as the paper's main contribution. However, the Results section (Section 3) contains **only** behavior cloning experiments (observation size and rule visibility ablations) and qualitative rollout analysis. There are zero experiments showing that warm-starting improves downstream RL, zero comparisons of the full pipeline against any baseline (e.g., PPO from scratch, UED from scratch), and zero quantitative evaluation of the adaptive environment-evolution stage. The conclusion effectively admits this: *"Future work will study how this data can be used to jump-start a generalist reinforcement learning game playing agent"* (line 304). A paper that claims a result and provides no evidence for that result has a structural flaw that invalidates its core contribution as advertised.

### Major

1. **Absence of the RL evaluation invalidates the paper's central claim.** Even setting aside the abstract's overstatement, the paper describes a two-stage method (BC → RL) but only evaluates the first stage. Without evidence that the imitation-learned policy actually improves subsequent RL, the method is an untested proposal, not a validated contribution. Related work comparisons (PAIRED, UED) are invoked but never empirically contrasted.

2. **Method details are critically underspecified for reproducibility.** Several aspects cannot be reconstructed from the description:
   - The search algorithm is called "best-first search" in one sentence and "breadth-first search" in the next (line 236), with "greedy tree search" used elsewhere — these are different algorithms.
   - The search budget increase criterion is described as being triggered when an environment's solution "approach[es] this limit to some degree" — a vague threshold.
   - All hyperparameters are absent: population size, mutation rates, PPO hyperparameters, the interval \(k_{evo}\), network architectures.
   - The observation patch size for BC is not specified; it is described as "local" (line 242) but Table 1 includes a "full observation" condition whose dimensions are not given.
   - The value function used for regret-based environment evolution (Section 2.3) is not explained — how it is learned alongside the policy, whether it is updated during evolution, and how its error is aggregated over an episode are all unspecified.

3. **No systematic characterization of Autoverse as a benchmark.** The paper claims Autoverse "stands out for allowing more complex environment dynamics and much more environmental diversity" (line 20) and positions it as a "scalable testbed for open-ended learning algorithms" (line 302), but provides no quantitative comparison to existing OEL environments (POET, XLand, Neural MMO, Procgen, GVG-AI, etc.) on any metric: diversity, simulation speed, coverage of game types, or downstream agent performance. The qualitative stable/chaotic analysis is interesting but does not substitute for systematic characterization.

4. **No baselines for the BC experiments.** The behavior cloning results show performance variation with observation size and rule visibility, but there is no comparison against any alternative approach (e.g., imitation from random trajectories, a scripted agent, or a model-free baseline). The reader cannot judge whether the absolute performance levels are good, or whether imitation from search data is beneficial at all.

### Minor

1. **Editing artifacts remain in the submission.** Lines 181, 217, and 221 contain `\sam{...}` notes (e.g., *"This section was condensed by Eugene, in whom I trust"*, *"we could probably lose this"*), which are clearly internal editing marks that should have been removed. While these do not affect the technical content, they undermine the paper's polish.

2. **Test environments not described.** The BC results refer to "test environments (environments also generated by the evolutionary process, but held out for testing)" (line 269), but no information is given about how many test environments were used, how they were selected, or whether they come from the same distribution as training environments.

3. **Nash equilibrium claim is unjustified.** Section 2.3 asserts that the generator-player game "converges to a Nash equilibrium" (citing Dennis et al. 2020), but the generator here is an evolutionary algorithm, not a learned policy. The paper does not explain how the theoretical guarantees from PAIRED apply to this setting, making the claim unsupported.

### Trivial

1. **Search terminology inconsistency.** The algorithm is referred to as "greedy tree search," "best-first search," and "breadth-first search" in different places (lines 5, 22, 127, 158, 165, 236), which is confusing.

## Nice-to-Haves

- A quantitative analysis of the evolved environment space (e.g., embedding environments by dynamics similarity, measuring coverage of distinct game types, tracking rule discovery over evolution) would substantially strengthen the claim that Autoverse supports rich diversity.
- Ablations on the evolutionary algorithm (e.g., comparing different mutation operators, fitness functions) would help validate the design choices.
- Even a small-scale pilot of the RL warm-starting stage (e.g., comparing BC-initialized PPO vs. cold-start PPO on a handful of evolved environments) would go a long way toward supporting the main thesis.

## Removed Points

These points are flagged to be removed from consideration; treat them with caution.

- **"The two tables included via \include{} are not visible"** — This is a PDF extraction artifact; the surrounding text clearly describes the tables' content and conclusions. The tables exist in the original submission.
- **"The paper would benefit from removing the BC experiments entirely"** — This is an overcorrection; the BC experiments are valid and support the auxiliary claim that rule visibility matters. The issue is the missing RL evaluation, not that the BC experiments shouldn't exist.
- **"Missing related works"** (GVG-AI, PCGRL, Obstacle Tower, CoinRun, Neural MMO) — The paper does cite several of these (Obstacle Tower, CoinRun, Neural MMO appear in Section 4, line 295). The claim about "few existing benchmarks" is a debatable opinion, not a factual error. Moreover, the "do not mention missing related works" rule applies.
- **"The possible extensions subsection is disconnected"** — This is a presentation preference; the content about scalar flows and counting is relevant to future expressivity. The editing note is a formatting issue.
- **Strength from Strength Finder about value function error / regret theory** — The paper claims this connection but does not adapt the proof to its evolutionary generator setting, making the strength overstated. The criticism about unjustified Nash equilibrium claim (Minor weakness #3) correctly identifies the gap.
- **Strength Finder claims about "directly supporting the paper's diversity claim"** — The BC rule-visibility experiments provide suggestive evidence, but do not constitute a systematic diversity analysis. The strength is kept in weakened form (Strength #3).

## Novel Insights

None beyond the paper's own contributions. The two reviews surface the same core gap (promised experiments not delivered) and the same genuine contribution (convolutional rewrite-rule DSL) but do not offer a new perspective on the paper's ideas or methodology beyond what is already present.

## Suggestions

1. **Either remove the abstract's unsupported claim** or run the RL warm-starting experiments and report them. The paper as written claims a result ("finding that this approach improves the performance and generality of resultant player agents") that is not present anywhere in the manuscript. This is the single most important fix.
2. **Add a clean comparison** of the full warm-starting pipeline (BC → RL + adaptive evolution) against at least two baselines: (a) PPO from scratch on random Autoverse environments, and (b) PPO from scratch with the adaptive evolution (UED-style) but without BC pre-training.
3. **Specify all missing hyperparameters and implementation details** (population size, mutation rates, PPO parameters, network architectures, \(k_{evo}\), observation sizes) for reproducibility.
4. **Resolve the search-terminology inconsistency** ("greedy tree search" vs. "best-first" vs. "breadth-first") and precisely define the pruning criterion and budget-increase rule.
5. **Add a quantitative characterization of Autoverse's environment diversity** — e.g., measuring the number of distinct rule-sets discovered, clustering environments by their dynamics, or comparing simulation throughput against a standard CPU-based alternative.
