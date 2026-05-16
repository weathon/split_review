Now I have a thorough understanding of the paper and can carefully cross-check each claim. Let me produce the consolidated review.

## Summary

This paper presents FedStruct, a subgraph federated learning framework that decouples graph structure from node features. Unlike prior subgraph FL methods that share node features or embeddings across clients, FedStruct shares explicit global structural information (via an L-hop combined adjacency matrix) to capture inter-node dependencies, while keeping node features strictly local. The paper also proposes Hop2Vec, a method to learn task-dependent node structure embeddings (NSFs) through gradient descent. Experiments on six datasets (Cora, Citeseer, Pubmed, Chameleon, Amazon Photo, Amazon Ratings) show that FedStruct with Hop2Vec achieves accuracy close to centralized GNNs and significantly outperforms baselines like FedSage+ and FedPub, particularly on heterophilic graphs.

## Strengths

1. **First subgraph FL framework to avoid sharing node features or feature embeddings.** All prior subgraph FL methods (FedSage+, FedNI, FedCog, etc.) require sharing or generating node features or feature-based embeddings. FedStruct instead shares structural information (the combined adjacency matrix) and structure embeddings, which are genuinely different in kind from node feature information. This design choice is principled and well-motivated. (Abstract, lines 86-88, Section 5)

2. **Hop2Vec provides a novel way to learn task-dependent structure embeddings without global graph knowledge.** Unlike Node2Vec or GDV, which require global graph access and are task-agnostic, Hop2Vec treats NSFs as learnable parameters optimized on the classification loss. It captures multi-hop structural dependencies without needing the full L-hop neighborhood upfront. In Table 1, FedStruct with Hop2Vec consistently outperforms variants using hand-crafted NSFs (Degree, FedStar) across all datasets (e.g., Cora 10 clients: 80.28% vs 68.64% Degree, 68.87% FedStar). (Section 5.3, Table 1)

3. **Strong performance on heterophilic graphs, where prior subgraph FL methods fail.** On Chameleon (edge homophily ratio ~0.23) with 20 clients, FedStruct (H2V) achieves 52.76% vs 34.33% for FedSage+ and 34.72% for FedSGD GNN — a gap of over 18 percentage points. This is because existing methods rely on homophily assumptions, while FedStruct's decoupled GCN with adjustable hop coefficients handles heterophily. The paper is the first subgraph FL framework demonstrated to handle heterophilic graphs. (Table 1, lines 101-102, Appendix discussion)

4. **Performance close to centralized training.** FedStruct (H2V) achieves accuracy within 2-4% of the centralized GNN across multiple datasets and client splits — e.g., Cora 5 clients: 79.53% vs central 82.06%; Amazon Photo 10 clients: 91.83% vs 93.99%; Pubmed 10 clients: 86.65% vs 87.71%. This is the closest any privacy-preserving subgraph FL method has come to centralized performance. (Table 1)

5. **Theoretical grounding for local training.** Propositions 1-3 formally derive that clients only need their local row partition of the combined adjacency matrix to compute predictions and gradients, justifying the decoupled architecture. (Section 5.2, Appendix proofs)

## Weaknesses

### Fatal
None.

### Major

1. **The Hop2Vec variant shares learned node-level vectors, which blurs the paper's central privacy claim.** While the paper correctly distinguishes between *node feature embeddings* (NFEs, not shared) and *node structure embeddings* (NSEs/NSFs, shared), the abstract's phrasing "eliminates the necessity of sharing or generating sensitive node features or **embeddings** among clients" (emphasis added) is imprecise. Hop2Vec's NSFs are learned node-level vectors shared globally at every round (online complexity O(E·K·n·d) — Table 2, col. 2). This is *a form of node embedding sharing*. The paper should explicitly qualify that it eliminates sharing of *feature-derived* embeddings but introduces sharing of learned *structure* embeddings, and should provide a clearer privacy analysis comparing what an adversary could infer from NSFs vs. from feature embeddings. The graph-isomorphism argument (line 383-385) is not sufficient on its own, and the deferred privacy appendix (line 577) does not appear in the main paper. The core contribution — a genuine and useful decoupling of features from structure — is strong and defensible, but the framing oversells the "no embedding sharing" aspect for the Hop2Vec variant.

### Minor

1. **Missing experimental comparison to FedCog.** FedCog (Lei et al., 2023) is discussed in related work (line 121) and also decouples internal/border graphs. Since FedCog shares intermediate embeddings (which the paper rightly flags as privacy-invasive), a direct comparison would help quantify the privacy-performance trade-off: how much accuracy does one sacrifice by refusing to share feature-informed embeddings vs. sharing only structural information? The paper's claim of being the "first subgraph FL framework capable of handling heterophilic graphs" would also be strengthened by showing that FedCog (which does not claim heterophily-handling) cannot match FedStruct on Chameleon. Including FedCog as a baseline is feasible since it uses the same cross-subgraph knowledge assumption.

2. **No ablation isolating the sGNN's contribution from NSF quality.** For fixed NSFs (Degree, FedStar), the paper uses an sGNN to transform NSFs into NSEs. For Hop2Vec, the sGNN parameters are absorbed into the learnable NSFs (line 411-412), effectively removing the sGNN. This makes it unclear whether Hop2Vec's advantage comes from (a) better NSFs, (b) removal of sGNN constraints, or (c) both. An ablation comparing FedStruct(Deg) with and without the sGNN, and Hop2Vec with the sGNN retained as a separate module, would isolate these effects.

3. **Offline O(L_s·n²) complexity is a practical concern for large graphs.** The paper acknowledges this (lines 447-449) and proposes pruning, but the offline computation of matrix powers for graphs with millions of nodes could be prohibitive. The pruning evaluation (p=30) is only shown for one setting, and the sensitivity of accuracy to p is not analyzed. While this does not invalidate the paper's contributions, a more thorough discussion of when the offline phase becomes intractable and whether approximate methods (e.g., power iteration with early stopping) could help would strengthen the practical applicability.

4. **FedStruct (Deg/FedStar) underperforms FedSGD GNN and FedSage+ on Pubmed.** On Pubmed with 5 clients, FedStruct(Deg) achieves 84.92% vs FedSGD GNN 86.14% and FedSage+ 85.89%. This suggests that fixed NSFs alone can sometimes hurt more than they help when local GNNs already capture sufficient structure. The paper should briefly discuss why structure information is less beneficial on Pubmed (a relatively homophilic graph with strong feature signals).

### Trivial

1. **Figure 1 legend entries ("features", "structure only", "Fed SGD") are not explained in the caption.** The caption says "GNN node classification accuracy from exploiting different sources of information" but does not define what each bar represents, making the figure hard to interpret in isolation.

2. **Table 2 uses different notation for the same quantities across rows** (e.g., "FedStruct pruning" vs "FedStruct + Hop2Vec") without a consistent naming pattern, slightly complicating comparison.

## Nice-to-Haves

- A sensitivity analysis for the pruning parameter p (accuracy vs. p for at least one dataset) to show the trade-off curve.
- Results for denser label settings (e.g., 60/20/20 split) to complement the challenging 10/10/80 split.
- A discussion of secure multi-party computation or differential privacy mechanisms that could further protect the shared structural information.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No privacy analysis"**: The paper references a privacy discussion in App.~\ref{app:privacy} (line 577). Per the parser-stripping rule, this content exists in the original submission and cannot be faulted as absent.
- **"Claim about 'no work has leveraged explicit structural information in subgraph FL' is wrong because of FedStar"**: The paper accurately distinguishes FedStar (graph-level FL, line 130) from subgraph FL. The claim is correct.
- **"Strong assumption that clients know external neighbors"**: This is standard in subgraph FL (FedCog makes the same assumption, as noted line 121). The paper explicitly states this scenario assumption.
- **"H2V beating FedSage+ ideal on heterophilic graphs is anomalous and unexplained"**: The paper explains this via the homophily assumption of FedSage+ vs. FedStruct's heterophily-handling capability (line 101, line 115). This is a strength, not a weakness.
- **"Offline complexity is not discussed"**: The paper discusses it in lines 447-451 and proposes pruning. The critic's claim that it "deserves attention in the main text" is addressed.
- **Formatting nitpicks and figure style complaints**: Per hard rules, parser artifacts and pure formatting issues are not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension in the paper's framing: the Hop2Vec variant indeed shares learned node-level vectors, which the abstract's blanket "no embedding sharing" claim oversimplifies. This is a useful precision check but does not invalidate the paper's core insight — that structural decoupling is a promising alternative to feature sharing in subgraph FL.

## Suggestions

- **Revise the abstract and contribution claims to be precise**: Replace "eliminates the necessity of sharing ... embeddings" with "eliminates the necessity of sharing *node feature* embeddings; the Hop2Vec variant shares learned structure embeddings, which capture topological rather than feature information." This honesty would actually strengthen the paper by preempting the most obvious line of criticism.
- **Add FedCog as a baseline** in experiments (or provide a clear argument for incomparability beyond privacy). Even one dataset would help substantiate the "first to handle heterophily" claim.
- **Add an sGNN ablation** comparing FedStruct(Deg) ± sGNN to quantify the sGNN's contribution beyond NSF quality.
- **Move the privacy discussion from the appendix to the main paper**, or at minimum add a 1-2 paragraph summary in the main text addressing what structural information reveals and what it does not.

## Score and Decision

The paper presents a technically sound framework with clear empirical advantages on heterophilic graphs. The core weakness is a framing imprecision rather than a methodological flaw: the paper's claim of eliminating embedding sharing is true for feature embeddings but not for the structure embeddings shared by Hop2Vec. This is fixable with a more precise framing that would not diminish the paper's contributions. The missing baselines and ablations are addressable. The paper's core technical contributions — the decoupled GCN formulation for subgraph FL and the Hop2Vec method — are novel and well-validated.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>