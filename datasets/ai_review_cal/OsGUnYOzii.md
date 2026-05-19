- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 5, 8
Now I have all the information needed. Let me compile the review.

## Summary

This paper proposes SCRaWl, a neural architecture for simplicial complexes that replaces expensive message passing with random walks on simplices, processed via 1D convolutions. The method extends the graph-based CRaWl framework to higher-order simplices by introducing two random-walk sampling strategies (uniform connection and uniform neighbor sampling) and constructing walk feature matrices that encode simplex features, face/coface features, and local structural information. The authors prove that SCRaWl's expressiveness is incomparable to message-passing simplicial networks (MPSN) and evaluate on citation imputation and social contact vertex classification tasks.

## Strengths

1. **Novel random-walk sampling schemes for simplicial complexes (Section 3.1):** The paper introduces two principled strategies (uniform connection sampling and uniform neighbor sampling) that extend random walks to higher-order simplices by explicitly handling faces and cofaces. This is a genuine methodological advance over prior work that only considered graph random walks.

2. **Clean demonstration of the value of higher-order interactions (Section 5.2, CRaWl ablation):** The ablation comparing SCRaWl against its graph-only counterpart CRaWl on the social contact datasets is the paper's strongest evidence. CRaWl achieves roughly 0.8 (primary) and 0.94 (high school), while SCRaWl achieves 0.927 and 1.0 respectively, cleanly isolating the benefit of capturing higher-order simplices. This is a well-designed control experiment.

3. **Competitive empirical performance on real-world datasets:** On the Semantic Scholar citation imputation task (Figure 4), SCRaWl matches or exceeds MPSN across most missing rates and simplex orders (e.g., 0.95–1.00 accuracy), and clearly outperforms SCNN, SAN, SNN, and SAT. On the primary school social contact dataset, SCRaWl (0.927) substantially outperforms MPSN (0.727). On the high school dataset, SCRaWl achieves perfect accuracy (1.0 ± 0.0).

4. **Walk re-use and efficient sampling via boundary maps (Section 3.5):** The paper describes computational optimizations — reusing the same collection of random walks across all layers and efficient sampling using boundary matrices — that address the combinatorial cost concerns inherent to higher-order models.

## Weaknesses

### Fatal
None.

### Major

1. **Abstract and introduction overclaim relative to the empirical evidence.** The abstract claims the model "outperforms other simplicial neural networks" and the introduction states it "outperforms existing approaches on real-world datasets." The evidence shows a more nuanced picture: on Semantic Scholar, SCRaWl is *on par with* MPSN (the paper's own text at line 880 says "on par with MPSN"), with both models achieving 0.94–0.99 accuracy across settings — the differences are a few percentage points at most. On the primary school dataset, CAt-Walk (a hypergraph method) marginally outperforms SCRaWl (0.932 vs 0.927). The paper also says in the conclusion "outperforms existing simplicial neural network architectures on a co-authorship network" — this is technically true since the co-authorship experiments show SCRaWl matching or exceeding baselines, but the overall tone of the abstract is stronger than the evidence comfortably supports. The paper would be more accurately served by language like "competitive with or better than existing simplicial neural networks."

### Minor

2. **Theoretical expressiveness result (Theorem 1) is technically correct but provides no insight specific to the simplicial setting.** The proof (lines 750–754) reduces entirely to the graph case: on 1-simplicial complexes (graphs), SCRaWl = CRaWl and MPSN = GNN, and CRaWl and GNN are incomparable per prior work. While this is a valid proof that incomparability holds for simplicial complexes generally (since graphs are a subclass), it adds nothing beyond what was already established by Toenshoff (2023). The paper does not construct any example involving actual 2-simplices (triangles) or higher where the two models diverge, and provides no analysis of expressiveness on complexes with genuine higher-order structure. This limits the theoretical contribution to a "by inheritance" result.

3. **The claimed computational trade-off is not empirically demonstrated.** Section 3.1 states: "by choosing the number of random walks sampled, we can effectively trade off the computational demands with the expressivity of our architecture." Despite this being a central motivation, the paper contains no experiment varying the number of walks *m*, no study of walk length, and no runtime comparisons against MPSN or other methods. Section 3.5 discusses efficient sampling but addresses implementation efficiency, not the trade-off claim. Without empirical characterization, this remains an untested assertion.

4. **Missing ablations on key architectural choices.** The method has several design knobs: two random walk sampling strategies (uniform connection vs. uniform neighbor), pooling method (mean vs. sum), window size *s*, and CNN architecture. None of these are ablated. Given the complexity of the method (six sub-matrix components in the walk feature matrices), the absence of ablations makes it difficult to attribute performance to specific design decisions rather than aggregate engineering.

5. **Comparison with CAt-Walk (hypergraph method) is handled only in text without tabular summary.** Line 1005 notes that CAt-Walk "marginally outperformed SCRaWl" on primary school (0.932 vs 0.927), but this comparison is not presented in a table or figure alongside the other methods. The paper would benefit from a consolidated results table.

### Trivial
None.

## Nice-to-Haves

- A runtime or wall-clock comparison between SCRaWl and MPSN on at least one dataset would substantiate the computational motivation.
- A non-trivial expressiveness example involving simplicial complexes with actual 2-simplices (rather than only graphs) would give genuine content to Theorem 1.
- Adding more diverse benchmark datasets from the simplicial literature (e.g., trajectory prediction or edge flow tasks) would test generalization beyond the two structurally similar domains tested.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper omits SNN and SAT results from the Semantic Scholar plot for readability"** — REMOVED. The paper explicitly states (line 871) that these were omitted for readability, which is a standard and reasonable practice. The paper also notes that these methods performed worse, so their omission does not hide negative results.
- **"No table of full results"** — REMOVED as a "missing" weakness. Figures with clear error bands are standard in this literature; a table would be helpful (moved to Nice-to-Haves) but omitting one is not a weakness.
- **"Hyperparameter details should be in main text"** — REMOVED. The paper refers to an appendix section (Section 6:training-details) that was stripped during extraction. The paper cannot be penalized for appendix content that the parser removed.
- **"Statistical significance testing"** — REMOVED. Reporting means and standard deviations over 5–10 runs is standard practice in this field; demanding significance tests is a field-specific preference, not a valid weakness.
- **Strength Finder's point about "Walk feature matrices encode rich local structural information"** — REMOVED. This is a generic description of the method's design, not a verifiable strength. Every method has a feature representation; calling it a strength without comparative evidence is sycophancy.
- **Harsh critic's claim that at 50% missing on Semantic Scholar "the best SCRaWl line reaches ~0.96 while the best MPSN line reaches ~0.97"** — REMOVED. The actual data shows SCRaWl's best line at 50% reaches 0.98 (dashed line), while MPSN's best reaches 0.97. The specific numerical claim is factually wrong, though the broader point about closeness remains and is already captured in Weakness #1.
- **"The overall picture is: SCRaWl is sometimes better, sometimes tied, and on one dataset slightly worse than a non-simplicial competitor"** — REMOVED from the main weakness section as it is the same concern already captured in Weakness #1 (overclaiming). The empirical picture is already accurately described in the strengths and weakness.
- **Criticism about missing related works** — REMOVED per instructions. I cannot verify whether related works are missing.
- **"Forcing minimum 100 epochs"** — REMOVED. The paper transparently explains this to avoid early stopping during the accuracy dip around epochs 30–50. This is standard practice, not a flaw.

## Novel Insights

None beyond the paper's own contributions. Both reviews largely re-state what the paper says, with the harsh critic identifying genuine but manageable gaps (overclaiming, missing ablations, thin theory). The most useful observation from the review process is that the paper's strongest contribution — the CRaWl ablation cleanly isolating the value of higher-order information — is underemphasized relative to the overclaimed "outperforms" narrative. The paper would be more compelling if it leaned into this controlled comparison as the primary evidence rather than making broad superiority claims.

## Suggestions

1. Temper the abstract and introduction claims: replace "outperforms other simplicial neural networks" with "is competitive with or exceeds existing simplicial neural networks" or "achieves strong empirical performance." The evidence supports competitiveness, not clear dominance.
2. Add an ablation study varying the number of random walks *m* and walk length, with runtime measurements, to support the claimed computational-expressivity trade-off.
3. Provide at least a brief analysis or example of expressiveness on a simplicial complex containing actual 2-simplices, or honestly note that the theoretical contribution inherits from the graph case.
4. Add a concise table of numerical results (mean ± std for all methods and datasets) so readers can compare directly without reading overlapping plot lines.
