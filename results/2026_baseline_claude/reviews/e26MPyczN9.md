## Summary

This paper re-evaluates three canonical benchmarks (TORCS, Karel, Parking) used to claim that programmatic policies generalize better OOD than neural policies. The authors show that much of the reported gap stems from experimental confounds—specifically, neural policies trained with cautious reward functions (TORCS) or sparse observations combined with action-augmented observations (Karel) can match programmatic policies. To frame the investigation, they introduce the concepts of *expressivity* (does the policy class contain a generalizing solution?) and *discoverability* (can search find it?). They then identify the genuine differentiator: tasks requiring working memory that grows with input size (e.g., pathfinding, nested subproblems) expose an inherent expressivity advantage of programmatic representations. As proof-of-concept, FUNSEARCH synthesizes a BFS implementation that provably generalizes OOD on a wall-sparse Karel maze.

---

## Strengths

- **Clear, falsifiable re-evaluation with concrete mechanism identification.** For TORCS, the paper pinpoints the speed-exploiting reward as the confound: neural policies with β=0.5 match NDPS's OOD lap times and crash avoidance on all test tracks. This is not speculation—it is a direct ablation that isolates the cause. For Karel, the modification (partial observation + last action as input) yields PPO matching LEAPS perfectly on 4 of 5 tasks (both achieve 1.00 at 100×100 on Stairclimber, Maze, TopOff, FourCorner), in contrast to PPO-ConvNet which obtains 0.00 on every large task.

- **The expressivity/discoverability framework is genuinely useful.** Prior literature conflates two distinct questions: can the representation *encode* a generalizing policy, and can the *search* find it? The paper demonstrates empirically that the DSLs in TORCS, Karel, and Parking induce spaces that are (informally) not more expressive than comparable neural architectures. The framework sharpens future experimental design by separating these factors and directing researchers toward problems where expressivity—not discoverability—is the bottleneck.

- **Strong theoretical grounding for the working-memory argument.** The claim that constant-capacity neural models cannot OOD-generalize on pathfinding is made rigorously: indexing among |V| vertices requires Ω(log|V|) bits, BFS/IDDFS both require Θ(|V|) or Θ(d) memory, and feedforward/recurrent models with fixed hidden state cannot scale. The connection to NetHack's nested subproblem structure (requiring a stack of unbounded depth) adds breadth.

- **Honest accounting of partial results.** The paper does not overstate the Parking result, explicitly noting that DQN achieves a higher raw test success rate (0.18) while PSM generalizes more consistently (smaller train-to-test drop), and concludes that Parking "is a challenging domain for both." This is appropriately calibrated.

---

## Weaknesses

### Fatal
None.

### Major

1. **FUNSEARCH is methodologically disconnected from the programmatic systems evaluated in the re-evaluation.** The original papers (NDPS/PROPEL/LEAPS/PSM) all use structured search within hand-crafted, domain-specific grammars with interpretable policy classes. The proof-of-concept switches to FUNSEARCH with a 30B LLM (Qwen 3-Coder), which generates general Python code rather than DSL programs. The paper claims that "programmatic representations can synthesize BFS," but BFS is not in the grammar of any prior system evaluated; it is found by a modern LLM-based code search tool with no explicit grammar constraints. The positive claim—that programmatic representations have an inherent advantage on working-memory tasks—is demonstrated via a method that is architecturally very different from the negative case, making the cross-comparison logically incomplete.

2. **The FUNSEARCH proof-of-concept is underspecified.** "Three runs of FUNSEARCH returned a correct implementation" is not a rigorous statistical result. The paper does not report: total number of runs attempted, the success rate across runs, how many FUNSEARCH evaluations were required per successful run, or systematic OOD testing of the synthesized BFS across a range of maze sizes. This leaves the demonstration as anecdotal. The wall-sparse maze (SparseMaze) on which FUNSEARCH is tested is also not fully described in the main paper, making the result difficult to assess independently.

3. **Karel HARVESTER failure is underweighted.** Table 2 shows "PPO with a_t-1" achieves only 0.04 at 100×100 on HARVESTER, compared to LEAPS's 0.00. Both fail, but the paper presents this as a success for the neural baseline. HARVESTER is a substantive task where neither representation generalizes. The paper should discuss why and whether this points to a domain-specific confound or to a genuine limitation of the approach—but it moves on without analysis.

### Minor

1. **The expressivity equivalence between TORCS's DSL and ReLU networks is asserted but not proven.** The paper states the ReLU space can be made a superset of the TORCS language by providing peek/fold as inputs, but this depends on whether the temporal aggregation functions can be encoded within ReLU circuits of bounded size. This needs either a formal lemma or a citation supporting the equivalence.

2. **Discoverability is not satisfactorily resolved for TORCS.** Only 13/30 seeds for G-TRACK-1 and 4/15 for AALBORG successfully completed laps. Among the seeds that solved the training task, 76% and 100% generalized. The high failure rate at the training stage means discoverability at the training level remains a significant barrier for neural policies even with the cautious reward—this nuance deserves more discussion.

3. **PARKING uses DQN for a continuous control problem.** DQN is not well-suited to continuous action spaces; the paper notes PPO and DDPG were inferior but does not try SAC or TD3, which are standard baselines for continuous control. The PSM vs. DQN comparison may undersell neural capabilities.

### Trivial

- Figure 3's caption is repeated three times (a parser artifact, not a content issue).

---

## Nice-to-Haves

- A quantitative comparison of success rates across multiple FUNSEARCH runs with confidence intervals would substantially strengthen Section 5.
- An experiment on even a small synthetic instance of nested subproblems (beyond NetHack, which is mentioned but not studied) would make the stack-memory argument empirical rather than theoretical.
- The Harvester failure deserves its own brief analysis—is it a discoverability failure, a partial-observability failure, or a hint of genuine expressivity limitation?

---

## Novel Insights

The clearest novel insight is the identification of working-memory growth as the principled dividing line between where programmatic and neural representations differ in expressivity, rather than in vague notions of "symbolic structure" or "interpretability." The argument is information-theoretic—constant-capacity models cannot allocate Ω(log|V|) bits to index vertices—and connects to the broader literature on the expressive limits of fixed-capacity RNNs. The secondary insight, that the DSLs used in prior programmatic RL papers induce policy spaces that are not meaningfully larger than those of comparable neural architectures (and that observed generalization gaps reduce to discoverability issues), is a clarifying contribution that should affect how future benchmarks are designed. The expressivity/discoverability dichotomy is a clean formalization of a distinction that the community implicitly recognized but had not systematically applied.

---

## Suggestions

- Report full FUNSEARCH run statistics (number of attempts, success rate, time/compute per run) to make Section 5 rigorous.
- Discuss HARVESTER failure explicitly: does partial observability + a_t-1 fail because of a structural limitation, and does this change the paper's conclusions?
- Consider at least one simple synthetic nested-subproblem domain (e.g., a two-level hierarchical maze) to give an empirical grounding to the stack-memory claim.
- Clarify the equivalence between TORCS's DSL and ReLU networks more carefully, or soften the claim to "informally similar."

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>