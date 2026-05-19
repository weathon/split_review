- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8
Now I have all the information needed. Let me write the consolidated review.

## Summary

The paper proposes the **Fourier head**, a neural network layer that replaces a standard linear classification head when the output tokens represent discretized continuous values (e.g., binned numerical quantities, directional actions). The layer learns a continuous probability density function parameterized as a truncated Fourier series, then discretizes it at bin centers to produce a categorical distribution. The central claim is that the Fourier head's inductive bias toward smoothness helps models learn signal while ignoring high-frequency noise. The paper provides a theoretical scaling law linking the number of frequencies to output smoothness, and evaluates the method on synthetic density estimation (MLP), offline RL (Decision Transformer on Seaquest), and time-series forecasting (Chronos, 20 benchmarks).

## Strengths

1. **Novel and well-motivated architectural contribution.** The Fourier head is a clean, principled idea: use Fourier series (universal function approximators with a natural smoothness bias) to parameterize the output distribution over continuously-indexed bins. The method is presented as a modular drop-in replacement — Algorithm 1 is concrete and the paper reports that only the frequency count and one regularization hyperparameter need tuning.

2. **Meaningful empirical gains on a large-scale forecasting benchmark.** Table 3 shows consistent improvement across all Fourier configurations on Chronos: MASE drops from 0.883 (linear) to 0.852 (Fourier-550), a 3.5% improvement averaged over 20 zero-shot benchmarks. The Fourier heads also achieve 8×–50× lower smoothness scores while using fewer parameters than the linear baseline. The ablation (regularization, mixed-precision binning) decomposes which design choices drive these gains.

3. **Controlled synthetic evidence supporting the smoothness hypothesis.** Table 1 reports ~40% KL divergence improvement on three synthetic distributions (Gaussian, GMM, GMM-2) with standard deviations over 4 seeds. Figure 2 visualizes that the Fourier head captures multi-modal structure that the linear head misses. This directly validates the claim in a clean setting.

4. **Formal theoretical analysis of the smoothness–expressivity tradeoff.** Theorem 1 provides an asymptotic formula \(s(y^{(N)}) = C_1 - C_2/N^{2t-1} + O(1/N^{2t})\) linking the number of frequencies \(N\) to smoothness degradation, conditioned on the target's Fourier decay rate \(t\). While the constants are not identified, the theorem formalizes a non-obvious relationship: smoother targets (larger \(t\)) degrade more slowly with increasing \(N\).

## Weaknesses

### Fatal

None.

### Major

1. **The autocorrelation construction in Algorithm 1 is presented without justification, making the method opaque.** The paper computes \(c_k = \sum_{\ell=0}^{N-k} a_\ell a_{\ell+k}^*\) (quadratic in the learned parameters) rather than learning Fourier coefficients directly via a linear layer. This design choice is never explained. From Fourier analysis, this construction guarantees that the resulting Fourier series has a non-negative Fourier transform — and therefore \(p(z) \ge 0\) on \([-1,1]\) — which a directly-learned coefficient layer would not. **The paper needs to state this rationale explicitly.** As written, readers must reverse-engineer why this specific nonlinearity is used, and the "by design, each \(y_k \ge 0\)" annotation in Algorithm 1 is unsupported without this explanation. This does not invalidate the method, but it is a significant communication gap that undermines reproducibility and trust.

2. **The experimental scope is narrower than the paper's claims warrant.** The paper claims broad effectiveness for "complex probability distributions" and "large-scale decision making," but the RL evaluation is limited to a single Atari game (Seaquest). Offline RL is known to exhibit high variance across games, and one game cannot demonstrate generality. The Chronos evaluation across 20 benchmarks is strong, but the RL component — a headline 46% improvement — rests on a single game with 4 seeds. The paper should either test more games or explicitly scope the claim to settings where actions have a meaningful spatial ordering (which Seaquest's 16 directional + 2 other actions provides).

### Minor

1. **Missing standard deviations for the main Chronos metrics.** Table 3 reports MASE and WQL without any variance estimate, even though these are aggregated over 20 datasets. The smoothness column does include \(\pm\) values, so the omission for the primary metrics appears to be an oversight. Without error bars, the 3.5% MASE improvement (0.883 → 0.852) cannot be assessed for statistical significance.

2. **The scaling law theorem has limited practical utility.** The asymptotic formula involves unknown constants \(C_1, C_2\) and the decay rate \(t\), none of which are identifiable from data. The first statement ("increasing \(N\) improves modeling power") is a standard property of Fourier series, not a novel result. While the theorem provides qualitative insight, it does not yield actionable guidance for choosing \(N\) beyond what trial-and-error would reveal. This weakens the paper's claim of a "scaling law."

3. **The Decision Transformer baseline returns are cited rather than recomputed.** The paper transparently states (Table 2 caption) that the linear baseline's normalized return is taken from the original DT paper, while the Fourier head results are newly computed. Differences in training setups, random seeds, or evaluation protocols could confound this comparison. The Fourier-8 result (2.78, within one standard deviation of the baseline 2.53±0.63) highlights the need for a controlled replication.

4. **The weight initialization factor of 1000 is unvalidated.** Dividing He-initialized weights by 1000 (Section 2.4) is justified as yielding near-uniform initial distributions, but no sensitivity analysis is provided. The choice of 1000 (vs. 100, 5000, or a principled scale based on the autocorrelation step's Jacobian) is ad-hoc.

5. **The smoothness metric involves an infinite sum with no discussion of truncation.** Definition 1 sums over \(\sigma = 1\) to \(\infty\); the paper does not state at what \(\sigma\) the sum is truncated or how the truncation error is bounded. This is a practical implementation detail that should be documented for reproducibility.

### Trivial

- The abstract's URL is cut off at the page margin.
- Line 259: "shouldn't affect" → "should not affect" (minor formality).

## Nice-to-Haves

- **Comparison to mixture density networks (MDNs):** For the time-series task, MDNs are a natural alternative that also produce continuous conditional densities and could be integrated as transformer heads. A comparison would sharpen the paper's claim that the Fourier parameterization specifically is beneficial.
- **Test on Atari games without directional action structure** (e.g., Pong, with only {up, down}). The Fourier head's smoothness bias could be harmful when the true action distribution is sharply peaked on semantically distant actions.
- **Wall-clock time comparison:** The Fourier head evaluates complex exponentials at all \(m\) bin centers, which may be computationally more expensive than a linear layer (especially for \(m=4096\) in Chronos). Reporting runtime per training step would help practitioners assess the tradeoff.

## Removed Points

These points from the reviews are flagged to be removed; treat them with caution.

- **"The Fourier head is not guaranteed to produce valid probability distributions" (Harsh Critic Critical Issue 1):** This is factually incorrect. The autocorrelation construction \(c_k = \sum_{\ell} a_\ell a_{\ell+k}^*\) makes \((c_k)\) a positive-definite sequence, so \(S(\pi z) = |\sum a_\ell e^{i\ell\pi z}|^2 \ge 0\) and \(p(z) = S(\pi z)/(2c_0) \ge 0\). The method does guarantee non-negative probabilities; the weakness is that the paper does not *explain* this guarantee (which is captured in Major weakness 1 above).
- **"The scaling law proof is missing" (various):** The parser strips appendix content from all papers; the proof exists in the original submission.
- **"The URL in the abstract is cut off":** Parser artifact, not an author error.
- **Missing related works:** Insufficient external knowledge to confirm or deny; against review rules.
- **"Not yet released" / "cannot be independently verified" comments about cited models and code:** Against review rules — all cited entities are assumed to exist.

## Novel Insights

The harsh critic's analysis of Critical Issue 1 inadvertently reveals the *true* justification for the autocorrelation construction that the paper omits. The autocorrelation step is not arbitrary or "likely unnecessary" — it is the mechanism that guarantees \(p(z) \ge 0\) by ensuring \((c_k)\) is a positive-definite sequence with a non-negative Fourier transform. The paper's silence on this point creates the false impression of a structural flaw where none exists. Conversely, the strength finder correctly identifies the Chronos experiments as the paper's strongest evidence but overstates the theoretical contribution by calling it a "provable scaling law" when the constants are unidentifiable. The tension between these two assessments highlights a paper that has a genuinely novel contribution but communicates it incompletely and evaluates it unevenly.

## Suggestions

1. **In the main text, explain why the autocorrelation step is used:** Show that \(p(z) = |\sum a_\ell e^{i\ell\pi z}|^2 / (2\sum |a_\ell|^2) \ge 0\), so the construction guarantees a valid PDF. This single equation would resolve the paper's most opaque design choice.
2. **Add variance estimates to Table 3's MASE and WQL columns** (e.g., standard errors across the 20 datasets, or per-dataset boxplots in the appendix).
3. **Expand the RL evaluation to 3–5 Atari games** with varying action structures (directional, non-directional). If this is infeasible, explicitly scope the claim: "for environments with spatially ordered actions."
4. **Recompute the DT linear baseline in the same training setup** rather than citing the original paper's number.
5. **Acknowledge the truncation of the smoothness sum** and state the chosen \(\sigma_{\max}\) or convergence criterion.
