Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper presents WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility constraints. The core technical contributions are: (1) a weighted cross-attention (WeCA) layer that places compatibility coefficients outside softmax, enabling the network to process variable numbers of pools and task types without fixed-size embeddings; (2) a longest directed distance GNN (LDDGNN) for encoding task dependencies; (3) a skip-action mechanism integrated into the single-pass generation map to address the optimality gap of list scheduling; and (4) empirical results on TPC-H and Computation Graphs benchmarks showing consistent makespan improvements over heuristics and older neural baselines.

## Strengths

- **Weighted cross-attention layer with outside-softmax compatibility bias (WeCA)**: Section 3.1 introduces an attention mechanism where compatibility coefficients act as multiplicative biases outside softmax (Equation 2), enabling the network to handle any number of pools and task types without fixed-size embeddings. Table 3 shows WeCA + LDDGNN outperforms WeCA-inside + LDDGNN by 3.7–4.7% on TPC-H-30/50. Figure 2 demonstrates that WeCAN maintains 6.7–20.4% improvement over heuristics under environment fluctuations (more pools, more task types, etc.), where One-Shot's improvement drops to as low as 0.9%.

- **Single-pass inference achieving heuristic-level runtimes**: Table 1 reports WeCAN-Greedy runtimes (0.15–1.72s) are within the same order as heuristics (0.18–3.35s) and orders of magnitude below PPO-BiHyb (20.48–179.19s), while WeCAN-S(256) makespan is 7.7–18.1% better than the best heuristic and 6.7–9.5% better than One-Shot-S(256). Tables 1 and 2 show consistent superiority across both benchmarks.

- **Systematic ablation isolating architectural components**: Table 3 systematically replaces WeCA (inside placement, decoder-only, final-only) and LDDGNN (GAT variants) while controlling layer count and dimensions. Every replacement increases makespan (e.g., WeCA-final-only drops to 0.5% improvement vs. 14.0% for the full model on TPC-H-30), confirming each component's necessity.

- **Generalization experiments under fixed training**: Figure 2 tests models trained on one environment and evaluated under four types of fluctuations (pool count, pool type, task count, task type). WeCAN retains 6.7–20.4% improvement over best heuristics while One-Shot drops to 0.9–10.2%, demonstrating that weighted cross-attention preserves adaptability to unseen environment configurations.

## Weaknesses

### Fatal
None.

### Major

- **The skip-action mechanism is not cleanly ablated**: The paper claims that the skip-action "mitigates the optimality gap and increases the performance in cases with 'heavy tasks'" (Section 5.3). However, the heavy-task experiment (Figure 3) compares WeCAN against WeCAN-inside, which differs in the attention mechanism (inside vs. outside placement of compatibility coefficients), not just in the presence/absence of the skip action. The paper does not include a direct comparison of the full WeCAN architecture *with* skip versus an otherwise identical variant *without* skip (i.e., using standard list scheduling as the generation map). Without this ablation, it is impossible to attribute the 8.3–8.9% improvement over HEFT to the skip action specifically, rather than to the architectural advantage of outside-softmax placement or to the interaction between the two. This undermines a core claimed contribution (contribution 3 in the introduction).

### Minor

- **Limited comparison with recent neural heterogeneous schedulers**: The paper benchmarks against PPO-BiHyb (2021) and One-Shot (2023) but not against Zhou et al. (2022), Zhadan et al. (2023), or Wang et al. (2025), all of which are cited in the introduction as methods for heterogeneous DAG scheduling. While the paper provides a rationale (these methods use fixed-size embeddings that limit adaptability), the absence of direct comparison weakens the claimed "significant gains compared to state-of-the-art methods." At minimum, the authors should discuss expected relative performance on compatible benchmarks.

- **Expressiveness of the skip score formula is not discussed in the main text**: The skip score uses the parametric form \(u_{\pi_{skip}} = u_a(1 - \frac{k}{2n})^{u_b} + u_c\). Theorem 1(iv) asserts existence of scores enabling optimal solutions, but the main text does not analyze whether this specific functional family can realize the required scores for all problem instances. The proof is deferred to the appendix (which was stripped from the submission). An explicit discussion or illustrative example in the main text would strengthen the claim.

- **Generalization experiment (Figure 2) is limited to TPC-H-30**: While the results are encouraging, generalization on Computation Graphs (where environment fluctuations also matter) is not shown. Additionally, the number of random seeds used for variance estimates is not specified in the reported tables.

### Trivial
- Table 1 caption says "standard deviation among random seed" but does not specify the number of seeds.

## Nice-to-Haves
- A direct Gantt-chart visualization of schedules produced with and without the skip action on a heavy-task instance would concretely illustrate how the skip resolves the identified optimality gap.
- An analysis of the non-autoregressive decoder's cost (referenced to Appendix B) could be briefly summarized in the main text, given that it is a simplifying assumption that may affect solution quality.

## Removed Points

- **"Non-autoregressive decoder impact not discussed"**: The paper explicitly says "(comparison with auto-regressive one in Appendix B)" on line 140. The discussion exists; it was deferred to the appendix. → Removed.
- **"LDDGNN appears to be a minor adaptation of Graphormer/Topformer"**: Subjective opinion, not a concrete weakness. The paper provides the design in detail and validates it in Table 3. → Removed.
- **"The theoretical analysis is not new (list scheduling not optimal)"**: The paper's specific framing (MILP reduced space, surjection condition, skip action as a principled fix) goes beyond the trivial observation. The analysis is a contribution, not a weakness. → Removed.
- **"Theorem 2 connection to algorithm is unclear"**: Section 4.2 explicitly explains the connection: the skip action enlarges \(B_f\) and lifts \(S_{list}\) to satisfy Assumption 1, enabling surjectivity. → Removed.
- **"Standard deviations only reported for sampling variants"**: Deterministic methods (HEFT, CP, etc.) do not have variance from sampling. The tables correctly report makespan as single values for deterministic baselines. → Removed.
- **"The large runtime gap between WeCAN and PPO-BiHyb is not a fair efficiency comparison"**: The paper is comparing methods as reported; PPO-BiHyb's beam search is part of its design. The paper does not claim a direct efficiency comparison for equivalent inference modes. → Removed.
- **Critic's speculation about the proof in the omitted appendix** (e.g., "likely assumes an idealized skip mechanism"): Not verifiable from the paper as written; the appendix was stripped. → Removed.
- **Strength Finder claims about the skip action being empirically validated by Figure 3**: As noted in the Major weakness, Figure 3 conflates architectural changes with the presence of skip. This strength conflicts with a verified weakness and is removed. → Removed.
- **Generic strengths about "addressing an important problem"** from Strength Finder: Not concrete enough. → Removed.
- **Missing related works** (general): The rules prohibit mentioning missing related works without external sources. → Removed.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces the tension between the paper's theoretical framing (skip action closes the optimality gap) and the empirical evaluation of this claim (the heavy-task experiment does not cleanly isolate the skip action), but this is a limitation, not a novel insight.

## Suggestions
1. **Add a clean skip-action ablation**: Compare the full WeCAN model using Algorithm 1 (with skip) against an otherwise identical model using standard list scheduling (without skip, i.e., remove lines 174–175 and 179–181 from Algorithm 1). Report makespan on both standard and heavy-task variants of TPC-H and Computation Graphs.
2. **Include at least one recent baseline** (Zhou et al. 2022, Zhadan et al. 2023, or Wang et al. 2025) in the comparison, or provide a documented explanation (e.g., code/instance unavailability alongside a best-effort reproduction).
3. **State the number of random seeds** used for all reported standard deviations.
4. **Discuss the expressiveness of the skip score formula**: Even briefly, explain why the form \(u_a(1 - k/(2n))^{u_b} + u_c\) is sufficient to achieve the surjectivity claimed in Theorem 1, or characterize the family of score functions it can represent.

## Score and Decision

The paper presents a meaningful architectural contribution (WeCA) that demonstrably outperforms existing methods on heterogeneous DAG scheduling with compatibility constraints. The core claim about the WeCA architecture is well-supported by the ablation study and generalization experiments. However, the skip-action contribution — positioned as a core innovation — lacks clean empirical validation because the heavy-task experiment conflates architectural differences with the presence of the skip action. This is a significant gap but not a fatal one, as the WeCA architecture alone (with standard list scheduling) already outperforms all baselines (Table 1, 2). The paper would be strengthened by the suggested ablation but is not invalidated in its current form.

**Score**: 6.0 — A solid paper with genuine contributions and a clear empirical advantage, marred by a materially incomplete ablation of one of its claimed innovations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>