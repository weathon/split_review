Now let me finalize with the calibration report.

## Calibration Report

**Round 1 — Bracketing:**
- Weak band (avg < 3.5): G2Lnqs4eMJ (2.50), fUz6Qefe5z (3.00), 2NwHLAffZZ (2.33), IqaQZ1Jdky (2.50) — topically related to NTK/KAN/approximation but not strong topically to SepNNs. The paper under review is clearly stronger.
- Middle band (3.5 < avg < 7.5): TNYLCF7vZA (4.75, spectral bias/INR preconditioning), 2C3CWCPxNS (5.00, PINN preconditioning), FK8tl47xpP (6.25, greedy L2O), b6juTJZ1I9 (5.00, preconditioned matrix sensing).
- Strong band (avg > 7.5): STUGfUz8ob (7.60, transformer reasoning), AoraWUmpLU (8.00, neural ODE NTK), 4xWQS2z77v (8.00, loss landscape), P7KIGdgW8S (8.00, graph separation).

**Initial bracket: 4.5 – 6.5.**

**Round 2 — Narrowing (same session):**
Anchors read in full:
- **TNYLCF7vZA (4.75)** — Rejected INR spectral bias paper (Shi et al. 2025, cited in the paper). Stronger experiments than the SepNN paper but weaker theory. The SepNN paper has more substantial theoretical contributions but poorer complexity justification. Comparable on balance, slight edge to SepNN paper.
- **2C3CWCPxNS (5.00)** — Rejected PINN preconditioning paper. The SepNN paper has broader theoretical scope (approximation + NTK + method) and better clarity. Slightly stronger.
- **8wAL9ywQNB (6.00)** — Accepted generalization bounds paper. The SepNN paper has comparable theoretical novelty and stronger empirical validation, but the unresolved complexity issue pulls it below this anchor.
- **Q0TEVKV2cp (6.75)** — Accepted debiasing paper. Stronger experimental rigor; the SepNN paper is weaker overall.

**Narrowed bracket: 5.0 – 6.0.** The paper is stronger than the 4.75 and 5.00 anchors, comparable to 5.50–5.75 anchors, and weaker than the 6.00 anchor.

**Final score: 5.5.** The paper has solid theoretical contributions (universal approximation theorem extending prior bivariate-only results, NTK regimes for SepNNs) and interesting algorithmic ideas (SepPGD with Kronecker/preconditioner connections). However, the O(nD) complexity analysis is underdeveloped — the described operations involve n^D residuals and n^{D-1} intermediates whose cost is not adequately accounted for — and the "provable" spectral adjustment is only established for D=2. These gaps prevent acceptance in current form but are addressable in revision.

---

## Summary

This paper makes three contributions to separable neural networks (SepNNs): (1) a universal approximation theorem for CP, TT, and Tucker SepNNs; (2) NTK regime analysis (deterministic and random limiting kernels); and (3) a separable preconditioned gradient descent (SepPGD) method. The approximation theory fills a genuine gap (prior work was bivariate-only) and the NTK analysis is novel. However, the core efficiency claim of SepPGD — O(nD) complexity for n^D training samples — is not adequately justified given that the operations in (8) involve an n^D residual tensor and n^{D-1} intermediate matrices whose costs are not fully accounted for. The "provably adjusts" claim is established only for D=2. These gaps undermine the central algorithmic contribution in its current form.

## Strengths

- **Universal approximation theorem for multi-dimensional SepNNs (Theorem 1).** Prior work (Cho et al., 2023) covered only the bivariate case. This paper proves that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets, using a clean Stone–Weierstrass argument combined with vector-valued universal approximation. The proof sketch in the main text is clear.

- **NTK regimes with deterministic and random limits (Theorem 2, Corollary 1).** The paper derives the NTK formula for CP SepNNs (Lemma 1) and establishes that under W→∞, R→∞ the NTK converges almost surely to a deterministic kernel; under W→∞, fixed R it converges to a random kernel. The empirical verification (Fig. 1) confirms the predicted asymptotic behavior across multiple seeds. This is a novel extension of NTK theory to separable architectures.

- **Practical demonstration across multiple tasks.** SepPGD shows faster wall-clock convergence on KRR, image/surface INRs, and PINNs compared to baselines (Figs. 2–4). Visual results (Fig. 3) show meaningful quality improvements (PSNR 26.48→33.30 dB on image representation, IoU 0.983→0.992 on surface representation).

## Weaknesses

### Major

- **The O(nD) complexity claim for SepPGD is not adequately justified and appears inconsistent with the described operations.** Remark 4 and Table 1 claim O(nD) complexity for SepPGD. However, computing M_d in (8) involves: (i) the residual tensor ℛ = 𝒵_Θ − 𝒴 ∈ ℝ^{n×⋯×n}, which is not low-rank because 𝒴 is arbitrary — the mode-d products ℛ ×_d 𝐒_d therefore cost O(n^D) for arbitrary labels; (ii) a matrix construction (⊕_r ⊗_{d′≠d}) that yields an R × n^{D-1} matrix multiplied by an n^{D-1} × n unfolded tensor, naively O(R n^D). Footnote 3 acknowledges "a matrix product with complexity O(n^{D-1})" for (8), which for D>2 already exceeds O(nD) (e.g., D=3 gives O(n²) vs O(3n)). The paper does not explain how these operations avoid materializing O(n^D) intermediates. Additionally, Remark 4 describes M_d as "n-by-n" while Definition 1 gives M_d ∈ ℝ^{R × n}. This dimensional inconsistency further obscures the complexity analysis. The SepPGD algorithm may still offer practical gains (especially for D=2 as the experiments suggest), but the claimed asymptotic advantage is not substantiated.

- **"Provably adjusts" is demonstrated only for D=2; extension to D>2 is conjectural.** The abstract and introduction claim SepPGD "provably adjusts" the NTK spectrum. However, Lemma 2 (the equivalence with classical PGD) and the subsequent spectral analysis are established only for D=2. The paper states "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2" (p. 8)—which is a conjecture, not a proof. While Section 4 is transparent about this, the high-level framing in the abstract and introduction overstates the scope of the theoretical guarantee.

### Minor

- **The forward pass complexity claim (O(nD) per epoch) conflates factor MLP evaluation cost with loss computation cost.** The SepNN output on a grid is a CP-rank-R tensor of size n^D. Computing the MSE loss ⟨𝒵_Θ − 𝒴, 𝒵_Θ − 𝒴⟩ requires an inner product with 𝒴 which, for arbitrary labels, involves all n^D entries. The O(nD) claim (inherited from prior SepNN literature) counts only the nD factor MLP forward passes, not the tensor operations needed to compute the loss. This issue propagates to SepPGD because the residual and its mode products inherit the same scaling.

- **Convergence reported only in wall-clock time.** Figures 2–4 plot loss vs. execution time. Without per-iteration convergence curves, it is unclear whether SepPGD converges faster because it improves the condition number (algorithmic improvement) or simply because each iteration is cheaper (implementation improvement). These should be separated.

- **Error bars missing from main experiments.** Only Fig. 1 (NTK verification) reports variance across multiple seeds; Figs. 2–4 show single-run convergence. This limits the statistical grounding of the empirical claims.

### Trivial

- Dimensional inconsistency: M_d is ℝ^{R×n} in Definition 1 (8) and Table 1, but Remark 4 calls it "n-by-n" and the D=2 discussion states M_d ∈ ℝ^{n×n} (p. 8). These should be reconciled.
- No algorithm pseudocode for SepPGD, which would help clarify the computational steps.

## Nice-to-Haves

- A rigorous complexity analysis separating preconditioner construction (S_d), M_d computation, and gradient backpropagation, with explicit scaling in n and D.
- Empirical scaling plots (wall-clock time vs. n for fixed D, vs. D for fixed n) to verify the claimed O(nD) scaling.
- Extension of Lemma 2 to D>2, or explicit qualification in high-level claims that the provable spectral adjustment is limited to D=2.
- Per-iteration convergence curves alongside wall-clock time plots.
- Error bars in all experimental figures.

## Removed Points

- *"The proof sketch for approximation theory does not clarify whether TT/Tucker forms are closed under addition and multiplication"* — The paper states the appendix handles these cases; the main text focuses on CP form and notes TT/Tucker contain CP as a special case. This is standard practice for deferring detailed proofs to the appendix.
- *"Missing algorithm pseudocode"* and *"NTK matrix computation cost details"* — These are presentation preferences or standard implementation details, not technical weaknesses.
- Various formatting/typo nitpicks and speculation about appendix contents removed per the filtering rules.

## Novel Insights

The cleanest insight is the connection between SepPGD and Kronecker-product structure for D=2 (Lemma 2): SepPGD is equivalent to classical PGD with preconditioner 𝐒̃ = 𝐒₁⊗𝐈 + 𝐈⊗𝐒₂, but the computation can leverage the vec-trick vec(𝐀𝐁𝐂) in O(n)-dimensional space rather than forming (𝐂ᵀ⊗𝐀)vec(𝐁) in O(n²)-dimensional space. This correctly identifies why separable structure can reduce preconditioner application cost. The limitation is that this exact equivalence exploits D=2 Kronecker structure, and the paper does not provide an analogous argument for D>2.

## Suggestions

1. Provide a rigorous per-iteration complexity analysis for SepPGD accounting for all tensor operations, clarifying which steps scale as O(n^D), O(n^{D-1}), and O(nD). Justify or correct the claim in Footnote 3.
2. Qualify the "provably adjusts" claim in the abstract/introduction to reflect the D=2 scope, or extend the proof to general D.
3. Add per-iteration convergence plots alongside wall-clock time. Include error bars from multiple seeds in all experimental figures.
4. Resolve the dimensional inconsistency for M_d and add a clear pseudocode listing.

## Score and Decision

**Round-1 bracket:** 4.5 – 6.5 (based on weak anchors around 2.3–3.0 for NTK/approximation theory, middle anchors 4.75–6.25 for spectral bias/preconditioning work, and strong anchors 7.6–8.0 for high-impact theoretical work).

**Round-2 narrowing to 5.0 – 6.0** based on reading:
- TNYLCF7vZA (4.75) — weaker theory, comparable experiments → SepNN paper is stronger
- 2C3CWCPxNS (5.00) — narrower scope → SepNN paper is slightly stronger
- 8wAL9ywQNB (6.00, Accept) — cleaner claims, no unresolved complexity gap → SepNN paper is slightly weaker
- Q0TEVKV2cp (6.75, Accept) — stronger empirical rigor → SepNN paper is notably weaker

The paper is positioned between the 5.00 and 6.00 anchors. The unresolved complexity analysis prevents it from reaching acceptance-level confidence, but the theoretical contributions (approximation theorem, NTK regimes) are genuine and novel.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>