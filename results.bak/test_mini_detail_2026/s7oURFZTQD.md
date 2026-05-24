Now I have a thorough calibration. Let me produce the final consolidated review.

## Summary

This paper proposes multi-grade deep learning (MGDL), an iterative residual-correction framework that trains a sequence of shallow networks rather than a single deep network end-to-end (SGDL). It provides convergence theorems for GD on each grade, a convexity result for single-layer ReLU grades, an eigenvalue analysis of the linearized GD dynamics, and experiments on image reconstruction (regression/denoising/deblurring), CIFAR-100 classification, and time-series forecasting with transformers. The paper claims MGDL unifies rigorous theoretical guarantees with broad empirical improvements.

## Strengths

- **Consistent empirical advantage across diverse tasks.** MGDL outperforms SGDL on 6 image regression tasks (0.42–3.94 dB PSNR gains), 3 denoising tasks across 6 noise levels (0.16–4.23 dB), 3 deblurring levels (0.85–2.84 dB), and CIFAR-100 (loss ~10⁻⁴ vs ~10⁻²). The breadth — FC networks, CNNs, and transformers — supports the claim that MGDL is a broadly applicable framework.

- **Quantitative learning-rate robustness demonstration (Section 6, Figure 2).** On synthetic data, SGDL works only for η ∈ [0.03, 0.08] while MGDL works for η ∈ [0.01, 0.3], and the gap widens on higher-frequency targets. This is a clean, controlled experiment that directly supports one of MGDL's claimed advantages.

- **Eigenvalue monitoring as an empirical diagnostic (Section 7).** Tracking eigenvalues of I − ηH(W^k) during training reveals that MGDL's eigenvalues stay in (−1,1) while SGDL's fall below −1, correlating with oscillatory loss. This is a suggestive mechanistic observation and a useful diagnostic tool, even if it falls short of a predictive theory.

- **Multi-grade transformer (MGT) extension.** Showing that the MGDL principle extends to transformers (synthetic time series: TeMSE 0.16 vs 2.6; SPX: 0.018 vs 0.089) demonstrates generality, though the baseline comparison needs strengthening.

## Weaknesses

### Fatal
None — no single error invalidates the paper's core claims.

### Major

- **Theory-practice disconnect: convergence theorems require smooth activations; experiments use ReLU.** Theorems 1 and 2 (and Theorem 4) explicitly assume σ is twice continuously differentiable. All experiments (image regression, denoising, deblurring, CIFAR, transformers) use ReLU, which is not differentiable at zero. The paper never reconciles this gap. While this pattern is common in deep learning theory, the paper's central narrative is that the theory *explains* the empirical advantages. As presented, the convergence theorems formally apply to a different class of networks than those evaluated. The paper should either (a) adapt the analysis to ReLU (e.g., via subgradient techniques or piecewise analysis), (b) validate with smooth activations (tanh, SiLU), or (c) at minimum discuss why the theory is expected to carry over.

- **Unsubstantiated claim that α_l ≪ α (the central theoretical justification for MGDL's advantage).** Line 170 states the key claim: "with α_l ≪ α, thereby improving stability and robustness." This is the crux of the theoretical argument for why MGDL admits a wider learning-rate range and converges more stably. Yet no bound, proof, or even empirical measurement of α_l vs α is provided. Without support, this claim is an assertion, not a result.

- **CIFAR-100 reports only training loss, not accuracy.** The paper claims MGDL delivers "superior accuracy" (line 283) but only shows training loss curves (Figure 3). For a classification benchmark, test accuracy is the standard metric. Training loss is a poor proxy for generalization. Classification accuracy is expected as a matter of reporting convention and is necessary to substantiate the claim.

- **No statistical significance or error bars.** All results are reported as single runs. Given the stochastic nature of training (Adam is used in several experiments), it is impossible to assess whether observed improvements are robust. This is particularly important for the transformer results where the gaps are very large (16× on synthetic time series), raising the possibility of an undertuned baseline rather than a genuine architectural advantage.

- **Transformer comparison may reflect undertuned baselines.** MGT uses single-block transformers per grade while SGT uses multiple blocks. The paper reports no hyperparameter search, learning rate tuning, or regularization study for SGT. SGT's predictions in Figure 8 appear to diverge, which is characteristic of an improperly configured deep model (e.g., excessive learning rate, insufficient regularization). Without evidence that SGT was reasonably tuned, the claimed 5–16× improvements are uninterpretable.

### Minor

- **Convexity result (Theorem 3) is an incremental application of existing work.** The theorem follows Pilanci & Ergen (2020) and shows that a shallow ReLU grade can be convexified by the same technique. The claimed extension "from shallow to deep architectures" relies on MGDL's decomposition into shallow pieces — a straightforward application. The exponential cost of the convex program (P_l variables, where P_l grows with input dimension) is not discussed, and the convex program is never solved in experiments. The result is theoretically valid but adds limited practical insight.

- **Eigenvalue analysis is diagnostic, not predictive.** Section 7 monitors eigenvalues during training and observes correlation with loss oscillations, but it does not *predict* MGDL's advantage (no bound on α_l is given, no theorem proves that shallower grades necessarily have smaller spectral radii). The linearization drops second-order terms, and the connection to the actual GD dynamics is heuristic. The analysis is presented as a key theoretical contribution but is better described as an empirical diagnostic.

- **Optimizer mismatch between theory and main experiments.** The convergence theorems and eigenvalue analysis analyze GD. The main CIFAR-100 and image reconstruction experiments use Adam. How Adam changes the eigenvalue picture or convergence guarantees is not discussed.

### Trivial

- Architecture descriptions in the paper use compact notation (e.g., (2,1,128,8)) that is not immediately interpretable without cross-referencing the appendix — a brief in-text explanation would help.

## Nice-to-Haves

- The paper could strengthen the α_l ≪ α claim by providing empirical measurements of Hessian spectral norms for shallow vs. deep networks of comparable total capacity.
- Adding smooth-activation experiments (tanh, SiLU) would close the theory-practice gap and validate that the theoretical predictions hold when assumptions are satisfied.
- For the transformer section, a proper hyperparameter search over SGT depth, learning rate, weight decay, and dropout would make the comparison fair.

## Removed Points

- *"Code is not visible to the reviewer"* — Removed per rule: criticisms questioning availability of cited artifacts are not author errors. The reproducibility statement points to supplementary material stripped by the parser.
- *"The paper does not acknowledge that the convex program has exponential cost"* — Actually, the paper states "only finitely many such matrices exist" and the proof's P_l notation implicitly acknowledges the combinatorial structure, so this is partially addressed. Moved here.
- *"SGDL baselines appear deliberately weak"* — The asymmetry in the transformer comparison (SGT uses deeper networks) favors SGT, not the proposed method. Removed per asymmetry rule.
- *"A properly regularized SGT would likely perform much better"* — Speculative; removed per rule against speculation-dependent fatal flaws. The concern about undertuning is retained in the Major section but the speculation about what a tuned SGT would achieve is removed.
- *Several generic strengths from the Strength Finder* (e.g., "this paper addressed an important problem," "comprehensive evaluation") — Removed per rule: generic/superficial strengths not grounded in specific evidence.

## Novel Insights

The harsh critic correctly identifies that the eigenvalue diagnostic — while not a full theory — is the paper's most interesting contribution. The observation that shallow subproblems keep iteration-matrix eigenvalues in (−1,1) while deeper networks push them below −1 is a plausible mechanism for MGDL's stability. However, this remains at the level of correlation, not causation. A genuinely novel contribution would require either proving a bound on spectral radii as a function of depth or providing causal experiments (e.g., explicitly controlling eigenvalue ranges during training). Neither is present, so the insight is suggestive but incomplete.

The critic also correctly notes a core tension in the paper: its stated goal is to *explain* why MGDL works, but the explanation components (smooth convergence theory, ReLU convexity, eigenvalue analysis) are each disconnected from the actual experimental setup. This observation — that the paper attempts to unify theory and practice but fails to align them — is a valuable meta-level insight that the paper itself does not articulate.

## Suggestions

1. **Report CIFAR-100 test accuracy.** This is a basic requirement for a classification benchmark and necessary to substantiate the claim of superior accuracy.
2. **Add error bars or multiple-seed runs** to all experiments, especially the transformer results where the gaps are large and suspicious.
3. **Either prove the convergence theorems for ReLU (subgradient analysis) or run experiments with smooth activations** to close the theory-practice gap.
4. **Measure α_l and α empirically** across tasks to support the claim that α_l ≪ α, or provide a theoretical bound.
5. **Tune the SGT (deep transformer) baseline** with a hyperparameter search over depth, learning rate, weight decay, and dropout before claiming 5–16× improvement.

## Score and Decision

**Calibration process:**

**Round 1 — Bracketing.** Three queries anchored the weak- (<3.5), middle- (3.5–7.5), and strong- (>7.5) score bands on topics similar to the paper. Weak anchors (2.50–3.33) were clearly below this paper — their contributions were either trivial or their experiments minimal. Strong anchors (8.0–8.5) were papers with rigorous, novel theory or major practical advances, clearly above this paper. Initial bracket: **4–6**.

**Round 2 — Narrowing.** Pulled anchors inside (3.5–5.5), (4.5–6.5), and (4.0–6.0):

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Layer-wise UAT for ResNets (68DwQWtdwr) | 4.00 | R2 | Very similar structurally: proposes progressive training, claims theoretical backing that doesn't fully hold, experiments on small-to-medium tasks. MGDL has broader experiments but similar theory-practice gap. Comparable quality. |
| FRE-RNN (e5l1sD0nk2) | 4.50 | R2 | Practical improvements to Equilibrium Propagation with controlled experiments. Narrower scope but stronger evidence. MGDL is weaker due to missing accuracy, no error bars, and undertuned baselines. |
| Convergence near-linear width (wGc6aWvRLa) | 4.50 | R2 | Focused, rigorous theory paper even if assumptions are restrictive. MGDL's theory is less rigorous. Comparable overall — different strengths/weaknesses. |
| Expectation Curvature (K79J5GRlQb) | 5.33 | R2 | Novel theoretical framework with mixed reviews. MGDL has less novel theory. Below this anchor. |
| Saddle-to-Saddle (B4zcoLvjw0) | 6.00 | R2 | Solid theory with clear novel results. MGDL is much weaker theoretically. |

The paper is most comparable to the Layer-wise UAT paper (4.00) and the FRE-RNN paper (4.50), sitting between them — slightly above the former due to broader experiments, slightly below the latter due to reporting gaps and undertuned baselines.

**Final score: 4.0 — Reject.** The MGDL idea has genuine merit, and the empirical results are directionally positive. However, (a) the theoretical framework does not apply to the models evaluated, (b) the α_l ≪ α claim central to the theoretical argument is unsubstantiated, (c) CIFAR-100 does not report accuracy despite claiming superior accuracy, and (d) the transformer comparisons likely reflect undertuned baselines. These issues collectively prevent acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>