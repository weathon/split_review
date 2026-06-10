## Summary

This paper studies positional encodings (PEs) for directed graphs. It introduces *Walk Profile*, a notion that counts bidirectional walks categorized by forward/backward edge composition, and shows it captures many practically relevant directed-graph relations (shortest/longest path distance, common successors/predecessors, feed-forward loops). The paper proves that existing PEs (symmetrized Laplacian, SVD-PE, single-q Magnetic Laplacian) cannot express walk profiles, and proposes **Multi-q Mag-PE** — concatenating eigenvectors from Magnetic Laplacians with multiple potential values q — which provably reconstructs walk profiles via a Fourier inversion argument. A stable architecture extending SPE to complex eigenvectors is also provided. Experiments on distance prediction, sorting network satisfiability, and circuit benchmarks show empirical gains.

---

## Strengths

- **Walk profile is a well-motivated, clean notion of expressivity for directed PEs.** The definition (Definition 2, line 89) naturally generalizes undirected walk counting to bidirectional walks and subsumes practically important relations (shortest/longest path distances, common predecessors/successors, feed-forward loops). This gives the paper a principled target for what a good directed PE should express, rather than evaluating expressivity ad hoc.

- **Theorem 2 (Multi-q Mag-PE provably reconstructs walk profiles) is a non-trivial theoretical contribution.** The proof (lines 136–144) identifies the relation $[\bm{A}_q^\ell]_{u,v} = e^{-i2\pi q\ell}\sum_k \Phi_{u,v}(\ell,k)e^{i4\pi qk}$, showing that recovering the walk profile reduces to inverting a Fourier matrix. The insight that the real-valuedness of $\Phi$ allows reducing the required q-values from $L+1$ to $\lceil L/2\rceil+1$ is clean and theoretically grounded. This goes well beyond empirical observations about Multi-q methods.

- **Theorem 1 (single-q failure) provides necessary grounding.** The statement (line 107–110) that there exist graphs/nodes indistinguishable under single-q Mag-PE with different walk profiles establishes the problem that Multi-q Mag-PE solves. Without this, the multi-q proposal would lack a clear motivation.

- **Dramatic empirical verification on distance/walk-profile prediction (Table 1).** Multi-q Mag-PE with SPE achieves RMSE 0.016 (spd), 0.185 (lpd), and 0.002 (wp) on directed acyclic graphs, versus 0.124, 0.432, 0.040 for the best single-q with SPE — improvements of 7.8×, 2.3×, and 20× respectively. These numbers directly confirm that using multiple q-values yields substantially more information about bidirectional walks.

- **Stable architecture extension to complex eigenvectors is practically useful.** The generalization of SPE (lines 155–185) to handle unitary (rather than orthogonal) basis ambiguity via separate processing of real/imaginary parts fills a real gap, since existing stable PE frameworks were designed for real eigenvectors. The ablation (Table 1: Multi-q Naive 0.353 vs. Multi-q SPE 0.016 for DAG spd) confirms the architecture is essential.

- **Scalability analysis (Section 5.5, Fig. 6).** Training with 10 q-values costs only 1.5–3× the cost of a single q, and preprocessing is negligible. This quantifies the expressivity–cost trade-off practitioners need.

---

## Weaknesses

### Major

- **Experimental confound in distance prediction: Multi-q Mag-PE receives Q× more eigenvector features than single-q Mag-PE, and there is no controlled ablation matching the total feature dimension.** Single-q Mag-PE uses one set of eigenvectors; Multi-q uses Q = ⌈L/2⌉+1 sets (4–9 in these experiments). The paper frames this as an "ablation study" (line 208), but an ablation that introduces more input features cannot distinguish between "the Fourier mechanism enables walk-profile reconstruction" and "more eigenvector features in general improve predictive performance." The dramatic improvements in Table 1 (e.g., 0.124 → 0.016 for DAG spd) could partly reflect increased feature count rather than the specific Fourier-theoretic benefit claimed. A controlled baseline — e.g., single-q Mag-PE using proportionally more top eigenvectors to match the Multi-q dimension, or random matrices of the same dimension — would be needed to cleanly attribute the gains.

- **Theory-experiment q-value range mismatch.** Theorem 2 requires $q \in [0, \frac{1}{4})$ for the Fourier symmetry argument to hold. However, the distance-prediction experiments (line 203) use $\vec{q} = (0, \frac{1}{2L}, \dots, \frac{L-1}{2L})$, giving max q = 0.4 (L=5), 0.45 (L=10), and ~0.467 (L=15) — all exceeding 0.25. The paper's own practical recommendation (line 147) of evenly-spaced q up to $\frac{\lceil L/2\rceil+1}{2(L+1)}$ also exceeds 0.25 (e.g., ~0.333 for L=5). The paper does not acknowledge this discrepancy or argue why the theory should extend to $q > 0.25$. While the linear system may remain well-posed in practice, the formal guarantee as stated does not cover the experimental protocol.

### Minor

- **Real-world gains are modest and sometimes within noise.** On circuit benchmarks (Table 2), Multi-q outperforms single-q on several metrics (Gain, BW) but the margins are small and occasionally overlap within one standard deviation (e.g., PM with undirected-GIN: Multi-q 1.137±0.004 vs. best single-q 1.113±0.022; DSP with SAT-bidirected-GIN: Multi-q 2.616±0.151 vs. best single-q 2.657±0.128). The paper would benefit from discussing why the practical advantage is smaller than the synthetic experiments predict.

- **No empirical validation of stability claims.** Section 3.4 claims that the architecture achieves generalization benefits from stability and smoothness as $q \to 0$, but no experiment measures sensitivity to eigenvector perturbations, adjacency noise, or continuity across q. These properties are asserted based on the architectural form (lines 184–185) but not demonstrated.

- **Theorem 2 statement contains a typo.** Line 133: "let $\vec{q} = (q_1, \dots, q_Q)$ with $Q$ distinct $q$'s and $q_1, \dots, q_{L+1} \in [0, \frac{1}{4})$" — but $Q = \lceil L/2\rceil + 1 < L+1$ for $L > 2$, so the condition references indices beyond the defined vector. This should be $q_1, \dots, q_Q \in [0, \frac{1}{4})$.

- **"First" claim for stable architecture is slightly overstated.** The paper claims "the first basis-invariant and stable neural architecture to handle complex eigenvectors" (lines 28, 183). The architecture follows the SPE template (Huang et al., 2023) extended from real to complex — a non-trivial but incremental generalization. Qualifying the novelty (e.g., "the first work to extend stable PE frameworks to the complex domain") would be more precise.

### Trivial

- None beyond the typo noted above.

---

## Nice-to-Haves

- A dimension-matched ablation (single-q with proportionally more top eigenvectors, or random basis vectors) to isolate the Fourier mechanism from the effect of more features.
- An explicit stability experiment (e.g., adding noise to the adjacency matrix and measuring how much the processed PE changes for single-q vs. Multi-q with and without SPE).
- A discussion of how to select $L$ (the target walk length) for real-world tasks where the relevant walk length is unknown.

---

## Removed Points

These points were flagged in the input reviews but are removed with justification:

- **SVD-PE implementation issues (Harsh Critic).** The claim that poor SVD-PE results "suggest possible implementation issues" is speculative. The paper provides a structural argument for SVD-PE's limitations (lines 115–117), and the poor results are consistent with that narrative. No evidence of implementation problems is presented. → *Removed as speculative.*

- **Missing baselines / comparison to other directed PE methods (Harsh Critic).** The paper compares Lap-PE, SVD-PE, and single-q Mag-PE — which are the standard directed PE baselines in the literature cited. Asking for additional baselines (motif-based PEs, depth-based PEs) is scope creep beyond the paper's stated focus. → *Removed as scope creep.*

- **Missing related works (Harsh Critic).** The reviewer cannot verify the existence of missing references. → *Removed per hard rules.*

- **Formatting/style/artifact complaints (Harsh Critic).** Any criticisms about formatting, missing appendix content, or broken symbols are parser artifacts. → *Removed per hard rules.*

- **Strength Finder's generic strengths.** Claims like "the paper addresses an important problem" or "the motivation is well-constructed" are generic and lack concrete anchors. → *Dropped.*

---

## Novel Insights

None beyond the paper's own contributions. The reviews affirmed the paper's core theoretical findings but raised valid concerns about the experimental design; neither reviewer identified a genuinely novel synthesis that the paper itself does not already provide.

---

## Suggestions

1. **Add a dimension-matched ablation for distance prediction.** Compare single-q Mag-PE using K× (K = Q) as many top eigenvectors (or using K independent eigen-decompositions of random Hermitian matrices). If Multi-q still dominates, the Fourier mechanism explanation is strongly supported; if not, recalibrate the empirical claims.
2. **Resolve the q-value range mismatch.** Either (a) restrict experiments to $q < 0.25$ and verify the results still hold, or (b) extend the theory to cover $q < 0.5$ (possible since the Fourier matrix depends on $e^{i4\pi q}$, which has period 0.5) and explicitly state the extended condition.
3. **Add one explicit stability experiment** (e.g., perturb the adjacency matrix and measure how much the processed PE changes) to validate the claimed stability benefits.
4. **Discuss the gap between synthetic and real-world performance.** The circuit benchmarks show smaller gains than distance prediction; a paragraph analyzing why (e.g., real tasks may not require long walk profiles, or other graph features already capture relevant information) would strengthen the paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>