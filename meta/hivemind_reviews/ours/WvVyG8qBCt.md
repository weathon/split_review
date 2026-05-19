## Summary
This paper proposes DPFormer, a method for training differentially private Transformers on long-tailed data with two contributions: (1) **Phantom Clipping**, an extension of Ghost Clipping that efficiently computes per-sample gradient norms for shared embedding layers, achieving near non-private memory and speed; and (2) **Re-Attention Mechanism**, a variance-propagation method that debiases attention scores inflated by DP noise, motivated by a theoretical analysis of "attention distraction" caused by high-variance (tail) tokens.

## Strengths
- **Phantom Clipping is a clean, practically useful technique.** Claim 1 (Eq. 3) provides a closed-form per-sample gradient norm for the shared embedding layer, overcoming a genuine limitation of Ghost Clipping. Figures 2–4 demonstrate 10–400× memory savings and 4–100× speedup, bringing DP Transformer training close to non-private efficiency. The memory complexity analysis (\(O(BL^2)\) vs. Ghost Clipping's \(O(BM^2+BL^2)\)) clearly explains the advantage.

- **The theoretical analysis of attention distraction is well-motivated and principled.** Equation (6) derives a multiplicative bias \(\exp(C\sigma_i^2/2)\) that inflates attention scores for high-variance tokens. The derivation uses the Gumbel-max trick (an exact identity) and a reasonable approximation for low-attention tokens, offering a concrete mechanism for performance degradation under DP on long-tailed data. This is a genuinely new lens on DP Transformer training.

- **Consistent and substantial accuracy improvements across privacy budgets.** Tables 1 and 2 show 5.4–29% relative improvement on MovieLens and 20–34% on Amazon. The improvement trend correlates with privacy stringency (larger at \(\varepsilon=5\) than \(\varepsilon=10\) on MovieLens), consistent with the theory that more noise causes more distraction. The full grid search visualization (Figure 9) confirms the advantage is not confined to a single "best" configuration.

- **Training stability improvement demonstrated.** Figure 5 (convergence plots) shows DPFormer achieving smoother convergence with narrower confidence intervals across 5 seeds, whereas the vanilla Transformer exhibits higher variance and fluctuation, particularly on the sparser Amazon dataset.

- **Ablation on parameter sharing (Figure 1) convincingly motivates Phantom Clipping.** The experiment systematically compares sharing vs. no-sharing vs. halved dimension, establishing that embedding sharing is essential for accuracy under DP — which in turn necessitates Phantom Clipping since Ghost Clipping does not support sharing.

## Weaknesses
### Major

- **Hyperparameter selection via grid search on test data.** The paper reports "best" results from grid search over learning rate and batch size on the test set (footnote, line 406). While the paper is transparent about this and all baselines receive identical treatment (preserving the validity of *relative* comparisons), the absolute numbers in Tables 1 and 2 are optimistic and may not reflect hold-out performance. A proper held-out validation set or privacy-preserving hyperparameter selection would substantially strengthen the empirical claims. The full grid visualization (Figure 9) mitigates this concern by showing consistent advantage across configurations, but does not fully resolve it — the reported numbers are still selected to maximize test accuracy.

- **Lack of direct validation for the Re-Attention mechanism's hypothesized effect.** The paper motivates Re-Attention with a theoretical analysis of attention distraction (§ 5.1) but provides no direct experiment showing that (a) attention distraction *actually* occurs in DP-trained Transformers (e.g., by comparing attention score distributions of DP vs. non-private models), (b) the estimated effective errors correlate with observed attention distortions, or (c) the variance correction specifically reduces the bias. The only evidence is end-to-end accuracy improvement, which could plausibly be attributed to other factors (e.g., implicit regularization from variance propagation). An ablation comparing DPFormer to a version that tracks variance but does not apply the correction factor would isolate the mechanism's contribution. End-to-end comparison with "vanilla Transformer" serves as a partial ablation, but this alone does not verify the internal mechanism.

### Minor

- **Insufficient implementation details for reproducibility.** The paper does not specify the number of Transformer layers, number of attention heads, whether error propagation covers all heads, or whether residual connections and layer normalization are accounted for in the variance propagation (§ 5.2). The constant \(C = \langle q, q \rangle\) in the correction step (Eq. 6) depends on the query — it is not explained whether this uses the mean query or the actual per-position query. These details are essential for reproducing the method.

- **No empirical measurement of the overhead of error propagation.** The paper claims error propagation incurs "minimal computational and memory overhead" (line 274) but provides no measurements. Given that per-token variances must be propagated through every layer, practitioners would benefit from a table or figure showing training time and memory with and without Re-Attention on a fixed model.

- **The theoretical derivation's approximation is not validated or bounded.** Equation (4) approximates the Gumbel-max by dropping the low-attention token \(i'\) from the max operation. The paper does not discuss the regime where this approximation holds, nor does it analyze the effect of the correction on high-attention tokens (where the derivation's assumptions do not apply). While the end-to-end results suggest the approximation is benign in practice, a formal or empirical characterization would strengthen confidence.

### Trivial

- **DP-SGD equation (Eq. 1) places the noise term inside the sum and inside \(\operatorname{Clip}_C\), which is technically incorrect** — it should be added after averaging/clipping. This appears to be a notational artifact rather than an implementation error, but it is confusing as written.

- **The convergence plots (Figure 5) show overlapping confidence intervals in several settings** (e.g., Amazon at \(\varepsilon=10\), NDCG@10), weakening the claimed superior stability for those specific conditions.

## Suggestions
1. **Fix the evaluation protocol:** Use a held-out validation set for hyperparameter selection, or report results from a single fixed validation-best configuration for all methods. This is the single change that would most improve the paper's credibility.
2. **Add a targeted ablation for Re-Attention:** Compare (a) DPFormer with full Re-Attention vs. (b) a version that tracks variance but does not apply the correction factor (i.e., omits the division by \(\exp(C\sigma_i^2/2)\)). This would isolate the correction's contribution.
3. **Specify architecture details:** Number of layers, number of heads, whether error propagation covers all heads, and how \(C = \langle q, q \rangle\) is computed per query.
4. **Measure the overhead of error propagation:** Provide a table comparing training time and peak memory with and without Re-Attention.
5. **Validate the approximation regime:** Add a brief synthetic or empirical analysis showing that the Gumbel-max approximation in Eq. (4) provides reasonable estimates under realistic DP noise levels.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
