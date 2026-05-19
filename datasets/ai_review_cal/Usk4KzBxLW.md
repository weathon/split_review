- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 5, 3
Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes LLM-LNS, a framework that uses a dual-layer self-evolutionary LLM agent to automatically generate neighborhood selection strategies for Large Neighborhood Search (LNS) in large-scale MILP problems. The inner layer evolves heuristic strategies (thoughts + code) for convergence, while the outer layer evolves prompt strategies to maintain diversity. Differential memory feeds fitness history back to the LLM to guide directional evolution. The agent is evaluated on heuristic generation for online bin packing and TSP, and the full LLM-LNS framework is evaluated on four classes of large-scale MILP benchmarks.

## Strengths

- **Novel dual-layer self-evolutionary architecture**: The paper proposes a structured two-level LLM agent where heuristic strategies and prompt strategies co-evolve. The inner layer evolves both natural-language thoughts and executable code representations of heuristics (Section 3.1.1, lines 94–100), while the outer layer evolves the prompts used to guide crossover/variation in the inner layer (lines 102–104). This is a genuine structural novelty compared to prior LLM+EA methods like FunSearch and EOH, which lack either thought evolution or prompt evolution.

- **Differential memory for directional evolution**: Section 3.1.2 introduces a concrete mechanism where the LLM receives tuples \(S^{(t)} = \{\langle H_i^{(t)}, \text{thought}_i, f(H_i^{(t)})\rangle\}_{i=1}^{m}\) — strategy-thought-fitness triples from previous generations — and uses the fitness differential between high- and low-performing strategies to guide crossover and variation (lines 110–115). This formalizes how the LLM acts as an optimizer rather than just a generator.

- **Consistent experimental advantages across three problem classes**: 
  - On online bin packing (Table 2), LLM-LNS achieves the lowest average excess bin fraction (1.63%) vs. FunSearch (1.90%) and EOH (2.12%).
  - On TSP (Table 3), it achieves 0.08% average gap to best-known solutions, outperforming EOH (0.26%), AM (4.80%), and specialized neural methods like POMO (0.19%) and LEHD (4.76%).
  - On large-scale MILP benchmarks (Table 5), LLM-LNS achieves the best objective values on 10 of 12 instances across SC, MVC, MIS, and MIKS, outperforming ACP, CL-LNS, Gurobi, SCIP, GNN&GBDT, and Light-MILPopt.

- **Adaptive neighborhood size mechanism**: Section 3.2 describes a concrete rule for dynamically adjusting the neighborhood size \(k\) — expanding when improvement stalls (below threshold \(\epsilon\) for \(p\) iterations) and contracting when subproblem solve time is excessive (lines 120–122). This is a well-specified algorithmic component with explicit formulas.

## Weaknesses

### Fatal
None.

### Major

1. **Method is insufficiently specified for reproducibility.** The dual-layer evolutionary process is described in prose and illustrated through an example (Figure 2, bin-packing), but critical implementation details are absent:
   - No prompt templates are given for how the LLM is instructed to perform crossover, variation, or consume the differential memory tuples. The paper says the LLM receives \(S^{(t)}\) (line 112) but never explains how the LLM uses these tuples to "learn from differences" or generate new strategies.
   - The "ranking provided by the LLM agent" used for variable selection in ALNS (line 128) is stated but never derived from the agent description in Section 3.1. No mechanism is described for how the agent produces a variable ranking.
   - The paper references Algorithm 1 (line 130) and Appendices A–D (line 137) for more details, which are not present in the reviewed text (stripped by parser). However, even in the material available, the core evolutionary loop lacks an algorithmic specification (pseudocode) adequate for reproduction.

2. **No measure of variance or statistical reliability.** Despite the stochastic nature of both LLM generation and evolutionary search, not a single experiment reports variance, standard deviation, confidence intervals, or mentions multiple random seeds. The claimed advantages on bin packing (1.63% vs 1.79%/1.87% — small absolute margins) could be noise without such reporting. This is a fundamental methodological gap for an LLM-based stochastic method.

3. **No ablation study isolating the contributions of claimed innovations.** The paper presents four novel components (dual-layer structure, inner-layer evolution, outer-layer prompt evolution, differential memory) but never ablatates any of them. It is impossible to determine which component drives the reported improvements. For instance, the paper does not compare ALNS with the agent's ranking vs. ALNS with random ranking or with a fixed heuristic strategy — which would directly validate the agent's role in the MILP setting.

4. **No computational cost reporting.** The paper reports objective values but never provides wall-clock time, LLM query counts, or solver time for any method. The only time-related mention is a 30,000-second limit in the Table 5 caption for methods that "failed." Without runtime data, it is impossible to interpret whether LLM-LNS achieves better solutions because of smarter search or simply because it was allocated more compute. This is critical for a method that uses an LLM (GPT-4o-mini) with population-based iterative evolution.

### Minor

5. **Disconnect between agent evaluation and full-framework evaluation.** The agent is evaluated on bin packing and TSP (combinatorial optimization heuristics), while the full LLM-LNS framework is evaluated on MILP neighborhood selection. The paper never directly demonstrates that the same agent mechanism is responsible for the MILP improvements or that the heuristics learned on small MILP training instances transfer to the large test instances. An ablation comparing ALNS with the agent's ranking vs. a non-adaptive ranking would directly address this but is absent.

6. **Missing training data and instance details.** The paper repeatedly refers to "scant small-scale training data" (line 20) and "problems with tens of thousands of variables" (line 166) but never specifies: how many training instances, their exact sizes, how they were generated, or the number of variables/constraints/density of the test instances (Table 4 provides sizes but the table is an image). These details are essential for reproducibility and assessing generalization claims.

7. **Limited discussion of limitations and failure modes.** The conclusion (Section 5) is generic. The paper does not discuss LLM query costs, sensitivity to prompt engineering, problems where the approach might fail (e.g., where LLM domain knowledge is insufficient), or situations where evolutionary search might converge prematurely despite the dual-layer design.

### Trivial

8. **Inconsistency in baseline naming**: ACP is referred to as "Adaptive Constraint Partitioning" in Section 2.2 (line 51) but "Adaptive Constraint Propagation" in Section 4.2 (line 172). Minor but should be corrected.

## Nice-to-Haves

- A direct validation of the agent's role in LNS: compare ALNS with the agent's ranking vs. ALNS with a random or heuristic ranking on the MILP benchmarks.
- Reporting wall-clock time or LLM query counts alongside objective values so the efficiency–quality trade-off is transparent.
- Multiple independent runs with mean and standard deviation for all experiments, especially the MILP results.
- Ablation study removing the outer layer (prompt evolution), differential memory, or both to isolate each component's contribution.

## Removed Points

These points were raised by the reviewers but are removed with justification:

- *"The method is critically under-specified...no algorithmic description or even a high-level pseudocode"* — Partially addressed: the paper does provide a high-level conceptual description (Section 3.1), an illustrative example (Figure 2), references Algorithm 1, and cites Appendices A–D. The specification is incomplete but not absent. Kept as Major but softened.
- *"Results on MILP benchmarks appear implausible (zero objectives)"* — I cannot verify the specific zero values claimed by the reviewer since Table 5 is an image stripped by the parser, and the paper's text does not mention these zeros explicitly. The general point about missing instance details is kept as Minor.
- *"The comparison with Gurobi and SCIP is insufficiently described and likely misleading"* — The paper explicitly states that "Gurobi is used as the sub-solver in the neighborhood search step across all methods" (line 172), which addresses the concern about asymmetric solver usage. The broader concern about missing time limits is partly valid but subsumed by Weakness #4 (no compute cost reporting). Merged.
- *Strength about "training on small-scale generalizing to large-scale"* — This is stated as a claim but lacks direct evidence (no transfer ablation, no progressive scaling study). It is a contribution claim, not a demonstrated strength. Moved here.
- *"Related work coverage" comment* — The instruction says not to mention missing related works. Removed.
- *Formatting/style nitpicks and requests for appendix content* — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the methodological gaps (missing variance, absent ablation, incomplete specification) but do not identify a fundamentally different interpretation of the results or a novel connection the paper missed.

## Suggestions

1. Provide a complete pseudocode or algorithmic specification of the dual-layer evolutionary process, including the exact prompt templates for crossover, variation, and differential memory consumption.
2. Add multiple random seeds (≥5) with mean and standard deviation to all experiments.
3. Report wall-clock time and approximate LLM query counts alongside objective values.
4. Add an ablation study: (a) ALNS with random ranking vs. agent's ranking on MILP benchmarks; (b) full dual-layer vs. inner-layer-only vs. no differential memory.
5. Provide training data details: number of instances, sizes, generation procedure.
6. Specify instance statistics (number of variables, constraints, density) for the MILP test set.
7. Add a limitations section discussing LLM query costs, potential failure modes, and prompt sensitivity.
