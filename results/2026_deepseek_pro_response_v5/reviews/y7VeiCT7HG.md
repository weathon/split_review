## Summary

This paper proposes qEHVI-SF, a batch acquisition strategy for multi-objective Bayesian optimization (MOBO) that multiplies the standard qEHVI acquisition function by a minimum-distance space-filling term. The method is motivated by a "Probability of Matching" framework that factorizes P(X = X*) into a quality component P(X ⊆ X*) and a coverage component P(X* ⊆ X | X ⊆ X*). Experiments on two synthetic benchmarks and an alloy design case study (six MOBO tasks across 2–6 objectives) show qEHVI-SF outperforming qEHVI and a QSVGD baseline on hypervolume and a new design-space coverage metric (EMD), with comparable computational cost.

## Strengths

- **Strong empirical results on the alloy design case study (Section 4.2, Figure 2):** Across 18 experimental configurations (six MOBO tasks × three batch sizes), qEHVI-SF consistently achieves the highest rediscovery ratio — a practically meaningful metric for materials inverse design. The 20-trial evaluation provides reasonable statistical power, and the result pattern aligns with the theoretical framing: qEHVI degrades at large batch sizes while qEHVI-SF remains stable.

- **Introduction of the Expected Minimum Distance (EMD) metric (Section 4.1, Eq. 9):** EMD evaluates design-space coverage by measuring average distance from true Pareto-optimal designs to the nearest discovered point. The paper provides clear justification — full Pareto front coverage does not guarantee recovery of all Pareto-optimal designs, but the converse holds — making EMD a stricter and more informative metric than IGD for design-space-focused evaluation.

- **Thorough complexity analysis with empirical validation (Section 3.3, Table 1):** The paper derives that the space-filling term adds only O(q(n+q)d) per iteration, dominated by the O(NmK(2^q−1)) hypervolume computation for large m or q. Table 1 confirms that qEHVI-SF's per-candidate runtime is comparable to qEHVI in practice.

- **Elimination of an explicit diversity-quality tradeoff hyperparameter (Section 3.1):** Unlike QSVGD, which requires a decaying schedule for its η hyperparameter, qEHVI-SF's multiplicative formulation integrates both concerns without any tunable coefficient, simplifying deployment across new problems.

## Weaknesses

### Fatal

None.

### Major

- **Gap between the probabilistic framework and the actual acquisition function (Section 3.2):** Equation (7) factorizes P(X = X*) into a quality term and a coverage term, presented as a principled derivation. But the bridge to Eq. (8) is heuristic, not derived. Specifically: (a) "normalized qEHVI" is mentioned exactly once (line 107) with no definition or normalization scheme — hypervolume improvement is a Lebesgue measure, not a probability; (b) the coverage term substitutes minimum-distance maximization for the conditional probability via a balls-of-radius-r argument where r is introduced and then never used in the final formula; (c) Eq. (8) multiplies objective-space hypervolume by design-space distance — two quantities with incompatible units and arbitrary relative scaling. The Conclusion (Section 5) partially acknowledges this gap, which is commendable, but the main text overclaims the connection. The method itself (multiplying qEHVI by a repulsion term) is reasonable, but the strength of the framing claim is not supported.

- **Missing ablation: multiplicative vs. additive combination:** The paper's central methodological claim is that the multiplicative formulation in Eq. (8) is superior to additive combinations (as in QSVGD). However, QSVGD uses a different diversity mechanism (batch entropy via KDE, not minimum distance), so the experiments cannot isolate whether the improvement comes from (a) the multiplicative formulation, (b) the choice of minimum-distance as the diversity measure, or (c) the removal of the η hyperparameter. An ablation comparing Eq. (8) against an additive variant such as qEHVI + λ · min-distance would directly test the paper's main thesis.

- **Thin baseline comparisons:** The paper compares against only two baselines: qEHVI (the quality-only component) and a QSVGD variant adapted by the authors from single-objective BO. For a 2026 MOBO submission, this is sparse. The paper critiques objective-space diversity methods (EMMI, IGD-NS) in Section 2.2 but does not include them as baselines. Results on ZDT/DTLZ benchmarks are in the appendix.

### Minor

- **"Normalized qEHVI" is undefined (line 107):** The term appears once with no definition of the normalization scheme. Reproducing the method requires specifying how hypervolume improvement is normalized, or clarifying that normalization is not actually needed for the final algorithm (since the raw qEHVI appears in Eq. 8).

- **The radius r argument is conceptually incomplete:** The balls-of-radius-r reasoning (lines 107–109) motivates maximizing minimum distance, but the validity of the simplification depends on r, which is never discussed further. This is a presentation issue rather than a methodological flaw.

- **Overstated claim about design-space diversity:** Section 2.2 asserts that "promoting diversity in the design space does not compromise solution quality" (point 3, line 69). Without the multiplicative qEHVI term, a diverse design-space set could include many low-quality solutions. The method mitigates this through multiplication, but the unqualified claim is too strong.

### Trivial

- The probabilistic notation P(X = X*) is used as if it were a well-defined probability over sets of potentially different cardinalities (|X| = q vs. |X*| typically much larger). This is a minor notational imprecision that the paper implicitly acknowledges (line 97: "approaches X*").

## Nice-to-Haves

- Quantifying whether qEHVI-SF is more robust to reference-point choice than qEHVI would strengthen the case, given that reference-point sensitivity is part of the paper's motivation.
- Broader evaluation on standard MOBO benchmarks (ZDT, DTLZ) in the main text rather than appendix-only.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: Missing experimental details (number of trials, initialization, reference point selection):** The paper directs readers to Appendix A.1, which was stripped by the parser. This is not an author error.
- **Harsh Critic: QSVGD adaptation description insufficient:** The paper describes the QSVGD MOBO adaptation in Section 2.2 (Eq. 6) and mentions the η schedule details are in Appendix A.1. The core description is present in the main text.
- **Harsh Critic: Figure 1 caption garbled:** This is a parser artifact, not an author error.
- **Strength Finder: "Principled probabilistic factorization framework":** While the factorization (Eq. 7) provides useful conceptual language, calling the framework "principled" is undermined by the gap between the framework and the actual acquisition function (see Major Weakness 1). The conceptual contribution has value but is overstated.
- **Harsh Critic: Large standard deviations in Table 1 runtime data:** The paper already discusses the higher standard deviation for qEHVI-SF in Section 4.3 (line 183). This is noted, not hidden.
- **Harsh Critic: Concerns about method/baseline availability or existence:** All cited methods (EMMI, IGD-NS, QSVGD, etc.) are established works assumed to exist and be available.
- **Harsh Critic: Demand for ZDT/DTLZ results:** Those results are in the stripped appendix; their absence from the main text is noted as a nice-to-have, not a weakness.

## Novel Insights

The factorization P(X = X*) = P(X ⊆ X*) × P(X* ⊆ X | X ⊆ X*) offers a genuinely useful conceptual lens for understanding the quality-diversity tradeoff in batch MOBO, even though the bridge to the specific algorithm is heuristic rather than derived. This lens clarifies why pure qEHVI over-exploits extreme regions (it optimizes only P(X ⊆ X*)) and why batch size alone cannot solve the coverage problem (larger batches increase P(X* ⊆ X) but decrease P(X ⊆ X*)). As a diagnostic framework for reasoning about batch MOBO acquisition, this decomposition has value independent of the specific algorithm proposed.

## Suggestions

- Reframe the method honestly as a heuristic motivated by the probability framework rather than derived from it. This would not weaken the empirical contribution and would make the paper more credible.
- Add the multiplicative-vs-additive ablation: compare Eq. (8) against qEHVI + λ · min-distance with a tuned or scheduled λ. This is the single highest-leverage experiment for supporting the paper's central thesis.
- Include at least one objective-space diversity baseline (e.g., EMMI or IGD-NS) to contextualize the results more thoroughly.
- Define how qEHVI is normalized (or clarify that normalization is not needed in practice since the unnormalized qEHVI is what appears in Eq. 8).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>