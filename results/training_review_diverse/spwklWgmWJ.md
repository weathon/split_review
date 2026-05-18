Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper studies the memory footprint of representing multiple models as Strong Lottery Tickets (SLTs) — i.e., as binary masks applied to a shared random source network. The authors show that sharing a source does not increase the required source width over the single-target case (theoretically), formulate the joint memory minimization objective as minimizing the union of masks, propose the $(m+1)$ storage scheme (overlap plane + extra planes), and develop algorithms (Partition, Local-bin, Local-bin+opt) that select approximating subsets to optimize sparsity or joint overlap. Experiments on synthetic multi-subsetsum problems validate that the Local-bin+opt algorithm with a shared source reduces total bits and computations compared to independent sparsification approaches.

## Strengths

1. **Problem formulation and joint optimization objective.** Identifying that the *union* of masks (rather than individual sparsity) is the correct objective for joint memory minimization in shared-source SLTs is a useful conceptual contribution. The $(m+1)$ storage scheme (overlap plane + extra planes) and the translation of mask overlap into a concrete encoding savings is a clean formulation that prior SLT work has not explicitly addressed.

2. **Formal width comparison for shared vs. separate sources.** Theorem 3.3 formalizes that sharing a source yields source width $d' \sim C d\log(1/\delta)$ versus $d' \sim C d\log(m/\delta)$ for separate sources, showing the width penalty is only logarithmic in $m$. While the underlying proof is a direct adaptation of Pensia et al. (2020), the explicit comparison is a useful reference point for practitioners considering shared-source SLTs.

3. **Algorithmic instantiation of joint mask optimization.** The Local-bin+opt algorithm, which explicitly minimizes overlap+extra bits within the $(m+1)$ scheme, is a concrete proposal that goes beyond independent sparsification. The experimental results in Figure 1 demonstrate that this approach yields measurable reductions in total bits and average computations compared to Partition and Local-bin when using the $(m+1)$ scheme.

4. **Empirical confirmation that source sharing promotes overlap.** Figure 1 shows that shared sources yield higher overlap bits and fewer extra bits than different sources for Local-bin+opt, directly supporting the theoretical intuition of Theorem 3.4.

## Weaknesses

### Fatal
None.

### Major

1. **Experiments are restricted to synthetic multi-subsetsum problems; no actual neural network is constructed or evaluated.** The paper motivates the work with reference to large-scale MoEs, ensembles, and foundation models, and the abstract promises "explicit SLT constructions in experiments." However, the experiments (Section 5) only test on random scalar targets and sources ($n \leq 17$, $m=4$). No actual neural network — not even a small MLP on MNIST — is ever built, pruned, or evaluated. While the subsetsum approximation is indeed the foundational primitive of SLT constructions, the paper would require validation on actual derived target networks to support its claimed relevance to practical model families. The gap between the motivating applications (billions of parameters, edge-device deployment) and the validated setting (scalars drawn uniformly at random) is substantial.

2. **The mask optimization algorithms do not scale to realistic network sizes.** Algorithm 1 enumerates all $2^n$ subsets of each source set (line: "Initialize each element of subsetSums of size $2^n$ to 0; for $i\in\{1,2,...,2^n\}$ do subsetSums[$i$] $\leftarrow X\odot binary(i)$"). For $n=17$ this is $131K$ evaluations per source element — feasible for scalar targets but prohibitive when scaled to millions of parameters. The paper acknowledges the exponential search space in the Discussion ("the space of all potential subsetsum approximations increases exponentially") but does not provide any approximation algorithm, heuristic, or complexity analysis to address this. Without a scalable approach, the proposed optimization framework cannot be applied to the settings that motivate the paper. This is the most significant barrier to the paper's practical relevance.

### Minor

1. **Theoretical novelty is modest; core results are straightforward extensions of existing work.** Theorem 3.2 is a simple union bound extending the single-target subsetsum bound to $m$ targets. Theorem 3.3's proof is stated as "analogous to the one of Theorem 1 (Pensia et al., 2020)." Theorem 3.4's first statement (identical targets $\implies$ identical masks) is definitional; the second statement (probability of overlap under reshuffled sources is $1/\binom{n}{k}$) is a basic combinatorial calculation. Theorem 3.5 (individual sparsity minimization is an upper bound on union minimization) follows directly from $|\bigcup M^k| \leq \sum |M^k|$ via the union bound. The paper's genuine contribution lies in *identifying and formulating* the joint memory optimization problem rather than in deep new theory, but the theorems are presented with weight disproportionate to their technical depth.

2. **No comparison against standard baselines for memory footprint.** The paper compares only between its own mask-selection strategies (Partition vs. Local-bin vs. Local-bin+opt) and between shared vs. separate sources. There is no comparison against simply storing the target model weights in a standard format (e.g., float16, int8, quantized) or against other model compression techniques mentioned in the related work. The central claim of "memory savings" is never quantified against a straightforward non-SLT alternative, making it difficult for the reader to assess whether the savings are practically significant.

3. **Limited exploration of the relationship between source size $n$ and memory savings.** The paper notes in the Discussion that "larger source sizes...can achieve higher memory savings" and hypothesizes saturation, but experiments only use $n=14,15,16,17$. A systematic study of how total memory scales with $n$ (and where the hypothesized trade-off becomes unfavorable) is absent.

### Trivial

1. The pseudocode in Algorithm 1 could be clearer: the algorithm is presented with parser artifacts and the `OptAlgorithm` branching is embedded inline, making it harder to distinguish the core multi-subsetsum routine from the specific optimization strategies.
2. Some notation is overloaded (e.g., $M$ used for masks, sets of masks, and the set of masks under different schemes).

## Nice-to-Haves

- An analysis or heuristic for approximating the optimal subset selection without exhaustive $2^n$ enumeration (e.g., greedy, dynamic programming, or randomized approaches) would substantially strengthen the practical relevance.
- Providing an estimate of total memory (source + masks) in the SLT framework and comparing it to the memory required to store the target models directly (e.g., in float16) would help calibrate the claimed savings.
- A small-scale validation on a real neural network (e.g., a 2-layer MLP on MNIST with $m=2$ targets) would significantly bolster the claim of "explicit SLT constructions."

## Removed Points

- The critic's claim that "subtraction with bitwise xor operator" is incorrect: in $GF(2)$, addition and subtraction are identical, and for the bit-level operation described (extracting non-overlapping bits), XOR is correct. This is a misunderstanding, not a paper error. **Removed.**
- Several formatting/style nitpicks about paper structure and the schematic diagram description. **Removed per hard rules.**
- The critic's comment that the paper "does not even test on a single target network derived from a standard dataset" is noted and preserved as a valid weakness, but the characterization that the paper's claims are "purely speculative" is an overstatement — the experiments validate the claims at the subsetsum level, which is the appropriate abstraction for the paper's theoretical contributions. **Downgraded from "fatal" to "major."**
- The critic's complaint that Theorem 3.5 is "not a theorem but an elementary inequality" is accurate, but the paper's framing is as an observation about suboptimality of independent optimization, which is a valid point even if the inequality itself is basic. **Kept as minor weakness (point 1 in Minor).**

## Novel Insights

The key insight that emerges from the reviews — one that the paper itself states but does not fully capitalize on — is the fundamental trade-off triangle between source size $n$, mask sparsity, and mask overlap. Larger $n$ gives more subset choices and can improve joint memory efficiency (more overlap opportunities), but simultaneously increases the per-mask bit-width and the search complexity. The paper identifies this trade-off qualitatively but provides neither a theoretical characterization (e.g., the optimal $n$ as a function of target statistics and $m$) nor an empirical map of the Pareto frontier. This is a genuinely interesting direction that the paper opens but does not resolve.

## Suggestions

1. **Address the scalability bottleneck.** The $2^n$ enumeration is the single largest barrier to practical relevance. Even a brief complexity analysis or a sketch of a polynomial-time approximation (e.g., greedy subset selection or relaxed optimization) would be valuable.
2. **Validate on at least one small neural network.** Constructing SLTs for a small MLP (e.g., MNIST, $m=2$ targets) using the proposed algorithms would substantially close the gap between the theoretical claims and practical validation.
3. **Add a baseline memory comparison.** Quantify the total storage (seed + masks) under the best (m+1)-scheme encoding against the size of the target weights in a standard compressed format (e.g., fp16 or int8) to give the reader a concrete sense of the savings magnitude.
4. **Systematically study the effect of source size $n$** on total memory to validate the hypothesized trade-off and saturation discussed in Section 6.

## Score and Decision

The paper identifies a genuinely underappreciated problem (joint memory optimization in shared-source SLTs) and provides a clean formulation and proof-of-concept algorithms. However, the validation is confined to synthetic subsetsum problems with $n\leq 17$, the optimization algorithms do not scale to realistic network sizes, and no baseline comparison against standard weight storage is provided. The theoretical results, while correctly stated, are straightforward extensions of existing work. These limitations are significant enough that the paper in its current form does not establish its claimed practical relevance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>