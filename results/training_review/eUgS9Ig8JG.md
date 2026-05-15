Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper proposes SaNN (simplicial-aware neural network), which precomputes aggregated features from multiple hop neighborhoods of each simplex (upper, lower, boundary, co-boundary) using *non-learnable* aggregation functions (e.g., summation). These fixed features are then fed into an MLP for training. This decouples the structural aggregation from the learnable transformation, eliminating the quadratic complexity of standard SNNs during training. The paper provides theoretical conditions under which SaNN is provably more powerful than the WL test and as powerful as the SWL test, and demonstrates competitive performance with 50–100× speedups on trajectory prediction, simplicial closure, and graph classification tasks.

## Strengths

- **Novel and practically motivated precomputation strategy for SNNs.** The idea of pre-aggregating simplicial features (across upper, lower, boundary, and co-boundary adjacencies at multiple hops) before training addresses a real bottleneck — existing SNNs require sequential aggregation during training with quadratic complexity in the number of simplices. This is the first work to systematically propose and evaluate this decoupling for simplicial complexes.

- **Conditional theoretical characterization of expressive power.** Theorems 4.1 and 4.2 establish that, under injectivity of all aggregation, transformation, and combination functions, SaNN is strictly more powerful than the WL test and as powerful as the SWL test (the strongest known discriminative test for simplicial complexes). The paper also provides an explicit counterexample (Figure 4) of non-isomorphic graphs that WL cannot distinguish but SaNN can. These results are mathematically sound as conditional statements and provide principled guidance for architecture design.

- **Competitive empirical performance with large computational speedups.** On simplicial closure prediction (Table 2), SaNN achieves AUC-PR values close to the best SNN models (e.g., 0.929 vs. 0.933 on contact-high-school for MPSN) while being over 100× faster per epoch. On graph classification, SaNN's accuracies are within one standard deviation of MPSN on most datasets, yet per-epoch training time is drastically lower (e.g., 0.05s vs. 0.31s on NCI1). The computational savings are most dramatic on datasets where existing SNNs run out of memory entirely.

- **Equivariance analysis.** Property 1 and Section 4.2 prove that SaNN is permutation equivariant and orientation equivariant — matching the key symmetry properties of powerful existing SNNs (Roddenberry et al., 2021; Bodnar et al., 2021). This shows the pre-aggregation design does not break the desirable inductive biases.

## Weaknesses

### Fatal
None.

### Major

1. **The headline "constant run-time" claim is misleading and factually inconsistent with the paper's own complexity expressions.** The abstract claims "constant run-time and memory requirements independent of the size of the simplicial complex." However, the paper's own complexity analysis (Section 3) gives SaNN's training complexity as O(T(3N_k D_k² + N_k D_{k-1}² + N_k D_{k+1}²)), which is *linear* in N_k (the number of k-simplices), not constant. The introduction specifies "constant training time" (line 14), but the forward pass time in Figure 3 is the MLP-only time, which can be nearly constant per *batch* but still scales with the total number of simplices. The huge improvement is real — SaNN eliminates the quadratic N_k² terms present in SNNs — but calling it "constant" misrepresents the method's actual scaling behavior. The abstract's phrasing is particularly problematic because it invites the reader to believe the method has O(1) cost regardless of problem size, which is not true even for training (precomputation scales with N_k and the adjacency structure).

2. **The "state-of-the-art" claim in the abstract is not supported by the paper's own experimental narrative.** The abstract claims SaNN "achieves state-of-the-art performance." Yet the experimental discussion (Section 5.2) states that MPSN has the best performance on smaller datasets, SaNN is described as "competitive" and "on par," and the paper explicitly notes that "the standard deviations are too high compared to the difference in their means" and "comparisons between the best, second best, and others are insignificant." The paper's own conclusion says SaNN "performs on par with the existing SNN models." The abstract overstates what the evidence supports. No statistical significance tests (e.g., paired t-tests, confidence intervals) are reported to substantiate superiority claims.

3. **Gap between the theoretical injectivity conditions and the practical instantiation.** Theorems 4.1 and 4.2 require injectivity of the aggregation functions f_{k,n}. The example architecture (Section 4.1) proposes summation as an injective aggregator, but explicitly qualifies this claim for "simplicial complexes with the same scalar feature a on all the simplices." For this restricted setting (all features are the same scalar), sum *is* injective (summing n copies of 'a' gives n·a, uniquely determining n). However, the actual experiments use real-valued feature vectors of varying dimensionality, and the paper does not explain how injectivity is maintained in this general setting, does not reference known injective aggregation results (e.g., the GIN line of work showing sum+MLP is injective over countable multisets), and does not analyze whether the specific feature spaces used in practice allow sum to distinguish distinct multisets. This creates a gap between the theoretical guarantees (which are stated as conditionals) and what the experimental architecture provably satisfies. The practical significance of this gap is unclear — the model works well empirically — but the paper needs to bridge it for the theoretical claims to apply rigorously.

### Minor

- **Asymmetric complexity comparison.** The paper compares SaNN's *training-only* complexity against SNN's *total* complexity (including aggregation). The precomputation cost for SaNN (which involves materializing the adjacency relations and performing sparse matrix multiplications) is reported separately in the tables but is not factored into the complexity comparison in Section 3. Including a fair comparison showing total wall-clock time (precomputation + training for SaNN vs. total for baselines) would strengthen the practical claims.

- **The aggregation functions used in experiments are not explicitly specified.** Section 4.1 describes two options (summation and degree-based weighted summation), but the experimental section never states which aggregation was actually used for the reported results. The ablation study mentions degree-based weighted summation is not injective, but doesn't clarify whether the main experiments use plain sum (and if so, what guarantees apply for general features) or the normalized variant.

- **No statistical significance tests.** Given that the paper's own discussion acknowledges statistical overlap between methods, reporting p-values, confidence intervals, or effect sizes for the key comparisons would substantiate the competitive claims.

### Trivial
- The conclusion (Section 6) uses the more accurate phrasing "performs on par," which conflicts with the abstract's "state-of-the-art." This inconsistency should be resolved.
- The $\hat{N_k}$ term in SaNN's complexity expression (line 80) appears to be a typo — it should likely be $N_k$ to match the other terms.

## Nice-to-Haves
- An end-to-end wall-clock time comparison (precomputation + training for SaNN vs. total for all baselines) across datasets would make the computational advantage more transparent.
- A synthetic experiment demonstrating whether the injectivity gap matters in practice (e.g., cases where two non-isomorphic complexes distinguishable by SWL are collapsed by SaNN with sum aggregation) would help the community understand the practical implications.
- Comparing against a simpler baseline — an MLP trained on handcrafted simplicial summary statistics — would help isolate the value of the precomputed structural features from the transformation learning.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"The proof sketches are too vague to verify the technical claims"** — The full proofs are in the appendix, which was stripped by the PDF parser. The paper clearly states it provides proof sketches and outlines the structure.
2. **"The tables are unusable in the extracted text"** — This is a PDF parsing artifact, not an author error.
3. **Strength: "Constant (size‑independent) run‑time and memory requirements"** from the Strength Finder — This conflicts with the verified weakness that the run-time is linear (O(N_k)), not constant.
4. **Strength: "Theoretical guarantee of expressive power matching the SWL test"** from the Strength Finder (in its unqualified form) — The guarantee is conditional on injectivity, and the injectivity gap (Weakness #3) tempers this claim. The theoretical framing itself is retained as a strength but with qualification.
5. **Criticism about "not yet released" or unavailable models/datasets** — None present in the reviews.
6. **Formatting/style nitpicks** about parser artifacts.

## Novel Insights
None beyond the paper's own contributions. The key insight — that precomputing simplicial neighborhood features (across all four adjacency types) decouples structural aggregation from feature transformation and enables training costs independent of the quadratic scaling that plagues existing SNNs — is the paper's own contribution, not a novel meta-insight from the reviews. The reviewer discussions surface an important subtlety about injectivity gaps between theoretical conditions and practical implementations, but this is a critique rather than a novel positive insight.

## Suggestions

1. **Fix the overclaims in the abstract.** Replace "constant run-time" with "training complexity independent of the quadratic adjacency terms (linear in the number of simplices)" and replace "state-of-the-art performance" with "competitive performance" or "on-par performance with dramatically reduced training cost." The paper's actual contributions — massive speedups with competitive accuracy — are strong enough to stand without inflated claims.

2. **Bridge the theory-practice injectivity gap.** Either (a) prove that sum over the specific feature spaces used in experiments is injective (referencing the GIN result that sum is injective over countable multisets), (b) explicitly restrict the theoretical claims to the uniform-scalar setting and add an empirical analysis of when injectivity collapse occurs in practice, or (c) redesign the example architecture to use a provably injective aggregator (e.g., sum of features passed through an injective MLP at each step). The current presentation leaves the reader uncertain whether the theoretical guarantees apply to the evaluated model.

3. **Provide a complete computational cost picture.** Add a table or figure comparing total wall-clock time (precomputation + training for SaNN, total training for baselines) for at least one dataset per task. This would make the practical advantage more concrete.

4. **Specify the experimental aggregation function explicitly** in the main text or a dedicated architecture table, and clarify which theoretical guarantees apply to that choice.

5. **Add statistical significance indicators** (confidence intervals or p-values) for the key comparisons, especially given the paper's own admission of statistical overlap.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>