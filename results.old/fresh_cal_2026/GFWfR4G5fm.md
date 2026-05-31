Now I have enough information to calibrate. Let me compile my final review.

**Round 1 Bracket**: The paper clearly sits between 5.5–7.5 — well above the weak papers (~2.5–3.0) and below elite papers (~8.0). The middle band returned causal discovery and TTT papers ranging from 5.5 to 6.8.

**Round 2 Narrowing**: After reading full reviews of CausalFM (6.67, Poster), Dynamic Causal Graphs (6.0, Poster), and QPE (5.5, Poster), I place this paper at **6.5**. It has stronger empirical breadth than Dynamic Causal Graphs (multiple datasets vs. one), comparable novelty to CausalFM but less theoretical depth, and much clearer motivation than QPE.

---

## Summary

This paper identifies three limitations of static supervised causal learning (SCL) — fragility to distribution shifts, compositional generalization failure, and synthetic-to-real performance gap — and proposes a test-time training framework (TTT-SCL) that dynamically generates a training set aligned to each test instance. The instantiation TACTIC uses an Alignment-of-Distribution (AD) metric plus sparsity penalty to guide stochastic graph refinement, then trains an SCL model on the resulting data. Experiments on synthetic, pseudo-real (Syntren), and real-world (Sachs) benchmarks show TACTIC outperforming traditional discovery methods (PC, GES, NOTEARS) and the strong SCL baseline AVICI, particularly under distribution shifts.

## Strengths

- **Well-motivated with concrete evidence of three SCL limitations.** Section 3.2 (Figure 2, Table 1) provides clean empirical demonstrations that static SCL is fragile under shifts (Mechanism shift drops AVICI from →42 on RFF_G_97.8), fails at compositional generalization (Component-mixed underperforms i.i.d. consistently), and exhibits a large synthetic-to-real gap (97.8→62.3 on Sachs). These experiments directly motivate the shift from diversity-seeking pre-training to test-time concentration.

- **Principled TTT-SCL framework with a tractable AD metric.** The Alignment-of-Distribution metric (Eq. 3, likelihood-based) and sparsity constraint (Eq. 4, L0 norm) are combined into a joint score (Eq. 5) that is well-motivated: AD captures both structural and mechanistic similarity, while sparsity enforces causal minimality. This gives the method a clear optimization target.

- **Strong empirical results, especially on real-world and OOD settings.** Table 2 shows TACTIC (Notears) achieves state-of-the-art AUROC on Linear_U (86.3), Chebyshev_G (83.0), real-world Sachs (78.9), and pseudo-real Syntren (80.1), substantially outperforming AVICI (e.g., 62.3→78.9 on Sachs) and all classical baselines. These results directly support the claim that test-time adaptation improves real-world generalization.

- **Stage-wise analysis confirms two-stage improvement.** Table 4 shows monotonic improvement from seed graph → highest-scoring refined graph → final SCL prediction across all four test domains (e.g., Sachs: 61.8→66.6→78.9), demonstrating that both the search and learning stages contribute meaningfully and that the SCL model adds value beyond the score-based search.

- **Ablation confirms sparsity is necessary.** Table 3 shows removing the sparsity penalty (TACTIC-s) causes consistent drops (e.g., Sachs: 78.9→63.5), validating that AD alone yields degenerate dense solutions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Missing standard deviations for Sachs and Syntren in Table 2.** The TACTIC (Notears) results for Sachs (78.9) and Syntren (80.1) are reported without standard deviations, while all other entries (including TACTIC on synthetic data) include them. Given the well-known variability in causal discovery scores on these benchmarks, this omission weakens the evidence. This is likely a formatting artifact or could be in the stripped appendix, but as presented it is a gap.

- **Hyperparameter λ and sensitivity analysis not in the main text.** The sparsity penalty weight λ (Eq. 5) is a critical hyperparameter that balances AD against sparsity. Its value and sensitivity analysis are not reported in the main text (may be in the stripped Appendix E). Without this, readers cannot assess robustness to this choice.

- **The mechanism regression method is not specified.** The AD metric (Eq. 3) requires fitting f_i^k (regressing each variable on its parents in the candidate graph). The paper does not state the functional form used (e.g., linear regression, GP, neural network). This is important because the quality of AD directly depends on the regression class; a misspecified family could favor incorrect graphs. This detail may be in the appendix.

- **No analysis of K (number of training graphs).** The paper uses K=200 fixed across experiments but provides no ablation showing how performance varies with K. Would K=50 or K=500 change results? Is the SCL model trained from scratch or fine-tuned? These are natural questions.

### Trivial

- **Acceptance rule positivity.** The Metropolis-style acceptance probability α = min(1, score(G^{k+1})/score(G^k)) assumes positive scores; AD is an average log-likelihood that can be negative. This is a minor technical point that could be addressed by exponentiating or adding a constant, and may be handled in the full appendix.

## Nice-to-Haves

- A discussion of the computational cost of TACTIC (stochastic search + SCL training per test instance) vs. the one-time pre-training of AVICI would help readers assess practical trade-offs.
- Additional real-world benchmarks beyond Sachs would strengthen the real-world applicability claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Data leakage concern** (Harsh Critic #1): The critic claims that fitting mechanisms from D_test leaks test information into the training pipeline, making comparisons unfair. This is not a valid weakness — the method is explicitly a test-time training approach, and using test data to adapt is the intended design. All baselines (PC, GES, NOTEARS, AVICI) also directly process D_test. The use of D_test to fit mechanisms and generate synthetic training data with fresh noise is standard TTA practice. The stage-wise analysis (Table 4) already addresses this indirectly by showing that the SCL model's output improves over the highest-scoring refined graph, ruling out the concern that the model simply memorizes test-specific patterns.

2. **Missing implementation details** (Harsh Critic #2): The critic notes missing details about mechanism regression, λ value, etc. The paper explicitly references Appendix A (AD implementation variants), Appendix B (detailed configurations), and Appendix E (AD/sparsity/score analysis). Since the parser strips appendices, these details are present in the original submission. Per policy, weaknesses about missing appendix content that exists in the full submission are removed.

3. **Insufficient ablation of core claim** (Harsh Critic #3): The critic asks for ablations like varying K, single vs. multiple graphs, and training from scratch vs. fine-tuning. These are reasonable analysis questions but not core flaws; the paper already provides the sparsity ablation (Table 3) and stage-wise analysis (Table 4) which are the most critical ablations for the central claim.

4. **Claims about "fundamental" limitations** (Section-by-Section): The critic suggests softening the claim that the three issues are "fundamental" limitations of the entire SCL paradigm. The paper already acknowledges this by testing two architectures (AVICI and SiCL, see Appendix C) and noting consistent patterns, which is sufficient for the paper's scope.

5. **Metropolis acceptance rule requiring positive scores** (Section-by-Section): The acceptance rule α = min(1, score(G^{k+1})/score(G^k)) with potentially negative scores is a minor technical point. If scores are negative, the ratio of two negatives is positive and the rule works (improvement with higher/less-negative score yields a ratio <1, meaning some acceptance but not all; worsening with more-negative score yields a ratio >1, always accepting which is wrong). This is a genuine but minor implementation-level concern that doesn't threaten the paper's contribution.

6. **Generic strengths** (Strength Finder): Several claimed strengths are removed: "Identification of a novel failure mode" (already in the paper's own contributions), "Practical search heuristics" (generic description), and supporting points that overlap with core strengths.

## Novel Insights

The most interesting observation arising from the review process is that the harsh critic's primary concern (data leakage) is actually a feature, not a bug — test-time training by definition uses test data to adapt. The real open question is whether the mechanism-fitting + forward-sampling pipeline (SIM) could be replaced by a simpler approach like a weighted loss on pre-training data, and whether the benefits of TACTIC come primarily from the graph search or the SCL training. The stage-wise analysis in Table 4 partially addresses this, but the gap between the highest-scored graph (66.6 on Sachs) and the SCL output (78.9) is large enough to warrant deeper investigation into what the SCL model learns from the generated data that the score-based search misses.

## Suggestions

1. **Report standard deviations for Sachs and Syntren** in Table 2, and clarify in the text if single-run or multi-run results.
2. **State the mechanism regression method** used for AD computation (linear regression, Gaussian process, neural network, etc.) in the main text.
3. **Provide λ values and a brief sensitivity analysis** (or reference the appendix section clearly) to demonstrate robustness to this hyperparameter.
4. **Add a brief discussion** of the positivity requirement for the Metropolis acceptance rule or clarify the variant used.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>