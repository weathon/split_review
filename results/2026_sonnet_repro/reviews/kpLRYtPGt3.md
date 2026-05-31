Now let me run the calibration search for scoring.Round 1 bracket: **6.5 – 8.5**. The paper is clearly above the middle anchors (5.6–6.0) and plausibly near the 8.0 strong anchors. Let me narrow.Now I have enough to write the full review. Let me synthesize.

---

## Summary

Neon (Negative Extrapolation from Self-Training) is a post-hoc parameter-merge technique that improves generative models by inverting the degradation direction incurred from briefly fine-tuning on self-generated data. The key theoretical contribution is a formal proof that common mode-seeking inference samplers (temperature/top-k, CFG, ODE solvers) induce a predictable anti-alignment between synthetic and real-data gradients—making the degraded checkpoint a corrective signal when negated. This is validated across four model families (diffusion, flow matching, autoregressive, few-step IMM) on ImageNet, CIFAR-10, and FFHQ, achieving a new state-of-the-art FID of 1.02 on ImageNet-256 with xAR-L at under 0.4% additional training compute.

---

## Strengths

- **Rigorous theoretical grounding.** Theorems 1 and 2 formally establish that mode-seeking samplers (temperature < 1, top-k, CFG, ODE solvers) cause cos φ < 0, which drives anti-alignment (s < 0), and that anti-alignment guarantees risk reduction under negative extrapolation (Eq. 4). The theory is honest about its local-approximation assumptions ("our theory guarantees anti-alignment only when the model error ‖ε‖_F is small"), a sign of intellectual rigor.

- **Compelling headline performance.** Neon applied to xAR-L achieves FID 1.02 on ImageNet-256 (from 1.28) using only 0.36% additional training compute and as few as 1k synthetic samples, surpassing the prior SOTA of UCGM (1.06). This is accompanied by qualitative evidence (Figure 1) and FID-vs-budget curves across multiple dataset sizes (Figure 5).

- **Mechanistic dissection via precision-recall.** Figure 4 shows precisely how Neon operates: precision monotonically decreases with extrapolation weight *w*, while recall peaks near the FID-optimal *w*. This quantitative decomposition—redistribution from over-represented to under-represented modes—confirms the theoretical prediction of anti-alignment correcting mode-seeking bias.

- **Cross-architecture transfer of the degradation signal.** Figure 8 shows that synthetic data from a flow-matching or IMM model can improve an EDM-VP model (FID 1.97 → 1.59 and 1.80), while CIFAR-10C (structured corruptions) yields no gain. This null control cleanly isolates the mode-seeking anti-alignment as the operative signal, not generic OOD perturbation.

- **Robustness to suboptimal base models and synthetic data quality.** Figure 9 shows Neon applied to a model trained on 30k samples nearly matches the baseline trained on 50k samples (FID ≈ 1.85), and Figure 10 shows near-optimal FID is maintained for CFG scales γ ∈ [1, 3] during synthetic data generation—practical robustness that broadens applicability.

- **Architecture universality at near-zero overhead.** The method delivers consistent improvements across diffusion (EDM-VP), flow matching, autoregressive (xAR, VAR), and few-step (IMM) models, each needing < 3% of original training budget and a single parameter merge with no inference modifications or auxiliary models.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation of CFG-only re-optimization for autoregressive headline results.** The paper's flagship numbers—xAR-L: 1.28 → 1.02 and VAR-d16: 3.30 → 2.01—are obtained by jointly optimizing both the merge weight *w* and CFG scale γ. The paper explicitly notes: *"Co-optimization is crucial to reaching the best FID: w increases recall at precision's expense, while γ does the opposite"* (Section 4.2). For VAR-d16, Figure 6 states that *"independent optimization (γ = 1.25) yields FID 3.01"*, but this appears to mean using the original γ rather than re-optimizing γ freely at w = 0. If the original xAR-L's FID of 1.28 was already γ-optimized by the original authors (which the paper implies by using their "FID-optimal inference settings"), then w = 0 with γ re-tuned returns approximately the same 1.28—but this is not explicitly confirmed. For VAR-d16, the original γ = 1.25 appears suboptimal, and whether γ-retuning alone (w = 0) could substantially close the gap from 3.30 is not directly addressed. The Figure 6 landscape heatmap is the best available evidence (showing a diagonal valley requiring both w > 0 and high γ for FID 2.01), but the minimum over γ at w = 0 is not explicitly reported. Adding a single row per AR model—FID achieved with w = 0 and γ grid-searched—would close this gap definitively.

### Minor

- **Comparison with DDO and SIMS confined to Appendix Table A.1.** DDO (Zheng et al., 2025) and SIMS (Alemohammad et al., 2024b) are the closest prior methods addressing the same problem setting. The paper discusses them qualitatively (Section 2) but relegates numerical comparison to Table A.1 in the appendix. For a paper making SOTA claims, at least a summary row of comparisons in the main body would strengthen the case and directly demonstrate the compute/architecture advantages.

### Trivial

- **Figure 4 caption typo.** The caption reads: *"w = −1 corresponds to the model directly trained on synthetic data, i.e., θ_Neon = θ_r"* and *"w = 0 corresponds to the base model, i.e., θ_Neon = θ_r."* By Eq. (2), θ_Neon = (1+w)θ_r − wθ_s, so w = −1 gives θ_Neon = θ_s (the synthetic fine-tuned model), not θ_r. The figure itself appears correctly interpreted in the main text; this is a caption error only.

---

## Nice-to-Haves

- **Quantitative validation of the theoretical w* prediction.** Section 4.1 notes that as fine-tuning progresses, the optimal w* decreases, which is qualitatively consistent with the prediction w* ≈ −s/(αz). A direct comparison of predicted vs. observed w* trajectories across models (even approximate) would sharpen the theory-to-experiment connection.

- **Connection to task arithmetic / model-merging literature.** The merge formula θ_Neon = θ_r − w(θ_s − θ_r) is structurally identical to the *negation* operation from task arithmetic (negating a task vector). The paper's contribution is the insight that the self-training task vector is anti-aligned—making negation beneficial—rather than the linear merge itself, but briefly situating Neon in the model-merging / task-arithmetic context would preempt reviewer confusion about what is claimed as novel.

- **Iterative Neon.** The paper uses a single round of synthetic generation and negation. Whether iterating (generate from θ_Neon, degrade again, negate again) provides further gains or quickly saturates is an interesting open question worth at least a brief discussion.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "task arithmetic literature overstates mechanical novelty"** — Removed as a formal weakness. The paper never claims the linear merge formula is novel; it claims the anti-alignment discovery and its theoretical proof are the contributions. The connection is worth mentioning (moved to Nice-to-Haves) but the paper is not overstating anything.

- **Harsh critic: "theory is local and may not cover weak base models"** — Removed. The paper explicitly acknowledges the local guarantee ("our theory guarantees anti-alignment only when the model error ‖ε‖_F is small") and Section 4.4 / Figure 9 empirically show the method works well even for weaker models. The authors address this honestly.

- **Harsh critic: "curvature-density coupling assumption (A-MONO) for diffusion ODE solvers is non-trivial and unverified"** — Demoted. The assumption is stated in Footnote 2, acknowledged as non-trivial, and the diffusion/flow results empirically confirm the method works regardless. This is honest theory rather than a failure.

---

## Novel Insights

The most conceptually striking finding in this paper is the reframing of model collapse from self-training not as a failure mode but as a structured, invertible signal. The proof that mode-seeking samplers universally produce anti-aligned gradients explains *why* self-training degrades performance (the model over-represents already well-captured modes) and simultaneously prescribes the remedy (reverse the gradient, redistribute mass). This reframing—degradation as a diagnostic signal for distributional bias—may have implications beyond image generation, wherever mode-seeking inference is used and self-generated data could be leveraged. The cross-architecture transferability of the anti-alignment signal (Figure 8) further suggests that the mechanism is a universal property of the learning-theoretic setting rather than architecture-specific behavior.

---

## Suggestions

1. **Add a single ablation row for w = 0, γ optimized for each AR model.** For xAR-L: confirm that the original 1.28 was already γ-optimal (making re-tuning a no-op). For VAR-d16: read off the minimum FID at w = 0 from Figure 6's heatmap and report it as a baseline. This directly answers the co-optimization concern and either solidifies or contextualizes the headline numbers.

2. **Move at least one representative row from Table A.1 to the main body.** A brief comparison showing Neon vs. DDO and SIMS on a common benchmark (FID, compute overhead, architecture scope) belongs in the main paper for a submission making SOTA claims.

3. **Briefly note the connection to task arithmetic / model negation.** A one-sentence acknowledgment that Eq. (1) resembles task vector negation, followed by the key distinction (the anti-alignment proof justifies *why* negation helps in this setting), would preempt this as a reviewer concern.

---

## Score and Decision

**Calibration anchors:**
- *Round 1:*
  - `/deepreview_13k_calibration/QKqWnNkwPL.md` (avg 3.0, self-distillation for diffusion) — much weaker than Neon; no SOTA results, narrower contribution
  - `/deepreview_13k_calibration/Xr5iINA3zU.md` (avg 5.75, model collapse analysis) — analyses self-consuming models but proposes no method; weaker
  - `/deepreview_13k_calibration/OlzB6LnXcS.md` (avg 8.0, shortcut models) — clean strong paper, strong empirical results, comparable novelty
  - `/deepreview_13k_calibration/zMoNrajk2X.md` (avg 8.0, CADS) — architecture-agnostic inference improvement; good comparison point
  - **Round 1 bracket: 6.5 – 8.5**

- *Round 2:*
  - `/deepreview_13k_calibration/JORAfH2xFd.md` (avg 6.75, stability of iterative retraining) — related topic (self-consuming generative models), theory + empirical; purely analytical, no method, smaller scope than Neon. Neon is clearly better.
  - `/deepreview_13k_calibration/ShjMHfmPs0.md` (avg 6.67, Self-Consuming Generative Models Go MAD) — empirical and theoretical analysis of autophagous loops; related inspiration paper, no novel method, weaker than Neon.
  - `/deepreview_13k_calibration/WNkW0cOwiz.md` (avg 7.50, Lipschitz singularities) — theory + method improving diffusion FID; comparable structure (theoretical diagnosis + practical fix + SOTA on a benchmark). Neon has broader coverage (4 model families vs. 1) and larger empirical scope.
  - `/deepreview_13k_calibration/kGvXIlIVLM.md` (avg 7.00, CCA guidance-free AR generation) — directly relevant: improves AR generation quality via fine-tuning, architecture-specific. Neon is broader and more theoretically grounded.
  - `/deepreview_13k_calibration/FE2e8664Sl.md` (avg 7.00, few-shot HDA) — generator adaptation paper, narrower scope, different problem.

**Comparison summary:** Neon is clearly stronger than the 6.67–6.75 anchors (those are analysis-only with no novel method or broader scope). Neon is comparable to or slightly above the 7.0–7.5 anchors: it is broader than Lipschitz singularities (4 model families), more practical than CCA (no architecture restriction), and achieves a cleaner state-of-the-art claim with strong ablations. The missing CFG-only ablation for AR results is the main drag preventing a confident 8.0. The non-AR results (diffusion, flow matching) are clean and unambiguous, providing solid evidence that the method works independent of the co-optimization concern.

**Final score: 7.5 — Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>