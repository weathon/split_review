Now I have all the information I need. Let me write the consolidated final review.

## Summary

This paper formalizes the Sparse Labels Node Classification (SLNC) problem, where only very few labels are available and they are selected randomly (not per-class). The authors propose ELI (Estimating Label Information), a framework that: (1) performs unsupervised clustering (AGC) on the full graph to obtain pseudo-labels, (2) selects "key nodes" from the pseudo-classes to serve as labeled nodes, and (3) incorporates the pseudo-label distribution into a Laplacian regularizer by averaging three graph Laplacians (graph structure, pseudo-label graph, and label graph). Results show 10–20% absolute accuracy gains over LP, SGC, DGI, GMI, and CGPN on 7 benchmark datasets under extreme label sparsity.

## Strengths

1. **Well-motivated problem definition (SLNC)**. The paper identifies a gap in existing semi-supervised node classification research: most methods assume per-class label selection or abundant base-class labels, neither of which reflects realistic settings where labels are scarce and randomly distributed. Definition 3.1 cleanly formalizes this scenario.

2. **Consistent and large accuracy gains under extreme sparsity**. Tables 3 and 4 show that ELI-enhanced methods outperform all baselines by 10–20% absolute on 7 datasets when only 1 labeled node per class-equivalent is available. For example, on Cora with l=c=7 labels, LP gets 41.47% while LP-ELI gets 69.72%; on Photo, GMI gets 32.41% while SGC-ELI gets 80.97%. These gains persist across the 1–4 label range.

3. **Framework generalizes to both label propagation and graph convolution**. Section 4.5 shows that the averaged Laplacian can replace the standard graph Laplacian in SGC's convolution operator, producing SGC-ELI which often further improves over LP-ELI (e.g., Cs with 2 labels: SGC-ELI 82.62% vs LP-ELI 75.43%).

4. **Computational efficiency consideration**. The paper identifies that the dense pseudo-label graph from HH^T is impractical and proposes a KNN-on-SVD sparsification (Section 4.4), reducing runtime substantially compared to the CGPN baseline.

## Weaknesses

### Major

1. **Zero standard deviation in the #1 condition is unexplained and undermines reader trust**. In Tables 3 and 4, every ELI method reports 0.00 standard deviation for the #1 column across all 7 datasets (e.g., Cora LP-ELI: 69.72 ± 0.00). The paper states experiments are run 10 times with random label selection. While the zero std is *explainable* — for #1 (l=c), the key node selection (Section 4.2) selects exactly one node per pseudo-class deterministically via smallest-loss, and the LP-ELI solution (Eq. 4) is closed-form, so the labeled set is the same across all runs — the paper never provides this explanation. Typical readers would (reasonably) see ±0.00 as either a mistake or a sign of fixed seeds. The paper must explicitly state that the key node selection makes the #1 labeled set deterministic and that the zero variance is therefore expected, not an error. This is a transparency failure in the current presentation.

2. **The key node selection heuristic is underspecified and its effect is not isolated from the Laplacian regularization**. Section 4.2 states that "l_H nodes were chosen" per pseudo-class with smallest loss, but never specifies what l_H is, how it relates to the total label budget l, or whether l_H is fixed across experiments. For #1 (l=c), the natural reading is l_H = 1 per pseudo-class and l_R = 0, but this is not stated. For higher label budgets (l=2c, 3c, 4c), it is unclear whether l_H grows or stays fixed. Moreover, the method combines two mechanisms — key node selection (deterministic, informative labeled nodes) and pseudo-label graph Laplacian (regularization from clustering) — without any ablation to attribute the gains to either component. A simple ablation (key node selection alone vs. Laplacian regularization alone) is essential.

3. **No evaluation on heterophilic graphs**. The method fundamentally relies on the smoothness (homophily) assumption through its Laplacian regularization. All 7 datasets tested are homophilic (Cora, Citeseer, Pubmed, Wiki, Computers, Photo, Cs). The paper should test at least one heterophilic benchmark (Texas, Wisconsin, Cornell, Chameleon, Squirrel) to demonstrate the scope and limits of the approach.

### Minor

1. **Equal weight averaging (β₁=β₂=β₃=1/3) is unsubstantiated**. The paper sets all three Laplacian weights to 1/3 "to simplify" (Section 4.3) without any sensitivity analysis or justification. Since the three Laplacians encode very different information (graph structure, noisy pseudo-labels, sparse true labels), equal weighting is not obviously optimal. A simple grid search over weights or a comparison to tuned weights would substantially strengthen the paper.

2. **Missing comparison to the clustering baseline itself**. The paper uses AGC clustering to produce pseudo-labels but never reports the clustering accuracy (i.e., the accuracy of assigning each node its cluster's majority class). This would clarify how much of the final gain comes from the clustering step alone versus the combined framework.

3. **Several baselines from the sparse-label graph literature are omitted**. The paper compares against LP, SGC, DGI, GMI, and CGPN, but does not include APPNP (Gasteiger et al., 2019) or GRAND (Feng et al., 2020), which are standard methods for label propagation on graphs with sparse supervision. Including APPNP would be a relatively straightforward addition.

4. **CGPN results are incomplete**. CGPN is marked as "-" on 4 of 7 datasets (Pubmed, Cs, Photo, Computers) with only a qualitative explanation ("it took too long"). This weakens the baseline comparison; the authors should either report partial results or drop CGPN from the main tables.

5. **No reporting of class coverage or missing-class frequency**. For #1 (l=c) with random selection, each class has only a c^(-c) probability of all being represented. The paper does not report how often classes are actually missing from the training set across the 10 runs, making it hard to assess the difficulty of the setting.

### Trivial

- The figure caption for Figure 1 appears three times in the text (lines 57–63), a formatting duplication.
- In Table 4, the variant "SCG-ELI" appears in the row label but should be "SGC-ELI" for consistency with the text and Table 3.
- The notation in Eq. (2): "𝒲(L_sym)" and "𝒦(L_𝒢_H)" are used without being explicitly defined as functions.

## Nice-to-Haves

- Sensitivity analysis for the KNN graph size (currently fixed at 60) with a few alternative values (20, 40, 80).
- An inductive variant where clustering is performed only on the training+validation set, to isolate the effect of using test-set features in the label estimation step.
- Analysis of how the gain from ELI changes as the number of labels grows beyond 4 (the appendix is stripped, so this may already exist).

## Removed Points

- **"Zero standard deviation is fatal/evidential flaw"** — Removed as framed. The zero std is actually explainable (deterministic key node selection + closed-form solution), not a fatal error. It is retained as a Major weakness but for the correct reason (lack of transparency).
- **"Method is inherently transductive and uses test-set information"** — Removed. The paper frames this as transductive semi-supervised learning, which is standard for graph node classification. Clustering on all nodes is no different in spirit from using the full adjacency matrix in message passing.
- **"Missing RECT baseline"** — Removed. The reviewer does not provide sufficient evidence that RECT is a relevant baseline for this specific setting. The existing baseline set (LP, SGC, DGI, GMI, CGPN) covers several methodological families.
- **"AGC choice not justified"** — Removed. The paper cites Kamhoua et al. (2022) which provides state-of-the-art clustering accuracy; this is sufficient justification for a design choice in a method-focused paper.
- **"Formatting/typo nitpicks"** — Removed per instructions (parser artifacts).
- **Generic strengths from Strength Finder (e.g., "comprehensive evaluation", "addressing computational cost")** — Moved here because they overstate the evidence slightly, but retained implicitly in the actual evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same issues the paper presents but do not uncover a fundamentally new understanding of the method or its behavior.

## Suggestions

1. **Clarify the zero-std issue explicitly in Section 4.2 or 5.2**: Add a sentence explaining that when l=c (the #1 condition), all labels are selected via the deterministic key node heuristic, so the labeled set is identical across runs, making the zero variance expected. This single change would eliminate the most serious concern reviewers will have.
2. **Add an ablation study** that separates (a) key node selection only (with random labels + standard LP) from (b) pseudo-label Laplacian only (with random labels + Eq. 2 without key selection) from (c) the full ELI. This would cleanly attribute the 10–20% gains.
3. **Specify l_H explicitly**: State clearly that for #1, l_H = 1 per pseudo-class (total = c), and discuss whether l_H grows with the label budget.
4. **Add at least one heterophilic benchmark** (e.g., Texas or Chameleon) to probe the scope of the homophily assumption.
5. **Include APPNP as a baseline** — it is a natural label-propagation-based method for sparse supervision and would make the comparison stronger.

## Score and Decision

**Initial bracket (Round 1):** Between 4.0 and 6.0. The lower bound is set by papers with limited datasets/poor writing (~3.0). The upper bound is set by well-executed, accepted papers (~8.0). Our paper is stronger than the 3.0-level papers but has significant presentation gaps compared to accepted papers.

**Round 2 narrowing:**
- Against *Semi-Supervised Clustering for Graph Learning* (avg 4.4, reject): Our paper has more datasets (7 vs 3), more baselines, and clearer problem framing. Slightly stronger. → paper is above 4.4.
- Against *KDGCN* (avg 5.25, reject with mixed 3,8,5,5): KDGCN had one very positive review and moderate weaknesses. Our paper's zero-std issue and underspecified method are more concerning. → paper is below 5.25.
- Against *Scale-Free GLM* (avg 5.75, accept poster): That paper is well-written with comprehensive ablations, a clearly stronger presentation. → paper is well below 5.75.

This places the paper at **4.5**. It has a genuine contribution (SLNC problem definition and the ELI framework showing large gains), but the presentation is rough in ways that would cause reviewers to question the results, and several standard methodological practices (ablation, justification of hyperparameters, baseline coverage) are missing. A thorough revision addressing these gaps could raise this to 5–6.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>