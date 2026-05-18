Now I have all the information I need to produce the final consolidated review.

---

## Summary

This paper proposes ER-AAE, a classical algorithm for constructing approximate amplitude encoding (AAE) circuits by greedily reducing linear entropy. The method builds circuits using CZ gates and single-qubit rotations, introduces a theoretical bound linking the final infidelity to the linear entropy of intermediate states (Proposition 2), and provides a tensor-network-based initialization (Proposition 1) to avoid barren plateaus. Experiments on MNIST, CIFAR-10, random vectors, and random quantum circuit states show ER-AAE outperforming existing AAE methods (MPS, AQCE, AQCE-MPS, ADAPT-VQE, hardware-efficient circuits) at the chosen operating point.

## Strengths

- **Novel greedy circuit construction via linear entropy minimization.** Algorithm 1 inductively builds a circuit by selecting, at each step, the two-qubit gate that maximally reduces linear entropy. This differs from prior AAE methods that either fix the circuit topology beforehand or rely on tensor-network decompositions without optimizing gate order based on an explicit entanglement metric. The effectiveness is demonstrated in Fig. 2(a), where linear entropy drops rapidly on real-world datasets.

- **Theoretical infidelity bound linked to linear entropy.** Proposition 2 proves that the initial fidelity after the entropy-reduction phase is at least \(2^{\lfloor-2L\rfloor}\), where \(L\) is the linear entropy of the intermediate state. This provides a formal guarantee that reducing entanglement directly improves approximation accuracy—a connection not established in previous AAE works. The bound is verified empirically in Fig. 2(b), where initial infidelity is away from zero for moderate gate counts.

- **Consistent outperformance at the chosen operating point.** Across all four datasets, ER-AAE achieves the lowest infidelity (Tab. 2) and highest PSNR (Tab. 3) compared to MPS, AQCE, AQCE-MPS, ADAPT-VQE, and hardware-efficient circuits. The comparison uses gate counts matched to at least 100 two-qubit gates for all baselines (the smallest feasible number in \([100,\infty)\) per Tab. 1), and ER-AAE uses exactly 100 CZ gates.

- **Observation of faster entropy decay on real-world data.** Figure 2(a) shows that MNIST and CIFAR-10 images exhibit substantially faster reduction of linear entropy than random vectors and random quantum circuit states. This insight—that natural image distributions are "easy to encode" in terms of low entangled structure—is a useful observation for future AAE research.

- **Practical initialization to avoid barren plateaus.** Propositions 1 and 2 together ensure that the initial encoding state has non-zero fidelity with the target, mitigating the barren-plateau problem. The strategy is specific to ER-AAE and is shown to work in experiments.

- **Gate-slide mechanism to improve global optimality.** The comparison of ER-AAE-0 (no retraining) and ER-AAE-100 (periodic retraining) demonstrates the benefit of the gate-slide mechanism, with the latter consistently yielding lower infidelity.

## Weaknesses

### Fatal

None.

### Major

1. **Experimental comparison at a single operating point without trade-off curves.** The central claim (abstract, Section 5) is that ER-AAE "surpasses the best existing encoding techniques, achieving lower error with an equivalent or fewer number of CNOT or CZ gates." The experiments compare all methods at essentially one gate budget per method: ER-AAE uses exactly 100 CZ gates, while baselines use the smallest feasible number ≥100 (per Tab. 1). Although this yields roughly comparable gate counts (e.g., MPS would use ~108 CNOT, AQCE-100 uses 300 CNOT), the comparison lacks trade-off curves of infidelity versus number of two-qubit gates across a range of budgets for *all* methods. Such curves are standard in the AAE literature (Shirakawa et al., 2021; Rudolph et al., 2023) and are necessary to establish whether ER-AAE's advantage holds across different resource regimes. Without them, the reader cannot evaluate whether the observed advantage is robust or specific to the chosen operating point. This is the paper's most significant weakness.

### Minor

2. **No standard deviations or error bars.** Results in Tables 2–3 are reported as averages over \(M\) samples (\(M=10\) or \(50\)), but no uncertainty estimates are provided. This makes it difficult to assess the statistical reliability of the comparisons.

3. **Computational cost of the gate-slide mechanism not discussed.** Setting \(C_{ER}=1\) means global re-optimization of all parameters using Adam after every single gate addition. This is computationally expensive (100 global optimizations for \(C=100\)), and the paper does not report wall-clock time, optimization step counts, or sensitivity to \(C_{ER}\). For larger systems this may become a practical bottleneck.

4. **No discussion of limitations.** The paper lacks a limitations section. Key limitations worth acknowledging: (a) the algorithm requires classically simulating the full \(2^N\)-dimensional state during circuit construction (memory cost exponential in \(N\)), (b) the greedy search over all \(\binom{N}{2}\) qubit pairs per iteration scales quadratically in \(N\), and (c) the theoretical bound (Proposition 2) ensures a non-zero starting fidelity but does not provide a meaningful guarantee on the final approximation error after training.

### Trivial

5. **The abstract's phrasing "infidelity bounded by the linear entropy" is a minor oversimplification.** The actual bound is \(|\langle v_{\mathrm{target}}|V(\theta)|0\rangle|^2 \ge 2^{\lfloor-2L\rfloor}\), which gives \(\mathrm{infidelity} \le 1 - 2^{\lfloor-2L\rfloor}\). For small \(L\) this scales as \(\mathcal{O}(L)\) (as correctly stated in the introduction), but the abstract's wording could be read as implying a simpler direct relationship. This is a presentational nitpick — the introduction and Proposition 2 are precise.

## Nice-to-Haves

- Add trade-off curves of infidelity vs. number of two-qubit gates for all methods across a range of budgets (e.g., 20–200 gates). This would directly validate the central claim about gate-count efficiency.
- Provide an ablation study on the gate-slide parameter \(C_{ER}\) and the number of slide steps \(T_{ER}\) to justify the chosen values and quantify the cost-benefit trade-off.
- Report standard deviations or confidence intervals for the main results.
- Discuss why real-world data (MNIST, CIFAR-10) exhibit faster entropy decay than random vectors — e.g., analyze the singular value decay or low-rank structure of the data.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that MPS uses 27 CNOT vs ER-AAE's 100 CZ, and the "equivalent or fewer gates" claim is false.** The reviewer calculated 27 CNOT for a single MPS layer, but the paper explicitly states that "the number of CZ/CNOT gates in other methods is chosen to be the smallest value in \([100,+\infty)\) according to constraints in Tab. 1." For N=10, MPS with multiple layers would use at least 108 CNOT (~4 iterations × 9 unitaries × 3 CNOT). The comparison is consistent with the paper's stated methodology. This criticism reflects a misunderstanding of the experimental setup.

2. **Criticism that the CIFAR-10 "compact amplitude encoding" is non-standard.** The paper clearly describes the construction (splitting the 3072-dimensional vector into real and imaginary parts padded to 2048 dimensions for 11 qubits) and cites prior work (Mitsuda et al., 2024) that uses the same approach. This is a legitimate construction, not a flaw.

3. **Criticism that hardware-efficient circuits are a "very weak baseline."** HE circuits are a standard baseline in the quantum ML literature. The paper is transparent about including them, and the significant margin over HE is not claimed as a core result — it provides a lower-bound comparison. Disagreement on baseline choice is a matter of taste, not a weakness.

4. **Criticism that Proposition 2 is "mischaracterized" in the abstract.** The abstract says "infidelity bounded by the linear entropy" and the introduction says "scales as \(O(L)\)." Both are reasonable descriptions: Proposition 2 gives fidelity \(\ge 2^{-2L}\) (ignoring floor), which for small \(L\) gives infidelity \(\lesssim (2\ln 2)L \approx 1.39L\). The bound is indeed a function of \(L\) that scales as \(O(L)\). The reviewer's objection that the exponential form "is not mentioned" ignores that the introduction explicitly states "scales as \(O(L)\)." This criticism substantially overstates the imprecision.

## Novel Insights

None beyond the paper's own contributions. The reviews substantially converge on the paper's framing and do not surface a genuinely novel interpretation that the authors themselves missed.

## Suggestions

1. **Most important:** Add trade-off curves of infidelity vs. number of two-qubit gates (e.g., 20, 40, 60, 80, 100, 120) for ER-AAE and all baselines. This single addition would resolve the main weakness and directly validate the paper's central claim about gate-count efficiency.
2. Add error bars / standard deviations to Tables 2 and 3.
3. Add a brief ablation or discussion of the gate-slide mechanism's computational cost and sensitivity to \(C_{ER}\).
4. Add a "Limitations" section discussing exponential classical memory, \(\mathcal{O}(N^2)\) per-iteration search cost, and the scope of the theoretical guarantee.
5. Correct the abstract to read "infidelity bounded by a function of the linear entropy" for precision, though this is a minor point.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>