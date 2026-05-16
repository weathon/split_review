## Summary

This paper proposes ER-AAE, a classical two-stage algorithm for approximate amplitude encoding of vectors into quantum states. The first stage greedily constructs a circuit by adding CZ-containing two-qubit blocks that maximally reduce the linear entropy of the evolving state. The second stage fine-tunes all circuit parameters via Adam to minimize infidelity. The method is evaluated on MNIST, CIFAR-10, random vectors, and random quantum circuit states, using N=10–11 qubits.

## Strengths

- **Consistently achieves lower infidelity and higher PSNR than all compared baselines (MPS, AQCE, AQCE-MPS, ADAPT-VQE, HE) across four datasets.** Tables 2 and 3 show ER-AAE-0 and ER-AAE-100 outperforming competing methods, using at most 100 CZ gates while baselines are constrained to use ≥100 gates. The margin is sometimes substantial (e.g., orders of magnitude on MNIST and CIFAR-10).

- **Gate-efficient design: each two-qubit block uses exactly one CZ gate.** The gate set in Eq. (1) is structurally justified (rotations that commute through CZ are removed), giving 4 parameters per block vs. the 15‑parameter general two-qubit unitary that would decompose to 3 CNOT/CZ gates. This directly addresses the inefficiency the paper identifies in prior tensor‑network AAE methods.

- **Theoretical guarantee linking initial fidelity to linear entropy.** Proposition 2 gives |⟨v_target|V(θ)|0⟩|² ≥ 2^{⌊−2L⌋}, which ensures the initial state (after TN initialization) has non-vanishing overlap with the target, avoiding barren plateaus. Figure 2(b) empirically confirms that initial infidelity stays well below 1.

- **Observation that real-world data (MNIST, CIFAR-10) exhibits much faster linear-entropy decay than random vectors (Figure 2(a)).** This is a genuinely useful empirical finding that could guide future AAE research toward data-dependent circuit construction.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Gate counts for baselines are not reported in the results tables.** The paper states that baselines use "the smallest value in [100, +∞) according to constraints in Tab. 1" — this *does* mean baselines use ≥100 gates while ER-AAE uses exactly 100, supporting the "fewer or equal" claim. However, Tables 2 and 3 do not actually list the gate counts for each method/experiment. A reader must compute them from Table 1 constraints, and for AQCE/AQCE-MPS the total gate count is not clearly derivable from the description given. Reporting exact gate counts alongside infidelity values would remove all ambiguity.

2. **The claim that the infidelity bound "scales as O(L)" (line 14, Introduction) is imprecise.** Proposition 2 gives fidelity ≥ 2^{⌊−2L⌋}, so the infidelity bound is 1 − 2^{⌊−2L⌋}. The floor function makes this piecewise constant (e.g., 0.5 for all L ∈ (0, 0.5)), not O(L) in the usual asymptotic sense. The bound serves its practical purpose (non-vanishing initial fidelity), but the O(L) characterization should be corrected or qualified.

3. **No ablation of the restricted gate set (1 CZ + 4 rotations).** The paper motivates this design choice (Eq. (1), lines 82–88) by noting that single-qubit rotations commute through CZ and can be absorbed. But it does not compare against a more expressive ansatz (e.g., general two-qubit unitaries with 3 CNOT gates) to show whether the restriction helps, hurts, or is neutral. An ablation on a small N would strengthen the paper.

4. **C_ER = 1 is used throughout without justification or ablation.** The gate slide parameter controls how often all parameters are jointly re-optimized. Using C_ER = 1 means full retraining after every added gate, which is the most expensive setting. Running even one comparison with C_ER > 1 (e.g., 10 or 100) would clarify the trade-off.

5. **Missing standard deviations / error bars for infidelity.** Tables 2 and 3 report only averages over M = 10 (RQC) or M = 50 (other) samples. For methods with close performance, variance matters. The paper would benefit from including standard deviations or at least noting when differences are within noise.

6. **No discussion of limitations or classical computational cost.** The algorithm simulates 2^N-dimensional vectors (classical), which is feasible for N = 10–11 but becomes prohibitive for larger N. The paper does not mention this regime of applicability, nor does it provide any runtime or complexity analysis (e.g., O(N²) BFGS minimizations per gate added, plus full-parameter retraining at each gate when C_ER = 1). A brief limitations paragraph would improve the paper.

7. **Proposition 2's bound is loose in practice.** The bound decays exponentially in L, but Figure 2 shows that for real data at C = 100, L is near 0, giving a trivial bound near 1. The paper does not report actual L values from experiments, so the reader cannot assess how informative the bound is. This is not a flaw — the bound still guarantees non-zero initial fidelity — but its practical significance is overclaimed relative to its tightness.

8. **The AQCE gate count is underspecified.** The paper says AQCE does forward-backward sweeps (1 or 100 iterations) but does not state how many two-qubit gates the circuit contains. The total gate count depends on whether gates are added during sweeps or only updated. This makes it hard to independently verify the comparison.

### Trivial
- The O(L) characterization in the Introduction (discussed in Minor #2 above) should be corrected.
- The conclusion is brief and repeats results without reflecting on limitations; this can be expanded.

## Nice-to-Haves
- **Matched-gate infidelity curves**: Present infidelity vs. number of two-qubit gates (e.g., 20, 40, 60, 100) for all methods on a single plot. This is the cleanest way to demonstrate gate savings.
- **Ablation of C_ER values** (e.g., 1, 10, 100) to show the effect of gate-slide frequency.
- **Ablation of gate-set expressiveness**: Compare the proposed 1-CZ gate against general two-qubit unitaries (3 CNOT) on a small-N task.
- **Standard deviations** added to Tables 2 and 3.

## Removed Points
These points were removed from the main review with justification:

1. **"The central claim about gate counts is not supported by the comparisons"** — Removed because the paper explicitly says baselines use "the smallest value in [100, +∞)" (i.e., ≥100 gates), while ER-AAE uses 100. The experimental design *does* support the "fewer or equal gates" claim. The critic misread the phrase. Replaced with a transparency issue (Minor #1 above).

2. **"Table 1 is hard to read"** — This is a PDF-parser formatting artifact, not a paper problem.

3. **"HE circuits are a weak baseline"** — HE circuits are a standard baseline in quantum circuit literature. Its inclusion is not a weakness; it merely provides a lower bound.

4. **"The conclusion is weak"** — Subjective. Concluding sections typically summarize. Not a substantive weakness.

5. **"The paper does not discuss whether this choice affects the comparison" (regarding CIFAR-10 encoding)** — The paper describes exactly how each dataset is encoded and states that all methods target the same state. This is sufficient.

6. **"The bound in Proposition 2 contradicts the O(L) claim"** — The critic's claim is too strong. The infidelity bound 1 − 2^{⌊−2L⌋} is imprecise as O(L), but not contradictory. Moved to Minor #2 with corrected explanation.

## Novel Insights
The most interesting insight from the review process is that the reviewers agreed on the paper's core contribution (entropy-reduction as a heuristic for AAE) being sound and the experiments showing good empirical performance, but disagreed on whether the gate-count comparison was properly controlled. This tension reveals that the paper's main weakness is not methodological but presentational: the gate-count claim is technically supported by the experimental design (≥100 gates for baselines), but the lack of explicit per-experiment gate counts in the results tables creates unnecessary ambiguity that could be resolved with a simple formatting change.

## Suggestions
1. **Report the exact gate count used for every baseline in every experiment directly in Tables 2 and 3** (or in a supplementary column). This single change would eliminate the main source of confusion about the central claim.
2. **Correct the O(L) scaling description in the Introduction** — either remove it or clarify that the bound from Proposition 2 gives an infidelity bound that is piecewise constant due to the floor function.
3. **Add a brief "Limitations" paragraph** discussing classical computational cost (O(2^N) simulation), the restricted gate set, and the fact that the theoretical bound is loose.
4. **Add standard deviations to Tables 2 and 3.**

## Score and Decision

This paper proposes a genuinely new approach (entropy-reduction-guided circuit construction for AAE), validates it on multiple datasets, provides a theoretical guarantee against barren plateaus, and outperforms several established baselines. The main advertised claim ("fewer or equal gates") is in fact supported by the experimental design — the critic's central objection was based on a misreading. The remaining weaknesses are presentation improvements, ablations, and quali cations, none of which threaten the core contribution. The paper makes a solid empirical and theoretical contribution to the AAE literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>