Now I have solid calibration data. Let me synthesize my scoring analysis.

**Round 1 Bracket:** The paper is clearly above the weak band (anchors at 2.0–3.0) and well below the strong band (8.0). It falls somewhere between 4.0 and 6.0.

**Round 2 Narrowing:** Compared to the most relevant anchors:
- "Reclaiming the Source" (3.67, Accept): Similar topic, smaller scope, cleaner experiments → our paper is stronger
- "Bad Habits" (5.25, Reject): Similar re-evaluation/confound theme, but narrower (toy domains) → our paper is slightly stronger
- "Level Sampling" (5.67, Reject): More rigorous experiments but narrower scope → our paper is comparable
- "Offline RL Generalization Gap" (6.50, Accept): Well-executed benchmark study with cleaner experiments → our paper is slightly weaker

**Final score:** 5.0. The paper has genuine contributions (confound identification, framework) but the experimental evidence has notable gaps (TORCS comparison not fully controlled, positive contribution lacks RL evidence) that prevent a higher score.

Here is the final consolidated review:

---

## Summary
This paper re-evaluates three influential RL benchmarks (TORCS, KAREL, PARKING) where programmatic policies were claimed to generalize better than neural policies. It shows that with simple modifications—a cautious reward in TORCS and sparse observations augmented with the last action in KAREL—neural policies match or exceed the OOD generalization of programmatic ones. The paper then proposes an expressivity + discoverability framework and argues that tasks requiring instance-scaling memory (e.g., general pathfinding) are a class where programmatic representations provide an inherent advantage, supported by a proof-of-concept using FUNSEARCH.

## Strengths

- **TORCS confound identification (Table 1)**: DRL with β=0.5 (cautious reward) generalizes to 76% of seeds on G-TRACK-2 and 69% on E-ROAD, while DRL with the original reward (β=1.0) crashes on all OOD tracks. This directly demonstrates that the reward function—not the representation—drove the previously reported generalization gap in this benchmark.

- **KAREL neural baseline matches/exceeds programmatic generalization (Table 2)**: "PPO with \(a_{t-1}\)" (feedforward network with last-action input) achieves perfect return on 100×100 grids for stairclimber, maze, topoff, and fourcorner, whereas LEAPS, PPO with ConvNet, and PPO with LSTM all fail on at least two of these tasks. This provides concrete evidence that neural policies can achieve OOD generalization when given appropriate (sparse) observations.

- **Expressivity + Discoverability framework (Definitions 2 and 3)**: Offers a principled decomposition for analyzing OOD generalization, clarifying why prior comparisons were confounded—both representations satisfied expressivity, but discoverability was not controlled.

- **Identification of a problem class for inherent programmatic advantage**: The analytical argument that tasks requiring working memory proportional to input size (pathfinding, nested subproblems) are a class where fixed-capacity neural architectures cannot satisfy expressivity is well-reasoned and grounded in computational complexity. This provides a clear forward-looking hypothesis.

- **Honest assessment of PARKING**: Table 3 is presented without overclaiming—neither representation reliably generalizes—providing a realistic baseline that avoids the temptation to claim success where none exists.

- **Broader implications (Section 6)**: Connects the confound diagnosis to other works in the literature, increasing the paper's reach beyond the three re-evaluated benchmarks.

## Weaknesses

### Major

- **TORCS comparison lacks full control**: The paper compares DRL (β=0.5) against NDPS numbers from Verma et al. (2018) without retraining NDPS/PROPEL under the same cautious reward. The paper argues NDPS policies were inherently slower (making them already "cautious"), but this is an untested assumption—NDPS might have performed differently under the β=0.5 reward, or the gap might have persisted. Since the claim is that "neural policies matched programmatic ones," the comparison should hold training conditions constant. The paper's own framework says discoverability depends on the training signal, and we simply do not know what happens to NDPS discoverability under the same reward change.

- **Positive contribution (memory-scaling advantage) lacks RL evidence**: The FUNSEARCH proof-of-concept (Section 5) is a code-generation demo using a large language model, not an RL experiment. (a) FUNSEARCH is not one of the programmatic RL methods (NDPS, LEAPS, PSM) studied in the benchmarks; (b) the paper does not show that any of those methods can learn a BFS-like policy; (c) there is no neural baseline comparison on the same task; (d) no experiment demonstrates the synthesized policy actually running in the KAREL environment and achieving OOD generalization with quantitative results. The paper's title and framing suggest it will answer *when* programmatic policies actually generalize better, but this central positive thesis remains a hypothesis supported only by a notional example.

### Minor

- **KAREL: architecture and observability confounded**: "PPO with \(a_{t-1}\)" changes both the architecture (feedforward instead of LSTM) and the observability (adds last action). Without an LSTM baseline with the \(a_{t-1}\) input or a feedforward baseline without it, the individual contributions of architecture vs. input augmentation cannot be separated.

- **Selection bias in TORCS reporting**: Of 30 seeds for G-TRACK-1, only 13 completed training and were evaluated for OOD generalization; for AALBORG, only 4 of 15. The generalization fractions (76%, 69%, etc.) are computed only over surviving seeds, conditioning on training success and potentially overstating the overall success rate. Reporting the unconditional rate (including seeds that failed to train) would be more informative.

- **PARKING seed asymmetry**: PSM uses 30 seeds while DQN uses 15. This asymmetry could affect the "Successful-on-100" comparison (it is easier for DQN to score 0/100 by chance with fewer seeds).

- **No analysis of why LSTM baseline failed in KAREL**: Table 2 shows the LSTM fails on most tasks (0.00 on stairclimber 100×100, 0.04 on maze), but the paper offers only a brief comment that it "often also fails to learn how to solve even the smaller problems" without investigation or analysis.

- **DSL expressivity for BFS unverified**: The memory-scaling argument uses programmatic representations generally, but the paper does not show that the specific DSLs used in the benchmarks (Figures 1, 2) can express growing-memory algorithms like BFS. The FUNSEARCH demo generates Python, not programs in these DSLs.

- **NDPS data limited to 3 seeds**: The NDPS results reused from Verma et al. (2018) cover only 3 seeds, providing limited statistical foundation for the comparison against the paper's DRL results.

### Trivial

None.

## Nice-to-Haves

- Train NDPS/PROPEL under the cautious reward (β=0.5) to directly test whether programmatic policies also change their generalization behavior, making the TORCS comparison fully controlled.
- Include an LSTM with \(a_{t-1}\) baseline in KAREL to isolate architecture effects from observability effects.
- Provide concrete evidence that the FUNSEARCH-synthesized BFS policy actually runs in the KAREL environment and achieves OOD generalization, with neural baselines for comparison.
- Analyze whether the specific DSLs in Figures 1 and 2 can express algorithms with growing memory requirements, to ground the memory-scaling argument in the actual RL methods studied.

## Removed Points

- **Criticism that Definition 1 is ambiguous (provable vs. empirical)**: The paper explicitly acknowledges "we often cannot prove that the learned π solves all x' in X" and states that empirical evaluation is the practical standard. Removed as nitpick of standard practice.
- **Criticism about the NDPS conjecture being "speculative and unsupported"**: The paper clearly labels it as a conjecture ("We conjecture that..."). Removed as mischaracterization.
- **Criticism that "fixed-capacity neural policies cannot represent algorithmic structures" is too strong**: The paper acknowledges "In theory [they are] computationally universal" and cites works showing practical limitations. Removed as the paper already addresses this.
- **Reproducibility nitpick about code release timing and undisclosed hyperparameters**: Following the hard rules, these are nitpicks/parser artifacts.
- **Missing appendix content (Figure 7, etc.)**: The parser strips appendices; they exist in the original submission. Removed.
- **Criticism that PARKING discussion contradicts earlier finding**: The paper says PARKING "points in the direction of benchmarks that could distinguish" representations, which is a forward-looking statement, not a contradiction. Removed.
- **Strength: "Thorough analysis of why certain modifications improve neural generalization"**: Overly generic. The analysis is brief and not deeply mechanistic. Removed.
- **Strength: "Honest assessment of a challenging domain"**: Borderline generic, but I kept it as it is concrete (Table 3).
- **Strength: "Broader applicability"**: Kept as it is concrete (Section 6).
- **Strength: "Formal framework isolates root cause"**: Kept because it's specific (Definitions 2, 3).

## Novel Insights

None beyond the paper's own contributions. The calibration did not surface any perspective on this paper that is not already captured by its own analysis or the reviewers' comments.

## Suggestions

1. **Reframe the positive contribution explicitly as a hypothesis** grounded in computational reasoning, and clearly separate it from the re-evaluation results. The current framing risks overclaiming given that the memory-scaling advantage is demonstrated only via a code-generation demo, not through any of the programmatic RL methods studied.
2. **Retrain NDPS/PROPEL under β=0.5** to fully control the TORCS comparison. This would substantially strengthen the paper's negative (debunking) contribution.
3. **Add an LSTM baseline with \(a_{t-1}\) and a feedforward baseline without it** in KAREL to disentangle architecture from observability.
4. **Report unconditional OOD success rates** in TORCS (including training failures in the denominator) alongside the conditional rates.
5. **If the memory-scaling claim is a central contribution**, provide an actual RL experiment using a programmatic RL method (e.g., augmenting LEAPS or NDPS with a larger DSL) on a task requiring growing memory, with neural baselines.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| fvTaoyH96Z.md | 2.33 | R1 (weak) | Much weaker; poorly motivated, unconvincing experiments |
| It4KL6XnPq.md | 3.00 | R1 (weak) | Much weaker; narrower contribution |
| 473sH8qki8.md | 2.00 | R1 (weak) | Much weaker; fundamental issues |
| hCfhfwSfCg.md | 2.00 | R1 (weak) | Much weaker |
| NGVljI6HkR.md | 3.67 | R1 (mid) | Similar topic; narrower scope, cleaner experiments → our paper is stronger |
| lUWf41nR4v.md | 4.50 | R1 (mid) | Method paper; different contribution type |
| tuEP424UQ5.md | 5.75 | R1 (mid) | Benchmark paper; well-executed → slightly stronger |
| UfczlMudN6.md | 6.00 | R1 (mid) | Method paper; cleaner evaluation → stronger |
| DzGe40glxs.md | 8.00 | R1 (strong) | Much stronger; polished, complete |
| OI3RoHoWAN.md | 8.00 | R1 (strong) | Much stronger |
| 9pW2J49flQ.md | 8.00 | R1 (strong) | Much stronger |
| pISLZG7ktL.md | 8.00 | R1 (strong) | Much stronger |
| ehSQZa4vuk.md | 5.25 | R2 (narrow) | Similar re-evaluation theme; toy domains → our paper is slightly stronger |
| lvDHfy169r.md | 5.75 | R2 (narrow) | Method paper; different contribution |
| 3w6xuXDOdY.md | 6.50 | R2 (narrow) | Clean benchmark study → stronger experimental execution |
| X1p0eNzTGH.md | 5.67 | R2 (narrow) | Similar generalization focus; more rigorous experiments → slightly stronger |

**Round 1 bracket:** 4.0 – 6.0  
**Round 2 narrowing:** The paper sits between the 3.67–5.25 anchors (where our paper is the stronger one) and the 5.75–6.50 anchors (where our paper is weaker). Most comparable to the "Bad Habits" paper (5.25) but with broader scope and more direct relevance to the programmatic RL literature.  
**Final score:** 5.0

The paper has real value: the confound identification in TORCS and KAREL is a useful service to the community, and the expressivity/discoverability framework provides a productive lens. However, the experimental evidence has notable gaps—the TORCS comparison lacks full control, the KAREL comparison confounds architecture with observability, and the central positive claim (memory-scaling advantage) is supported only by a code-generation demo rather than an RL experiment. The paper attempts two contributions (negative re-evaluation + positive identification of programmatic advantages) but neither is fully executed. A revision focused on tightening one of the two—preferably the re-evaluation with proper controls—would substantially strengthen the paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>