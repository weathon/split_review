Now I have enough information from the paper. Let me produce the final consolidated review.

---

## Summary

This paper challenges the prevailing assumption that Graph Structure Learning (GSL) meaningfully improves GNN performance. It proposes a three-step framework for understanding GSL (bases generation, structure construction, view fusion), provides a theoretical bound showing that mutual information does not increase when graph convolution is applied to GSL-constructed graphs (for deterministic construction methods), and presents extensive experiments showing that GSL fails to improve over baselines under fair comparison. Adding GSL to 4 GNN backbones does not improve accuracy, and removing GSL from 8 SOTA GSL methods maintains or improves performance while reducing computational cost. The paper argues that apparent GSL gains actually stem from pretrained bases and self-training, not from the graph structure learning itself.

## Strengths

1. **Comprehensive and carefully controlled empirical evaluation.** The paper evaluates both "add GSL to baselines" (4 GNN backbones × 5 bases × multiple datasets) and "remove GSL from SOTA methods" (8 existing GSL methods), under controlled hyperparameter tuning. The SOTA-GSL ablation — where GSL graphs are replaced with the original graph or MLP layers — is particularly clean and provides direct evidence that the structure learning component adds no value. This is the strongest evidence in the paper.

2. **Conceptually useful three-step framework.** Decomposing GSL into bases generation, structure construction, and view fusion (Section 3, Figure 2) is more comprehensive than prior categorizations that focus only on structure construction. This framework enables the paper to isolate and test each component's contribution, and provides a valuable organizing principle for the community.

3. **Identification that pretrained bases (not graph structure) drive improvements.** The ablation in Section 5.3 (Figure 6) shows that using pretrained representations (MLP(X), GCN(X,A)) significantly boosts performance on heterophilous datasets like Texas, Cornell, and Wisconsin, while the graph construction step itself adds no benefit. This reframes the discussion from "GSL helps" to "self-training and better representations help."

4. **Novel insight into why GSL can appear to help on heterophilous graphs.** The paper's Observation 3 and theoretical framing explain that when MLP outperforms GCN on heterophilous graphs, GCN+GSL may also appear to outperform GCN — but only because it is bounded by the MLP on the same bases, not because the structure learning is beneficial.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Abstract overclaims relative to what the theory proves.** The abstract states that "no matter which type of graph structure construction methods are used, after feeding the same GSL bases to the newly constructed graph, there is no MI gain." However, Theorem 2 only covers deterministic graph construction from fixed bases (e.g., kNN). The paper's own footnote (line 146) acknowledges this limitation: "this theoretical analysis cannot be extended to optimization-based GSL." This creates a mismatch between the strength of claim in the abstract and what the theory actually supports. The empirical experiments on optimization-based SOTA methods do shore this up, but the abstract should be scoped to match the theory.

2. **Ambiguity in "best-performing GSL bases" for Table 1.** The paper states (line 163) that all models were trained on each of the 5 GSL bases, which implies a fair per-base comparison. However, the claim that results are reported "using the best-performing GSL bases" (line 167) is ambiguous: it is unclear whether the same base is used for all methods on a given dataset or whether each method's best base is reported independently. The paper should clarify this explicitly. (This is a presentation issue, not a methodological flaw, since all models were trained on all bases — but the reporting choice matters for interpretability.)

3. **Theorem 2 is a straightforward application of the data processing inequality.** The theorem shows that aggregating a deterministic function of B (i.e., averaging over kNN neighbors) cannot increase mutual information. This is correct but unsurprising, and the paper's framing as a novel theoretical result slightly overstates its contribution. The paper's empirical contributions are far more valuable.

4. **The SOTA-GSL ablation does not separate structure learning loss/regularization from graph structure.** When the paper removes the GSL graph from SOTA methods, it replaces the constructed graph 𝒢' with 𝒢 or MLP layers. However, some GSL methods also have auxiliary losses or regularization terms tied to structure learning. The ablation removes the graph structure but may not fully ablate all related training objectives. This does not invalidate the results but is worth acknowledging.

### Trivial

- "sightly" (line 146) should be "slightly."
- The paper does not explicitly state how many GNN layers are used in the GNN+GSL experiments; this would be helpful for reproducibility but is a minor detail.

## Nice-to-Haves

- A conditional mutual information analysis I(Y; E' | B) on real datasets would further strengthen the claim that GSL edges carry information already present in the bases.
- An explicit re-running of one GSL paper's claimed gains with the authors' fair comparison protocol would be compelling supporting evidence, though the current SOTA-GSL ablation already covers this direction.
- A discussion of whether the findings generalize to deeper GNNs (beyond 2 layers) where over-squashing might matter more.

## Removed Points

- **Selection bias in Table 1 (reviewer's concern about different bases for different methods):** The paper explicitly states "we consider 5 GSL bases as input choices and train all models on each GSL bases" (line 163). All models are compared on the same bases; "best-performing" refers to selecting among these 5 tested bases. The reviewer's concern that MLP and GNN+GSL might be compared on different bases is not supported by the paper's methodology description. Removed (factually incorrect reading).

- **The paper doesn't discuss why GSL papers report strong gains:** The paper does discuss this — it attributes gains to pretrained bases, self-training, and unfair hyperparameter tuning (Section 5.3, line 209). Removed (paper already addresses this).

- **Claim that "GSL is unnecessary" is too strong:** The paper consistently qualifies its claims with "in most cases" / "in most datasets" (abstract, line 230). The SOTA-GSL experiments specifically address optimization-based methods. Removed (strawman — the paper is already properly qualified).

- **Missing conditional MI analysis on real data:** This is a reasonable suggestion but goes beyond the paper's scope; the paper uses synthetic CSBM-H data for MI analysis (where ground truth is available) and accuracy on real data, which is standard practice. Moved to Nice-to-Haves.

- **Number of layers not discussed:** While not explicitly stated in the text for GNN+GSL, the experiments follow OpenGSL defaults which are standard in the literature. This is a minor clarity issue at most. Moved to Trivial.

## Novel Insights

The most novel insight is not theoretical but empirical: the paper demonstrates that the apparent benefits of GSL can be attributed to the quality of the underlying bases and self-training, not to the structure learning itself. The three-step framework provides a clean vocabulary for this decomposition that the community has lacked. The observation that even "successful GSL" (where GSL builds homophilic connections) is unnecessary because the prerequisite — consistent intra-class bases — already guarantees informative representations, is a crisp conceptual contribution that ties the empirical and theoretical threads together.

## Suggestions

1. **Scope the abstract to match the theory.** Replace "no matter which type of graph structure construction methods are used" with something like "for similarity-based/structure-based GSL methods where the graph is a deterministic function of fixed bases" to accurately reflect what Theorem 2 proves.

2. **Clarify the "best-performing GSL bases" reporting.** State explicitly whether Table 1 reports results from the same base for all methods on a given dataset, or each method's individually best base. This takes one sentence.

3. **Add an explicit discussion of the GSL auxiliary losses.** In the SOTA-GSL experiments, briefly note whether the structure-learning-related regularization/loss terms are also removed, and if not, whether their retention could affect the conclusions.

4. **Acknowledge the DPI nature of Theorem 2 more directly.** Rather than presenting it as a novel theoretical result, frame it as "a data-processing-inequality-style argument showing that..." — this would better calibrate reader expectations.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>