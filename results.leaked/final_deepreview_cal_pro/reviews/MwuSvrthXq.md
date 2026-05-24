Now let me produce the final review.

---

## Summary

WeCAN proposes an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task–resource compatibility coefficients. The key architectural innovations are (1) a weighted cross-attention (WeCA) layer that places compatibility coefficients outside the softmax to capture global compatibility while maintaining adaptability across variable numbers of pools and task types, (2) a longest-directed-distance GNN (LDDGNN) for encoding DAG dependencies, and (3) a single-pass skip-action mechanism that theoretically closes the optimality gap inherent in list scheduling. The method achieves fast, single-pass inference and demonstrates substantial makespan improvements over both classical heuristics (HEFT, Tetris) and two neural baselines (PPO-BiHyb, One-Shot) on TPC-H and Computation Graphs benchmarks.

## Strengths

- **Well-motivated architectural design with strong ablation support**: The WeCA layer's outside-softmax placement of compatibility coefficients is cleanly motivated (Section 3.1), and the ablation in Table 3 convincingly demonstrates its importance — replacing outside placement with inside placement degrades makespan by 3.5–4.5 percentage points, while limiting WeCA to decoder-only layers costs up to 9.1 points. The LDDGNN similarly outperforms forward and bidirectional GAT variants. These are specific, verifiable design contributions.

- **Substantial and consistent empirical gains over heuristics**: On TPC-H-30/50/100, WeCAN-S(256) achieves 14.0–18.1% makespan improvement over the best heuristic (Tetris), with single-pass greedy inference times as low as 0.15s (Table 1). On Computation Graphs, improvements range from 9.9–13.4% across three graph types (Table 2). The gains are large, reported with standard deviations, and consistent across problem sizes and graph structures.

- **Strong generalization evidence**: Figure 2 shows WeCAN maintains or improves its advantage over One-Shot when evaluated under environment shifts (more pools, different pool types, more tasks, different task types) without retraining. This directly supports the claimed adaptability of the architecture.

- **Theoretical analysis of the optimality gap**: Section 4 provides a formal framework (spaces A, B, maps T, S, Assumption 1, Theorem 2) for analyzing when a generation map can represent optimal solutions, and Theorem 1 guarantees that the skip-augmented algorithm can represent optimal solutions that pure list scheduling cannot. This adds depth beyond a purely empirical contribution.

- **Computational efficiency is a genuine practical strength**: The single-pass design yields inference times (0.15–1.72s for greedy, 2.43–10.43s for S(256)) that are comparable to heuristics and orders of magnitude faster than PPO-BiHyb (20–179s), making the method viable for time-sensitive applications.

## Weaknesses

### Major

- **One-Shot baseline adaptation is undocumented in the main text**: One-Shot (Jeon et al., 2023) was designed for homogeneous scheduling and does not natively handle compatibility coefficients or heterogeneous pool allocation. The main text provides no description of how it was extended for the heterogeneous setting used in Tables 1–2. The paper acknowledges the gap (lines 60–64: "their architecture does not consider compatibility coefficients or pool allocation"), but the reader cannot assess whether the reported 7.7–9.5% improvement over One-Shot reflects a fair comparison or a poorly adapted baseline. The gains over heuristics (HEFT, Tetris) remain independently convincing, so the overall contribution is not invalidated, but the state-of-the-art neural comparison is compromised.

- **Skip-action benefit demonstrated only on artificial heavy-task variants, not on standard benchmarks**: The skip action is presented as one of three main contributions and is supported by theoretical analysis (Section 4, Theorem 1). However, its practical benefit is evaluated only on TPC-H datasets where 1% of tasks are artificially replaced with "heavy tasks" (Figure 3). On the standard benchmarks where the method's main results are reported (Tables 1–2), the skip-action component is never ablated. The paper itself acknowledges that the optimality gap matters most for heavy-task cases (lines 205–206), but the reader does not know whether skip helps, hurts, or is neutral for typical heterogeneous instances. The theoretical contribution stands, but the claimed practical value of skip for general scheduling problems is not supported by the evidence presented.

### Minor

- **Narrow neural baseline coverage**: Only two neural baselines are compared: PPO-BiHyb (which is orders of magnitude slower and represents a different regime) and One-Shot. The related-work section cites several recent heterogeneous neural schedulers (Zhou et al., 2022; Zhadan et al., 2023; Wang et al., 2025) that are not compared against. Including at least one additional recent heterogeneous scheduler would strengthen confidence that WeCAN's gains are architectural rather than an artifact of baseline selection.

- **Unsubstantiated clustering claim in Section 4**: The paper states that the skip-score parameterization "clusters most poor solutions in the high-u_a, high-u_c region" and that "this concentration makes such regions easier to handle during training and reduces variance" (lines 213–214). This claim is presented as a design property but is supported by neither theoretical analysis nor empirical evidence. It should be either substantiated or clearly labeled as design intuition.

- **"Up to 18.1%" improvement reporting**: The abstract and Section 5.2 report "up to 18.1%" improvement, which is standard phrasing but obscures whether this represents a typical gain or an outlier. Reporting the average improvement across the test set would be more informative and is already partially available from the tables.

### Trivial

- The skip score formula (Equation for u_{π_skip} in Section 3.2) is presented without much justification for why the specific functional form — a power-law decay with step count — is chosen over alternatives. A brief rationale would aid readability.

## Nice-to-Haves

- **Skip ablation on standard benchmarks**: Training and evaluating WeCAN with skip disabled (e.g., u_a = 0) on the standard TPC-H and Computation Graphs settings would directly quantify skip's contribution beyond the heavy-task corner case. Even a null result would be informative.

- **Additional heterogeneous neural baseline**: Including a recent method such as Zhou et al. (2022) or Zhadan et al. (2023) would strengthen the neural comparison and situate WeCAN more precisely within the literature.

- **Analysis of skip-action usage frequency**: Reporting how often the skip action is actually selected during evaluation (on both standard and heavy-task instances) would give tangible insight into when the mechanism activates in practice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic's claim that the paper "hints at" averaging coefficients for One-Shot*: This is a misreading. The text about averaging coefficients (line 73) refers to Zhou et al. (2022), not to the One-Shot adaptation. The actual adaptation of One-Shot is simply undocumented, not misleadingly described. **Removed as factually incorrect.**

- *Harsh critic's claim that "the phrase 'closes the optimality gap' suggests a stronger practical guarantee than the existence result provided"*: The abstract says "addressing this gap" and the introduction says "theoretically closes this gap," which is appropriately qualified given Theorem 1. **Removed as overly pedantic.**

- *Harsh critic's note about missing proof sketch for Theorem 1*: The paper defers proofs to Appendix A (which is standard practice), and Theorem 1 is stated clearly with all four parts. **Removed as a formatting nitpick about appendix placement.**

- *Harsh critic's demand for statistical significance tests*: The reported standard deviations are tight relative to effect sizes (e.g., WeCAN-S(256): 18964 ± 10 vs. One-Shot-S(256): 20399 ± 181 on TPC-H-30), making formal tests unnecessary. Single-run evaluation with variance reporting is standard in this subfield. **Removed as a methodological demand not standard for the field.**

- *Strength Finder's generic strengths about "important problem" or "interesting question"*: These are generic. **Removed as superficial.**

## Novel Insights

None beyond the paper's own contributions. The theoretical framework connecting generation maps, surjectivity, and optimality representability (Section 4) is the most conceptually novel element, providing a criterion (Assumption 1, Theorem 2) that could be applied to analyze other scheduling formulations beyond this paper's specific setting.

## Suggestions

- Describe the One-Shot adaptation for heterogeneous scheduling explicitly in the main text or a dedicated appendix section, including pool-selection rules, how compatibility coefficients are incorporated, and any hyperparameter tuning performed.
- Ablate the skip action on the standard (non-heavy) benchmarks to establish its practical value or lack thereof beyond the heavy-task corner case. Even a negative result would appropriately scope the contribution.
- Consider adding one additional heterogeneous neural scheduler as a baseline to broaden the comparison.

## Score and Decision

**Anchor comparison summary**:
| Anchor ID | Avg Score | Round | Comparison to WeCAN |
|-----------|----------|-------|---------------------|
| `10eQ4Cfh8p` (FJSP RL) | 3.00 | R1 | WeCAN is substantially stronger in methodology, theory, and empirical evidence |
| `6hvtSLkKeZ` (Bin packing encoder-decoder) | 6.40 | R1/R2 | WeCAN is stronger: better ablation, theoretical depth, clearer empirical gains |
| `yEwakMNIex` (RedCO, unified CO solver) | 6.25 | R2 | WeCAN is stronger: more focused contribution, better empirical support |
| `GM7cmQfk2F` (Neat Weight Embedding MOCO) | 7.00 | R2 | WeCAN is slightly weaker: similar architectural innovation quality but with evaluation gaps (undocumented baseline adaptation, skip only on corner cases) |
| `jBYQAtzp5Z` (Fair scheduling with predictions) | 6.80 | R1 | Different subfield (theoretical CS); WeCAN's empirical contribution is strong but evaluation gaps bring it slightly below |

**Round 1 bracket**: 5.5 – 7.0. **Round 2 narrows to**: 6.0 – 6.5. The paper is stronger than the 6.25–6.40 anchors but has evaluation gaps that prevent it from reaching the 7.0 level. Final score: **6.5**.

**Evaluation dimensions**: 
- *Originality*: Good — the WeCA design and single-pass skip mechanism are novel in heterogeneous DAG scheduling.
- *Importance*: Solid — heterogeneous scheduling with compatibility coefficients is a real and challenging problem.
- *Claims supported*: Mostly — architectural claims are well-supported by ablation; skip-action practical claims are overextended relative to evidence.
- *Soundness*: Good — the method is sound and the experiments are generally well-executed.
- *Clarity*: Good — the architecture, algorithm, and theory are described clearly.
- *Value to community*: Solid — the WeCA design and theoretical framework have transferable value.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>