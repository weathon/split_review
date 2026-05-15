I now have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

The paper proposes FedStruct, a subgraph federated learning framework that decouples node features from graph structure. Unlike prior methods that share node features or embeddings across clients, FedStruct shares only structural information (the local partition of a combined L-hop adjacency matrix and node structure features). It incorporates a decoupled GCN to enable local training without sharing intermediate embeddings, and introduces Hop2Vec, a method to learn task-dependent node structure embeddings via gradient descent. Experiments on six datasets show FedStruct (especially with Hop2Vec) achieves near-centralized accuracy and substantially outperforms FedSage+ and FedSGD baselines, particularly on heterophilic graphs like Chameleon.

## Strengths

- **Novel decoupling of structure from features in subgraph FL.** FedStruct is the first subgraph FL framework that explicitly avoids sharing node features or feature embeddings by relying solely on structural information. Propositions 1–3 (Section 5.2) formally show that training requires only the local partition of the combined adjacency matrix $\boldsymbol{\Bar{A}}^{[i]}$ and the structure matrix $\bS$, providing a principled foundation for this design.

- **Near-centralized accuracy on multiple benchmarks.** On six datasets with random partitioning and a challenging 10%/10%/80% train/val/test split, FedStruct with Hop2Vec achieves accuracy within 1–3% of the centralized GNN while far exceeding realistic baselines. For example, on Cora (10 clients): 80.28% vs central 82.06% vs FedSage+ 66.32%; on Chameleon (10 clients): 52.36% vs central 54.43% vs FedSage+ 35.48% (Table 1). These results demonstrate that structural information alone can recover most of the performance that previously required feature sharing.

- **Task-dependent structure embeddings (Hop2Vec).** Unlike task-agnostic structural features (degree, GDV, Node2Vec, FedStar), Hop2Vec learns node structure features end-to-end via gradient descent without requiring global graph knowledge. The consistent outperformance of FedStruct(H2V) over FedStruct(Deg) and FedStruct(FedStar) across all datasets and client counts validates the advantage of task-adaptivity.

- **Robustness to increasing clients and different partitionings.** FedStruct(H2V) shows minimal degradation as clients increase from 5→10→20 (e.g., Cora: 79.53%→80.28%→79.39%), while baselines drop more sharply. The paper also demonstrates robustness across random, Louvain, and K-means partitionings in the appendix.

- **Lower online communication than FedSage+.** FedStruct's online communication is O(E·K·|θ|) per round (vs FedSage+'s O(E·K²·|θ| + E·K·n·d)). A pruning variant reduces offline complexity from O(L·n²) to O(L·p·n) with only slight accuracy drops.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Privacy claims are qualified but lack rigorous analysis in the main paper.** The paper claims that structural information is "often less sensitive" (line 88) and that FedStruct shares "less sensitive information" (line 577), and it references a privacy discussion in the appendix (App.~\ref{app:privacy}). However, the main text does not adequately address that (1) graph structure itself can be sensitive in many applications (e.g., transaction networks, supply chains), and (2) the Hop2Vec variant shares learned node-specific parameters ($\bs_u$) across clients, which is a form of embedding sharing — albeit of structural rather than feature information. The paper's core narrative would benefit from more precise scoping of what privacy guarantee is actually provided versus what is merely different from existing methods. This does not invalidate the contribution but tempers the claimed privacy advantage.

- **Missing comparison with FedCog.** FedCog (Lei et al., 2023) is discussed in related work as also using decoupling in subgraph FL, and is the most directly comparable prior art. Its absence from the experimental comparison is a gap. The paper does compare against FedSage+ and FedPub, but adding FedCog would strengthen the evaluation.

- **The heterophily claim is modestly over-extended.** The paper states "FedStruct is the first subgraph FL framework capable of handling heterophilic graphs" (line 102). Results on Chameleon (edge homophily < 0.3) and Amazon Ratings (~0.4) support this, and the decoupled GCN's inter-layer combination is a known technique for heterophily. However, there is no ablation isolating the effect of the learnable $\beta_l$ coefficients on heterophily handling, no controlled experiment varying homophily levels, and no systematic comparison showing FedStruct handles heterophily better than alternatives that could be adapted to heterophilic GNNs. The claim is directionally correct but the evidence is thinner than the statement suggests.

- **FedStruct uses gradient averaging (FedSGD) rather than FedAvg.** The paper formalizes training via gradient averaging at the server (Section 4.2), which incurs higher communication than FedAvg. This is a design choice, not an error, but the paper does not discuss why FedAvg is not used or whether FedStruct is compatible with it. The appendix references "federated averaging" results, so some investigation exists, but the main text is silent on the rationale.

### Trivial

- **Fig. 1 (motivation):** The "structure only" baseline is not explicitly identified in the caption or text. It is presumably a model using only structural features with no node features, but this should be stated.  
- **Line 491:** "For the GNN, we rely on GraphSAGE" is ambiguous — it could be read as applying to FedStruct's internal fGNN (which the formalism defines as a decoupled GCN). The paper later notes that decoupled GCN performs similarly (appendix reference), but the presentation could be clearer.

## Nice-to-Haves

- A formal privacy analysis (e.g., discussion of differential privacy, or an argument about why structure is less sensitive than features in specific domains like anti-money laundering) would substantially strengthen the paper's core claim.  
- An ablation or analysis of the learned $\beta_l$ coefficients on heterophilic vs. homophilic datasets would substantiate the heterophily claim.  
- Comparison with FedCog and actual FedNI (not just the upper bound) would address completeness concerns.  
- Reporting statistical significance tests (e.g., confidence intervals beyond std deviation) for key comparisons would strengthen the empirical claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that the offline computation of $\boldsymbol{\Bar{A}}^{[i]}$ is missing from the paper.** The paper states it is in App.~\ref{app:schemes}. The parser strips appendix content from all papers. This exists in the original submission.  
- **Claim that "fedsage+ ideal" is cherry-picked for narrative effect.** The paper transparently describes it as an upper bound on FedSage+/FedNI that is "not feasible in practice" (line 495). Both realistic and ideal baselines are reported side-by-side.  
- **Claim that the paper does not acknowledge Hop2Vec shares learned parameters.** The communication complexity table (Table 2) explicitly lists the online cost of Hop2Vec as O(E·K·n·d), acknowledging that the learned NSFs are shared. The paper's claim is about not sharing *node features* or *feature embeddings* — structural embeddings are a different category, and the paper consistently refers to "less sensitive" structural information, not "no information."  
- **Claim that the privacy motivation "invalidates the paper's core narrative."** The paper's core contribution is decoupling structure from features in subgraph FL, enabling training without sharing node features. The privacy advantage is relative to existing methods (which share features/embeddings), not absolute. The paper qualifies its claims with "often less sensitive" and references an appendix privacy discussion.  
- **Nitpick about the Figure 1 "structure only" baseline not being identified** — kept in Trivial but softened.  
- **Complaint about gradient formulas being "not novel"** — these are provided for completeness, not claimed as novel contributions.  
- **Complaint about the 10/10/80 split being "highly unbalanced"** — the paper explicitly describes this as "strongly semi-supervised" and appropriate for the scenario; the split is a deliberate design choice.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Scope the privacy claim more precisely in the main paper.** Acknowledge explicitly: (a) that graph structure can be sensitive in some applications, and (b) that Hop2Vec shares learned structural parameters (though not node features). Move a brief privacy discussion into the main text rather than deferring entirely to the appendix.  
2. **Add FedCog as a baseline** and, if possible, the actual (non-idealized) FedNI.  
3. **Include an ablation on $\beta_l$ coefficients** to demonstrate how the decoupled GCN handles heterophily, or at minimum report learned $\beta$ values.  
4. **Clarify why gradient averaging (FedSGD) is used over FedAvg** and whether FedStruct is compatible with FedAvg. If the appendix already has FedAvg results, mention them in the main text.  
5. **Define the "structure only" baseline in Figure 1** explicitly.  
6. **Add a sentence clarifying the GNN architecture choices** — what uses GraphSAGE vs. decoupled GCN — to avoid ambiguity for readers.

## Score and Decision

The paper introduces a genuinely novel approach to subgraph FL with strong empirical results and a well-motivated design. It has real but fixable weaknesses: the privacy framing could be more precise, one missing baseline (FedCog), and the heterophily claim mildly over-extends the evidence. No fatal flaws. The paper would benefit from the suggested revisions but makes a clear contribution as-is.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>