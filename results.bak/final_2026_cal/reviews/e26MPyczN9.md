## Summary

This paper re-evaluates prior claims that programmatic policies generalize out-of-distribution (OOD) better than neural policies in RL. Across three benchmarks (TORCS, Karel, Parking), the authors show that neural policies can match or exceed programmatic generalization when experimental confounds are controlled (reward shaping, observation design). They introduce an expressivity/discoverability framework to explain these results, and argue that the genuine advantage of programmatic representations lies in tasks requiring working memory that grows with input size — providing a proof-of-concept via FUNSEARCH synthesizing BFS. The re-evaluation is thorough and the framework is clear, though the positive claim about memory-scaling tasks is supported by theory and proof-of-concept rather than a direct empirical comparison.

## Strengths

- **Systematic re-evaluation across three influential benchmarks with strong evidence.** Table 1 shows DRL with β = 0.5 achieves OOD generalization on TORCS tracks (76% of models on G-TRACK-2, 69% on E-ROAD), closing the gap previously attributed to representation. Table 2 shows PPO with last-action augmentation matches LEAPS on 100×100 Karel grids on 4/5 tasks. Both results are backed by multi-seed runs, directly refuting the claim of inherent programmatic superiority in these domains.

- **Clear theoretical framework (expressivity/discoverability) that explains both the re-evaluation results and the boundary conditions for genuine programmatic advantage.** Definitions 2 and 3 decompose OOD generalization into two independent requirements, providing a principled explanation for why prior comparisons were confounded (both representations were expressive, but discoverability was uncontrolled for neural models).

- **Identification of memory-scaling tasks as the class where programmatic representations provide a principled advantage.** The argument that fixed-capacity neural architectures cannot encode algorithms with instance-growing working memory (e.g., BFS with Θ(|V|) frontier/visited sets) is well-reasoned and grounded in computational complexity. This provides a concrete criterion for future research.

- **Proof-of-concept that programmatic synthesis can produce provably generalizing solutions for memory-scaling tasks.** FUNSEARCH with Qwen 3‑Coder synthesizes a correct BFS implementation for a wall-sparse Karel maze, demonstrating the feasibility of obtaining formal OOD guarantees via programmatic representations.

## Weaknesses

### Major

- **The claim that "commonly used neural architectures cannot encode a solution to this type of problem" (abstract, Section 5) is stronger than the evidence provided.** The paper argues this theoretically through capacity bounds (expressivity), which is sound, and demonstrates that programmatic synthesis *can* produce such solutions. But no experiment directly tests whether standard neural policies (feedforward, LSTM, or the last-action-augmented model that worked on Karel) *fail* on the wall-sparse maze task. The theoretical argument is credible, but an empirical demonstration of neural failure on the same task used for the programmatic proof-of-concept would substantially strengthen the central positive claim. As written, the paper convincingly shows that programmatic representations *can* express growing-memory algorithms, but does not empirically demonstrate that neural ones *cannot*.

### Minor

- **The TORCS re-evaluation compares new neural results (β = 0.5) against original NDPS results without training programmatic policies under the same modified reward.** The paper acknowledges this asymmetry and labels the counterfactual as a conjecture (Section 4.4: "We conjecture that NDPS and PROPEL would not generalize…"), but the comparison remains asymmetric. Training NDPS with β = 0.5 would sharpen the conclusion regardless of outcome.

- **The HARVESTER failure is not analyzed.** PPO with a_{t-1} achieves only 0.04 return on 100×100, which is the one task where the simple neural approach fails. Since the paper's framework classifies Karel tasks as solvable by constant-memory heuristics, the HARVESTER result deserves discussion — does it actually require growing memory, or does the failure stem from discoverability? This omission weakens the paper's own taxonomy.

- **The FUNSEARCH proof-of-concept lacks experimental detail.** No prompt, no description of the wall-sparse maze configuration, no evaluation metric beyond "correct implementation," and no neural baselines tested on the same task. Three successful runs are reported but the criteria for correctness, the determinism of the evaluation, and failure modes are not described. This section reads more as an illustration than a replicable experiment.

- **The PARKING results are ambiguous:** Test success rate slightly favors DQN (0.18 vs. 0.16), while gap-based metrics favor PSM. The paper is honest about this inconclusiveness, but it means the Parking re-evaluation does not cleanly support either side of the argument.

### Trivial

- **The "cannot encode" phrasing is used for both expressivity (theoretical impossibility) and practicality (fixed capacity prevents representation).** Section 5 sometimes addresses this carefully (distinguishing exact representation from learnability via cited literature on LSTM imprecision), but the abstract and introduction use the stronger phrasing without qualification. A consistent distinction between formal expressivity and practical feasibility would improve clarity.

## Nice-to-Haves

- **Train programmatic policies (NDPS/PROPEL) with β = 0.5 on TORCS** to close the comparison loop. This would determine whether the programmatic advantage disappears entirely when reward function is controlled.
- **Run neural baselines (PPO with a_{t-1}, LSTM) on the wall-sparse maze** to empirically verify the expressivity gap predicted by the theory.
- **Provide prompt details, maze specification, and evaluation protocol for the FUNSEARCH experiment** in an appendix for reproducibility.

## Removed Points

The following points from the reviews were removed after cross-checking:

- **"Incoherence between structure and evidence"** — The paper is internally coherent. The re-evaluation is well-supported, and the positive claim is explicitly labeled as a proof-of-concept with a theoretical grounding. The structure follows logically from negative findings → theory → positive identification → demonstration.
- **General scope-creep demands** (e.g., "the paper should connect to existing RL domains where programmatic policies have been shown to work better") — The paper already provides concrete examples (NetHack, pathfinding) and correctly scopes its contribution.
- **"NDPS trained with only 3 seeds"** — The paper acknowledges using the original published data and reports the asymmetry; this is a limitation of available data, not an error.
- **Any criticism about missing appendices, code availability, or supplementary materials** — The parser strips these; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Conduct the missing experiment: train PPO with a_{t-1} and LSTM baselines on the wall-sparse Karel maze (Figure 7) and measure OOD generalization to larger mazes. If they fail (as the theory predicts), this would transform the proof-of-concept into a demonstrative result and significantly strengthen the paper.
2. Provide the FUNSEARCH prompt, maze specification, and correctness verification criteria in detail — ideally in an appendix.
3. Analyze why HARVESTER is hard for the last-action-augmented neural model — does it require more than constant memory, or is it a discoverability issue?

## Score and Decision

The paper makes a solid contribution through its well-executed re-evaluation of three influential benchmarks and its clear theoretical framework. The weaknesses center on the positive claim about memory-scaling tasks, where the evidence (theory + proof-of-concept) is credible but falls short of the strong "cannot encode" language used in the abstract. The paper is comparable in quality to papers scoring 5.5 in the calibration corpus (e.g., NAORIWBaoO "Gradient-Based Program Synthesis with Neurally Interpreted Languages" at 5.50; CJJ8VxOWbG "RL Grokking Recipe" at 5.20). It is stronger than the rejected ARC-AGI program synthesis paper (0ACUx9pMWJ at 5.00) due to broader scope and cleaner framework, and weaker than the top-6.00 anchors which have stronger empirical validation of their core claims.

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| eM8Db7ukSB | 2.50 | R1 | Much weaker; generic approach with thin experiments |
| kzRWbQgady | 3.33 | R1 | Weaker; narrower evaluation, withdrawn |
| CJJ8VxOWbG | 5.20 | R1,R2 | Comparable; similar quality but different topic (RL grokking) |
| 0ACUx9pMWJ | 5.00 | R1,R2 | Weaker; narrower scope (18/1000+ tasks), rejected |
| OHFNJoNtjW | 4.00 | R1 | Weaker; limited to 2 environments, incremental novelty |
| UQ36IrVCw2 | 4.67 | R1 | Weaker; single domain, clarity issues |
| NAORIWBaoO | 5.50 | R2 | Comparable; similar quality in neurosymbolic program synthesis |
| 14dlTHVxDX | 6.00 | R2 | Stronger; formal proofs + strong empirical validation |
| LMD8ndMqs0 | 5.50 | R2 | Different topic (TD vs MC); similar quality tier |
| OBpQdCWLfd | 6.00 | R2 | Stronger; more complete empirical story |

**Round 1 bracket:** 4.5–6.5. **Round 2 narrowing:** Within this bracket, the paper is closest to the 5.0–5.5 anchors. It is stronger than the 5.00 anchor (broader scope, cleaner theoretical framework) and comparable to the 5.20 and 5.50 anchors, but the thin empirical support for the positive claim prevents it from reaching the 6.00 level.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>