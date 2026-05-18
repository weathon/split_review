Now I have all the information I need. Here is my consolidated review.

## Summary

This paper studies memory savings for families of Strong Lottery Tickets (SLTs) that share a single random source network. The authors show theoretically that sharing a source avoids a log(m) width penalty incurred by using m separate sources (Theorems 3.1–3.3), propose that the union of binary masks — rather than individual mask sparsity — is the correct objective for memory-efficient storage (Theorem 3.5), and introduce an (m+1) plane storage scheme with three algorithms (Partition, Local-bin, Local-bin+opt) for joint mask selection. Experiments on synthetic data (n=14–17, m=4) validate that shared sources and union-optimized masks reduce bit-level storage compared to separate sources or sparsity-only optimization.

## Strengths

1. **Identifying that SLT source sharing avoids a width increase for model families.** Theorem 3.2 and Theorem 3.3 rigorously show that sharing a single source requires width d' ~ C d log(1/δ) whereas m independent sources require d' ~ C d log(m/δ). While the derivation is a straightforward union bound, the paper is the first to formalize this comparison in the SLT context and note that the existing SLT existence proofs (Pensia et al., 2020) already support multiple targets from a single source without additional width cost.

2. **Proposing union-of-masks as the correct memory optimization objective.** Theorem 3.5 and Eq. (4) identify that individually minimizing each mask for sparsity only upper-bounds the total storage, and that directly minimizing the union of masks can yield better memory efficiency. This is a conceptually clean insight that reframes the problem beyond per-mask sparsity, which prior SLT work (Ramanujan et al., 2020; Otsuka et al., 2024) did not address.

3. **The (m+1) plane storage scheme and Local-bin+opt algorithm.** Decomposing masks into one overlap plane plus m extra planes (Eq. 5) is a simple encoding that exploits shared structure. Local-bin+opt (Alg. 3) is designed to directly minimize total bits under this scheme. Experimental results confirm that this combination reduces total bits and average computations compared to the standard (m)-plane scheme with sparsity-only optimizers (Section 5, Figure 1).

4. **Experimental confirmation of shared-source advantage on synthetic data.** The experiments (Section 5) show that shared sources increase overlap bits and reduce extra bits compared to separate sources, particularly for Local-bin+opt, consistent with Theorem 3.4. For synthetic subset-sum approximation problems, the results cleanly separate the regimes where each algorithm and storage scheme is preferable.

## Weaknesses

### Fatal
None.

### Major

1. **No experiments on actual neural networks, despite claims of practical relevance.** The paper's abstract and introduction frame the contribution in terms of "large-scale models," "resource-constrained devices," and "explicit SLT constructions in experiments." Yet all experiments are on synthetic subset-sum approximation with random targets and sources (n=14–17, m=4). There is no experiment on any actual neural network — not even a small MLP on a standard benchmark like MNIST or CIFAR-10. The bit-level memory savings reported do not correspond to actual model storage (bytes saved, parameters eliminated). Without validation on real architectures at any scale, the paper's practical claims are unsubstantiated.

2. **Algorithms are heuristic with no analysis of complexity or approximation guarantees, and the main optimization objective is acknowledged as computationally intractable.** Algorithms 1–3 are described procedurally with no analysis of runtime complexity, approximation ratios, or optimality gaps relative to the union-minimization objective. Algorithm 3 (Local-bin+opt) requires enumerating overlap patterns across all targets, which is exponential in m and n. Section 6 acknowledges that "this threshold is not attainable in a computationally effective way because the space of all potential subsetsum approximations increases exponentially in the source set size." The paper offers no practical alternative or scalable approximation for realistic n (e.g., n in the millions, as in neural networks), which severely limits the applicability of the proposed approach.

### Minor

1. **The theoretical contributions are elementary extensions of known results.** Theorem 3.2 is a direct union bound (replacing δ with δ/m). Theorem 3.3 is an immediate corollary plugging Theorem 3.2 into the standard MLP construction, with a one-line proof citing Pensia et al. (2020). Theorem 3.4 states that identical targets can use identical masks (immediate from the definition of subset-sum approximation) and that random reshuffling gives overlap probability 1/choose(n,k) (a basic combinatorial count). Theorem 3.5 observes that individual minimization is an upper bound on the union (immediate from the union bound inequality). While these results are correct and useful for framing the problem, the paper's claim of "novel insights into subset-sum approximation" is overstated — the novelty lies in the problem framing (union minimization) and algorithmic design, not in the theorems themselves.

2. **The "larger source sizes → more memory savings" claim is stated but unsupported.** Section 6 discusses that larger sources offer more subset choices, potentially improving overlap and reducing total bits, but acknowledges this effect saturates at a computationally unattainable threshold. The paper provides no bound, empirical demonstration, or even a synthetic experiment isolating this trade-off to show that savings outweigh the increased mask size. As stated, the claim remains an interesting hypothesis without evidence.

3. **Connection between bit-level counts and actual memory storage is not developed.** The paper compares masks in terms of number of bits, with a brief mention of "bitwise compression, run-length encoding, etc." (Section 4). No analysis is given of how masks would be stored in practice (e.g., compressed sparse row format, integer encoding) or what overhead the mask representation would incur relative to storing the original model weights. The numbers reported — bits in synthetic masks — are not translated into any realistic memory metric, making it difficult to assess the practical magnitude of the claimed savings.

### Trivial
None.

## Nice-to-Haves

- An experiment on at least one small neural network (e.g., an MLP on MNIST) using the existing SLT construction pipeline would greatly strengthen the paper's practical claims. Reporting actual memory in bytes (number of stored weights + masks + seed) rather than bit counts would bridge the gap to practice.
- A greedy or relaxation-based approximation algorithm for mask selection at large n, with some complexity or approximation analysis, would make the approach more credible as a practical method.
- An ablation isolating the effect of source size on total memory (bits in mask + bits in source) for moderate n (e.g., n up to 30) could support or refute the "larger sources help" claim.

## Removed Points

- **Criticism that Theorem 3.1 is a "restatement":** The paper transparently attributes Theorem 3.1 to Lueker (1998) and Pensia et al. (2020). The fact that it is a restatement of prior work is acknowledged, not concealed — this is proper scholarship, not a weakness.
- **Garbled equation and formatting criticisms in Point 5:** The garbled equation (line 61: "d′i ≥ Cdi−1 logmdiin−{1ϵd,iδℓ}") is a PDF parser artifact, not a submission error. Pseudocode readability issues are partly attributable to parsing. Per the hard rules, these are removed.
- **Criticism that the paper "does not meet the standard for a theoretical contribution":** The paper's contribution is not purely theoretical — it is a mix of problem framing, algorithmic design, and proof-of-concept experiments. Evaluating it solely as a theory paper (requiring nontrivial bounds) or solely as a systems paper (requiring large-scale deployment) is unreasonable. Evaluated on its own terms, the paper makes a recognizable if limited contribution.
- **Missing related works:** Per the hard rules, I cannot confirm whether specific related works exist, so I do not raise or retain this criticism.

## Novel Insights

The reviews surface a misalignment between the paper's framing and its execution. The paper is presented as a practical memory-saving technique for large models, but all evidence is at the synthetic subset-sum level with tiny n. Meanwhile, the theoretical results are too elementary to stand as a self-contained theory contribution. The paper would be better positioned as what it actually is: a problem-framing paper that identifies union-of-masks minimization as the right objective for multi-target SLT memory, provides simple supporting theory, and gives a proof-of-concept on synthetic data. This reframing would eliminate most of the tension between the reviews. The (m+1) scheme and the observation that individual sparsity optimization is suboptimal for joint storage are genuine insights that the SLT community should be aware of, but the paper needs either stronger theoretical results (nontrivial bounds on achievable union size) or real neural network experiments to meet the standards implied by its current framing.

## Suggestions

1. Reframe the paper to accurately reflect its scope: a problem-framing and proof-of-concept paper rather than a fully-validated practical method. This would align claims with evidence.
2. Add at least one experiment on a real neural network (even a tiny MLP) using existing SLT construction methods, and report actual memory (bytes) rather than abstract bit counts.
3. Either provide a scalable approximation algorithm for mask selection at large n (e.g., greedy or relaxation-based) with some analysis, or explicitly position the exhaustive enumeration as a small-n analysis tool and scope the paper accordingly.
4. Tone down the "novel insights" framing for the theorems, which are straightforward derivations from known results. The genuine novelty is in the problem formulation (union minimization) and the algorithmic design, not in the proofs.
5. Clarify or remove the unsupported "larger source sizes → more memory savings" claim, or provide a concrete bound or experiment that quantifies the trade-off.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>