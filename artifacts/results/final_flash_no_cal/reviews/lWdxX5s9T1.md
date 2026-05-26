## Summary

RADAR proposes two complementary mechanisms—SVD-based initialization and Sinkhorn-normalized attention—to enable neural VRP solvers to handle asymmetric distance matrices. The SVD component constructs compact node embeddings that encode each node's role as source and destination by factorizing the cost matrix; the Sinkhorn component replaces standard row-wise softmax with joint row-column normalization to capture bidirectional neighborhood context in attention. The paper evaluates on 17 synthetic VRP variants (ATSP, ACVRP, 16 multi-task variants) and 3 real-world benchmarks, demonstrating consistent improvements over existing neural baselines with strong zero-shot generalization.

## Strengths

- **SVD-based initialization with theoretical grounding and strong empirical gains.** Section 4.1 provides a clean formal definition (Definition 1) of asymmetry-aware embeddings and proves that the SVD construction satisfies it. Ablations (Table 6) show this component reduces the ATSP100 gap from 2.08% to 1.19% relative to random initialization, and Figure 2 demonstrates consistent improvements over alternative initialization methods (ICAM, RRNCO, UniCO) across both in-distribution and out-of-distribution sizes.

- **Sinkhorn normalization yields substantial and consistent performance improvements.** Table 6 shows that adding Sinkhorn on top of SVD further reduces the ATSP100 gap from 1.19% to 0.72%, with improvements persisting across all tested sizes (100–1000). Appendix D.5 also reports faster convergence compared to softmax, providing direct evidence beyond final performance.

- **State-of-the-art results on asymmetric synthetic benchmarks with strong zero-shot generalization.** In Table 1, RADAR achieves the lowest gaps among learning-based methods on ATSP (0.72% on 100 nodes, 1.01% on 200, 2.13% on 500) and ACVRP (1.64% on 100, −0.75% on 200). It maintains gaps under 4.2% when generalizing zero-shot to ATSP1000 without fine-tuning, substantially outperforming all neural baselines (next best: ReLD at 13.39%, ELG at 10.74%).

- **Convincing real-world validation against strong baselines.** Table 3 shows RADAR outperforms both MatNet and RRNCO across three real-world tasks (ATSP, ACVRP, ACVRPTW) under in-distribution, out-of-distribution city, and out-of-distribution cluster settings. The gap reductions are consistent and non-trivial (e.g., ATSP in-distribution gap: RRNCO 1.80% → RADAR 0.74%).

- **Well-designed analysis of coordinates vs. distance matrices (Section 5.4).** Table 4 cleanly demonstrates that RADAR without coordinates still outperforms RRNCO with coordinates plus augmentation, isolating the effectiveness of the SVD-based distance embedding and showing that coordinates mainly provide augmentation diversity in asymmetric settings.

- **Robustness across varying asymmetry levels (Section 5.5).** Table 5 systematically compares initialization strategies under controlled asymmetry levels; RADAR's informed embedding degrades gracefully while uninformed methods (MatNet, UniCO) exhibit sharp performance collapses at high asymmetry.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The multi-task experiment (Section 5.2) compares only against ablated versions of the same RouteFinder framework (RF, RF-NN) rather than against existing asymmetric-capable neural solvers.** While Table 1 and Table 3 already establish SOTA against MatNet, RRNCO, ReLD, etc., the multi-task comparison would be strengthened by including at least one of these methods under the same training protocol. As it stands, Table 2 primarily demonstrates that RADAR improves over the RouteFinder base architecture across 16 variants—a useful but narrower claim than "consistently outperforms state-of-the-art baselines" in this specific setting. The authors should either add such a comparison or reframe the claim to reflect that this experiment validates generalization across variants, with competitive SOTA evidence coming from the other tables.

- **The connection between Sinkhorn normalization and "dynamic asymmetry" is motivated intuitively but not directly validated.** The paper hypothesizes that Sinkhorn captures dynamic asymmetry because joint row-column normalization makes attention scores aware of both interacting nodes' neighborhoods (Section 4.2). The ablation (Table 6) and convergence analysis (Appendix D.5) show that Sinkhorn empirically helps, but no analysis directly examines whether attention weights become more directionally sensitive (e.g., measuring |A_ij − A_ji| with Sinkhorn vs. softmax, or correlating attention asymmetry with cost asymmetry). This leaves the "dynamic asymmetry" framing as a plausible intuition rather than a verified mechanism. The paper would be strengthened by even a simple diagnostic plot of attention asymmetry under the two normalizations.

- **No discussion of the scalability of SVD computation for very large instances (n > 10,000).** The paper evaluates on sizes up to 1000 and provides runtime profiling (Figure 4, Appendix D.4), but SVD on a dense n×n matrix has O(n² · k) cost with standard truncated SVD, and the paper does not discuss when this might become a bottleneck or how it compares to methods using local neighborhood sampling (e.g., ICAM's k-NN, RRNCO's probabilistic sampling). A brief limitations paragraph would improve the paper's credibility.

- **The informed/uninformed classification in Table 5 could be clearer.** RRNCO is listed as "uninformed" (†) despite using distance-based probabilistic sampling in its original formulation (as the paper itself notes in Section 4.1). The text explains that "single-embedding variants without coordinate inputs" are used to isolate initialization effects, but it is not explicitly stated that the RRNCO variant tested strips out its distance-based initialization. While the classification is justified by the experimental design, a reader could reasonably be confused. Making the experimental setup for each baseline explicit (e.g., "RRNCO variant using random initialization") would avoid this.

### Trivial

- The paper uses the symbol "†" in Table 1 to denote checkpoints (evaluation with authors' official checkpoints) and in Table 5 to denote uninformed initialization. These different uses of the same symbol across tables could be confusing but are not harmful.

## Nice-to-Haves

- **Per-variant breakdown of multi-task results in the main text.** The paper references Table 8 (appendix) for detailed results across the 16 variants. Including a concise summary in the main text (e.g., best and worst variants for each method) would improve transparency, though the appendix is likely sufficient for the camera-ready.

- **Direct analysis of whether the asymmetry-aware property of SVD embeddings persists after encoder layers.** Definition 1 guarantees the initial embeddings are asymmetry-aware, but it would be illuminating to check reconstruction error of the original distance matrix from final-layer embeddings to see if this property is preserved or enhanced through the encoder.

- **Runtime breakdown for Sinkhorn normalization in the main text.** The appendix contains this (Figure 4); a summary sentence (e.g., "Sinkhorn adds <5% overhead on n=500") would help readers assess the practical trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"RRNCO classification inconsistency"** (Harsh Critic, Section 5.5 notes). The critic claimed RRNCO should be "informed" not "uninformed" in Table 5. However, the paper explicitly states: "For RRNCO and ICAM, we use single-embedding variants without coordinate inputs to isolate initialization effects." The critic missed this methodological clarification. REMOVED.

- **"Formatting of Table 1 is difficult to parse"** (Harsh Critic). This is a parser artifact, not a paper flaw. REMOVED.

- **"Plots are only in the appendix"** (Harsh Critic, Section 6). The paper references the appendix for detailed plots; this is standard practice for managing space. REMOVED (moved to Nice-to-Haves).

- **Strength: "Comprehensive multitask evaluation on 16 asymmetric VRP variants"** (Strength Finder). While the evaluation breadth is a strength, it is tempered by the baseline limitation (RF/RF-NN only). The strength is retained but contextualized as demonstrating breadth, not necessarily superiority over all existing methods in that setting.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add at least one external neural baseline (e.g., ReLD or RRNCO) to the multi-task comparison** (Table 2), or clearly reframe the claim from "SOTA across many variants" to "validates generalizability across variants, with competitive SOTA established in Tables 1 and 3."
- **Include a brief diagnostic of attention asymmetry** (e.g., mean |A_ij − A_ji| under Sinkhorn vs. softmax) to support the dynamic asymmetry narrative, even as a small table or figure.
- **Add a limitations paragraph** discussing SVD cost for n > 10k and potential mitigation strategies (e.g., randomized SVD, which the paper already uses, or sparse approximations).
- **Clarify the experimental setup for RRNCO and ICAM in Table 5** by stating explicitly which initialization variant is used (e.g., "random embedding variant" rather than just "single-embedding variant without coordinates").

## Score and Decision

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>