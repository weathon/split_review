Now let me produce the final formatted review with proper anchor documentation.

**Calibration Summary:**

All anchors retrieved from `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/`:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 2NwHLAffZZ.md | 2.33 | R1 | Much weaker — paper has unclear core contribution; our paper's theory is cleaner |
| xA25Ib7H8U.md | 2.33 | R1 | Much weaker — geometric theory paper not directly comparable |
| xpmDc76RN2.md | 2.33 | R1 | Much weaker — operator network optimization, narrow scope |
| xw3fStKCwm.md | 3.75 | R1 | Somewhat weaker — tensor decomposition for compression, no NTK analysis |
| mbo4YnWCHd.md | 4.25 | R1 | Somewhat weaker — tensor mixture learning, no neural network theory |
| 6aRMQVlPVE.md | 4.33 | R1 | Somewhat weaker — tensor rank pruning, no NTK/preconditioning theory |
| **TNYLCF7vZA.md** | **4.75** | **R1/R2** | **Most comparable — NTK preconditioning for INR spectral bias; similar method contribution but our paper has stronger theory (approximation theorem)**
| **2C3CWCPxNS.md** | **5.00** | **R1/R2** | **Comparable — preconditioning for PINNs; more experiments but weaker theory; rejected for math concerns in some reviews**
| YN4uWzcbtt.md | 4.25 | R2 | Somewhat weaker — pure NTK positive definiteness, narrow contribution |
| h7GAgbLSmC.md | 7.00 | R1/R2 | Stronger — cleaner theoretical analysis with sharper guarantees |
| QibPzdVrRu.md | 6.50 | R1 | Stronger — clean theoretical analysis of neuron alignment |
| 88rjm6AXoC.md | 6.25 | R1 | Stronger — well-executed pruning method with solid theory |
| **VEJzjAvaIy.md** | **5.75** | **R2** | **Stronger — accepted; cleaner NTK theory with clear result, but more incremental contribution** |
| 4xWQS2z77v.md | 8.00 | R1 | Much stronger — polished theory, accepted with high scores |
| STUGfUz8ob.md | 7.60 | R1 | Much stronger — clean theory, accepted |
| fMTPkDEhLQ.md | 8.00 | R1 | Much stronger — tight bounds, accepted |

**Round-1 bracket:** Based on the calibration, the paper sits between the weak-reject range (~4.75-5.00) and the weak-accept range (~5.75). The most informative anchors are the INR spectral bias paper (4.75, Reject) and the PINN preconditioning paper (5.00, Reject).

**Round-2 narrowing:** Comparing directly to the 4.75 anchor (inductive gradient adjustment for spectral bias): that paper was rejected for insufficient novelty relative to Geifman et al. (2024) and poor presentation. Our paper has a stronger theoretical contribution (the approximation theorem is genuinely novel and clean) and better presentation, but also has more significant concerns (the NTK scaling issue and overclaimed "provably" language). The 5.00 PINN preconditioning anchor was rejected partly due to questionable mathematical rigor. Our paper's theory is sounder, but the NTK scaling gap is a real concern.

**Final calibration:** The paper is slightly above the 4.75 anchor (stronger approximation theory, clearer presentation) but below the 5.75 anchor (which had a sharper, more complete theoretical result). This places it at **5.0** — a weak reject.

---

## Summary

This paper makes three contributions concerning separable neural networks (SepNNs): (1) a universal approximation theorem for CP, TT, and Tucker SepNNs using a Stone-Weierstrass argument that extends prior bivariate-only results to D≥2, (2) an NTK regime analysis under infinite-width/infinite-rank and infinite-width/fixed-rank asymptotics, and (3) a separable preconditioned gradient descent (SepPGD) that reduces preconditioning complexity from O(n^D) to O(nD) for n^D grid samples.

## Strengths

- **Clean multivariate universal approximation theorem (Theorem 1).** The proof combines Stone-Weierstrass with standard universal approximation for factor MLPs, extending prior work (Cho et al., 2023) from D=2 to D≥2 and unifying CP, TT, and Tucker forms under a single framework. The proof strategy is simpler than the orthogonal-basis approach in prior art.

- **Exponential complexity reduction via SepPGD (Table 1, Remark 4).** SepPGD achieves O(nD) per-iteration complexity compared to O(n^D) for standard NTK-based PGD (Geifman et al., 2024) and O(n^D/p) for the mini-batch variant (Shi et al., 2025). Preconditioner construction drops from O(n^{3D}+n^{2D}P) to O(D(n^3+n^2P)). The change from exponential to linear scaling in D is a substantial practical advantage for higher-dimensional problems.

- **Lemma 2 (equivalence for D=2 via Kronecker algebra).** The proof that SepPGD for D=2 equals the classical NTK-based PGD update with a Kronecker-structured preconditioner, and the insight that applying it via vec(ABC) in O(n) space is exponentially cheaper than (C^T⊗A)vec(B) in O(n²) space, is a clean, well-motivated algorithmic contribution that bridges the new method with established theory.

- **Honest treatment of the fixed-rank regime (Corollary 1, Remark 3).** The paper explicitly acknowledges that under finite rank (the practically relevant setting), the NTK remains random and "training dynamics can not be characterized uniformly using a fixed NTK matrix." This candid discussion of a limitation strengthens the paper's credibility.

## Weaknesses

### Major

1. **The 1/√R scaling causes the network output to diverge as R→∞, creating tension with standard NTK convergence guarantees.** The SepNN output is f = (1/√R) Σ_r ∏_d (f_{Θ_d})_r. Each (f_{Θ_d})_r = O(1) under the stated 1/√W initialization. Each product term is O(1), so the sum is O(R), and with 1/√R scaling, f = O(√R). As R→∞, the output diverges. Classical NTK theory (Jacot et al., 2018; Arora et al., 2019a) assumes the network output is O(1) at initialization for well-behaved gradient dynamics and a convergent NTK. While Lemma 1 shows the NTK formula acquires a compensating 1/R factor, the paper's footnote 1 ("we introduce a scaling factor 1/√R in the SepNN to ensure the convergence of NTK") provides only a brief justification. The main text does not explain how the standard NTK convergence proof adapts to the diverging-output regime. The appendix (Sections A.6–A.7) likely contains the derivation but is not available for verification. This is a significant gap in the NTK contribution.

2. **The "provably" claim for SepPGD's spectral bias alleviation is not commensurate with what is demonstrated.** The abstract states: "we propose an efficient separable preconditioned gradient descent (SepPGD) for optimizing SepNN, which alleviates the spectral bias of SepNN by provably adjusting its NTK spectrum." However, the actual evidence is substantially weaker:
   - Lemma 2 (equivalence to classical NTK-based PGD) is proved only for **D=2**.
   - The spectrum adjustment argument (line 201) depends on Lemma 3, which is in the appendix and not stated in the main text, and on the *supposition* that "K̃ is close to the true NTK matrix K."
   - Extensions to D>2 are stated as "It is believed that the result... can be readily extended."
   - Convergence and solution consistency are explicitly "left for future research" (line 202).
   The word "provably" in the abstract claims more than what is actually established in the main paper.

### Minor

3. **The approximation theorem is an existence result without rates.** Theorem 1 shows that for any ε>0 there exists a SepNN with some rank R approximating the target function, but does not bound the required rank R as a function of ε and the target function's smoothness. This limits its practical implications.

4. **The three contributions are largely disconnected.** The approximation theory (Section 2) is never used in the NTK analysis or the SepPGD design. It is a standalone result — interesting but orthogonal to the paper's other claims.

5. **Experimental evaluation lacks statistical rigor.** Beyond the NTK verification in Fig. 1 (10 seeds), the main experimental results (KRR, image/surface INR, PINNs) do not report error bars or statistical significance. Ablation studies on key hyperparameters (eigenvalue truncation k, preconditioner update frequency) are absent from the main paper.

6. **The SepPGD construction complexity for D>2 includes an O(n^{D-1}) term** (footnote 3, line 187). The paper argues this is "orders of magnitude less expensive" than O(n^{3D}), which is plausible, but the gap between the headline O(nD) application complexity and the O(n^{D-1}) construction term is not analyzed. For D=3 and moderate n, this term could be significant.

### Trivial

None.

## Nice-to-Haves

- Provide approximation rates linking required rank R to target function smoothness and dimension D.
- Include a convergence analysis for SepPGD at least for D=2.
- Add tabular summaries of final metrics with standard deviations in the main paper.
- Discuss when SepPGD might not help (e.g., small n, non-grid inputs, finite width/small rank).

## Removed Points

- **"Wall-clock comparison conflates two comparisons"** (Harsh Critic): REMOVED. Plotting convergence against execution time rather than iteration count is the *correct* way to compare methods with different per-iteration costs. This is a strength, not a weakness.
- **"Experimental details relegated to appendix"** (Harsh Critic): REMOVED. Standard practice given page limits; the main paper shows convergence curves and quantitative metrics (PSNR, IoU, MSE).
- **Formatting/style nitpicks, grammar comments, missing related works, missing appendix complaints:** REMOVED per policy.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's identification of the 1/√R scaling issue is the most insightful observation — it is a genuinely subtle mathematical point that the paper does not adequately address, and it is not a standard criticism that would apply to most papers.

## Suggestions

1. **Address the NTK scaling issue** by either (a) adopting 1/R scaling and re-deriving the limiting kernel, (b) providing a rigorous justification for why the standard NTK convergence proofs still apply when the output is O(√R), or (c) transparently discussing this as a limitation.

2. **Calibrate the "provably" language** to match what is actually proved. Replace "provably adjusts" with "can adjust" or "empirically improves" unless the full proof (including Lemma 3) is presented in the main text.

3. **Add error bars** to all main experimental results and include ablation studies on key hyperparameters.

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>