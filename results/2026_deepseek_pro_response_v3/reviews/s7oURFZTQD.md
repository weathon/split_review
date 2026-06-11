Now I have a good calibration picture. Let me finalize.

**Round 2 comparison:**
- **Multiscale Training (5.75, Reject):** Novel training method + theory, but limited experiments (shallow nets, small datasets). My paper has broader experiments but weaker theory.
- **Spectral Dynamics (6.25, Reject):** Empirical spectral analysis across tasks, criticized for being largely descriptive. My eigenvalue analysis is similar in spirit but my paper additionally tries (incompletely) to provide theoretical justification.
- **Feature Learning SGD (6.25, Accept):** Systematic theoretical + empirical framework with clear scaling laws. My paper's theory is less systematic and less well-connected to experiments.

My paper lands between the Multiscale paper (5.75) and Spectral Dynamics (6.25) in empirical breadth, but with theory gaps that push it toward the lower end. **Final score: 5.0.**

Now let me write the final review.

---

## Summary
This paper provides theoretical and empirical arguments for why Multi-Grade Deep Learning (MGDL) — which decomposes end-to-end training into sequential shallow-network stages trained on residuals — outperforms standard single-grade training (SGDL). It presents convergence theorems for GD, a convex reformulation for single-layer ReLU grades, an eigenvalue-based analysis of training stability, and experiments spanning image reconstruction, classification, and transformer time-series prediction.

## Strengths
- **Broad architecture coverage with consistent advantage:** The paper tests MGDL across fully connected networks (image regression, denoising, deblurring — Tables 1–3), CNNs (CIFAR-100), and transformers (MGT on synthetic and SPX time series — Tables 4–5), showing MGDL outperforms SGDL in every comparison. The transformer extension to financial time series is particularly novel, where MGT achieves test MSE of 0.018 vs. 0.089 for SGT and maintains accuracy under distribution shift where SGT collapses entirely (Figures 7–8).
- **Eigenvalue monitoring across four task types:** The paper tracks eigenvalues of I−ηH during training across synthetic regression (Figures 4, 21), image regression (Figure 5), image denoising (Figures 26–29), and CIFAR-10 (Figure 6). The consistent pattern — SGDL eigenvalues exit (−1,1) coincident with loss oscillations while MGDL eigenvalues stay inside — provides a genuinely informative empirical observation about why MGDL training is more stable.
- **Quantified learning-rate robustness:** Section 6 reports specific admissible LR intervals. For high-frequency synthetic data, SGDL converges only near η≈0.005 while MGDL remains stable with loss <0.01 for η∈[0.08,0.3]. For low-frequency data, MGDL sustains performance across η∈[0.01,0.3] vs. SGDL's η∈[0.03,0.08]. These numeric ranges give actionable guidance.
- **Wall-clock efficiency:** On CIFAR-10 with full-batch GD, MGDL reaches lower loss (2.56×10⁻³ vs. 7.16×10⁻³) in less time (22,177s vs. 26,878s). MGT trains in 741s vs. 2,693s (synthetic) and 972s vs. 1,712s (SPX) while achieving better test performance.

## Weaknesses

### Fatal
None.

### Major
- **Classification experiments omit standard metrics:** CIFAR-100 and CIFAR-10 experiments report only training MSE loss. MSE is non-standard for classification and training loss alone cannot measure generalization. The paper reports no test accuracy, top-1 error, or any classification metric. For a paper promising "broad empirical improvements," this omission substantially weakens the classification evidence. Section 5's CIFAR-100 results (Figure 3) show training loss curves but zero information about whether MGDL actually classifies better.
- **The core theoretical advantage is unsubstantiated:** Theorems 1 and 2 prove the same convergence result for both SGDL and MGDL. The claimed MGDL advantage rests entirely on the assertion that α_l ≪ α (per-grade Hessian norm is much smaller than full-network Hessian norm) — stated in Section 3 without proof, quantitative bounds, or any connection to network architecture. This is the only comparative theoretical content, and it is an unbacked claim.
- **Disconnect between GD theory and Adam experiments:** Sections 2–4 and 7 develop theory exclusively for gradient descent. Sections 5–6 use the Adam optimizer. The paper never acknowledges or bridges this gap. Adam's adaptive per-parameter learning rates and momentum fundamentally alter optimization dynamics, so the GD eigenvalue analysis does not directly explain the Adam-based experimental results claimed throughout Sections 5–6.

### Minor
- **Convex reformulation (Theorem 3) is incremental and unused:** The proof follows Pilanci & Ergen (2020) essentially verbatim. The extension to deep architectures via MGDL decomposition is structurally straightforward — each grade is a shallow network, so each inherits convexification. The resulting convex program has P_l regions growing exponentially in input dimension; this infeasibility is never discussed. The result is never solved or empirically demonstrated, even on a toy problem. It reads as a theoretical ornament.
- **Eigenvalue analysis is heuristic, not rigorous:** Section 7 uses local linearization around the previous iterate to draw global conclusions about convergence from eigenvalue spectra. The derivation is valid as a first-order approximation but the paper presents the eigenvalue mechanism as a causal explanation without acknowledging the limitations of the linearization. The correlation between eigenvalues and loss is empirically informative but the causal claim is not rigorously established.
- **Eigenvalue experiments use different learning rates:** Figure 4 compares SGDL at η=0.08 against MGDL at η=0.06; Figure 5 compares η=0.02 against η=0.2. While Section 6 systematically varies LR, the eigenvalue comparisons at different LRs conflate eigenvalue effects with LR effects.
- **No error bars or statistical significance:** All tables report single numbers. Variance across random seeds is not reported for any experiment.

### Trivial
- The twice-continuously-differentiable σ assumption in Theorems 1–2 conflicts with ReLU activations used throughout experiments. This is a standard tension in DL theory but should be acknowledged.
- Architecture details for CNN experiments and transformer setups reference equations in the stripped appendix, making experimental setup hard to verify from the main text.

## Nice-to-Haves
- Report test accuracy for CIFAR-100 and CIFAR-10 classification experiments.
- Provide quantitative bounds or empirical evidence for the α_l ≪ α claim, or reframe Theorems 1–2 as establishing parity rather than advantage.
- Acknowledge the Adam/GD disconnect explicitly, or run a subset of key experiments with GD to bridge theory and practice.
- Reframe the eigenvalue analysis honestly as an empirical observation rather than a theoretical explanation of the mechanism.
- Either demonstrate the convex program empirically (even on a toy problem) or acknowledge its practical infeasibility and reposition it as a conceptual insight.
- Add standard deviations across random seeds.
- Discuss relationship to greedy layer-wise pretraining (Bengio et al., 2006) more substantively.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Fundamental algebraic mistake in eigenvalue analysis":** The harsh critic claimed the Taylor expansion ∂F/∂W(W^k) = H_F(W^{k−1})W^k + u^{k−1} + r^{k−1} replaces (W^k−W^{k−1}) with W^k and is a "category error." This is incorrect. A correct first-order Taylor expansion: ∇F(W^k) = ∇F(W^{k−1}) + H(W^{k−1})(W^k−W^{k−1}) + remainder = H(W^{k−1})W^k + [∇F(W^{k−1})−H(W^{k−1})W^{k−1}] + remainder, which matches the paper's form. The algebra is valid. REMOVED as a factual error by the reviewer.
- **"Data leakage" concern about SPX data through August 2025:** Speculation about model training cutoffs; not a valid methodological criticism. The dataset endpoint is explicitly stated. REMOVED.
- **"SGT is severely misconfigured" because test MSE gap is too large:** Speculation. The paper reports what it reports; inferring misconfiguration without evidence is not valid criticism. REMOVED.
- **"No comparison to greedy layer-wise pretraining":** Moved to Nice-to-Haves as a suggestion rather than a weakness, since the paper does cite Bengio et al. 2006 and the contribution is framed around MGDL specifically.
- **"Architectures not equated in depth" for image experiments:** Upon verification, SGDL (2,1,128,8) has 8 hidden layers; MGDL (2,1,128,2,4) has 4 grades × 2 layers = 8 hidden layers. SGDL (2,1,128,12) vs MGDL (2,1,128,3,4) = 12 hidden layers each. Total depth is matched. The structural difference (sequential vs. joint training) is the variable under study, not a confound. REMOVED.
- **"Memory cost claim needs qualification":** The paper does claim lower memory cost (Section 3: "its memory cost is much lower than that of a single deep network, since each grade trains only a shallow model"). The harsh critic noted feature maps must be cached. This is a reasonable engineering concern but not a substantive weakness — the paper's claim is directionally correct. DEMOTED and not included as a standalone weakness.

## Novel Insights
The eigenvalue monitoring across four task types, showing a consistent pattern where SGDL eigenvalues cross below −1 in tandem with loss oscillations while MGDL eigenvalues stay within (−1,1), provides an empirically grounded narrative for MGDL's stability that goes beyond prior MGDL papers. The transformer extension (MGT) with distribution-shift results on financial data is a genuinely novel demonstration that the multi-grade decomposition can improve transformer generalization under covariate shift in ways not previously shown for this architecture family. These two empirical contributions are the paper's strongest.

## Suggestions
- The strongest contribution is the empirical eigenvalue monitoring and the transformer results. Consider restructuring the paper to lead with these empirical findings and position the convergence theorems and convex reformulation as supporting context rather than central contributions. Currently the theory sections (2–4) occupy substantial space but deliver limited comparative insight.
- For the Adam/GD disconnect, either add a brief discussion acknowledging the gap and citing work on why GD intuitions sometimes transfer to adaptive methods, or run a subset of experiments (e.g., the synthetic regression from Section 6) with GD to directly bridge theory and practice.
- The convex reformulation (Theorem 3) could be cut or moved to an appendix without weakening the paper's core narrative, freeing space for more substantive empirical analysis.

## Score and Decision

**Round 1 bracket:** 5.0–6.5. The paper is stronger than anchors at 4.00 (BCD paper — circular proofs, weak experiments) and 5.00 (PL paper — incremental, two-layer only, no experiments), but weaker than 7.00 (Sharper Guarantees — genuinely novel tighter bounds, theory-verified experiments) and 8.00 papers (accepted with strong reviews across the board).

**Round 2 narrowing:** Compared against Spectral Dynamics (6.25, Reject — broad empirical spectral analysis but criticized as descriptive with weak theoretical foundation) and Multiscale Training (5.75, Reject — novel method + theory but limited experiments). My paper has broader empirical coverage than Multiscale Training and a concrete method (MGDL) rather than purely descriptive analysis, but its theory is less novel and less rigorous than either anchor's. The classification experiments are weaker than what either anchor provides. The Adam/GD disconnect and unproven α_l ≪ α claim pull the paper below 6.0.

**Anchor summary:**
| Anchor | Score | Round | Comparison |
|---|---|---|---|
| n2RIkaf1S4 (BCD paper) | 4.00 | R1 | Worse — circular proofs, very limited experiments |
| O0FOVYV4yo (PL paper) | 5.00 | R1 | Worse — incremental, two-layer only, no experiments |
| h7GAgbLSmC (Sharper Guarantees) | 7.00 | R1 | Better — genuinely novel bounds, theory-verified |
| n0YCAMVh8b (Multiscale Training) | 5.75 | R2 | Comparable — similar mix of theory + method + experiments; our paper slightly weaker on theory, broader on tasks |
| PJjHILiQHC (Spectral Dynamics) | 6.25 | R2 | Better — stronger empirical analysis; our paper weaker on theory rigor |
| iEfdvDTcZg (Feature Learning SGD) | 6.25 | R2 | Better — more systematic theory-experiment connection |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>