Now I have a clear calibration picture. Let me write the final review.

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| NGVljI6HkR (Programmatic vs Latent Spaces) | 3.67 | R1 | Current paper clearly stronger — covers 3 benchmarks, adds theoretical framework, identifies memory as key differentiator |
| ehSQZa4vuk (Bad Habits: Policy Confounding) | 5.25 | R2 | Current paper stronger — more comprehensive benchmarks, better causal ablations, actionable findings |
| QiUitwJDKI (InnateCoder) | 5.75 | R1 | Comparable — InnateCoder has stronger positive experiments, current paper has stronger framework and re-evaluation |
| 3w6xuXDOdY (Generalization Gap in Offline RL) | 6.50 | R2 | Current paper slightly weaker — less thorough experiments, thinner proof-of-concept, but has theoretical framework that 3w6xuXDOdY lacks |
| oTRwljRgiv (ExeDec) | 7.00 | R1 | Current paper clearly weaker — ExeDec has stronger methodology, more polished evaluation, and tighter integration |

**Round 1 bracket: 5.0–6.5 → narrowed to ~5.5 after Round 2 comparisons.**

---

## Summary
This paper re-evaluates three prior benchmarks (TORCS, KAREL, PARKING) where programmatic policies were reported to generalize better OOD than neural policies. Through controlled experiments, it shows that modest adjustments — a cautious reward function in TORCS, sparse observations plus last-action augmentation in KAREL — allow neural policies to match or exceed programmatic ones. The paper then proposes an expressivity/discoverability framework for analyzing OOD generalization and argues that programmatic representations have a genuine advantage only for problems requiring instance-scaling working memory that fixed-capacity neural architectures cannot represent, supported by a proof-of-concept using FUNSEARCH to synthesize BFS for a modified KAREL maze.

## Strengths
- **Causal diagnosis of the TORCS generalization gap**: The paper identifies that programmatic policies in TORCS generalized better because they moved the car more slowly, not because of representational advantages. Table 1 confirms this cleanly: DRL with the original reward (β=1.0) crashes on all OOD tracks, while DRL with a cautious reward (β=0.5) generalizes on 69–100% of seeds across test tracks, matching NDPS. This is a well-controlled ablation that isolates the confound.
- **Counterintuitive KAREL result**: Table 2 shows that "PPO with a_{t-1}" (a simple feedforward network using only local observations plus the last action) achieves perfect generalization (return 1.00) to 100×100 grids on STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER, while the fully-observable ConvNet baseline fails entirely (0.00 on all tasks at 100×100). This directly overturns the prior conclusion that programmatic representations were necessary for this level of OOD generalization, and the finding that *less* information improves generalization is genuinely interesting.
- **Clean theoretical framework**: Definitions 2 and 3 (expressivity and discoverability) provide a crisp, useful lens for reasoning about when representations enable OOD generalization. The framework cleanly explains the re-evaluation results (prior work controlled discoverability for programmatic search but not for neural search) and points toward where genuine representational differences lie.
- **Principled identification of instance-scaling memory as the key differentiator**: Section 5 argues that fixed-capacity neural architectures cannot represent solutions requiring working memory that grows with input size (e.g., pathfinding requires Ω(log|V|) bits just to index vertices; BFS requires Θ(|V|) for the frontier). This is a well-specified theoretical argument that goes beyond confound-hunting.
- **Honest treatment of ambiguous results**: The PARKING results (Table 3) show that neither PSM nor DQN reliably generalizes. The authors do not overclaim — they acknowledge PARKING is challenging for both representations (lines 266–267, 274–275) and appropriately describe it as pointing toward future benchmark design rather than as a confirmation of their thesis.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **FUNSEARCH proof-of-concept is too thin to carry evidential weight**: The experiment occupies two sentences (lines 304–308): FUNSEARCH with Qwen 3-Coder (30B) was run on a wall-sparse KAREL maze, and three runs returned a correct BFS implementation. No experimental details are provided — prompt structure, search budget, total runs attempted, evaluation protocol, maze specifications are all absent. The paper also does not address the obvious confound that BFS is among the most canonical algorithms in computer science and almost certainly appears in Qwen 3-Coder's training data. While the paper explicitly labels this a "proof-of-concept," two sentences is an anecdote, not an experiment, and this weakens the paper's ability to substantiate its positive claim about programmatic synthesis for memory-bound tasks.
- **The bridge between the two halves of the paper is under-argued**: The paper's narrative — that prior DSLs are expressively equivalent to neural architectures (linking the re-evaluation in Part 1 to the memory argument in Part 2) — is argued in a few sentences (lines 284–288). The TORCS argument is a brief analogy (if-then-else chains with parameters "resemble" ReLU networks, citing Orfanos & Lelis 2023). For KAREL, the paper notes LSTMs can approximate FSMs. The PARKING DSL receives no expressivity analysis. The claim is plausible but the argument is suggestive rather than rigorous, making the paper's unified thesis less secure than it could be.
- **HARVESTER anomaly not analyzed**: In Table 2, HARVESTER is the only KAREL task where neither PPO+a_{t-1} (drops from 0.59 to 0.04 on 100×100) nor LEAPS (drops from 0.45 to 0.00) generalizes. This may be the one KAREL task that genuinely requires more than constant-memory heuristics — making it directly relevant to Section 5's memory argument. The paper mentions the result but does not investigate why HARVESTER resists generalization for both representations, missing an opportunity to connect the two halves of the paper.

### Trivial
None.

## Nice-to-Haves
- Statistical significance tests for the TORCS results (e.g., comparing the 76% generalization rate against the NDPS baseline of 3/3 seeds) would strengthen the quantitative claims, though the effect sizes are already clear.
- A more explicit characterization of the SparseMaze domain (grid size, obstacle density) in the main text would help readers evaluate the FUNSEARCH proof-of-concept even without the stripped Figure 7.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "PARKING results are used inconsistently with the paper's framing"** — REMOVED. The paper honestly reports that both representations perform poorly on PARKING and acknowledges the ambiguity (lines 266–267, 274–275). It says PARKING "points in the direction of benchmarks that could distinguish" representations — appropriately tentative, not inconsistent.
- **Harsh Critic: "The discoverability analysis is asymmetric"** — REMOVED. The paper explicitly acknowledges (line 290) that "controlling for the discoverability property can be challenging because it depends on search heuristics that may not be initially obvious" and deliberately pivots to expressivity. This is a scoping choice, not an oversight.
- **Harsh Critic: "Section 6 makes speculative claims that could be removed without loss"** — REMOVED. This is a style preference. The section appropriately uses hedging language ("may have implications," "could be the result") and situates the work in a broader context, which is standard practice.
- **Harsh Critic: "Missing appendix, missing figures, missing references"** — REMOVED per hard rules (parser strips these from all papers).
- **Harsh Critic: "'Bounded time limit' in Definition 3 is vague"** — REMOVED. The paper is not doing complexity theory; the definition is adequate for the paper's conceptual purposes.
- **Harsh Critic: "Statistical testing not performed"** — MOVED to Nice-to-Haves. Standard deviations and confidence intervals are reported where appropriate (Table 3); formal tests would strengthen but are not universally expected.
- **Strength Finder: "FUNSEARCH proof-of-concept closing the expressivity argument"** — WEAKENED and retained only as a qualified aspect of the framework strength. The concept is valid but the evidence is too thin to "close" the argument.

## Novel Insights
The paper's reframing of the programmatic-vs-neural OOD generalization debate through the lens of expressivity and discoverability is genuinely useful. Prior work treated "programmatic policies generalize better" as an empirical finding without disentangling whether the advantage came from representation (expressivity) or from search (discoverability). By showing that simple training adjustments close the gap on established benchmarks, the paper demonstrates that the prior advantage was almost entirely a discoverability effect. The identification of instance-scaling working memory as the principled boundary where programmatic representations have an inherent expressivity advantage over fixed-capacity neural architectures is a concrete, falsifiable claim that can guide future benchmark design. The counterintuitive KAREL result — that providing *less* information (sparse observations) combined with a simpler model yields better OOD generalization — is an insight with implications beyond this paper's specific domain.

## Suggestions
- Expand the FUNSEARCH experiment with at least a half-page of detail: prompt structure, search budget, number of runs, evaluation protocol, and a discussion of the BFS-in-training-data confound. Even if the result remains preliminary, readers need enough information to assess its validity.
- Provide a brief expressivity analysis for the PARKING DSL. Since the DSL is a Boolean expression language over state variables (line 189), neural networks can clearly represent Boolean functions — a sentence or two would close the gap in the bridging argument.
- Analyze or at least hypothesize about why HARVESTER resists generalization for both representations. If it genuinely requires instance-scaling memory, it directly supports Section 5's thesis; if not, understanding why would be informative for the framework.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>