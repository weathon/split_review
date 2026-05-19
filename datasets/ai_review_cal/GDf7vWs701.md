- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 1, 5, 3
I have all the information I need. Let me now produce the final consolidated review.

## Summary

The paper proposes ProdInfluencerNet (PIN), a product-centric influencer recommendation framework that models brands, influencers, and product categories as a heterogeneous information network (HIN). Sponsored post images are classified into Google Taxonomy categories to create product-category nodes, and inductive GraphSAGE is used to handle unseen nodes. The framework is evaluated on two Instagram datasets (I&B and a proprietary iKala dataset) and compared against GNN-IR.

## Strengths

1. **Product-centric HIN framework with hierarchical taxonomy**: The network schema linking brands, influencers, and product categories (Figure 2b, Section 3.1) is a well-motivated design that enables information sharing across brands offering the same product category, directly addressing the cold-start problem the paper targets.

2. **Inductive learning for unseen nodes**: The paper explicitly adopts GraphSAGE with inductive learning and demonstrates through experiments (Tables 1, 3; Section 4.3) that the model maintains high accuracy when product category nodes in the test set were unseen during training. This is a clear and meaningful operationalization of the cold-start motivation.

3. **Empirical finding that text features dominate images for product-influencer matching**: Across both datasets, $\mathrm{PIN}_{\text{text}}$ consistently outperforms $\mathrm{PIN}_{\text{multi}}$ and $\mathrm{PIN}_{\text{image}}$ in link prediction (Tables 1, 3; Section 4.3). This finding contrasts with prior work emphasizing visual style and provides practical guidance for framework deployment.

4. **Validation on two large-scale real-world Instagram datasets**: The framework is tested on the I&B dataset (70k+ posts, 3k+ influencers) and a proprietary iKala dataset (83k+ brand-product edges, 104k+ influencer-product edges), demonstrating robustness across different data sources (Section 4.1).

## Weaknesses

### Fatal
None.

### Major

1. **GNN-IR comparison is uncontrolled, undermining the claimed superiority.** The paper states "To facilitate a direct comparison with GNN-IR (Park et al., 2024), we aligned our metrics with theirs" (Section 4.2) but never specifies whether GNN-IR was re-run under identical conditions (same data splits, same filtered subset of the I&B dataset, same evaluation protocol). The GNN-IR results in Tables 1 and 2 appear to be single numbers taken from or reproduced from the original paper without evidence of controlled re-implementation. Since the paper's central claim is that PIN "demonstrates a significant improvement over previous work" (Section 4.3), this comparison must be controlled. The magnitude of the reported gap (F1 ~0.7 vs. ~0.2 for recommendation) itself raises suspicion that the evaluation protocols differ fundamentally.

2. **Product category classification pipeline is underspecified.** The entire framework depends on mapping sponsored post images to Google Taxonomy categories (the core mechanism that produces product-category nodes from which the graph is constructed), yet the paper never describes the classification model, its training data, its accuracy, or even which level of the taxonomy is used. Section 3.2.2 ("Google Taxonomy Class") merely shows examples of fine-grained eye-makeup categories with no methodological detail. The abstract mentions "image classification techniques" generically. Without this information the method cannot be reproduced, and the reader cannot assess how classification errors propagate to downstream tasks. This is a central methodological gap for a method paper.

3. **Recommendation evaluation protocol is not defined.** The paper evaluates recommendation using Precision@K, Recall@K, and F1-score@K (Tables 2, 4) but states only "We leveraged the link probabilities obtained from the previous part to generate recommendations" (Section 4.2). It does not specify: (a) how link probabilities are converted to an influencer ranking for a brand, (b) which edges constitute ground truth for the recommendation task, or (c) whether evaluation is performed on a held-out set of (brand, influencer) pairs. The meaning of the reported numbers is therefore ambiguous.

4. **Cold-start claim is asserted but not experimentally validated.** The paper repeatedly motivates the work with cold-start scenarios (new products, new markets, unfamiliar categories) and presents inductive learning as the solution. Yet no controlled cold-start experiment is conducted. The claim that "the product category nodes in the testing phase include nodes that were not seen during training" (Section 4.3) is stated but not demonstrated with a comparison to a transductive baseline that would be blocked on those nodes. A proper evaluation would hold out a set of product categories from training entirely and measure performance specifically on those held-out nodes.

### Minor

1. **Source of feature embeddings is not specified.** The paper reports dimension counts (512-d text embeddings, 640-d image embeddings, etc. — Section 4.1) but does not identify which pre-trained models produced these embeddings (e.g., which text encoder, which vision model). This is critical for reproducibility.

2. **Notation inconsistency in Section 3.2.** The sets for brands ($B$), influencers ($K$), and products ($P$) are all indexed with $m$ (line 65), even though they are later corrected to distinct variables $m, n, i$ on line 73. This is a minor presentation issue but causes confusion.

3. **No statistical variance or confidence intervals reported.** All results appear as single numbers with no indication of variance across runs or splits. Given potential randomness in splits and negative sampling, this limits the reader's ability to assess result reliability.

4. **The product category feature dimensionality "11" is unexplained.** Section 4.1 states "product category (11 dimensions)" but never clarifies what these 11 dimensions represent (one-hot encoding of taxonomy level? a learned embedding?).

5. **Text-only outperforming multimodal is discussed but not analyzed.** The paper notes that $\mathrm{PIN}_{\text{text}}$ outperforms $\mathrm{PIN}_{\text{multi}}$ (Section 4.3) but does not investigate why the fusion strategy degrades performance — this could indicate a poor fusion design rather than that images are genuinely unhelpful.

### Trivial

- The variable notation in Section 3.2 uses $m$ for the cardinality of all three sets ($B$, $K$, $P$) before later introducing distinct counts $m, n, i$ in the same section (lines 65, 73).

## Nice-to-Haves

- An ablation experiment removing the graph structure entirely (e.g., replacing it with logistic regression on node features) would directly quantify the benefit of the HIN.
- Analysis at different levels of the Google Taxonomy hierarchy would be directly relevant to the cold-start narrative (since new products may only be classifiable at higher levels).
- A description of the train/validation/test split mechanism (edge-level vs. node-level) would help interpret the inductive learning experiments.

## Removed Points

- **"The iKala dataset is not publicly available"** — The paper transparently states it is a proprietary dataset from a corporate partner (Section 4.1). This is not a weakness of the paper.
- **"Missing related works"** — Not verifiable without external sources; excluded per instructions.
- **"Formatting/style nitpicks" and "typos"** (e.g., "lunching" → "launching") — These are parser artifacts or trivial and excluded per instructions.
- **"The evaluation lacks rigor" / "Could the metric be measuring a proxy?"** — These are generic concern-sweeps without specific anchors in the paper; excluded.
- **Strength Finder claim: "Detailed data pipeline for product category extraction"** — This is inaccurate; the pipeline is not detailed. The classification method is a black box. Removed.
- **Strength Finder's generic strengths about "addressing an important problem"** — Removed as generic/superficial.

## Novel Insights

Both reviews converge on the same structural gaps: the GNN-IR comparison is not demonstrably controlled, the product classification mechanism is a black box, and the recommendation evaluation protocol is underspecified. Interestingly, the harsh critic's concern about the cold-start validation and the strength finder's emphasis on the inductive learning results point to the same issue — the paper makes a plausible cold-start case but never delivers the definitive controlled experiment that would seal it. The paper's core idea (product categories as a bridge in an inductive HIN) is sound and the within-method results (text vs. image) are valuable, but the external comparison and methodological specification are too weak to support the paper's stronger claims.

## Suggestions

1. **Re-run GNN-IR under identical conditions** (same data splits, same node features, same filtering criteria, same evaluation code) and report the exact configuration. If this is infeasible, clearly state that the GNN-IR numbers are taken from the original paper and explain the protocol differences.

2. **Specify the product category classification pipeline in full**: model architecture, training data, source of supervision, accuracy on a held-out sample, and the chosen taxonomy level. If a third-party API is used, name it and report its accuracy on your data.

3. **Define the recommendation evaluation protocol precisely**: describe how link probabilities produce a ranked influencer list for a brand, specify what ground-truth edges are used, and include a worked example.

4. **Design a dedicated cold-start experiment**: hold out a set of product categories from training entirely and report link prediction and recommendation performance on those held-out nodes, with a transductive baseline for comparison.
