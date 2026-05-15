Now I have all the material I need. Let me write the comprehensive review.

## Summary

This paper studies memory savings for families of Strong Lottery Ticket (SLT) models that share a single random source network. It provides theoretical results showing that sharing a source network does not increase the required width beyond the single-target bound (Theorem 3.3), whereas separate sources incur a log(m) width penalty. The paper also proposes novel mask selection criteria (minimizing the union of masks rather than individual sparsity) and an m+1 plane storage scheme that separates overlap bits from per-target extra bits. Experiments on synthetic subsetsum problems (n ≤ 17, m = 4) illustrate that source sharing with overlap-optimized selection reduces total stored bits.

## Strengths

- **First formal comparison of width requirements for shared vs. separate sources in SLT model families.** Theorem 3.3 explicitly derives that a shared source network requires width ~ C d log(1/δ), while m separate sources require C d log(m/δ). Though the log(m) factor is mild, the result cleanly formalizes an overlooked advantage of source sharing and is a genuine theoretical contribution.

- **Novel and well-motivated optimization objective for joint mask selection.** The paper identifies that minimizing the size of the union of masks (Eq. 4) is a more memory-relevant objective than minimizing each mask independently. Theorem 3.5 proves that independent minimization is only an upper bound on the true joint objective, providing formal justification for the proposed Local-bin+opt algorithm that directly optimizes overlap + extra bits.

- **Introduction of the m+1 plane storage scheme.** Decomposing masks into a common overlap plane and per-target extra planes (Eq. 5) is a clean conceptual contribution that directly exploits the structure enabled by source sharing. The paper correctly identifies when this scheme is beneficial (high overlap) versus when it is redundant (low overlap / single-model deployment).

- **Theoretical insight that larger source sizes can improve memory savings.** The counter-intuitive observation that larger source sets (implying larger masks) provide more candidate subsets to choose from, enabling better overlap optimization, is noted in Section 6. While not rigorously proven, it is a genuine insight that challenges naive assumptions.

## Weaknesses

### Fatal
None.

### Major

- **Experiments are entirely synthetic and do not demonstrate the claimed memory savings on actual model families.** The experiments (Section 5, Appendix B) only test single-variable subsetsum approximation with random source sets X ~ U[-1,1] and random targets Z ~ U[-½,½]. The paper's title, abstract, and introduction promise memory savings for "model families," ensembles, and mixtures of experts, but there is zero validation on any trained neural network, even a small one (e.g., MNIST MLPs). How the proposed mask selection translates to compressing full networks with millions of parameters is entirely unaddressed. This is the most significant gap between the paper's claims and its evidence.

- **The mask selection algorithms are exponential in n and fundamentally unscalable to practical source sizes.** Algorithm 1 explicitly initializes an array of size 2^n enumerating all subsets. For realistic SLT constructions, where source widths n must be large (at least hundreds to thousands to achieve meaningful approximation guarantees), exhaustive enumeration is computationally intractable. The paper acknowledges this in passing in Section 6 ("this threshold is not attainable in a computationally effective way") but does not propose any approximate, greedy, or heuristic alternatives. Without such alternatives, the connection between the theoretical insights and any practical compression is severed. The problem of how to find good overlap-optimized subsets at scale is left completely open.

### Minor

- **Theorem 3.4 is sloppily stated and its proof is inconsistent.** The theorem claims M¹ = M² for "similar targets," but the proof says "the targets are identical" — these are different things. The theorem asserts that if two targets lie within ε of the same value z, the same subset M works for both, which is true as an existence statement, but the wording "we have M¹ = M²" reads as a forced equality rather than a choice. Moreover, the remark immediately following the theorem — "similarity of targets does not tend to be associated with higher mask overlaps if we optimize for memory efficiency" — partially contradicts the theorem's implication, creating reader confusion. This does not invalidate the paper's main contributions but reflects unclear reasoning in a supporting result.

- **Experimental scale is very small (n ≤ 17, m = 4) with no scaling analysis.** While we understand the computational limitation arising from the 2^n enumeration, the paper does not probe even moderately larger sizes (e.g., n = 20, 22) to show the wall, nor does it report runtime. The discussion of "moderate, practical sizes" in Section 6 is vague and unsupported.

### Trivial
- Minor language issues (e.g., "we have propose" on line 178).
- Some garbled equation text from parsing artifacts (e.g., line 120).

## Nice-to-Haves
- A comparison against straightforward baselines (e.g., storing target weights directly with half-precision floats, storing independent sparse masks without overlap optimization) would help contextualize the claimed memory savings. The current experiments only compare the paper's algorithms against each other.
- A concrete worked example (n=5, m=2) showing the actual masks, overlap pattern, and how the m+1 scheme stores less data would improve pedagogical clarity.
- A greedy or LP-based approximation for mask selection that runs in polynomial time would be the natural next step to bridge the theory-to-practice gap.

## Removed Points
These points are flagged to be removed; treat them with caution if using them:

1. **"The paper does not discuss this limitation [exponential complexity]"** (from Harsh Critic Issue 2) — The paper explicitly states in Section 6: "this threshold is not attainable in a computationally effective way because the space of all potential subsetsum approximations increases exponentially in the source set size." The paper does discuss it, though it does not resolve it. The valid residue (no approximate alternative proposed) is kept as a Major weakness above.

2. **"No error analysis: the algorithm just guarantees existence, not that the chosen subset satisfies the bound"** (from Harsh Critic's "Missing Verification" point) — This is factually incorrect. Algorithm 1 pre-computes satIndices, which contain only subsets satisfying |subsetSums[s] - Z[i]| < ε. The optimization step (Local-bin+opt) selects from these pre-filtered candidates, so the ε bound is automatically respected by construction.

3. **Calling Theorem 3.5 "a trivial inequality" as a weakness** — The theorem is indeed a simple union bound, but its purpose is to formally establish that independent mask minimization is an upper bound on the joint objective, which is a conceptual contribution that motivates the subsequent optimization strategy. A theorem does not need to be deep to be useful in a paper's logical flow.

4. **"The paper only tests n ≤ 17" stated as a standalone criticism without acknowledging why** — The 2^n complexity constrains the feasible n. This is better captured as a consequence of the scalability issue (Major weakness above) rather than a separate independent criticism.

## Novel Insights
An interesting observation that emerges from synthesizing the reviews is that the paper's strongest contribution is actually the most implicit one: it reframes the SLT mask selection problem from an individual sparsity objective to a joint compression objective. This reframing — minimizing the union of masks rather than independent mask sizes — is a genuinely new perspective that could inform future work even if the specific exponential algorithms proposed here are not directly usable. The paper also correctly identifies that the flexibility from larger source sizes creates a non-trivial trade-off: larger sources give more subset choices for better overlap optimization but increase the baseline storage and the search space. Formalizing this trade-off would be a natural next step for follow-up work.

## Suggestions
1. **Most critical: Bridge the gap between theory and practice.** Either (a) demonstrate the method on at least one small real neural network family (e.g., MLPs on MNIST), verifying that masks found via these (exhaustive) algorithms actually reconstruct the weights and that total memory beats storing models directly, or (b) pivot the paper's framing to explicitly state that it provides theoretical insights and exact algorithms for small-scale settings, leaving approximate methods for future work. Currently the framing oversells the practical applicability.

2. **Develop a polynomial-time approximate alternative.** The field would benefit from a greedy or LP-relaxation approach to overlap-optimized mask selection. Even a simple heuristic with a bound on its suboptimality would make the paper's ideas accessible at practical scales.

3. **Correct Theorem 3.4.** Clarify that M¹ = M² is a choice (there exists a common representation) rather than a forced outcome, and remove the contradictory remark or reconcile it with the theorem statement.

4. **Add baselines.** Compare against storing target weights as half-precision floats and storing independent sparse masks without overlap optimization. This would help readers assess the absolute memory savings, not just relative comparisons among the paper's methods.

## Score and Decision

**Originality:** The core ideas — sharing sources across SLT model families and optimizing mask union rather than individual sparsity — are novel and have not been explored in prior SLT literature.  
**Importance of research question:** Reducing memory footprints of multiple models (ensembles, MoEs) is practically relevant, and SLTs offer a principled approach. The question is well-motivated.  
**Claims support:** The theoretical claims (Theorem 3.3) are well-supported. The practical memory-savings claims are not supported — experiments are on tiny synthetic problems, not on actual models.  
**Soundness of experiments:** The experiments correctly illustrate the theoretical concepts on the synthetic setting but are insufficient to support the paper's broader claims about model families.  
**Clarity of writing:** Generally clear, though Theorem 3.4 and its remark create confusion, and Algorithm 1's notation is dense.  
**Value to community:** The theoretical framing and the m+1 storage scheme provide a foundation that future work could build upon. The paper's main value is theoretical; the practical contributions are limited by scalability.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>