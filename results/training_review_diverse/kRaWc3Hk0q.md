Now I have all the information needed. Let me synthesize the final review.

## Summary

ReHub introduces a graph transformer that achieves linear complexity by dynamically reassigning each graph node (spoke) to a constant number of virtual nodes (hubs) per layer. The reassignment uses cheap hub-hub similarity to avoid expensive O(n√n) spoke-hub computations. The method is evaluated on LRGB benchmarks, large-graph node classification, and memory scaling experiments, consistently improving over Neural Atoms and achieving competitive accuracy with Exphormer at lower memory cost.

## Strengths

- **Linear memory scaling with competitive accuracy.** Figure 3 shows ReHub's peak memory grows linearly on graphs from 10K to 700K nodes, using less than half the memory of Neural Atoms and Exphormer. Table 4 confirms this memory reduction (1.13GB vs. 1.77GB on Coauthor Physics) comes with only a small accuracy gap (96.89 vs. 97.16), directly supporting the core claim.

- **Consistent improvement over Neural Atoms across MPNNs and datasets.** Table 1 shows ReHub (sparse and dense) outperforms Neural Atoms on Peptides-func, Peptides-struct, and PCQM-Contact for every tested MPNN (GCN, GCN2, GINE, GatedGCN, GatedGCN+RWSE). For example, with GatedGCN on Peptides-func: ReHub 0.6685 AP vs. Neural Atoms 0.6562.

- **Sparse variant matches dense variant.** Tables 1 and 2 repeatedly show ReHub (sparse, k=3) achieves nearly identical performance to ReHub-FC (fully connected). On Peptides-struct with GatedGCN+RWSE: ReHub 0.2488 MAE vs. ReHub-FC 0.2490 — within one standard deviation. This validates that the reassignment mechanism makes sparse connectivity as effective as dense.

- **Ablation study cleanly isolates each design choice.** Table 3 decomposes contributions on PascalVOC-SP: learned hubs (0.3084) → cluster mean (0.3574) → dynamic hub count (0.3703) → reassignment (0.3797) → spoke encoding (0.3860). Each step adds a clear performance gain, confirming the design rationale.

- **Hub utilization analysis shows consistent connectivity.** Figure 4 demonstrates that across layers and configurations (k=3 or 5, r=1 or 4), only about 10% of hubs remain unused per graph, indicating the reassignment does not collapse information flow to a subset of hubs.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence. The method is sound, the experiments are well-designed, and the limitations are honestly stated.

### Minor

- **Over-optimistic framing of the comparison with Exphormer.** The abstract states ReHub "outperforms competitive baselines," and the paper frames the results as a clear win. But Exphormer achieves higher accuracy on 2 of 4 LRGB datasets (PCQM-Contact MRR 0.3637 vs. 0.3534; PascalVOC-SP F1 0.3975 vs. 0.3860) and on both large-graph benchmarks (Coauthor Physics 97.16 vs. 96.89; OGBN-Arxiv 72.44 vs. 71.06). The results actually show a memory–accuracy trade-off: ReHub saves memory but often trails Exphormer in accuracy. The conclusion acknowledges this more honestly ("competitive accuracy... with lower memory consumption"), but the abstract and introduction would benefit from calibrated language that makes the trade-off explicit rather than implying uniform superiority.

- **The reassignment heuristic lacks direct validation of its approximation quality.** Algorithm 1 replaces a spoke's k−1 underperforming hubs with the k nearest hubs of the spoke's closest hub, avoiding O(n√n) exhaustive computation. The empirical evidence that the sparse variant matches the dense variant is strong support for the overall approach. However, the paper provides no analysis of how well the heuristic's chosen hubs match the truly optimal k hubs per spoke (e.g., via exhaustive computation on a small graph), nor does it characterize cases where the approximation might break down. The authors' self-acknowledged limitation ("make the reassignment module learnable") partially mitigates this, but a brief empirical validation would strengthen the paper.

### Trivial

- In Algorithm 1, the notation H(hubs) is used before it is formally introduced. The algorithm is readable but could be slightly cleaner.

- The hub utilization analysis reports ~10% unused hubs across layers (Figure 4) but does not comment on whether this is a harmless side-effect or a potential inefficiency worth addressing.

## Nice-to-Haves

- A sensitivity analysis of k and hub ratio r on at least one LRGB dataset would help users understand the method's robustness to hyperparameter choices.

- A brief discussion of the one-time computational cost of METIS clustering for hub initialization, noting that it can be amortized over training, would be useful for practitioners applying the method to graphs with millions of nodes.

- A direct comparison of the heuristic hub selection against exhaustive optimal selection on a small graph (even a single-layer analysis) would strengthen confidence in the reassignment design.

## Removed Points

These points were raised by reviewers but are removed from the main assessment, with brief justifications:

- **"The linear complexity claim is an oversimplification (O(n log n) due to sorting)."** Removed as factually incorrect. The Bottom-k-Indices operation in Algorithm 1 can be implemented in O(h) per hub (using selection algorithms such as `torch.topk` with O(h log k) = O(h) for constant k), keeping the overall complexity O(n). The paper's complexity derivation in Section 3.5 is technically correct.

- **"Neural Atoms results missing on PascalVOC-SP."** Removed — the paper appropriately notes "only available results." Authors cannot report what the original paper did not publish.

- **"The airline analogy is not directly analogous."** Removed — not a substantive weakness. Analogies are high-level illustrations, not literal descriptions of the algorithm.

- **"Should include additional large-graph datasets (e.g., OGBN-Products)."** Moved to Nice-to-Haves as scope creep. The current evidence with two large-graph datasets and a memory scaling experiment is already adequate.

## Novel Insights

The most striking finding in the reviews is the confirmation that the reassignment heuristic, despite being a simple approximation, enables sparse connectivity that matches dense connectivity in accuracy. This is a non-trivial result: it means that the paper's central design insight — that each node only needs a small, adaptively selected set of virtual nodes per layer — is validated by the experiments. The ablation study further reveals that cluster-based initialization (using METIS) contributes the largest single performance gain (from 0.3084 to 0.3574), suggesting that initialization strategy matters more than the reassignment itself. This is a useful observation that the authors could highlight more.

## Suggestions

1. **Rephrase comparative claims in the abstract and introduction** to explicitly describe the memory–accuracy trade-off rather than suggesting uniform improvement. For example: "ReHub achieves competitive accuracy with Exphormer while using substantially less memory, and consistently outperforms the Neural Atoms baseline."

2. **Add a brief validation of the reassignment heuristic** — on a small dataset where exhaustive computation is feasible, compare the hubs selected by the heuristic to those selected by the true top-k spoke-hub similarity. Even a one-layer analysis would be informative.

3. **Clarify the hub utilization result** — comment on whether the ~10% unused hubs across layers is expected behavior, a consequence of the heuristic's approximation, or an artifact of graph structure.

## Score and Decision

**Originality:** The dynamic hub-spoke reassignment based on hub-hub similarity is novel. The idea of growing the number of virtual nodes as O(√n) while keeping per-node connections constant is a clever relaxation of prior approaches that fix the number of virtual nodes.

**Importance of research question:** Scalable graph transformers are an active and important area. Addressing the memory bottleneck of virtual-node approaches is practically relevant.

**Claims well-supported:** The core claims (linear memory, competitive accuracy, improvement over Neural Atoms) are supported by the evidence. The only issue is the framing of the comparison with Exphormer, which mildly overclaims uniform superiority.

**Soundness of experiments:** Well-designed experiments covering LRGB benchmarks, large-graph node classification, memory scaling, and ablations. Reproducibility is adequate (5 seeds reported, standard deviations provided).

**Clarity of writing:** The paper is clearly written and the architecture is easy to follow. The method section is well-structured.

**Value to the community:** The method is modular (compatible with various MPNNs) and practical (significant memory savings). The code release would enable adoption.

The paper makes a solid contribution. There are no fatal or major weaknesses. The minor issues (framing calibration, lack of heuristic validation) are addressable in revision. The paper should be accepted.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>