Now I have a complete understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes SaNN (Simplicial-aware Neural Networks), which precomputes neighborhood-aggregated features from simplicial complexes *before* training, then feeds these precomputed features into an MLP. This design moves the expensive adjacency-multiplication operations of existing SNNs to a precomputation stage, yielding substantial reductions in per-epoch training cost. The paper provides theoretical conditions under which SaNN matches the expressiveness of the simplicial Weisfeiler-Lehman (SWL) test, proves permutation and orientation equivariance, and demonstrates competitive empirical performance on trajectory prediction, simplicial closure prediction, and graph classification.

## Strengths

1. **Computationally efficient design with strong empirical speedups.** The core idea of precomputing simplicial neighborhood aggregation and then training only an MLP is practically motivated and effective. The complexity analysis (Section 3) shows SaNN eliminates the O(N_k²) terms present in existing SNNs, reducing per-epoch training complexity to O(T(3N_k D_k² + N_k D_{k-1}² + N_k D_{k+1}²)). Figure 3 empirically confirms that SaNN's runtime stays nearly flat as the simplicial complex grows, while MPSN's grows sharply. The per-epoch runtimes reported in Tables 2–3 show SaNN is often orders of magnitude faster (e.g., 0.001s vs. 5.213s on email-Enron for simplicial closure).

2. **Theoretical analysis linking precomputation-based models to the SWL test.** Theorems 4.1 and 4.2 establish that, with injective aggregation and transformation functions, SaNN is strictly more powerful than the WL test and as powerful as the SWL test — the strongest known higher-order isomorphism test. This is notable because SaNN does not use the sequential message-passing paradigm of prior SNNs. The concrete example (Figure 4) of two non-isomorphic graphs that WL cannot distinguish but SaNN can makes the theoretical claim tangible.

3. **Proof of equivariance properties.** Section 4.2 formally proves that SaNN with summation-based aggregation, MLP transformations, and concatenation is both permutation equivariant and orientation equivariant. These properties are essential for processing oriented simplicial complexes (e.g., trajectory prediction with flow orientations) and place SaNN on equal footing with prior SNNs on geometric consistency.

4. **Competitive accuracy across three diverse tasks.** Despite being far simpler and faster, SaNN achieves competitive (and sometimes best) results on trajectory prediction, simplicial closure prediction, and graph classification. The ablation studies (Section 5.2) validate that combining multiple neighborhood hops and multiple simplex orders improves performance, consistent with the theoretical characterization.

## Weaknesses

### Fatal
None.

### Major

1. **The "constant run-time" claim is overstated and contradicts the paper's own complexity analysis.** The abstract states SaNN has "constant run-time and memory requirements independent of the size of the simplicial complex and the density of interactions in it" (line 4). The introduction repeats "constant training time and memory requirement (independent of the number of interacting simplices)" (line 14). However, the paper's own complexity analysis in Section 3 gives SaNN's complexity as O(T(3N_k D_k² + N_k D_{k-1}² + N_k D_{k+1}²)), which is *linear* in N_k (the number of simplices), not constant. The empirical text more accurately says "almost constant" (line 80). The advantage over existing SNNs is that quadratic terms O(N_k²) are removed from *per-epoch training* time — a genuine and significant saving. But claiming "constant...independent of the size of the simplicial complex" is factually inconsistent with the presented complexity analysis. This language appears in three critical locations and undermines the precision of the paper's primary motivation. **The authors should replace all instances with precise language such as "per-epoch training complexity that scales linearly (not quadratically) with the number of simplices, and is independent of the expensive adjacency multiplications required during training by existing SNNs."**

### Minor

2. **Overclaim of "state-of-the-art" accuracy.** The abstract claims SaNN "achieves state-of-the-art performance" (line 4). Yet the paper's own discussion (Section 5.2) acknowledges that MPSN "is observed to have the best performance on some of the smaller datasets" and describes SaNN's results as "competitive" — which is accurate. SaNN is rarely the top performer in accuracy metrics (MPSN is often better on smaller datasets where it can run), and on larger datasets where MPSN runs out of memory, there is no competitive baseline to compare against. The paper's strength is primarily in computational efficiency, not accuracy dominance. The "state-of-the-art" language should be tempered to describe accuracy as "competitive with existing SNNs" while highlighting the computational advantage.

3. **Statistical significance and variance not reported.** The paper asserts that "in most of the results, the accuracies have significant statistical overlap, i.e., the standard deviations are too high compared to the difference in their means" (line 195) but does not actually report standard deviations, confidence intervals, or error bars for the results in Tables 1–3. Without these, the claim of statistical overlap is unverifiable. The number of runs/trials is also not specified. This affects the reader's ability to assess whether the reported differences between methods are meaningful.

4. **Experimental details insufficient for reproducibility.** The paper does not specify hyperparameters (learning rate, hidden dimensions, number of layers T, optimizer), train/validation/test splits, or how simplicial complexes are constructed from graph-structured datasets. While some of these may appear in a missing appendix (stripped by the parser), the main text currently lacks the information needed to reproduce the results.

### Trivial

5. Minor notation inconsistency: The complexity expression for SaNN uses N̂_k (hat notation) for one term but N_k for others, without explaining the distinction.

6. The garbled footnote text appearing in Section 4.1 (extracted as "T w o t y p i c a l a p p l i c a t i o n s c e n a r i o s ...") is clearly a PDF extraction artifact and would not appear in the submitted PDF.

## Nice-to-Haves

- **Non-simplicial baselines for graph classification.** The graph classification experiments (Table 3) include SPIN (a graph-level method) but not standard GNN baselines such as GCN, GIN, or GraphSAGE. Comparing against these would help isolate the benefit of simplicial structure over graph-level approaches. The paper mentions GAMLP, SPIN, and SIGN as prior scalable graph methods in the theoretical discussion (Section 4) but does not include them as experimental baselines for graph classification.

- **Ablation tables in the main paper.** The ablation results are described qualitatively in the text (Section 5.2) but no tables or figures display the actual numbers. Including ablation tables would strengthen the empirical contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's Claim #2 about injectivity of summation.** The reviewer claimed summation is not injective and that the theoretical guarantees do not apply to the example architecture. However, the paper explicitly qualifies the setting: "Consider simplicial complexes with the same scalar feature *a* as initial feature on all the simplices. For such a scenario, one choice of the aggregation functions...that preserves injectivity is the summation function" (lines 124–125). In this constrained setting, sum = count × a uniquely determines the multiset because all elements are identical. The paper *does* address this. Removed as factually incorrect about the paper's content.

- **Harsh critic's "The paper also frames SaNN as 'simpler' than existing SNNs, but the description of the method...is not noticeably simpler."** This is subjective opinion about presentation style, not a concrete weakness. A model that replaces multi-layer message passing with precomputation + MLP is objectively simpler in training dynamics. Removed.

- **"The ablation studies are referenced but not fully presented."** The text describes ablation results in detail. Tables may have been stripped by the parser. Removed as a parser artifact concern.

- **"Missing related works" / "compare against Y."** The rule prohibits citing missing related works without external confirmation. Removed.

- **Criticisms about garbled text, missing appendix content, or broken characters.** These are parser artifacts, not author errors. Removed per hard rules.

## Novel Insights

One genuinely interesting observation that emerges from the reviews is the subtlety of the "constant time" claim. The paper's empirical runtime curve (Figure 3) is *nearly* flat across simplicial complexes of very different sizes — which is genuinely remarkable and goes beyond what the asymptotic complexity analysis would predict (linear scaling). This suggests that the constant-factor overhead of the precomputation pipeline dominates at practical scales, or that the datasets tested happen to have relatively stable N_k. Understanding when and why the empirical runtime stays flat despite O(N_k) complexity would be a useful follow-up investigation. Beyond this, the main novel insight is the paper's own: that precomputing simplicial neighborhood aggregates can match SWL-level expressiveness while achieving dramatic speedups.

## Suggestions

1. **Fix the "constant-time" language throughout.** Replace every instance of "constant run-time" or "constant training time" with precise phrasing such as "per-epoch training time that is independent of adjacency-multiplication cost and scales linearly (not quadratically) with the number of simplices."

2. **Add standard deviations or error bars** to all tables, and specify the number of independent trials.

3. **Temper the "state-of-the-art" accuracy claim** to "competitive performance" and explicitly state that SaNN's primary advantage is computational efficiency.

4. **Include experimental details** (hyperparameters, splits, optimizer configuration) either in the main paper or an appendix.

5. **Consider adding injective aggregation beyond summation** (e.g., sorted-sum, histogram-based, or a learnable injective function over multisets) to bridge the gap between the theoretical ideal and the practical implementation for non-uniform features.

## Score and Decision

The paper makes a solid contribution: a clearly motivated, theoretically grounded, and empirically validated method that significantly improves the computational efficiency of simplicial neural networks. The theoretical analysis connecting precomputation-based models to SWL expressiveness is noteworthy. The main issues are presentation overclaims (constant time, SOTA) and missing statistical rigor — all fixable without changing the core contribution. This is a solid methods paper suitable for a conference track on geometric/topological deep learning.

**Score: 7.0** (solid accept with minor corrections)

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>