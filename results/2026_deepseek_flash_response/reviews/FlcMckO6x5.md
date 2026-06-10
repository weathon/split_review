## Final Review — Separable Neural Networks: Approximation Theory, NTK Regime, and Preconditioned Gradient Descent

### Summary
This paper makes three contributions to separable neural networks (SepNNs): (1) a universal approximation theorem covering CP, TT, and Tucker decompositions for any D≥2, proven via Stone-Weierstrass + standard UAT; (2) characterization of SepNN NTK regimes (deterministic under infinite width+rank, random under fixed rank); and (3) a separable preconditioned gradient descent (SepPGD) algorithm achieving O(nD) complexity for n^D training samples versus O(n^D) for prior NTK-based PGD methods, with Lemma 2 proving equivalence to classical PGD in the bivariate case.

### Strengths
- **Universal approximation theorem for all three SepNN variants (CP, TT, Tucker) with any D≥2**, going substantially beyond prior bivariate-only results (Cho et al., 2023). The proof via Stone-Weierstrass + standard universal approximation theory is clean, unified, and applicable to non-polynomial activation functions.
- **Two distinct NTK regimes (deterministic under infinite width+rank, random under fixed rank)** providing new theoretical insights into SepNN training dynamics. This fills a gap in the literature where SepNNs previously lacked any theoretical account of their optimization behavior. Figure 1 provides clear empirical validation with multiple seeds — the only experiment with proper statistical reporting.
- **SepPGD with O(nD) per-iteration complexity**, an exponential improvement over the O(n^D) cost of standard NTK-based PGD (Geifman et al., 2024). Lemma 2 proves equivalence to classical PGD for D=2, meaning the algorithmic speedup does not sacrifice convergence guarantees in this case. The complexity reduction is clearly documented in Table 1.
- **Consistent empirical improvements across KRR, image/surface INRs, and PINNs**, with e.g., 7 dB PSNR improvement on image representation (Figure 3) and improved convergence across multiple PDEs.

### Weaknesses

#### Major
- **Overclaimed "provably" guarantee for SepPGD's spectral bias alleviation**: The abstract and introduction state that SepPGD "provably adjusts the NTK spectrum" and "provably alleviates spectral bias." However, Section 4's analysis (lines 199-201) uses hedging language throughout: "This can possibly be verified," "Suppose that...we can ultimately show," "It is believed that the result...can be readily extended," "This is left for future research." The equivalence to classical PGD is proven (Lemma 2, D=2), but the spectral bias alleviation argument goes through a chain (S̃ has better spectrum than K̃ → K̃ ≈ K → KS̃ has better spectrum than K) where the link from "K̃ ≈ K" to "KS̃ benefits" is asserted rather than formally established. For D>2, the extension is explicitly conjectural. This mismatch between advertised guarantees and actual evidence is the paper's most significant weakness. The SepPGD algorithm's complexity advantages and empirical performance are independently valuable and do not require this overclaiming.

- **Insufficient experimental rigor**: Convergence curves in Figures 2-4 are presented without error bars, confidence intervals, or any measure of variance. Only Figure 1 reports multiple seeds. Single-run convergence curves are insufficient to substantiate claims of faster convergence, especially given the stochastic nature of neural network training. Additionally, no comparison is provided with standard optimizers (Adam, SGD with momentum, L-BFGS) for SepNN training, making it difficult to assess the practical utility of SepPGD relative to methods practitioners would commonly use.

#### Minor
- **NTK and SepPGD analysis restricted to CP SepNN without qualification in title/abstract**: The NTK analysis (Lemma 1, Theorem 2, Corollary 1) and SepPGD derivation are conducted exclusively for CP SepNNs. Footnote 1 acknowledges this but states the extension "can be readily extended" without providing it. The scope restriction should be stated more prominently — ideally in the title or abstract — rather than relegated to a footnote.

- **No guidance on hyperparameter k**: The preconditioner construction modulates k eigenvalues, but the paper provides no discussion of how to choose k or how sensitive performance is to this choice. Similarly, the interaction between decomposition rank R and SepPGD's effectiveness is not discussed.

- **Non-grid input caveat appears late**: Footnote 2 (line 158) mentions that for non-grid inputs SepPGD's complexity advantage disappears and it reduces to standard PGD. This caveat substantially narrows the method's applicability regime and should appear earlier and more prominently.

#### Trivial
- **Stone-Weierstrass condition misstated**: Line 82 says the theorem requires the algebra to "contain the identity function" when it should say "contain the constant functions." This is an expositional slip — the algebra manifestly contains constant functions — not a proof error.

### Nice-to-Haves
- A comparison with full NTK-based PGD for small D (e.g., D=2, n small) where the O(n^D) cost is manageable would directly validate whether the Kronecker-structured preconditioner retains the full preconditioner's effectiveness.
- A comparison with the mini-batch PGD of Shi et al. (2025) would contextualize SepPGD's efficiency advantages.
- Timing breakdowns (preconditioner construction vs. application) would substantiate the claimed complexity advantages beyond the asymptotic analysis.

### Removed Points
- The Harsh Critic's claim that PINN improvements are modest and that the benefit might come from SepNN architecture rather than SepPGD: **REMOVED** because both SepPINN and SepPINN+SepPGD use the same SepNN architecture, so the 0.042→0.037 improvement is directly attributable to SepPGD. The critic misinterpreted the comparison.
- The Harsh Critic's demand to compare SepPGD against full PGD for small D: **WEAKENED to Nice-to-Have** — this is a reasonable suggestion but not a missing requirement; the equivalence result (Lemma 2) already establishes theoretical alignment.
- The Harsh Critic's complaint about missing mini-batch PGD comparison: **WEAKENED to Nice-to-Have** for similar reasons.
- Strength Finder's general praise about "addressing an important problem": **REMOVED** as generic/superficial. Specific strengths were retained with supporting evidence.

### Novel Insights
None beyond the paper's own contributions. The reviewer inputs do not surface any synthesis that the paper itself does not already articulate.

### Suggestions
1. **Align the language with the evidence**: Replace "provably adjusts the NTK spectrum" in the abstract/introduction with precise statements about what is established (Lemma 2's equivalence result for D=2, the complexity reduction, and the empirical evidence). The algorithm is interesting and useful without the overclaiming.
2. **Add error bars to all experimental results**: A minimum of 3-5 random seeds is standard practice for convergence experiments.
3. **Include standard optimizer baselines** (Adam, SGD with momentum) for SepNN training to contextualize SepPGD's performance.
4. **State the CP-restricted scope** of the NTK and SepPGD analyses explicitly in the title or abstract.
5. **Discuss the choice of k** (eigenvalue modulation count) and how it affects performance, ideally with an ablation study.

### Score and Decision

**Calibration Anchors** (retrieved from human-review corpus):

| Paper | Avg Score | Round | Comparison to this paper |
|-------|-----------|-------|------------------------|
| Optimal NN Approximation (G2Lnqs4eMJ) | 2.50 | R1 (weak) | Much weaker — niche incremental theory, poor writing |
| KAN Variable Basis (IqaQZ1Jdky) | 2.50 | R1 (weak) | Much weaker — marginal improvements, poor comparisons |
| Weak Correlations (2NwHLAffZZ) | 2.33 | R1 (weak) | Much weaker — unclear contribution |
| Simplicity Bias (KNQJtoPZmz) | 3.00 | R1 (weak) | Different focus, weaker contribution clarity |
| **IGA Spectral Bias (TNYLCF7vZA)** | **4.75** | **R1/R2** | **Similar topic (NTK spectral bias + INRs). Our paper has stronger theoretical originality but similar overclaiming issue and better writing** |
| **Preconditioning PINNs (2C3CWCPxNS)** | **5.00** | **R1/R2** | **Similar topic (preconditioning for PINNs). Our paper's theory is sounder** |
| GD Matrix Factorization (fAGEAEQvRr) | 5.50 | R2 | Comparable — both have novel theory with experimental limitations and some overclaiming |
| Hessian-Free Natural GD (Oqk1Ui6m0n) | 5.00 | R2 | Different focus |
| **KAN Expressiveness+Spectral Bias (ydlDRUuGm9)** | **6.25** | **R2** | **Accepted. Very similar structure (theory + spectral bias + experiments). Our paper has more original theory but a more significant overclaiming flaw** |
| Equivariant Tensor (kyVzYpDxHg) | 5.75 | R2 | Different focus |
| Min Width UAP (dpDw5U04SU) | 7.00 | R2 | Pure theory, accepted. Clean and well-executed but narrower scope |
| Hölder Stability GNNs (P7KIGdgW8S) | 8.00 | R1 (strong) | Pure theory, accepted. Much stronger | 

**Round 1 bracket:** [4.5, 6.5] — clearly above the weak band (~2.5) and below the strong band (7.5+)

**Round 2 narrowing:** The paper sits between the IGA paper (4.75, rejected) and the KAN paper (6.25, accepted). It is comparable to the 5.50 matrix factorization anchor (rejected): both have genuine theoretical contributions undermined by overclaimed framing and limited experimental validation.

**Final determination:** Score 5.5, Decision Reject. The paper's theoretical contributions (UAT and NTK regimes) are solid and represent meaningful progress. However, the central algorithmic claim is overstated relative to what is actually proved, and the experimental evaluation lacks the rigor (no error bars, missing standard baselines) needed to support the convergence claims at a top venue. The paper could be a strong submission after (a) aligning the language with what is actually proven, (b) adding proper experimental methodology, and (c) including standard optimizer baselines.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>