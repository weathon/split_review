Now I'll compose the final consolidated review.

---

## Summary

This paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. The method has three main pillars: (1) a weighted cross-attention (WeCA) mechanism that incorporates compatibility coefficients outside the softmax so that task-pool suitability is preserved without depending on the number of pools or task types; (2) a longest-directed-distance GNN (LDDGNN) to capture task dependencies; and (3) a theoretical analysis of the optimality gap in list scheduling, together with a skip-action mechanism designed to close this gap under single-pass inference. Empirical results on TPC-H and Computation Graphs benchmarks show consistent makespan improvements over heuristics (HEFT, Tetris) and neural baselines (One-Shot, PPO-BiHyb).

---

## Strengths

1. **Weighted cross-attention with outside-softmax placement is a clean design for heterogeneous task-pool compatibility.** The WeCA layer multiplies the attention output by a diagonal matrix of compatibility coefficients *after* softmax normalization, rather than integrating them inside the log-softmax. This avoids the normalization effect that would wash out per-task compatibility differences. The two-task example in Section 3.1 is illustrative, and the ablation in Table 3 confirms the point: WeCA-outside + LDDGNN achieves 19,908 makespan on TPC-H-30 vs. 20,729 for WeCA-inside + LDDGNN (a 3.5% gap). The design is architecturally elegant and lets the same network handle varying numbers of pools and task types without fixed-size embeddings.

2. **Theoretical characterization of the list-scheduling optimality gap and a principled skip-action framework.** Section 4 formally identifies that list scheduling's generation map S_list is not surjective onto the optimal solution space (it fails for cases with heavy tasks). Theorem 1 and Theorem 2 prove that introducing skip actions enables the generation map to become surjective while retaining single-pass inference, and Theorem 1(iv) establishes that, in principle, there exist scores that allow greedy selection to recover an optimal solution. This provides a theoretically grounded motivation for the skip mechanism that goes beyond ad-hoc reasoning.

3. **Strong empirical performance across two benchmark families.** Tables 1 and 2 show that WeCAN-S(256) achieves the lowest makespan in all six dataset×size settings. On TPC-H-100, makespan is 61,373 vs. 66,173 for the best neural baseline One-Shot-S(256) (7.3% improvement), with greedy inference in 1.72s (vs. 179s for PPO-BiHyb). On Computation Graphs (Erdős-Rényi), WeCAN-S(256) achieves 10,083 vs. 11,071 for One-Shot (8.9%). These gains are consistent and statistically significant, with low variance across random seeds.

4. **Evidence of generalization to environment shifts.** Figure 2 tests models trained on a fixed TPC-H-30 distribution and evaluated under changes to pool count, pool type, task count, and task type. WeCAN-S(256) maintains a 20.4% improvement over best heuristics under "more pool" conditions, compared to 9.2% for One-Shot-S(256). This directly supports the claim that the WeCA design preserves adaptability across heterogeneous environment sizes.

5. **Systematic ablation isolating component contributions.** Table 3 compares seven architectural variants, confirming that removing WeCA layers degrades performance (e.g., WeCA-final-only + LDDGNN yields -4.2% relative to Tetris on TPC-H-50), and that LDDGNN outperforms standard GAT variants. This helps establish that the reported gains come from the proposed components rather than from general architectural capacity.

---

## Weaknesses

### Fatal
None.

### Major

1. **The heavy-task ablation confounds the skip-action evaluation with architectural changes.** The paper's central claim about skip actions is that they close the optimality gap and improve performance on heavy tasks. However, the experiment in Figure 3 compares WeCAN-S(256) (WeCA-outside + skip) against WeCAN-inside-S(256) (WeCA-inside, which the paper calls the "non-skipping variant"). Since WeCA-inside already underperforms WeCA-outside even on standard tasks (Table 3: 20,729 vs. 19,908 on TPC-H-30), the observed gap on heavy tasks conflates two differences: the skip-action mechanism *and* the WeCA coefficient placement. Without a direct ablation — WeCAN-S(256) with skip vs. the same architecture with the skip action masked — the paper cannot attribute the gain to skip specifically. This weakens the empirical support for contribution (3), which is one of the paper's two main technical claims. The issue is addressable (a controlled ablation would resolve it) but as written, the evidence for skip's benefit is incomplete.

2. **The skip-score functional form is introduced without justification or comparison.** The score \(u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c\) is a specific parametric choice. The paper states it "prevents the skip action from overly prioritized" and "clusters poor solutions in the high-\(u_a\), high-\(u_c\) region," but provides no analysis of why this particular form (an exponential decay modulated by learned exponents) was chosen, no comparison with alternatives (e.g., a learned MLP that directly outputs the score, a constant bias, or a simpler linear decay), and no sensitivity analysis. The theoretical map \(S_n\) described in Section 4 is distinct from the actual implemented mechanism, and the connection between them is not rigorously established. While this does not invalidate the method, it reduces the paper's scientific rigor.

### Minor

1. **Reproducibility of the heavy-task experiments is limited.** The paper says heavy tasks are created by "randomly replacing 1% of tasks with 'heavy tasks'" but does not specify quantitative properties (e.g., how much larger the processing time or resource demand is, or whether "heavy" means a fixed multiplier or a distribution). The number of random seeds, whether the replacement is done once globally or per trial, and the precise pool-resource configurations are not reported. These details are necessary for reproduction.

2. **Figure 3 appears mislabeled.** The figure caption lists "WeCAN-S(256)" as both the first (blue) and fourth (green) bar, which is confusing. It appears the green bar may be a different variant (possibly a no-skip WeCAN-outside), but this is not clearly explained. The paper text calls WeCAN-inside-S(256) the "non-skipping variant," but the figure legend and the caption should be reconciled.

3. **The paper does not empirically verify that the trained policy realizes the theoretical guarantee of Theorem 1.** Theorem 1(iv) shows *existence* of scores that would allow optimal greedy solutions, but the experiments do not measure whether the learned policy assigns non-negligible probability to optimal or near-optimal solutions. A simple check — e.g., computing the fraction of greedy/sampling solutions that match or beat the best MILP-derived lower bound on small instances — would strengthen the link between theory and practice.

### Trivial

- The paper's reference to "Appendix A," "Appendix B," "Appendix C," etc., is a consequence of the PDF-to-text parsing; these would be present in the original submission.
- Figure 1's description appears three times in the text (a parsing artifact).

---

## Nice-to-Haves

- A comparison with an auto-regressive decoder baseline (the paper refers to Appendix B, which was stripped).
- A controlled variation of heavy-task proportion (e.g., 0%, 1%, 5%, 10%) comparing skip vs. no-skip makespan on the same architecture.
- A visualization of when skip actions are actually used in a solved instance (frequency, timing) to validate that the learned policy uses skip appropriately.

---

## Removed Points

The following points from the harsh critic are removed with justification:

- **"The proof is relegated to Appendix A (stripped)"** and similar remarks about missing appendices — The parser strips appendix sections from all papers; they exist in the original submission. Per hard rules, criticisms about missing appendix content are removed.
- **"No comparison with an auto-regressive decoder is provided (the paper says 'comparison in Appendix B,' which is stripped)"** — Same reason: appendix-removal artifact.
- **"The generation map's loop remains, so inference time is still dominated by the map, not the network"** — The paper already addresses this in Section 5.2 ("the generation map's runtime dominates for both WeCAN and One-Shot"), so this is not a weakness.
- **"One‑Shot already achieves single‑pass scheduling without skip"** — The paper acknowledges this and explicitly states that One-Shot does not handle compatibility coefficients or pool allocation. The contribution is not single-pass scheduling per se, but single-pass scheduling *in heterogeneous environments with compatibility constraints*.
- **Strength Finder's claim that Figure 3 "validates" the skip action** — This conflates the same confound described above. The strength of the theoretical framing is kept, but the validation claim is removed.
- **Generic strengths from the Strength Finder** ("the problem is important," "the paper addresses a challenging problem") — These are superficial and add no specific evidence; removed.

---

## Novel Insights

The most valuable insight from this set of reviews is the identification of the confound in the skip-action ablation (Major Weakness 1). The reviewers independently identified that Figure 3 compares architectures differing in *two* respects (WeCA placement and skip action), making it impossible to attribute the improvement to skip alone. This is an unusually sharp methodological observation that would genuinely help the authors improve the paper. The second insightful observation is the tension between the existential nature of Theorem 1 (it proves existence of scores for optimal solutions) and the empirical evaluation (which does not verify that the learned network actually realizes such scores). This gap between theory and practice is common but worth flagging.

---

## Suggestions

1. **Add a direct skip vs. no-skip ablation.** Keep the architecture (WeCA-outside + LDDGNN) fixed and compare inference with vs. without the skip action (mask the skip action always in the no-skip variant). Report this on both standard and heavy-task variants of TPC-H.
2. **Quantify heavy-task properties.** Specify the multiplier or distribution for heavy-task processing time and resource demand.
3. **Fix Figure 3 labeling.** Ensure the legend clearly distinguishes all variants and matches the description in the caption.
4. **Add a justification or sensitivity analysis for the skip-score formula.** Show that alternative forms (linear decay, learned MLP) perform similarly or worse, or provide a principled derivation.
5. **Add a small-scale optimality verification.** Solve small random DAGs with MILP and compare WeCAN's greedy/sampling solutions to the true optimum, checking whether Theorem 1(iv) is realized in practice.

---

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison to This Paper |
|---|---|---|
| `/home/.../jsWCmrsHHs.md` (JSSP improvement heuristic) | 7.50 | Stronger: cleaner ablation design, more comprehensive baselines. This paper has broader scope (heterogeneous environments) and theory but weaker experimental validation of one key component. |
| `/home/.../jBYQAtzp5Z.md` (Scheduling with predictions) | 6.80 | Comparable: both have theoretical contributions and empirical validation. That paper's theory is tighter (competitive ratios), while this paper's experiments cover more diverse settings. |
| `/home/.../AEFVa6VMu1.md` (Approximation with predictions) | 7.50 | Stronger: cleaner theoretical framing, broader problem scope. This paper has more practical empirical evaluation on real-world datasets. |
| `/home/.../6hvtSLkKeZ.md` (Bin packing encoder-decoder) | 6.40 | Comparable: both propose neural architectures for CO variants with good empirical results. This paper has stronger theoretical grounding. |
| `/home/.../yEwakMNIex.md` (Unified neural TSP solvers) | 6.25 | Comparable: both have interesting ideas but some methodological gaps. This paper is more focused and has cleaner experimental design overall (except the skip confound). |
| `/home/.../CFLEIeX7iK.md` (Neural solver selection) | 5.75 | Weaker: limited novelty, thin experiments. This paper has more substantive contributions (architecture + theory). |
| `/home/.../b9aCXHhdbv.md` (Pipeline parallelism DRL) | 4.50 | Weaker: missing experimental details, unclear contributions. This paper is significantly stronger despite the highlighted weakness. |
| `/home/.../bntJK4NyIW.md` (Decentralized training) | 2.00 | Weaker: serious flaws, unclear novelty. This paper is in a different quality tier. |

The paper has genuine contributions — a novel architecture (WeCA outside-softmax), a theoretical framework for the optimality gap, strong empirical results on two benchmarks, and demonstrated generalization — all of which are well above the acceptance threshold for a venue like ICLR. The major weakness is the confounded skip-action ablation, which is real but addressable; it does not undermine the core results (Tables 1 and 2), which demonstrate the full system's superiority regardless of whether skip's individual contribution can be isolated. Positioned relative to the calibration anchors, this paper sits above the 5.75 rejected papers and in the lower part of the accepted range (6.0–6.5).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>