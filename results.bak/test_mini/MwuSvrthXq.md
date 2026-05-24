Now I have a thorough understanding of the paper and the calibration. Let me write the final review.

## Summary

This paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility constraints. The core technical contributions are: (1) a **weighted cross-attention (WeCA)** mechanism that embeds compatibility coefficients outside the softmax, enabling variable-sized heterogeneous environments without fixed-dimensional encodings; (2) a **skip-action mechanism** in the single-pass setting that theoretically closes the optimality gap of list scheduling; and (3) a longest-directed-distance GNN (LDDGNN) for encoding task dependencies. Experiments on TPC-H and Computation Graphs benchmarks show up to 18.1% makespan improvement over the best heuristics and up to 9.5% over neural baselines, with inference times comparable to heuristics.

## Strengths

1. **Weighted cross-attention is a well-motivated, novel architectural contribution.** The WeCA layer (Eq. 3, Section 3.1) places compatibility coefficients outside softmax as a diagonal weight matrix, allowing the network to distinguish tasks with identical attributes but different compatibility profiles across pools. The ablation study (Table 3) cleanly isolates this: replacing WeCA with an inside-softmax variant degrades improvement from 14.0% to 10.5%, and removing WeCA entirely collapses to near-baseline performance (0.5% improvement).

2. **Strong and consistent empirical results.** WeCAN-S(256) outperforms the best heuristic (Tetris) by 14.0–18.1% on TPC-H and 9.5–13.4% on Computation Graphs, and outperforms the best neural baseline (One-Shot-S(256)) by 4.7–9.5% across all settings. Gains are reported with standard deviations over random seeds and are consistent across problem sizes (30–100 query variants, 500-task graphs).

3. **Generalization experiments demonstrate a concrete advantage of the architecture.** Figure 2 shows WeCAN maintains 14–20% improvement over best heuristics under environment fluctuations (pool count, pool type, task count, task type) without retraining, while One-Shot degrades to 0.9–10.2%. This directly validates the paper's claim that WeCA preserves adaptability across varying heterogeneous configurations — a non-trivial result.

4. **Comprehensive ablation study.** Table 3 systematically ablates both the WeCA placement (inside, decoder-only, decoder-inside, final-only) and the GNN component (GAT forward, GAT bidirectional), controlling for layer count and hidden dimensions. This gives high confidence that both WeCA and LDDGNN contribute meaningfully.

5. **Single-pass speed is competitive with heuristics.** WeCAN-Greedy runs in 0.15s on TPC-H-30 vs. heuristics 0.18–0.30s, while the multi-round PPO-BiHyb takes 20.48s. This supports the claimed efficiency advantage of single-pass network inference.

## Weaknesses

### Fatal

None.

### Major

1. **Missing comparison to the most closely related heterogeneous scheduling methods.** The paper cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) as methods that handle compatibility coefficients in heterogeneous DAG scheduling (Section 1, lines 69–76), noting that they "represent compatibility coefficients by averaging them across pools, potentially losing fine-grained information." These are precisely the baselines that would most directly validate the advantage of weighted cross-attention over existing approaches, yet none are included in the experiments (Section 5.1 lists six heuristic/algorithmic baselines and two neural baselines — PPO-BiHyb from 2021 and One-Shot from 2023, the latter designed for homogeneous settings). The paper's central claim of "outperforming state-of-the-art methods" (Abstract) is therefore not fully supported by the evidence presented. This gap is structural: the evaluation protocol compares against methods that are either dated (PPO-BiHyb, 2021) or mismatched to the task (One-Shot does not handle compatibility), while the methods that specifically address the paper's problem setting are discussed but not evaluated. This weakness does not invalidate the results against the included baselines, but it substantially tempers the strength of the claims that can be drawn.

### Minor

2. **The skip-score formula and clustering claim lack main-text justification.** The skip score $u_{\pi_{\text{skip}}} = u_a(1 - k/2n)^{u_b} + u_c$ (Section 3.2, line 148) is presented without explanation of why this particular parametric form was chosen (e.g., monotonicity in $k$, boundedness, or other desirable properties). Furthermore, Section 4.2 claims that the skip-action design "clusters most poor solutions in the high-$u_a$, high-$u_c$ region" — this is stated without formal analysis or empirical support in the main text. Theorem 1 and Theorem 2 establish existence results, but the gap between "there exists a score that works" and "this specific learned formula achieves it" is not bridged in the main text. The heavy-task experiment (Figure 3) provides empirical evidence that skip helps, which partially addresses this, but the theoretical framing over-promises relative to what is demonstrated.

3. **Only one heavy-task rate (1%) is tested in the skip-action ablation.** The heavy-task experiment (Figure 3) replaces 1% of tasks with heavy tasks. A sensitivity study varying this rate (e.g., 0.5%, 1%, 2%, 5%) would more convincingly validate the claim that skip's benefit grows with heavy-task proportion. The current single-point result is suggestive but thin.

### Trivial

None.

## Nice-to-Haves

- A comparison to Zhou et al. (2022), Zhadan et al. (2023), or Wang et al. (2025) would be the single most impactful addition. Even reporting their published results on similar datasets or adapting public code would substantially strengthen the evaluation.
- A sensitivity analysis on the heavy-task proportion (varying the replacement rate) would strengthen the empirical support for the skip-action analysis.
- Providing per-instance statistics (mean and std over test instances, rather than over seeds only) would give a clearer picture of variance across problems.
- A brief justification of the skip-score functional form in the main text (e.g., why the $(1 - k/2n)^{u_b}$ structure) would improve readability.

## Removed Points

The following points from the harsh critic were removed per the filtering rules:

- **"The proof is relegated to an appendix that is not available in the main paper."** — Removed. The parser strips appendix content from all papers; the proof exists in the original submission. This is a parser artifact, not an author error.
- **"Critical experimental details are deferred to an appendix that is not present"** (network architecture, hyperparameters, dataset generation details). — Removed. These are standard appendix contents, and the parser strips them from all papers.
- **"Figure 1 caption says LDDNN (Long Short-Term Memory Network) but the text uses LDDGNN."** — Removed. The text "LDDNN (Long Short-Term Memory Network)" appears only in the OCR-extracted figure alt text, which is a parser artifact from the embedded image. The paper's actual text consistently uses LDDGNN and defines it correctly as "Longest Directed Distance based Graph Neural Network."
- **Criticisms about missing related works, missing appendices, or missing references.** — Removed per the hard rules.
- **Generic concerns about "evaluation lacking rigor" without specific anchors.** — Removed as they were category-driven noise rather than concrete, verifiable problems.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives largely converge — the core methodological contributions (WeCA, skip-action) are genuinely novel and well-evaluated in isolation, but the experimental comparison is incomplete for the strength of claims made. The best insight from the synthesis is that the missing-baselines gap is structural (the paper compares against methods not designed for its setting while omitting methods that are) rather than incidental, which usefully frames the most critical revision target.

## Suggestions

1. **Add the missing heterogeneous-scheduling baselines.** Even approximate comparisons using published results on similar datasets would significantly strengthen the paper's evaluation. If code is not available, clearly state this and reframe claims from "outperforming state-of-the-art methods" to "outperforming the baselines tested."
2. **Provide main-text intuition for the skip-score formula.** A short paragraph explaining why the $(1 - k/2n)^{u_b}$ term prevents excessive skipping (it decays towards zero as $k$ approaches $2n$, making skip less attractive later in scheduling) would help readers evaluate the design.
3. **Run a heavy-task proportion sweep** (0.5%, 1%, 2%, 5%) to demonstrate the trend predicted by the theoretical analysis.
4. **Tone down the "SOTA" claim** or qualify it explicitly as "SOTA among the methods compared" unless the missing baselines are added.

## Score and Decision

**Calibration anchors consulted:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| GAA-PtrNet (UbWy2QVmke) | 4.50 | R1 | Worse: similar missing-baselines issue but significantly less novelty (incremental GNN+P trNet) and weaker ablation |
| DEFT (yVFOdLjd7V) | 5.00 | R1, R2 | Similar: accepted poster, weaker ablations, less novel (MoE application), but stronger on baseline comparisons |
| RESCHED (s5pWbwf2tk) | 5.00 | R1, R2 | Similar: accepted poster, comparable ablation quality, but training data comparison concerns |
| Multi-Obj FJSP (YAgOaYedLQ) | 5.50 | R2 | Similar: accepted poster, weaker novelty (DAN extension), missing ablation |
| Found. Models Industrial Sched (qRjLjYrvMi) | 6.00 | R2 | Stronger in breadth of experiments but rejected due to missing DAG context — a more fundamental flaw |
| Scheduling low-band papers | 2.0–3.0 | R1 | Clearly worse: basic methodology, limited results, no novel architecture |

**Round 1 bracket:** 4.5–7.0 (between GAA-PtrNet and high-quality/out-of-area papers).

**Round 2 narrowing:** Compared to accepted posters at 5.0–5.5 (DEFT, RESCHED, Multi-Obj FJSP), this paper has stronger architectural novelty and better ablation studies but shares a common weakness pattern: incomplete baseline comparisons. The paper is better than GAA-PtrNet (4.50, Reject) which had less novelty and similar baseline gaps. It is slightly stronger than DEFT (5.00) and RESCHED (5.00) due to more novel contributions and cleaner ablation, but the missing-baselines issue prevents it from reaching the 6+ range.

**Final position:** 5.5 — comparable to accepted poster papers but with a notable evaluation gap that the authors should address in revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>