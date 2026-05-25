Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary

The paper studies separable neural networks (SepNNs) and makes three contributions: (1) a universal approximation theorem for multivariate SepNNs (CP, TT, Tucker) using Stone-Weierstrass, (2) NTK analysis identifying deterministic and random kernel regimes, and (3) a separable preconditioned gradient descent (SepPGD) method to alleviate spectral bias. The theory contributions (1-2) are solid and represent genuine advances. The SepPGD algorithm is creative but its experimental validation and complexity analysis have significant gaps.

## Strengths

1. **Universal approximation theorem for multivariate SepNNs (Theorem 1).** The paper proves that CP, TT, and Tucker SepNNs with any non-polynomial activation can approximate any continuous multivariate function on compact sets. This extends prior bivariate results (Cho et al., 2023) to arbitrary dimension D≥2 and multiple tensor decomposition types. The proof technique combining Stone-Weierstrass with vector-valued MLP approximation is cleaner than the orthogonal-basis construction used in prior work.

2. **NTK regimes for SepNNs (Theorem 2, Corollary 1, Figure 1).** The paper derives the SepNN NTK, proving convergence to a deterministic kernel under infinite width and infinite rank, and to a random kernel under infinite width and fixed rank. The empirical validation in Figure 1(a-d) shows the NTK differences decreasing with width/rank, confirming the theory. This is the first NTK characterization for separable architectures.

3. **Equivalence for D=2 (Lemma 2).** The proof that SepPGD for D=2 is equivalent to classical NTK-based PGD with preconditioner \(\tilde{\mathbf{S}} = \mathbf{S}_1 \otimes \mathbf{I}_n + \mathbf{I}_n \otimes \mathbf{S}_2\) is elegant and uses the Kronecker-product identity to achieve computational savings. The D=2 case is fully rigorous and demonstrates the core insight.

4. **Diverse experimental validation.** SepPGD is evaluated on kernel ridge regression, image/surface INR, and PINNs across multiple PDEs (diffusion, Klein-Gordon, Helmholtz). The visual quality improvements (Figure 3: PSNR 33.30 vs 26.48) are striking.

## Weaknesses

### Major

1. **The O(nD) complexity claim is misleading without a full account of all costs.** The abstract and Table 1 state that SepPGD has O(nD) complexity. This claim is for the per-iteration gradient computation once the preconditioner matrices {M_d} are available. However:
   - Computing M_d via (8) involves a matrix product costing O(n^{D-1}) (acknowledged in Footnote 3). For D=3 this is O(n²), already larger than O(nD)=O(3n).
   - More importantly, the mode-d products R ×_d S_d inside (8) cost O(n^{D+1}) if done naively, and the paper does not explain how the separable structure reduces this cost. The paper cannot simply defer this to the "primary cost" of NTK computation, because the mode-d products are part of the preconditioner *application*, not just its construction.
   - Table 1 compares against Geifman et al. O(n^D) — SepPGD is certainly cheaper, but the claimed O(nD) is an oversimplification. The honest comparison for general D would be at best O(n^{D-1}) per iteration for constructing M_d.
   - The paper should provide a complete per-iteration complexity breakdown identifying the cost of: (a) forward pass, (b) computing residual R, (c) mode-d products, (d) constructing M_d, (e) preconditioned gradient computation.

2. **Experimental evidence does not isolate the effect of preconditioning on convergence per iteration.** All main convergence curves (Figures 2, 4) are plotted against execution time, not iteration number. The paper explicitly states this is because "the efficiency advantage of SepNN and SepPGD comes from the lower complexity in an iteration." This conflates two distinct benefits: (a) SepPGD may have cheaper per-iteration cost (which is fine but not about spectral bias), and (b) SepPGD may actually improve the conditioning and converge in fewer iterations (which is the spectral-bias claim). The paper provides some iteration-based evidence (Figure 3 surface results "under the same iteration number", Figure 4 visual results "under the same iteration"), but these are partial. The core claim that SepPGD "alleviates spectral bias by provably adjusting its NTK spectrum" requires showing that the preconditioner flattens the eigenvalue distribution — yet no figure compares the eigenvalues of K S̃ vs K. Without this, the mechanism claimed for the acceleration remains unverified.

### Minor

1. **Lemma 2 equivalence only proven for D=2; D>2 is speculative.** The paper states "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2" — this is a statement of belief, not a proof. For D>2, the Kronecker-sum structure would be \(\tilde{\mathbf{S}} = \sum_d \mathbf{I} \otimes \dots \otimes \mathbf{S}_d \otimes \dots \otimes \mathbf{I}\), but the paper never formalizes this or shows that SepPGD implements it. The algorithm's justification is therefore incomplete for the multivariate setting that the complexity analysis targets.

2. **No comparison of preconditioned vs original NTK spectrum.** The paper explains theoretically (following Lemma 2) that SepPGD adjusts the NTK eigenvalue distribution, but never empirically demonstrates this. Figure 1(d) shows the SepNN NTK eigenvalues decay rapidly, establishing the spectral bias problem. However, there is no equivalent figure showing that K S̃ has a more uniform eigenvalue distribution, which is the claimed mechanism. This would be straightforward to compute and would substantially strengthen the paper.

3. **Missing ablations on key parameters.** The rank R and the preconditioner parameter k (number of modified eigenvalues) affect both computational cost and convergence behavior, but no ablation studies are provided. The PINN experiment uses D=3 where the complexity concerns are most relevant, yet the paper does not report wall-clock time per iteration or the impact of different R/k choices.

4. **Only CP SepNNs tested.** The approximation theorem covers CP, TT, and Tucker, but experiments only use CP SepNNs. Acceptable as a limitation, but should be explicitly noted.

### Trivial

- Figure 3 caption is ambiguous about whether the image results are "under the same iteration number" (explicitly stated only for surface representation).
- The statement "multiplying D n-by-n preconditioning matrices {M_d}" in Remark 4 is inconsistent with "M_d ∈ ℝ^{R×n}" in Table 1 caption.

## Nice-to-Haves

- Ablation study on rank R and preconditioner parameter k.
- Iteration-wise convergence plots for all experiments as supplementary material.
- Eigenvalue comparison of K vs K S̃ to directly verify the spectral-adjustment mechanism.
- Extension of Lemma 2 to D>2 or a clear discussion of the gap.
- Test on TT/Tucker SepNNs for at least one task.
- Table reporting wall-clock time per iteration for each method.

## Removed Points

These points were raised by one of the reviewers but filtered out as either factually incorrect, non-substantive, or outside scope:

- **"Approximation theorem sketch omits uniform error bound discussion"** — The paper states the complete proof is in the appendix (which is stripped by the parser). The main text sketch is adequate for a theory section.
- **"Theorem 2 conditions (both W→∞ and R→∞) are non-standard"** — This is an observation, not a weakness. The paper explicitly acknowledges this and includes Corollary 1 for the fixed-rank case. The empirical verification in Figure 1 partly bridges the gap.
- **"Missing related works"** — Cannot verify; the paper's reference list is not available for inspection due to parser stripping.
- **"Missing proofs in appendix"** — The appendix is removed by the parser; these exist in the original submission.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.
- **Reproducibility concerns about undisclosed hyperparameters** — The paper points to Appendix A.12 for experimental settings, which is stripped by the parser.
- **Non-grid input extension should be in main text** — The paper references Section A.2 for non-grid inputs. Moving this to main text would be nice but not required given the paper's grid-input focus.

## Novel Insights

**None beyond the paper's own contributions.** The individual review inputs did not surface a genuinely novel observation about the paper that was not already present in the paper's own framing.

## Suggestions

1. **Provide a complete complexity breakdown for SepPGD.** State the cost of each step (forward pass, mode-d product, M_d construction, gradient computation) clearly, and report the honest complexity as O(R n^{D-1}) or better if structure is exploited, rather than the oversimplified O(nD). For D=2 the O(nD) claim is accurate via Lemma 2; for D>2 it should be qualified.

2. **Add iteration-wise convergence plots** for at least one task (e.g., KRR or image representation) to separate preconditioning effect from per-iteration cost advantages.

3. **Compare the eigenvalue spectrum of K S̃ vs K** for a small-scale experiment (e.g., the KRR setting). This would directly validate the claimed mechanism.

4. **For D>2,** either extend Lemma 2 to show that SepPGD implements the Kronecker-sum preconditioner \(\tilde{\mathbf{S}} = \sum_d \mathbf{I} \otimes \dots \otimes \mathbf{S}_d \otimes \dots \otimes \mathbf{I}\), or explicitly discuss the gap and how SepPGD approximates this structure.

## Score and Decision

**Calibration analysis:**

Round 1 bracket: 4.0–6.0

Anchor papers used for calibration:

| Anchor | Score | Round/Query | Comparison |
|--------|-------|-------------|------------|
| xpmDc76RN2 | 2.33 | R1-topic-low | Optimization of operator networks — had incomplete proofs. Current paper's theory is solid; no such flaw. |
| NbbsRnPBoS | 2.33 | R1-topic-low | Deep linear networks — different topic, limited scope. Not comparable. |
| fUz6Qefe5z | 3.00 | R1-topic-low | NTK with derivative labels. Current paper has more contributions. |
| 2C3CWCPxNS | 5.00 | R1-topic-mid + R2 | Preconditioning for PINNs — had scalability concerns. Current paper has comparable theoretical depth. |
| TNYLCF7vZA | 4.75 | R1-weakness + R2 | Inductive gradient adjustment for spectral bias in INRs — very similar topic. Current paper has stronger theory (approximation theorem + NTK regimes) but similar experimental limitations. |
| Oqk1Ui6m0n | 5.00 | R1-topic-mid | Hessian-free natural gradient for PINNs. |
| FK8tl47xpP | 6.25 | R1-topic-mid | Greedy L2O — stronger experimental validation, theory concerns. |
| ydlDRUuGm9 | 6.25 | R2 | KAN expressiveness and spectral bias — accepted paper with comparable theory depth and better experimental validation. Current paper is weaker on experimental side. |

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** Low-band anchors (score ≤ 3.0) either had incomplete proofs, insufficient experimental validation, or unclear contributions. The current paper does NOT share these failures: its proofs are complete (the sketch is clear), its experimental scope is adequate, and its contributions are clearly stated. However, the current paper has significant issues with the clarity and completeness of its complexity analysis and the separation of experimental confounds, placing it in the 4.5–5.5 range rather than higher.

Based on the anchor comparison, particularly against TNYLCF7vZA (4.75, similar topic with similar gaps) and ydlDRUuGm9 (6.25, stronger on both theory and experiments), the paper scores at 5.0. The solid theory contributions push it above the 3–4 range, but the incomplete experimental validation of the core algorithmic claim and the misleading complexity presentation prevent it from reaching the 6+ range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>