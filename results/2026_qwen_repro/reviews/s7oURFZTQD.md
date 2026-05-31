Now I have a comprehensive understanding of the paper and the calibration anchors. Let me write the final review.

---

## Summary

This paper proposes a theoretical framework for Multi-Grade Deep Learning (MGDL), a sequential residual-fitting approach to deep network training. The authors prove convergence guarantees for gradient descent on MGDL showing wider admissible learning rate ranges compared to single-grade deep learning (SGDL), demonstrate that with single-layer ReLU grades the non-convex optimization reduces to a sequence of convex programs, and provide spectral analysis showing MGDL keeps iteration matrix eigenvalues within (-1, 1). Empirical results cover image regression, denoising, deblurring, CIFAR classification, and transformer-based time series forecasting.

## Strengths

- **Comprehensive theoretical toolkit.** The paper provides multiple complementary theorems: convergence analysis via Lipschitz constants of shallow subproblems (Theorems 1 and 2), convex reformulation for ReLU single-layer grades (Theorem 3, extending Pilanci & Ergen, 2020 to deep architectures via grade decomposition), and eigenvalue analysis of the GD iteration matrix (Theorem 4). These results are mathematically sound and address a coherent research question.

- **Effective spectral mechanistic explanation.** Section 7's tracking of eigenvalues during training provides a concrete explanation for MGDL's stability: Figures 4-6 show that MGDL keeps eigenvalues of I - ηH within (-1, 1) while SGDL's frequently drop below -1 (correlating with oscillatory loss). This observationally validates the theoretical claims and concretely links the "Edge of Stability" phenomenon to MGDL's behavior.

- **Strong Transformer results on distribution shift.** The Multi-Grade Transformer (MGT) experiments in Section 8 are the most practically compelling results: MGT achieves ~5× lower test MSE than SGT on financial SPX data under distribution shift (Table 5, 1.8e-2 vs 8.9e-2) while requiring only 33% of the training time. Figure 8 clearly shows SGT diverging from reality on test sequences while MGT remains accurate.

- **Consistent improvements across diverse tasks.** Tables 1-3 show MGDL outperforms SGDL on all tested image reconstruction tasks (regression gains of 0.42–3.94 dB, denoising gains of 0.16–4.23 dB, deblurring gains of 0.85–2.84 dB). Figure 2 demonstrates MGDL's robustness to learning rate across a wider range than SGDL.

## Weaknesses

### Fatal
None.

### Major

- **SGDL baseline lacks standard modern stabilization techniques, inflating MGDL's apparent advantage.** The paper compares MGDL against SGDL — fully connected networks with no residual connections, batch normalization, layer normalization, or warmup schedules. Section 5 uses "the fully connected architecture in equation 26" for SGDL vs. "the architecture in equation 27" for MGDL. These are vanilla deep networks trained with Adam or GD. In modern deep learning (even for comparable tasks), it is standard to include these stabilizations. The oscillations observed in SGDL Figures 2, 3, and 4 are consistent with what modern literature predicts *without* these mechanisms. If the same residual structure that MGDL provides (sum of shallow networks that effectively implements skip connections, see Section 3: output is $\tilde{g}_L = \sum_l g_l$) were added to SGDL, the baseline would likely be substantially more competitive. This is a significant concern because MGDL's architecture is structurally equivalent to a residual network: each grade adds a new set of layers whose output is summed over previous grades (Figure 1 and Section 3). The paper never addresses this correspondence or compares against a ResNet-style baseline.

- **Convexity theorem (Theorem 3) is never used in practice.** The primary theoretical novelty — showing that MGDL with single-layer ReLU grades reduces to a sequence of convex programs (Equation 8) — is disconnected from all experiments. Sections 5–8 use Gradient Descent and Adam on the non-convex formulation (Equation 7). The convex solver is not implemented or compared anywhere. The authors appeal to the convexity result to justify using GD on the non-convex form, but the experiments do not validate this connection in any way. The convexity result would be substantially more impactful if the paper at least demonstrated it on a small dataset (e.g., MNIST) by solving the convex program.

- **Computational cost is not quantified despite claims of scalability.** The paper claims MGDL is "scalable" (abstract and conclusion) but provides no comparison of training time, FLOPs, or wall-clock costs between comparably-capacity SGDL and MGDL models. The only timing data comes from Section 8 (transformers only): MGT uses 28–33% of SGT's training time. For the core ML experiments (image reconstruction, CIFAR), there is no cost analysis at all. Since MGDL trains L sequential grades, its total training time scales linearly with L, which could be slower than a single deep network of equivalent depth depending on implementation. Without this analysis, the scalability claim is unsubstantiated.

- **The classification experiments use MSE loss, which is non-standard.** For CIFAR-100 (Section 5) and CIFAR-10 (Section 7), the paper explicitly states "We use mean squared error (MSE) as the loss function." Cross-entropy is the standard loss for classification, and MSE is known to produce different optimization dynamics and convergence behavior (e.g., gradient vanishing at saturated outputs, sensitivity to output saturation). This choice is not justified in the paper and may contribute to the poor SGDL convergence observed (loss stuck at ~10⁻² in Figure 3). Using a non-standard loss function makes it difficult to assess whether the observed SGDL failure mode would replicate with standard classification training.

### Minor

- **Convergence theorems rest on standard smooth optimization results.** Theorems 1 and 2 apply standard GD convergence analysis using the Hessian spectral norm as Lipschitz constant. The key difference from SGDL is that $\alpha_l \ll \alpha$ because gradients of shallow networks have smaller Hessian norms than deep ones. While correct, this is a restatement of the well-known principle that shallower networks are easier to optimize (e.g., vanishing gradient literature dating back to Bengio et al., 2003; Glorot & Bengio, 2010). This is a useful formalization but not a novel theoretical insight.

- **MGDL's relationship to residual networks and boosting is underexplored.** The paper acknowledges the connection briefly (citing ResNet in the introduction) but does not analyze MGDL's relationship to residual connections in standard architectures. MGDL's output is a sum of per-grade network outputs — this is mathematically equivalent to a residual structure. The paper would benefit from a clearer discussion of whether MGDL's benefits are specific to the multi-grade sequential training protocol or are shared by residual architectures trained end-to-end.

### Trivial

- The CIFAR-10 experiment (Section 7) uses only 10,000 sampled images; using the full dataset would strengthen the result.
- The learning rate range in Section 5 goes up to 10⁻⁴, while Section 6 uses wider ranges — these could be more consistent.

## Nice-to-Haves

- Compare SGDL against ResNet-based or LayerNorm-enhanced baselines on at least one standard benchmark to quantify whether MGDL's gains persist after controlling for architectural regularization.
- Include a small-scale experiment solving the convex program (Equation 8) to validate Theorem 3 empirically.
- Add wall-clock training time and FLOPs comparison between SGDL and MGDL models of comparable capacity, beyond just the transformer experiments.
- Use cross-entropy instead of MSE for the CIFAR classification experiments to align with standard practice.

## Removed Points

- **Harsh Critic: "Triviality of convergence results"** — The criticism itself has merit (convergence theorems are standard), but the characterization as "trivial" is overstated. They are correctly applied standard optimization analysis, which is useful formalization. Demoted to Minor.

- **Harsh Critic: "MGT is just an ensemble"** — This is speculative; the paper's MGT description (single-block Transformers trained sequentially on residuals) is distinct from standard ensembling. Removed as unsupported.

- **Harsh Critic: "Missing related works"** — Removed per hard rules (cannot verify existence without external sources).

- **Strength Finder: "Scalability and distribution-shift robustness"** — Kept as valid, specifically the transformer generalization on financial data (Section 8, Tables 4–5, Figure 8).

- **Strength Finder: "Provable widening of stable learning rate range"** — Kept as valid, but the magnitude of the widening (α_l ≪ α) is not quantified empirically.

- **Strength Finder: "Exact convexification"** — Kept as a theoretical strength, though weakened by the lack of empirical validation (addressed as Major weakness above).

## Novel Insights

The convergence of MGDL's gradient dynamics and the "Edge of Stability" phenomenon (Arora et al., 2022) provides an interpretable mechanistic explanation: the eigenvalue analysis shows that the same underlying mechanism — large negative eigenvalues of the iteration matrix — causes SGDL oscillations, and MGDL's shallower per-grade optimization keeps these eigenvalues bounded. This is a genuinely useful observation that connects two literatures (theoretical optimization and practical deep training dynamics) through a clean experimental protocol. However, the observation that gradient descent on shallow layers has better-conditioned Hessians than on deep layers is expected, and the novelty lies in the empirical tracking rather than a new theoretical insight.

## Suggestions

- Add a baseline comparison using a ResNet-style architecture (with residual/skip connections) to quantify whether MGDL's stability gains persist when SGDL is given comparable architectural inductive biases.
- Present FLOPs and wall-clock time in the main experiments, or add a supplementary table, to substantiate the scalability claim.
- Include a brief discussion in Section 3 of how MGDL relates mathematically to residual networks, and whether there are meaningful differences in expressivity vs. optimization dynamics between the two frameworks.

## Score and Decision

**Round 1 — Bracketing:**
- Weak anchor (score 3.0): *Three ways that non-differentiability affects neural network training* (Zap3nZhRIQ) — theory paper with limited experimental support. Our paper is clearly stronger, with more experiments and better organized results.
- Middle anchors (scores 5.75–7.0): *Reevaluating Theoretical Analysis Methods* (JslyktsKMY, 5.75) has similar theory+empirical structure but the paper under review has more comprehensive experiments; *Convex BCD for Neural Networks* (n2RIkaf1S4, 4.00) has more serious proof issues than our paper.
- Strong anchors (score 7.0+): *Sharper Guarantees for Learning Neural Network Classifiers* (h7GAgbLSmC, 7.0) has comparable theory+experiment structure but the bounds are genuinely improved over prior work; the paper under review's theorems are more restatements than improvements. *Convergence of GD on Continual Linear Classification* (DTqx3iqjkz, 6.25) is a similar tier paper with solid theory and limited experiments.

**Initial bracket: 4.5–6.5**

**Round 2 — Narrowing:**
- *Large Learning Rates without the Agonizing Pain* (LNYL96VIsD, 4.75): more empirical than theoretical, weak theory-practice link. Our paper's theory is stronger, experiments more structured. Our paper is clearly better.
- *Convergence of GD on Continual Linear Classification* (DTqx3iqjkz, 6.25): accepted paper with solid theory and very limited experiments. Our paper has broader empirical coverage (image, classification, transformers) but baseline fairness concerns similar in severity to the limited experiments concern in this anchor. Roughly comparable.
- *AID-based Bi-level Optimization* (9vZ8UjP2Mz, also ~5.0): similar theory+empirical structure with concerns about significance. Our paper has more breadth.

**Comparison**: The paper under review has more empirical breadth than the 6.25 anchor but has a significant baseline fairness concern that the 6.25 paper does not have (its theory is purely on linear models and accepted despite limited experiments). The convexity/practice disconnect is an additional structural weakness. These concerns put the paper below clear acceptance territory. It is clearly above the 4.75 anchor on both theoretical rigor and experimental structure. The paper is comparable to the mid-5s, with real contributions (spectral analysis, transformer results) balanced by genuine methodological gaps (straw-man baseline, orphaned convex theory, MSE for classification).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>