Now I have all the information I need. Let me compile the final review.

---

**Round 1 bracket**: Based on calibration search, this paper sits between the weak anchors at 2.0-3.0 (papers with fundamental flaws, narrow scope, or poor execution) and the strong anchors at 7.5-8.0 (papers introducing major new methods or benchmarks). The plausible range is 4.5–6.5.

**Round 2 narrowing & anchor comparisons**: I examined several anchors in detail:

1. **"Bad Habits: Policy Confounding" (5.25, Reject)** — Similar in identifying a confound in RL, but had only toy experiments and unclear practical relevance. The current paper has broader, more convincing experiments (TORCS, KAREL, PARKING) and clearer practical implications. **The current paper is stronger.**

2. **"The Generalization Gap in Offline RL" (6.50, Accept)** — Thorough benchmark and experiments, but criticized for unsurprising results. The current paper has a more novel insight (identifying specific confounds) but less comprehensive experimental coverage. **Comparable but slightly weaker due to uneven execution.**

3. **"On Generalization Within MORL" (5.75, Accept)** — Introduces a benchmark and formalization, similar empirical scope. The current paper has a similar contribution type but slightly more novel findings. **Comparable.**

4. **"Harnessing Discrete Representations" (6.00, Reject)** — Empirical study of representations, limited to Minigrid. The current paper covers multiple domains which is stronger, but has weaker support for its second claim. **Comparable, slightly stronger on breadth.**

After comparing, I place the paper at **5.5**. The main experiments are solid and the re-evaluation findings are a genuine contribution, but the second contribution (memory-growing tasks) is under-supported, and several reporting gaps (selection bias, observation ambiguity) prevent a higher score.

---

## Summary

This paper re-evaluates claims in the literature that programmatic policies generalize better than neural policies in RL. Through controlled experiments on three benchmark domains (TORCS, KAREL, PARKING), the authors demonstrate that much of the reported gap stems from experimental confounds—specifically, reward shaping in TORCS and observation design in KAREL—rather than intrinsic representational advantages. The paper introduces an expressivity/discoverability framework to formalize this analysis and identifies a class of problems (requiring instance-scaling working memory) where programmatic representations may provide a genuine advantage.

## Strengths

- **Systematic identification of specific confounds in influential prior work.** Table 1 shows that DRL with a cautious reward (β=0.5) generalizes to OOD race tracks (76% from G-TRACK-1 to G-TRACK-2, 100% from AALBORG to ALPINE-2 and RUUDSKOGEN), directly contradicting the earlier narrative that neural policies consistently crash. This is a clean, reproducible finding with clear practical import for how these benchmarks are used.

- **Expressivity/discoverability framework (Definitions 2 and 3) provides a useful conceptual lens.** The paper cleanly separates the question of whether a representation *can* encode a generalizing solution (expressivity) from whether a search algorithm *can find* that solution (discoverability). This framework explains the experimental results: the DSLs and neural networks induce similar policy spaces (both are expressive), but the original experimental designs inadvertently favored discoverability in the programmatic space while hampering it in the neural space.

- **Simple architectural modification (augmenting observations with the last action) suffices to match LEAPS in KAREL.** Table 2 shows that PPO with a_{t-1} achieves perfect OOD generalization on 4 of 5 KAREL tasks (Stairclimber, Maze, TopOff, FourCorner) at 100×100, while the ConvNet and LSTM baselines from prior work collapse to near-zero. This is a striking empirical result that isolates the confound (observation design) from representation.

- **Honest reporting of mixed results.** The PARKING experiments (Table 3) are presented transparently, with the paper concluding that neither representation reliably generalizes OOD in this domain, rather than spinning the result.

## Weaknesses

### Major

- **The second contribution (memory-growing tasks) lacks RL experiments to match the strength of the claim.** Section 5 argues that programmatic representations have an inherent advantage for tasks requiring instance-scaling working memory. The paper provides a theoretical argument (fixed-capacity neural networks cannot encode Θ(|𝒱|) memory) and a proof-of-concept where FUNSEARCH (an LLM-based program synthesizer, not an RL program synthesis method) generates BFS for a wall-sparse maze. However, no existing RL program synthesis method (LEAPS, NDPS, PSM) is evaluated on this task, and no neural baseline is run on the modified maze to empirically demonstrate the claimed failure. The paper frames the result as a "proof-of-concept" but the abstract and introduction present it as a key contribution alongside the re-evaluation, creating a mismatch between presentation and evidence. This gap weakens what would otherwise be a clean narrative.

### Minor

- **TORCS generalization statistics are conditioned on training success, understating reliability differences.** The paper reports that 13/30 seeds (G-TRACK-1) and 4/15 seeds (AALBORG) successfully learned the training task, and generalization fractions are reported only over these successful seeds (e.g., 76% → 10/13 seeds). NDPS generalizes across all 3 seeds. While the raw training-failure numbers are transparently given (13/30, 4/15), the comparison would be more informative if overall reliability (treating training failures as non-generalizing) were also reported. As written, the paper's conclusion that neural policies "match" programmatic ones understates NDPS's advantage in reliability.

- **KAREL observation vector is not explicitly specified.** The paper states that "PPO with a_{t-1}" operates under partial observability and adds the last action to the observation, but never specifies whether the observation consists of the binary perception predicates from the DSL (frontIsClear, leftIsClear, etc.) or raw local grid cells. The caption of Table 2 says "uses a fully connected network with the observation space augmented with the agent's last action" without specifying the base observation. While the context suggests local grid cells, this is an important design detail that should be stated unambiguously for reproducibility.

- **HARVESTER failure case is not discussed.** Table 2 shows PPO with a_{t-1} achieves only 0.04 on 100×100 HARVESTER (LEAPS also scores 0.00, so neither method succeeds). The paper's narrative emphasizes that neural policies "match or exceed" programmatic ones, but this task is a failure case for both. A brief discussion of why HARVESTER differs from the other four tasks would strengthen the analysis.

- **Hyperparameter tuning is not discussed.** For a re-evaluation paper that challenges prior conclusions, it matters whether the neural baselines' hyperparameters were tuned separately per domain or adopted from prior work. A single sentence about the tuning budget would address this concern.

### Trivial

- The paper states it re-evaluates "Verma et al. (2018) and Verma et al. (2019) (PROPEL)" but the main-text experiments only use NDPS data. If PROPEL results exist in Appendix B (which is stripped by the parser), this is not an issue; if not, a brief justification would be helpful.

## Nice-to-Haves

- Report overall TORCS generalization treating training failures as crashes (i.e., fraction of all 30/15 seeds that both learn and generalize).
- Run LEAPS or NDPS on the wall-sparse Karel maze to test whether existing RL program synthesis methods can exploit the expressivity advantage claimed in Section 5.
- Add confidence intervals to Table 1 lap times, which vary across seeds.

## Removed Points

These points were flagged in the input reviews but are removed with justification:

1. **"Central claim about programmatic representations' inherent advantage is unsupported"** — Overstated. The paper explicitly frames Section 5 as a theoretical argument about *expressivity* and the FUNSEARCH result as a "proof-of-concept." It does not claim that existing RL program synthesis methods can discover BFS. The gap is real (noted as a Major weakness above) but the critic's framing that the entire claim is unsupported ignores the paper's careful scoping.

2. **"The paper overstates the memory argument because some problems have bounded memory"** — The paper acknowledges this explicitly: "Since all corridors of the maze are one-cell wide, wall-following strategies can solve this problem. The neural models considered in our experiments can encode a wall-following algorithm because such algorithms have a constant-memory requirement." The critic's concern is already addressed.

3. **"NDPS and PROPEL would not generalize conjecture is speculative"** — The paper says "We conjecture that NDPS and PROPEL would not generalize..." — it is explicitly labeled as a conjecture. This is not a weakness.

4. **"PROPEL experiments missing"** — The paper mentions "Appendix B" which is stripped by the parser; per instructions, this criticism cannot be verified and is removed.

5. **"Limited statistical rigor"** — Means and standard deviations are reported, which is standard in this literature. Not a genuine weakness.

6. **"Inconsistent number of seeds across methods"** — Transparently reported and explained. The asymmetric seed counts are not a flaw if the variance is discussed.

7. **"Missing related works"** — Per instructions, cannot be verified without external sources.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder both identified the same core contributions and limitations; no new insight emerged from their synthesis that the paper does not already articulate.

## Suggestions

1. **Add a clarifying sentence to Section 4.2** stating the exact observation vector for "PPO with a_{t-1}" (e.g., "a 3×3 binary grid of cells around the agent plus a one-hot encoding of the last action").

2. **In Table 1**, add a row showing overall generalization rate across all seeds (training failures treated as non-generalizing) alongside the conditional rate.

3. **Add a brief paragraph discussing HARVESTER** (Section 4.2) explaining why this task resists OOD generalization for both LEAPS and the neural baseline.

4. **Acknowledge the scope gap in Section 5** more explicitly: the proof-of-concept uses FUNSEARCH (an LLM-based synthesizer) rather than an RL-specific program synthesis method, and evaluating existing RL methods on this task is left to future work.

5. **Add a sentence about hyperparameter tuning** (e.g., "Hyperparameters for DRL methods were adopted from prior work without additional tuning") in Section 4.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>