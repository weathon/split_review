Now I have a thorough understanding of the paper. Let me produce the consolidated final review.

## Summary

This paper proposes HOGT, a graph transformer architecture that groups graph nodes into communities, introduces a representative "community node" for each, and performs a three-step message-passing strategy (G2C-MP → C2C-ATTN → C2G-MP). This design captures local structure within communities while enabling long-range information propagation via attention among community nodes. The paper also proposes a learnable community sampling method using reinforcement learning. Empirically, HOGT achieves strong results on homophilic, heterophilic, and large-scale graph benchmarks with substantially better efficiency than standard graph transformers.

## Strengths

- **Strong empirical results on heterophilic graphs**: HOGT achieves substantial improvements over prior methods on datasets where global attention typically struggles — e.g., +4.6% absolute over GPRGNN on Wisconsin (95.9% vs. 91.3%), +2.7% on Cornell, +2.8% on Actor (Section 5.1, Table 3). These are meaningful gains on challenging benchmarks.

- **Scalability without sacrificing performance**: On ogbn-proteins and ogbn-products, HOGT achieves state-of-the-art results (85.1% and 80.3%) while being 3.6× more memory-efficient than Polynormer and orders of magnitude faster per epoch than Graphormer and LiteGT (Tables 5, 6). The community-structured design directly addresses the quadratic bottleneck of standard GTs.

- **Structural encoding via communities eliminates need for positional encoding**: Ablation results (Table 4) show that HOGT without positional encoding performs comparably or better than with Laplacian/RWPE, especially on heterophilic datasets (+4.5% on Cornell without PE vs. with lpe). This supports the paper's claim that community structure itself encodes topological information.

- **Broad and systematic evaluation**: Experiments span homophilic graphs, heterophilic graphs, hypergraphs, and large-scale benchmarks, with three community sampling strategies compared and multiple ablations. The coverage is comprehensive for a method paper.

## Weaknesses

### Fatal
None.

### Major

- **The RL-based community sampling is underdescribed and empirically dispensable.** Section 3.1 describes the learnable sampling method in a single paragraph (~7 lines): a projection vector scores nodes, top-k become community centers, and "Q-learning" updates k adaptively. The state space, action space, reward function, training procedure, and how the RL loop interacts with model training are all unspecified. This is insufficient for reproducibility. Moreover, the empirical results (Tables 2, 3) show that random walk sampling performs comparably or sometimes better than the learnable method — e.g., on Citeseer (83.2% learnable vs. 83.2% random walk), on Texas (86.5% vs. 86.8%). The RL component contributes marginal gains at best, yet is listed as a core contribution. Either a complete RL formulation with evidence of benefit is needed, or the claim should be scaled back.

- **The theoretical analysis in the main text is too thin to support the central expressivity claim.** The paper's contribution statement claims to "theoretically show that the three-step message-passing with newly introduced community node can achieve global attention as general transformers do." However, Section 4 only states Proposition 4.1 (citing Cai et al. 2023) and Theorem 4.1 without providing a proof sketch, derivation of approximation bounds, or even a clear mapping of how the three-step process (G2C-MP, C2C-ATTN, C2G-MP) decomposes into the claimed approximation. The main text says "We briefly show how the approximation error can be bounded in Proposition 4.1 and provide the proof of Theorem 4.5" — but no such derivation appears in the main text. While the full proof may exist in the appendix (which is stripped by the parser), the main text should give a convincing intuition sketch. As it stands, a reader cannot evaluate whether the claim holds.

### Minor

- **Baseline hyperparameter tuning is not described.** The paper does not specify how baselines were configured for each dataset — whether hyperparameters were tuned from scratch, taken from published defaults, or optimized using the same protocol as HOGT. Given that performance gaps on some datasets are modest (e.g., ~1–2% on Cora, Citeseer), the lack of clarity on tuning fairness weakens confidence in comparisons.

- **Number of communities (m) per dataset is not reported.** The choice of m directly controls the efficiency-expressiveness trade-off (fewer communities → more compression, less expressivity). The paper only notes that roman-empire and amazon-ratings used a single community with spectral clustering. Without m values for each dataset and sampling method, the results are harder to interpret and reproduce.

- **The p-value claim lacks statistical detail.** The paper states "improvements of HGT over baselines are all statistically significant (p-value ≪ 0.05)" but does not specify which test was used, against which baseline(s), or how multiple comparisons were handled.

- **G2C-MP uses softmax attention (not standard GNN message-passing) — terminology could cause confusion.** Section 3.2's "Message-Passing" steps are in fact attention operations (Equation 2 uses softmax over queries and keys). The term "message-passing" is used broadly throughout the paper, which may mislead readers about how the architecture relates to standard MPNNs.

### Trivial
- The paper mentions "link prediction task on TEG-DB datasets" (Section 5, line 153), but no link prediction results appear in the main text. This dangling reference should be either fulfilled or removed.

## Nice-to-Haves
- An ablation varying the number of communities (m) would help characterize the expressivity-efficiency trade-off.
- Comparison against simpler differentiable sampling alternatives (e.g., Gumbel-softmax) would better isolate the value of the RL approach.
- An analysis of community quality (e.g., internal edge density, label homogeneity) could provide insight into when the method works best.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The sentence about communities substituting for positional encoding conflates two types of information."* — This is a stylistic/subjective complaint. The paper provides empirical evidence (Table 4) supporting the claim, so the criticism is not substantive.

2. *"Link prediction results are missing."* — The paper mentions link prediction experiments; results may appear in the appendix (which is stripped by the parser). Per instructions, missing appendix content is not a valid criticism.

3. *"The paper does not ablate the neighbor component in C2G-MP separately."* — The paper does include this information in the design (Equation 5 combines community and neighbor information), and the C2G-MP description explains the design rationale. This is a deeper ablation that would be nice but is not a weakness.

4. *"Requesting more models/datasets/broader scope"* — The paper's evaluation is already broad (homophilic, heterophilic, hypergraph, large-scale). Demands for further breadth constitute scope creep.

## Novel Insights

The core insight — that structuring graphs into communities with dedicated community nodes and a three-step message-passing scheme (G2C → C2C attention → C2G) can simultaneously capture local structure, high-order correlations, and long-range dependencies while avoiding quadratic complexity — is genuinely useful. The connection to hypergraph structure (community nodes acting like hyperedges) and the empirical demonstration that community structure can substitute for positional encoding are interesting findings. However, the most ambitious claim (approximating global attention) is not sufficiently developed in the main text to be evaluated as a novel theoretical insight.

## Suggestions

1. **Rein in or flesh out the RL contribution.** Either (a) provide a complete description of the RL formulation (state space, actions, reward, training procedure) with evidence that the adaptive k yields meaningful improvements, or (b) remove the RL claim and adopt a simpler fixed or random sampling strategy as the primary method, treating the RL variant as a secondary extension.

2. **Add a clear theoretical sketch to Section 4.** Even a one-paragraph intuition of how the three-step process decomposes — e.g., how G2C-MP computes local statistics, C2C-ATTN propagates them globally, and C2G-MP distributes them back — and how this collectively approximates a full attention matrix, would substantially strengthen the paper. State the dependence of the approximation error on the number of communities.

3. **Report m (number of communities) per dataset and sampling method** in the main tables or a supplementary table.

4. **Clarify baseline tuning protocol** — state for each baseline whether hyperparameters were tuned, and if so, the search space and procedure.

## Score and Decision

The paper presents a well-motivated architecture with strong empirical results across diverse benchmarks and clear efficiency advantages. The core idea — community-structured message-passing with dedicated community nodes — is sound and practically useful. However, the paper overclaims in two ways: (a) the RL-based community sampling is presented as a contribution but is underdescribed and empirically marginal, and (b) the theoretical expressivity analysis is too sketchy in the main text to support the central "unifying MP and GTs" claim. These issues are addressable with revisions (scaling back claims, adding clarity) and do not invalidate the core empirical contributions. I recommend acceptance with major revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>