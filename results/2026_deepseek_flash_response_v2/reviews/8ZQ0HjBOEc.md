## Summary

This theoretical paper studies the Neural Tangent Kernel (NTK) of infinitely wide fully-connected ReLU networks as depth \(L\to\infty\) (with width growing faster than depth). It makes two main theoretical claims: (1) the normalized NTK entries converge to 1 (Theorem 2), implying the kernel becomes singular; and (2) despite this singularity, the NTK regression expression \(\kappa_x^\top\kappa^{-1}\) converges to a well-defined limit (Theorem 3), using rough differential equations. The paper also provides empirical visualizations of convergence rates for individual kernel entries and abstracts general criteria for extending the analysis to other kernels.

## Strengths

- **Relaxed assumptions compared to prior work**: The paper states that its results do not require assumptions on the Hermite expansion spectrum or Mercer decomposition of the kernel (lines 15–17), which contrasts with Nguyen et al. (2021) and Murray et al. (2023). This is a meaningful relaxation for the parts of the paper that are properly established.

- **Generalization criteria abstracted beyond the ReLU NTK**: Section 6 (lines 238–242) distills three concrete properties that any sequence of kernels must satisfy for the analysis to generalize, and provides a second example (the \(\eta^{(L)}\) kernel via \(h(z)=(1+e^{-z})^{-2}\) in Proposition 7). This abstraction gives other researchers a recipe to apply the technique beyond the single ReLU-NTK case.

## Weaknesses

### Major

- **Proof of Theorem 3 — the paper's central claim — is not presented in a verifiable form.** The proof sketch (lines 193–225) has multiple problems that together prevent assessment of whether the result holds:

  1. **Unjustified determinant inequality**: The chain
     \[
     \frac{\det(A)}{\det(\tilde{\Theta}^{(L+1)})^{\psi}\det(\tilde{\Theta}^{(L)})^{1-\psi}} \le \frac{\det(A)}{\det(\tilde{\Theta}^{(L+1)})\det(\tilde{\Theta}^{(L)})}
     \]
     relies on the claim \(\det(A_n^{(L+1)}(t)) \ge \det(\tilde{\Theta}^{(L+1)})^{\psi}\det(\tilde{\Theta}^{(L)})^{1-\psi}\). But \(A\) is a linear interpolation of two matrices, and this inequality does not follow from standard determinant properties (log-concavity on PSD matrices, Hadamard, etc.) in the form stated. The argument that determinants being \(<1\) suffices is insufficient because the inequality relates the determinant of an interpolation to the product of endpoint determinants, not to the individual determinants.

  2. **Incomplete RDE machinery**: The proof invokes Lyons' Universal Limit Theorem and the continuity of the Itô-Lyons map without constructing the rough path lift, verifying that the drivers satisfy the required regularity (e.g., finite \(p\)-variation with the claimed topology), or establishing that convergence in the rough path topology translates to convergence of the specific quantity \(\tilde{\Theta}_\infty^{(L)}(x^\top X)(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}\).

  3. **Unclear logical connection**: The interpolation \(A_n^{(L+1)}(t)\) connects solutions at depths \(L\) and \(L+1\), but the proof does not show that this yields a Cauchy sequence whose limit solves the claimed equation. The step "the \(v_{(i,j)}\) converge to 0 in the 1-variation metric, therefore by Lyons' theorem the solution converges" is asserted without establishing the required convergence topology for the sequence indexed by \(L\).

  Because Theorem 3 is positioned as the paper's headline contribution, a non-verifiable proof is a major weakness.

- **The notation \(\tilde{\Theta}\) (theta-tilde) is used throughout Theorem 3 and the experiments without definition.** The notation section (Section 3) defines only \(\Theta\) and \(\bar{\Theta}\) (the normalized kernel, Definition 4). Yet Theorem 3 (line 183), its proof (lines 195–227), and the experimental section (line 245) all use \(\tilde{\Theta}_\infty^{(L)}\) as though it were a defined quantity. If \(\tilde{\Theta}\) is meant to be \(\bar{\Theta}\) (the normalized kernel from Definition 4), this must be stated explicitly. If it is a different normalization, it requires its own definition. This ambiguity makes large portions of the paper unverifiable as written.

### Minor

- **Experiments do not directly test the paper's central claim.** The headline claim is that the NTK predictor \(\kappa_x^\top\kappa^{-1}\) converges despite kernel singularity. The experiments visualize convergence of individual kernel entries (\(\rho\), \(\eta\), \(\bar{\Theta}\) entries) but do not quantitatively evaluate the actual NTK predictor. The third column of Figure 1 is labeled as showing \(\bar{\kappa}^{(l)}(x^\top X^\top)(\bar{\kappa}^{(l)}(XX^\top))^{-1}\), but the analysis is purely qualitative (visual inspection). No error bars, no quantitative convergence metrics for the predictor, and no comparison to trained finite-width networks are provided. The claim that convergence is "fast" (line 262) is supported only by an assertion about \(\tilde{v}_{i,j}\) converging exponentially faster than the determinant — a claim the paper says follows from "inspection of the proof of Theorem 3" (line 245), which itself is not in verifiable form.

- **Proposition 1's proof sketch is incoherent.** The sketch (line 77) states "\(\mu = 0\) implies \(x^\top x' \ge 0\) with probability \(\frac{1}{2}\)," which does not parse as a coherent step in deriving the claimed closed forms for \(\Sigma^{(L)}\), \(\dot{\Sigma}^{(L)}\), and \(\Theta_\infty^{(L+1)}\) at \(\rho=1\).

### Trivial

- **Lemma 1 (convergence of \(\rho^{(L)}\) to 1) is stated without proof or citation** (line 133). This is a non-trivial claim about the dynamics of the arccosine kernel correlation recursion and deserves at least a reference or a brief justification.

## Nice-to-Haves

- Training finite-width networks to validate that the NTK-predicted behavior matches actual network outputs at practical depths would strengthen the practical relevance.
- Characterizing the limiting function — what does \(\lim_{L\to\infty} \kappa_x^\top\kappa^{-1}\) actually look like as a predictor? — would help readers understand the practical implications.
- Error bars or quantitative convergence metrics for the experiments would improve confidence in the empirical claims.

## Removed Points

The following points from the inputs were removed with justification:
- **"Novelty of Theorem 2 relative to prior work is overstated"** — The paper's explicit recursive characterization of convergence to 1 is a clean formulation even if the phenomenon (kernel becoming singular in the ordered phase) was previously observed; this is a matter of degree, not a verifiable flaw.
- **"Incomplete positioning relative to Bietti & Bach (2021)"** — Scope creep; the paper mentions this work adequately for its purposes.
- **"Stereographic projection changes geometry"** — Misreading of the paper (paper correctly states the sphere dimension as \(S^{n_0}\)).
- **"Depth limited to 30 undermines claims"** — The paper openly acknowledges sublinear/logarithmic convergence and uses Theorem 2 to establish the limit theoretically; it does not claim depth 30 empirically demonstrates convergence of \(\bar{\Theta}\) to 1.
- **"No finite-width networks trained"** — Moved to nice-to-have; the paper's setting is the infinite-width limit where the NTK is exact.
- **Strength: "Theorem 3 proves a well-defined limit"** — Removed because it conflicts with the verified weakness that the proof is not verifiable.
- **Strength: "Empirical demonstration that predictor converges faster"** — Removed as overstated; experiments do not directly measure the predictor.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a significant gap between the paper's claimed contribution (Theorem 3 with RDE machinery) and what is actually established (Theorem 2 about kernel entry convergence with a cleaner, standard derivation). The missing definition of \(\tilde{\Theta}\) is a basic exposition issue noted independently.

## Suggestions

1. Explicitly define \(\tilde{\Theta}\) or replace it with \(\bar{\Theta}\) if they refer to the same normalized kernel.
2. Either provide a self-contained, verifiable proof of Theorem 3, or restructure the paper to honestly scope the contribution to Theorem 2 (kernel entry convergence) and the empirical observations, presenting the singular-limit predictor convergence as a conjecture supported by preliminary analysis.
3. Quantitatively evaluate the convergence of the actual NTK predictor (not just individual kernel entries) with error metrics, and ideally compare to trained finite-width networks.
4. Provide a proof sketch or citation for Lemma 1.
5. Clean up the Proposition 1 proof sketch.

## Score and Decision

**Calibration anchors** (all rounds, listed with path, avg human score, round, and comparison):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/VEJzjAvaIy.md` | 5.75 | R1 mid | **Stronger** — has a sound proof that reviewers could verify, accepted |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WH9NhxOeu9.md` | 5.00 | R2 narrow | **Stronger** — solid theory despite overclaiming concerns |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/V6JRkfj9dU.md` | 4.67 | R2 narrow | **Stronger** — theory is sound even if scope was limited |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/YN4uWzcbtt.md` | 4.25 | R1 mid / R2 narrow | **Comparable or slightly stronger** — clean, verifiable proof though incremental |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kOtFuzoA93.md` | 4.00 | R1 mid / R2 narrow | **Comparable** — broad theory with no experiments, unclear practical implications |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5EtSvYUU0v.md` | 6.00 | R1 mid | **Stronger** — connects NTK and NNGP with solid theory |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fUz6Qefe5z.md` | 3.00 | R1 low | **Weaker** — lower-quality NTK extension |

**Round 1 bracket**: Between approximately 3.0 (weak anchors) and 5.75 (stronger NTK theory papers). Narrowed range: 3.0–4.5.

**Round 2 narrowing**: Anchors at 4.67, 5.00, 5.75 are all stronger — they have sound proofs. The current paper's core theorem proof is not verifiable, placing it below these. Anchors at 4.00–4.25 (kOtFuzoA93, YN4uWzcbtt) are comparable or slightly stronger. The paper at 3.00 is weaker.

**Final score**: 3.5. The paper has genuine useful content (Theorem 2, generalization criteria, relaxed assumptions) but its headline contribution (Theorem 3) is not established by a verifiable proof. The undefined notation and experiments that don't test the central claim further weaken the presentation. This places it below papers with sound (even if incremental) proofs, in the range where a promising idea is not yet backed by sufficient evidence.

MY FINAL SCORE: 3.5
MY FINAL DECISION: Reject