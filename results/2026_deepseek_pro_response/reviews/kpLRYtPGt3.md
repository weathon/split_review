Now let me write the final consolidated review with the calibration results.

## Summary
Neon is a post-hoc parameter merge that improves generative models by reversing weight updates from brief fine-tuning on the model's own synthetic outputs. Given a base model θ_r, Neon fine-tunes it on self-generated data to obtain a degraded checkpoint θ_s, then extrapolates away via θ_Neon = (1+w)θ_r − wθ_s. The paper proves that mode-seeking inference samplers (low-temperature, top-k/top-p, CFG) create predictable anti-alignment between synthetic and real-data population gradients, making negative extrapolation reduce true-data risk. The method is demonstrated across four model families (diffusion, flow matching, autoregressive, few-step) on CIFAR-10, FFHQ, and ImageNet, achieving SOTA FID 1.02 on ImageNet-256 with xAR-L using only 0.36% additional fine-tuning compute.

## Strengths
- **Theoretical foundation for the anti-alignment mechanism (Theorems 1–2, Section 3.1):** The paper proves that mode-seeking inference samplers create anti-alignment (s < 0) between synthetic and real-data population gradients. Theorem 1 derives a sufficient condition for anti-alignment in terms of sampler bias and Hessian geometry; Theorem 2 proves that mode-seeking samplers guarantee cos φ < 0 to first order. This provides a principled explanation rather than a heuristic — a distinguishing feature relative to prior work on self-training collapse.
- **Consistent empirical gains across four model families (Figures 3–7):** Neon delivers FID improvements across diffusion (EDM-VP CIFAR-10: 1.78→1.38; FFHQ-64: 2.39→1.12), flow matching (CIFAR-10: 3.5→2.32), autoregressive (xAR-L: 1.28→1.02, a new SOTA; VAR-d16: 3.30→2.01), and few-step generators (IMM T=4: 1.98→1.69), all with <1% additional fine-tuning compute.
- **Precision-recall decomposition reveals the mechanistic basis (Figure 4):** For EDM-VP on CIFAR-10, the paper traces FID's unimodal dependence on w into constituent precision and recall curves: precision monotonically decreases with w while recall follows an inverted-U peaking at the optimal weight. This directly corroborates the theoretical claim that Neon redistributes mass from over- to under-represented modes.
- **Cross-architecture transferability with a clean negative control (Figure 8, Section 4.4):** Synthetic data from a flow matching model improves EDM-VP from FID 1.97 to 1.59; IMM data reaches 1.80. The CIFAR-10C null result (no FID improvement with corrupted real images) confirms the effect is specific to sampler-induced anti-alignment, not any OOD dataset.
- **Extreme data efficiency (Figure 5):** xAR-L achieves FID 1.05 with only 1k synthetic samples — near-optimal relative to the 750k-sample result of 1.02 — confirming the degradation direction stabilizes rapidly.
- **Robustness to base model quality and synthetic data quality (Figures 9–10):** Neon compensates for a 40% real-data reduction (Figure 9), and final FID remains within 3% of optimal across a wide range of synthetic-data CFG scales (Figure 10). Both extend practical scope and address the theory's near-optimality requirement.

## Weaknesses

### Fatal
None.

### Major
- **No experimental comparison against other synthetic-data improvement methods:** The paper's related work (Section 2) positions Neon against DDO, SIMS, Discriminator Guidance, and Self-Play Fine-Tuning, arguing Neon is simpler, architecture-agnostic, and cheaper. However, no experimental comparison against any of these methods is provided. The paper demonstrates that Neon improves over base models, but readers cannot assess the performance-simplicity tradeoff. The paper's claim is about architectural advantages (no auxiliary models, no inference modifications, no likelihood computations) rather than superior FID, so this gap does not undermine the core contribution. Nonetheless, a single head-to-head comparison (e.g., against DDO on CIFAR-10 diffusion) would substantially strengthen evidential standing.

### Minor
- **Hyperparameter tuning performed on the evaluation distribution:** The paper uses a 10k/50k split from the same underlying dataset (e.g., ImageNet validation set) for hyperparameter search and final evaluation. While this split approach is better than tuning on the full evaluation set, both come from the same distribution, creating a risk that reported gains partially reflect overfitting to FID. The U-shaped curves in Figure 4 suggest the optimum is not pathologically sharp, mitigating this concern somewhat, but the risk should be acknowledged.
- **Compute accounting omits synthetic data generation cost:** The reported compute percentages (0.36% for xAR-L, <0.005% for IMM) count only the fine-tuning budget. Generating S (e.g., 750k ImageNet-256 samples from xAR-L) is not free, especially for autoregressive models. The omission does not change the "Neon is cheap" story but makes the efficiency narrative less complete.
- **No limitations section:** The paper lacks an explicit discussion of limitations. Worth acknowledging: the need for joint hyperparameter tuning (w and γ), the requirement to generate and store a synthetic dataset, and the theory's scope being restricted to near-optimal models (though Figure 9 shows empirical robustness beyond this regime).
- **Gap between theory scope and algorithm practice:** The theory analyzes a single gradient step from θ_r; the actual method runs many fine-tuning steps. The paper partially addresses this via the Taylor expansion (Eq. 4) and finite-|S| analysis (line 173), but does not formalize how multi-step fine-tuning interacts with the anti-alignment condition as the model moves away from θ_r. Strong empirical results across all settings suggest this gap is not practically significant.
- **No error bars or variance reporting:** All FID numbers are single-point estimates. Given FID's sampling variance and the stochastic generation of S, reporting standard deviation across at least 3 runs would improve credibility.
- **Precision-recall analysis in the main paper limited to one model:** The mechanistic story (Figure 4) is central to the paper's contribution but shown for only EDM-VP / CIFAR-10 in the main text. The paper references Appendix D for other models.

### Trivial
- **Only FID reported; no Inception Score or alternative metrics:** IS would be a useful complement given the claim of improved "sharpness and realism" (Figure 1) and is essentially free to compute alongside FID.

## Nice-to-Haves
- A head-to-head comparison against at least one synthetic-data improvement baseline (e.g., DDO) would strengthen evidentiary standing.
- Report generation cost alongside fine-tuning cost for complete compute accounting.
- Identify and characterize a failure case (e.g., a sampler configuration where anti-alignment breaks down) to delineate the method's boundaries.
- The "1k samples gets near-optimal performance" result deserves more analysis — e.g., a control experiment with random-direction perturbations to distinguish degradation-signal effects from parameter-merge regularization.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"No experimental comparison against methods that also leverage synthetic data" — kept as Major but reframed.** The original harsh-critic framing suggested the paper claims superior *performance* over DDO/SIMS/DG. The paper's actual claim is about simplicity and architectural generality ("requires no auxiliary models, no inference modifications, no likelihood computations"). The weakness is valid as an evidential gap in situating the performance-simplicity tradeoff.
- **Speculation that "1k samples result is suspiciously close to 750k result" and "parameter merge itself acting as a regularizer"** — removed. This is speculation not grounded in specific paper evidence; the paper provides a theoretical mechanism for why the degradation direction stabilizes quickly.
- **"Missing appendix, missing proofs in appendix"** — removed per hard rules. The parser strips appendix sections; they exist in the original submission.
- **Formatting/style nitpicks** — removed per hard rules.
- **All Strength Finder points kept** — all were concrete and verifiable against the paper. None were generic "important problem" claims.

## Novel Insights
The most genuinely novel insight from the reviews is that the paper's strength lies in the combination of (a) a clean theoretical explanation for *why* self-training degrades models in a predictable way and (b) the precision-recall mechanism showing exactly how probability mass redistributes. This reframes model collapse from a pathology to avoid into a structured signal to exploit — a perspective shift with implications beyond the method itself. The cross-architecture transferability result (Figure 8) further suggests the degradation signal is a fundamental property of mode-seeking sampling rather than an artifact of any specific architecture.

## Suggestions
- Add at least one experimental comparison against a synthetic-data improvement baseline (DDO on CIFAR-10 diffusion would be the most natural) to help readers assess the performance-simplicity tradeoff.
- Discuss the hyperparameter tuning protocol more transparently, acknowledging the risk of overfitting to FID and justifying why the effect is likely small (the U-shaped curves provide some reassurance).
- Report the generation cost of S alongside the fine-tuning cost, even if only as an estimate.
- Add a limitations subsection.
- Run 3 seeds for key results and report mean ± std for FID.
- Include IS as a complementary metric.

## Calibration

### Round 1 — Bracketing
- **Weak band (≤3.5):** `8TbqoP3Rjg` (2.00, Reject) — KD for model collapse; much weaker in novelty, theory, experiments. `QKqWnNkwPL` (3.00, Reject) — self-distillation; much weaker. `vK8C37eHXM` (3.20, Reject) — autoencoder+diffusion; much weaker.
- **Middle band (3.5–7.5):** `svIdLLZpsA` (6.00, Accept) — synthetic data for classification; Neon is clearly stronger (generative, more extensive experiments, SOTA). `S5EqslEHnz` (5.60, Accept) — generated data for contrastive learning; Neon stronger. `CjPt1AC6w0` (6.25, Reject) — synthetic data for transfer learning; different domain. `9aIlDR7hjq` (4.00, Reject) — augmented conditioning; much weaker.
- **Strong band (≥7.5):** `OlzB6LnXcS` (8.00, Accept) — Shortcut Models; comparable quality tier. `6O3Q6AFUTu` (8.00, Accept) — NoiseDiffusion; different topic. `3b9SKkRAKw` (8.00, Accept) — LeFusion; different topic. `I5lcjmFmlc` (8.00, Reject) — diffusion classifier; different topic.

**Round 1 bracket: 6.5–8.5.** Neon is clearly above the ~6.7 self-training analysis papers (MAD, iterative retraining stability, recursive stability) and comparable to the ~8.0 strong-accept papers.

### Round 2 — Narrowing within the bracket
- `JORAfH2xFd` (6.75, Accept) — iterative retraining stability theory; Neon is stronger (has theory + method + extensive experiments + SOTA results vs. theory + limited experiments).
- `WttfQGwpES` (6.67, Accept) — recursive stability theory; Neon is stronger (has empirical method, not just theory).
- `ShjMHfmPs0` (6.67, Accept) — the MAD paper Neon directly builds on; Neon is stronger (adds theory + method for improvement, not just characterization of collapse).
- `HXc5aXeoc8` (6.75, Accept) — diffusion sampling with momentum; different topic but similar quality tier; Neon has stronger theory.
- `OlzB6LnXcS` (8.00, Accept) — Shortcut Models; comparable. Both have novel methods, strong experiments, and some weaknesses. Shortcut Models has a cleaner, more focused contribution; Neon is more ambitious (4 architectures) with stronger theory. Similar overall quality.

**Final score: 7.5.** Neon is clearly above the 6.67–6.75 self-training analysis papers in both theoretical depth and empirical scope. It is comparable to Shortcut Models (8.00) in novelty and execution quality, but the evidential gap (no comparison to other synthetic-data improvement methods) and the theory-practice gap place it slightly below. The paper is a solid accept for ICLR.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>