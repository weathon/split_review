Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Pi-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment by maintaining a compact, prompt-invariant certificate summarizing the top-\(k\) canonical spectrum and subspaces. During adaptation on new tasks, the method enforces spectral and subspace-angle consistency with this certificate using only mini-batch statistics (no past data, generators, or reference corpora). Experiments across MTIL, X-TAIL, VLCL, and ConStruct-VL benchmarks show Pi-CCA achieves state-of-the-art performance among replay-free methods, including surpassing a synthetic-replay method on retrieval/structured-concept tasks.

## Strengths

- **State-of-the-art replay-free performance across four diverse benchmarks.** Tables 1 and 2 show Pi-CCA achieves the highest scores on MTIL (Avg 76.8, Last 75.5, Transfer 73.2), X-TAIL (Avg 68.1), VLCL (I2T R@1 48.6, T2I R@1 37.4), and ConStruct-VL (FA 75.2, AF 2.7), outperforming all compared replay-free methods and even a synthetic-replay method (GIFT) on retrieval/structured-concept tasks.

- **Novel geometry-first conceptual framing.** The paper reframes forgetting as alignment-geometry drift and directly constrains the canonical correlation spectrum and subspaces, rather than regularizing proxy signals (similarities, logits, parameters, or routing). This is a principled departure from prior VL-CL methods. The ablation in Table 3 confirms that removing the spectral term (\(\lambda_1=0\)) drops MTIL Avg by 2.5 points and removing the subspace term (\(\lambda_2=0\)) drops it by 2.2 points — the largest single-component degradations — validating that direct geometry preservation is essential.

- **Explicit prompt-invariance mechanism with demonstrated effect.** The paper introduces \(\mathcal{L}_{\text{pi}}\) (Eq. 11) that aligns the mean sketched projector and contracts dispersion across prompt perturbations. The stress test in Figure 4 shows the mechanism flattens degradation: at perturbation strength \(s=1.0\), Pi-CCA with \(\mathcal{L}_{\text{pi}}\) improves R@1 by +2.44 p.p. (ID) / +2.51 p.p. (OOD) and reduces AF by ≈1.10/0.96 compared to the variant without it.

- **Compact, constant-memory certificate with empirical Pareto analysis.** The certificate stores sketched bases \(S_v \in \mathbb{R}^{h \times k}, S_t \in \mathbb{R}^{h \times k}\) with \(h \ll d_v, d_t\), achieving constant memory relative to embedding dimensionality. Figure 2 maps the capacity Pareto frontier, identifying a broad efficient ridge for \(k \in [48, 96], h \in [192, 320]\), confirming that small certificates suffice for high performance.

- **Comprehensive evaluation.** The paper tests on four diverse VL-CL protocols (classification, retrieval, structured concepts), includes task-order sensitivity over 20 random orders (Figure 5), capacity Pareto analysis (Figure 2), and a prompt-invariance stress test (Figure 4). Task-order robustness is demonstrated with narrow interquartile ranges across shuffles.

## Weaknesses

### Fatal
None.

### Major

- **Suspiciously perfect correlations in Figure 3.** The paper reports Pearson \(r=1.00\) and Spearman \(\rho=1.00\) for two of four panels and \(r=0.99/\rho=1.00\) for the remaining two, correlating geometry drift with performance drop across a sweep of hyperparameter configurations. Such values are essentially impossible in realistic experimentation with measurement noise across multiple hyperparameter settings. The paper also states a "95% confidence interval shaded area" is plotted, but an \(r=1.00\) implies zero-width CI, which is inconsistent. The drift metrics (\(D_{\text{ang}}, D_\rho\)) are also the same quantities being optimized in the losses, so the correlation is partially tautological — it confirms that when the losses are high, performance drops, rather than providing independent causal evidence. This analysis section needs correction or clear explanation; as presented it undermines confidence in the paper's analytical rigor. However, this does **not** affect the paper's core SOTA claims (Tables 1, 2) which stand independently.

- **Ablation study (Table 3) reports single-point values without error bars or variance estimates.** The main retrieval results (Table 2) include \(\pm\) intervals, but the most diagnostic experiments — component ablations, certificate EMA, covariance EMA, pairing variants — are reported as single numbers. Given the importance of the ablation for attributing contribution to each loss term, the reader cannot assess whether observed differences (e.g., the 0.1-point gap between Hungarian and sorted pairing) are statistically meaningful or within noise.

### Minor

- **The streaming EMA CCA estimation under non-stationary data is not theoretically characterized.** The paper uses EMA updates (Eq. 12) on covariance matrices and then whitens to compute the cross-covariance. Under abrupt task shifts where the data distribution changes sharply, the EMA will mix past and present statistics. Whether the resulting whitened cross-covariance approximates current canonical structure, retains stale structure, or inadvertently causes forgetting via smoothing is not analyzed. The empirical results suggest the method works, but a theoretical or analytical treatment of this approximation would strengthen the paper.

- **Notation inconsistency at line 64**: \(\theta_v = (\theta_v, \phi_v)\) uses the same symbol on both sides of the equation, which is confusing. From context it means the full parameter set includes both frozen backbone (denoted \(\theta_v\)) and trainable adapter (\(\phi_v\)), but the reuse of \(\theta_v\) for two different objects could confuse readers.

### Trivial

- Deferred details (perturbation set \(\mathcal{P}\), hyperparameter sensitivity sweeps, full training procedure) are relegated to the appendix which is stripped by the parser. The main text provides the key specifications (e.g., \(M=4\) for the stress test, \(s\) defined as token-level perturbation ratio) but some implementation specifics are only referenced in the appendix.

## Nice-to-Haves

- A runtime comparison (step time) against the strongest baselines (e.g., C-CLIP, ZAF, DIKI) would be useful context for practitioners, complementing the existing Pareto analysis of Pi-CCA's own capacity trade-offs.
- A 2D sweep over \(\lambda_1\) and \(\lambda_2\) would help demonstrate robustness to loss weighting, complementing the single-factor disabled-component ablations in Table 3.
- A timeline plot showing canonical correlation values across the task stream (e.g., comparing Pi-CCA to naive fine-tuning) would visually reinforce the claim that the certificate stabilizes alignment geometry.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that Figure 3 correlations are "spurious" or potentially invalidate the paper's core claims**: The suspicious \(r=1.00\) values are a genuine concern (retained as a Major weakness above), but the reviewer's framing that this "invalidates the paper's central claim" is overreaching. The core SOTA results in Tables 1 and 2 are independent of this correlation analysis, so even if Figure 3 had issues, the main contributions stand. The weakness is retained but downgraded from "potentially fatal" to Major.

- **Harsh critic's "no error bars in Figure 5"**: Figure 5 shows boxplots over 20 random orders with 3 seeds each — a comprehensive visualization of variability that is *more* informative than simple error bars. This criticism is factually incorrect about the figure.

- **Strength Finder's "Strong empirical correlation between geometry stability and downstream performance" (Figure 3)**: Conflicts with the verified weakness about suspicious \(r=1.00\) values. Per instructions: when a strength and weakness disagree, the weakness wins. Removed.

- **"Missing related works on CCA-based continual learning"**: Cannot be verified as existing; per instructions, do not mention missing related works.

- **"Missing qualitative examples"**, **"extension to multimodal instruction tuning"**: Generic suggestions, not weaknesses.

- **"Prompt-invariance mechanism is under-specified"**: The main text defines \(M=4\) for the stress test (line 237), defines \(s\) as "token-level synonym swap/back-translation/template jitter ratio" (line 237), and specifies the loss (Eq. 11). The remainder is deferred to Appendix §A.2, which is standard practice for the full perturbation set. Demoted from methodological gap to minor/trivial.

- **Criticism about the EMA formula (Eq. 12) having formatting garbles**: Line 142 shows a parser artifact ("M^{(t)} = (∑_{v=1}^t S_v^{(t)})^{-1/2}..."), not an author error.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the suspicious \(r=1.00\) values in Figure 3 highlight how easy it is to produce tautological or inflated correlation evidence when the "cause" measure (geometry drift) and the "effect" measure (performance drop) are both functions of the same model state and are exactly the quantities being optimized. The paper's claim that "preserving CCA geometry predicts retention" would be much stronger if it used an independent measure of alignment quality not already embedded in the training objective.

## Suggestions

1. **Recompute or explain the Figure 3 correlations.** Run the sweep with multiple seeds and report the distribution of correlation values. Show the raw scatter with jitter or seed-specific coloring. If the near-perfect correlation is genuine, explain why — e.g., is the drift-performance relationship deterministic under these controlled perturbations? Remove the "95% CI" annotation if it is not meaningful.

2. **Add error bars or run-level replication to Table 3.** Even a single additional seed column or a statement that results are from a fixed seed with analysis of seed sensitivity (if available in the appendix) would allow readers to assess the reliability of the component-wise comparisons.

3. **Add a brief discussion** (1-2 paragraphs) analyzing how the EMA estimation behaves under distribution shift — e.g., what the effective timescale of the EMA is relative to task duration, and whether the stale statistics could cause interference.

4. **Clarify the notation** for the parameter set at line 64 to avoid confusion between the backbone weights and the full parameter set.

## Score and Decision

This paper makes a clear conceptual contribution (geometry-first replay-free VL-CL), supports it with SOTA results across four benchmarks, and provides extensive analysis. The two main weaknesses — suspicious correlation values in Figure 3 and missing variance in the ablation study — are real but do not invalidate the paper's core claims, which are grounded in the benchmark comparisons (Tables 1, 2). The Figure 3 issue needs correction but Tables 1-3 tell a coherent story without it. With the specified corrections, this paper would be strong.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>