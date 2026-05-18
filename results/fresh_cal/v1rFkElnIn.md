Now I have a thorough understanding of the paper. Let me compose the final consolidated review by carefully cross-checking every claim against the paper's actual content.

---

## Summary

This paper proposes FedStruct, a subgraph federated learning framework that avoids sharing node features or embeddings by instead sharing structural information encoded via a decoupled GCN. The framework introduces Hop2Vec, a learnable task-dependent node structure embedding method, and is evaluated on six datasets for semi-supervised node classification. The core idea — using global graph topology rather than node features as the cross-client currency — is novel within the subgraph FL setting and is supported by empirical results that approach centralized performance on multiple benchmarks.

## Strengths

- **First subgraph FL method demonstrated on heterophilic graphs.** Table 1 shows FedStruct (H2V) achieves 52.76% accuracy on Chameleon (a heterophilic dataset) with 20 clients, versus 34.33% for FedSage+ and 34.72% for FedSGD GNN. No baseline exceeds 37% on this dataset. This is a genuine contribution — the paper explicitly identifies that prior subgraph FL methods rely on a homophily assumption (line 123), and FedStruct is the first to address this gap.

- **Near-centralized accuracy across diverse datasets with varying client counts.** FedStruct (H2V) achieves accuracy within 1–3 percentage points of the central GNN on all six datasets (e.g., Cora 10 clients: 80.28% vs central 82.06%; Amazon Ratings 10 clients: 41.23% vs 41.32%). The performance also degrades minimally as clients increase from 5 to 20 (e.g., Chameleon: 53.06% → 52.76%; Pubmed: 86.07% → 86.24%), contrasting with baselines that drop substantially.

- **Task-dependent Hop2Vec clearly outperforms fixed structure embeddings.** Table 1 shows FedStruct (H2V) consistently outperforms FedStruct (Deg) and FedStruct (FedStar) across all datasets and client counts (e.g., Cora 10 clients: 80.28% vs 68.64% (Deg) and 68.87% (FedStar)). This internal comparison controls for the shared structural information, showing that the *specific design* of Hop2Vec — not merely access to global topology — drives the large gains.

- **Communication-efficient pruning with minimal accuracy loss.** FedStruct-p reduces offline complexity from O(L·n²) to O(L·p·n) with p=30, while Table 1 shows only small accuracy drops (e.g., Cora 10 clients: 78.75% vs 80.28%; Chameleon 10 clients: 52.26% vs 52.36%), demonstrating practical viability.

## Weaknesses

### Fatal

None.

### Major

- **Privacy claims are overstated relative to what is actually shared.** The paper claims FedStruct "eliminates the necessity of sharing or generating sensitive node features or embeddings" and that structure is "often less sensitive" (line 88). However, the framework requires sharing (1) rows of the global combined adjacency matrix Â^{[i]} (an n_i × n matrix encoding L-hop path counts), which can leak degrees, distances, and community structure, and (2) for Hop2Vec, the full NSF matrix **S** of dimension n × d (Table 2 shows online complexity O(E·K·n·d) for Hop2Vec, which involves these learnable NSFs). The argument that "due to graph isomorphism, Â^{[i]} cannot be used to uniquely determine the adjacency matrix" (line 383-385) is technically true but does not imply low sensitivity — non-uniqueness is not a privacy guarantee. No differential privacy analysis, reconstruction attack discussion, or quantitative comparison of structural vs. feature sensitivity is provided in the main text. The paper references App.~\ref{app:privacy} for privacy considerations, but the main text's framing substantially understates the leakage. This is the most consequential weakness because the privacy motivation is central to the paper's positioning.

- **The relative contribution of the decoupled GCN architecture vs. structural sharing is not ablated.** FedStruct uses a decoupled GCN for both fGNN and sGNN, while the baselines (FedSGD GNN, FedSage+) use standard GraphSAGE. Decoupled GCNs are known to benefit heterophilic graphs, and the largest gap is on Chameleon (FedStruct H2V 52.76% vs FedSGD GNN 34.72%). The paper claims "DCGN performs similarly" to GraphSAGE (line 491, referencing the appendix), which partially addresses this. But an explicit ablation — e.g., "FedStruct without structural sharing" using the decoupled GCN with only the local Â^{(i)} — is missing from the main evaluation. Without this, it is unclear how much of the gain on heterophilic graphs comes from the decoupled architecture versus the structural sharing.

### Minor

- **Missing comparison with FedCog.** The related work (line 112) identifies FedCog as a closely related method that also operates in the same setting (known cross-subgraph edges) and uses a decoupling approach. FedCog is not included as a baseline in Table 1, and the paper does not explain its omission. While FedSage+ ideal is described as providing an upper bound for both FedSage+ and FedNI, FedCog is a different class of method and a direct comparison would strengthen the evaluation.

- **No statistical significance tests.** Results are reported as means over 10 runs with standard deviations, but no significance tests (e.g., paired t-tests) are provided for the key comparisons (FedStruct H2V vs. FedSage+ ideal on Cora, etc.). Given that some differences are small (e.g., Cora 10 clients: FedStruct H2V 80.28% vs FedSage+ ideal 80.85%), significance testing would help the reader assess whether the claimed improvements are reliable.

- **Figure 1 motivation is under-described.** The bar chart (Figure 1) compares "features," "structure only," and "Fed SGD," and is used to motivate the entire approach. The paper does not explain how the "features" and "structure only" baselines were constructed (e.g., what method was used for the structure-only variant, and how were node features excluded?). This makes the motivation figure unverifiable.

### Trivial

None.

## Nice-to-Haves

- An ablation of the hop coefficients β_l (fixed vs. learned) and sensitivity to L.
- A more detailed description in the main text of the offline computation of Â^{[i]}, rather than deferring entirely to the appendix.
- Reporting results for non-random partitionings (Louvain, K-means) in the main table rather than only in the appendix, or at least summarizing the key pattern.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing contemporary baselines (FedNI, FedStar)."** FedNI is addressed via FedSage+ ideal (line 495), which the paper explicitly describes as an upper bound for both FedSage+ and FedNI. FedStar is included as an NSF variant within FedStruct (FedStruct (FedStar) in Table 1). Only FedCog is genuinely missing. The criticism as originally stated over-counts the missing baselines.

- **"FedStruct has access to global topology while baselines do not — comparison is staged."** This is partially addressed by the internal FedStruct variants (Deg, FedStar) that use the same Â^{[i]} but perform much worse than H2V. The paper also includes FedSage+ ideal, which has access to true 1-hop neighbor features (arguably more informative than structural topology). The criticism overstates the problem: the evidence does show that specific design choices matter, even if a cleaner ablation would strengthen the case.

- **"Computing Â^{[i]} is a nontrivial distributed algorithm with privacy implications."** The paper references an algorithm in App.~\ref{app:schemes} that computes Â^{[i]} "without gaining any additional information about the global graph" (line 382). Per the meta-review guidelines, criticisms about content deferred to the appendix should be removed since the parser strips those sections.

- **"The paper uses FedSGD not FedAvg."** The paper explicitly states that "Additional results including federated averaging... are provided in App.~\ref{app:MoreResults}" (line 567).

- **"Complexity table notation is unclear."** The comparison uses standard big-O notation; the notational differences between methods are explained in the text (lines 440-452).

- **Formatting/style nitpicks and speculation about appendix content.**

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation that emerges from the review is that the *internal* comparison between FedStruct variants (Deg → FedStar → H2V) provides a quasi-ablation of the structural encoding quality. Because all three variants share the same Â^{[i]} and decoupled architecture, the progression in performance (e.g., Cora 10 clients: 68.64% → 68.87% → 80.28%) cleanly isolates the benefit of task-adaptive learned NSFs over fixed structural encodings. This is actually stronger evidence for the Hop2Vec contribution than the comparison against baselines without structural information. The paper does not highlight this internal progression as a controlled experiment, which it effectively is.

## Suggestions

1. **Add an explicit ablation**: Include a "FedStruct-local" variant that uses the decoupled GCN with only the local combined adjacency matrix Â^{(i)} (no cross-client structural information). This isolates the effect of the decoupled architecture from the effect of structural sharing.

2. **Add a "structure-augmented" baseline**: A variant of FedSGD where clients receive rows of Â^{[i]} as additional input to a standard GraphSAGE model. This would directly test whether the gains come from having global topology or from FedStruct's specific method of using it.

3. **Re-frame the privacy discussion honestly**: Acknowledge that while node features are not shared, structural information (Â^{[i]}, NSFs S) is shared and can leak topology. Discuss what practical protection this provides relative to the threat model (e.g., in anti-money laundering, transaction graph structure may itself be sensitive). If differential privacy can be applied to Â^{[i]}, sketch how.

4. **Include FedCog as a baseline** on at least the homophilic datasets where it is designed to work.

5. **Describe Figure 1's construction** (what methods were used for the "features" and "structure only" bars) so that the motivation is verifiable.

## Score and Decision

**Originality:** The paper presents a novel combination of decoupled GCNs with structural information sharing in subgraph FL, and Hop2Vec is a genuinely new method for task-dependent node structure embeddings.  
**Importance of research question:** Subgraph FL is an important and growing area, and the privacy-motivated angle of avoiding node feature sharing addresses a real limitation of existing methods.  
**Claims support:** The central claims (competitive accuracy, robustness across client counts, effectiveness on heterophilic graphs) are supported by Table 1. The privacy claim is partially supported but overstated relative to what is actually shared.  
**Soundness:** The theoretical derivation (gradients, information requirements) is sound. The experimental design would benefit from additional ablations to isolate architecture vs. structural sharing, but the current results are informative.  
**Clarity:** The paper is generally well-written with clear notation, though Figure 1 is under-described and some technical details are deferred to the appendix.  
**Value:** The paper makes a meaningful contribution to subgraph FL by demonstrating that structural information can substitute for node feature sharing, and Hop2Vec is a practical contribution. The heterophilic graph results are a clear advance over prior work.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>