## Summary

NEUROLIFTING reparameterizes MAP inference in Markov Random Fields by using a GNN to map randomly initialized node embeddings to probability distributions over variable states, then minimizing the expected energy via gradient descent. The core idea—using a continuous relaxation parameterized by a GNN to enable gradient-based optimization of discrete MRF energies—is clearly presented and has some empirical support on large-scale instances.

## Strengths

- **Strong performance on large-scale MRFs (50k nodes).** On the largest synthetic instances (Tables 1, 2), NEUROLIFTING consistently achieves the lowest energy, often by a wide margin over LBP, TRBP, and Toulbar2. For example, on P.potts\_5 (50k nodes) it reaches 11466.5 vs. Toulbar2's 12468.2, and on H.Instances\_3 it achieves -3601.7 vs. Toulbar2's 1423.8. This scalability result is the paper's strongest evidence.

- **Real-world validation on Physical Cell Identity (PCI) data.** Table 5 shows NEUROLIFTING beating Toulbar2 on the largest PCI instance (929 nodes, 29009 cliques: 1087.3 vs. 1118.1) and outperforming on all synthetic PCI instances. This demonstrates practical applicability beyond synthetic benchmarks.

- **Complexity analysis showing linear scaling.** Section 3.5 derives O(|𝒳|(|V| + c_max|C|) + K|V|(N_v + d)) time complexity, confirming linear growth with nodes, layers, and feature dimensions—a useful formal property for a method targeting large-scale inference.

- **Principled padding strategy for variable-state mismatch.** Section 3.2 describes why padding with the per-term max energy is preferable to masking or using a global maximum, with reasoning about how alternative approaches can distort the loss landscape. This is a thoughtful design decision.

- **Ablation establishing GraphSAGE as the backbone.** Figure 3 compares GCN, GAT, and GraphSAGE across UAI, PCI, and synthetic datasets, showing GraphSAGE gives the lowest loss and fastest convergence—supporting the intuition that equal-weight neighborhood aggregation suits MRF structure.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation: no comparison against a non-GNN baseline (independent parameterization).** The paper never compares NEUROLIFTING against a version where each node has its own independently learned probability vector (no GNN, no shared parameters, just direct gradient descent on the continuous relaxation). This is the single most critical control: without it, the reader cannot determine whether the GNN's message-passing structure is essential, helpful, or irrelevant. The ROS paper (5.67, rejected) received the same criticism for the same omission. As the paper's central claim is that GNNs serve as a non-parametric lifting scheme, this gap is major.

- **No runtime/wall-clock data for NEUROLIFTING.** The paper claims efficiency ("linear computational complexity," "efficient and parallelizable optimization") but reports no timing results of its own. Toulbar2 is given time limits (1200s, 3600s, 18000s), but for NEUROLIFTING the reader gets iteration counts only (100–150 iterations). On 50k-node instances with high-order cliques, whether this takes seconds, minutes, or hours is unknown. The efficiency claim is unsubstantiated without wall-clock data or scaling plots.

- **No statistical variance reported.** Every result is a single number for a method that involves random feature initialization, simulated annealing, and potentially nondeterministic GPU training. On instances where the difference between NEUROLIFTING and LBP is tiny (e.g., P.potts\_8: 24552.413 vs. 24552.400; P.random\_8: 24555.995 vs. 24556.000), the reader cannot assess whether these differences are meaningful or within run-to-run noise.

- **Abstract/Introduction overclaim relative to the data.** The paper claims NEUROLIFTING "performs very close to the exact solver Toulbar2" and "significantly surpasses existing approximate methods." The data does not consistently support this: on ProteinFolding\_12, NEUROLIFTING's energy (16051.8) is 4.5× the optimal (3562.4); on many small-to-moderate instances in Table 1 (P.potts\_1–3, P.random\_1–3), LBP or Toulbar2 beats NEUROLIFTING. The paper's own text acknowledges scale-dependency ("as the problem size scales up"), but the abstract omits this qualification.

### Minor

- **Simulated annealing is mentioned but never described.** The paper states "employ simulated annealing during the training process" (Section 3.4) with no detail on the temperature schedule, mixing steps, or how it is incorporated (learning rate schedule? noise injection? output perturbation?). This is a reproducibility gap for a method that is otherwise described clearly.

- **The "lifting" connection is metaphorical rather than formalized.** The paper repeatedly draws an analogy between deeper GNN layers and classical lifting into higher-dimensional spaces (Section 3.5, Figure 4), but does not formalize what property of lifting is being instantiated (fewer local minima? better conditioning?). The loss landscape visualization in Figure 4 is only on one instance (Segmentation\_19) and has no comparison against a non-GNN baseline, so it is suggestive but not conclusive.

- **On UAI 2022 pairwise cases (Table 3), NEUROLIFTING is consistently worse than Toulbar2 and often comparable to or worse than LBP.** The paper positions itself as outperforming approximate methods, but on this benchmark Toulbar2 (with a 1200s timeout) finds optimal solutions on most small instances and NEUROLIFTING is sometimes the second- or third-best method. The narrative of "surpassing" is selective.

### Trivial
None.

## Nice-to-Haves

- A comparison to other neural combinatorial solvers (e.g., Karalias & Loukas, Cappart et al.) that the paper itself cites would broaden the evaluation.
- An analysis of failure cases (e.g., ProteinFolding\_12 where the gap from optimal is 4.5×) could clarify the method's limitations and guide future improvements.
- Reporting hyperparameter sensitivity (lifting dimension, learning rate, number of layers) would help assess robustness.

## Removed Points
- **Criticism about "no comparison to convex BP, dual decomposition, or other learned methods"**: These are broad categories that the paper does not claim to cover, and the baselines included (LBP, TRBP, Toulbar2) are standard for the UAI competition framework.
- **Criticism about "Toulbar2 may not have converged to optimality"** for large instances: This is acknowledged by the paper's use of time limits following UAI competition norms. A fixed time limit is standard practice when comparing against exact solvers on large instances.
- **Criticism about padding justification being "assertion without support"**: The paper provides a concrete reasoning chain for why max-energy padding is preferable to masking. While an empirical comparison would strengthen the claim, the reasoning is explicit and reasonable.
- **Strength about loss landscape visualization (Fig. 4) supporting the lifting analogy**: This strength was overstated in the Strength Finder—the visualization is on one instance with no GNN-free baseline—but I retain a weaker version of it in the Minor Weaknesses section.

## Novel Insights

The harsh reviewer correctly identifies that the paper never tests the most important control (independent parameterization without a GNN), which would directly test whether the GNN architecture is the source of any performance gain. This is a recurring pattern in GNN-for-combinatorial-optimization papers—the ROS paper on Max-k-Cut received nearly identical criticism. The Strength Finder's primary evidence (large-instance wins) is genuine but weakened by the fact that no alternative neural baseline is tested, making it unclear whether the wins come from the GNN's inductive bias or simply from gradient descent on a continuous relaxation. Conversely, neither reviewer noted that the paper's strongest point—consistently beating Toulbar2 on 50k-node high-order MRFs (Table 2)—is a genuinely non-trivial result that holds across multiple problem classes and suggests the method is discovering meaningful structure, even if the source of the advantage is not fully isolated.

## Suggestions

1. **Add the critical GNN ablation**: Compare NEUROLIFTING against direct gradient descent on independent per-node probability vectors (no message passing). If the GNN version wins, the aggregation hypothesis is supported; if not, the paper needs to reframe its contribution.
2. **Report wall-clock time** for NEUROLIFTING across problem sizes, ideally as scaling plots. Without this, the efficiency and scalability claims are empty.
3. **Report multiple runs (at least 5) with means and standard deviations** for key tables, especially on instances where differences from baselines are small.
4. **Tone down the abstract** to qualify the scope: "on large-scale MRFs, NEUROLIFTING delivers superior solution quality" is supported by the data; "very close to the exact solver" is not consistently supported.
5. **Describe the simulated annealing procedure** concretely (temperature schedule, how it is applied) for reproducibility.

## Score and Decision

**Calibration anchor references (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| /home/wg25r/review_agent/human_reviews/F8l0llkMk0.md | 3.33 | 1 | Weaker: less rigorous experiments, unclear contribution |
| /home/wg25r/review_agent/human_reviews/mnRLzeNsVN.md | 3.00 | 1 | Weaker: method has basic design problems, withdrawn |
| /home/wg25r/review_agent/human_reviews/CpiJWKFdHN.md (ROS) | 5.67 | 2 | Slightly stronger: similar approach but reports runtime and has theory; still rejected |
| /home/wg25r/review_agent/human_reviews/4Hd7u3LHlZ.md (PD-GNN) | 5.25 | 2 | Comparable: similar methodological depth and experimental gaps; rejected |
| /home/wg25r/review_agent/human_reviews/7vVWiCrFnd.md | 6.60 | 1 | Stronger: solid theoretical contribution; accepted (poster) |
| /home/wg25r/review_agent/human_reviews/kbQIWi4ZiL.md | 5.00 | 2 | Comparable: similar unsupervised relaxation approach; withdrawn/rejected |
| /home/wg25r/review_agent/human_reviews/WszeEzjcq2.md | 5.33 | 2 | Comparable: empirically focused but withdrawn |
| /home/wg25r/review_agent/human_reviews/0u9uvPdRgV.md | 4.25 | 3 | Weaker: less clear methodology |
| /home/wg25r/review_agent/human_reviews/Dgc5RWZwTR.md | 4.75 | 2 | Weaker: narrower contribution |

**Round-1 bracket:** Between ~3 (weak anchors) and ~8 (strong anchors). The paper clearly exceeds the weak-anchor papers (fatal flaw papers scoring 3.0–3.33) but falls well short of the strong-accept papers (7.6+).

**Round-2 narrowing:** The most comparable anchor is ROS (5.67, rejected)—same GNN+relaxation paradigm with a similar missing-ablation weakness. NEUROLIFTING is slightly weaker than ROS because it also omits runtime data and confidence intervals entirely. This places the paper in the 4.5–5.5 range.

**Final score:** 5.0. The paper has a reasonable core idea and strong results on large-scale instances, but three major experimental gaps (no GNN ablation, no runtime data, no statistical variance) collectively prevent acceptance at a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>