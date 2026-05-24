Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper provides theoretical and empirical analysis of Multi-Grade Deep Learning (MGDL), which decomposes end-to-end DNN training into a sequence of shallow subproblems trained on residuals. The paper presents convergence theory for smooth activations, a convex reformulation for ReLU single-layer grades, an eigenvalue analysis revealing why MGDL's iteration matrices stay within the stable (-1,1) spectral range, and experiments on image regression, denoising/deblurring, CIFAR classification, and time-series transformers — all showing consistent MGDL advantages.

## Strengths

1. **Eigenvalue analysis as a mechanistic explanation (Section 7, Figures 4–6).** The paper tracks the eigenvalues of I − ηH(W) during training and shows that MGDL's eigenvalues remain in (-1,1) across synthetic regression, image regression/denoising, and CIFAR-10, while SGDL's eigenvalues frequently drop below -1, causing oscillatory loss. This is the paper's most compelling insight and is directly verified on ReLU networks.

2. **Empirical breadth with consistent gains across diverse architectures (Tables 1–5, Figures 3, 7–8).** MGDL outperforms SGDL on 6 image regression tasks (PSNR gains 0.42–3.94 dB), 3 denoising tasks across 6 noise levels (gains 0.16–4.23 dB), 3 deblurring tasks, CIFAR-100 (training loss ~10⁻⁴ vs ~10⁻²), synthetic time series (TeMSE 0.16 vs 2.6), and SPX financial data (TeMSE 0.018 vs 0.089). This span across FCNs, CNNs, and transformers is impressive and rules out architecture-specific explanations.

3. **Convex reformulation for single-layer ReLU grades (Theorem 3).** The paper shows that when each MGDL grade is a single-layer ReLU network, the nonconvex problem decomposes into a sequence of convex subproblems, extending the Pilanci & Ergen (2020) convexification framework from shallow to deep architectures.

4. **Learning-rate robustness analysis (Section 6, Figure 2).** The paper quantifies that MGDL maintains low loss over a wider LR range (e.g., [0.01, 0.3] vs [0.03, 0.08] on synthetic data) and remains stable where SGDL diverges — a concrete practical advantage.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap: convergence theorems assume smooth activations while experiments use ReLU.** Theorems 1, 2, and 4 require σ (or F) to be *twice continuously differentiable* (lines 110, 128, 162, 313), but the paper defines ReLU as the activation (line 94) and uses it in all experiments (line 212). ReLU is not differentiable at 0 and has a discontinuous second derivative, so the convergence guarantees of Theorems 1 and 2 technically do not apply to the models trained and evaluated. The paper never acknowledges this gap or discusses its implications. This weakens the claim that MGDL "unites rigorous theoretical guarantees with broad empirical improvements" (Abstract). That said, the convex result (Theorem 3) explicitly handles ReLU, and the eigenvalue analysis in Section 7 is *computed* on ReLU networks (line 315: "Explicit Hessians for SGDL and MGDL under ReLU are given in the Supplementary Material") — so the issue is confined to Theorems 1–2 and the framing, not the entire theoretical apparatus.

2. **CIFAR-100 classification lacks test accuracy — the standard metric.** The CIFAR-100 section (lines 281–284) reports only *training loss* (MSE) and claims "superior accuracy," but no test accuracy is reported anywhere. For a classification benchmark, reporting accuracy is the expected standard; training loss alone (especially with MSE loss instead of cross-entropy) does not establish that MGDL generalizes better on classification. The same applies to CIFAR-10 (line 347), where only loss and training time are given.

3. **No parameter counts or capacity controls.** The paper never reports the total number of trainable parameters for SGDL vs. MGDL models in any experiment. Without this, it is impossible to determine whether MGDL's advantage comes from the multi-grade procedure itself or simply from differences in model capacity. For example, the transformer experiments (Section 8) compare MGT (multi-block, single-block per grade) vs. SGT (multi-block deep) without establishing parameter parity — an apples-to-oranges comparison risk. This is the single most actionable experimental omission.

### Minor

4. **No variance or statistical significance reported for any result.** No standard deviations, confidence intervals, or multi-seed runs are reported. For the time-series results, the test MSE gaps (0.16 vs 2.6 on synthetic; 0.018 vs 0.089 on SPX) are large enough to be credible, but the image results and CIFAR-100 loss would be much more convincing with variance estimates.

5. **CIFAR classification uses MSE loss instead of cross-entropy.** MSE is not the standard loss for classification (line 281). While the paper can choose its loss function, using MSE makes it harder to relate the results to the broader literature, and the absence of accuracy makes the classification experiments difficult to interpret.

6. **Convex program's exponential complexity not acknowledged.** Theorem 3's convex program (8) involves P_l activation regions — which can be exponential in N (the number of data points). The condition m_l ≥ P_l is therefore infeasible for realistically sized datasets. The paper presents this as "extending convexification from shallow to deep architectures" (line 206) without noting that the program is intractable. This is a well-known limitation of the Pilanci & Ergen framework, but it should be stated explicitly.

### Trivial

7. Notation in equation (3) uses `H_{D_{l-1}}` where the subscript could be read as depth or grade index — slightly ambiguous but decipherable from context.

## Nice-to-Haves

- Provide test accuracy (top-1) for CIFAR-100 and CIFAR-10 alongside the loss curves.
- Report parameter counts for every SGDL vs. MGDL pair to rule out capacity-driven gains.
- Add variance estimates over ≥3 random seeds for experimental results.
- Discuss the scope of the convex result (Theorem 3) by explicitly noting its exponential complexity.
- Acknowledge the smooth-activation assumption used in Theorems 1–2 and clarify how the eigenvalue analysis (Section 7) bridges the gap by computing on ReLU networks directly.

## Removed Points

These points were flagged by reviewers but are removed or demoted for the reasons stated below. Treat with caution.

- **"SGT baseline is undertuned" (Harsh Critic, time series critique):** Pure speculation. The paper reports that both MGT and SGT fit training data well (TrMSE 1.2×10⁻² vs 7.1×10⁻²), so the SGT is not obviously undertrained. Removed.
- **"Architecture descriptions deferred to appendix" (Harsh Critic):** The appendix is stripped by the parser; it exists in the original submission. Removed per hard rule.
- **"Linearization drops remainder unjustifiably" (Harsh Critic):** The paper explicitly says "Neglecting r^{k-1} gives the linearized update" (line 310) — this is a standard linearization, clearly stated. Removed.
- **"Analysis does not scale to practical models" (Harsh Critic):** The paper demonstrates eigenvalue analysis on CIFAR-10 with 3072-dim inputs and ~100K parameters, which is non-trivial. The claim is speculative. Removed.
- **"Notation issues / exposition nitpicks" (Harsh Critic, Section-by-Section):** Minor presentation preferences, not substantive weaknesses. Moved to Trivial where applicable.
- **"Transformer experiments only on time series" (Harsh Critic):** The paper explicitly introduces MGT for time series (line 353). Criticizing it for not covering NLP/vision is scope creep. Removed.
- **"10⁶ epochs is extreme" (Harsh Critic):** The paper is studying convergence properties, not practical deployment. The large epoch count is a deliberate experimental choice. Weakened to nice-to-have.

## Novel Insights

Neither reviewer surfaces an insight beyond the paper's own contributions. The paper's eigenvalue-based explanation for MGDL's stability is itself the most novel observation in the discourse.

## Suggestions

1. **Bridge the theory-practice gap explicitly.** Add a sentence after Theorems 1–2 noting that the convergence results assume smooth activations, while ReLU-specific analysis is provided in Theorem 3 (convexity) and the eigenvalue analysis (Section 7), which operates on ReLU Hessians numerically. This simple acknowledgment would defuse the most serious criticism.
2. **Report test accuracy for all classification experiments.** Without it, the classification claims are unconvincing.
3. **Add a table with parameter counts** for every architecture comparison in the paper, and comment on parity or the lack thereof.
4. **Scope the convex result.** Add a sentence noting that P_l can be exponentially large and the result is mainly of theoretical interest regarding the optimization landscape.

## Score and Decision

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**