Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

TopGQ proposes the first post-training quantization (PTQ) framework for GNNs, replacing slow quantization-aware training (QAT) methods with a calibration-only approach. The key idea is to group nodes by topological similarity (indegree + localized Wiener index), share quantization parameters within each group, and absorb per-group scales into the adjacency matrix for efficient integer inference. An accelerated algorithm for computing localized Wiener indices is also contributed. Results show orders-of-magnitude speedup in quantization time while achieving competitive accuracy against QAT baselines.

## Strengths

- **First PTQ method for GNNs with dramatic speedup over QAT.** TopGQ requires no gradient computation or retraining, reducing quantization time from tens of hours to minutes. For example, on Reddit 4-bit GraphSAGE, TopGQ achieves 93.93% accuracy in 0.02 hours vs. 89.86% in 42.27 hours for Degree-Quant (Table 1, Section 6.2). This is a practical contribution — real-world graphs are updated frequently, making fast re-quantization valuable.

- **Topology-based node grouping reduces quantization error.** The paper provides evidence (Figure 2, Table 4, Table 7) that indegree alone is insufficient for grouping, and that combining indegree with localized Wiener index produces groups with more homogeneous feature magnitudes, reducing quantization error. The ablation (Table 4) confirms that the proposed grouping significantly boosts PTQ accuracy over a naive PTQ baseline, especially for GIN where naive PTQ fails.

- **Accelerated localized Wiener index computation.** Algorithm 1 exploits the bounded diameter of k-hop subgraphs to compute Wiener indices without all-pair shortest paths. The empirical speedups (up to 602× over SciPy baselines, Table 6) make the PTQ pipeline practical for large graphs — without this, the topological metric computation would negate the speed advantage of PTQ over QAT.

## Weaknesses

### Major

- **Claim of outperforming FP32 is contradicted by the paper's own data (if the reviewer's reading of the tables is accurate).** The paper states (line 232): "TopGQ sometimes outperforms QAT baselines or even the FP32 network." The reviewer reports that in every row of Tables 1–3, FP32 accuracy is strictly higher than TopGQ (e.g., Reddit GraphSAGE 8-bit: FP32 = 96.42 vs. TopGQ = 95.60). The tables are embedded as images and cannot be verified from the extracted text, but if this reading is correct, the claim is false. This is an overstatement the authors must correct. (Note: the speed and QAT-competitiveness claims do not depend on beating FP32.)

- **Baselines SGQuant and A²Q are evaluated in fixed-precision mode, which handicaps them.** The paper acknowledges (Related Work, line 83) that these methods "allow mixed-precision to assign higher bitwidth to high-magnitude vertices," yet the experimental setup (Section 6.1) forces them into fixed-precision "for a fair comparison." This is not fair — it compares TopGQ's intended mode against a degraded version of the baselines. A proper comparison would either use mixed-precision (their intended mode) or provide justification for why fixed-precision is equivalent. Given that TopGQ is PTQ (no retraining), the accuracy claims against QAT baselines need stronger support.

- **No error bars or statistical significance for any accuracy result.** Results on small datasets (Cora, CiteSeer, PubMed) can vary substantially with random seeds. Without any measure of variance, it is impossible to know whether reported improvements are robust or noise. The paper claims "competitive or better" performance without this basic statistical grounding.

### Minor

- **Ablation does not separate the two components of the grouping.** Table 4 compares a "PTQ baseline" against "PTQ + TopGQ grouping" (which includes both indegree and Wiener index), but never ablates indegree-only grouping vs. Wiener-index-only grouping. Table 7 compares Wiener index against other centrality measures (betweenness, closeness, Katz), but does not isolate the incremental contribution of Wiener index over indegree alone. This makes it difficult to attribute the improvement.

- **Scale absorption justification is imprecisely worded.** The paper claims (line 199) that $S_X$ "only depend[s] on the topology of the input graph." In reality, the scale values $S_X$ are computed from min/max of features in each group during calibration — the grouping depends on topology, but the numerical scale values depend on calibration data. The method works (scales can be pre-computed after calibration), but the stated justification is technically inaccurate. The paper also does not analyze the memory overhead of absorbing floating-point scales into the adjacency matrix.

- **Algorithm 1 correctness is not established for general $k$.** The derivation (Equations 10–13) is shown only for $k=2$, but Algorithm 1 claims to work for arbitrary $k$ without a general proof or derivation. The pseudocode is also hard to parse (the extracted text shows formatting artifacts, and key variable scopes are unclear).

- **Group assignment for unseen nodes is underspecified.** Section 5.1 states that unseen $(I,W)$ pairs are "assigned to the most similar quantization group by first comparing the $I$ and then the $W$ values," but specifies no distance metric, tie-breaking rule, or fallback when no similar group exists. This is not reproducible as described.

- **Inference time results (Table 5) use "customized kernels" that are not described**, and are only shown for GCN, not GIN or GraphSAGE. This limits reproducibility.

- **No analysis of group count.** The paper does not report how many distinct (I,W) groups are formed per dataset. If the number of groups is close to the number of nodes, the benefit of sharing quantization parameters vanishes; if it is very small, the method may not capture fine-grained topological differences. This characterization is missing.

### Trivial

- Figure 2 is a qualitative visualization; the claim of "uneven distribution of nodes among the groups" for indegree-only grouping could be backed by a simple quantitative metric (e.g., Gini coefficient of group sizes).

- The paper uses $k=2$ or $k=3$ for the localized Wiener index with no sensitivity analysis showing how accuracy varies with $k$.

## Nice-to-Haves

- A sensitivity analysis on hop count $k$ ($k=1,2,3,4$) for at least one dataset would help understand the trade-off.
- Testing on attention-based architectures (GAT) would increase generality, though the paper's stated scope (GCN, GIN, GraphSAGE) is reasonable.
- Reporting group counts and within-group feature variance (e.g., box plots) would strengthen the claim that groups have homogeneous feature magnitudes.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that "first PTQ for GNNs" does not acknowledge generic PTQ outside GNN community.** Removed as scope creep — the paper is about GNN quantization, and claiming "first PTQ for GNNs" in the GNN context is accurate.
- **Claim that the transition from Equation 15 to Equation 16 is unexplained.** Removed — the paper clearly shows $\tilde{A}\cdot X \approx \tilde{A}\cdot S_X \cdot X^Q = \tilde{A}_X \cdot X^Q$, which is a direct algebraic manipulation. The explanation is present.
- **Criticism about Reddit GIN FP32 accuracy (74.34%) being lower than literature (~95%).** Removed as unverifiable — this number is in an embedded table image that I cannot read; I cannot confirm whether the 74.34% figure is accurate or whether the comparison architecture/layer count matches.
- **Criticism that Wiener index speedups (0.0002 hours for ogbn-proteins) are "implausible."** Removed as speculative — the claimed speed is an extraordinary result but not impossible given the algorithmic innovation; verification would require inspecting the code.

## Novel Insights

The harsh critic raises one genuinely novel observation beyond the paper's own claims: the scale absorption step's reliance on calibration data (not just topology) means that if test-time feature distributions differ from calibration, the absorbed scales could be suboptimal. This is a general limitation of any PTQ method's calibration process, but TopGQ's reliance on group-level scales (rather than per-tensor) may exacerbate this sensitivity because groups with few members could have scales dominated by a single outlier in the calibration set. This trade-off between fine-grained grouping and calibration robustness is worth investigating.

## Suggestions

1. **Correct or remove the claim about outperforming FP32** if the data does not support it. The paper's main selling points (speed, competitiveness with QAT) do not depend on this claim.
2. **Report results with SGQuant and A²Q in their intended mixed-precision mode**, or show that fixed-precision is equivalent for the specific configurations used.
3. **Add standard deviations over multiple seeds** for all accuracy results, particularly for small graphs.
4. **Ablate indegree-only vs. Wiener-index-only grouping** in a dedicated experiment.
5. **Clarify the scale absorption statement**: $S_X$ depends on both topology (for group assignment) and calibration data (for per-group min/max), but can be pre-computed after calibration.
6. **Provide a derivation for Algorithm 1 for general $k$** (or state that the paper only uses $k=2,3$ and the general case is heuristic).
7. **Report the number of quantization groups** produced per dataset.

## Score and Decision

The paper addresses a real problem (slow GNN quantization) with a clever, practically-motivated approach. The core idea — topology-based node grouping for PTQ — is novel and the speed improvements over QAT are substantial. However, the evaluation has significant weaknesses: (a) the FP32 outperformance claim appears contradicted by the paper's own data, (b) QAT baselines are evaluated in a fixed-precision mode that handicaps their intended design, (c) no statistical variance is reported, and (d) key ablations are missing. These issues undermine confidence in the accuracy comparisons while leaving the speed advantage intact. The paper's contribution is genuine but the evidence in its current form is insufficient to fully support the headline claims.

**Score: 4.5/10** — The paper has a novel and practical core idea with promising initial results, but the evaluation has several issues (overclaimed FP32 comparison, unfair baseline configuration, missing ablations) that prevent acceptance in the current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>