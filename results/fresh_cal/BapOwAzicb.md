Now I have a thorough understanding of the paper and have verified the claims against the actual text. Let me synthesize the final review.

## Summary

HOGT proposes a graph transformer architecture that partitions the graph into communities, introduces a representative "community node" for each community, and uses a three-step message-passing scheme (Graph-to-Community → Community-to-Community → Community-to-Graph) to capture local, higher-order, and global information. The paper presents strong empirical results on heterophilic node classification, demonstrates scalability advantages over dense graph transformers, and shows that positional encodings can be omitted without loss. However, its most distinctive claimed contribution—a learnable community sampling method via reinforcement learning—is critically underspecified and numerically unevaluated, and the baseline comparisons omit several relevant recent graph transformers.

## Strengths

- **Strong empirical gains on heterophilic graphs (Table 3).** HOGT outperforms all baselines on multiple small-scale heterophilic datasets (e.g., +2.7% on Cornell, +4.6% on Wisconsin, +2.8% on Actor over GPRGNN) and achieves large margins on the larger roman-empire and amazon-ratings datasets where most existing graph transformers struggle. These results are the paper's strongest evidence that the community-based design captures long-range dependencies effectively.

- **Scalability advantages over dense graph transformers (Table 6).** HOGT demonstrates orders-of-magnitude savings in training time, inference time, and GPU memory compared to Graphormer and LiteGT (which run out of memory on many datasets). This directly addresses the quadratic-complexity bottleneck that the paper correctly identifies as a limitation of prior GTs.

- **Positional encoding is shown to be unnecessary (Table 4).** The ablation systematically compares HOGT with and without Laplacian/random-walk positional encoding. On heterophilic datasets, omitting PE yields better performance, and on homophilic datasets the gap is minor. This validates the paper's claim that the community-based message-passing inherently encodes structural information.

- **Well-motivated architectural design.** The three-step framework (G2C-MP → C2C-ATTN → C2G-MP) is clearly described and the intuition that community nodes serve as bridges between local aggregation and global attention is sensible. The design unifies several existing model types as special cases (virtual-node GNNs at one extreme, full transformers at the other), which provides a useful conceptual framing.

## Weaknesses

### Fatal

None. The core architecture is sound and produces competitive results even with simple sampling methods. The weaknesses below are serious but addressable.

### Major

- **The learnable RL-based community sampling—a central claimed contribution—is critically underspecified and numerically unevaluated.** The abstract and introduction highlight "a learnable community sampling method with reinforcement learning" as a key innovation. However, Section 3.1 devotes only three sentences to the RL method: "We model the updating process of k as a finite horizon Markov Decision Process (MDP) and adopt Q-learning to learn the MDP." No state space, action space, reward function, training procedure, or integration with the main graph learning objective is specified. The ablation (Section 5.3) claims "HOGT with proposed learnable sampling slightly outperforms random walk" but provides no numerical evidence—the actual numbers are asserted to be "included in Tables 2 and 3," yet those tables show only a single HOGT row per dataset (presumably random walk). For a contribution highlighted in the abstract, this degree of specification and evidential support is insufficient. **Impact:** This is the paper's most distinctive claim; a reader cannot reproduce or assess it.

- **Baseline comparisons are incomplete for the claimed state-of-the-art.** The paper evaluates on standard benchmarks but omits several strong and relevant graph transformers: GraphGPS (Rampasek et al., 2022), NodeFormer (Wu et al., 2022), GOAT (Liu et al., 2023), Polylatte (Zhong et al., 2024), and G2G (Jain et al., 2024) are not included in any comparison table. On ogbn-arxiv, HOGT reports 72.14%, while published results for NodeFormer (~73.0%) and GraphGPS (>72.5%) are competitive or higher. On heterophilic datasets like Texas and Wisconsin, G2G reports 86.5% and 91.0% versus HOGT's 82.5% and 88.1%. The efficiency analysis (Table 6) compares against dense GTs (Graphormer, LiteGT) but not against other efficient GTs designed for scalability (NodeFormer, GOAT). Without these comparisons, the "state-of-the-art or competitive" claim is unsupported. **Impact:** Directly weakens the paper's central empirical claim.

- **The theoretical analysis (Section 4) does not provide meaningful new insight.** Theorem 4.1 asserts that the three-step framework can approximate full self-attention arbitrarily well. However, this relies on Proposition 4.1, which cites a known result (Cai et al., 2023) about virtual-node MPNNs, and then essentially states that stacking MP→Attention→MP preserves that expressiveness. No novel analysis is given about why the *multiple-community* design is beneficial vs. a single virtual node; no bound relates community size, number of communities, or graph structure to approximation error; no proof sketch beyond deferral to the appendix is provided. The theory functions as a sanity check rather than a substantive contribution. **Impact:** The paper would be more honest if it reframed this as a unifying perspective rather than a formal result.

### Minor

- **Ablation reporting is unclear.** The paper states that results for three community sampling methods (learnable, random walk, spectral clustering) are in Tables 2 and 3, but those tables only show a single HOGT row per dataset. It is never specified which sampling method corresponds to the main reported HOGT results, making the main results difficult to interpret in light of the central design choice. A dedicated table or separate rows would resolve this.

- **On large heterophilic datasets, the best configuration uses a single community (essentially a virtual node), which somewhat undercuts the multi-community motivation.** The paper acknowledges (Section 5.3) that spectral clustering with a single community works best on roman-empire and amazon-ratings, and that increasing communities degrades performance. This deserves more analysis—when and why do multiple communities help vs. hurt?

- **Statistical significance claim lacks rigor.** The paper states "the improvements of HGT over baselines are all statistically significant (p-value << 0.05)" without specifying which test was used, whether it was pairwise, or whether corrections for multiple comparisons were applied.

### Trivial

- In Equation 5 (C2G-MP), the notation for combining community-node and neighbor keys/values is shown as vertical concatenation in the equation, but the surrounding text calls it a "combination" without explicitly saying "concatenation." Clarifying this in the text would aid readability.

## Nice-to-Haves

- Hyperparameter sensitivity analysis for the number of communities (currently deferred to appendix).
- Qualitative analysis of what communities represent (e.g., node label distributions within communities) to support the claim that communities capture meaningful structure.
- Comparison with subgraph-based methods like LSPE (Dwivedi et al., 2021) and subgraph tokenization (Zhang et al., 2022) that are closely related.

## Removed Points

- **"The C2G-MP equation is ambiguous; 'combination' is not defined."** The paper's equation shows vertical concatenation via bracket notation, so the operation is specified. This criticism is factually incorrect. **(Removed: factually wrong, per Hard Rules)**

- **"Hypergraph results table not shown in main text."** The hypergraph results table is referenced but appears to be in the appendix (stripped by the parser). Per Hard Rules, criticism about missing appendix content should be removed. **(Removed: appendix content stripped by parser)**

- **"Proof is missing from the main paper."** Per Hard Rules, weaknesses about missing proofs in the appendix should be removed. The substantive criticism about the theory being thin is retained in Major. **(Removed: Hard Rule on appendix content)**

- **"The claim that HOGT discards positional encoding is overstated."** The ablation in Table 4 does show comparable-or-better performance without PE across tested datasets. The paper's claim is about its own model on these datasets, not a universal guarantee. This criticism is a generic caveat applicable to all empirical findings. **(Removed: generic concern, not a specific weakness)**

- **Strength: "Learnable community sampling via RL... the ablation confirms it slightly outperforms fixed methods."** This directly conflicts with the verified weakness that the RL method is unevaluated (no numerical evidence given). Per the filtering rule, when a strength and weakness disagree, the weakness wins. **(Removed: conflicts with verified weakness)**

- **Strength: "Theoretical proof of global attention approximation."** The paper does contain a theorem, but the strength is substantially undermined by the verified weakness that the theory is thin and not novel. A tempered version is reflected in the Architecture strength above rather than as a standalone "proof" strength. **(Downgraded from standalone strength)**

## Novel Insights

None beyond the paper's own contributions. The reviews identify significant gaps (underspecified RL method, missing baselines, thin theory) but do not surface novel technical observations about the paper that the authors miss. The key insight from the meta-review is that the paper's architecture itself is reasonable and the heterophilic results are genuinely strong, but the most hyped contribution (RL sampling) is the weakest part and the SOTA claims are unsupported by the chosen baselines.

## Suggestions

1. **Either fully specify and evaluate the RL sampling, or remove it from the contribution list.** Provide the MDP specification (state/action/reward), training procedure, and a dedicated table comparing HOGT(learnable), HOGT(random walk), and HOGT(spectral) with standard deviations. If the learnable variant does not consistently outperform simple sampling, be honest about that and frame it as a preliminary attempt.

2. **Add missing baselines.** Include GraphGPS, NodeFormer, GOAT, and G2G on the datasets where they have published results. If compute constraints prevent retraining, clearly acknowledge the gap and position HOGT as competitive within its compute budget rather than claiming unconditional SOTA.

3. **Reframe the theory section.** Either provide a concrete analysis showing when multiple communities provide benefits that a single virtual node cannot (e.g., expressiveness separation), or drop the formal theorem framing and present Section 4 as a unifying perspective on how existing models relate.

4. **Clarify the ablation.** Add separate rows for each sampling method in the main tables, or show a dedicated table. Specify which sampling was used for the reported HOGT results in Tables 2 and 3.

5. **Analyze the single-community result.** Discuss when and why multiple communities matter vs. when a single community works best, turning this apparent contradiction into a design insight.

## Score and Decision

The paper presents a well-motivated architecture with genuinely strong results on heterophilic benchmarks and clear scalability advantages. However, the most prominently advertised contribution (learnable RL sampling) is unevaluated, the SOTA claims are weakened by missing baselines, and the theoretical analysis does not deliver substantive insight. These are fixable issues—the core architecture is sound—but in the current form the paper does not meet the evidentiary bar for its claimed contributions.

**Score: 5.0** (borderline reject; major revision needed)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>