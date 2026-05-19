- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3
Now I have full understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes SINE, a symbolic regression framework that recovers exact and compact Boolean functions from truth tables for logic synthesis. It uses Shannon decomposition to factorize truth tables into smaller sub-tables, an MCTS-based search with lexicographic optimization (prioritizing accuracy over circuit size), and a "self-symmetric" motif mining mechanism to encourage sub-expression sharing across cofactors. Evaluated on 10 circuits from three benchmarks, SINE outperforms four SR baselines in recovery accuracy and two EDA baselines (SOP, BDD) in circuit size, with post-optimization improvements after ABC's Resyn2.

## Strengths

1. **Diagnosis of SR failure on Boolean functions.** Section 4.1 and Figure 2a empirically demonstrate that four popular SR methods (GPLearn, Boolformer, DSR, SPL) cannot recover exact Boolean functions when input dimension exceeds 7, establishing a clear gap and motivation. The exponential growth in function length (Figure 2b) is well-documented.

2. **Controlled ablation establishing component contributions.** Table 4 decomposes SINE into four components (F: factorized representation, M: motif mining, C: crossover, L: legalization) and shows incremental benefit from each component across diverse circuits. F improves accuracy over plain MCTS; F+M improves circuit size over F alone; FMC further improves; L adds exactness with minimal overhead.

3. **Clear empirical results against SR baselines.** SINE generates circuits with 100% accuracy on 2.5× more circuits than Boolformer (Table 1), and after legalization reduces circuit size substantially (Table 2). The online evaluation (Table 3) shows SINE's circuits provide better starting points for ABC's Resyn2 optimization than SOP/BDD baselines, with up to ~20% initial size reduction and 10.10% average improvement after optimization.

4. **Analysis linking logical sharing to circuit size.** Figure 2d provides a controlled experiment showing that, for Boolean functions of equal length, circuit size is inversely proportional to logical sharing nodes — directly motivating the motif mining mechanism.

5. **Principled multi-objective handling via lexicographic optimization.** Integrating lexicographic selection into the MCTS UCT formula (Section 5.2) is a clean solution for the dual objectives of exact recovery and circuit minimization, where accuracy must be strictly prioritized.

## Weaknesses

### Major

1. **Legalization mechanism is never described.** The paper repeatedly states that a "legalization" mechanism is applied to boost accuracy to 100% (Sections 5.3 and 6), and post-legalization circuit size is a key comparison metric (Tables 2, 3). However, the paper provides zero algorithmic or implementation details about how legalization works. Without knowing whether legalization adds arbitrary correction logic or if its overhead varies across methods, the post-legalization size comparisons in Tables 2 and 3 are uninterpretable relative to the quality of the original search. This is the single most consequential gap in the paper.

2. **No statistical variance reported for any result.** All tables report single numbers with no standard deviations, confidence intervals, or indications of multiple trials. This is especially concerning for the MCTS-based components, which are inherently stochastic. The differences between methods could be within the noise of a single run. (Note: SOP and BDD are deterministic, but the SR baselines and SINE itself involve randomness.)

### Minor

3. **EDA baselines are weak.** The paper compares against SOP and BDD as "state-of-the-art" EDA methods. These are fundamental representations, not modern logic synthesis flows. A proper comparison would include ABC's optimized synthesis scripts (e.g., `dc2`, `&balance`, `if`), or at minimum show what ABC produces when run directly on the truth table without SINE. The Resyn2 post-optimization mitigates this somewhat, but the initial representation comparison against SOP/BDD alone is insufficient to support the broad claim of "boosting logic synthesis."

4. **"Self-symmetric" transfer mechanism is heuristic and insufficiently justified.** The paper asserts that motifs extracted from one cofactor's solution ($f_1$) should transfer to the other cofactor's agent ($f_2$) because the sub-tables are "symmetric," but no formal or empirical justification is provided for why this transfer is beneficial. The cofactors $f_{X_i=1}$ and $f_{X_i=0}$ are different functions — they share a domain structure but are not mathematically symmetric. The ablation (Table 4) shows that the M component (which includes both motif mining + symmetric search) helps, but doesn't isolate whether cross-cofactor transfer specifically provides value versus a simpler approach of motif mining within each independent search.

5. **"First framework" novelty claim is overstated.** The abstract and contribution list state SINE is "the first symbolic regression framework capable of exactly recovering optimized boolean functions for circuit optimization." Boolformer (d'Ascoli et al., 2023) explicitly targets Boolean function learning, and prior IWLS competition entries used decision trees/random forests for this task. The novelty lies in SINE's specific design (factorization + MCTS + motif mining), which is genuine, but the "first" framing is imprecise and undermines credibility.

### Trivial

6. **Greedy variable selection policy lacks detail.** Section 5.1 says variables are selected "based on the circuit size after decomposition," but no specification is given for how circuit size is estimated before the sub-functions are learned. No sensitivity analysis for the decomposition depth hyperparameter $k$ (used up to 3) is provided.

7. **Certain hyperparameters unreported.** MCTS rollout counts, UCT constants, motif size limits, crossover rates, and sampling budgets are not disclosed, which hinders reproducibility.

## Nice-to-Haves

- A controlled experiment isolating the cross-cofactor motif transfer mechanism (e.g., random transfer vs. no transfer vs. the proposed self-symmetric transfer) would strengthen the central claim about logical sharing.
- Reporting wall-clock runtime or node evaluations would help assess practical applicability, especially since MCTS on $2^k$ sub-problems could be computationally expensive.
- A random variable-selection baseline for the factorization step would help quantify the benefit of the greedy selection policy.

## Removed Points

- *"Missing comparison with exact synthesis (SAT-based, Knuth 2015)"* — Removed per instructions on missing related works. This is outside the paper's stated scope of SR-based methods, and exact synthesis targets a different regime (very small functions).
- *"Larger benchmarks needed / doesn't scale to industrial designs"* — Removed as scope creep. The paper's benchmarks (5–12 inputs, up to 13 outputs) are standard for the Boolean-function-level synthesis setting, and the paper honestly discusses scalability as a challenge.
- *"Missing discussion of related work (Petersen et al. 2022, Schmitt et al. 2023)"* — The paper *does* cite these in the related work section (Section 2). The harsh critic's claim that they are missing is factually wrong.
- *"Greedy selection is circular"* — The paper's claim that variables are selected "based on the circuit size after decomposition" is not circular; one can estimate circuit size from sub-truth-table characteristics. The detail is insufficient, but the concept is not fundamentally flawed. Moved to trivial weakness #6 above.
- *"Formatting artifacts (garbled tables)"* — Removed per instructions; these are parser artifacts, not author errors.
- *"Section 7 mentions LLMs as future work, feels tangential"* — This is a subjective nitpick about a single sentence in the conclusion and carries no weight.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that significantly reframes or extends what the paper itself provides.

## Suggestions

1. **Describe the legalization mechanism in full.** Without this, the central comparison (post-legalization circuit sizes) is opaque. Report results both before and after legalization, and characterize the overhead legalization adds for each baseline method.
2. **Run multiple trials (≥10) and report mean ± std** for the stochastic SR methods (including SINE) to establish reliability of the reported improvements.
3. **Add ABC-optimized synthesis flows as EDA baselines.** Compare against running ABC's `dc2`, `&balance`, or the full `resyn2` script directly on the truth table, not just as post-processing of initial representations.
4. **Isolate the cross-cofactor transfer mechanism** in the ablation. Show that extracting motifs from $f_1$ and injecting into $f_2$'s search is specifically beneficial (vs. independent searches, or random motif transfer).
5. **Tone down the "first" novelty claim** to something more precise, e.g., "SINE is, to the best of our knowledge, the first search-based symbolic regression framework that combines truth-table factorization with sub-expression sharing to exactly recover compact Boolean functions for logic synthesis."
6. **Provide hyperparameters** (MCTS UCT constant, rollout budget, motif size limits, crossover sampling strategy) and sensitivity analysis for the decomposition depth $k$.
7. **Add a random variable-selection baseline** for the factorization step to justify the greedy selection policy.
