## Summary
This paper proposes TAK (Task Arithmetic with KFAC regularization), a dataless regularizer for improving weight disentanglement in Task Arithmetic. The key insight is that under model linearization, the representation drift regularizer reduces to a quadratic form involving the Jacobian Gram matrix, which is an instance of the generalized Gauss-Newton (GGN) matrix. This enables the use of KFAC approximation to compute the regularizer without access to other tasks' data. The paper also proposes a constant-complexity Kronecker accumulation heuristic for multi-task settings. Experiments on CLIP ViT (B/32, B/16, L/14) and T5-base across vision and language benchmarks demonstrate state-of-the-art task addition and negation performance while being fully dataless.

## Strengths
- **Novel conceptual bridge between representation drift regularization and curvature matrices (§3.1, Eq. 3):** The paper cleanly shows that under linearization, the representation drift regularizer is a quadratic form of the Jacobian Gramian, which corresponds to the GGN with squared-error criterion (§3.2). This is a non-obvious connection that enables importing well-established curvature approximation tools.

- **Strong empirical results while being fully dataless (Tables 1 & 2):** TAK matches or exceeds τJp (which requires external task data) in the linearized regime across all three CLIP ViT variants (e.g., 86.0% vs 85.6% on ViT-B/32, 91.6% vs 91.1% on ViT-L/14). On task negation (Tab. 2), TAK outperforms τJp across all model scales (e.g., 3.4% vs 6.7% target accuracy on ViT-B/32), despite requiring no external data.

- **Constant-complexity Kronecker accumulation is near-lossless (Eq. 8, Tab. 3):** The merging heuristic reduces per-task storage from O(T) to O(1). Tab. 3 shows this is empirically sound: accumulated TAK matches or exceeds naïve multi-task formulation for ViT-B/16 and T5-base, with only a small gap for ViT-B/32.

- **Robustness to task-vector rescaling eliminates held-out tuning (Fig. 4a):** The α-sweep shows KFAC-regularized linearized FT maintains high accuracy across α ∈ [0, 2], unlike unregularized merging methods (TA, TSV, ISO, TIES) which exhibit sharp peaks and declines. This directly supports the claim that post-hoc tuning can be omitted.

- **Task localization evidence (Fig. 5):** Histograms of ‖J_θ f(x, θ₀) τ_t‖²₂ show that with KFAC regularization, out-of-distribution normalcy scores are pushed toward zero while in-distribution scores remain informative — direct evidence of weight disentanglement.

- **Comprehensive evaluation across modalities and regimes:** Results span vision (3 CLIP ViTs) and language (T5-base), both linearized and non-linear fine-tuning, task addition and negation, robustness analysis, computational cost analysis, KFAC estimation and compression studies.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Non-linear regime extension rests on an empirical bridge (§4, line 227):** The theoretical derivation assumes model linearization (§3.1–3.3), but TAK is applied in the non-linear regime by pairing with Attention-Only Fine-Tuning, justified by the claim that this "implicitly induces kernel-like behavior." The paper honestly acknowledges that "our regularization is not theoretically exact in the non-linear regime," but provides no diagnostic (e.g., relative approximation error of the linearized model) to validate this bridge. The strong empirical results are compelling, but a quantitative bound on when the linear approximation breaks down would strengthen the argument — especially since the non-linear results actually drive the headline comparison with TaLoS.

- **β hyperparameter treatment not visible in main text (Eq. 7, line 145):** The multi-task objective includes β controlling overall regularization strength. The paper specifies how λ_t is set (proportional to dataset size) but does not state in the main text how β is chosen. This matters for the "dataless" framing — if β requires cross-task validation, the claim needs qualification. (The appendix likely addresses this, but given its centrality to the paper's framing, main-text visibility would be beneficial.)

- **TaLoS comparison uses numbers from the original paper (Tab. 1, footnote †):** The non-linear regime comparison with TaLoS uses numbers "taken from the original paper" (line 159), which may involve different training configurations. While common and likely unavoidable, this caveat deserves more prominence since TaLoS is a key competitor in the non-linear setting.

### Trivial
None.

## Nice-to-Haves
- A quantitative diagnostic for the linear approximation quality in the non-linear regime (e.g., measuring ‖f(x, θ₀+τ) − f_lin(x, θ₀+τ)‖ / ‖f(x, θ₀+τ)‖) would bound the empirical bridge.
- Discussing the KFAC quadratic storage scaling more explicitly as a constraint on very large models, since experiments use relatively small models (ViT-B/16 ~86M, T5-base ~220M).
- Reporting the actual difference between ∑ λ_t B_t ⊗ A_t and the merged approximation in Tab. 3 would deepen the analysis of the Kronecker heuristic.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Strength about "extending to non-linear regime via attention-only FT": This is kept as a strength but qualified — the theoretical gap in the non-linear regime is acknowledged as a minor weakness. The paper is honest about this limitation.
- The harsh critic's point about β not being discussed in the main text was partially retained as a minor weakness. The appendix likely covers this, and the paper's claim is "dataless w.r.t. other tasks' data," not "hyperparameter-free."

## Novel Insights
The paper's central novel insight is that representation drift regularization in Task Arithmetic, under model linearization, reduces to a Jacobian Gram matrix quadratic form — which is an instance of the GGN matrix. This reframing is non-obvious and powerful: it transforms a data-dependent regularization problem into a well-studied curvature approximation problem, enabling the use of KFAC and eliminating the need for external task data. The constant-complexity Kronecker accumulation heuristic (Eq. 8) is a useful engineering contribution that reduces the multi-task storage burden, though the merging approximation is honestly labeled as a heuristic.

## Suggestions
- Add a short paragraph or sentence in §3.4 or §4 stating how β is set (fixed, tuned on current task data, etc.) to preempt concerns about the dataless claim.
- Provide a quantitative diagnostic for the linear approximation quality in the non-linear regime.
- Add a sentence in §4 acknowledging that the TaLoS comparison uses numbers from the original paper with potentially different training configurations.

## Calibration Report

**Round 1 anchors (bracketing):**
- `lNtio1tdbL.md` (ATM: Alternating Tuning and Merging) — avg 3.00, Round 1. Weak paper proposing iterative tuning-merging without strong theoretical or empirical contribution.
- `XVHXVdoV11.md` (Collective Model Intelligence) — avg 3.40, Round 1. Weak paper on compatible specialization, limited experiments.
- `1VwWi6zbxs.md` (τJp: Key Indicator for Weight Disentanglement) — avg 6.00, Round 1. Direct baseline — TAK matches/exceeds τJp results while being dataless.
- `dj0TktJcVI.md` (Attention-Only FT for Weight Disentanglement) — avg 6.25, Round 1. Baseline method that TAK builds upon and improves with curvature regularization.
- `irPcM6X5FV.md` (Submodule Linearity for Task Arithmetic) — avg 6.00, Round 1. Similar contribution space; TAK has cleaner theory and stronger results.
- `Bq3fEAGXUL.md` (Realistic Evaluation of Model Merging) — avg 5.33, Round 1. Evaluation/benchmarking paper with limited novelty.
- `vRvVVb0NAz.md` (When is Task Vector Provably Effective) — avg 7.50, Round 1. Stronger theoretical contribution (first generalization analysis), but less practical.
- `dqMqAaw7Sq.md` (Mitigating Backdoor Effect for Model Merging) — avg 7.00, Round 1. Similar contribution level; TAK has cleaner theory.
- `iynRvVVAmH.md` (Parameter-Efficient Multi-Task Model Fusion) — avg 7.00, Round 1. Similar contribution level; TAK has broader evaluation.
- `g8sGBSQjYk.md` (Second-Order Optimization Parameterization) — avg 7.33, Round 1. More focused on optimization theory.
- `puTxuiK2qO.md` (AdaFisher) — avg 6.25, Round 1. Second-order optimizer paper.
- `8j9hz8DVi8.md` (CASPR) — avg 7.33, Round 1. Optimization preconditioner paper.
- `NvbeD9Ttkx.md` (FOSI) — avg 6.25, Round 1. Hybrid first/second-order optimizer.
- `q3ztjJRQuJ.md` (Task Arithmetic in Trust Region) — avg 5.75, Round 1. Model merging paper with limited novelty.

**Round 1 bracket:** Between 6.5 and 7.5. TAK is clearly stronger than the 6.0–6.5 anchors (τJp, Attention-Only FT, Submodule Linearity) because it subsumes their contributions while adding a novel theoretical framework and being dataless.

**Round 2 anchors (narrowing):**
- `dqMqAaw7Sq.md` (DAM) — avg 7.00, Round 2. TAK has a cleaner theoretical contribution and more comprehensive evaluation.
- `iynRvVVAmH.md` (L-LoRA) — avg 7.00, Round 2. TAK has a stronger theoretical contribution and broader evaluation.
- `vRvVVb0NAz.md` (Task Vector Provably Effective) — avg 7.50, Round 2. This paper provides first theoretical characterization of task vectors on nonlinear Transformers — a more fundamental contribution. TAK is more practically oriented with stronger empirical evaluation.

**Round 2 narrowing:** The paper sits between 7.0 and 7.5. Compared to the 7.0 anchors (DAM, L-LoRA), TAK has a cleaner theoretical contribution and more comprehensive evaluation. Compared to the 7.50 anchor (Task Vector Provably Effective), TAK has a more practical contribution but less fundamental theoretical advance. I position TAK at 7.0, at the upper end of the 7.0 anchors, slightly below the 7.50 theoretical paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>