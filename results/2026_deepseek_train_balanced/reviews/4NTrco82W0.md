## Summary

This paper establishes a theoretical framework connecting regression loss functions used in GFlowNet training to $f$-divergences, enabling principled design of losses with specific zero-forcing (exploitation) or zero-avoiding (exploration) properties. Theorem 1 proves that the gradient of any GFlowNet objective with a twice-differentiable convex regression loss $g$ equals the gradient of a weighted sum of $f$-divergences, generalizing the known result that squared loss corresponds to reverse KL divergence. Based on this framework, the paper introduces three losses (Linex(1), Linex(1/2), Shifted-Cosh) and evaluates them across hyper-grid, bit-sequence generation, and molecule generation tasks with four GFlowNet algorithms.

## Strengths

- **Theorem 1 provides a rigorous, general mapping from any twice-differentiable convex regression loss $g$ to an $f$-divergence $D_f$** (Section 3.2, Eq. 210–211). The result subsumes the prior result that squared loss corresponds to reverse KL as a special case and extends to any convex $g$, which is a genuine theoretical advance for the GFlowNet literature.

- **The closed-form constructive procedure (Remark 2, line 224–226)** gives practitioners a direct formula to derive a regression loss from any desired $f$-divergence: $g(t) = f(e^t) - \int_1^{e^t} \frac{f(s)}{s} ds$. This turns an ad-hoc choice into a principled design process and is the most actionable contribution of the paper.

- **Mode-finding improvements are quantitatively demonstrated.** In bit-sequence generation (Table 2), Linex(1) achieves 5/5 runs finding all modes across TB, DB, and STB, while Quadratic (baseline) collapses to 1/5 in TB. This is a clean, reproducible improvement on a standard benchmark.

- **The predicted zero-forcing/zero-avoiding trade-off is borne out in molecule generation** (Figure 2). Zero-forcing losses (Quadratic, Shifted-Cosh) yield higher average reward, while zero-avoiding losses (Linex(1), Linex(1/2)) produce more diverse samples — confirming that the theoretical analysis in Section 3.3 translates into observable behavior.

- **The paper systematically unifies five GFlowNet algorithm families into a single objective** (Eq. 1, Table 1). The decomposition into five components (training objects, parameterization, sampling weights, backward policy, regression loss) reveals structural relationships across FM, DB, TB, STB, and their variants, which is useful independent of the loss design contribution.

## Weaknesses

### Fatal
None.

### Major

- **The theory-experiment gap from off-policy sampling is acknowledged but not addressed.** Theorem 1's central condition requires $\mu(o) = \hat{p}_F(o) \sum_{C\in\mathcal{C}, o\in C} w(C)$ (on-policy sampling), but all experiments use $\epsilon$-noisy forward policies (random-action probability 0.001 for bit-sequence, 0.05 for molecule generation) where this condition is violated. The paper says this gap exists (line 309) but offers no analysis of how large the discrepancy is, whether the divergence interpretation degrades gracefully or collapses, or what error bounds apply. While the empirical patterns are consistent with the theory's predictions, the paper's strongest claim — that the theory *explains* the experimental results — is weakened because the theorem's conditions do not hold in the experiments. This does not invalidate the theory (which is correct under its stated conditions) but creates a disconnect between the theoretical apparatus and the empirical evidence used to support it.

- **The claim of "significant improvement" in the abstract is overstated given the mixed results.** In the bit-sequence Spearman correlation (Table 3), which measures distribution-matching quality, the proposed Linex(1) and Linex(1/2) losses *underperform* the Quadratic baseline across all three algorithms (e.g., DB: 0.7464 vs. 0.7907). The paper explains this post-hoc as "zero-forcing losses have advantages on the qualities of samples," but this means the proposed losses do not uniformly improve performance — they improve mode-finding exploration at the cost of distribution-matching quality. Additionally, in hyper-grid (Figure 1), all four losses converge to essentially the same L1 error; the only difference is convergence speed, shown without error bars. The abstract's characterization of "significant improvement" in "convergence speed, sample diversity, and robustness" should be calibrated to reflect the specific settings where improvements occur and the trade-offs involved.

### Minor

- **The molecule generation results are presented qualitatively from plots** (Figure 2) without summary statistics in the text. Final average reward values, top-k reward values, pairwise similarities, and standard deviations across seeds would substantially strengthen the empirical case. As-is, claims like "Linex(1/2) demonstrates the best robustness" (line 405) rest on visual interpretation of a single plot.

- **The hyper-grid experiment uses a learned backward policy** (line 322), while all other experiments use fixed/uniform backward policies. The paper does not comment on why this choice was made or how it might interact with the loss functions differently than in the other settings. Since the theoretical framework assumes a fixed $P_B$, this asymmetry could affect the cross-experiment comparisons.

- **No sensitivity analysis for the Linex parameter.** The Linex(1) and Linex(1/2) losses differ only by a parameter in the exponent, and the paper presents both as fixed proposals without investigating how varying this parameter affects the exploration-exploitation trade-off. This limits the practical utility of the framework — a practitioner reading the paper would not know how to tune this parameter for their own task.

### Trivial

- "Pseudo $f$-divergence" (line 139) is introduced but never referenced again in the paper; the concept appears to be unused.

## Nice-to-Haves

- An on-policy ablation experiment (e.g., on hyper-grid) where Theorem 1's condition holds exactly, to verify that the theoretically predicted behaviors occur cleanly before the off-policy setting where the theory becomes approximate.
- A bound or characterization of how the off-policy gap affects the divergence correspondence, e.g., relating the error to the $\epsilon$ in the noisy forward policy.
- Comparison against additional convex loss functions not derived from a specific divergence (e.g., Huber loss) to isolate whether the *divergence-based design principle* specifically drives the improvements.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Conflates squared-error loss in log-space with standard quadratic regression"** — The paper clearly specifies this is in log-space (line 10). This is not a genuine issue.
- **"Limited conceptual novelty of the loss functions themselves"** — The paper's contribution is the *framework* connecting losses to divergences, not the functions as standalone mathematical innovations. The reviewer acknowledges this ("this is fine as a contribution given the theoretical framework") but still lists it as a weakness. The framing is over-critical.
- **"No comparison against alternative loss designs"** — This demands evaluation breadth beyond the paper's stated scope. The paper provides a framework and evaluates losses derived from it. The comparison against the standard baseline (quadratic) is appropriate. Softened to a nice-to-have.
- **"Pseudo f-divergence never used again"** — A trivial observation about a definitional term that has no impact on the paper's contributions.
- **Vague/generic concerns without concrete anchors** from the harsh critic's section-by-section notes (e.g., questioning whether convexity conditions are satisfied for all losses — these are verified in the paper and the critic's own subsequent analysis confirms they are).

## Novel Insights

The most interesting observation that emerges from combining the reviews is the following asymmetry: the framework's *design capability* (Remark 2) and the *theory* (Theorem 1) are cleanly separated in the paper. Remark 2 lets a practitioner derive *any* loss from any $f$-divergence, and this constructive procedure does *not* depend on Theorem 1's sampling condition — it is purely algebraic. So even if the gradient-equivalence in Theorem 1 is only approximate under off-policy sampling, the qualitative zero-forcing/zero-avoiding analysis (which depends only on the divergence's $f(0)$ and $f'(\infty)$ limits) can still guide loss selection. The paper does not explicitly draw this distinction, but it means the design framework is empirically useful even when the precise gradient correspondence is approximate. The weakness is that the paper's strongest claims rely on Theorem 1's exact equivalence, while its practical value may come from the coarser qualitative properties.

## Suggestions

1. **Calibrate the claims in the abstract and introduction** to reflect the trade-off revealed in Table 3 (improved exploration/mode-finding, sometimes at the cost of distribution-matching quality). Replace "significantly improve the performances...concerning convergence speed, sample diversity, and robustness" with a more precise characterization.

2. **Either add an on-policy ablation or provide an analytical characterization of the off-policy gap.** The simplest fix: run the hyper-grid task with pure on-policy sampling (no $\epsilon$-noise) and verify that Theorem 1's predictions hold exactly. Alternatively, derive a bound showing how the gradient approximation degrades with the degree of off-policiness.

3. **Add summary statistics for the molecule experiment** — a table with final average reward, top-k reward, and pairwise similarity with standard deviations over multiple seeds — to replace the purely qualitative visual description.

4. **Include error bars or confidence bands on the hyper-grid L1 curves** to support the convergence-speed claim.

5. **Acknowledge and explain the learned-backward-policy choice in hyper-grid**, or use a fixed backward policy to match the other experiments.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>