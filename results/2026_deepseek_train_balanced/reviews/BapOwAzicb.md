## Summary

HOGT proposes a community-based hierarchical message-passing framework for graph transformers. The method partitions graph nodes into communities, introduces a learned community node per community, and uses a three-step scheme (node→community, community→community via attention, community→node) to capture local and long-range information. The paper reports strong empirical results on node classification, particularly on heterophilic graphs where prior GTs struggle, and provides a theoretical analysis showing the architecture can approximate global attention by varying the number of communities.

## Strengths

- **Large and statistically significant gains on heterophilic graphs, where GTs typically underperform**: On heterophilic datasets, HOGT outperforms the best heterophily-specific GNN (GPRGNN) by margins of 2.7% (Cornell), 4.6% (Wisconsin), and 2.8% (Actor), and outperforms the GT baseline Gapformer by 2.1% (Cornell), 3.1% (Texas), and 3.7% (Wisconsin). These improvements are reported as statistically significant (p-value ≪ 0.05). This is the paper's strongest empirical contribution, as most GT baselines degrade sharply on heterophilic graphs.

- **Orders-of-magnitude efficiency advantage over O(N²) GTs on large graphs**: Table 6 reports that Graphormer, LiteGT, and Polynormer encounter out-of-memory errors even on Cora, while HOGT scales to ogbn-arxiv (169K nodes) and ogbn-products (2.4M nodes) with competitive or state-of-the-art accuracy (Table 5). This directly addresses the scalability bottleneck the paper identifies in prior GTs.

- **Theoretical unification spanning from MPNN to full transformer by varying community granularity**: Proposition 4.1 and Theorem 4.1 show that with one community (m=1), HOGT reduces to an MPNN with a virtual node, and with N communities (m=N), it becomes the standard transformer. The general case provably approximates global self-attention. While this is an expressiveness result rather than a mechanistic explanation, it formally connects two previously separate paradigms.

- **Discarding positional encoding without degradation, notably on heterophilic graphs**: Table 4 shows HOGT achieves better accuracy without positional encoding on heterophilic datasets (Cornell, Texas, Wisconsin) and matching performance on homophilic datasets. This is a genuine insight: the community structure itself encodes sufficient structural information, making traditional PE redundant and even harmful when the graph topology is noisy.

## Weaknesses

### Fatal
None.

### Major

- **The RL-based community sampling — highlighted as a key contribution — is critically underspecified and its marginal gains undermine its claimed importance.** The entire description of the "learnable community sampling method based on reinforcement learning" (lines 69–71) consists of a single paragraph. It states that the updating process of the scalar *k* (the top-k ratio) is modeled as a finite-horizon MDP and solved with Q-learning, but provides none of the following: the state space, action space, reward function, transition dynamics, training procedure, how the Q-function is parameterized (neural network or table), or how RL training is integrated with the end-to-end HOGT optimization. The paper's own ablation (line 254) reports that the learnable method only "slightly outperforms" random walk sampling. Given both the marginal empirical gain and the total absence of specification, the RL component as presented cannot be evaluated as a meaningful contribution. This is a significant weakness for something the abstract highlights in blue text as a primary innovation.

### Minor

- **The "higher-order" framing in the title and throughout the paper is overclaimed.** The method operates through a two-level hierarchy of standard (pairwise) attention operations: nodes attend to their community node, community nodes attend to each other, then community nodes attend back to graph nodes. There is no modeling of interactions involving more than two entities (no hypergraph-like multi-entity attention, no simplicial complexes, no tensor decompositions). The approach is better described as hierarchical or multi-resolution attention. The paper acknowledges that for actual hypergraphs it "intuitively view[s] each hyperedge as a community" — precisely because hypergraphs already contain multi-entity structure, whereas regular graphs do not under this method. The persistent "higher-order" terminology creates an expectation the architecture does not meet.

- **The theoretical analysis does not address the paper's own narrative.** Theorem 4.1 shows that the three-step message passing can approximate global self-attention. But the paper's motivation (line 15) is that existing GTs suffer from "massive unrelated information aggregation" and fail to capture useful topological information. If HOGT approximates the same global attention as standard GTs, the theory offers no explanation for why its community structure should succeed where they fail. The analysis proves expressive power equivalence, not why the specific community partitioning helps — a gap between the framing and the formal results.

- **The paper does not specify the neighborhood radius used to form communities.** Line 71 says "for each selected node i, we generate a community with its neighbors" without indicating whether this means 1-hop neighbors, multi-hop, or a learned radius. This is a key architectural detail that affects both the method's behavior and its comparison to baselines.

- **The PE overinterpretation (line 262).** The paper states that "community sampling in HOGT are able to integrate structural information in a more flexible and effective way" based on Table 4. The ablation only shows that PE doesn't help when communities are already present — it does not show that communities provide the *same* structural information as PE more effectively. The claim overreaches the evidence.

### Trivial

- **Theorem numbering error (line 146):** The text references "the proof of Theorem 4.5" but the paper contains only Theorem 4.1. This appears to be a labeling inconsistency from a prior draft.

## Nice-to-Haves

- The local message-passing is concatenated only in the final C2G-MP step (Equation 4) rather than integrated into the earlier G2C aggregation or run as a parallel path. The paper says local information is "necessary to maintain" but does not justify the specific placement. An ablation comparing alternatives would strengthen the architectural analysis.
- A sharper delineation from Gapformer (Wu et al., 2021) would be helpful: the paper notes that with m=1 HOGT reduces to a virtual-node model like Gapformer, but the multi-community case (m>1) is the true contribution and deserves a clearer contrast explaining what the additional communities enable that a single virtual node cannot.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **Missing graph classification and link prediction results:** The paper states (line 153) that these results are in Appendices A.10 and A.11. The parser strips appendix content from all papers; the results exist in the original submission. Removed per protocol.
- **OOM on Cora is "surprising" / suggests suboptimal implementation:** The paper reports OOM as an empirical observation. The reviewer's speculation about implementation quality is not evidence-based. Removed.
- **Code availability / hyperparameters in main text:** The paper references appendices for these. Per protocol, missing appendix content is not a valid criticism when the parser strips it.
- **RL-sampling as a strength:** The Strength Finder claimed this as a strength, but the RL component is critically underspecified (see Major weakness 1). Per protocol, strengths that conflict with verified weaknesses are dropped.
- **Generic scope-creep criticisms** (e.g., "could the metric be measuring a proxy"): Removed as category-driven noise without concrete anchors in the paper.

## Novel Insights

The reviews surface a tension that the paper itself does not resolve: its strongest empirical signal (heterophilic graphs) and its strongest theoretical result (approximation to global attention) point in opposite explanatory directions. The heterophilic success suggests the community mechanism *restricts* information flow in a beneficial way (filtering noisy edges), yet the theory shows the architecture can *recover* full global attention. Understanding when the community bottleneck helps versus hurts — and whether the RL sampling provides any benefit beyond a well-chosen fixed *k* — would be a genuinely informative follow-up study that the current paper does not address.

## Suggestions

1. **Either fully specify the RL component (state space, action space, reward, Q-function parameterization, training protocol, hyperparameters) or remove it from the claimed contributions.** Given that it only marginally outperforms random walk and the core architecture does not depend on it, the simplest path is to drop the RL framing and present the GNN-based projection + top-k as the primary sampling method, with random walk as a practical alternative.

2. **Replace "higher-order" with more precise terminology** such as "hierarchical," "multi-resolution," or "community-structured" attention. Reserve "higher-order" for cases where the method actually models multi-entity interactions.

3. **Reposition the theoretical analysis** to focus on what the community granularity controls (effective receptive field, information bottleneck, complexity-expressiveness trade-off) rather than proving approximation to the very architecture the method aims to improve upon.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>