Now I have thoroughly verified the paper's content. Let me write the consolidated review.

---

## Summary

This paper investigates memory savings for families of neural network models (ensembles, MoEs) represented via Strong Lottery Tickets (SLTs). It shows theoretically that sharing a single random source network across multiple target models does not increase the source width requirement beyond the single-model case (log(1/δ) instead of log(m/δ)), and that shared sources enable better mask overlap for similar targets. The paper proposes an (m+1) mask storage scheme and several mask selection strategies (Partition, Local-bin, Local-bin+opt) that optimize joint memory footprint. Experiments on random scalar subset-sum approximation validate that the Local-bin+opt method with shared sources reduces total bits under the (m+1) scheme compared to individual sparsity optimization.

## Strengths

- **Theoretical width advantage of shared sources (Theorems 3.2, 3.3).** The paper formally proves that reusing a single source for m targets requires source width scaling as C·d·log(1/δ) rather than C·d·log(m/δ) for independent sources. This logarithmic (rather than linear) dependence on m is a concrete and non-obvious theoretical advantage, supported by proofs in Section 3.

- **Formalization of mask-overlap benefit (Theorem 3.4).** The theorem shows that identical targets yield identical masks under a shared source, while with separate reshuffled sources the probability of perfect overlap is only 1/C(n,k). This provides a clean theoretical basis for why shared sources enable better mask compression when targets are similar.

- **Novel algorithmic contributions.** The (m+1) mask storage scheme (Section 4) and the Local-bin+opt algorithm provide a concrete, novel approach to optimizing joint mask storage by minimizing total length (overlap bits + sum of extra bits), going beyond per-mask sparsity optimization typical in prior SLT work.

- **Experimental validation of shared source advantage.** The experiments (Figure 1, n=17, ε=0.001, m=4) show that under Local-bin+opt, a shared source increases overlap bits and reduces extra bits compared to different sources, leading to lower total bits and fewer computations under the (m+1) scheme. The results confirm the theoretical intuition from Theorem 3.4.

## Weaknesses

### Fatal
None.

### Major

- **Gap between claimed scope and experimental validation.** The abstract claims the paper provides "explicit SLT constructions in experiments" and the introduction frames the contribution as memory savings for model families (ensembles, MoEs). However, the experiments are limited to multi-subset-sum approximation on random scalar target values (Z, X sampled uniformly), not on actual neural network parameters. There is no construction of SLTs for any target network, no measurement of actual memory footprints (MB/GB), and no comparison against storing full-precision models or standard independent SLT masks without overlap tricks. The experiments validate the algorithmic comparison at the subset-sum level but do not demonstrate that the proposed scheme yields practical memory savings for real model families. The conclusions drawn are broader than the evidence supports.

- **Scalability of Local-bin+opt is unaddressed.** Local-bin+opt enumerates up to 2^n subsets per source set to find optimal overlaps. The experiments cap n at 17, where this is tractable, but realistic SLT constructions require n ≈ C·log(1/ε) which for moderate precision exceeds 20, making exhaustive search infeasible. The paper acknowledges this computational threshold (Section 6: "this threshold is not attainable in a computationally effective way because the space of all potential subsetsum approximations increases exponentially") but offers no practical algorithm or heuristic for realistic n. Since Local-bin+opt is recommended as the best method under the (m+1) scheme, this limits its practical relevance.

### Minor

- **No comparison against full-precision storage.** The paper reports memory savings purely in "total bits" (set bits in masks), but never compares this against storing the target models in full precision (e.g., float32). Without such a comparison, a reader cannot assess whether the proposed techniques yield any practically meaningful compression ratio. A back-of-the-envelope calculation for even a tiny model would significantly strengthen the paper.

- **"Explicit SLT constructions" overclaim.** The abstract states "we provide explicit SLT constructions in experiments." In practice, the experiments construct masks for random scalar targets — the fundamental building block of SLT constructions — but do not construct SLTs for any actual neural network. This overstates what is demonstrated.

### Trivial
None.

## Nice-to-Haves

- A demonstration on a small real model (e.g., a 2-expert MoE with MLP layers of modest width) that measures actual memory footprint (mask bits + source seed/weights) against full-precision and independent-SLT baselines would greatly strengthen the paper.
- Including a computationally scalable heuristic (e.g., greedy search or relaxed optimization) for finding overlap-efficient masks at larger n would address the main practical limitation.
- Reporting compression ratios (bits saved vs. storing models in float32) for at least the n=17 case would help ground the results.

## Removed Points

These points are flagged to be removed from the harsh critic's review; treat them with caution:

- **"The experiments do not validate the paper's central claims" (in full generality).** The experiments DO validate the core algorithmic claims about shared sources improving mask overlap at the subset-sum level. What they don't validate is the practical memory-savings claim for real models. The Weaknesses section above captures this more precisely as a scope gap, not a wholesale invalidation.

- **"The claimed 'explicit SLT constructions' do not appear" (as a fatal criticism).** The experiments construct masks via the subset-sum approximation that IS the core mechanism of SLT construction; they are "explicit SLT constructions" in the sense that they solve the fundamental approximation problem. The overclaim is real but minor, already captured above.

- **"Lack of any baseline comparison that would justify the claimed memory savings."** The paper DOES compare against baselines: Partition and Local-bin in the m-scheme serve as baselines for storing independent masks without overlap optimization. The missing comparison is against full-precision storage, which is captured as a minor weakness above.

- **"The bit-counting metric is insufficient—it ignores the fact that the source network itself must also be stored."** The paper explicitly discusses storing just the seed for the source network (Section 4: "we only need s and the binary subset masks"), which is standard in SLT memory analysis. The overhead of a single seed is negligible.

- **Criticism of Theorems 3.4–3.5 as "trivial" or low novelty.** While these are simple consequences of existing theory, they serve a useful purpose: they formalize why shared sources enable better overlap and why per-mask optimization is suboptimal. Their value is in framing the problem, not in technical depth.

- **Criticism about missing confidence intervals or single-run evaluation.** These are not standard for this type of synthetic subset-sum simulation; the paper uses 10,000 iterations which provides adequate statistics.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface any insight about the paper that the paper itself does not already express.

## Suggestions

1. **Scope the claims to match the evidence.** Revise the abstract and introduction to state clearly that the experiments validate the subset-sum approximation mechanisms, not full model SLT constructions. Add an explicit limitations paragraph noting that practical memory savings for real model families require future validation.

2. **Add a small-scale neural network experiment.** Construct SLTs for a tiny target model (e.g., a single-layer MLP with width ~10-20) using the proposed methods and report actual memory footprints (mask bits + seed storage) against full-precision and independent-SLT baselines.

3. **Propose a scalable heuristic for Local-bin+opt.** Since exhaustive enumeration is intractable for realistic n, even a simple greedy or randomized variant that approximates the overlap objective, tested for n up to ~25-30, would significantly increase practical relevance.

4. **Include a compression ratio table.** Convert the bit counts into compression ratios relative to full-precision (float32) storage for the parameter values being approximated, to help readers gauge practical impact.

## Score and Decision

**Originality:** The observation that shared sources do not increase width requirement is a valid but incremental extension of existing SLT theory. The (m+1) scheme and Local-bin+opt are genuinely novel algorithmic contributions.

**Importance of research question:** The question of jointly compressing multiple models via SLTs is timely and relevant given the growth of ensembles and MoEs.

**Claims support:** The theoretical claims are well-supported. However, the experimental claims about "explicit SLT constructions" and practical memory savings are not adequately supported — the experiments are at the subset-sum level on random scalars, not on real models.

**Soundness of experiments:** The experimental setup is clean for what it tests (synthetic subset-sum comparison of algorithms), but the connection to the paper's broader claims about model families is missing.

**Clarity of writing:** Generally clear, though some algorithmic descriptions (e.g., bitwise operations in Section 4) could benefit from pseudocode formatting.

**Value to community:** The paper lays conceptual groundwork for multi-model SLT compression and proposes concrete optimization strategies, but the lack of validation on real models limits immediate practical value.

**Overall:** The paper has valid theoretical and algorithmic contributions, but the gap between the claimed scope (memory savings for real model families) and the validation (subset-sum on random scalars) is a significant weakness. The scalability limitation further limits practical relevance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>