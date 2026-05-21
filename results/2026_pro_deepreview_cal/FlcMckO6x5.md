Now I have enough context. Let me finalize my analysis and write the consolidated review.

---

## Summary

This paper provides three theoretical contributions for separable neural networks (SepNNs): (1) a universal approximation theorem establishing that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets; (2) a derivation of NTK regimes, showing the NTK converges to a deterministic kernel under infinite width and rank, and to a random kernel under fixed rank; and (3) SepPGD, a factor-wise preconditioned gradient descent algorithm that reduces preconditioner complexity from $\mathcal{O}(n^D)$ to $\mathcal{O}(nD)$ for grid inputs. Experiments on kernel ridge regression, INR-based image/surface representation, and PINNs demonstrate improved convergence.

## Strengths

- **Universal approximation theorem for multivariate SepNNs (Theorem 1).** The proof combines Stone-Weierstrass with classical universal approximation theory to establish that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets to arbitrary precision. This extends prior bivariate results (Cho et al., 2023) to general dimensions and multiple decomposition formats through a unified proof technique (Section 2, lines 81-89). The theorem fills a genuine theoretical gap.

- **Rigorous NTK derivation and asymptotic analysis (Lemma 1, Theorem 2, Corollary 1).** The NTK for CP SepNNs is derived as a weighted sum over factor MLP NTKs (Lemma 1, Eq. 4), and the convergence to a deterministic kernel under double limits (width → ∞, rank → ∞) is proved in Theorem 2. The fixed-rank regime yielding a random kernel (Corollary 1) captures the practical setting where SepNNs operate with limited rank. The spectral bias characterization via NTK eigenvalue decay (Eq. 5) provides a clear theoretical basis for understanding training dynamics.

- **Lemma 2 provides a clean equivalence between SepPGD and classical NTK-based PGD for the 2D case.** The proof shows that the factor-wise updates in SepPGD are exactly equivalent to applying a Kronecker-structured preconditioner $\tilde{\mathbf{S}} = \mathbf{S}_1 \otimes \mathbf{I}_n + \mathbf{I}_n \otimes \mathbf{S}_2$ to the gradient, connecting the proposed method to the established NTK preconditioning framework (Geifman et al., 2024; Shi et al., 2025). The decomposition via $\text{vec}(\mathbf{ABC}) = (\mathbf{C}^\top \otimes \mathbf{A})\text{vec}(\mathbf{B})$ is the key insight enabling the complexity reduction (lines 206-207).

- **Clear efficiency advantage (Table 1, Remark 4).** The $\mathcal{O}(nD)$ preconditioner application complexity for $n^D$ grid samples is a substantial improvement over prior $\mathcal{O}(n^D)$ and $\mathcal{O}(n^D/p)$ methods. The preconditioner construction cost also scales favorably ($\mathcal{O}(D(n^3 + n^2 P))$ vs. $\mathcal{O}(n^{3D} + n^{2D} P)$).

- **Broad empirical validation.** Experiments span KRR, image representation (PSNR improvement from 26.48 to 33.30), 3D surface representation (IoU improvement from 0.983 to 0.992), and PINNs for PDE solving. SepPGD consistently accelerates convergence over unconditioned SepNNs and other baselines across these tasks (Figures 2-4). The NTK convergence properties (Figure 1) are also empirically validated.

## Weaknesses

### Fatal

None.

### Major

- **The "provably adjusting" claim in the abstract and contributions is not substantiated by the main text.** The abstract states SepPGD works by "provably adjusting its NTK spectrum" (line 15) and the contributions say it "provably adjusts the eigenvalue distribution" (line 57). However, the actual theoretical support in Section 4 (lines 208-209) uses qualifying language: "This can *possibly* be verified," "Suppose that $\tilde{\mathbf{K}}$ is close to the true NTK matrix $\mathbf{K}$," and "we can *ultimately* show that $\mathbf{K}\tilde{\mathbf{S}}$ has better spectrum." The argument invokes Lemma 3 (in the appendix, not visible in the main text) to bridge $\tilde{\mathbf{K}}$ and $\mathbf{K}$, and the eigenvalue analysis relies on the Kronecker product structure holding exactly — which is only established for $D=2$. The gap between "could provably" (body) and "provably adjusting" (abstract/claims) is significant. The equivalence result of Lemma 2 is solid, but the step from equivalence to *proven* spectrum improvement is not completed in the paper as presented. This affects the headline claim around which the paper's third contribution is organized.

### Minor

- **The construction of factor preconditioning matrices $\mathbf{S}_d$ is described only at the level of referencing prior work.** The paper states that $\mathbf{S}_d$ is built by computing a pseudo NTK matrix "using sum-of-logits (Mohamadi et al., 2023), followed by eigenvalue modulation as described in (Geifman et al., 2024; Shi et al., 2025)" (lines 163-164). While referencing prior work is acceptable, the connection between the pseudo NTK computed via sum-of-logits and the true factor MLP NTK — and why this proxy leads to effective preconditioning — deserves a brief justification in the main text given that the algorithm's behavior depends on it.

- **The extension to $D>2$ is asserted rather than proved.** Lemma 2 only establishes the Kronecker-structured equivalence for $D=2$, and the text states "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases $D>2$" (line 209). Since experiments use $D=3$ (surface representation, PINNs), the theoretical basis for the claimed spectral adjustment in those settings is not verified. The paper is honest about this limitation, but it limits the scope of the theoretical guarantees.

- **Spectral bias alleviation is inferred from convergence curves rather than directly measured.** The experiments show that SepPGD improves convergence, but do not include direct measurements of the NTK eigenvalue distribution before and after applying SepPGD. Plotting the eigenvalue decay with and without preconditioning would provide more direct evidence for the claimed mechanism (spectral bias alleviation) rather than relying on indirect inference from convergence speed.

### Trivial

- The meaning of "MSK" in the legend of Figure 2 could be clarified at first use.

## Nice-to-Haves

- A direct empirical demonstration of spectral bias alleviation (e.g., plotting NTK eigenvalue distributions with and without SepPGD during training) would strengthen the mechanistic claim.
- The grid-input limitation (footnote 2, line 165) could be briefly discussed in the main text rather than only in a footnote, as it bounds the domains where the $\mathcal{O}(nD)$ complexity advantage holds.
- An ablation comparing different choices for constructing the pseudo NTK (e.g., true factor NTK vs. sum-of-logits approximation) would clarify whether the proxy is faithful.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that "Lemma 3 is not presented in the main paper" as a structural gap.** REMOVED because Lemma 3 is an appendix item — the parser strips appendices from all papers. The original submission presumably includes it. The reviewer's concern about the proof depending on appendix material is noted but does not mean the lemma doesn't exist.

- **Harsh critic's characterization of the proof gap as "decisive" / "structural" / "fatal."** DEMOTED to Major. While the "provably" claim is overstated relative to what's shown, the core algorithmic contribution (SepPGD with Lemma 2 equivalence and $\mathcal{O}(nD)$ complexity) stands independently. The overclaim can be fixed by softening the language; it does not invalidate the algorithm or the experiments.

- **Harsh critic's claim that "experiments should report per-iteration time or flop counts."** MOVED to Nice-to-Haves. The execution-time convergence curves already communicate the practical efficiency advantage. Per-iteration measurements would add precision but are not essential.

- **Strength Finder claim about "provable equivalent Kronecker-based preconditioning" being fully validated.** WEAKENED. Lemma 2 is solid as an equivalence result, but the "provable spectrum adjustment" claim is not fully supported — see Major weakness above.

- **Harsh critic's criticism about the scale of experiments being "modest."** REMOVED. The experiments cover three distinct task domains with reasonable settings; "modest scale" is a generic criticism without a concrete benchmark for what would constitute sufficient scale.

- **Harsh critic's demand for "a complete proof" connecting factor-wise preconditioning to eigenvalue distribution.** This is essentially the same as the Major weakness about the overclaim. Merged; not listed separately.

## Novel Insights

The paper's most interesting conceptual contribution is the observation that the NTK of a separable neural network decomposes into a sum over factor NTKs (Lemma 1, Eq. 4), and that this decomposability can be exploited algorithmically: by preconditioning each factor separately and leveraging the Kronecker product structure (Lemma 2), one can achieve the effect of a full $n^D \times n^D$ preconditioner at $\mathcal{O}(nD)$ cost. This exploitation of architectural structure for algorithmic efficiency — going beyond the standard observation that SepNNs are cheaper to evaluate — is a genuinely useful insight that could inspire similar factor-wise preconditioning in other decomposable architectures.

## Suggestions

- **Soften the "provably adjusting" language** in the abstract and contributions to match the body text. Replace "provably adjusting its NTK spectrum" with something like "designed to adjust the NTK spectrum, with provable equivalence to classical NTK-based PGD (Lemma 2) and empirical evidence of accelerated convergence." This preserves the genuine contribution without overclaiming.
- **Include a brief summary of Lemma 3 in the main text** (even a one-sentence statement) so that the argument connecting $\tilde{\mathbf{K}}$ to the true NTK $\mathbf{K}$ is self-contained.
- **Add a short justification** (2-3 sentences) for why the sum-of-logits pseudo NTK is a reasonable proxy for the factor MLP's NTK.
- **Acknowledge the $D>2$ limitation explicitly** in the main text near Lemma 2 rather than deferring the extension claim to a closing remark.

## Score and Decision

**Round 1 bracket:** Based on comparison with round-1 anchors — TNYLCF7vZA (Shi et al. 2025, 4.75, weaker theory), 2C3CWCPxNS (PINN preconditioning, 5.00, comparable domain), and h7GAgbLSmC (sharper NTK guarantees, 7.00, stronger theory) — the paper sits in the **5.5–7.0** range.

**Round 2 narrowing:** Comparison with the KAN expressiveness paper (ydlDRUuGm9, 6.25, accepted) which has a similar structure (approximation theory + spectral bias analysis + experiments) and the unified NTK/NNGP paper (5EtSvYUU0v, 6.00, rejected) which has ambitious theory with presentation issues. The SepNN paper is comparable to the KAN paper in theoretical depth, has an additional algorithmic contribution (SepPGD), but is weakened by the "provably" overclaim. It is somewhat stronger than the unified NTK/NNGP paper in terms of rigor and experimental validation.

**Final score: 6.0.** The paper has genuine theoretical contributions (universal approximation, NTK analysis) and a practical algorithm with clear efficiency advantages, validated across multiple tasks. The headline overclaim about "provably adjusting" the NTK spectrum is a real but fixable weakness — it requires softening language, not a fundamental rewrite. The paper contributes meaningfully to understanding and improving separable neural networks.

**Anchor summary:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| xpmDc76RN2 | 2.33 | 1 | Much weaker |
| kkVTeMvC9D | 3.40 | 1 | Weaker, different domain |
| 2NwHLAffZZ | 2.33 | 1 | Much weaker |
| NbbsRnPBoS | 2.33 | 1 | Much weaker |
| 2C3CWCPxNS | 5.00 | 1 | Slightly weaker, similar domain |
| FK8tl47xpP | 6.25 | 1 | Slightly stronger, L2O |
| TNYLCF7vZA | 4.75 | 1 | Weaker (Shi et al. 2025) |
| h7GAgbLSmC | 7.00 | 1 | Stronger theory |
| 4xWQS2z77v | 8.00 | 1 | Much stronger |
| STUGfUz8ob | 7.60 | 1 | Much stronger, different domain |
| AoraWUmpLU | 8.00 | 1 | Much stronger |
| P7KIGdgW8S | 8.00 | 1 | Much stronger |
| Tkkrm3pA35 | 5.25 | 2 | Different domain |
| 5EtSvYUU0v | 6.00 | 2 | Comparable (unified NTK/NNGP) |
| GqI4fTVUXC | 6.00 | 2 | Comparable (NTK theory/practice) |
| 2gwo9cjOEz | 6.00 | 2 | Different domain |
| PJjHILiQHC | 6.25 | 2 | Slightly stronger |
| ydlDRUuGm9 | 6.25 | 2 | Most comparable (KAN theory) |
| 8wAL9ywQNB | 6.00 | 2 | Different domain |
| QibPzdVrRu | 6.50 | 2 | Slightly stronger |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>