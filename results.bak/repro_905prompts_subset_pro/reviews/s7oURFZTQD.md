Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary
This paper proposes Multi-Grade Deep Learning (MGDL), a training framework that decomposes end-to-end neural network optimization into a sequence of shallower subproblems, each trained on the residuals of previous grades. The authors provide convergence theorems for gradient descent under MGDL, a convex reformulation for single-layer ReLU grades, and an eigenvalue-based analysis linking the spectrum of \(\mathbf{I} - \eta\mathbf{H}\) to training stability. Experiments span image regression, denoising, deblurring, CIFAR classification, and time series prediction with transformers, showing MGDL consistently outperforms standard end-to-end (SGDL) training.

## Strengths
- **Convincing empirical evidence across diverse tasks and architectures**: Tables 1–3 and Figures 2–8 demonstrate consistent PSNR gains for MGDL over SGDL on image regression (0.42–3.94 dB), denoising (0.16–4.23 dB), deblurring (0.85–2.84 dB), and orders-of-magnitude lower training loss on CIFAR-100 with CNNs. The multi-grade transformer (MGT) in Section 8 shows dramatically better test-time generalization on synthetic and financial time series. The breadth of settings lends credibility to MGDL as a generally applicable training strategy.
- **Eigenvalue monitoring provides a useful diagnostic for training stability**: Section 7 tracks eigenvalues of \(\mathbf{I} - \eta\mathbf{H}\) during GD across synthetic regression, image regression, denoising, and CIFAR-10. The consistent pattern — SGDL eigenvalues frequently drop below \(-1\) while MGDL eigenvalues remain in \((-1,1)\) — offers a plausible empirical explanation for why MGDL training loss decays smoothly while SGDL oscillates.
- **Systematic learning-rate robustness study**: Section 6 (Figure 2) shows MGDL maintains low training loss over a substantially wider learning-rate range than SGDL on synthetic and image regression tasks trained with GD. The high-frequency setting is particularly striking: SGDL converges only at \(\eta \approx 0.005\) while MGDL remains stable at \(\eta \in [0.08, 0.3]\).
- **Convex reformulation of deep ReLU networks via multi-grade decomposition**: Theorem 3 shows that when each grade is a single-hidden-layer ReLU network with sufficient width, the nonconvex training decomposes into a sequence of convex programs, extending convexification techniques from shallow to deep architectures through the multi-grade structure.

## Weaknesses

### Major
- **Convergence theorems assume smooth activations; all experiments use ReLU**: Theorems 1, 2, and 4 all require \(\sigma\) to be twice continuously differentiable (lines 110, 128, 162, 313). The paper explicitly defines the architecture with ReLU activation \(\sigma(x) = \max\{0,x\}\) (line 94) and every experiment—image reconstruction, CIFAR, synthetic regression, eigenvalue analysis—uses ReLU networks. The paper never acknowledges this mismatch, nor does it discuss whether the results extend via subgradient analysis or smoothing approximations. The abstract's claim of "rigorous theoretical guarantees" is therefore overstated. The eigenvalue analysis in Section 7 computes Hessians for ReLU empirically (line 315: "Explicit Hessians for SGDL and MGDL under ReLU are given in the Supplementary Material"), which is a valid empirical contribution, but the convergence guarantees of Theorems 1–2 do not formally apply to the setting studied.
- **Section 5 experiments use Adam while the theoretical framework is built for gradient descent**: The image reconstruction and CIFAR-100 experiments (Section 5, line 212) use Adam. The convergence theorems, learning-rate analysis (Section 6), and eigenvalue analysis (Section 7) are all developed for full-batch gradient descent. While Sections 6–7 do use GD (on smaller architectures), the main empirical results in Section 5 are disconnected from the theoretical claims. The paper does not argue that the GD-based analysis carries over to Adam dynamics, weakening the claimed theory-practice bridge.
- **The claim \(\alpha_l \ll \alpha\) is unsubstantiated**: The key theoretical distinction between MGDL and SGDL rests on the assertion that the per-grade Hessian bound \(\alpha_l\) is much smaller than the full-network bound \(\alpha\) (line 170). No bound, estimate, or quantitative comparison is provided. Shallowness of subproblems does not automatically imply a smaller Hessian spectral norm, since the input features \(\mathbf{x}_{l,n}\) to later grades are outputs of fixed nonlinear networks with unknown scaling.

### Minor
- **Eigenvalue analysis is observational rather than explanatory**: Section 7 convincingly shows that eigenvalue excursions correlate with loss oscillations, and that MGDL avoids these excursions. However, the paper does not analytically explain *why* MGDL keeps eigenvalues in \((-1,1)\) — it observes the phenomenon without proving the mechanism. Theorem 4 provides sufficient conditions for convergence of the linearized iteration (\(\tau < 1\)) but does not prove these conditions hold for MGDL in general. The claim that "the smallest eigenvalue predominantly determines loss behavior" is justified only by visual inspection of the plots.
- **Convex reformulation conditions are practically severe**: Theorem 3 requires \(m_l \geq P_l\) where \(P_l\) (the number of sign patterns) can grow exponentially with the number of data points \(N\). The paper is honest about the condition but does not discuss its practical severity. Additionally, the reformulation applies to single-hidden-layer ReLU grades, whereas experiments use grades with multiple hidden layers. The result is a genuine theoretical contribution but has limited bearing on the experimental settings.
- **Missing comparisons to alternative progressive training schemes**: The paper compares MGDL only against end-to-end SGDL. Greedy layer-wise training (Bengio et al., 2006, cited in passing) and other progressive or boosting-style methods are natural baselines for a sequential residual-fitting scheme. Without them, it is difficult to isolate what MGDL offers beyond the well-studied idea of sequentially fitting residuals.
- **Multi-grade transformer section is disconnected from the stability narrative**: Section 8 shows promising results but provides no eigenvalue analysis, learning-rate study, or stability investigation for MGT. The architectural comparison (single-block-per-grade MGT vs. multi-block SGT) is not detailed in the main text, making fairness hard to assess.

### Trivial
- Architectures "26", "27", "28", "29" are referenced but not described in the main body (presumably defined in the stripped appendix), making the experimental setup hard to follow from the main text alone.
- Loss oscillation differences between SGDL and MGDL are described qualitatively but never quantified or tested for statistical significance across seeds.

## Nice-to-Haves
- Running the Section 5 experiments with full-batch GD (perhaps on smaller datasets) would bridge the Adam-GD gap and connect the main empirical results to the eigenvalue analysis.
- A quantitative study of how the Hessian spectrum evolves under Adam for MGDL vs. SGDL would assess whether the eigenvalue observations generalize beyond GD.
- Adding greedy layer-wise training or a simple sequential residual fitting baseline would strengthen the empirical contribution and better isolate the effect of the multi-grade scheme.
- Discussing whether the smoothness assumption in Theorems 1–2 can be relaxed (e.g., via Clarke subdifferentials or smoothed approximations of ReLU) would acknowledge the theory-practice gap and point toward resolution.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"The theoretical backbone of the paper does not apply to any of the settings it claims to explain"** — Overstatement. The eigenvalue analysis (Section 7) computes Hessians for ReLU networks empirically and is a valid empirical contribution that doesn't depend on the smoothness theorems. The convex reformulation (Theorem 3) explicitly handles ReLU. The learning-rate study (Section 6) is purely empirical. Removed as too sweeping.
- **"Architectures 26-29 are not described in the main body" as a major flaw** — The appendix is stripped by the parser; the original submission presumably contains these definitions. Moved to Trivial.
- **"No error bars or statistical testing"** — Standard for PSNR-based image reconstruction benchmarks at this scale. Demoted to Trivial.
- **"The observation that SGDL oscillates may be an artefact of Adam hyperparameters"** — Speculative without evidence. Removed.
- **"Theorem 1 is a direct application of the standard descent lemma; α is never instantiated"** — The descent lemma is a standard tool; the paper's contribution is applying it to the MGDL structure, not reinventing the lemma. Removed as overly dismissive.
- **Harsh critic's "Strengthening the Paper on Its Own Terms" suggestions to de-emphasize theory entirely** — Too prescriptive. The theory, even with acknowledged limitations, provides useful scaffolding. Moved to Nice-to-Haves in moderated form.
- **Strength Finder: "Convergence analysis with explicit learning-rate robustness" as a core strength** — Weakened by the smoothness mismatch. Kept in moderated form under eigenvalues, which is the stronger contribution.
- **Strength Finder: generic statements about "important problem" or "interesting question"** — Removed as non-specific.

## Novel Insights
The eigenvalue monitoring approach — tracking the spectrum of \(\mathbf{I} - \eta\mathbf{H}\) during training and linking eigenvalue excursions outside \((-1, 1)\) to loss oscillations — provides a compelling diagnostic framework. While the idea that eigenvalues crossing \(-1\) causes instability is not new in itself, the systematic comparison between SGDL and MGDL across multiple tasks reveals a consistent pattern: the multi-grade decomposition appears to naturally constrain eigenvalues within the stable range. This observation, while empirical rather than proven, suggests a concrete mechanistic hypothesis for why sequential residual fitting improves training stability that could inspire further theoretical work.

## Suggestions
- The paper would benefit from explicitly acknowledging that Theorems 1, 2, and 4 assume smooth activations and do not formally apply to ReLU. A discussion of whether the results extend (e.g., via smoothed ReLU approximations, subgradient analysis, or by noting that ReLU is differentiable almost everywhere) would substantially improve the paper's intellectual honesty without requiring new proofs.
- If possible, run a subset of the Section 5 experiments with full-batch GD to demonstrate that the eigenvalue observations carry over to the main empirical settings, or empirically verify that Adam trajectories exhibit similar eigenvalue behavior.
- Quantify the oscillation differences (e.g., variance of loss over the last N iterations) to move beyond qualitative claims.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Three ways that non-differentiability affects NN training (Zap3nZhRIQ) | 3.00 | R1 | Our paper has broader empirical evidence and a clearer positive contribution |
| Block Coordinate Descent for NNs (n2RIkaf1S4) | 4.00 | R1 | Similar structure (block-wise training + convergence theory) but our paper has much broader experiments |
| Can Stability be Detrimental? (zPaTnGjgpa) | 4.20 | R2 | Both study stability via eigenvalues; our paper has more empirical breadth and a clearer training recipe |
| On the Power of Multitask Representation Learning (6Ey8mAuLiw) | 5.25 | R1 | Similar theory-empirics structure; our theory is less tight but empirical scope is broader |
| Gradient descent for matrix factorization (fAGEAEQvRr) | 5.50 | R2 | Tighter theory for a simpler setting; our paper trades theoretical precision for empirical breadth |
| A Precise Characterization of SGD Stability (UMOlFJzLfL) | 5.75 | R2 | Cleaner, more rigorous theory-empirics connection; accepted |
| How do students become teachers (25j2ZEgwTj) | 6.00 | R1 | Tighter, more rigorous theory scoped to a specific setting; accepted |

**Round-1 bracket**: 3.5–6.0. The paper is clearly stronger than the weak anchors (3.0–3.5) but not as theoretically tight as the strong anchors (6.0+).

**Round-2 narrowing**: The paper sits below the 5.25–5.75 anchors. The "Precise Characterization of SGD Stability" (5.75) had a cleaner contribution with tighter theory-empirics connection. The "Can Stability be Detrimental?" paper (4.20) had a similar gap between claimed mechanism and demonstrated evidence. Our paper is stronger than 4.20 (broader experiments, convex reformulation, concrete training method) but weaker than 5.25–5.75 (smoothness mismatch in theorems, Adam-GD disconnect, unsubstantiated α_l ≪ α claim). Score: **5.0**.

The paper makes genuine contributions — the multi-grade decomposition is a practical training strategy, the eigenvalue monitoring provides a useful diagnostic, and the empirical evidence is broad and consistent. However, the convergence theorems do not apply to ReLU (the activation used in every experiment), and the paper never acknowledges this gap. The main experiments use Adam while the theory is for GD. These issues prevent the paper from delivering the "rigorous theoretical guarantees" it promises, pulling the score below the acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>