## Summary

This paper re-evaluates claims that programmatic policies generalize better than neural policies in RL across three benchmarks (TORCS, KAREL, PARKING). The authors show that when experimental confounds are controlled — a cautious reward function for TORCS, partial observability plus last-action augmentation for KAREL — neural policies match or exceed the OOD generalization of programmatic ones. They then introduce an expressivity/discoverability framework and argue that programmatic representations offer a genuine advantage when solutions require working memory scaling with input size (e.g., pathfinding requiring BFS), supported by a proof-of-concept using FUNSEARCH to synthesize BFS for a modified KAREL maze.

---

## Strengths

1. **TORCS reward confound isolated cleanly (Table 1).** DRL with β=0.5 generalizes to OOD tracks (e.g., 1:48 on G-TRACK-2 vs. NDPS's 1:40), while DRL with β=1.0 crashes on every OOD track. This directly demonstrates that the prior gap was caused by the speed-optimization reward signal, not representational superiority. The paper correctly notes that the reward is intrinsic (Equation 2 defines training signal, not evaluation metric), so changing β does not change the problem being solved.

2. **KAREL: Simple architectural change closes the gap (Table 2).** PPO with the agent's previous action (a_{t-1}) achieves 1.00 return on 100×100 versions of Stairclimber, Maze, TopOff, and FourCorner, matching LEAPS. The LSTM and ConvNet baselines from prior work drop to near-zero on the same test instances (0.00–0.04). This cleanly shows the prior gap was due to architectural choices — the LSTM used in prior work was poorly suited to the partial-observability setting — rather than a fundamental representational limitation of neural policies.

3. **Expressivity-discoverability framework (Definitions 2 and 3, Section 5).** Provides a crisp decomposition: a representation must both *contain* a generalizing solution (expressivity) and be *searchable* enough to find it (discoverability). This explains why the confounds in prior work mattered — gradient search could not achieve discoverability under the original training setup — and makes testable predictions about when programmatic representations should genuinely outperform neural ones (when expressivity fails due to fixed memory capacity).

4. **Principled fixed-memory limitation argument (Section 5).** The Ω(log|V|) lower bound for vertex indexing establishes that constant-capacity neural policies cannot encode exact pathfinding algorithms like BFS that need Θ(|V|) memory. This is more rigorous than typical generalization arguments in RL and correctly identifies a genuine architectural limitation rather than a training-pipeline artifact.

5. **Honest treatment of PARKING (Section 4.3, Table 3).** The paper reports that neither PSM nor DQN reliably generalizes, with DQN having higher absolute test success rate (0.18 vs. 0.16) but PSM having a smaller generalization gap (0.10 drop vs. 0.68). Not overclaiming a winner here strengthens the credibility of the positive findings on TORCS and KAREL.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **FUNSEARCH proof-of-concept is too thin to carry much weight.** Three runs of FUNSEARCH returning "a correct implementation of breadth-first search" for one modified KAREL maze is reported without: systematic evaluation across maze sizes or topologies, quantitative success rate (3/3? or were failed runs discarded?), comparison against any neural baseline (e.g., Transformer, stack-RNN, Neural Turing Machine), verification methodology, or discussion of computational cost. The paper's broader claim about programmatic superiority for memory-scaling problems is theoretically sound, but the empirical component is merely illustrative. Given that the paper explicitly frames this as a "proof-of-concept," this weakness does not undermine the core re-evaluation claims.

2. **Limited analysis of why LSTMs fail in KAREL.** The paper attributes LSTM failure to being "more complex to train" (Section 4.2) but does not investigate the root cause. Given that LSTMs achieve only 0.13 on small Stairclimber while PPO with a_{t-1} gets 1.00, the failure seems deeper than training complexity. The LSTM also gets 1.00 on small Maze but 0.00 on large — suggesting task-specific failure modes that the paper does not explore. This is a missed opportunity for the discoverability analysis.

3. **No statistical significance tests across conditions.** Especially for PARKING, where conclusions hinge on interpreting differences between PSM and DQN, the paper would benefit from bootstrap or permutation tests. The 95% confidence intervals reported for PARKING help but do not address between-condition comparisons. For TORCS, the fraction-of-seeds metric (e.g., 76% generalized from G-TRACK-1 to G-TRACK-2) is informative but also lacks uncertainty quantification.

4. **Seed filtering in TORCS could introduce selection bias.** 13 of 30 DRL(β=0.5) seeds learned G-TRACK-1 and were evaluated on OOD tracks; 17 were excluded. The paper is transparent about this, but does not report outcomes when all 30 models (including non-learners) are evaluated on test tracks. If the inability to learn the training task correlates with optimization instability, the reported OOD generalization rate may be optimistic.

### Trivial
None.

---

## Nice-to-Haves

- Running programmatic methods under the modified conditions (NDPS with β=0.5, LEAPS with last-action augmentation) would further strengthen the confound analysis, although the current evidence already supports the main claims without these controls.
- Adding at least one neural baseline to the FUNSEARCH experiment (e.g., a stack-RNN or Transformer trained on the wall-sparse maze) would make the memory-capacity argument more empirically grounded.
- An ablation on the role of the last-action signal in KAREL — does PPO with a_{t-1} still generalize on 100×100 without the last action but with LSTM? — would help isolate whether the improvement comes from the added signal or the simpler optimization.

---

## Removed Points

These points from the inputs were removed with justification:

**"Asymmetric comparison undermines central re-evaluation claim" (Harsh Critic).** The critic claimed TORCS compares NDPS(β=1.0) vs DRL(β=0.5) asymmetrically. This misreads the paper's methodology. The paper's hypothesis is that the speed-optimization reward was the confound, tested by showing DRL(β=1.0) crashes while DRL(β=0.5) generalizes. This is a valid causal demonstration. Running NDPS(β=0.5) would test a different question (whether NDPS also benefits from slower speed) that is orthogonal to the paper's claim. **Removed: strawman — misunderstands the paper's causal methodology.**

**"KAREL comparison frame shifted" (Harsh Critic).** The critic claimed PPO with a_{t-1} uses richer observations than LEAPS's Boolean sensors and that the sparsity explanation is contradictory. The paper uses "fewer input features" to mean partial observability (local cells) vs. the full grid used by the ConvNet baseline — not comparing to LEAPS's sensor set. PPO with a_{t-1} operates in the same partial-observability setting as LEAPS. The critic conflated two different comparisons. **Removed: factually wrong — misunderstands what the paper compares.**

**Missing related works.** Hard rule: cannot mention missing related works. **Removed.**

**Formatting/style nitpicks.** Hard rule: parser artifacts and formatting issues must be removed. **Removed.**

**Generic/superficial strengths about problem importance (Strength Finder).** **Removed.**

---

## Novel Insights

The most distinctive observation emerging across the reviews is the asymmetric failure pattern in KAREL: PPO with a_{t-1} achieves perfect 1.00 on 100×100 versions of Stairclimber, Maze, TopOff, and FourCorner, but only 0.04 on HARVESTER. This suggests that the last-action augmentation interacts with task structure in ways the paper's sparsity explanation does not fully capture. HARVESTER involves picking markers, which may require different memory patterns than wall-following navigation tasks. Neither the paper nor the reviews probe why HARVESTER remains hard when structurally similar tasks become trivial — this could point to a limitation in the neural approach that the paper attributes entirely to confounds elsewhere. Understanding this asymmetry could sharpen the discoverability analysis.

---

## Suggestions

1. Expand the FUNSEARCH proof-of-concept: report success rate across multiple runs (was it genuinely 3/3?), evaluate across different maze sizes and topologies, and include at least one neural baseline (stack-RNN or Transformer) on the wall-sparse maze.
2. Add an ablation testing LEAPS with the last action as an additional perception function in the DSL — this would directly test whether the programmatic advantage was an observation-space artifact.
3. Analyze why HARVESTER resists the a_{t-1} augmentation when the other four KAREL tasks achieve perfect generalization — this could reveal a more fundamental limitation.
4. Add bootstrapped significance tests for between-condition comparisons, especially for PARKING.
5. Report TORCS OOD results with all 30 seeds included (treating non-learners as failures) to bound possible selection bias.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NGVljI6HkR — "Reclaiming the Source of Programmatic Policies" | 3.67 | R1 low | Our paper is clearly stronger: broader scope (3 domains vs 1), cleaner methodology, conceptual framework |
| 473sH8qki8 — "Reward as Observation" | 2.00 | R1 low | Not directly comparable; different subfield, much weaker |
| fvTaoyH96Z — "Non-Parameterized Randomization" | 2.33 | R1 low | Not directly comparable; weaker methodology |
| lUWf41nR4v — "Addressing Long-Horizon Tasks / POMP" | 4.50 | R1 mid | Comparable domain (programmatic RL) but our evidence is cleaner; our paper is somewhat stronger |
| PH7ja3T0vN — "State Combinatorial Generalization" | 4.50 | R1 mid | Different topic; similar quality level |
| ehSQZa4vuk — "Bad Habits: Policy Confounding" | 5.25 | R2 narrow | **Most similar conceptually** — both identify confounds in RL generalization. Our paper is stronger: uses real published benchmarks (TORCS, KAREL) rather than toy gridworlds; provides multiple domains; adds conceptual framework. Our paper is ~1 point stronger |
| tuEP424UQ5 — "On Generalization Within MORL" | 5.75 | R2 narrow | Comparable contribution type (framework + evaluation). Slightly less clean empirically; our paper is marginally stronger |
| X1p0eNzTGH — "Level Sampling Process impacts ZSG" | 5.67 | R2 narrow | Related topic (generalization confounds). Similar quality; our paper has clearer positive findings |
| UfczlMudN6 — "GRAM: Generalization in Deep RL" | 6.00 | R1 mid | Different genre (new method); comparable experimental quality |
| QiUitwJDKI — "InnateCoder" | 5.75 | R2 narrow | Programmatic options with LLMs; similar domain, our paper has cleaner empirical results |
| 3w6xuXDOdY — "Generalization Gap in Offline RL" | 6.50 | R2 narrow | Benchmark paper; stronger empirical scope |
| OI3RoHoWAN, pISLZG7ktL, 9pW2J49flQ, etc. (8.00s) | 8.00 | R1 high | Not comparable — large-scale system papers or theoretical contributions with much stronger empirical scope |

**Round 1 bracket:** 4.0 – 6.5. **Round 2 narrowing:** The paper is clearly stronger than ehSQZa4vuk (5.25) and NGVljI6HkR (3.67), comparable to tuEP424UQ5 (5.75, accepted) and UfczlMudN6 (6.00, rejected). It is weaker than the 6.5+ papers due to the thin proof-of-concept and lack of significance testing. Final score positioned between tuEP424UQ5 (5.75) and 3w6xuXDOdY (6.50).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>